---
categories: [Life & Work, Business, Recommender Systems]
date: 2022-01-16
lang: en
title: '"Diversity" Means More Than What We Typically Think'
audio: [/audio/the-power-of-diverse-thinking.mp3]
keywords: [diversification, diversity, diverse, body, bubbles, filter, user, echo,
  chambers, voices]
recommendations: [/note/recsys-2021-echo-chambers-and-filter-bubbles/, /note/recsys-2021/,
  /note/ethical-challenges-in-recommender-systems/]
images: [/images/the-power-of-diverse-thinking/similar-vs-diverse.png]
summary: It clearly goes beyond how it's been normally discussed in business, and
  that's why my recent interest is outside of traditional accuracy/business metrics
  that we can "easily" optimize.
---

My recent reading of "[The Power of Diverse Thinking](https://www.amazon.com/Rebel-Ideas-Power-Diverse-Thinking-ebook/dp/B088DRDNN5/)" was eye-opening, and one of the key takeaways was "**we won't realize the benefit of diversity until it's actually diversified**."

<iframe type="text/html" width="212" height="362" frameborder="0" allowfullscreen style="max-width:100%" src="https://read.amazon.ca/kp/card?asin=B088DRDNN5&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_3FS8J0EH7PR289WC6HSP&hideBuy=true&hideShare=true" ></iframe>

To demonstrate the power of diversity, the author highlighted several real-world examples accompanied by scientific facts.  Ultimately, the book demonstrates how diversity helps us to work, act, and think better on a variety of occasions, ranging from politics and sports to diet and engineering.

I particularly see these insights through the lens of recommender systems development.

### Diversification as a practical tool

People can easily *get use to it* against something they are normally doing, because it's comfortable, and realizing the power of diversity gets harder and harder. Thus, it is important for us to consciously bring and interact with something/someone different so that we can see an outside of our own world and maximize the chance of diversification.

For example, when we think of diet, we could eat the same menu every day following the "best practice" written in a random recipe/nutrition book. It is indeed easy and efficient. However, in practice, our body reacts to the macros differently (e.g., carbo-loading vs. keto), and eating also plays an important role in bringing joy. In this regard, diversifying what we eat enables us to continuously optimize our eating habits and be healthier in a true sense.

Or, when it comes to fitness, one way is to do the same exercise every day to grow a specific part of your body. But if we diversify the training plan and consciously stimulate different parts of our body, it will increase overall body strength even further.

Therefore, diversification does have a practical benefit, and it means not only for increasing the coverage of a certain objective but for maximizing the chance of "success."

### What diversity means for recommender systems

To be more precise, the author illustrated the difference between a group of similar vs. diverse people as follows.

![similar-vs-diverse](/images/the-power-of-diverse-thinking/similar-vs-diverse.png)

_\* Original illustration is in the book._

From my view, the boundary boxes in this picture don't necessarily have to mean "population". It could also represent nutrition, emotion, and body parts. Literally anything can be considered under the boundary-and-coverage framework, and a solution that leads us to an ultimate success may be at the very corner of the problem space.

The same statement can be considered in the field of recommender systems. Content diversification is one of the key changes the researchers have been continuously discussing as we've seen in "[User-Centricity Matters: My Reading List from RecSys 2021](/note/recsys-2021/)". Here, it's not just for generating more serendipitous contents to maximize user engagement but for maximizing overall customer satisfaction from a fairness standpoint by showing diverse contents.

Everyone is different, and we know there is no one-size-fits-all solution. However, at the same time, it's "easy" for developers to assume a convex function, rather than spending costs on user-level optimization and model ensembling by taking multimodality into account.

### Possible directions

*How can we give a maximum chance of finding a local optima that sits to the edge of problem spaces?*&mdash;I personally feel this is the most important question we as a developer of personalized applications need to think of.

If recommenders were successfully optimized in terms of the diversity metrics, more users could safely and confidently use the service regardless of their unique background, preference, and/or restrictions.

Additionally, we don't want to overlook the [existence of echo chambers and filter bubbles when it comes to personalization](/note/recsys-2021-echo-chambers-and-filter-bubbles/), and diversification does matter to overcome the issue. It should be noted that the book emphasized "filter bubbles" and "echo chambers" are fundamentally different; a user is completely in an enclosed environment without any external voices in case of filter bubbles, whereas the latter means user's opinion is rapidly amplified by the other's voices coming from both inside and outside of a community the user is belonging to. Thus, these problems must be treated differently, but the research field of recommender systems is not still in the phase as far as I can observe.

"Diversity" means so much for everyone's life, and it clearly goes beyond how it's been normally discussed in business. That's why my recent interest is outside of traditional accuracy and business metrics that we can "easily" optimize.
