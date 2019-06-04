---
title: How to Apply a Filter Defined in the Frequency Domain by a Continuous Function ?
image: /assets/img/blog/discrete-ipol.png
description: > 
   with T. Briand.
---
{% bibliography --cited --prefix post1 %}
<!--{% cite Briand2016how  --prefix post1 %}-->

Mathematical details of discretization in Fourier domain.

{% bibliography --cited --prefix post2 %}

## Abstract<!--{% cite Briand2016how  --prefix post2 %}-->

We propose algorithms for filtering real-valued images, when the filter is provided as a contin-uous function defined in the Nyquist frequency domain. This problem is ambiguous because images are discrete entities and there is no unique way to define the filtering. We provide a theoretical framework designed to analyse the classical and computationally efficient filtering implementations based on discrete Fourier transforms (DFT). In this framework, the filtering is interpreted as the convolution of a distribution, standing for the filter, with a trigonometric polynomial interpolator of the image. The various plausible interpolations and choices of the distribution lead to three equally licit algorithms which can be seen as method variants of the same standard filtering algorithm. In general none should be preferred to the others and the choice depends on the application. In practice, the method differences, which come from the boundary DFT coefficients, are not visible to the naked eye. We demonstrate that claim on several experimental configurations by varying the input image and the considered filter. In some cases however, we discuss how the choice of the variant may affect fundamental properties of the filtering. Source Code The source code and the online demo are accessible at the IPOL web part of this article 1. The C99 implementation of the code that we provide is the one which has been peer reviewed and accepted by IPOL. It contains two modules : one performs the standard filtering algorithm (Algorithm 1) presented in Section 3 and the other performs the comparison detailed in Section 4. The comparison module computes for nine filters the filtered images obtained by applying the three variant methods. For each filter a pairwise comparison of the results is done by computing the (absolute) difference image, the maximum difference and the mean difference. It creates fifty-five images: twenty-seven filtered images, twenty-seven difference images and the modulus of the DFT input in logarithmic scale. See Section 4 and the code documentation for additional information.


