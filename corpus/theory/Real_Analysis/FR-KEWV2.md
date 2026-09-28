---
schema: qual/card@1
id: FR-KEWV2
kind: proof
title: A series of functions with summable $L^1$ norms converges absolutely almost everywhere
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - L¹
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $f_n\colon X\to\CC$ for $n\geq1$ be [[D-DHFN4|measurable]], and let $S(x) \coloneqq \sum_{n\geq1} \abs{f_n(x)}\in[0,\infty]$.
Then
$$
\int_X S\dmu = \sum_{n\geq1} \norm{f_n}_1 .
$$
In particular, if $\sum_{n\geq1} \norm{f_n}_1<\infty$, then $S\in L^1(X,\mu)$ and $\sum_{n\geq1} \abs{f_n(x)} < \infty$ for $\mu$-almost every $x\in X$.
:::

::: {.proof}
The partial sums $S_N \coloneqq \sum_{n=1}^N \abs{f_n}$ are nonnegative, measurable, and increase pointwise to $S$.
By the monotone convergence theorem,
$$
\int_X S\dmu = \lim_{N\to\infty} \int_X S_N\dmu = \lim_{N\to\infty} \sum_{n=1}^N \int_X \abs{f_n}\dmu = \sum_{n\geq1} \norm{f_n}_1.
$$
Now assume $\sum_{n\geq1} \norm{f_n}_1<\infty$, so $\int_X S\dmu<\infty$.
Let $A\coloneqq\theset{x\in X\suchthat S(x)=\infty}$, which is measurable.
For every $t>0$ we have $S\geq t\,\one_A$, so $t\,\mu(A)\le\int_X S\dmu$; letting $t\to\infty$ gives $\mu(A)=0$.
Therefore $\sum_{n\geq1} \abs{f_n(x)} < \infty$ for almost every $x$.
:::
