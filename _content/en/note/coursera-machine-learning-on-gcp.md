---
categories: [Machine Learning, Business, Data Science & Analytics]
date: 2022-09-14
lang: en
title: Seeing Past and Present in Coursera "Machine Learning on Google Cloud" Specialization
images: [/images/coursera-machine-learning-on-gcp/certificate.png]
keywords: [specialization, google, cloud, vertex, bigquery, feature, solving, systems,
  engineering, keras]
recommendations: [/note/gcp-dataflow/, /note/machine-learning-product/, /note/coursera-scala-capstone/]
---

I have recently got a chance to review machine learning (ML) basics through [**Machine Learning on Google Cloud Specialization** on Coursera](https://coursera.org/share/28e4b7d13b11fbf63f5795f0701cf283). Although none of the contents was really new to me, it was a well-developed series of courses that gives us a high-level overview of the field both in theory and practice, accompanied by hands-on assignments on Google Cloud so we can familiarize ourselves with how to turn the basic concepts into workable implementations. I would definitely recommend the course if someone has a plan to build a data/ML pipeline on Google Cloud from scratch knowing little to nothing about ML.

![certificate](/images/coursera-machine-learning-on-gcp/certificate.png)

### The basics

What you will learn from the specialization can be summarized as follows.

1. [How Google does Machine Learning](https://www.coursera.org/learn/google-machine-learning?specialization=machine-learning-tensorflow-gcp)
    - Introduction to Google's ML offerings, such as Vertex AI and BigQuery ML.
    - Showcasing best practices for solving a real-world problem by using data & ML, with a particular emphasis on explainable and responsible AI.
2. [Launching into Machine Learning](https://www.coursera.org/learn/launching-machine-learning?specialization=machine-learning-tensorflow-gcp)
    - Understanding the basic steps in a common ML lifecycle such as hyperparameter tuning, evaluation, and deployment.
    - Implementing solutions with Vertex AI Workbench (Jupyter Notebooks) and BigQuery ML by taking full advantage of AutoML.
3. [TensorFlow on Google Cloud](https://www.coursera.org/learn/intro-tensorflow?specialization=machine-learning-tensorflow-gcp) 
    - Creating non-AutoML, deeper neural network-based models with TensorFlow & Keras, and containerizing the resulting models.
    - Diving deep into key ML concepts, like loss function and regularization.
4. [Feature Engineering](https://www.coursera.org/learn/feature-engineering?specialization=machine-learning-tensorflow-gcp)
    - Highlighting the importance of feature engineering and some of the common techniques.
    - Engineering features on BigQuery ML, Keras, and Apache Beam-based Dataflow, so that we can "package" a featurization pipeline and manage its resulting feature set in Vertex AI Feature Store.
5. [Machine Learning in the Enterprise](https://www.coursera.org/learn/art-science-ml?specialization=machine-learning-tensorflow-gcp)
    - Seeing how a cross-functional team can work on Google Cloud across multiple services, not only for scalable model training and optimization but for data/model management and governance.
    - For instance, we manipulated raw data stored in BigQuery with [Dataprep by Trifacta](https://cloud.google.com/dataprep), which reminds me of a conversation from [Trifacta with Joe Hellerstein - Software Engineering Daily](https://softwareengineeringdaily.com/2021/12/20/trifacta-with-joe-hellerstein/).

Note that the majority of the assignments are based on a [collection of Jupyter notebooks available on GitHub](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2).

### Evolution of the field

It's been more than 8 years since I first formally studied ML from an "original" version of Andrew Ng's famous online course, Machine Learning[^1]. Ever since then, the field of ML has evolved a lot at a faster pace than we anticipated. Obviously, it's not easy for practitioners to follow all the technological advances and apply them in their day-to-day work. 

Thus, the specialization was a good reminder of the key principles and where the industry standards are; even though I've been continuously working on relevant projects over the last few years, my work covers a tiny fraction of the entire domain space "ML" speaks about.

Meanwhile, many of the state-of-the-art topics are not necessarily useful for real-life scenarios, and a lot of "complex" problems we are facing can be solved by much simpler ideas such as heuristics and classic algorithms invented decades ago. That's why [I want to be conscious about the definition of AI vs. use of ML](/note/klara-and-the-sun/), and starting from problem framing (as opposed to *"running an ML project for the sake of using ML"*) is one of the most important steps every practitioner must undergo.

### Non-ML solution still matters

Speaking of *"ML for the ML sake",* I have an impression that the specialization does not emphasize the importance of easier paths (e.g., heuristics, human-in-the-loop, simpler rule-based or linear models) enough, though the first course briefly mentioned how critical problem framing is. To give an example, when the specialization teaches a concept of recommender systems, they define the systems as:

> Recommendation systems are machine learning systems that ...

But I disagree with the statement because non-ML techniques often derive satisfactory outcomes when it comes to personalization. Notice that I am a strong advocate of building intelligent systems from the least complicated approach as I've been writing about [Machine Learning](/note/category/machine-learning/) and [Recommender Systems](/note/category/recommender-systems/) in this blog.

On one hand, we are lucky as everyone can easily get started with ML under decent internet connectivity e.g., on Google Cloud. On the other hand, sophisticated tools like Vertex AI may hinder the learners from pausing for a moment and questioning themselves like "[Why do we build this?](/note/foundations-of-humane-technology/)". Hence, I hope the educational content like the specialization pays stronger attention to setting a proper tone for the use of these advanced technologies and enabling learners to equip a diverse mindset, so they can think and choose the right technology for solving an underlying problem in a true sense.

In conclusion, I would like to echo what I stated in [What I Think About When I Talk About ML Product](/note/machine-learning-product/). You, as a practitioner, must be excited after learning how to run ML on GCP, but let's pause for a moment and ask the following questions before moving forward:

1. Do we have a clear mapping between business and technical problems?
2. Is using ML for solving problems cost-effective?
3. How quickly can we have "MVPs"?
4. How do we ensure humans are in the loop?
5. Why should customers use your ML solution?

[^1]: The legacy course page doesn't exist on Coursera anymore, and it's currently part of a [new specialization offering](https://www.coursera.org/specializations/machine-learning-introduction).
