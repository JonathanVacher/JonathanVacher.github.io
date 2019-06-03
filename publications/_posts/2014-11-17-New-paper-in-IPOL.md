---
title: The Heeger & Bergen Pyramid Based Texture Synthesis Algorithm 
image: /assets/img/blog/hb-tex.png
description: > 
   with T. Briand, B. Galerne and J. Rabin.
---

{% bibliography --cited --prefix post1 %}
<!--{% cite Briand2014heeger  --prefix post1 %}-->

Reproduction of the Heeger-Bergen pyramid-based texture analysis/synthesis algorithm. Code in C and algorithmic details.

{% bibliography --cited --prefix post2 %}

## Abstract<!--{% cite Briand2014heeger  --prefix post2 %}-->

This contribution deals with the Heeger-Bergen pyramid-based texture analysis/synthesis algorithm. It brings a detailed explanation of the original algorithm tested on many characteristic examples. Our analysis reproduces the original results, but also brings a minor improvement concerning non-periodic textures. Inspired by visual perception theories, Heeger and Bergen proposed to characterize a texture by its first-order statistics of both its color and its responses to multiscale and multi-orientation filters, namely the steerable pyramid. The Heeger-Bergen algorithm consists in the following procedure: starting from a white noise image, histogram matchings are performed to the image alternately in the image domain and the steerable pyramid domain, so that the corresponding output histograms match the ones of the input texture.


