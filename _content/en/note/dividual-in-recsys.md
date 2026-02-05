---
categories: [Data & Algorithms, Recommender Systems, Society & Business]
series: [data]
date: 2022-11-27
lang: en
title: 'Fluid People and Blended Society: How Systems Model "Dividuals"'
keywords: [user, data, users, systems, dividual, multiple, group, model, identities,
  ing]
recommendations: [/note/ethical-challenges-in-recommender-systems/, /note/data-feminism/,
  /note/coursera-data-science-ethics/]
---

*"Let $\mathcal{U}$ be a set of users ..."*

User modeling research often begins by stating a set of individuals to formulate. But, since our world is highly contextualized as [economics and complexity science have revealed](/note/why-information-grows/), representing a user as an element of a logical set may be an oversimplification. Here, the fluidity of user behavior explains the importance and potential risks of recent trends in personalization systems research, such as context-aware, group, multi-stakeholder, and/or serendipitous/diversified recommenders.

### There is no such a thing as an "individual"

Most importantly, a single user can take multiple different states. The term *individual* means *indivisible*, meaning a single person is the smallest unit in human society. However, in reality, each of us consists of multiple identities, and hence the unit is actually *divisible* into smaller chunks, resulting in what anthropologists call *[dividual](https://en.wikiversity.org/wiki/Social_Relations_as_Persons)*.

The concept of dividual represents the contextualized nature of our behaviors. For example, I can be divided into multiple units depending on a situation, and I behave differently for each:

- Location: I'm traveling in Europe vs. Asia.
- Language: I speak in English vs. Japanese.
- Group: I'm working for company X vs. Y.
- Occupation: I serve an engineering role vs. a business role.
- Shared identity: I talk with a friend A vs. B vs. family member.

Consequently, two friends may have completely distinct impressions about my character, or I might easily make a contradicting statement to the one I made on a different occasion.

So, which one of them is the true version of myself? If I see myself as a dividual, the answer is that all of them are in fact true parts of myself. That is, since each person has their limitation to the amount of knowledge and knowhow to hold, *personbytes*, we are naturally distributing the capacity to multiple states for efficiency and effectiveness.

Therefore, the mathematical formulation of a user is oversimplified when they are considered as a static element $u \in \mathcal{U}$.

### How systems capture the multifaceted nature

Given the extended understanding of individuals, we can summarize that the [trends of user modeling research, recommender systems in particular, over the last few years](/note/recsys-wordcloud/) are collectively capturing users' multifaceted character.

First, feature-based, location/context-aware recommender systems enable the systems to better understand what kind of circumstances a user is surrounded by at a particular point. To be more precise, unlike traditional user modeling techniques such as collaborative filtering, practitioners have enriched the input data (user vectors) with as much auxiliary information as available. As a consequence, a resulting model becomes more sensitive to subtle changes in the context users are in i.e., which dimension of dividual is currently activated for a particular user, and such systems are more robust, which means that there is less chance to suppress users' unique identities.

Secondly, our identity is largely influenced by interactions with others. Thus, multi-stakeholder or group recommenders that comprehensively deal with such surrounding factors play a crucial role, even if the ultimate goal is to make a prediction for a single user. To give an example, my purchase behavior can ultimately be determined by the interests in greater society (e.g., environmental impact) regardless of the "average" behavior of those who are in the same gender & age group. Or, a common goal of an organization I'm belonging to may directly intervene in my decision-making process, and I won't have enough control over the choices. Meanwhile, the service providers do not always value users' interests the most because they cannot survive without making revenue; as a user, we need to consider and be conscious about our choice. In any case, a data-driven application is a place where multiple parties get together with different (and often conflicting) interests.

Besides the continuous evolution of deep neural network-based personalization systems, there has been a lot of discussion about how to enrich and diversify input data to data-driven applications. A naive understanding of this trend is that more data points allow the systems to be more accurate, and providers become more profitable thanks to users' higher engagement. However, when we look at the situation through the lens of social science, it means a lot more than accuracy maximization as [Dr. Silvia Milano connected the discussions to ethical challenges](/note/ethical-challenges-in-recommender-systems/).

### Information, technology, data. By whom, and for whom?

In summary, it's natural for each of us to have different versions of ourselves, and hence it would be oversimplification if data-driven applications assume users are indivisible. Rather, the systems need to take multiple dimensions of users and surrounding situations into account so that they don't overlook underlying ethical implications.

Furthermore, our identities can change over time for many reasons. Thus, it's important to think of time factors when it comes to user modeling. For instance, my day-to-day small choices accumulate and will eventually shape my future identity, like 10 years later. A person's life itself contains a lot of biases brought by external and internal factors both in visible and invisible ways, and that is the beauty of our life. Here, although it sounds contradicting to the high-efficiency data-driven approaches unlock, acknowledging the complexity of human society seems to be a foundational challenge today's field data scientists are facing.

Ultimately, even though user modeling is all about the abstraction of our complex real world, how much raw inputs they preserve/lose is determined by a choice of algorithm, and such a decision is made by humans. In that sense, I, as a practitioner, am trying to intentionally see and contribute to an intersection of data and social science. Human life tends to be biased, but it doesn't mean data science applications can take it as-is and amplify the biases; if the applications made racial predictions, it's a matter of humans who collected, analyzed, and simplified the data by naive aggregation.
