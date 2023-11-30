---
audio: [/audio/coursera-data-science-ethics.mp3]
categories: [Machine Learning, Business, Data Science & Analytics]
date: 2022-03-20
lang: en
title: 'It "Was" Ethical: Key Takeaways from UMich''s Data Science Ethics Course'
lastmod: '2022-09-02'
keywords: [data, ethics, ethical, validate, regulation, science, cameras, privacy,
  driven, society]
recommendations: [/note/ethics-and-relationship/, /note/data-validation/, /note/airflow-lineage/]
---

One of the most important takeaways from [UMich's "Data Science Ethics" on Coursera](https://www.coursera.org/learn/data-science-ethics/) is that **ethics is defined by social consensus**.

### "What's good" changes

First of all, since the definition of "right" and "wrong" changes as time goes by & technology advances, we as a data science practitioner should keep questioning ourselves like *"Is this socially acceptable?"* throughout the data-driven product development lifecycle. In particular, by balancing an individual's value and public benefit, our deliverables must meet shared expectations from the society.

To give an example, we commonly see cameras at supermarkets or shopping malls nowadays, and many of us do not think our privacy is threatened because of the devices; there is social consensus that these cameras are "good" for security reasons and do contribute to making the public places safer. However, if the videos or images captured by the cameras are used for unintentional purposes, it becomes questionable whether the practice is ethical or not.

Thus, a boundary between good and bad tends to be fuzzy, and social acceptance criteria depend largely on the contexts when it comes to technology/data-driven solutions. Even though a behavior *was* ethical 10 years ago, it's possible that the same action is considered as unethical by the latest society. This is how ethics differ from religion, law, policy, and regulation, which are typically more stable and don't fluctuate that much. These fixed criteria rely on ethical behaviors defined by the society as of their original publication though; normally, society defines ethics, and regulation follows (after a long time).

### Ethical data-driven work

Meanwhile, even though ultimate societal impact is unpredictable, there are several good practices for data scientists to minimize the risk of doing something unethical. For instance, when we collect data, we could ensure if sampled data is a statistically reasonable representative of the population i.e., no imbalance among the attributes. Otherwise, it is "easy" to make algorithms racial as a model fits to (is biased by) the majority; minor samples can be easily suppressed in a resulting predictor unless we make a conscious treatment.

Moreover, it is crucial to validate the data and model based on proper measurement, meaning [Validate, Validate, and Validate Data. But, in terms of what?](/note/data-validation/) A validation phase enables us to make the whole system less error-prone and overcome potential drift (i.e., temporal change). As the professor mentioned in the course, ***systems are only as good as data***.

Another important topic in the ethics context is user's privacy and anonymity. Historically, these are considered as part of trust relationships based on local face-to-face communications, but it has become challenging on the internet; we don't have enough information about the person we are interacting with, and hence there is no guarantee that the person is trustable. Even though [blockchain](/note/coursera-blockchain-specialization/) has slightly changed the situation, it is still mandatory for developers to provide privacy related features *by design* e.g., allowing users to control their own data, preventing the possibility of leakage, taking into account recall-precision trade-off.

### Mindful data science

Last but not least, as regulation tends to come later, the course emphasized the value of **code of ethics** at an individual level; [Ethical Product Developer
](/note/ethical-product-developer/) describes my code of ethics, for example, although I should make it more succinct. Being mindful about the externalities of data-driven decisions is clearly the first step to being ethical, and we should not forget a fact that there are real human beings behind the data.

> When we see a dataset on a Jupyter notebook, we shouldn't forget the fact that there is a real world upstream. The oil is not a toy for unconscious software engineers and/or data scientists, and it's not a tool for capitalistic competition based on an extrinsic motivation. It is rather highly sensitive and precious information depicting everyone's beautiful life. ([Data Ethics with Lineage](/note/airflow-lineage/))

In that sense, there must be no difference between medical or social scientific studies vs. data science at large. Therefore, obtaining informed consent & receiving objective review from third-parties would also need to be the norm for real-world data science.


