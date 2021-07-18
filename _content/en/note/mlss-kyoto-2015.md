---
categories: [Machine Learning]
date: 2015-10-03
images: ['https://res.cloudinary.com/takuti/image/upload/l_text:Open%20Sans_32:Machine%20Learning%20Summer%20School%202015%20Kyoto%20%23MLSSKYOTO,co_rgb:eee,w_800,c_fit/v1626628472/takuti_bgimyl.jpg']
keywords: [lecture, optimization, really, learning, learn, theoretical, professor,
  try, mathematica, aspects]
lang: en
recommendations: [/note/mlconf-sf-2018/, /note/phpcon-2015/, /note/learn-how-others-work/]
title: 'Machine Learning Summer School 2015 Kyoto #MLSSKYOTO'
---

Hi, I am takuti, a master's student in Japan. Currently, I am working on matrix factorization and approximation. Also, my research interests are in web engineering, mining and their applications such as recommender systems.

I have attended to [Machine Learning Summer School 2015 Kyoto](http://www.iip.ist.i.kyoto-u.ac.jp/mlss15/) (MLSS'15) from August 23 to September 4. This entry briefly reviews each of 14 exciting lectures in the summer school. Note that there might be mistakes in the content. In that case, please let me know via comments or [twitter](http://twitter.com/takuti).

Slides for the lectures are available at: http://www.iip.ist.i.kyoto-u.ac.jp/mlss15/doku.php?id=schedule

### TL;DR

https://twitter.com/takuti/status/636907107107803137

(with strong emphasis on regularization and LASSO)

![sensu](/images/jekyll/2015-10-03-sensu.jpg)
*MLSS Sensu*

### Convex Optimization

**Stephen P. Boyd, Stanford**

This is one of the most impressive lectures in MLSS'15 because Prof. Boyd provided us really interesting and stimulating lecture; it was like a show. He interactively discussed key ideas and specific applications of convex optimization problems. Also, thanks to [Convex Optimization Short Course](http://stanford.edu/~boyd/papers/cvx_short_course.html), we can easily learn and try to solve real convex optimization problems on our laptop after MLSS.

As mentioned in the above tweet, optimization problems are everywhere in machine learning field. How can we find optimal weights? Which cluster assignment is the best? What is the best approximation? All of the answers can be found from optimization problems. Hence, the MLSS'15 lecture schedule seems to be well-organized (that's why this lecture is the first one in this summer school).

