---
categories: [Recommender Systems, Data Science & Analytics, Machine Learning]
date: 2021-07-15
lang: en
title: Reviewing Ethical Challenges in Recommender Systems
lastmod: '2022-03-20'
keywords: [user, recommendation, ethical, systems, stakeholders, provider, recommendations,
  stakeholder, accuracy, authors]
recommendations: [/note/recsys-2021/, /note/recsys-2022/, /note/novelty-diversity-serendipity/]
---

As I captured in [Understanding Research Trends in Recommender Systems from Word Cloud](/note/recsys-wordcloud/), many real-life applications are nowadays applying recommendation techniques to a wide variety of datasets and scenarios.

However, their objective focuses too much on the accuracy of recommendations. That is, the major goal of many recommender systems is to accurately capture user preference and maximize the chance of positive user-item interactions, and hence consideration about surrounding non-performance-related problems is lacking. In that sense, I have to hesitantly say that [my past studies](/work/) are not an exception; over the past few years, I cared only about how to improve the accuracy of recommendations in a scalable manner.

By contrast, a survey paper "[Recommender systems and their ethical challenges](https://link.springer.com/article/10.1007/s00146-020-00950-y)" shows an important concept of **multi-stakeholder recommender systems** and argues how today's recommender research unintentionally helps to pose ethical challenges to the world. I believe having such an ethical perspective is one of the most important responsibilities for the developers of modern intelligent systems. Notice that, since we are engaging with the advanced systems literally on a second-by-second basis in our daily life e.g., on a mobile phone, e-commerce, social networks, and maps, it's critical for all of us to rethink the definition of good recommender systems.

With that in mind, let's see what the authors discussed in the paper and what I learned from them.

### Why multiple stakeholders matter

Conventionally, recommender systems are mainly studied in the context of business applications to improve the accuracy of user profiling and maximize the possibility of user engagement (e.g., click, purchase, rating). It means that the traditional recommenders care only about one type of stakeholder *"user"* *(receiver; consumer)*, and a model is optimized and evaluated by user-focused metrics such as recall and precision.

But there are other stakeholders in practice, including *recommendation provider*, *systems (administrators) themselves*, and *society*. Each stakeholder has different interests in the recommendation scenarios:

- *Provider* wants to minimize product inventory and maximize profitability;
- *Systems* need to ensure security, scalability, and flexibility without sacrificing user's satisfaction;
- *Society* has its desired condition that everyone establishes trustable, healthy mutual relationships.

Most importantly, since the recommendation results largely influence user's digital and physical behaviors, taking care of the ethical, security, and moral aspects of the system is critical. Here, the risks and rights are typically carried by the non-user stakeholders; we (as end-users) cannot do anything to mitigate the ethical challenges unless providers make special treatment and/or systems are specially designed to help us.

Therefore, balancing multiple stakeholders' interests is a crucial challenge in modern recommender systems.

### 6 ethical challenges in recommender systems

The authors investigated several academic papers discussing recommender systems from an ethical perspective, and they classified the problems into six key topics.

| Challenge | Problem statement | 
|:--:|:--|
|Inappropriate content|Users encounter unintended use of their data that leads to exposure to A/B testing and inaccurate recommendation results.|
|Privacy|Since recommender systems fully rely on user's behavioral data, the potential risk of leakage eventually enables external parties to obtain sensitive information.|
|Autonomy & personal identity|Algorithms largely change user's behavior and control their identity; our personality is biased by recommendation, and we become less autonomous as a result of day-to-day interaction with the systems.|
|Opacity|Knowing how the recommendations are generated encourages us to be more autonomous but may diminish the accuracy of recommendations at the same time. To overcome the situation, design methodology and evaluation techniques for explainable, transparent recommender systems are required.|
|Fairness|Every consumer must be able to receive the most relevant recommendation (C-fairness), whereas every provider should be capable to recommend their products to those who potentially show interest with a high likelihood (P-fairness). Developers need to identify the interests of different parties and design a system/algorithm to balance them without discrimination. |
|Social effects|Like fake news in Twitter/YouTube recommendations, consumers can easily be biased by the recommendation results, and public opinions are polarized as a consequence. Meanwhile, in the social networks, it is easy for small active groups to manipulate system outputs, and an opportunity of having public debates can be taken away.|

When we think about potential solutions to the challenges, the paper cautions that user-centered system design may not work in practice. 

For example, to eliminate a chance of encountering inappropriate content, systems could parametrize some factors and leave room for users to configure recommendation algorithms. Meanwhile, privacy concerns can be mitigated if the systems let users explicitly consent to the use of their data and control their privacy. 

However, both cases simply shift the responsibility for protecting rights to the end-users. Individuals can't understand the system and manage everything on their accountability. That's why considering multiple stakeholders is important; it's not a simple problem on one side (user vs. system/provider), and taking into account both objectives and balancing them is the only way to come up with a satisfactory solution.

### Bottom line

The challenges are mutually dependent, and we need to have a different mindset beyond user-focused accuracy metrics to holistically tackle the ethical problems both in theory and practice.

Speaking of recommendation metrics (i.e., objective functions to optimize recommenders), diversity and serendipity could play a particularly important role to minimize negative social effects. These metrics are opposed to biased/polarized outcomes, and recommenders could potentially be more "ethical" thanks to these viewpoints.

Last but not least, as the authors noted, interdisciplinary studies could bring the field of recommender systems to the next step in terms of its "goodness". Computer scientists do a great job to algorithmically make the systems more accurate and secure e.g., by using machine learning and cryptographic techniques, but other perspectives from social sciences are equally (and even more) valuable to satisfy the multiple stakeholders.

To learn further, a [Podcast episode](https://towardsdatascience.com/ethical-problems-with-recommender-systeems-398198b5a4d2) with Silvia Milano, the author of the paper I introduced in this post, is highly insightful.