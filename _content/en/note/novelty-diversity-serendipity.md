---
audio: [/audio/novelty-diversity-serendipity.mp3]
images: [/images/novelty-diversity-serendipity/novelty-diversity-serendipity.png]
categories: [Recommender Systems, Data Science & Analytics, Machine Learning]
date: 2022-03-06
lang: en
title: 'Serendipity: It''s Relevant AND Unexpected'
lastmod: '2022-05-07'
keywords: [serendipity, recommendation, diversity, novelty, serendipitous, user, kotkov,
  fig, accuracy, relevant]
recommendations: [/note/recommender-diversity/, /note/cross-validation-julia-recommender/,
  /note/ethical-challenges-in-recommender-systems/]
---

As I've been discussing over the last months, I personally believe measuring non-accuracy aspects of intelligent systems is one of the most important challenges to [make algorithmic recommendations ethical](/note/ethical-challenges-in-recommender-systems/).

- ["Diversity" Means More Than What We Typically Think](/note/the-power-of-diverse-thinking/)
- [Validate, Validate, and Validate Data. But, in terms of what?](/note/data-validation/)
- [Recommender Diversity is NOT Inversion of Similarity](/note/recommender-diversity/)

Now, let's dive deep into the most ambiguous type of non-accuracy recommender metric: **Serendipity**.

By definition, we can say **recommendation is serendipitous** ***if and only if*** it's (1) **relevant** to a user **AND** (2) **unexpected** for them.

> *First, a serendipitous item should be not yet discovered and not be expected by the user [unexpected]; secondly, the item should also be interesting, relevant and useful to the user [relevant].*<br/><br/>Source: "[Beyond Accuracy: Evaluating Recommender Systems by Coverage and Serendipity](https://dl.acm.org/doi/10.1145/1864708.1864761)" (2010)

Hence, the practitioners need to consider what defines relevance and unexpectedness of a recommended item, on a case-by-case basis. This is a big open-ended question, and that's why the concept of serendipity is rarely discussed both in academia and industry.

It should be noted that Serendipity is not the only metric that goes "beyond accuracy". For instance, **Novelty** and **Diversity** can also be employed to measure the goodness of recommendation as you can find at a [dedicated section in the Recommender Systems Handbook](https://link.springer.com/chapter/10.1007/978-1-4899-7637-6_8).

Importantly, regardless of the measurements, capturing the user's taste/desire in the form of relevance is a must. That is, it is not a good idea to naively show random irrelevant contents without taking user-centricity into account for the novelty and diversity sake.

Meanwhile, novelty and diversity are essentially different from serendipity in terms of unexpectedness i.e., how "obvious" the recommendation is. Here is the citation from the ["Beyond Accuracy" paper](https://dl.acm.org/doi/10.1145/1864708.1864761) again:

> *[...] movie is then called **novel recommendation** instead of serendipitous recommendation because he might discover this movie by himself. [...] It is then called a **diverse recommendation** instead of a serendipitous recommendation as he might be not surprised about the recommendation.*

- If the recommendation is novel, a user hasn't seen the content yet. However, they will eventually have an opportunity to interact with the item soon-ish, even if the recommender doesn't help anything.
- If the recommendation is diverse, it definitely helps users to break their unconscious bias and expand their "solution space", but the recommended items are still within the range of predictable outcomes.

Therefore, going beyond user's expectation is a unique, foundational requirement for serendipitous recommenders, and such a candidate must be in a tiny fraction of the entire relevant contents.

![novelty-diversity-serendipity](/images/novelty-diversity-serendipity/novelty-diversity-serendipity.png)

Notice that, since serendipitous recommendation makes users surprised, it's important to consider how to display the recommendation e.g., along with proper explanation. Otherwise, users would have no idea of what the recommendation is, and it unlikely becomes a positive "aha moment" for them.

Last but not least, there are several variations of the definition of serendipity and its relationship to the other metrics. To give an example, "[A Survey of Serendipity in Recommender Systems](https://dl.acm.org/doi/10.1016/j.knosys.2016.08.014)" illustrates the problem spaces as follows, which extends the discussion to e.g., irrelevant unexpected items and familiar items that aren't new to a user.

![Kotkov-et-al-fig1](/images/novelty-diversity-serendipity/Kotkov-et-al-fig1.png)<br/>_\* Image source: Kotkov, et al. "[A Survey of Serendipity in Recommender Systems](https://dl.acm.org/doi/10.1016/j.knosys.2016.08.014)" Fig. 1._
