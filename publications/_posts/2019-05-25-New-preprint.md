---
title: Combining mixture models with linear mixing updates&#58; multilayer image segmentation and synthesis
image: /assets/img/blog/combining.png
description: > 
   with R. Coen-Cagli.
---

{% bibliography --cited --prefix post1 %}

We propose a flexible framework for mixture models. We apply this framework to natural image segmentation using deepnet features at all layers. We show that these mixture models can achieve state-of-the-art boundary scores.<!--{% cite vacher2019combining  --prefix post1 %}-->. 

{% bibliography --cited --prefix post2 %}

## Abstract<!--{% cite vacher2019combining  --prefix post2 %}-->

Finite mixture models for clustering can often be improved by adding a regularization that is specific to the topology of the data. For instance, mixtures are common in unsupervised image segmentation, and typically rely on averaging the posterior mixing probabilities of spatially adjacent data points (i.e. smoothing). However, this approach has had limited success with natural images. Here we make three contributions. First, we show that a Dirichlet prior with an appropriate choice of parameters allows – using the Expectation-Maximization approach – to define any linear update rule for the mixing probabilities, including many smoothing regularizations as special cases. Second, we demonstrate how to use this flexible design of the update rule to propagate segmentation information across layers of a deep network, and to train mixtures jointly across layers. Third, we compare the standard Gaussian mixture and the Student-t mixture, which is known to better capture the statistics of low-level visual features. We show that our models achieve competitive performance in natural image segmentation, with the Student-t mixtures reaching state-of-the art on boundaries scores. We also demonstrate how to exploit the resulting multilayer probabilistic generative model to synthesize naturalistic images beyond uniform textures.


