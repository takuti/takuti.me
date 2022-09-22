---
categories: [Programming, Conference, Recommender Systems]
date: 2019-07-26
lang: en
title: 'Lightning Talk about Recommender Systems in Julia at #JuliaCon 2019'
lastmod: '2022-08-06'
keywords: [julia, recommendation, package, computing, juliacon, community, ecosystem,
  onference, book, baltimore]
recommendations: [/note/recommendation-julia-documenter/, /note/juliacon-2022/, /note/julia-travis-ci-to-github-actions/]
---

I have attended and presented at [JuliaCon 2019](https://juliacon.org/2019/) held in Baltimore, MD, USA:

- **[Recommendation.jl: Building Recommender Systems in Julia](https://pretalx.com/juliacon2019/talk/FFXKCX/)**

<script async class="speakerdeck-embed" data-id="7c5a8d8d54b44719b535f7e9b9764efc" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

Recording is available at YouTube:

<iframe width="560" height="315" style="max-width: 100%;" src="https://www.youtube.com/embed/kC8LKQ_YjyM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The 10-min lightning talk was very short. But it was a great opportunity to introduce my [Recommendation.jl](https://github.com/takuti/Recommendation.jl/) package and hear the comments from the audiences. Plus, I was inspired a lot by the other sessions and nice people I've met throughout the conference.

### Recommender Systems in Julia

As I spoke, since recommendation is not only about machine learning, I'm trying to keep the Recommendation.jl package as simple as possible with leaving enough space for user-side customization. This approach works particularly well for Julia because of its easiness, efficiency, and great package ecosystem.

In fact, due to the limited number of practical use cases, I'm still unsure if I created the package in the right way. However, a fact that Recommendation.jl is used in a book "[Julia Programming Projects](https://www.packtpub.com/big-data-and-business-intelligence/julia-programming-projects)" hopefully shows a certain degree of usability:

> In this article, we will look at machine learning based recommendations using Julia. We will make recommendations using a Julia package called ‘Recommendation’.<br /><br />
> This article is an excerpt from a book written by Adrian Salceanu titled [Julia Programming Projects](https://www.packtpub.com/big-data-and-business-intelligence/julia-programming-projects).<br/><br />
> *&mdash; [How to make machine learning based recommendations using Julia [Tutorial]](https://hub.packtpub.com/how-to-make-machine-learning-based-recommendations-using-julia-tutorial/)*

*Didn't know the book until very recently! I'd like to thank the author because it strongly motivates me to work more heavily on the personal project :)*

Meanwhile, someone at the conference said to me like:

> Oh, are you the author of Recommendation.jl? My first Julia code was actually with the recommendation package!

That's the power of the Julia ecosystem...everyone can easily and equally accessible to a wide variety of community-developed packages, and using the packages in their code is quite straightforward.

After my talk, Abhijith Chandraprabhu, a person working dedicatedly for the Julia Computing organization and creator of [RecSys.jl](https://github.com/abhijithch/RecSys.jl), reached out to me. We shared a lot of our experiences and opinions for Julia and recommender systems, even during the conference dinner and Inner Harbor cruise. It was the most meaningful time at this conference.

Excited to contribute more to the Recommender Systems in Julia field from now on.

### Julia Ecosystem in 2019

To be ready for the presentation, I have revisited my code and released [v0.3.0](https://github.com/takuti/Recommendation.jl/releases/tag/v0.3.0) of the recommendation package. For this purpose, walking through the "[Think Julia](https://benlauwens.github.io/ThinkJulia.jl/latest/book.html)" book was so helpful to make sure my understanding of the basics.

Interestingly, as an inactive holiday Julia programmer, I always find something new every time I review my Julia code thanks to the actively developed ecosystem. For example, this time I noticed that the community has developed [Registrator.jl](https://github.com/JuliaRegistries/Registrator.jl) and changed a way to release Julia packages; the official registry has been moved from [METADATA.jl](https://github.com/JuliaLang/METADATA.jl) to [JuliaRegistries/General](https://github.com/JuliaRegistries/General). 

Therefore, I was able to catch up recent progress on the Julia community before going to Baltimore. Currently, in combination with my JuliaCon 2019 experience, I believe the following topics particularly play an important role in the entire language ecosystem:

- Maturity of the language itself since the [last year's announcement of Julia 1.0.0](https://julialang.org/blog/2018/08/one-point-zero)
- GPU/hardware-based acceleration e.g., "[XLA.jl: Julia on TPUs](https://www.youtube.com/watch?v=QeG1IWeVKek)"
    - [GPUs &mdash; Julia Computing](https://juliacomputing.com/domains/gpus.html)
    - [Parallel Computing &mdash; Julia Computing](https://juliacomputing.com/domains/parallel-computing.html)
- Machine learning toolkits e.g., "[MLJ - Machine Learning in Julia](https://www.youtube.com/watch?v=ByFglWPqNlg)"
    - [Machine Learning and Artificial Intelligence &mdash; Julia Computing](https://juliacomputing.com/domains/ml-and-ai.html)

Meanwhile, I enjoyed a [keynote talk by Prof. Madeleine Udell from Cornell](https://www.youtube.com/watch?v=BjMgo3liDZ8). She introduced [LowRankModels.jl](https://github.com/madeleineudell/LowRankModels.jl), and the topic is exactly the one that I studied in my master's project.

### Julia Unifies Academia and Industry

The reason why I'm working as a data science engineer in the industry is that here is the great place to work in the middle of scientific algorithms and real-world applications; I do like scientific theories, but I strongly believe almost all of them are useless without practical real-world implementation. On that point, the Julia community is exceptionally attractive as an intersection between academia and industry.

Importantly, [Julia Survey Results](https://www.youtube.com/watch?v=yx6lBSHqGfc) demonstrated that the most common non-Julia language expertise of Julia programmers includes not only "fashionable" modern languages (e.g., Python, R, JavaScript, Scala) but also more like specialist-focused ones such as C, C++, MATLAB, Fortran. Thus, the community has an incredible diversity of technical background, and it certainly has a positive impact on creating innovative ideas and implementing them in the real world.

At JuliaCon 2019, I met a wide variety of professionals and students coming from different fields and geographical locations. Can you imagine a situation that everyone including university professors, industrial researchers, data scientists, financial analysts, software engineers, students studying in different departments, and weekend coders gathers together at the single location? JuliaCon does make it real. 

To be honest, I didn't expect such an exciting and productive conference experience. Thank you all of the community members for making it possible!