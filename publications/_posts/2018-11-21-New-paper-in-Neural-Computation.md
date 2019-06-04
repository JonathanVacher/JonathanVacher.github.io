---
title: Bayesian modeling of motion perception using dynamical stochastic textures
image: /assets/img/blog/neco-2018.png
description: > 
   with A. I. Meso, L. Perrinet and G. Peyré.
---

{% bibliography --cited --prefix post1 %}

Reproduction of the Heeger-Bergen pyramid-based texture analysis/synthesis algorithm. Code in C and algorithmic details<!--{% cite Vacher2018bayesian  --prefix post1 %}-->. 

{% bibliography --cited --prefix post2 %}

## Abstract<!--{% cite Vacher2018bayesian  --prefix post2 %}-->

A common practice to account for psychophysical biases in vision is to frame them as consequences of a dynamic process relying on optimal inference with respect to a generative model. The present study details the complete formulation of such a gen-erative model intended to probe visual motion perception. It is first derived in a set of axiomatic steps constrained by biological plausibility. We then extend previous con-tributions by detailing three equivalent formulations of the Gaussian dynamic texture model. First, the composite dynamic textures are constructed by the random aggrega-tion of warped patterns, which can be viewed as 3D Gaussian fields. Second, these textures are cast as solutions to a stochastic partial differential equation (sPDE). This essential step enables real time, on-the-fly, texture synthesis using time-discretized auto-regressive processes. It also allows for the derivation of a local motion-energy model, which corresponds to the log-likelihood of the probability density. The log-likelihoods are finally essential for the construction of a Bayesian inference framework. We use the model to probe speed perception in humans psychophysically using zoom-like changes in stimulus spatial frequency content. The likelihood is contained within the genera-tive model and we chose a slow speed prior consistent with previous literature. We then validated the fitting process of the model using synthesized data. The human data replicates previous findings that relative perceived speed is positively biased by spatial frequency increments. The effect cannot be fully accounted for by previous models, but the current prior acting on the spatio-temporal likelihoods has proved necessary in accounting for the perceptual bias.


