---
categories: [Recommender Systems]
date: 2021-10-05
images: [/images/recsys-2021/2021.png]
lang: en
title: 'User-Centricity Matters: My Reading List from RecSys 2021'
keywords: [recsys, bias, papers, wordcloud, user, echo, recommendations, recommender,
  chamber, trends]
recommendations: [/note/recsys-2021-echo-chambers-and-filter-bubbles/, /note/recsys-wordcloud/,
  /note/ethical-challenges-in-recommender-systems/]
---
 
Conference season is here, and [RecSys](https://recsys.acm.org/) is back. I've been watching the evolution of recommender systems in the last few years, along with my physical attendances at RecSys [2016](/work/recprofile-2016/) and [2018](/work/recsys-2018/). It's great to see that the research community comes back to a physical conference unlike 2020.
 
After taking a quick look at the list of accepted papers, for me, one of the biggest trends in 2021 is **user-centricity**, which focuses on how to allow users to intervene in a recommendation process while minimizing the risk of biases and maximizing diversity & fairness of recommendations. In that sense, a list below highlights the papers that attract me the most:
 
- [An Audit of Misinformation Filter Bubbles on YouTube: Bubble Bursting and Recent Behavior Changes](https://dl.acm.org/doi/10.1145/3460231.3474241)
- [The Dual Echo Chamber: Modeling Social Media Polarization for Interventional Recommending](https://dl.acm.org/doi/10.1145/3460231.3474261)
- [I Want to Break Free! Recommending Friends from Outside the Echo Chamber](https://dl.acm.org/doi/10.1145/3460231.3474270)
- [Towards Unified Metrics for Accuracy and Diversity for Recommender Systems](https://dl.acm.org/doi/10.1145/3460231.3474234)
- [“Serving Each User”: Supporting Different Eating Goals Through a Multi-List Recommender Interface](https://dl.acm.org/doi/10.1145/3460231.3474232)
- [User Bias in Beyond-Accuracy Measurement of Recommendation Algorithms](https://dl.acm.org/doi/10.1145/3460231.3474244)
 
Of course, this observation is "biased" by my current personal interest*&mdash;[Ethical challenges in recommender systems](/note/ethical-challenges-in-recommender-systems/)&mdash;*but it's certainly an emerging area for the community as the conference has a dedicated session for "Echo Chambers and Filter Bubbles", "Users in Focus", and "Privacy, Fairness, Bias".
 
I started seeing such a tendency in the recent couple of years, and it's a good indication that the researchers are trying to go beyond the simple accuracy metrics. It reminds me a [podcast episode](https://dataskeptic.com/blog/episodes/2017/recommender-systems-live-from-farcon) that [Joseph Konstan](http://konstan.umn.edu/), one of the legendary professors in the field of recommender systems, emphasized how important defining the right metrics is. That is, quantifying the outcome of recommendation is a big challenge in this domain.
 
When I published "[Understanding Research Trends in Recommender Systems from Word Cloud](/note/recsys-wordcloud/)" in 2017, this type of trend wasn't clear enough, and the papers discussed mainly about "problem" (e.g., review, ranking, product, online) as opposed to "end users" or "eventual impact". But in 2020 and 2021, although many studies are still talking a lot about algorithms and accuracy improvements, the terms "bias", "metric", and "behavior", which complements the lack of foundational consideration and makes the recommenders more user-centered, have clearly arisen.
 
**2020**:
 
![recsys-2020-wordcloud](/images/recsys-2021/2020.png)
 
**2021**:
 
![recsys-2021-wordcloud](/images/recsys-2021/2021.png)
 
Notice that several papers are aggressively using the word "interaction" in the context of reinforcement learning. It basically enables users/developers to provide explicit feedback (even more explicit than rating feedback) so that humans can navigate a recommender to the right direction.
 
In other words, bi-directional interactions between humans and systems play an important role to bring the machine-generated recommendations to a higher level. I personally believe it's time to stop building a *selfish* intelligent system that naively aggregates and analyzes original data points with no care.
 
Last but not least, I'm looking forward to diving deep into the industrial challenges. As always, RecSys shows a unique balance between theory and practice both from academia and industry. They commonly pose insightful, motivating problem statements that give us an opportunity to rethink about how recommenders should be:
 
- [AIR: Personalized Product Recommender System for Nike's Digital Transformation](https://dl.acm.org/doi/10.1145/3460231.3474621)
- [Personalizing Peloton: Combining Rankers and Filters To Balance Engagement and Business Goals](https://dl.acm.org/doi/10.1145/3460231.3474610)
- [Recommendations and Results Organization in Netflix Search](https://dl.acm.org/doi/10.1145/3460231.3474602)
- [Recommender Systems for Personalized User Experience: Lessons learned at Booking.com](https://dl.acm.org/doi/10.1145/3460231.3474611)
- [RecSysOps: Best Practices for Operating a Large-Scale Recommender System](https://dl.acm.org/doi/10.1145/3460231.3474620)
 
Another interesting read would be "[Amazon at RecSys: Evaluation, bias, and algorithms](https://www.amazon.science/blog/amazon-at-recsys-evaluation-bias-and-algorithms)". As the professor highlighted the trends as "evaluation" and "bias" similarly to what I observed, the field finally started focusing more on the essential problems every recommender will can face.
