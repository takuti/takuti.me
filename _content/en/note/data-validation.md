---
audio: [/audio/data-validation.mp3]
categories: [Programming, Data Science & Analytics]
series: [data]
date: 2022-02-20
lang: en
title: Validate, Validate, and Validate Data. But, in terms of what?
lastmod: '2022-09-02'
keywords: [data, accuracy, validation, tfx, pipeline, paper, metrics, schema, observability,
  privacy]
recommendations: [/note/coursera-data-science-ethics/, /note/data-leaders-summit-europe-2019/,
  /note/airflow-lineage/]
---

When it comes to modern machine learning and data analytics applications, I cannot stress the importance of data validation enough. However, it's rarely discussed what defines the validity of our data.

Most importantly, accuracy, which many practitioners can easily think, is just a single aspect of the problem, and I strongly believe **privacy, security, and ethics measurements must be equally treated as the accuracy metrics**. Is our job done once we confirm a statistically significant increase in recall/precision and/or certain business metrics? No, absolutely not. On top of that, we (as a modern data-driven developer) must be more conscious about individual data points we are interacting with, as I discussed in [Data Ethics with Lineage](/note/airflow-lineage/).

That is, the developers need to implement a way to ensure if the data is truly "good" to use. For instance, if the data contains some PIIs, your machine learning model can reasonably show better performance, but the model must not be deployed from the privacy standpoint. Or, when the data is highly skewed toward a certain population (e.g., by gender, country, religion), prediction results must be biased. These situations are carefully treated by a proper mechanism embedded in a data pipeline.

***Lack of non-accuracy aspect of data validation in the TensorFlow Extended (TFX) paper***. I was recently reviewing [Google's classic TFX paper (2017)](https://research.google/pubs/pub46484/). The idea behind the data validation mechanism of TFX is schema matching; by validating data schema, the system prevents users from using/publishing any corrupted data they haven't expected. It contributes to maintaining the accuracy of the dataset itself, as well as the accuracy of downstream machine learning models. It should be noticed that, even though the paper spent a good chunk of paragraphs for *defining a "good" model* and *judgment of model goodness,* the discussion about the models hasn't been extended to data itself. As far as I read, we don't see such consideration even in its follow-up paper [Data Validation for Machine Learning (2019)](https://research.google/pubs/pub47967/).

***Emerging trend in data observability and quality***. I might be biased by the topics I'm regularly following, but it shouldn't be a coincidence I repeatedly heard the names of enterprise vendors over the last couple of months, which are similarly tackling underlying data validation issues. It includes the ones that I listened through [Software Engineering Daily Podcast](https://softwareengineeringdaily.com) e.g., [Monte Carlo](https://www.montecarlodata.com), [Trifacta](https://www.trifacta.com), and [Anomalo](https://www.anomalo.com). In fact, I'm not working on a B2B data business anymore, and hence I have zero opportunity to work with these third-parties on my day-to-day job. But they are caught by my radar on a regular basis. Thus, there seems to be a trend in data observability and quality domain. Personally, it is really nice to see active discussions about "how data itself should be"; after a few years since Google gently unlocked the domain of data validation in academia, the practitioners also finally started thinking about what happens somewhere in the middle of ETL and modeling work.

***Towards "zero-trust" data pipeline***. That said, the domain is still immature as far as I can see, and the measures users could validate are limited to the basic ones, such as the traditional accuracy metrics, missing values, and PII detection. You might think security, privacy, and ethics related treatments e.g., data anonymization, normalization, amplification must be done by the upstream jobs that are in charge of ETL/data wrangling stuff, but it is not a good practice unless you have the full control/ownership of the upstream jobs; anywhere in the pipeline could suddenly be broken for some random reasons, and the issues don't always surface as clear deterioration of accuracy metrics. Therefore, I would rather suggest building a data pipeline in a zero-trusted manner. Having solid definition of "valid" data and making sure the validity in your own scope are crucial to prevent any undesired consequences, and non-accuracy aspects must be properly taken into account to keep product quality & reliability high.
