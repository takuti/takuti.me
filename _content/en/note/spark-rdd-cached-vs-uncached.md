---
categories: [Programming]
date: 2017-04-16
lang: en
title: Comparison of Running Time of Cached/Uncached Spark RDD
keywords: [transformation, scala, rdd, operations, distributed, rdds, collections,
  spark, map, filter]
recommendations: [/note/coursera-scala-capstone/, /note/hivemall-pyspark/, /note/machine-learning-product/]
---

**Resilient Distributed Dataset** (RDD) is a distributed parallel data model in Spark. The model enables us to think of our distributed data like a single collection. In this article, I introduce some basics and show experimental result which clearly demonstrates the strength of RDD.

First and foremost, there are two different types of operations for RDD: ***transformation*** and ***action***.

### Type I: Transformation

**Transformation** corresponds to Scala transformers such as `map()` and `filter()`; we can apply both `map()` and `filter()` operations for RDDs in a similar way to the standard Scala collections.

In the Scala collections, this kind of operations return a new collection as:

```scala
scala> Seq(1, 2, 3).map(_ * 10)
res: Seq[Int] = List(10, 20, 30)
```

In RDDs, transformation similarly behaves; a new RDD will be returned as a result of transformation.

However, there is a huge difference between Scala collections and RDDs: result of transformation is *NOT immediately* computed. That is, transformation stands on **laziness**.

In case that we have a RDD which contains same values as the above example, `rdd.map()` does not return any "collections":

```scala
scala> val rdd: RDD[Int] = sc.parallelize(Seq(1, 2, 3))
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[5] at parallelize at <console>:20

scala> rdd.map(_ * 10)
res: org.apache.spark.rdd.RDD[Int] = MapPartitionsRDD[6] at map at <console>:22
```

Note that, if you want to compute RDD and convert it to Scala collection, you can use `collect()` operation as follows.

```scala
scala> rdd.map(_ * 10).collect()
res: Array[Int] = Array(10, 20, 30)
```

### Type II: Action

**Action** corresponds to Scala accessors e.g., `fold()` and `aggregate()`, and the usage is very similar to what Scala collections do.

Importantly, in contrast to transformations, actions return something like value.

```scala
scala> Seq(1, 2, 3).fold(0)(_ + _)
res: Int = 6
```

```scala
scala> val rdd: RDD[Int] = sc.parallelize(Seq(1, 2, 3))
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[5] at parallelize at <console>:20

scala> rdd.fold(0)(_ + _)
res: Int = 6
```

It is obvious that actions are evaluated **eager**; result is *immediately* computed.

### Uncached vs Cached

Even though you applied transformations for RDD, nothing happens until actions are kicked because transformations are lazy operations. This fact indicates that actions could be a bottleneck in code which handles RDDs.

In a context of machine learning, since iteration over large-scale data is necessary, same operations are repeatedly executed until convergence. To give an example, for an algorithm which iteratively runs `rdd.filter().map().count()`, all of three operations `filter()`, `map()` and `count()` are internally repeated. So, when size of data in RDD is huge, this iterations will be surprisingly slow.

In order to run such repeatedly-computed transformations more efficiently, RDD has a special operation named `parallel()` (or, `persist()`). If you define a RDD with the `cache()` operation, RDD internally caches the result of transformations, and hence iterative `count()` operations should be much faster than the uncached case.

```scala
val rddUncached = rdd.filter().map()
for (i <- 0 to n) { // inefficient :(
	// recompute `filter` -> `map` -> `count` in each time
	rddUncached.count()
}
```

```scala
val rddCached = rdd.filter().map().cache()
for (i <- 0 to n) { // efficient :)
	// result of `filter` -> `map` is internally cached
	rddCached.count()
}
```

### Experiment

Let's finally check if cached RDD is truly faster than uncached one.

1) Define a Spark context and dummy data `randomList` which consists of 10k random integers:

```scala
val conf: SparkConf = new SparkConf().setMaster("local").setAppName("RDDTest")
val sc: SparkContext = new SparkContext(conf)

val rng: Random = new Random
val randomList: List[Int] = (for (i <- 1 to 10000) yield rng.nextInt).toList
```

2) Create a function which measures running time (cf. [Easily measuring code execution time in Scala](http://biercoff.com/easily-measuring-code-execution-time-in-scala/)):

```scala
def time[R](block: => R): R = {
	val t0 = System.nanoTime()
	val result = block
	val t1 = System.nanoTime()
	println("Elapsed time: " + ((t1 - t0) / 1000000000.0) + " sec")
	result
}
```

3) Compare running time of the same operations over cached/uncached RDD:

```scala
for (i <- 1 to 3) { // try 3 times
	println("========")
	println("Uncached")
	println("========")
	time {
		val rdd: RDD[Int] = sc.parallelize(randomList).map(f)
		for (i <- 1 to 1000) rdd.count()
	}

	println("========")
	println("Cached")
	println("========")
	time {
		val rddCached: RDD[Int] = sc.parallelize(randomList).map(f).cache()
		for (i <- 1 to 1000) rddCached.count()
	}
}
```

Here, mapped function `f` is a dummy function which takes a long-time:

```scala
def f(v: Int): Int = {
	for (i <- 1 to 10000) {}
	v
}
```

Note: In view of unrelated optimization done by Scala itself, our code tries the same procedure three times.

Woo-hoo! As a consequence, we can observe that the cached RDD is much more efficient even for the same data and same number of iterations:

```
========
Uncached
========
Elapsed time: 40.727146166 sec
========
Cached
========
Elapsed time: 3.947885796 sec
```

```
========
Uncached
========
Elapsed time: 37.857984933 sec
========
Cached
========
Elapsed time: 3.149896662 sec
```

```
========
Uncached
========
Elapsed time: 35.778371576 sec
========
Cached
========
Elapsed time: 3.6294217 sec
```

Complete code is available at: [RDDTest.scala](https://github.com/takuti-sandbox/tmp/blob/644d7c6e85c7f111b0f340ece37bc1d4434bb5e5/scala/src/main/scala/rdd/RDDTest.scala).

### Conclusion

Spark optimization basically relies on laziness, and caching transformation is one of the simplest and most effective ways to optimize your code utilizing RDDs.

The contents of this article is based on an online course "[Big Data Analysis with Scala and Spark](https://www.coursera.org/learn/scala-spark-big-data)". This well-structured course is really interesting and exciting from a practical point of view :)