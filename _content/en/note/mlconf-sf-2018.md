---
categories: [Conference, Machine Learning]
date: 2018-11-22
keywords: [scalable, conference, amazon, stream, single, session, program, industrial,
  efforts, paper]
lang: en
recommendations: [/note/hivemall-events-2018-autumn/, /note/umap-2019/, /note/td-to-amazon/]
title: 'Attending MLconf SF 2018 #mlconf18'
---

I have attended **[MLconf](https://mlconf.com/)** 2018 in San Francisco. Since awesome [speakers](https://mlconf.com/events/mlconf-sf-2018/) came from highly recognized industrial organizations, I can confidently say that MLconf can be a great place to see industrial trends and real-world "successful" use cases.

Surprisingly (and unsurprisingly), all of the following topics were covered in this one-day conference:

- **Interpretability**
    - Saliency map for images vs. [TCAV](https://arxiv.org/abs/1711.11279)
- Large-scale satellite image **data collection**
    - Make it available for [developers](https://developers.planet.com/)
- **Scalable ML** with [Amazon SageMaker](https://aws.amazon.com/sagemaker/)
    - Providing cheaper scalable solution on the cloud
    - Train local states (i.e., partial models) on multiple GPU-enabled instances in parallel in the streaming, incremental fashion, and finally merge them into single shared state
    - Reinventing k-means to make it scalable
- Uber's **NLP** efforts on building AI for riders and drivers
    - TF-IDF + LSA vs. CNN
- ML and deep learning **applications**
  - Geospatial processing
    - [Generative address](https://research.fb.com/publications/generative-street-addresses-from-satellite-imagery/) to get a better understanding of geographical characteristics from satellite images
  - Healthcare
    - Baidu's efforts on DL for pathology with [neural conditional random field](https://github.com/baidu-research/NCRF)
  - Fake news detector "[FakerFact](https://www.fakerfact.org/)"
- Practical lessons on **differential privacy**
- *and more!*

My favorite session was [Edo Liberty's one](https://mlconf.com/interview-with-edo-liberty-principal-scientist-at-aws-and-head-of-amazon-ai-labs-by-himani-agrawal/) about **Amazon SageMaker**:

https://twitter.com/takuti/status/1062869880892928000

I have a special feeling for Edo because my master's research was strongly motivated by his [paper](https://arxiv.org/abs/1206.0594); the paper eventually guided me to the world of scalable ML.

Hearing this session confirmed that I made the right decision by attending this year's MLconf. In fact, inside of SageMaker is still like a black box for me, but I can easily imagine that this out-of-the-box application is based on many advanced studies as Edo mentioned about approximation techniques for streaming data.

At the end of the event, the above tweet luckily won a free book:

https://twitter.com/MLconf/status/1062884267867291649

Thanks organizers, I got "[The Deep Learning Revolution](https://mitpress.mit.edu/books/deep-learning-revolution)"!

Overall, I really enjoyed this single-track, single-day conference thanks to the high-quality talks and well-organized program, as well as many networking opportunities. I personally believe ML, DL, and data science conferences should be more compact in terms of duration, number of sessions and attendees, just like MLconf, because the recent chaotic situation in those fields easily messes conference program; as an audience, too much input can sometimes be harmful to learning something truly valuable and important.