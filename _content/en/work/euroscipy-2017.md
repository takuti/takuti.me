---
title: "FluRS: A Library for Streaming Recommendation Algorithms"
date: 2017-08-01
meta: EuroSciPy 2017
---

<b><a href="https://www.euroscipy.org/2017/descriptions/19827.html" target="_blank" rel="noopener">FluRS: A Library for Streaming Recommendation Algorithms</a></b> @ <a href="https://www.euroscipy.org/2017/"  target="_blank" rel="noopener">EuroSciPy 2017</a>

- <a href="https://github.com/takuti/flurs/tree/0.0.2" target="_blank" rel="noopener">Code</a>

### Abstract

This talk demonstrates FluRS, a library for efficient and flexible recommendation algorithms, based on the speaker’s past experience in academia and industry. Eventually, the speaker guides you to the world of an emerging trend, “streaming” recommender systems, in terms of both theory and practice.

### Description

#### Overview

**[FluRS](https://github.com/takuti/flurs)** is a Python library for streaming recommendation algorithms which enables you to efficiently and flexibly build a recommendation model from complex user-item data. By focusing around the library, this talk discusses each aspect of **past**, **present** and **future** as follows:

- **Past**: Challenges in classical recommendation engines (with their Python implementation),
- **Present**: How the speaker designed and implemented new kinds of recommendation algorithms as the Python library,
- **Future**: The feasibility of fast, real-time recommendation at scale with or without FluRS.

Note that, in order to learn the basic concept underlying the FluRS library, you can refer to the following article: [FluRS: A Python Library for Online Item Recommendation](https://takuti.me/note/flurs/). In short, implementation of FluRS takes advantage of the dependency injection technique, and developers do not need to worry much about recommender-specific code which commonly appears regardless of algorithm.

#### Target

This talk is designed for people who have fundamental knowledge of machine learning (e.g., [matrix computations](https://en.wikipedia.org/wiki/Matrix_(mathematics)), [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent), [cross validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics))) and Python coding with the NumPy & SciPy libraries; that is, audience does not have to be a professional machine learning researcher or Python developer. In particular, since the speaker explains the field of recommender systems from basics, people can enjoy without previous knowledge of recommendation techniques.

Eventually, the speaker expects audiences to become able to teach their friends the basic of recommender systems and implement recommendation algorithms by themselves.

#### Background

Recommendations nowadays play an important role in real-world applications such as e-commerce and social networking services in order to improve customers' satisfaction, but the widely-developed systems pose a crucial challenge which cannot be properly handled by the classical techniques. More concretely, even though users' interests and item properties change dynamically over time on modern systems, there is a lack of effective ways and empirical studies to catch up with the dynamic data.

In that context, throughout his master's program and experience in the industry, the speaker fully realized how building real-world recommender systems is difficult over the past years. Thus, he ultimately invented two novel recommendation techniques to tackle the challenging scenario, and published corresponding research papers:

- **Incremental Factorization Machines for Persistently Cold-starting Online Item Recommendation** \[[Paper](https://arxiv.org/abs/1607.02858)\] \[[Slides](https://speakerdeck.com/takuti/incremental-factorization-machines)\] \[[GitHub](https://github.com/takuti/stream-recommender/tree/v0.3.1-recprofile-2016)\]
- **Sketching Dynamic User-Item Interactions for Online Item Recommendation** \[[Paper](http://dl.acm.org/citation.cfm?id=3022152)\] \[[Poster](https://takuti.me/docs/chiir-2017-poster.pdf)\] \[[GitHub](https://github.com/takuti/stream-recommender/tree/v0.5.0-chiir-2017-and-thesis)\]

Notice that, as the GitHub links suggest, these inventions have been achieved along with the development of FluRS. So, one of the main topics of this talk is to dig deep into the experience.

For the reasons mentioned above, FluRS is a "package" of things what the speaker has experienced in both academia and industry, and hence he decided to give a talk on the library from a practical point of view.

*Note: All contents are based on the speaker's own thought, and they do not reflect the view of any of his previous and current affiliations.*

### Slides

<script async class="speakerdeck-embed" data-id="f8e9917ab2cf46dfaba1be61b6e449cd" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>

### Video

<span class="iframe-container">
    <iframe src="https://www.youtube.com/embed/nARfsX63nDc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</span>
