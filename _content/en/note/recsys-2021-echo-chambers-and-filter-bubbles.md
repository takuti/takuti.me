---
categories: [Recommender Systems]
date: 2021-11-25
lang: en
draft: true
title: 'The Role of Recommender Systems to Overcome Echo Chambers and Filter Bubbles'
---

As I summarized in "[User-Centricity Matters: My Reading List from RecSys 2021](/note/recsys-2021/)", the field of recommender systems have clearly entered a new phase of research trend by focusing more on their downstream impact, and it is particularly interesting to see that RecSys 2021 had a dedicated session for "Echo Chambers and Filter Bubbles":

- [An Audit of Misinformation Filter Bubbles on YouTube: Bubble Bursting and Recent Behavior Changes](https://dl.acm.org/doi/10.1145/3460231.3474241)
- [The Dual Echo Chamber: Modeling Social Media Polarization for Interventional Recommending](https://dl.acm.org/doi/10.1145/3460231.3474261)
- [I Want to Break Free! Recommending Friends from Outside the Echo Chamber](https://dl.acm.org/doi/10.1145/3460231.3474270)

### Why echo chambers and filter bubbles matter

As a result of algorithmic recommendations, the information a user will interact with can be easily biased (and even manipulated by a malicious service provider). Such a controlled, enclosed flow of information is known as ***filter bubbles***; the situation naturally decreases the diversity of information sources and eliminates a chance of knowing something new. Ultimately, the environment keeps amplifying user's existing opinion, and this phenomenon is what we call ***echo chamber effect***.

Recently, the harm of computer algorithms accelerating filter bubbles and echo chambers has been widely recognized in the context of conspiracy theory and polarization in social networks. That is, people are overwhelmed by not only the massive volume of similar contents but also the substantial amount of misinformation within that. That's why the developers of recommendation algorithms must seriously think about the problem, and ethical aspect of intelligent systems is considered at a high priority.

Since the news about Facebook whistleblower publicly shed a light on the guilty of service providers, there is no option to ignore the problems.

### Paper overview

#### An Audit of Misinformation Filter Bubbles on YouTube: Bubble Bursting and Recent Behavior Changes

- Social network 
- The authors implemented bot(s) that intentionally watch misinformation-related videos on YouTube e.g., anti-vaccination, flat earth. Then, they let the bots watch something different and see the users can escape from the misinformation recommendations.
- Human annotation. Data is available online: https://github.com/kinit-sk/yaudit-recsys-2021
- They found that although it's certainly possible to avoid misinformation by user's effort, the difficulty varies depending on the type of misinformation.
- They didn't see any positive impact as a result of service provider's effort on adjusting content moderation logic.
- It's very sad to see this type of research as the motivation implicitly assumes "We cannot trust the companies".
- Of course, users could change their behavior to avoid misinformation, but they are usually not realizing that they actually suffered from misinformation.
- Instead of forcing users to stand up, the service providers must learn from the study and undergo a proper self-reflection process to design their recommenders.

#### The Dual Echo Chamber: Modeling Social Media Polarization for Interventional Recommending

- 2 echo chambers: 
    - Epistemic - structured information gap (social graph), no connection w/ opposite community
    - ideological - intentionally avoid counter opinions., shut out, do not trust outsiders
- How to mitigate an issue? - Twitter knowledge graph -> identify graph -> embedding in the single space (user, community, content), build a recommender, simulate accept/reject of recommender based on epistemic/ideological case
- Relative distance between a user and centroid of opposite community
- Which rec result works effectively to let users accept the recs?
- Epistemic was relatively easier to mitigate. Both cases, recommending based on "boundary users" would work effectively
- "Is diversifying the recommendations really helpful?"

#### I Want to Break Free! Recommending Friends from Outside the Echo Chamber

- MOdeling preference, recommending preferred -> simply causes a bias
- echo chamber-aware friend recommendation approach - diversifying social connections
- Target: Twitter
- Consider embedding each of word (tweets) and user aspect
- Train Graph Conv NN based on the vectors, while taking into account of intermediate representation of target (characterostocs) and recommendees' content they shared
- Design an echo chamber-aware loss function based on user-user similarity and # of interactions.
- Achieve satisfactory results both on relevance (recall, precision, ndcg) and diversity and novelty metric, compared to several recommendation techniques.
- Novelty optimization works successfuly as the model considers both community (interactions) and content tendency (words); in other content but still same content tendency -> improve novelty while maintaining relevance
- Repo: https://github.com/tommantonela/frediech_recsys2021

### Bottom line

- Foo 