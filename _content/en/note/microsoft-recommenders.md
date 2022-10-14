---
categories: [Recommender Systems, Data Science & Analytics, Machine Learning]
date: 2022-05-07
lang: en
images: []
title: What I Like About Microsoft Recommenders Repository
lastmod: '2022-09-02'
keywords: [recommenders, microsoft, repository, pypi, package, minimal, metrics, functionality,
  written, diversity]
recommendations: [/note/travis-gh-pages-deployment/, /note/flurs/, /note/recommender-diversity/]
---

I recently found [Microsoft's Recommenders repository](https://github.com/microsoft/recommenders) is particularly useful to understand common discussion points when it comes to recommender systems. The motivation and brief history of the repository can be found in their paper "[Microsoft Recommenders: Tools to Accelerate Developing Recommender Systems](https://arxiv.org/abs/2008.13528)," which were demonstrated at [RecSys 2019](https://dl.acm.org/doi/10.1145/3298689.3346967) and [WWW 2020](https://dl.acm.org/doi/abs/10.1145/3366424.3382692).

What I like about the repository can be three fold:

- High-quality, well-written Jupyter notebooks
- Minimal functionality on its PyPI package
- Consideration about non-accuracy metrics

***High-quality, well-written Jupyter notebooks.*** Even though the repository contains an [installable PyPI package `recommenders`](https://pypi.org/project/recommenders/) (!), the most important part is a [collection of well-written Jupyter notebooks](https://github.com/microsoft/recommenders/tree/463fb3ee943c5635502a7c0b8f5b24fe3223b74e/examples) that enable us to understand how to build recommender systems from data preparation and model training to evaluation and deployment.

![microsoft-recommenders-pipeline](/images/microsoft-recommenders/microsoft-recommenders-pipeline.png)
_Source: [recommenders/examples at main · microsoft/recommenders · GitHub](https://github.com/microsoft/recommenders/tree/463fb3ee943c5635502a7c0b8f5b24fe3223b74e/examples)_

Importantly, the notebooks are not just for a series of code snippets + inline comments (like most of the repositories do) but for providing detailed texts/references so we can use the contents as "tutorial." Moreover, as mentioned in the paper, [integration tests](https://github.com/microsoft/recommenders/tree/08a9eba1b50640a13af109c8e35ae382669c049b/tests/integration/examples) use [`papermill`](https://papermill.readthedocs.io/) for validating the notebooks.

***Minimal functionality on its PyPI package.*** Basically, the `recommenders` package itself is a set of utility functions that are widely applicable to a variety of scenarios, which makes the repository surprisingly minimal and useful; to avoid reinventing the wheel, the implementation of recommendation algorithms largely relies on the other packages such as [PySpark](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.recommendation.ALS.html) and [Surprise](http://surpriselib.com/), while some minor ones are implemented from scratch (e.g., [Restricted  Boltzmann Machine](https://github.com/microsoft/recommenders/blob/d4181cf1d1df6e71f7e6b202b0875bb3bd54150c/recommenders/models/rbm/rbm.py#L14)).

***Consideration about non-accuracy metrics.*** When we evaluate recommender systems, I cannot emphasize the importance of non-accuracy metrics enough as I wrote in [Recommender Diversity is NOT Inversion of Similarity](/note/recommender-diversity/). The Recommenders repository is doing a great job in this regard since there is a [dedicated notebook for explaining coverage, novelty, diversity, and serendipity metrics](https://github.com/microsoft/recommenders/blob/0d2385681b2320f98d5ff0e448f505146b69df99/examples/03_evaluate/als_movielens_diversity_metrics.ipynb). I hope the package and repository evolve more around these topics moving forward.

Overall, I have an impression that Microsoft Recommenders nicely summarizes a good chunk of techniques every recommendation problems are commonly interested in; if there is someone who is completely new to recommender systems but familiar with Python-based data science & machine learning ecosystem, I'd first recommend to take a look at this repository. One potential area of improvement I can think of is around [operationalizing recommenders](https://github.com/microsoft/recommenders/tree/1178adb9a111d03e7dbcab7a453490d3cc884b99/examples/05_operationalize). Currently, the examples are highly optimized for Azure-based deployment, which makes sense as the repository is owned by Microsoft, but it would be great if they could generalize the insights in a more OSS way.
