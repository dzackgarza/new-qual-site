---
schema: qual/card@1
id: FS-BM2PV
kind: strategy
title: Interchanging a series and an integral by Fubini--Tonelli on $X\times\NN$
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Convergence of Integrals
  - Series of Functions
relations: []
review: draft
---

::: {.strategy}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f_n\colon X\to\CC$ for $n\geq1$ be [[D-DHFN4|measurable]] functions with
$$
\sum_{n=1}^\infty \int_X \abs{f_n} \dmu < \infty .
$$
Then $\sum_{n}f_n(x)$ converges absolutely for almost every $x$, and
$$
\sum_{n=1}^\infty \int_X f_n \dmu = \int_X \sum_{n=1}^\infty f_n \dmu.
$$
The method views the sum as an integral against counting measure on $\NN$ and applies the Fubini--Tonelli theorem on $X\times\NN$.

<1>1. Encode the series as an integral over $\NN$.

<2>1. Let $\nu$ be counting measure on $\NN$, so that $\int_{\NN} g \, d\nu = \sum_{n=1}^\infty g(n)$ for every $g\colon\NN\to[0,\infty]$ and every $\nu$-integrable $g\colon\NN\to\CC$.

<2>2. Define $F \colon X \times \NN \to \CC$ by $F(x, n) \coloneqq f_n(x)$.
It is measurable for the product $\sigma$-algebra, since $F^{-1}(B)=\bigcup_n f_n^{-1}(B)\times\theset{n}$ for every Borel set $B\subseteq\CC$.

<2>3. The two sides of the identity are the two iterated integrals of $F$:
$$
\sum_{n=1}^\infty \int_X f_n \dmu = \int_{\NN} \int_X F(x, n) \, d\mu(x) \, d\nu(n), \qquad \int_X \sum_{n=1}^\infty f_n \dmu = \int_X \int_{\NN} F(x, n) \, d\nu(n) \, d\mu(x).
$$

<1>2. Reduce to a $\sigma$-finite measure space.

<2>1. For each $n$ and $k\geq1$, $\mu\qty{\theset{\abs{f_n}>1/k}}\le k\int_X\abs{f_n}\dmu<\infty$, so $A\coloneqq\bigcup_n\theset{x\in X\suchthat f_n(x)\neq0}$ is a countable union of sets of finite measure.

<2>2. Every $f_n$ vanishes outside $A$, so both sides of the identity are unchanged when $X$ is replaced by $A$ and $\mu$ by its restriction to $A$, which is $\sigma$-finite.
Counting measure on $\NN$ is $\sigma$-finite as well.

<1>3. Verify the hypothesis of Fubini's theorem.

<2>1. Since $\abs{F}$ is nonnegative and measurable on $A \times \NN$, Tonelli's theorem gives
$$
\int_{A \times \NN} \abs{F} \, d(\mu \times \nu) = \int_{\NN} \int_A \abs{F} \dmu \, d\nu = \sum_{n=1}^\infty \int_X \abs{f_n} \dmu < \infty.
$$

<2>2. Hence $F \in L^1(A \times \NN, \mu \times \nu)$.

<1>4. Apply Fubini's theorem.

<2>1. Because $F$ is integrable on the product space, Fubini's theorem shows that $\int_{\NN}\abs{F(x,n)}\,d\nu(n)=\sum_n\abs{f_n(x)}$ is finite for almost every $x$ and that the iterated integrals agree:
$$
\int_{\NN} \int_A F \dmu \, d\nu = \int_A \int_{\NN} F \, d\nu \dmu.
$$

<2>2. Substituting the definitions of $F$ and $\nu$ into step <1>1 yields
$$
\sum_{n=1}^\infty \int_X f_n \dmu = \int_X \sum_{n=1}^\infty f_n \dmu.
$$
:::

::: {.remark}
The same argument, with counting measure on $\NN\times\NN$, applies to a doubly indexed family $(f_{m,n})_{m,n\geq1}$ of measurable functions: the hypothesis $\sum_{m,n} \int_X \abs{f_{m,n}}\dmu < \infty$ justifies interchanging the double sum with the integral.
:::
