---
categories: [Data & Algorithms]
series: [ab, ai, data]
date: 2026-05-01
lang: en
title: Data, Transparency, Information, Fairness, and Trust
draft: true
---

By large, digital systems consist of two different parts: **data** and **information**.

This website, [takuti.me](/), for example, is made of a bunch of numbers, texts, images, and links. They exist in the digital world as data, which can be represented by 0s and 1s. Think of them as raw ingredients of a meal; each of them is something yet nothing to us as-is.

On the other hand, information is the result of processing and organizing data in a meaningful way. It is a menu, dish, and course that you will eventually feel and taste. I need to intentionally put the ingredients into context (i.e., recipe) so that deliverables are useful and relevant to a specific purpose or goal. Hopefully, [takuti.me](/) effectively visualizes my identity and conveys certain messages to its audiences as such.

Yes, there are a lot more things going on behind the scene, such as version control, hosting, networking, research, optimization, personalization, and interface design. But all the tools, methods, and processes are to be chosen in a way that makes sense to the given data and purpose. (If you disagree with this point, you may want to read about [ethical product development](/note/ethical-product-developer/).)

So, anything digital is essentially fuelled by data&mdash;input&mdash;and produces information&mdash;output&mdash;hoping to bring desired outcomes down the line. This is the foundational understanding that derives a set of practices required for ethical technology development, especially in the AI era.

An ultimate question is: How can we maximize the certainty of achieving desired outcomes? Researchers suggest we can do the following in each part.

### Data: Document contexts

In *[Datasheets for Datasets](https://arxiv.org/abs/1803.09010),* researchers suggested the practices of making a datasheet (spec document) for a dataset so that the data is accurately understood and effectively utilized.

Based on years of the authors’ field experience and external feedback, the study proposes a series of template questions that help two distinct types of stakeholders, dataset creators and dataset consumers, work on data more mindfully.

There are seven categories of questions, with samples below (I changed some wording for clarity):

- **Motivation**: For what purpose was the dataset created? Who created the dataset?
- **Composition**: What data does each instance consist of? Are there any errors, sources of noise, or redundancies in the dataset?
- **Collection**: How was the data acquired? Over what timeframe was the data collected?
- **Preprocessing**, cleaning, labelling: Did the data already undergo any of them? Was the "raw" data saved in addition to the processed ones?
- **Uses**: Has the dataset been used for any tasks already? Are there tasks for which the dataset should not be used?
- **Distribution**: How/when will the dataset be distributed? Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use?
- **Maintenance**: Who will be responsible for supporting, hosting, and maintaining the dataset? Will the dataset be updated? If so, how often, by whom, and how will updates be communicated to its consumers?

By asking intentional questions and examining given data, subsequent solutions will better reflect the reality and become more impactful. It is a communication tool to build trust between consumers and producers, as [they often conflict](/note/the-producer-consumer-gap/) due to the difference in perspectives.

Coming back to the example of food ingredients, it is essential as much as we care about their traceability by going to farmers' markets and looking for "Made in XXX" and "Organic" labels at supermarkets. Documenting where the sources are coming from, what kind of intermediate processing was done, and who made the products available from farms to factories to last-mile deliveries enable both chefs and eaters to be more confident in the dishes they eventually cook/eat.

It's all about transparency and accountability.

## Information: Frame a goal in sociotechnical systems

Now, we have ingredients and know about them very well. Time to cook!

Here, there are two things developers, or chefs, must avoid: oversimplification and overcomplication. The former encourages one-size-fits-all solutions, even though consumers' preferences and needs clearly vary. The latter, on the other hand, lets you overlook simpler solutions, making your work unsustainable and wasteful.

Technologists have this tendency to over-quantify things and ignore social contexts, as if we are dealing with rock-solid static materials. But our world and humans are more complex, and sooner than later, the solutions enter social contexts that involve real-life decision-making and behavioural change.

For example, people nowadays talk about responsibility and fairness in AI applications, which rely heavily on computer scientific abstraction and modular design following the engineering best practices.

Metric, metric, metric.

Consequently, when it's naively deployed to real world, tech interventions cannot cope with social complexities, making the generated information ineffective, inaccurate, and misleading.

That's why we need to put information into sociotechnical, not only technical, contexts.

In the fair-AI/ML domain, in particular, researchers [suggested](https://dl.acm.org/doi/10.1145/3287560.3287598) checking the following situated criteria to measure fairness.

*The solution…*

1. is appropriate to the situation (contextual understanding);
2. affects the social context in a predictable way (minimize externality by making sure a solution doesn’t introduce a new problem);
3. can appropriately handle a robust understanding of requirements (contextual adaptation);
4. has appropriately modelled the social and technical requirements of the actual context (applicability);
5. is heterogeneously framed so as to include the data and social actors relevant to the localized question of fairness (good problem framing).

It’s about how to define a problem and goal in a way that makes sense to the context, before you start cutting the ingredients.
