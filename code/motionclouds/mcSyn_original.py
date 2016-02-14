import numpy as np
import scipy.io

import cv2

from reikna.cbrng import CBRNG
from reikna.cbrng.bijections import threefry
from reikna.cbrng.samplers import normal_bm
from reikna import cluda
from reikna.cluda import functions
from reikna.core import Type, Annotation, Parameter
from reikna.algorithms import PureParallel
from reikna.fft import FFT

def mul_array(carr_t1):
    return PureParallel(
            [Parameter('output', Annotation(carr_t1, 'o')),
            Parameter('input1', Annotation(carr_t1,'i')),
            Parameter('input1p', Annotation(carr_t1,'i')),
            Parameter('input2', Annotation(carr_t1,'i')),
            Parameter('input2p', Annotation(carr_t1,'i')),
            Parameter('input3', Annotation(carr_t1,'i')),
            Parameter('input3p', Annotation(carr_t1,'i'))],
            "${output.store_same}(${mul}(${input1.load_same}, ${input1p.load_same}) \
            +${mul}(${input2.load_same}, ${input2p.load_same})+${mul}(${input3.load_same}, ${input3p.load_same}));",
            render_kwds=dict(mul=functions.mul(carr_t1.dtype, carr_t1.dtype, out_dtype=carr_t1.dtype)))

def copy_array(carr_t1):
    return PureParallel(
            [Parameter('output', Annotation(carr_t1, 'o')),
            Parameter('input', Annotation(carr_t1,'i'))],
            "${output.store_same}(${input.load_same});")


def mcSyn(fileName = 'mc.mat', overSamp = 1, timeOffset = 2, N = 512, \
    framePerSecond=60, duration=5, varConst=35.0, octave=1, theta=0.0, thetaSpread=10, \
    fMode=30.0, fSpread=1.0, lifeTime=0.300):    

    dt=1.0/(overSamp*framePerSecond) 
    
    carr_t = Type(np.complex64, shape=(N,N))
    
    # Initialize random numbers generator
    bij=threefry(32,2)
    samp=normal_bm(bij, np.complex64, mean=0, std=1)
    rng=CBRNG(carr_t, 1, samp)
    
    # Initialize fft
    fft = FFT(carr_t) 
    
    recur = mul_array(rng.parameter.randoms)
    copy = copy_array(rng.parameter.randoms)
   
    PYOPENCL_COMPILER_OUTPUT=1
    api = cluda.ocl_api()
    thr = api.Thread.create(api)
    
    fftc = fft.compile(thr)
    
    counters = rng.create_counters()
    counters_dev = thr.to_device(counters)
    rngc = rng.compile(thr)
    
    recurc = recur.compile(thr)
    copyc = copy.compile(thr)
    
    # class for future library
    class options:
        def __init__(self, rho, srho, theta, stheta, sv):
            self.rho = rho
            self.srho = srho
            self.theta = theta
            self.stheta = stheta
            self.sv = sv
    if octave == 1:
        u = np.sqrt(np.exp((fSpread/np.sqrt(8)*np.sqrt(np.log(2)))**2)-1)
    elif octave == 0:
        u=np.roots([1,0,3,0, 3,0,1,0,-fSpread/fMode**2])
        u=u[np.where(np.isreal(u))]
        u=np.real(u[np.where(u>0)])
        u=u[0]

    
    options.rho=fMode*(1+u**2)
    options.srho=u
    options.theta=theta*np.pi/180
    options.stheta=thetaSpread*np.pi/180
    options.sv=1/(options.rho*lifeTime)
    
    if options.sv >(-2*np.sqrt(2)+4)/(N*dt):
        print('lifeTime=%f must be greater than %f, change lifeTime or the overSamp parameter. \n' %(lifeTime,((N*dt)/((-2*np.sqrt(2)+4)*options.rho))) )
    else:
        print('Correct parameters lifeTime = %f > %f. \n' % (lifeTime,((N*dt)/((-2*np.sqrt(2)+4)*options.rho))))
    
    Lx=np.concatenate((np.linspace(0,N/2-1,N/2),np.linspace(-N/2,-1,N/2)))
    x,y=np.meshgrid(Lx,Lx)
    R=np.sqrt(x**2+y**2)
    R[0,0]=10**(-6)
    Theta=np.arctan2(y,x)
    
    # CAR coefficients
    oneovertau=options.sv*R
    a=2*oneovertau
    b=oneovertau**2
    
    # AR coefficients
    al=np.complex64(2-dt*a-dt**2*b)
    be=np.complex64(-1+dt*a)
    
    # Spacial kernel
    angular=np.exp(np.cos(2*(Theta-options.theta))/options.stheta)
    radial=np.exp(-(np.log(R/options.rho)**2/np.log(1+options.srho**2))/2 )*(options.rho/R)
    K=angular*radial*(options.rho/R)**2*oneovertau
    K=K.astype(np.complex64)
    
    # Compute normalization constant
    C=dt**3*N**2/np.sum(K/(4*oneovertau**3))
    K=varConst*np.sqrt(C*K)
    
    # initialize value on device
    Z = np.zeros((N,N), dtype=np.complex64)
    
    TX = thr.to_device(Z)
    ITX = thr.to_device(Z)
    w_dev = thr.to_device(Z)
    A = thr.to_device(al)
    B = thr.to_device(be)
    C = thr.to_device(K)    
    F1 = thr.to_device(Z)
    F2 = thr.to_device(Z)

    i=0
    NframeOffset = timeOffset*framePerSecond
    Nframe = (timeOffset + duration)*framePerSecond
    I = np.zeros((N,N,Nframe-NframeOffset))
    
    while i<Nframe:
        
        for j in range(overSamp):
            # Noise                
            rngc(counters_dev, w_dev)
            
            # Recursion
            recurc(ITX, A, F1, B, F2, C, w_dev)
            
            # Update recursion
            copyc(F2, F1)
            copyc(F1, ITX)

        # ifft
        fftc(TX,ITX,0)
         
        # Save frame
        if i>NframeOffset-1:
            I[:,:,i-NframeOffset]=np.uint8(np.real(TX.get())/512.0 + 127)

        
        i+=1 
        
    if (fileName!=''):


        fileNameVid = fileName + '.avi'
        fileNameIm = fileName + '.png'
        
        cv2.imwrite(fileNameIm, I[:,:,0])

        fourcc = cv2.VideoWriter_fourcc('D','I','V','X')
        cv2.imwrite(fileNameIm, I[:,:,0])
        out = cv2.VideoWriter(fileNameVid, fourcc, framePerSecond, (N, N), False)
        
        if out.isOpened()==0:
            print('Codec problem')
        
        for i in range(I.shape[2]):
            out.write(np.uint8(I[:,:,i]))

        out.release()
                
    return I