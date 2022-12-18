---
categories: [Recommender Systems]
date: 2022-10-14
lang: en
title: Ethics in Recommendation Pipeline—A First Look at RecSys 2022 Papers
images: [/images/recsys-2022/wordcloud.png]
keywords: [recommendation, recommender, evaluation, recsys, metrics, privacy, recpack,
  papers, design, industry]
recommendations: [/note/recsys-2021/, /note/cross-validation-julia-recommender/, /note/ethical-challenges-in-recommender-systems/]
---

[RecSys 2022](https://recsys.acm.org/recsys22/), the 2022 edition of a top academic conference in the field of recommender systems, happened last month in Seattle. Even though I didn't attend the event like the [last couple of years](/note/recsys-2021/), it's still fun to check out the papers and see how the research trends, as well as the industry's focuses, are shifting.

![wordcloud](/images/recsys-2022/wordcloud.png)

At a glance, while many studies continuously try to fulfill the gap between theory and practice by applying state-of-the-art neural network-based techniques to their own problem spaces (e.g., news, music), more research also started casting "deeper" problem statements that cannot be easily addressed by the conventional optimization problems: privacy, fairness, and offline evaluation vs. online performance. In fact, these topics are not new, and we've seen the presence of relevant work over the last few years as [I summarized the 2021 trend as **user-centricity**](/note/recsys-2021/). However, I feel the number of papers incorporating these perspectives into a key message has increased at a steady pace.

In my view, such a trend surfaces an underlying challenge about [ethics in recommender systems](/note/ethical-challenges-in-recommender-systems/). As Big Tech popularized the power of personalization in their services, we see not only the benefits of these capabilities but a flip side of them such as privacy threats, polarization, and [loss of autonomy](/note/autonomy-vs-algorithmic-recommendation/) at large. To address these concerns, developers need to make conscious design choices at every step of recommender system development, ranging across UI/UX design, data collection, model training, evaluation, deployment, and monitoring.

With that in mind, here is my reading list from the proceeding of RecSys 2022:

- [Countering Popularity Bias by Regularizing Score Differences](https://dl.acm.org/doi/10.1145/3523227.3546757)
- [EANA: Reducing Privacy Risk on Large-scale Recommendation Models](https://dl.acm.org/doi/10.1145/3523227.3546769)
- [Towards Fair Federated Recommendation Learning: Characterizing the Inter-Dependence of System and Data Heterogeneity](https://dl.acm.org/doi/10.1145/3523227.3546759)
- [Measuring Commonality in Recommendation of Cultural Content: Recommender Systems to Enhance Cultural Citizenship](https://dl.acm.org/doi/10.1145/3523227.3551476)
- [Recommender Systems and Algorithmic Hate](https://dl.acm.org/doi/10.1145/3523227.3551480)

Unlike the previous years, where the fairness aspects were primarily associated with the evaluation phase in the form of metrics, we can see further consideration about how to incorporate fairness "by design" at the pre-/post-evaluation phases of a recommendation pipeline.

Speaking of recommender pipeline, this year's best demo paper, *[RecPack: An(other) Experimentation Toolkit for Top-N Recommendation using Implicit Feedback Data](https://dl.acm.org/doi/10.1145/3523227.3551472),* was a good read. The authors nicely extracted common patterns every recommender will equally require, and they strongly highlighted how crucial improving the reusability of recommender implementation is [to fulfill the offline evaluation vs. online performance gap]. A [recent podcast episode of Recsperts](https://www.recsperts.com/episodes/9-recpack-and-modularized-personalization-by-froomle-with-lien-michiels-and-robin-verachtert) invited the authors and had insightful conversations about the package and motivation.

<iframe allow="autoplay *; encrypted-media *; fullscreen *; clipboard-write" frameborder="0" height="175" style="width:100%;max-width:660px;overflow:hidden;background:transparent;" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-top-navigation-by-user-activation" src="https://embed.podcasts.apple.com/us/podcast/9-recpack-and-modularized-personalization-by-froomle/id1587222271?i=1000579601557"></iframe>

My immediate question after reading the paper was *Where do the non-accuracy metrics fit into RecPack's evaluation module?* and it was answered in the podcast. They mentioned the difficulty in standardizing the interfaces of these metrics when it comes to modularization, and I share the sense based on my experience of [creating a recommender package in Julia](/note/juliacon-2022/) and implementing diversity & serendipity metrics in it. I think we need a good "design pattern" of recommender systems outside of the machine learning domain; replicating scikit-learn's `fit` interface isn't enough to make recommender implementation widely (re)usable because recommendation is not always the same as machine learning in many cases.

Since 2021-2022 was a special period for me [working closely with real-world recommenders at Amazon's industry-leading personalization team](/note/becoming-a-freelancer-in-canada/), I realized that how I read the list of accepted papers changed a lot in a meaningful way. One interesting observation is that I've become less curious about the industry talks. Maybe I read too much into it, but, although they are talking about different products with cool technologies and algorithms, I see the objectives are still very much flattened and boring&mdash;Maximizing user engagement and downstream profit. Hopefully, the reality of the industry's recommender development is (will be) the same as much as the research trend indicates. Ultimately, I'd like to take the situation more seriously and turn the concerns into actions whenever I interact with recommender systems both as a user and developer.
