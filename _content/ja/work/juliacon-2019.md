---
title: 'Recommendation.jl: Building Recommender Systems in Julia'
date: 2019-07-01
lastmod: '2021-10-16'
meta: Tech Conference
---

### JuliaCon 2019

<b>Recommendation.jl: Building Recommender Systems in Julia</b> @ <a href="https://juliacon.org/2019/"  target="_blank" rel="noopener">JuliaCon 2019</a>

### Abstract

This talk demonstrates [Recommendation.jl](https://github.com/takuti/Recommendation.jl), a Julia package for building recommender systems. We will eventually see (1) a brief overview of common recommendation techniques, (2) advantages and use cases of their Julia implementation, and (3) design principles behind the easy-to-use, extensible package.

### Description

[Recommendation.jl](https://github.com/takuti/Recommendation.jl) allows you to easily implement and experiment your recommender systems, by fully leveraging Julia's efficiency and applicability. This talk demonstrates the package as follows.

The speaker first gives a brief overview of theoretical background in the field of recommender systems, along with corresponding Recommendation.jl functionalities. The package supports a variety of well-know recommendation techniques, including k-nearest-neighbors and matrix factorization. Meanwhile, their dedicated evaluation metrics (e.g., recall, precision) and non-personalized baseline methods are available for your experiments.

Next, this talk discusses pros and cons of using Julia for recommendation. On the one hand, a number of algorithms fits well into Julia's capability of high-performance scientific computing in this field, but at the same time, it is challenging to make Julia-based recommenders production-grade at scale. The discussion ends up with future ideas of how to improve the package.

We will finally see the extensibility of the package with an example of building our own custom recommendation method. In practice, Recommendation.jl is designed to provide separated, flexible *data access layer*, *algorithm layer*, and *recommender layer* to the end users. Consequently, the users can quickly build and test their custom recommendation model with less efforts.

Reference: [Recommendation.jl: Building Recommender Systems in Julia](https://takuti.me/note/recommendation-julia/), an article written by the speaker.

### Slides

<script async class="speakerdeck-embed" data-id="7c5a8d8d54b44719b535f7e9b9764efc" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

### Video

<span class="iframe-container">
    <iframe src="https://www.youtube.com/embed/kC8LKQ_YjyM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</span>