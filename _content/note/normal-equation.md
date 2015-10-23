---
layout: post
title: "How to Derive the Normal Equation"
lang: en
date: 2015-04-21
---

In the linear regression tasks, the normal equation is widely used to find optimal parameters. However, [Pattern Recognition and Machine Learning](http://www.springer.com/gp/book/9780387310732) (RPML), one of the most popular machine learning textbooks, does not explain details of the derivation process. So, this article demonstrates how to derive the equation.

### Linear regression model

We define linear regression model as:

$$
y = \textbf{w}^{\mathrm{T}}\boldsymbol{\phi}(\textbf{x})
$$

for a input vector $\textbf{x}$, base function $\boldsymbol{\phi}$ and output $y$.

The main task is to find an optimal parameter $\textbf{w}$ from $N$ learning data sets, $(\textbf{x}_1, t_1), (\textbf{x}_2, t_2), \ldots, (\textbf{x}_N, t_N)$. As a result of such learning step, we can predict output for any input $\textbf{x}$.

### Least squares method

How can we estimate an optimal parameter $\textbf{w}$? The answer is quite simple: minimization of the total prediction error. When we already have parameters, the total prediction error for the $N$ learning data may be computed by $\sum_{n=1}^{N} (t_n-\textbf{w}^{\mathrm{T}}\boldsymbol{\phi}(\textbf{x}_n))$. Is it correct?

Unfortunately, this formula has two problems. First, if learning data such that $t_n-\textbf{w}^{\mathrm{T}}\boldsymbol{\phi}(\textbf{x}_n)< 0$ exists, above formula does not represent "total error". Second, since the formula is linear for $\textbf{w}$, we cannot minimize it. Thus, squared error function $E(\textbf{w})$ is considered as:

$$
E(\textbf{w}) = \sum_{n=1}^{N} (t_n-\textbf{w}^{\mathrm{T}}\boldsymbol{\phi}(\textbf{x}_n))^2.
$$

$E(\textbf{w})$ is a quadratic function, and it will be concave up. So, we can minimize it by finding $\textbf{w}$ which satisfies $\frac{\partial E}{\partial \textbf{w}} = 0$.

Note that, in the PRML, squared error function is represented as $E(\textbf{w}) = \frac{1}{2} \sum_{n=1}^{N} (t_n-\textbf{w}^{\mathrm{T}}\boldsymbol{\phi}(\textbf{x}_n))^2$ with mysterious $\frac{1}{2}$, but it just deletes $2$ in $\frac{\partial E}{\partial \textbf{w}}$. Hence, the coefficient is not so important to understand the normal equation.

### Normal equation

For the reasons that I mentioned above, we want to obtain $\frac{\partial E}{\partial \textbf{w}}$. For better understanding, I will first check the result of vector derivation for a small example. When we have just one learning data, and input vector has two dimensions, the squared error function is:

$$
E(\textbf{w}) = \sum_{n=1}^{1} (t_n-\textbf{w}^{\mathrm{T}}\boldsymbol{\phi}(\textbf{x}_n))^2
= \left( t_1- \left(
    \begin{array}{c}
      w_0 \\\\
      w_1
    \end{array}
  \right)^{\mathrm{T}}
  \left(
    \begin{array}{c}
      \phi_0 \\\\
      \phi_1
    \end{array}
  \right)\right)^2
= (t_1 - w_0\phi_0 - w_1\phi_1)^2.
$$

Also,

$$
\frac{\partial E}{\partial \textbf{w}}
= \left(
    \begin{array}{c}
      \frac{\partial E}{\partial w_0} \\\\
      \frac{\partial E}{\partial w_1}
    \end{array}
  \right).
$$

For instance,

$$
\begin{array}{ccl}
\frac{\partial E}{\partial w_0} &=& 2(t_1 - w_0\phi_0 - w_1\phi_1) \cdot \frac{\partial}{\partial w_0}(t_1 - w_0\phi_0 - w_1\phi_1) \\\\
&=& 2(t_1 - w_0\phi_0 - w_1\phi_1) \cdot (-\phi_0).
\end{array}
$$

As a consequence,

$$
\frac{\partial E}{\partial \textbf{w}}
= -2(t_1 - w_0\phi_0 - w_1\phi_1) \left(
    \begin{array}{c}
      \phi_0 \\\\
      \phi_1
    \end{array}
  \right).
$$

By extending this simple example to arbitrary $N$ and dimensions,

$$
\begin{array}{ccl}
\frac{\partial E}{\partial \textbf{w}}
&=& -2 \sum_{n=1}^{N} ((t_n-\textbf{w}^{\mathrm{T}}\boldsymbol{\phi}_n)\cdot\boldsymbol{\phi}_n ) \\\\
&=&-2 \sum_{n=1}^{N} ((t_n-\textbf{w}^{\mathrm{T}}\boldsymbol{\phi}_n)\cdot\boldsymbol{\phi}_n ) \\\\
&=& -2 \sum_{n=1}^{N} t_n\boldsymbol{\phi}_n +2 \sum_{n=1}^{N}(\textbf{w}^{\mathrm{T}}\boldsymbol{\phi}_n ) \cdot \boldsymbol{\phi}_n \\\\
&=& -2 \sum_{n=1}^{N} t_n\boldsymbol{\phi}_n +2 \left(\sum_{n=1}^{N}\boldsymbol{\phi}_n \boldsymbol{\phi}_n^{\mathrm{T}}\right)\textbf{w},
\end{array}
$$

with $\boldsymbol{\phi}(\textbf{x}_n)=\boldsymbol{\phi}_n$. Importantly, since $\textbf{w}^{\mathrm{T}}\boldsymbol{\phi}_n$ is scalar, exchangeable parts exist as: $\textbf{w}^{\mathrm{T}}\boldsymbol{\phi}_n = \boldsymbol{\phi}_n^{\mathrm{T}}\textbf{w}$, and $(\boldsymbol{\phi}_n^{\mathrm{T}}\textbf{w})\cdot\boldsymbol{\phi}_n = \boldsymbol{\phi}_n \cdot (\boldsymbol{\phi}_n^{\mathrm{T}}\textbf{w}) = (\boldsymbol{\phi}_n\boldsymbol{\phi}_n^{\mathrm{T}})\cdot\textbf{w}$.

Next, we solve the equation for $\textbf{w}$ as:

$$
\begin{array}{rcl}
-2 \sum_{n=1}^{N} t_n\boldsymbol{\phi}_n +2 \left(\sum_{n=1}^{N}\boldsymbol{\phi}_n \boldsymbol{\phi}_n^{\mathrm{T}}\right)\textbf{w} &=& 0 \\\\
\left(\sum_{n=1}^{N}\boldsymbol{\phi}_n \boldsymbol{\phi}_n^{\mathrm{T}}\right)\textbf{w} &=& \sum_{n=1}^{N} t_n\boldsymbol{\phi}_n \\\\
\textbf{w} &=& \left(\sum_{n=1}^{N}\boldsymbol{\phi}_n \boldsymbol{\phi}_n^{\mathrm{T}}\right)^{-1}\sum_{n=1}^{N} t_n\boldsymbol{\phi}_n.
\end{array}
$$

Additionally, the PRML introduces __design matrix__ by:

$$
\boldsymbol{\Phi} = \left(
    \begin{array}{cccc}
      \phi_0(\textbf{x}_1) & \phi_1(\textbf{x}_1) & \ldots & \phi_{M-1}(\textbf{x}_1) \\\\
      \phi_0(\textbf{x}_2) & \phi_1(\textbf{x}_2) & \ldots & \phi_{M-1}(\textbf{x}_2) \\\\
      \vdots & \vdots & \ddots & \vdots \\\\
      \phi_0(\textbf{x}_N) & \phi_1(\textbf{x}_N) & \ldots & \phi_{M-1}(\textbf{x}_N)
     \end{array}
  \right)
$$

for $M$, dimensions of input vector. It can be simply written as
$\boldsymbol{\Phi} = \left[
\boldsymbol{\phi_1} \
\boldsymbol{\phi_2}
\ldots
\boldsymbol{\phi_N}\right]$. Therefore, we can easily confirm $\sum_{n=1}^{N}\boldsymbol{\phi}_n \boldsymbol{\phi}_n^{\mathrm{T}} = \boldsymbol{\Phi}^{\mathrm{T}}\boldsymbol{\Phi}$, and $$\sum_{n=1}^{N} t_n\boldsymbol{\phi}_n = \boldsymbol{\Phi}^{\mathrm{T}}\textbf{t}$$.

Finally, we get the normal equation with the design matrix:

$$
\textbf{w} = (\boldsymbol{\Phi}^{\mathrm{T}}\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^{\mathrm{T}}\textbf{t}.
$$

Now, we can find an optimal parameter for any learning data $(\textbf{x}_1, t_1), (\textbf{x}_2, t_2), \dots, (\textbf{x}_N, t_N)$ by computing the equation.

### Conclusion

- The PRML book does not explain details of derivation process of the normal equation.
- I derive the normal equation step-by-step from the definition of linear regression models.
- Since vector derivation is not easy to follow, checking the result with simple examples is good idea.