**Next**: Try [Convex Optimization Short Course](http://stanford.edu/~boyd/papers/cvx_short_course.html)

### Concentration Inequalities

**Gábor Lugosi, Pompeu Fabra**

This topic seemed to be super advanced mathematics, and the lecture was really hard to follow. In particular, computer scientists who are familiar with engineering aspects were easily left behind, because we were not able to imagine specific applications from lots of equations/proofs.

While at the same time, I can feel how concentration inequalities, inequalities for bounding random fluctuations $P\\{Z \leq t\\}$, are important in machine learning field. In fact, modern machine learning techniques strongly depend on probabilistic approaches (random fluctuations), so importance of guarantees for the fluctuations is clear.

**Next**: Read [Concentration Inequalities: A Nonasymptotic Theory of Independence](http://www.amazon.com/Concentration-Inequalities-Nonasymptotic-Theory-Independence/dp/0199535256)

### Topics in Selective Inference

**Emmanuel Candès, Stanford**

His lecture started from a discussion about reliability of science. In my opinion, this was good introduction to show how selective inference can be an important field to discuss experimental results on so-called "BigData". Currently, we will first collect huge data before asking questions and planning experiments, so reliability of inference from BigData is a crucial problem.

I am especially interested in **Knockoff Machines**, a simple algorithm to select statistically favorable hypothesis from many different hypotheses. For the reliability of inference, we need to decrease **false discovery rate** (FDR), and Knockoff Machines allow us to select hypotheses which give low FDR. This algorithm is also promising in terms of feature selection. When we would like to choose better features from many different features, Knockoff Machines-like algorithm can choose features which give low false positives. In the future, I would like to survey on this application.

**Next**: Learn more about Knockoff Machines from the lecture slide and related online sources

### Probabilistic Programming

**Luc De Raedt, KU Leuven**

This lecture was really different from the others. At first, I was afraid of a term "programming"; I imagined this indicates something like "linear programming" stuff, but this was not true. The content focused on writing probabilistic code, especially in **ProbLog**, extension of Prolog. Since I am already familiar with Prolog, I really enjoyed the lecture.

One of the most important things of ProbLog is that this programming language can infer from predicates with uncertainty. When we tackle AI problems, programming languages need to deal uncertainty in it; that is, dealing uncertainty is important problem to represent human intuition.

**Next**: Try probabilistic programming in [ProbLog](https://dtai.cs.kuleuven.be/problog/)

### Submodular Functions

**Stefanie Jegelka, MIT**

I heard a term **submodular** many times before, but I did not know what submodular actually is. The answer was in this lecture; this lecture started from definition of set functions and submodularity with good intuitive examples. After such introduction, she gradually moved to mathematical details, optimization and approximation of submodular functions.

One of the most interesting applications I have learnt from this lecture is summarization. This idea assumes that summarization is just choosing subset of words from target article; that is, we can summarize articles by maximizing set function for words in terms of coverage or relevance. This idea is very interesting, and I am also interested in incremental summary updating and application to recommender systems. I would like to learn more about this field.

**Next**: Read one curious paper found on the web "[Streaming Submodular Maximization:
Massive Data Summarization on the Fly](http://las.ethz.ch/files/badanidiyuru14streaming.pdf)"

### Statistical and Computational Aspects of High-Dimensional Learning

**Philippe Rigollet, MIT**

We needed to highly focus on **Statistical and Computational Aspects** in the title. The content consisted of mathematical discussion in these aspects. Even though the professor first introduced well-known technique, Principal Component Analysis, I was not able to follow the lecture due to difficult mathematical discussion.

I was only able to understand what **high-dimensinal** setting is; high-dimensional setting is situation such that the number of parameters is much bigger than the number of observations. However, what is more concrete difference between high-dimensional learning and usual machine learning? What is the key idea in high-dimensional learning? Which points are new in the field? To grasp these points, I should learn more before listing this lecture.

**Next**: First and foremost, I need to review this lecture :(

### Learning Representations

**Lorenzo Rosasco, MIT / Genoa**

Data representation $$\mathbf{\Phi}$$ is $$X \rightarrow F$$, mapping data space $$X$$ to representation space $$F$$. Keeping in mind this point really helps us to understand a wide variety of ideas in the field. This course was really well-organized because the professor taught several different representations one-by-one and summarized them from practical viewpoint.

Representations discussed in the lecture were: Dictionary, Random Projection, Kernel and Deep Representation. All of them were scientifically stimulating, but which representation is appropriate to my problem? This lecture covered such practical points, and important thing is ***Good representation decreases complexity of samples***. Currently, I am curious about online dictionary learning, so this lecture was good introduction.

**Next**: Review dictionary learning from online sources such as [Sparse Coding Course](https://sites.google.com/site/kacstsparsecoding/), and its online setting

### Scalable Machine Learning

**Alexander J. Smola, CMU**

Are there anybody who are studying in engineering department? OK, it's time for you! 

Two-thirds of this lecture discussed computer and system architecture in the BigData era. Since I am definitely curious about engineering and applicational aspects in machine learning rather than theoretical, mathematical points, the lecture was quite exciting.

This course has three parts: (1) efficient machine learning on single machine, (2) distributed machine learning, and (3) system architecture for Deep Learning. The last part was pale compared to the others, because it was just overview of well-known recent studies on Deep Learning. During the introduction, the professor said things like ***You don't have to be a professional hardware researcher, but please care about the efficiency of memory usage***. This is very important point in recent large-scale machine learning.

**Next**: Check his lectures on [YouTube channel](https://www.youtube.com/user/smolix), and try Deep Learning techniques by my hand on cloud environment

![bamboo](/images/jekyll/2015-10-03-bamboo.jpg)
*In a weekend, I visited Arashiyama and saw famous bamboo forest.*

### Reinforcement Learning

**Csaba Szepesvári, Alberta**

Even though I can see many interesting articles and videos related to reinforcement learning on the web, I have never learnt about theoretical aspect of the technique. So, this field was a huge black box for me.

The professor said that reinforcement learning has all of machine learning problems such as regression, classification and density estimation. This is true; I confirmed this statement through the lecture. However, after taking this short course, my understanding of reinforcement learning is still unclear.

**Next**: Read [Algorithms for Rainforcement Learning](http://www.ualberta.ca/~szepesva/RLBook.html), free pdf written by the lecturer

### Machine Learning for Computer Vision

**Zaid Harchaoui, NYU/INRIA**

What kind of lecture are you expect from this title? Your thought is probably wrong. 

This lecture focused on some specific theories such as [Convolutional Kernel Networks](http://arxiv.org/abs/1406.3332) and Stochastic Gradient Descent, so we were not able to obtain practical techniques in computer vision. Of course, these theories are really important to realize better application, but the title "Machine Learning for Computer Vision" was definitely inappropriate.

After this course, I shortly discussed with one Japanese researcher who is working on computer vision in a research institute. He also said the same things, and he actually expected more practical topic like 3D reconstruction. Due to this disappointing situation, I was not able to enjoy this lecture.

**Next**: Learn and try Convolutional Neural Networks and Convolutional Kernel Networks

### Tensor Decompositions

**Ryota Tomioka, TTI Chicago**

As I said at the beginning, I am currently working on machine learning for matrices, so I really looked forward to this lecture. And, this lecture was actually scientifically stimulating for me. Most importantly, the lecture was well-organized and really easy to follow. For example, he used enough time to explain what rank of matrices is, and he repeatedly emphasized this fundamental point is important to understand tensors. 

However, tensor decomposition and its related theory/application are wide-ranging, and, in this lecture, the professor just focused on one of them, theoretical analysis of tensor decomposition. When we need to use tensors in a practical problem, you should learn more from different studies beyond this lecture.

**Next**: Try tensor decomposition on real-world data set and learn more applications

### Stochastic Optimization

**Taiji Suzuki, Tokyo Tech**

Since I am interested in online learning, Stochastic Gradient Descent is one of my curious topics. However, this lecture has too much mathematical formulas. I was not able to follow at all.

In fact, most lectures in MLSS strongly emphasized theoretical, mathematical aspects of recent machine learning studies, but this lecture was too much. I would like to learn more about this topic from the other sources.

**Next**: Understand Stochastic Gradient Descent theoretically

### Large Scale Deep Learning

**Vincent Vanhoucke, Google**

This was very good introductory lecture on Neural Networks and Deep Learning. We were able to obtain brief overview of recent significant achievements and theoretical basics in the field.

Most importantly, he first emphasized Deep Learning is not the only way to get sufficient results in real-world machine learning problems. Actually, on [Kaggle](https://www.kaggle.com/), other techniques quite often win. So, try Rogistic Regression, Gradient Boosting and Random Forest first! This is the message from the lecture.

**Next**: Review basic techniques (rogistic regression, random forest, gradient boosting) and attend data competision with them :)

### Statistical Guarantees in Optimization

**Martin Wainwright, Berkeley**

The last lecture focused on sketching, and first started from **Johnson–Lindenstrauss lemma**. During MLSS, since some professors introduced J-L lemma in their lecture, I understood how the lemma has an important role to approximate data. So, this notice strongly motives for learning these theoretical fundamentals.

He introduced his latest work called [Newton Sketch](http://arxiv.org/abs/1505.02250) in the lecture. This paper seems very interesting and exciting, so I would like to read later.

**Next**: Learn more about statistical guarantees with starting from Johnson–Lindenstrauss lemma, and read [Newton Sketch](http://arxiv.org/abs/1505.02250)

### Conclusion

Overall, MLSS was really, really exciting two weeks. We were able to briefly see all of machine learning field, and these knowledge definitely leads a new research idea!

MLSS also posed a shade of anxiety to us by difficult math, but I guess we do not have to think too much about that. In machine learning, key ideas and essential problems we need to solve are usually quite simple. So, when we tackle own problem, let us start from the simplest approach, and gradually extend it.

Finally, one thing I would like to introduce is one cool podcast channel talking about machine learning called [Talking Machines](http://www.thetalkingmachines.com/). I found this podcast after MLSS, and listening the excellent talks is intellectually stimulating. If you have not subscribed it yet, go ahead!

![masu](/images/jekyll/2015-10-03-masu.jpg)
*MLSS Masu, Japanese traditional sake glass*