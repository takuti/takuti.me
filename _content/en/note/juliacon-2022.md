---
categories: [Programming, Conference, Recommender Systems]
date: 2022-08-06
lang: en
title: 'Recommendation.jl Came Back to #JuliaCon 2022'
images: [/images/juliacon-2022/discord.png]
keywords: [juliacon, julia, discord, talk, note, validate, validation, recommendation,
  diversity, data]
recommendations: [/note/juliacon-2019/, /note/cross-validation-julia-recommender/,
  /note/novelty-diversity-serendipity/]
---

At [**JuliaCon 2022** @ Online](https://juliacon.org/2022/) held during the last week of July, I gave a lightning talk about [Recommendation.jl](https://github.com/takuti/Recommendation.jl/), a Julia package for building recommender systems. It's been 3 years since the last time I talked about the package at [JuliaCon 2019](/note/juliacon-2019/), and, since polishing the (outdated) implementation towards v1.0.0 is [one of my recent focus areas](/now/), I decided to showcase the updates of the package and take it as an opportunity to review the remaining steps ahead of me.

Check out the presentation at YouTube:

<span class="iframe-container">
    <iframe src="https://www.youtube.com/embed/PI7HZFzMSVc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</span>

Over the last few months, my biggest technological interest has been in ***what defines the "goodness" of data-driven applications,*** including recommender systems. Intuitively, more accurate prediction is better as algorithmic recommendation eventually encourages the users to "efficiently" use their time on the applications. However, it often causes unintended consequences as we've discussed in the context of [ethical product development](/note/ethical-product-developer/), [data science ethics](/note/coursera-data-science-ethics/), and [humane use of technology](/note/foundations-of-humane-technology/). Thus, I do believe non-accuracy aspects of the systems are equally or even more important, and I'm glad that I was able to turn the idea into actual implementation as part of the Julia package.

The topics I highlighted in the talk mostly overlap with the following articles that I posted early this year:

- [Recommendation.jl v0.4.0: Working with Missing Values, Data Typing, and Factorization Machines](/note/recommendation-julia-v040/)
- [Validate, Validate, and Validate Data. But, in terms of what?](/note/data-validation/)
- [Recommender Diversity is NOT Inversion of Similarity](/note/recommender-diversity/)
- [Serendipity: It's Relevant AND Unexpected](/note/novelty-diversity-serendipity/)
- [Cross Validation for Recommender Systems in Julia](/note/cross-validation-julia-recommender/)

I wish I could discuss more about each of these concepts in the talk, but stay tuned for now - As mentioned, I'm planning to write a [JuliaCon proceeding paper](https://proceedings.juliacon.org/) in the coming months so that I can provide in-depth explanation, discussion, and evaluation results.

Last but not least, the online conference experience of JuliaCon 2022 was superb.
During my talk, I simply needed to make myself available in a dedicated Discord channel, and Q&A happened there:

![juliacon-2022-discord](/images/juliacon-2022/discord.png)

(Yes, I was down for COVID when I recorded the talk...)

I would like to thank organizers for the hassle-free video recording/uploading process and well-organized "virtual venue" on Discord. Similarly to my previous experience at the physical conference in 2019, it is clear how powerful & supportive the Julia community is.

<script async class="speakerdeck-embed" data-id="18ee2fd0898048d9bfb59237b314cbb1" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>


