---
schema: qual/card@1
id: E-BB4BN
kind: problem
title: Intervals homeomorphic with the unit interval
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that the subspace $(a, b)$ of $\mathbb{R}$ is homeomorphic with $(0, 1)$ and the subspace $[a, b]$ of $\mathbb{R}$ is homeomorphic with $[0, 1]$.
:::

::: {.solution}
Assume $a<b$. The affine map
\[
f:[a,b]\longrightarrow[0,1],\qquad f(x)=\frac{x-a}{b-a}
\]
is continuous, bijective, and has continuous inverse
\[
f^{-1}(t)=a+(b-a)t.
\]
Hence $[a,b]\cong[0,1]$.

Restricting the same formulas gives mutually inverse continuous maps
\[
(a,b)\longleftrightarrow(0,1),
\]
so $(a,b)\cong(0,1)$ as well.
:::
