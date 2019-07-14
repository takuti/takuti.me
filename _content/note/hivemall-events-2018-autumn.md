---
date: 2018-10-26
lang: en
recommendations: [/note/mbed-simulator-td/, /note/hivemall-pyspark/, /note/umap-2019/]
title: 'Apache Hivemall at #ODSCEurope, #RecSys2018, and #MbedConnect'
---

[Apache **Hivemall**](https://github.com/apache/incubator-hivemall) is a scalable machine learning library running on top of the Hadoop ecosystem, and you can freely enjoy its functionalities in your [Apache Hive](https://hive.apache.org/) or [Spark](https://spark.apache.org/) environment.

Do you know [Google BigQuery ML](https://ai.googleblog.com/2018/07/machine-learning-in-google-bigquery.html)? It is a new machine learning solution that runs in their BigQuery data warehousing platform. BigQuery ML enables us to apply machine learning to our massive data by just issuing a series of queries, and what Hivemall allows us to is basically the same thing; both BigQuery ML and Hivemall introduce a new paradigm *"**machine learning in query language**,"* but Hivemall is more flexible in terms of selection of platform and algorithm.

I've recently spent one of the busiest and most exciting months in 2018 to talk about Hivemall at a couple of different events, **[Open Data Science Conference Europe](https://odsc.com/london)** (ODSC Europe), **[ACM Recommender Systems](https://recsys.acm.org/recsys18/)** (RecSys), and **[Mbed Connect USA](https://mbed.com/en/about-mbed/events/mbed-connect-usa-2018/)**, in the different contexts. Let's see what I've talked there.

### [Open Data Science Conference Europe](https://odsc.com/london) @ London

As the name suggests, this conference strongly focuses on publicly available research result, practical lessons, and open-source software in the field of machine learning and data science; advertising talk from industries is basically prohibited.

My talk was about Hivemall as an example of open-source software for scalable machine learning:

- **[Apache Hivemall: Query-Based Handy, Scalable Machine Learning on Hive](https://odsc.com/training/portfolio/apache-hivemall-query-based-handy-scalable-machine-learning-hive)**

<script async class="speakerdeck-embed" data-id="a5d4885dca69494dab8064b7d8f0fd00" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

When I asked "Is there anybody who currently uses Hive in your work?," 80% of the audiences raised a hand. Honestly I didn’t expect that, and I eventually realized that not a few companies are still maintaining their own Hadoop cluster and using Hive to analyze data. Hivemall can definitely be a deeply satisfying tool for such companies to leverage machine learning capabilities in their day-to-day data analytics.

I've attended and enjoyed many other sessions as well. Of course, almost all talks mentioned about deep learning. In my impression, theory and practice of deep learning is gradually getting matured (and peaked) in these days.

It should be noted that large number of conference attendees (2000+) had very different background and skill levels, and such chaotic situation clearly represents how ML and data science plays an important role in a wide variety of fields.

### [ACM Recommender Systems](https://recsys.acm.org/recsys18/) @ Vancouver

RecSys is an academic conference focusing on theory and practice of recommender systems, and I've [previously attended RecSys 2016](https://takuti.me/note/recsys-2016/) held in Boston.

Due to the exceptionally high demand of intelligent recommendation systems in real-life applications, the RecSys conference normally has many industrial attendees including researchers, data scientists and software engineers. Of course, this year’s RecSys was not an exception; more than 80% of participants I’ve chatted in person during the conference were coming from industry. I believe this year’s conference had more industrial demographics and presentations than 2 years ago.

Our paper about recommendation with Hivemall has been accepted to a demo session, and we presented in the form of poster during a conference buffet lunch break:

- **[Query-Based Simple and Scalable Recommender Systems with Apache Hivemall](https://dl.acm.org/citation.cfm?id=3241592)**

<script async class="speakerdeck-embed" data-id="9e6c5c2b5b524a76a9a0d01ce167b48a" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

If you are interested in this topic, there is a [YouTube video](https://www.youtube.com/watch?v=cMUsuA9KZ_c) in addition to the paper and poster.

Since many people were coming from industry, the session was a great opportunity to introduce Hivemall for practitioners and learn how each company implements their own recommendation engines in a scalable manner. Basically, what I understood during the session was:

- Many companies are actively using Spark and [Spark MLlib](https://spark.apache.org/mllib/) in production.
- Many people recognize Hive, but obviously it’s less famous than Spark.
  - Even if companies have their own Hive environment, developers of recommendation engine itself generally are not in charge of maintaining its underlying infrastructure.
  - That is, it’s hard for the developers to install Hivemall to their in-house big data analytics platform under their responsibility.
- While people commonly understand the importance of scalability, I felt Hivemall's query-based machine learning capability is less stimulating for them than Python- or Scala-based programming-driven recommender implementation.

Therefore, as a developer of Hivemall, thinking about how to effectively tell the strength of Hivemall to such technology-oriented practitioners should be important.

When we see other accepted papers, it is obvious that many paper focus more on a unique, specific scenario that has originally been motivated by the development of real-life recommender system, than traditional "research"-oriented topics. As far as I can observe, the situation has not been changed from 2 years ago, and this is exactly how recommender research rapidly grows and becomes popular in recent years. However, at the same time, such trend is slightly disappointing for me because there is a lack of stimulation in deeper theoretical, mathematical consideration.

From an algorithmic perspective, many studies and attendees' interests focused more on deep learning and something relevant e.g., item embedding. In fact, I already saw how deep learning plays a dominant role in the field of recommender systems at 2016’s RecSys, but the tool becomes much more important and common in these days.

Surprisingly (and unsurprisingly), organizers of a workshop session [Deep Learning for Recommender Systems](http://dlrs-workshop.org/) (DLRS), which was initiated in 2016 to encourage practitioners to apply deep learning techniques to recommender systems, stated that this year’s DLRS workshop is the final one, because deep learning is now widely used in many studies and getting matured in the context of recommender systems. This announcement is really impressive and clearly demonstrates the strong relationship between deep learning and recommender systems.

### [Mbed Connect USA](https://mbed.com/en/about-mbed/events/mbed-connect-usa-2018/) Workshop @ San Jose, CA

Our company [Arm Treasure Data](https://www.treasuredata.com/) develops an enterprise-grade advanced big data analytics platform, which is currently placed in a data management layer of the [Arm Pelion IoT platform](https://www.arm.com/products/iot/pelion-iot-platform), and the platform internally bundles Hivemall so that users can easily leverage machine learning capability on their massive data at scale without any expertise in Python programming and mathematics.

On behalf of Treasure Data, I have attended Mbed Connect USA 2018, a meet-up event focusing on the [Arm Mbed ecosystem](https://www.mbed.com/en/), held in conjunction with [Arm TechCon 2018](https://www.armtechcon.com/), and had 1-hour workshop session to introduce Treasure Data’s big data analytics capability in the context of data science and machine learning:

- **[Introduction to Data Science](https://www.mbed.com/en/about-mbed/events/mbed-connect-usa-2018/)**

<script async class="speakerdeck-embed" data-id="88e26e5ae97e4ae2ae11e646799f6814" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

There is a [Jupyter notebook](https://gist.github.com/takuti/6edab4a504368a0e58bb81a3158a1e07) as an auxiliary material.

Since Mbed Connect audiences are normally from electric engineering and IoT industry, I designed a workshop scenario with public IoT-ish data taken from [City of Chicago data portal](https://data.cityofchicago.org/); the city has a bunch of sensors in many places to collect environmental data such as temperature and soil moisture, and the local government makes the data public online.

Unfortunately, playing with [big sensor data](https://data.cityofchicago.org/Environment-Sustainable-Development/Smart-Green-Infrastructure-Monitoring-Sensors-Hist/ggws-77ih) and effectively utilizing Hivemall's ML capability (i.e., preprocessing, training, prediction, and evaluation) in the 1-hour session is nearly impossible. Hence, the workshop content was two-fold as:

1. Step-by-step tutorial from data load to ML-based prediction and evaluation with [tiny energy benchmarking data](https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c) (~300 records), which is also from the City of Chicago data portal.
2. Introduce the bigger real sensor data and show a way to join with the energy benchmarking data to enrich the input to a ML algorithm.

I hope the workshop was enjoyable and insightful for all participants, but I'm sure there are many things I can improve to make it better. On that point, since the workshop comes back to **Mbed Connect Tokyo** on December 5, 2018, we are now much more aware of realistic Mbed data and actively working on refining workshop scenario and materials.

### What's next?

As I mentioned above, you can see Hivemall's machine learning capability, especially in the context of IoT, at Mbed Connect Tokyo 2018 on December 5. Meanwhile, we're continuously seeking an opportunity to demonstrate how the paradigm of query-based machine learning makes our life easy.

Visit our [GitHub repo](https://github.com/apache/incubator-hivemall), [documentation](http://hivemall.incubator.apache.org/userguide/) and [tutorial](http://hivemall.incubator.apache.org/userguide/supervised_learning/tutorial.html) now, and see the new world!