---
layout: post
title: "Parallel Programming vs. Concurrent Programming"
lang: en
date: 2017-02-25
---

What is the difference between **parallel programming** and **concurrent programming**? There is a lot of definitions in the literature.

### "Executing simultaneously" vs. "*in progress* at the same time"

 For instance, **[The Art of Concurrency](http://shop.oreilly.com/product/9780596521547.do)** defines the difference as follows:

> A system is said to be *concurrent* if it can support two or more actions *in progress* at the same time. A system is said to be *parallel* if it can support two or more actions executing simultaneously. The key concept and difference between these definitions is the phrase "in progress."

This definition says that, in concurrent systems, multiple actions can be *in progress* (may not be executed) at the same time. Meanwhile, multiple actions are simultaneously executed in parallel systems. In fact, concurrency and parallelism are conceptually overlapped to some degree, but "in progress" clearly makes them different.

Even though such definition is concrete and precise, it is not intuitive enough; we cannot easily imagine what "in progress" indicates.

Recently, I am taking an online course [Parallel Programming](https://www.coursera.org/learn/parprog1/) on Coursera, and the course gave me more intuitive and easy-to-understand definition of parallel and concurrent programming as follows.

### Parallel: Efficiency is its main concern

When we consider parallel programming, programs use parallel hardwares to **execute computation more quickly**.

Here, "parallel hardwares" could be:

- multi-core processors
- symmetric multiprocessors
- graphics processing unit (GPU)
- field-programmable gate arrays (FPGAs)
- computer clusters

in wide-ranging scale.

More concretely, parallel programming requires us to think about:

- How does code divide original huge problem into smaller sub-problems? 
- Which is the optimal use of parallel hardware?

Since parallel programming strongly focuses on **speeding-up** computational time, applications such as matrix multiplication, data analysis, 3D rendering and particle simulation can be discussed in the paradigm.

### Concurrent: Modularity, responsiveness and maintainability are important

In parallel programming, multiple actions are strictly executed at the same time to improve efficiency. By contrast, multiple actions are not necessarily to be executed simultaneously in concurrent programming because of **user-side manageability**.

Concurrency cares about beyond efficiency, and our main concern is:

- When can an execution start?
- How can information exchange occur?
- How does code manage access to shared resources?

Well-organized practical applications such as web server, user interface and database should be implement in the concurrent paradigm. Even if parallelism is lost to some degree, **convenience** behind systems is more important in concurrent programming.

Distinguishing parallelism from concurrency is important to seek an appropriate way to solve large scale problems, but they are considered interchangeably in reality. The definitions provided by the online course are tremendously valuable to figure out the very similar but different two paradigms.