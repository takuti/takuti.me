---
categories: [Business, Data Science & Analytics]
date: 2022-12-04
lang: en
title: Data Are Created, Collected, and Processed by People
keywords: [data, gender, feminism, sex, knowledge, human, localized, decisions, society,
  practices]
recommendations: [/note/data-leaders-summit-europe-2019/, /note/coursera-data-science-ethics/,
  /note/data-validation/]
---

That is, information in human society is localized, and there is always the existence of real humans throughout the data lifecycle from their generation to collection to aggregation. Even though a specific dataset you are analyzing looks simple, you cannot (and must not) reach a conclusion without understanding its context—how the data are generated, collected, and used by whom, and to whom your work is presented.

### Why people matter in data science

[***Data Feminism***](https://mitpress.mit.edu/9780262044004/data-feminism/) is a new way of looking at data with a special emphasis on underlying human biases. Unlike what we imagine from the wording, data feminism is not just about gender inequity behind data science, though it's certainly one of the most representative examples. In a wider sense, the idea reminds us that human biases exist everywhere across the data pipelines. Thus, every practitioner needs to acknowledge the facts and turn the understanding into conscious actions whenever they interact with data.

<a href="https://www.amazon.ca/Data-Feminism-Catherine-DIgnazio/dp/0262044005?&linkCode=li2&tag=takuti-20&linkId=9fe17056ffe6df5091c4ef99a50ffc95&language=en_CA&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=0262044005&Format=_SL160_&ID=AsinImage&MarketPlace=CA&ServiceVersion=20070822&WS=1&tag=takuti-20&language=en_CA" ></a><img src="https://ir-ca.amazon-adsystem.com/e/ir?t=takuti-20&language=en_CA&l=li2&o=15&a=0262044005" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />

To be more precise, biases are not something a tiny fraction of the population rarely experiences, and the challenges rather sit in the systemic nature of the entire society. A societal structure itself, lack of detailed metadata describing stories behind datasets, corporate's dependency on massive anonymous labors, white/male-dominated tech industry, and data science best practices that let the numbers speak for themselves—even though complex systems we live in today is not "flat" by any means, the reality is that the contexts are often overlooked by the majorities, and hence individual's voices can be easily suppressed thanks to the law of large numbers.

What makes the guidebook to data feminism crucial is that the seven principles—*examine power, challenge power, elevate emotion and embodiment, rethink binaries and hierarchies, embrace pluralism, consider context, and make labor visible*—have been introduced in an actionable form. The authors not only criticized bad (yet widely accepted) practices of data science but also discussed how we can approach complex, contextualized datasets in a more humane way.

They even exercised the data feminist practices throughout the writing process of the book, by carefully choosing words and making conscious decisions on which information sources to cite. Eventually, the book has demonstrated both the effectiveness and limitations; there are limitations because our view of the world is *situated*, and even with abundant effort on ensuring fairness, individual's arguments will remain positional to some degree.

### How to exercise data justice

So, what should we do in practice?

First and foremost, I'd say [we must begin with intrinsic motivation when it comes to (data) product development](/note/product-management-and-bullshit-job/), because that's how we can maximize the awareness of our positions that naturally limit individual's view of society. I, for example, can speak as a Japanese male raised in a middle-class family, software engineer holding a master's degree, single, Canadian permanent resident living in Vancouver, and so on. But I cannot speak for e.g., women, parents, Indigenous population, European people, and medical workers, simply because I'm not directly situated there. That's why individual, or [dividual](/note/dividual-in-recsys/), to be more accurate, is a [core of three pillars of ethics, wrapped by society and personal relationship](/note/ethics-and-relationship/).

Knowing the limitations, I then advocate the [need for working \*with\* customers](/note/internet-for-the-people/), or domain experts and stakeholders in general, so that we can complement the missing perspectives of each other and co-create a solution. Since knowledge is experiential, [we need diversity for practical reasons](/note/the-power-of-diverse-thinking/). This way of thinking is what the *Data Feminism* book calls "data for co-liberation", as opposed to the ambiguous "data for good" movement. What it means is to transfer the experts' knowledge to communities and create/store data in a cooperative, participatory way, resulting in [bridging a gap between localized knowledge and macroeconomy](/note/why-information-grows/).

Finally, a lineage of data, from their origin to final deliverables such as data product, visualization, and business decisions, needs to be accompanied by the names of people involved in the process and contextual metadata in the form of stories. I'm serious when I say [we should appreciate individual rows on a pandas `DataFrame`](/note/airflow-lineage/), since each row is derived from the physical instance(s) in this society, and countless people had been involved across what's called *data supply chain*. We cannot deal with complex systems without shedding a light on these unsung heroes. At one point when I was working on a never-ending data project, I jokingly talked to my colleague "once this project is finished, we should build a memorial monument with all labors' names on the surface".  Well, I should have said the joke in a more serious tone.

### If we overlook humans, the insights are simply "wrong"

The data feminist practices do take time, and they won't be aligned with conventional ways of data-driven work that value high efficiency. However, it won't be an excuse for data practitioners to overlook human aspects of data; if human factors were not taken into consideration, the outcomes would most likely be biased because of your own contexts.

To give an example of unconscious decisions I made, my biggest regret in [past publications](https://scholar.google.co.jp/citations?user=4GzRikkAAAAJ) is that I used gender data from a public dataset, [MovieLens](https://grouplens.org/datasets/movielens/), as a feature without spending enough effort to think of its seriousness. In fact, the papers were undergone a review process in terms of English writing by an English native professional, and I received a critical review comment: "Is gender really about gender? If it's about own identity, it's okay. But if it's about biological one, it should be labeled as sex." At that moment, I at least knew personal identity is not a binary thing, but since the dataset only had M/F binary values, I decided to use the data as a feature named sex. It took only about 10 seconds to craft a response to the reviewer. However, in reality, the [biological classification also isn't binary](https://www.malecontraceptive.org/blog/biological-sex-is-not-binary). Furthermore, even though it was somewhat of a conscious choice, it was not a good idea to casually change a label from its original dataset (gender) to something different (sex) without understanding the context. I should have thought deeper and probably not used the feature to train a model.

The list of bad examples grows further. For instance, I learned the importance of having contextual knowledge in painful ways when I worked on some projects that involved non-English conversations in foreign countries where I have zero knowledge about the local economies. Or, in the context of nuclear power development, the [gap between data-driven decisions and localized emotions](/note/a-bright-future/) visualizes the criticality of human factors, and these problems cannot be addressed purely by rationality. Technology is not magic, and data scientist is not god. 

Considering the complexity of this world, such insights lacking acknowledgment to all sorts of stakeholders can be simply "wrong" even if it theoretically sounds to the majority. Therefore, we need a radical shift in how to work on data without making an easy shortcut.
