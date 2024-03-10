---
audio: [/audio/recommendation-julia-v040.mp3]
series: [julia]
categories: [Recommender Systems, Programming]
date: 2022-01-08
lang: en
title: 'Recommendation.jl v0.4.0: Working with Missing Values, Data Typing, and Factorization
  Machines'
lastmod: '2022-02-27'
keywords: [recommendation, julia, factorization, machines, scientifictypes, types,
  missing, proper, implemented, general]
recommendations: [/note/recommendation-julia/, /note/juliacon-2019/, /note/recommendation-julia-documenter/]
---

This week I have released [version 0.4.0 of Recommendation.jl](https://github.com/takuti/Recommendation.jl/releases/tag/v0.4.0), a library for recommender systems in Julia. As usual, you can get the package from the Julia centralized package repository and play with it as follows:

```julia
julia> using Pkg; Pkg.add("Recommendation")
```

It's been more than two years since the last version was released (and I presented at [JuliaCon 2019](/work/juliacon-2019/)). This rework is in fact part of my new year's resolution, which is about "writing more code to deliver actual values in the form of products".

Working on recommender systems in the scientific computing-focused programming language always brings a fresh perspective, and the experience enables me to rethink of *how recommender interfaces should be* in terms of e.g., type, hyper-parameter representation, function naming, computational efficiency; in our day-to-day work as a developer, it's easy to overlook such essential aspects when we aggressively leverage well-developed application-oriented tools such as scikit-learn and Spark MLlib.

In this release, there are three key updates I would like to highlight and want you to think of.

### What "missing" means in the context of recommender

When it comes to implementing recommender systems, handling missing values in vectors and matrices (or tensors, in general) is indeed one of the most important challenges. In practice, the missing values in user-item data could have multiple different meanings, for instance. It could be a case that a user simply hasn't been exposed to the item yet (truly missing observation). Or, on the other hand, they did see it but intentionally ignored the item (negative feedback). Thus, thinking carefully about the special cases is a common problem the developers encounter.

In Julia, there are multiple ways to represent "this is not an actual value that the element is supposed to be": `missing`, `nothing`, `NaN`, and `undef`.

Recommendation.jl v0.3.0 used `NaN` without thinking much about the point, but I had an impression that this design choice was semantically incorrect; `NaN` is returned by `0 / 0`, for example, and the value explicitly represents "something went wrong". Meanwhile, `undef` represents uninitialized values that should eventually be fulfilled in some ways, which is actually tricky to deal with and also semantically different from what we are looking for in the context of user-item interaction matrix.

Therefore, I decided to leverage Julia's special-purpose types, `Missing` and `Nothing`, for our particular use case. Both represent "unknown" but could be used in different ways:

- `Missing` is mainly for model parameters, which should exist but have not been calculated yet.
- Input data is expected to use `Nothing` as an explicit indication of "no value".

Both values are eventually filled by zero in the current implementation, but there is certainly a room for improvement e.g., filling by means, considering positive-only feedback recommendation techniques. Regardless, I believe staying away from `NaN` is an important step the recommender implementation needed to take.

See [this stackoverflow answer](https://stackoverflow.com/questions/61936371/usage-and-convention-differences-between-missing-nothing-undef-and-nan-in-jul) for more thoughts.

### Data typing

Beyond the conventional deterministic `Float64` type, the library has generalized a value type associated with an user-item event (e.g., click, purchase, frequency, rating) as `Infinite` as follows:

```julia
Infinite = Union{AbstractFloat, Integer}

type Event
   user::Integer
   item::Integer
   value::Infinite
end
```

Importantly, both `AbstractFloat` and `Integer`, as well as their union `Infinite`, are abstract types. The fact makes the interface applicable to a wider range of datasets. What "value" indicates differs depending on a dataset, and the possibility includes not only `missing` and floating point numbers but signed and unsigned integers.

For data-driven applications in general, setting proper expectation to the types is critical so that all the subsequent numerical computations run correctly. From that perspective, in Julia, [ScientificTypes.jl](https://juliaai.github.io/ScientificTypes.jl/dev/) is currently inspiring me to dig deep into the problem. They attached proper semantics to the standard types, and it empowers applications to be more usable, readable, and maintainable.

I would try to keep increasing the type coverage including non-trivial string representations, and Recommendation.jl may eventually use ScientificTypes.jl as its dependency.

### Factorization Machines

Last but not least, I have finally implemented and merged Factorization Machines, a polynomial regression-based general predictor widely used by machine learning and recommendation communities. In fact, when I presented Recommendation.jl at JuliaCon 2019, several audiences reached out to me and asked for supporting the algorithm in the package. I did a quick implementation afterward, but it had stayed as a pull request for a while.

Currently, the basic combination of least squares and SGD-based optimization is the only option, but I will definitely support ranking loss along with the extension of how to handle/represent missing/numeric values as discussed above.

Speaking of supported algorithms, I'm currently thinking of limiting the complexity to Factorization Machines at most. I originally implemented Recommendation.jl as a collection of basic recommendation techniques mostly for the educational sake, so I would like to spend more time on sophistication and generalization rather than complication and over-optimization.

Ultimately, performance improvement is the biggest topic I personally want to invest more effort on. Interpretable, semantically meaningful design of code sometimes (and unnecessarily, in many cases) sacrifices computational efficiency. Since Julia has been best known as an efficient programming language, it's worth thinking deeply about the efficient use of language features.


