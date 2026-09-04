---
schema: qual/card@1
id: P-BHLSJ
kind: problem
title: Laurent expansions of $e^{1/z}$ and $\cos(1/z)$ about $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Essential Singularities
  - Principal Parts
relations: []
review: draft
---

Find the Laurent expansions about $z=0$ of the following functions:
\[
e^{1\over z} \hspace{8em} \cos \qty{1\over z}
.\]

::: {.solution}
Substitute $1/z$ into the usual Taylor series.

For the exponential,
\[
e^{1/z}
=\sum_{n=0}^\infty {1\over n!z^n}
=1+{1\over z}+{1\over2!z^2}+{1\over3!z^3}+\cdots.
\]

For the cosine,
\[
\cos\qty{1\over z}
=\sum_{n=0}^\infty {(-1)^n\over(2n)!z^{2n}}
=1-{1\over2!z^2}+{1\over4!z^4}-{1\over6!z^6}+\cdots.
\]

Both Laurent series converge for every $z\neq0$, so their annulus of convergence is $0<|z|<\infty$.
:::

