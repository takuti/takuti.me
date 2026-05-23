---
title: Streaming Recommendation Algorithms
date: 2014-01-01
lastmod: '2017-12-31'
meta: Research, Open Source, Personalization, Machine Learning
---

### Scope

Developed novel recommendation algorithms and a Python library to handle dynamic user-item interactions in real-time streaming scenarios, addressing the cold-start problem and enabling efficient online learning.

### Technology

- **Algorithms**: Factorization Machines, Sketching-based Online Learning, Relational Clustering
- **Implementation**: Python, NumPy, SciPy
- **Use Cases**: E-commerce recommendations, social networking, folksonomies

### Key Innovations

- **Incremental Factorization Machines**: Persistently handles cold-starting items in online recommendation scenarios
- **Dynamic Sketching**: Efficiently captures and adapts to changing user-item interactions in streaming data
- **FluRS Library**: Python library providing flexible, efficient streaming recommendation algorithms with dependency injection design pattern

### Publications & Presentations

- **EuroSciPy 2017**: FluRS: A Library for Streaming Recommendation Algorithms [[Video](https://www.youtube.com/watch?v=nARfsX63nDc)] [[Slides](https://speakerdeck.com/takuti/flurs-a-library-for-streaming-recommendation-algorithms)]
- **CHIIR 2017**: [Sketching Dynamic User-Item Interactions for Online Item Recommendation](http://dl.acm.org/citation.cfm?id=3022152) [[Paper](/docs/chiir-2017-paper.pdf)] [[Poster](/docs/chiir-2017-poster.pdf)]
- **RecProfile 2016**: [Incremental Factorization Machines for Persistently Cold-starting Online Item Recommendation](https://arxiv.org/abs/1607.02858) [[Paper](https://arxiv.org/pdf/1607.02858.pdf)] [[Slides](https://speakerdeck.com/takuti/incremental-factorization-machines)]
- **WIMS 2015**: [User Modeling in Folksonomies: Relational Clustering and Tag Weighting](http://dl.acm.org/citation.cfm?id=2797129) [[Paper](/docs/wims-2015-paper.pdf)] [[Slides](https://speakerdeck.com/takuti/user-modeling-in-folksonomies)] [[Code](https://github.com/takuti/wims-2015)]
    - *Not exactly a "streaming" recommender, but it was a foundational study surfacing the limitations of batch algorithms.*

### Learn More

- **Code**: [stream-recommender](https://github.com/takuti/stream-recommender) (Research implementations)
- **Library**: [FluRS](https://github.com/takuti/flurs) (Production-ready Python library)
- **Article**: [FluRS: A Python Library for Online Item Recommendation](https://takuti.me/note/flurs/)

<script async class="speakerdeck-embed" data-id="f8e9917ab2cf46dfaba1be61b6e449cd" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>
