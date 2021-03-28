---
categories: [Recommender Systems, Programming]
date: 2017-01-14
keywords: [recommendation, julia, age, factorization, package, waiting, tensor, returns,
  registered, promising]
lang: en
recommendations: [/note/recommendation-julia-documenter/, /note/juliacon-2019/, /note/flurs/]
title: 'Recommendation.jl: Building Recommender Systems in Julia'
---

I have recently published [Recommendation.jl](https://github.com/takuti/Recommendation.jl), a Julia package for recommender systems. The package is already registered in [METADATA.jl](https://github.com/JuliaLang/METADATA.jl), so it can be installed by:

```sh
$ julia
julia> Pkg.add("Recommendation")
```


Last year, I took ***Introduction to Recommender Systems***, an online course created by University of Minnesota, on Coursera. Although the course assignments originally require us to use spreadsheet (on Google Drive or MS Excel), I personally solved all of them by programming in Julia. Recommendation.jl is created as a result of the coursework assignments.

This article explains about the details of Recommendation.jl. If you are interested in functionality and usage, you can refer to README of the repository. In case you have comments or suggestions for future update, issues and/or pull requests are very welcome!

*Note: The online course is now opening as [Recommender Systems Specialization](https://www.coursera.org/specializations/recommender-systems). Course contents might be different from the previous version that I have completed.*

### Why Julia?

[Julia](http://julialang.org/) is a relatively new programming language developed by computer scientists at MIT, and the language mainly focuses on high-performance scientific computing by utilizing the just-in-time compiler. Conventionally, [MATLAB](http://www.mathworks.com/) has been widely used for numerical computing, but it is in some sense inefficient proprietary software. Thus, open-sourced Julia's efficient implementation is getting the attention of research communities in these days: *[Julia: A Fast Language for Numerical Computing](https://sinews.siam.org/Details-Page/julia-a-fast-language-for-numerical-computing-1)*.

We can readily use various scientific algorithms on MATLAB and Julia by integrating third-party packages, and their syntax dedicated to vector and matrix computations definitely accelerates algorithm development both in industry and academia. However, in terms of recommender systems, there are currently no effective Julia packages which enable us to make fundamental CF, SVD and MF-based recommendation. Therefore, I developed a basic toolkit for recommender systems in Julia.

Static analysis on a local machine with classical techniques is essentially important as the first step for building your own recommender systems, and the package helps you to analyze own user-item data. Additionally, since the implementation and Julia itself are highly flexible, implementing new algorithms on the package should be easy.

### Basic structure

In general, recommender systems somehow handle a number of events which represents user-item interactions. So, our package describes each event as an `Event` composite type:

```julia
type Event
    user::Int
    item::Int
    value::Float64
end
```

A field `value` can be unary or arbitrary real number depending on the feedback types.

In order to represent a series of `Event`, we define a data accessor as follows:

```julia
immutable DataAccessor
    events::Array{Event,1}
    R::AbstractMatrix
    user_attributes::Dict{Int,Any} # user => attributes
    item_attributes::Dict{Int,Any} # item => attributes
end
```

This abstraction allows us to interchangeably access to an array of `Event` and user-item matrix. Notice that user and item attributes can be stored as key-value pairs on `DataAccessor` for content-based and feature-based recommenders.

Once a dataset is converted into a data accessor, we can launch various kinds of recommenders on the package. Importantly, all of the recommendation techniques implemented in the package are based on an abstract base type `Recommender`, and the following functions should be implemented on each recommender:

- `build(rec::Recommender; kwargs...)`
	- Building a recommendation engine from a data accessor.
- `check_build_status(rec::Recommender)`
	- Check whether recommender is already built before making recommendation.
- `predict(rec::Recommender, u::Int, i::Int)`
	- Making prediction for a given user-item pair.
- `ranking(rec::Recommender, u::Int, i::Int)`
	- Computing a ranking score for a given user-item pair.
- `recommend(rec::Recommender, u::Int, k::Int, candidates::Array{Int})`
	- Making top-$k$ recommendation for a given user from a list of item candidates.

In particular, what `recommend()` does is to compute ranking scores for all possible user-item pairs and return top-$k$ highest-ranked items. Since this recommendation procedure is always same regardless of recommenders, the function is precomposed in the package:

```julia
function recommend(rec::Recommender, u::Int, k::Int, candidates::Array{Int})
    d = Dict{Int,Float64}()
    for candidate in candidates
        score = ranking(rec, u, candidate)
        d[candidate] = score
    end
    sort(collect(d), by=tuple->last(tuple), rev=true)[1:k]
end
```

The `recommend()` function actually works correctly, but the implementation is not efficient enough; computing the ranking scores one-by-one might be computationally expensive, especially for the massive item candidates. Hence, the function should be improved in the future by taking more efficient approaches such as parallelization.

Another common function is `check_build_status()`. The function checks a recommenders' build state and throws an error if it is still not built:

```julia
function check_build_status(rec::Recommender)
    if !haskey(rec.states, :is_built) || !rec.states[:is_built]
        error("Recommender $(typeof(rec)) is not built before making recommendation")
    end
end
```

### Implementing a recommendation algorithm on Recommendation.jl

To give an example, the following code demonstrates implementation of the simple popularity-based recommender:

```julia
immutable MostPopular <: Recommender
    da::DataAccessor
    scores::AbstractVector
    states::States
end

MostPopular(da::DataAccessor, hyperparams::Parameters=Parameters()) = begin
    n_item = size(da.R, 2)
    MostPopular(da, zeros(n_item), States(:is_built => false))
end

function build(rec::MostPopular)
    n_item = size(rec.da.R, 2)

    for i in 1:n_item
        rec.scores[i] = countnz(rec.da.R[:, i])
    end

    rec.states[:is_built] = true
end

function ranking(rec::MostPopular, u::Int, i::Int)
    check_build_status(rec)
    rec.scores[i]
end
```

The `MostPopular` recommender type is initialized by a data accessor, and a recommendation engine can be built by counting the number of nonzero elements in each column (i.e., item) of a user-item matrix. Ultimately, the frequency is the ranking scores which determine the most promising items.

It should be noticed that `predict()` does not necessarily to be implemented because `recommend()` internally uses scores obtained from `ranking()`. In case only `predict()` is implemented on a recommender, `ranking()` works as an alias of the `predict()` function by default:

```julia
function predict(rec::Recommender, u::Int, i::Int)
    error("predict is not implemented for recommender type $(typeof(rec))")
end

function ranking(rec::Recommender, u::Int, i::Int)
    check_build_status(rec)
    predict(rec, u, i)
end
```

The separation of `predict()` and `ranking()` functions is based on [LibRec](http://www.librec.net/), a Java library for recommender systems.

Consequently, when researchers and engineers like to implement new recommendation techniques in Julia by using the Recommendation.jl library, they simply need to care about the following three points:

- How to build a recommender from a data accessor,
- How to make prediction for a given user-item pair,
- How to compute a ranking score for a given user-item pair,

in addition to converting own data into a data accessor. The flexible data accessors and Julia's dynamic type systems clearly make the package extensible. Note that the idea of the flexible implementation originally comes from [LensKit](http://lenskit.org/), a recommender-specific toolkit running in JVM. LensKit is fully taking advantage of flexibility achieved by dependency injection.

### Example of matrix-factorization-based recommendation

Integrating a data accessor, recommender and metric eventually enable us to compute the accuracy of recommendation. Here, I give an example of the whole procedure using Recommendation.jl:

```julia
using Recommendation

const n_user = 5
const n_item = 10

# Create a data accessor from events
events = [Event(1, 2, 1), Event(3, 2, 1), Event(2, 6, 4)]
da = DataAccessor(events, n_user, n_item)

# Initialize a MF-based recommender with the data accessor
# The number of latent factors is set to 2
recommender = MF(da, Parameters(:k => 2))

# Build the MF-based recommender based on the SGD optimization
build(recommender, learning_rate=15e-4, max_iter=100)

# Make top-k recommendation for a user from a set of item candidates
u = 4
k = 2
candidates = [i for i in 1:n_item] # all items
recommend(recommender, u, k, candidates)
```

`recommend()` eventually returns tuples of sorted item IDs and their scores.

### What's next

This article has introduced the basic concept underlying my new Julia package for recommender systems.

Currently, the package has very limited functions what I have learnt from the "Introduction to Recommender Systems" course. More powerful recommendation techniques (e.g., Tensor Factorization, Factorization Machines) should be implemented in the future. Moreover, creating `update()` method is another promising direction in order to test recommendation algorithms in an incremental fashion.

In terms of efficiency, current implementation is naive and does not take advantage of Julia's performance. This view should be considered more to improve feasibility of the package. Meanwhile, comparison with the other recommender-specific libraries is important.

Recommendation.jl is still in version 0.0.1. Keep waiting till new releases and further improvements!