---
categories: [Recommender Systems]
date: 2021-11-25
lang: en
draft: true
title: 'The Role of Recommender Systems to Overcome Echo Chambers and Filter Bubbles'
---
 
As I summarized in "[User-Centricity Matters: My Reading List from RecSys 2021](/note/recsys-2021/)", the field of recommender systems have clearly entered a new phase of research trend that focuses more on their downstream impact, and it is particularly interesting to see that RecSys 2021 had a dedicated session called *"Echo Chambers and Filter Bubbles":*
 
- [An Audit of Misinformation Filter Bubbles on YouTube: Bubble Bursting and Recent Behavior Changes](https://dl.acm.org/doi/10.1145/3460231.3474241)
- [The Dual Echo Chamber: Modeling Social Media Polarization for Interventional Recommending](https://dl.acm.org/doi/10.1145/3460231.3474261)
- [I Want to Break Free! Recommending Friends from Outside the Echo Chamber](https://dl.acm.org/doi/10.1145/3460231.3474270)
 
### Why echo chambers and filter bubbles matter
 
As a result of algorithmic recommendations, information a user will interact with can be easily biased (and even manipulated by a malicious service provider). Such a controlled, enclosed flow of information is known as ***filter bubbles***; the situation naturally decreases the diversity of data sources and eliminates a chance of knowing something new. Ultimately, the environment keeps amplifying user's existing opinion, and this phenomenon is what we call ***echo chamber*** effect.
 
Recently, the harm of computer algorithms that accelerate filter bubbles and echo chambers has been widely recognized in the context of conspiracy theory and extreme polarization in social networks. That is, people are overwhelmed by the massive volume of not only similar contents but also misinformation within that. For instance, the news about the Facebook whistleblower publicly shined a light on the guilt of service providers.
 
It is important to notice that, since the internet and physical world are completely blended nowadays, misinformation has a direct impact on our real life by changing critical behaviors/decisions of certain people. That's why the developers of recommendation algorithms must be serious about the problem, and an ethical aspect of intelligent systems needs to be treated at a top priority as we've seen in: "[Reviewing Ethical Challenges in Recommender Systems](/note/ethical-challenges-in-recommender-systems/)".
 
### Research outcomes from RecSys 2021
 
That said, it's not trivial for us to think of meaningful action items that contribute to mitigate filter bubbles and echo chambers. Let's see how the research community is tackling the crucial challenge in practice.
 
#### An Audit of Misinformation Filter Bubbles on YouTube: Bubble Bursting and Recent Behavior Changes
 
In this study, the authors assessed the possibility of "bursting the bubbles" when we interact with diverse perspectives after falling into the filter-bubble situation.
 
To be more precise, the researchers implemented bots that intentionally watch misinformation-related contents on YouTube (e.g., anti-vaccination, flat earth) first of all. Next, they let the bots watch something different and see if the dummy users can escape from the misinformation recommendations. Evaluation data is based on human annotation and [publicly available on GitHub](https://github.com/kinit-sk/yaudit-recsys-2021).
 
As a result, they found that, although it is certainly possible to avoid misinformation by the user's conscious choice of engaged contents, the difficulty of escaping from the bubbles varies depending on the type of misinformation. Meanwhile, the paper has reported they were not able to observe any positive consequence of [YouTube's aggressive content moderation strategy](https://www.youtube.com/howyoutubeworks/our-commitments/fighting-misinformation/) they are actively advertising lately.
 
Personally, it's very sad to see this type of research because the motivation implicitly assumes *"We cannot trust the companies"*. I don't want to believe this is the right approach to take; instead of forcing users to change their behaviors, I hope the service providers must learn from the outcomes and undergo a proper self-reflection process to redesign their recommenders. Of course, it'd be great if users could actively change their behavior to avoid misinformation, but those who actually suffered from misinformation are likely losing the ability of identifying which statement is true or not. This is the reason why spreading misinformation is highly concerning.
 
#### The Dual Echo Chamber: Modeling Social Media Polarization for Interventional Recommending
 
This paper states there are two different types of echo chambers in reality, *epistemic* and *ideological echo chambers*. The former is caused by a structured problem in social graphs that easily illustrate poor connections to opposite communities a user is not belonging to. Meanwhile, the latter is a result of the user's intentional avoidance of counter-arguments; they tend to shut out unseen information and not trust outsiders as they become part of the echo chamber effect.
 
By applying a graph embedding technique to Twitter knowledge graphs, they built a recommender that effectively takes into account all of user, community, and content (Tweet) factors, and the goal was to find out a promising way to mitigate both epistemic and ideological echo chambers. A major benefit of graph embedding is that we become able to define a user-community similarity based on a "relative" distance between a user and centroid of an opposite community. The distance measure enables us to identify "boundary users" who are in the middle of two different communities.
 
The simulation results on the recommender ultimately revealed that generating recommendations based on the boundary users is a promising recommendation diversification strategy, especially for the epistemic case. Diversity is obviously a key criterion of "good" recommendation, but it is not trivial how to diversify a list of recommendations. Here, their contribution is not only discussing deeply about echo chamber effects but showing a workable solution that leverages the widely-recognized graph embedding approach.
 
#### I Want to Break Free! Recommending Friends from Outside the Echo Chamber
 
This paper is similar to the previous one in a sense that both of them (1) used Twitter as a data source, (2) set an object to diversifying recommendation results, (3) used an embedding technique to represent user-content data. It makes sense as Twitter is one of few social networks that easily polarize public opinions by allowing users to actively share/hear comments literally on a second-by-second basis.
 
Meanwhile, this study focused purely on a friend recommendation task on Twitter and uniquely introduced a dedicated graph CNN-based solution that fully leverages intermediate representation of users' characteristics and word-level Tweet tendency. Furthermore, the authors invented an echo chamber-aware loss function based on user-user similarity and number of interactions. We can refer to the implementation in a [GitHub repository](https://github.com/tommantonela/frediech_recsys2021).
 
The experiments showed the proposed approach outperforms several well-known recommenders in terms of both relevance (Recall, Precision, NDCG) and diversity/novelty. Interestingly, a novelty metric particularly demonstrated a positive consequence as the model considers both community (interactions) and content tendency (words); that is, if two users are in the different communities but share the same tendency in contents (words in interested Tweets), the embedding approach is capable to improve novelty without sacrificing the relevance.
 
### Bottom line
 
The three papers presented in the *"Echo Chambers and Filter Bubbles"* session at RecSys 2021 clearly represented an industry trend in recommender ethics (i.e., caring end users and minimizing negative downstream impact).
 
When it comes to a solution, there is certainly a way to mitigate the problems and allow users to escape from a closed environment, but nothing is still outstanding as far as I can see. On the one hand, users can change their behavior to break down the biases, which might be infeasible due to a foundational problem that it's hard for humans to recognize/accept their own biases. On the other hand, a recommender system itself can be specially designed in an echo chamber-aware fashion. A right choice of metric and model is unknown though.
 
Despite all the current limitations, I hope this research area expands more as time goes by. Eventually, it'd be great if the big companies would more seriously consider the challenges and implement a REAL solution that goes beyond traditional success criteria e.g., profit/engagement maximization, accuracy improvement.
