---
categories: [Programming, Data Science & Analytics]
date: 2021-01-23
images: [/images/datavis-2020/fitbit-official-dashboard.png, /images/datavis-2020/fitbit-steps-chart.png]
lang: en
title: 'Datavis 2020: A Free Online Course About D3.js & React'
lastmod: '2022-05-05'
keywords: [datavis, visualization, fitbit, dashboard, chart, curran, data, augmented,
  official, ourse]
recommendations: [/note/augmented-analytics/, /note/first-vis-with-fitbit/, /note/flight-emissions/]
---

I have recently studied data visualization with D3.js and React from [Datavis 2020](https://datavis.tech/datavis-2020/) by [Curran Kelleher](https://github.com/curran). 

<span class="iframe-container">
  <iframe src="https://youtube.com/embed/videoseries?list=PL9yYRbwpkykuK6LSMLH3bAaPpXaDUXcLV" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</span>

Here is a demo page I deployed the outcomes: **[takuti-sandbox.github.io/datavis-2020](https://takuti-sandbox.github.io/datavis-2020/)** \[[repo](https://github.com/takuti-sandbox/datavis-2020)\]

### What Datavis 2020 introduces

Overall, the course was just AMAZING and does teach us a wide variety of essential knowledge, including not only basic usage of D3.js but advanced performance optimization techniques:

- Key concepts in data visualization e.g., types of data and chart, starting from a [hand-writing sketch](https://github.com/unhcr/dataviz-streamgraph-explorer/issues/2) and communicating with stakeholders
- Git basics
- Tracking license and source of a public dataset
- React and ES6 basics
- Creating modules
- Performance optimization by memoization

That is, I believe the video series is also beneficial as an 101 course for programming and software engineering. 

As Curran referred in a video, Datavis 2020 follows the following principle:

> *Make it work, make it right, make it fast.* &mdash; Kent Beck

One thing I like about the course is how the contents are well-structured from the basics to advanced topics in this particular order.

What the course doesn't cover, on the other hand, is about production-grade package management tools and transpilers in a modern JavaScript ecosystem. It makes a lot of sense as there are so many options in this field and the trends change so rapidly; we can easily lose sight of our goal if we dive deep into those details. 

By using an online coding platform, [VizHub](https://vizhub.com/), which internally uses [rollup.js](https://www.rollupjs.org/guide/en/) and [buble](https://github.com/bublejs/buble) (not "Babel"), the course nicely simplified such a complex process of installation, dependency management, and compilation. 

### It's modern

The practical courses of Datavis 2020 did a great job of updating my out-of-date knowledge and learning something new.

Historically, "[Interactive Data Visualization for the Web: An Introduction to Designing with D3](https://amzn.to/3o4Jqhv)" was one of the most popular guides to D3.js data visualization as far as I observed:

<a href="https://www.amazon.co.jp/dp/B074JKZ9Z3/ref=as_li_ss_il?&linkCode=li2&tag=takuti-22&linkId=e9616168d907d94303c2b0cb01b59366&language=ja_JP" target="_blank"><img border="0" src="//ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B074JKZ9Z3&Format=_SL160_&ID=AsinImage&MarketPlace=JP&ServiceVersion=20070822&WS=1&tag=takuti-22&language=ja_JP" ></a><img src="https://ir-jp.amazon-adsystem.com/e/ir?t=takuti-22&language=ja_JP&l=li2&o=9&a=B074JKZ9Z3" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />

However, its 2nd edition relying on D3 v4 is already outdated since v5 has been released[^1], and the book is too basic for experienced developers. 

Meanwhile, if I remember correctly, my last in-depth D3 experience was its v3, which is 3 major versions older than the latest, and I used the library with [Leaflet](https://leafletjs.com/) and jQuery for geospatial data visualization. jQuery...it's so nostalgic, isn't it? 

By contrast, Datavis 2020 is a valuable guide to modern JavaScript & D3.js that relies on React.

### What's next?

As I wrote in "**[What Makes a Good Dashboard: The Rise of Augmented Analytics](/note/augmented-analytics/)**", I'm currently interested in the possibility of visualization as a tool for effective use of data and machine learning. Thus, by leveraging what I learned from Datavis 2020, I'd like to build an interactive dashboard that brings a clear value to our life.

To be more precise, I'm trying to explorer my health and activity log collected by Fitbit. 

They do expose an official dashboard on their website, but I don't see any **actionable insights** on the top; it's far from how Augmented Analytics should be.

![fitbit-official-dashboard](/images/datavis-2020/fitbit-official-dashboard.png)

As a first step, I just started looking into [Fitbit API](https://dev.fitbit.com/build/reference/web-api/activity/) and creating a simple bar chart from there:

![fitbit-steps-chart](/images/datavis-2020/fitbit-steps-chart.png)

As Curran has built a chart for the number of COVID-19 cases in Datavis 2020, there is a direct relationship between data visualization and real-world circumstance. It means that data visualization has a huge potential to change our lives.

[^1]: In fact, Datavis 2020 is also going to be outdated since D3 v6 has been released in the middle of the year.