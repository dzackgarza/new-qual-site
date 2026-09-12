---
schema: qual/card@1
id: P-CAF06D
kind: problem
title: "Growth estimate for entire functions in terms of their zeros"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Assume that $f$ is an entire function.
Let $M(r) = \sup_{|z|=r} |f(z)|$.
Assume that the discrete sequence $\{a_n\}$ are zeros of $f$, indexed so that
$|a_1|\le |a_2|\le\cdots$, and $f(0) = 1$.
Show that $$k\log 2 \leq \log(M(2|a_k|)).$$
:::

::: remark
The Fall 2006 source does not state the ordering of $\{a_n\}$. The displayed
inequality requires the standard convention that the zeros are indexed by
nondecreasing modulus; without it, an arbitrary re-enumeration makes the claim
false.
:::

::: solution
Jensen's formula for $f(0)=1$ gives, for every $R>0$ avoiding zeros on the
circle,
\[
\sum_{|a_j|<R}\log\frac{R}{|a_j|}
=\frac1{2\pi}\int_0^{2\pi}\log|f(Re^{it})|\,dt
\le \log M(R).
\]
The same inequality follows for arbitrary $R$ by a limiting argument.

Take $R=2|a_k|$. By the ordering,
\[
|a_j|\le |a_k|\qquad(1\le j\le k),
\]
so for each of the first $k$ zeros,
\[
\log\frac{2|a_k|}{|a_j|}\ge\log2.
\]
Therefore
\[
k\log2
\le \sum_{j=1}^k\log\frac{2|a_k|}{|a_j|}
\le \log M(2|a_k|),
\]
which is the required estimate.
:::
