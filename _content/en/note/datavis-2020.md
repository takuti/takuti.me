---
categories: [Programming]
date: 2021-01-21
draft: true
keywords: [zero, finding, fine, fix, flexible, flexibly, flow, flurs, focus, focused]
lang: en
recommendations: [/note/recommendation-julia/, /note/stop-drinking-alone/, /note/hugo-markdown-and-mathjax/]
title: 'Datavis 2020: A Free Online Course About D3.js & React'
---

I have recently studied data visualization with D3.js and React from [Datavis 2020](https://datavis.tech/datavis-2020/) by [Curran Kelleher](https://github.com/curran). 

<span class="iframe-container">
  <iframe src="https://youtube.com/embed/videoseries?list=PL9yYRbwpkykuK6LSMLH3bAaPpXaDUXcLV" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</span>

Here is a demo page I deployed the outcomes: **[takuti-sandbox.github.io/datavis-2020](https://takuti-sandbox.github.io/datavis-2020/)** \[[repo](https://github.com/takuti-sandbox/datavis-2020)\]

Overall, the course was just AMAZING and does teach us a wide variety of essential knowledge, including not only basic usage of D3.js but advanced performance optimization techniques:

- Key concepts in data visualization e.g., types of data and chart, starting from a [hand-writing sketch](https://github.com/unhcr/dataviz-streamgraph-explorer/issues/2) and communicating with stakeholders
- Git basics
- Tracking license and original source of public dataset
- React and ES6 basics
- Creating modules
- Performance optimization by memonization

That is, I believe the video series is also benefitial as an 101 course for programming and software engineering. 

What the course doesn't cover, on the other hand, is about production-grade package management tools and transpilers in the modern JavaScript ecosystem. It does make sense as there are so many options in this field and the trends change so rapidly; we can easily lose sight of our goal if we dive deep into those details. By using an online coding platform, [VizHub](https://vizhub.com/), which internally uses [rollup.js](https://www.rollupjs.org/guide/en/) and [buble](https://github.com/bublejs/buble) (not "Babel"), the course nicely simplied such a complex process of installation, dependency management, and compilation. 

Historically, "[Interactive Data Visualization for the Web: An Introduction to Designing with D3](https://amzn.to/3o4Jqhv)" is one of the most popular guides to D3.js data visualization as far as I observed. 

<a href="https://www.amazon.co.jp/dp/B074JKZ9Z3/ref=as_li_ss_il?&linkCode=li2&tag=takuti-22&linkId=e9616168d907d94303c2b0cb01b59366&language=ja_JP" target="_blank"><img border="0" src="//ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B074JKZ9Z3&Format=_SL160_&ID=AsinImage&MarketPlace=JP&ServiceVersion=20070822&WS=1&tag=takuti-22&language=ja_JP" ></a><img src="https://ir-jp.amazon-adsystem.com/e/ir?t=takuti-22&language=ja_JP&l=li2&o=9&a=B074JKZ9Z3" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />

However, its 2nd edition relying on D3 v4 is already outdated since v5 has been released, and I'm personally not interested in something super basic e.g., how to write JavaScript/CSS, how to use D3. In that sense, Datavis 2020 was way more practical and just did a job that I was looking for[^1].

As Curran stated in a video, Datavis 2020 follows a following principle:

> *Make it work, make it right, make it fast.* &mdash; Kent Beck

One thing I really like about the course is how the contents are well-structured from the basics to advanced topics.

[^1]: In fact, Datavis 2020 is also going to be outdated since D3 v6 has been released in the middle of the year.