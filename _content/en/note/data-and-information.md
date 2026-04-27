---
categories: [Data & Algorithms, Society & Business]
series: [ab, ai, data]
date: 2026-05-01
lang: en
title: Contextualize Data, Information, and Anything Digital
draft: true
---

By and large, digital systems consist of two different parts: **data** and **information**.

This website, [takuti.me](/), for example, is composed of a combination of numbers, text, images, and links. They exist in the digital world as data, which can be represented by the binary digits 0 and 1. Think of them as raw ingredients of a meal; each of them can be something yet unsophisticated to us as-is.

On the other hand, information is the result of processing and organizing data in a meaningful way. It is a menu, dish, and course that you will eventually come to appreciate and savour. I need to intentionally put the ingredients into context (i.e., recipe) so that deliverables are useful and relevant to a specific purpose or goal. Hopefully, [takuti.me](/) effectively visualizes my identity and conveys certain messages to its audiences as such.

Yes, there are a lot more things that happen in the kitchen, such as version control, hosting, networking, research, optimization, personalization, and interface design. But the **tools, methods, and processes are to be chosen in a way that makes sense to the given data and purpose**. (If you disagree with this point, you may want to examine the idea of [ethical product development](/note/ethical-product-developer/).)

So, anything digital is essentially fueled by data, *input,* and produces information, *output,* to achieve desired outcomes down the line. This is the foundational understanding for sustainable technology development, particularly in the era of AI. Notice that AI is a kind of tool built on top of data that generates information to its consumers, and its [skewed usage in wealthy nations](https://blogs.worldbank.org/en/investinpeople/from-predictions-to-practice--what-ai-usage-data-reveals-about-t) suggests varying needs for the inputs and outputs.

Here, the ultimate question is: *Given data, how can we maximize the certainty of achieving desired outcomes in an uncertain environment?* The following basic practices have been proposed at the data and information layers.

### Data: Document its WHY, WHERE, WHEN, WHO, WHAT, and HOW

First of all, **creators and consumers need to share an accurate understanding of data**. For this purpose, *[Datasheets for Datasets](https://arxiv.org/abs/1803.09010)* recommends documentation of a dataset, which can look like a spec document or a user guide of data.

Based on the authors' field experience and external feedback, the study proposed a series of template questions that help stakeholders work on data more mindfully.

There are seven categories of questions, with samples below (I changed some wording for clarity):

- **Motivation**: For what purpose was the dataset created? Who created the dataset?
- **Composition**: What data does each instance consist of? Are there any errors, sources of noise, or redundancies in the dataset?
- **Collection**: How was the data acquired? Over what timeframe was the data collected?
- **Preprocessing, cleaning, labelling**: Did the data already undergo any of them? Was the "raw" data saved in addition to the processed ones?
- **Uses**: Has the dataset been used for any tasks already? Are there tasks for which the dataset should not be used?
- **Distribution**: How/when will the dataset be distributed? Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use?
- **Maintenance**: Who will be responsible for supporting, hosting, and maintaining the dataset? Will the dataset be updated? If so, how often, by whom, and how will updates be communicated to its consumers?

By examining a dataset and documenting its intentions, subsequent solutions can better reflect the reality in terms of strengths, weaknesses, opportunities, and threats on the data, making its applications more impactful and sustainable in a given context. It is also a communication tool to build trust between consumers and producers, as [they often conflict](/note/the-producer-consumer-gap/) due to the difference in perspectives.

As for the example of food ingredients, datasheets are essential as we care about their traceability when shopping at farmers' markets or looking for "Made in XXX" and "Organic" labels at supermarkets. Documenting the sources, intermediate processing, and the chain of distribution from farms to factories to last-mile deliveries enables both chefs and eaters to be more confident in the dishes they eventually cook/eat.

It's about transparency and accountability.

### Information: Put your goal into social context

Now, we have ingredients and know about them very well. Time to cook!

Here, there are two things developers, or chefs, must avoid: oversimplification and overcomplication. The former is the attempt to make a one-size-fits-all solution, even though consumers' preferences and needs clearly vary. The latter, on the other hand, lets you overlook simpler solutions, making your work selfish, unsustainable, and wasteful.

Technologists tend to over-quantify things, use technology for its own sake (because "It's cool"), and ignore social contexts, as if we are dealing with rock-solid static materials. But our world and humans are more complex, and the **effectiveness of informational applications depends heavily on real-life constraints and human behaviours**.

That is, when tech interventions are naively deployed to the real world, they cannot cope with social complexities, and this makes the generated information ineffective, inaccurate, and even misleading.

That's why we need to consider information in sociotechnical, not only technical, contexts. In the fair-AI/ML domain, researchers [suggested](https://dl.acm.org/doi/10.1145/3287560.3287598) reviewing the following situated criteria to open developers' minds:

*The solution…*

1. *is appropriate to the situation?*
2. *affects the social context predictably?*
3. *can appropriately handle a robust understanding of requirements?*
4. *has appropriately modelled the social and technical requirements of the actual context?*
5. *is heterogeneously framed to include the data and social actors relevant to the localized question of fairness?*

Imagine wealthy individuals and organizations sending state-of-the-art informational products, say, Android tablets, to the world's poorest communities. I hope it's self-explanatory whether the attempt is (1) appropriate, (2) has predictable downstream impacts, (3) incorporates situational characteristics into its design, (4) addresses tangible challenges the locals are facing, and (5) stays relevant to them.

In other words, development activities must be deeply grounded in:

1. Contextual understanding
2. Minimum externality, i.e., one intervention doesn't introduce a new problem
3. Contextual adaptation
4. Applicability in the context
5. Good problem framing

Owning a Japanese restaurant in a Japanese suburb requires a completely different mindset and approach from serving Japanese food to New Yorkers in the heart of Manhattan, for example; the practice of framing a goal in a sociotechnical system is as simple as this. However, when it comes to information technology, stakeholders suddenly become insensitive to the [locality](/note/why-information-grows/) and assume that great devices and software are neutral and location-agnostic &mdash; regardless of whether it's too simple or too complicated.

We need to frame a goal at an appropriate level of abstraction.

### Bottom line

As digital tools are tightly embedded into the real world, the [flow of information](/note/how-information-flows/) shows complex, if not chaotic, patterns that are essentially uncontrollable to its creators. Therefore, an equitable and sustainable world needs deliberate efforts to mitigate risks at both ingredient and finished product levels.

First, use the sources that you &mdash; and everyone else &mdash; know well; you can't tell how this stranger's stew tastes without knowing its ingredients, or risking yourself by actually tasting it. (It may be poisoned!) To avoid such uncertainty, documenting what's in place, when it was created, where it is located, who is responsible for what, and why, is the least that developers can do. It's similar to the back of product packages, where you find nutritional facts, an expiration date, the manufacturer's name and contact, and all the disclaimers about product safety. It is still up to consumers what to do with the product, but the datasheet enables us to make an informed decision.

Then, optimize the process and deliverables for *where* and *who* you are at this point. As long as human activities are nuanced, your work cannot satisfy everyone, and even Michelin-starred restaurants can receive bad reviews on Google Maps. So, spend your time understanding your situation and strategizing what to do with the ingredients that you have. Long-term consequences remain uncertain anyway, but the investment at least increases the likelihood of success and makes failures more meaningful.

It should be noted that, in our capitalist world, incentives can easily override intentions; regardless of how mindful one is about the data and information generated from it, profit-maximizing applications will win and sustain in the short term. Thus, yes, you need to mitigate the risks, but also align the strategy with the rulebook of the economic game happening at the macro level.
