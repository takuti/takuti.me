---
categories: [Recommender Systems]
date: 2021-11-24
lang: en
title: How Can Recommender Systems Contribute to Mitigate Echo Chambers and Filter
  Bubbles?
keywords: [echo, misinformation, chamber, bubbles, user, chambers, filter, graph,
  embedding, community]
recommendations: [/note/recsys-2021/, /note/the-power-of-diverse-thinking/, /note/recommender-diversity/]
---
 
As I summarized in "[User-Centricity Matters: My Reading List from RecSys 2021](/note/recsys-2021/)", the field of recommender systems has clearly entered a new phase of research trend that focuses more on their downstream impact, and it is particularly interesting to see that RecSys 2021 had a dedicated session called *Echo Chambers and Filter Bubbles* with three of the following papers:
 
- [An Audit of Misinformation Filter Bubbles on YouTube: Bubble Bursting and Recent Behavior Changes](https://dl.acm.org/doi/10.1145/3460231.3474241)
- [The Dual Echo Chamber: Modeling Social Media Polarization for Interventional Recommending](https://dl.acm.org/doi/10.1145/3460231.3474261)
- [I Want to Break Free! Recommending Friends from Outside the Echo Chamber](https://dl.acm.org/doi/10.1145/3460231.3474270)
 
### Why echo chambers and filter bubbles matter
 
As a result of algorithmic recommendations, information a user will interact with can be easily biased (and even manipulated by a malicious service provider). Such a controlled, enclosed flow of information is known as ***filter bubbles***; the situation naturally decreases the diversity of data sources and eliminates a chance of knowing something new as a consumer. Ultimately, the environment keeps amplifying user's existing opinion, and this phenomenon is what we call ***echo chamber*** effect.
 
Recently, the harm of computer algorithms that accelerate filter bubbles and echo chambers has been widely recognized in the context of conspiracy theory and extreme polarization in social networks. That is, the problem is not only about the overwhelming volume of contents but the density of misinformation within that. For instance, the [news about the Facebook whistleblower](https://www.npr.org/2021/10/05/1043377310/facebook-whistleblower-frances-haugen-congress) publicly criticized how lazy service providers are for this matter and reported their guilt.
 
It is important to notice that, since the internet and physical world are completely blended nowadays, **digital misinformation has a direct impact on our real life** by changing critical behaviors and decisions. That's why the developers of recommendation algorithms must be serious about the problem, and an **ethical aspect of intelligent systems needs to be treated at a top priority** as we've seen in: "[Reviewing Ethical Challenges in Recommender Systems](/note/ethical-challenges-in-recommender-systems/)".
 
### Research outcomes from RecSys 2021
 
That said, it's not trivial for us to think of meaningful action items that contribute to mitigate filter bubbles and echo chambers. Here, let's see how the research community is tackling the crucial challenge in practice. I will first highlight key takeaways, and more details follow.
 
#### An Audit of Misinformation Filter Bubbles on YouTube: Bubble Bursting and Recent Behavior Changes

- It is certainly possible to avoid misinformation by user's conscious choice of contents.
- But the difficulty of escaping from the bubbles varies depending on a category of misinformation.
- It's hard to observe any positive consequence of [YouTube's aggressive content moderation strategy](https://www.youtube.com/howyoutubeworks/our-commitments/fighting-misinformation/) they are actively advertising lately. 

In this study, the authors assessed the possibility of "bursting the bubbles" when we intentionally interact with diverse perspectives, even after falling into a filter-bubbling condition.
 
To be more precise, the researchers implemented a bot that watches misinformation-related contents on YouTube (e.g., anti-vaccination, flat earth) first of all. Next, they let the bot watch something different and see if the synthetic user can escape from the recommendations of misinformation. Evaluation data is based on human annotation, and it is [publicly available on GitHub](https://github.com/kinit-sk/yaudit-recsys-2021).
 
Personally, it's very sad to see this type of research because the motivation implicitly assumes *"We cannot trust the companies";* I don't want to believe this is the right approach to take. Instead of forcing users to change their behaviors, I hope the service providers must learn from the outcomes and undergo a proper self-reflection process to redesign their recommenders. Of course, it'd be great if users could actively change their behavior to avoid misinformation, but those who actually suffered from misinformation are likely losing the ability to identify which statement is true or not. This is the reason why spreading misinformation is highly concerning.
 
#### The Dual Echo Chamber: Modeling Social Media Polarization for Interventional Recommending

- There are two different types of echo chambers in reality, *epistemic* and *ideological echo chambers*.
- Echo chambers can be modeled as a graph, and an embedding technique helps us to optimize recommendation from the diversity perspective.
- Generating recommendations based on the "boundary users", who are in the middle of two different communities, is promising.

According to the paper, an epistemic echo chamber is caused by a structured problem in social graphs that easily illustrate poor connections to opposite communities a user is not belonging to. Meanwhile, the ideological one is a result of user's intentional avoidance of counter-arguments; they tend to shut out new information and not trust outsiders as they become part of the echo chamber effect.
 
By applying a graph embedding technique to Twitter knowledge graphs, the authors built a recommender that effectively takes into account user, community, and content (Tweet) factors. An ultimate goal was to find out a promising way to algorithmically mitigate both epistemic and ideological echo chambers. A major benefit of graph embedding is that we become able to define user-community similarities based on a "relative" distance between a user and centroid of an opposite community. 

The embedded graph representation enables us to easily identify boundary users, and their simulation results revealed that a proposed algorithm particularly works well for the epistemic case by diversifying recommendations. Diversity is obviously a key criterion of "good recommendation", but it is not trivial how to diversify a list of recommendations in practice. Here, their contribution is not only discussing deeply about echo chamber effects but showing a workable solution that leverages the widely studied graph embedding approach.
 
#### I Want to Break Free! Recommending Friends from Outside the Echo Chamber

- Recommending friends from a different (but still similar enough) community helps effectively diversifying the user's perspective.
- To choose the right recommended user from a complex network, taking into account both community structure and their content consumption pattern is important.
- If we could design the right model and metric, it is certainly possible to optimize relevance (accuracy) and novelty (diversity) simultaneously.

Similarly to the previous one, this paper (1) used Twitter as a data source, (2) set an object to diversifying recommendation results, (3) used an embedding technique to represent user-content data. It makes sense as Twitter is one of few social networks that easily polarize public opinions by allowing users to actively share/hear comments literally on a second-by-second basis.
 
Meanwhile, this study focused purely on a friend recommendation task on Twitter and uniquely introduced a dedicated graph convolutional neural network-based solution, which fully leverages intermediate representation of user's characteristics and word-level Tweet tendency. Furthermore, the authors invented an echo chamber-aware loss function based on user-user similarity and number of interactions among them. We can refer to the implementation in a [GitHub repository](https://github.com/tommantonela/frediech_recsys2021).
 
The experiments showed the proposed approach outperforms several well-known recommenders in terms of both relevance (Recall, Precision, NDCG) and diversity/novelty. Interestingly, their novelty metric demonstrated a positive consequence because their model considers both community (interactions) and content tendency (words); that is, if two users are in the different communities but share the same tendency in contents (i.e., words in Tweets they posted and/or showed interests), the embedding approach is capable to improve novelty without sacrificing the relevance.
 
### Bottom line
 
The three papers presented in the *Echo Chambers and Filter Bubbles* session at RecSys 2021 clearly represented an industry trend in the recommender ethics (i.e., caring more about end users and minimizing negative downstream impact).
 
When it comes to a solution, there is certainly a way to mitigate the problems and allow users to escape from a closed environment, but nothing is still outstanding as far as I can see. On the one hand, users can change their behavior to break down the biases, which might be infeasible due to a foundational problem that it's hard for humans to recognize/accept their own biases. On the other hand, a recommender system itself can be specially designed in an echo chamber-aware fashion. A right choice of model, metric, and its optimization scheme is unknown though.
 
Despite all the current limitations, I hope this research area expands more as time goes by. Eventually, it'd be great if the big companies would more seriously consider the challenges and implement a REAL solution that goes beyond traditional success criteria such as profit/engagement maximization and accuracy improvement.
