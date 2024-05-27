---
categories: [Machine Learning]
series: [ai]
date: 2020-08-29
lang: en
title: What I Think About When I Talk About ML Product
lastmod: '2022-05-07'
keywords: [product, business, solution, problems, solving, loop, cost, model, technical,
  questions]
recommendations: [/note/product-management-and-bullshit-job/, /note/ethical-product-developer/,
  /note/the-productize-book/]
---

Everyone wants to leverage machine learning (ML) in their daily work, and I'm sure they will be excited about your awesome ML product whatever the detail is. But, what do *we, as a product developer,* really have to think about when we create ML products?

Based on my experiences and what I learned from the following insightful articles, let me summarize five key questions we should ask ourselves.

- [5 Questions To Build Your AI Product Strategy Around](https://www.linkedin.com/pulse/5-questions-build-your-ai-product-strategy-around-vin-vashishta/)
- [Creating a Data Strategy for Machine Learning as a Product Manager](https://medium.com/pminsider/creating-a-data-strategy-for-machine-learning-as-a-product-manager-b56b7890ecf7)
- [7 Elements of AI Product Strategy](https://towardsdatascience.com/defining-your-ai-product-strategy-7-areas-of-focus-2cf112c82c07)

### 1. Do we have a clear mapping between business and technical problems?

Regardless of whether it's ML-based or not, our product should translate high-level business requirements into specific technical problems.

Since “AI/ML” sounds exceptionally attractive but cannot solve all the problems in the world, making sure the connection is particularly important.

For example, if our business requirement is to improve product margin, a technical problem our product handles is solving an optimization problem to find an optional product price.

On the other hand, the following scenarios easily lead us in the wrong direction.

*“We want to use AI to grow our business”* &mdash; A business requirement isn’t clear enough. What metrics are you tracking? What is your measurable goal?

*“We want to produce 2x more units in a single factory by using ML”* &mdash; Inappropriate choice of technology. In fact, ML might bring an innovative solution (e.g., the brand-new architecture of factory machines designed by ML algorithms), but it’s still unclear if that’s the case for this type of hardware/machine-oriented business requirements.

## 2. Is using ML for solving the problems cost-effective?

Similar to the other product features, our first step is to understand customers and their problems.

Once we identified a set of problems, one important question has naturally arisen: *Which problem(s) could ML solve?*

Finally, we must justify cost vs. performance gain when we apply ML to these problems: *Is solving this problem by ML cost-effective? What alternatives we can think of?*

It is important to note that ML is generally expensive when we undergo an end-to-end development lifecycle from data collection and preprocessing to training and evaluation; more human resources, as well as computing power, are surely needed over a long period of time. If you come up with a much simpler solution, try it first of all.

### 3. How quick can we have “MVPs”?

Compared to the other engineering problems, the development of ML-based products tends to be longer (and even be a never-ending story) since continuous evaluation & optimization is the core of a successful ML solution.

Consequently, it’s easy to spend an infinite amount of time on building “MVP”, which won’t be “minimum” anymore.

We must pay special attention to building an end-to-end solution as quickly as possible in the shortest path. (Of course, we can say the same thing for all the product features, but ML, in particular.)

- [Start with a cupcake](https://www.intercom.com/blog/start-with-a-cupcake/)

Here are some examples of what to do at a minimum:

- Collecting a reasonably small set of data before building a complete data pipelines.
- Running Exploratory Data Analysis (EDA) for understanding a big picture of the data.
- Starting from the simplest model (e.g., linear model) with offline evaluation.

Notice that answering Questions #1 and #2 helps you to find an appropriate approach you could take.

### 4. How do we ensure humans in the loop?

It depends on a target persona of your product, but, since running a feedback loop is a must for ML, the product should have a way of providing human feedback in the end-to-end pipeline, even if the feature is designed as an out-of-the-box packaged solution.

As we covered in Question #1, the ML solution must be strongly tied to business objectives, and hence customer needs to be able to measure the quality of ML-based outcomes and be confident on it. Otherwise, ML models guide their business in the wrong direction and cause a serious problem in some cases.

That is, in order to make your product reliable and usable for end-users, a fully automated solution won’t work, and leaving a space for human interactions in an appropriate way is highly important. It doesn't matter if the model uses state-of-the-art techniques and shows the best accuracy in a lab setup.

### 5. Why should customers use your ML solution?

Nowadays, there are so many options to leverage ML in the customer’s business process:

- Human
    - The in-house data science team
    - Non-experts who learned the basics from a book/online course
    - Consultancy
- Tools
    - Jupyter
    - Python
    - Numpy
    - Spark
- Infrastructure
    - AWS
    - GCP
    - Azure
- ...

Hence, unless there is a strong competitive advantage in our solution, our customer doesn’t necessarily have to choose it.

Examples of competitive advantages include:

- Strong professional service team supporting ML model deployment.
- A domain-specific model built by unique private dataset.
- Seamless integration with user's daily business process and external tools their business relies on.

### Bottom line

While offering no ML features definitely has a negative impact on the modern tech businesses, making the functionalities worthwhile to customers is rather difficult.

Therefore, I want to carefully ask the questions to myself when I think about the ML product:

1. Do we have a clear mapping between business and technical problems?
2. Is using ML for solving the problems cost-effective?
3. How quick can we have “MVPs”?
4. How do we ensure humans in the loop?
5. Why should customers use your ML solution?
