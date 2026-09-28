---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-04
kind: problem
title: A separable metric space is second countable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Show that if the metric space $(X,d)$ is separable, then the metric topology on $X$ is second countable.
:::

::: {.solution}
Let $D=\{p_1,p_2,\dots\}$ be a countable dense subset of $X$. Consider
$$
\mathcal B=\{B(p,q):p\in D,\ q\in\mathbb Q_{>0}\}.
$$
This family is countable.

To show it is a basis, let $U$ be open and let $x\in U$. Choose $\varepsilon>0$ with $B(x,\varepsilon)\subset U$. By density choose $p\in D\cap B(x,\varepsilon/3)$, and choose rational $q$ satisfying
$$
d(x,p)<q<\varepsilon-d(x,p).
$$
Then $x\in B(p,q)$, and if $y\in B(p,q)$,
$$
d(x,y)\le d(x,p)+d(p,y)<d(x,p)+q<\varepsilon.
$$
Hence
$$
x\in B(p,q)\subset B(x,\varepsilon)\subset U.
$$
Therefore $\mathcal B$ is a countable basis, so $X$ is second countable.
:::
