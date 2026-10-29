---
schema: qual/card@1
id: E-UJAF4
kind: problem
title: Equicontinuity and pointwise convergence on a compact set imply uniform convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Uniform Convergence
  - Sequences of Functions
  - Compactness
relations: []
review: draft
---

::: {.exercise}
Prove the following: if $\theset{f_n}$ is equicontinuous on $K$ a compact set and $f_n\to f$ pointwise, then $f_n\to f$ uniformly.

:::

::: {.solution}
Fix $\varepsilon>0$.

::: pf

::: {.pf-step #delta}
There is $\delta>0$ such that $\abs{f_n(x)-f_n(y)}<\varepsilon/3$ and $\abs{f(x)-f(y)}\le\varepsilon/3$ for all $n$ and all $x,y\in K$ with $\abs{x-y}<\delta$.

::: pf-proof
Equicontinuity on the compact set $K$ gives a $\delta$, independent of $n$ and of the points, for the first inequality.
Letting $n\to\infty$ in $\abs{f_n(x)-f_n(y)}<\varepsilon/3$ and using pointwise convergence gives the second.
:::

:::

::: {.pf-step #net}
There are $y_1,\ldots,y_m\in K$ with $K\subseteq\bigcup_{j=1}^m B_\delta(y_j)$, and $N$ such that $\abs{f_n(y_j)-f(y_j)}<\varepsilon/3$ for all $n\ge N$ and all $j$.

::: pf-proof
The balls $B_\delta(y)$, $y\in K$, cover $K$, and compactness gives a finite subcover.
Pointwise convergence at each of the finitely many $y_j$ gives an $N_j$; take $N=\max_j N_j$.
:::

:::

::: pf-step
$\sup_{x\in K}\abs{f_n(x)-f(x)}<\varepsilon$ for all $n\ge N$, so $f_n\to f$ uniformly on $K$.

::: pf-proof
For $x\in K$ choose $j$ with $x\in B_\delta(y_j)$ by step [](#net){.pf-ref}.
Then
$$
\abs{f_n(x)-f(x)}\le\abs{f_n(x)-f_n(y_j)}+\abs{f_n(y_j)-f(y_j)}+\abs{f(y_j)-f(x)}<\varepsilon,
$$
bounding the outer terms by step [](#delta){.pf-ref} and the middle term by step [](#net){.pf-ref}.
:::

:::

:::

:::
