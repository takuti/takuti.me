---
categories: [Recommender Systems, Programming]
date: 2019-03-31
keywords: [julia, documentation, recommendation, pages, filtering, website, techniques,
  collaborative, mas, theoretical]
lang: en
recommendations: [/note/juliacon-2019/, /note/recommendation-julia/, /note/julia-travis-ci-to-github-actions/]
title: Publishing My Master's Thesis with Documenter.jl
---

When I was a master's student, I had developed [Recommendation.jl](https://github.com/takuti/Recommendation.jl), a collection of well-known recommendation techniques written in Julia:

- [Recommendation.jl: Building Recommender Systems in Julia](/note/recommendation-julia)

Recently I have been working on creating its [documentation site](https://takuti.github.io/Recommendation.jl/latest/) by using [Documenter.jl](https://github.com/JuliaDocs/Documenter.jl), a documentation generator for Julia. This article describes how the tool allows me to easily create the website and what I'm writing on it.

### Importance of documentation for Julia packages

In fact, I do not actively add state-of-the-art recommendation techniques to the Recommendation.jl package because the package simply focuses on providing a way to test well-studied traditional methods, with leaving room for user-side customization. I personally believe everything in the package is trivial in the field of recommender systems, and hence I did not write any dedicated documentations so far.

However, even if the implemented techniques are widely known (e.g., collaborative filtering, matrix factorization), I recently realized that explicitly documenting their underlying scientific concepts and mathematical equations is beneficial to provide a better understanding of the package, especially in case of the Julia programming language.

Most importantly, Julia is designed for high-performance scientific computing, mostly in academia. As an alternative option to MATLAB, the language gives an easy access to complex scientific techniques to those who are relatively familiar with their theoretical aspect. Consequently, documentation of third-party Julia packages needs to be structured properly for the unique demographics.

To give an example, when I see a [documentation page of Distribution.jl](https://juliastats.github.io/Distributions.jl/stable/multivariate.html#Distributions-1), it shows the probability density functions of a variety of distributions. On the other hand, [scikit-learn documentation](https://scikit-learn.org/stable/modules/mixture.html) explains a similar topic in a more intuitive and visually stimulating way by showing abundant figures and function interfaces.

For the reasons that I mentioned above, documentation should be written for the right readers in the right way, and the detailed theoretical descriptions help Julia users a lot in practice.

### Documenter.jl

Once I figured out the importance of theoretical documentation, I googled an effective way and finally found Documenter.jl. By the way, I do like Julia's language ecosystem that consists of such a variety of community-owned utility repositories like [METADATA.jl](https://github.com/JuliaLang/METADATA.jl) and [julia-logo-graphics](https://github.com/JuliaGraphics/julia-logo-graphics); it simply makes developers comfortable.

We can easily create our documentation website by using Documenter.jl as follows:

1. Install Documenter.jl:
    ```julia
    julia> import Pkg; Pkg.add("Documenter")
    ```
2. Write Markdown documents under `docs/src` and/or write docstrings in your source code.
3. Create `docs/make.jl` like:
    ```julia
    using Documenter, Recommendation

    makedocs(
        format = :html,
        modules = [Recommendation],
        sitename = "Recommendation.jl",
        authors = "Takuya Kitazawa",
        linkcheck = !("skiplinks" in ARGS),
        pages = [
            "Home" => "index.md",
            "Getting Started" => "getting_started.md",
            "References" => [
                "notation.md",
                "baseline.md",
                "collaborative_filtering.md",
                "content_based_filtering.md",
                "evaluation.md",
            ],
        ],
    )

    deploydocs(
        repo = "github.com/takuti/Recommendation.jl.git",
        target = "build",
    )
    ```
4. Compile documentation:
    ```sh
    $ julia docs/make.jl
    ```
5. Open and check the site from `docs/build/index.html`.
6. [Push to your GitHub repo to update a `gh-pages` branch.](https://juliadocs.github.io/Documenter.jl/stable/man/hosting/#gh-pages-Branch-1)

That's all. Thanks to Documenter, you can flexibly organize your pages in `makedocs(pages=[])`, and the website will automatically be published under `gh-pages` according to the `deploydocs()` configuration. Of course, the tool does support MathJax-based LaTeX syntax as well as [many other useful syntax](https://juliadocs.github.io/Documenter.jl/stable/man/syntax/).

### Porting my master's thesis to the Recommendation.jl documentation

Finally, I have been published the first version of Recommendation.jl documentation site. As I described above, the pages describe the theoretical detail of common recommendation techniques e.g., [collaborative filtering](https://takuti.github.io/Recommendation.jl/latest/collaborative_filtering).

It should be noted that these contents are originally from `.tex` files of my master's thesis. The thesis was entitled as "**Persistently Cold-Starting Online Item Recommendation for Implicit Feedback Data**," and I spent a lot of time to survey classical recommendation techniques. The topics are also compatible with [Recommender Systems Specialization in Coursera](https://www.coursera.org/specializations/recommender-systems); it is a great introductory course to see the inside of recommender systems.

While our thesis becomes publicly available after graduation, re-publishing it on the Internet in a different format gives another chance to attract attention and get feedback from more people. Building a relevant Julia package and writing its documentation (with Documenter.jl) would be a great option to do so.

Let's say, my master's thesis has been reborn on the website.