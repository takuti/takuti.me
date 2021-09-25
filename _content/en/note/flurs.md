---
categories: [Recommender Systems, Machine Learning, Programming]
date: 2017-01-21
keywords: [library, flurs, recommendation, feature, recommenders, techniques, julia,
  implementing, unlike, ready]
lang: en
recommendations: [/note/hello-faust/, /note/recommendation-julia/, /note/recommendation-julia-documenter/]
title: 'FluRS: A Python Library for Online Item Recommendation'
---

Last week, I introduced a Julia package for recommender systems: [Recommendation.jl: Building Recommender Systems in Julia](http://takuti.me/note/recommendation-julia/).

However, its functionality is still low, and I argued that implementing more powerful recommendation techniques and `update()` function is important. Thus, this article provides **[FluRS](https://github.com/takuti/flurs/)**, another open-sourced library for recommendation. Unlike **Recommendation.jl**, this recommender-specific library is written in Python from a practical point of view.

The initial version (v0.0.1) of **FluRS** is already published to PyPI. You can install and use the library by:

```sh
$ pip install flurs
```

This article simply describes basic ideas and concepts behind the implementation. See the README file to learn how to use the library.

### Python for recommendation

In a context of recommendation, one of the most popular open-source libraries written in Python is [fastFM](https://github.com/ibayer/fastFM), a library for *factorization machine* (FM) which is a state-of-the-art flexible factorization model. However, fastFM is actually a more generic library for FM-based prediction; it can be used for various applications such as, but not limited to recommendation.

Although there are several recommender-specific packages in the other programming languages like [LensKit](https://github.com/lenskit/lenskit) and [LibRec](https://github.com/guoguibing/librec) running in the Java virtual machine, and [MyMediaLite](https://github.com/zenogantner/MyMediaLite) written in C\#, Python implementation and related research papers do not exist to the best of my knowledge. Furthermore, incremental updating (i.e., `update()` method) of recommendation engines is a less well-developed feature compared to batch training functions. Hence, I developed the new Python library for online, incremental recommendation named **FluRS**.

### Recommendation algorithms

Currently, **FluRS** supports the following (incremental) recommendation algorithms.

- **Incremental Collaborative Filtering** (UserKNN)
  - M. Pepagelis et al. **Incremental Collaborative Filtering for Highly-Scalable Recommendation Algorithms**. In *Foundations of Intelligent Systems*, pp. 553–561, Springer Berlin Heidelberg, 2005.
- **Incremental Matrix Factorization** (MF)
  - J. Vinagre et al. **Fast Incremental Matrix Factorization for Recommendation with Positive-only **. In *Proc. of UMAP 2014*, pp. 459–470, July 2014.
- **Incremental Matrix Factorization with BPR optimization** (BPRMF)
  - S. Rendle et al. **BPR: Bayesian Personalized Ranking from Implicit Feedback**. In *Proc. of UAI 2009*, pp. 452–461, June 2009.
- **Incremental Factorization Machines** (FM)
  - T. Kitazawa. **Incremental Factorization Machines for Persistently Cold-Starting Online Item Recommendation**. [arXiv:1607.02858 [cs.LG]](https://arxiv.org/abs/1607.02858), July 2016.
- **Matrix Sketching** (OnlineSketch)
  - T. Kitazawa. **Sketching Dynamic User-Item Interactions for Online Item Recommendation**. In *Proc. of CHIIR 2017*, March 2017. (to appear)

### How to represent users, items and events

Similarly to **Recommendation.jl**, **FluRS** also encapsulates a user, item and corresponding event in entity classes as follows:

```py
import numpy as np


class User:

    def __init__(self, index, feature=np.array([0.])):
        self.index = index
        self.feature = feature


class Item:

    def __init__(self, index, feature=np.array([0.])):
        self.index = index
        self.feature = feature


class Event:

    def __init__(self, user, item, value, context=np.array([0.])):
        self.user = user
        self.item = item
        self.value = value
        self.context = context
```

`User` and `Item` can store their internal features as array (vector) representation for feature-based recommendation. An `Event` entity then consists of `user` and `item` entities, and `value` describing the feedback (e.g., rating). Additionally, `context` is an auxiliary vector which holds contextual information of the events such as time and location. Note that the features and contexts can be dummy 1-dimensional vectors in case the vectors are not explicitly specified by the arguments.

### Separating algorithms from recommender-specific implementations

Most importantly, this library separates algorithms from recommender-specific implementations which depend on the `User`, `Item` and `Event` entities. In particular, I defined two types of base classes for each of algorithms and recommenders as follows:

```py
class BaseModel:

    def __init__(self, *args):
        """Set the hyperparameters.
        """
        pass

    def init_params(self):
        """Initialize model parameters.
        """
        pass

    def update_params(self, *args):
        """Update model parameters.
        """
        pass
```

```py
class RecommenderMixin:

    def init_recommender(self, *args):
        # number of observed users
        self.n_user = 0

        # store user data
        self.users = {}

        # number of observed items
        self.n_item = 0

        # store item data
        self.items = {}

    def is_new_user(self, u):
        return u not in self.users

    def add_user(self, user):
        self.users[user.index] = {'known_items': set()}
        self.n_user += 1

    def is_new_item(self, i):
        return i not in self.items

    def add_item(self, item):
        self.items[item.index] = {}
        self.n_item += 1

    def update(self, event):
        pass

    def score(self, user, candidates):
        return

    def recommend(self, user, candidates):
        return
```

The former only provides model-specific functions such as updating model parameters, and the latter extends it to incremental recommender systems by injecting additional functions which use the `User`, `Item` and/or `Event` entities. The properties defined in the latter mixin continuously track observed users and items, and, if new users (items) are arrived, a recommender registers them on the internal dictionaries.

Generally speaking, performance of recommender systems is highly data-dependent, so we usually modify both underlying algorithms and recommenders' functionality depending on data. The separation in the library certainly makes the modifications easier.

In case we like to apply the dimensionality reduction techniques to input vectors, we only need to add some code to the recommender side's `update()` method and modify the entity-to-feature-vector converting procedure. Likewise, model-specific modification such as changing a loss function simply requires us to overwrite the `update_params()` method in a model class.

### Example: Factorization machines on FluRS

To give a concrete example, the **FluRS** library defines a FM-based recommender as follows:

```py
class FMRecommender(FactorizationMachine, FeatureRecommenderMixin):
```

Base classes `FactorizationMachine` and `FeatureRecommenderMixin` respectively inherit `BaseModel` and `RecommenderMixin`. Unlike `RecommenderMixin`, `FeatureRecommenderMixin` takes an additional argument `context` in a `score()` and `recommend()` method, because feature-based techniques allow us to represent an event as a feature vector by encoding and concatenating arbitrary variables.

### Conclusion

From a practical perspective, **FluRS** can be applicable to a wide variety of datasets thanks to the encapsulation of users, items and events; once the samples are converted into an array of `Event`, testing the online item recommendation techniques on own data should be easy for **FluRS**. In addition, since algorithms and recommenders are separately implemented in the library, both extending the ready-made techniques and implementing new kind of recommenders are straightforward on the library.

In terms of evaluation and further modifications, our library equips several metrics and utility functions for the dimensionality reductions, so **FluRS** can also be a useful toolkit for feature-based and/or top-$N$ recommendation.

However, at the same time, efficiency of the library is still inadequate. Therefore, following [the fastFM's highly efficient core implementation written in C](https://github.com/ibayer/fastFM-core) is one possible future direction.