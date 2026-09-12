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
Let \(D=\{d_1,d_2,\dots\}\) be a countable dense subset of \(X\). Consider
\[
\mathcal B=\{B(d,q):d\in D,\ q\in\mathbb Q_{>0}\}.
\]
This family is countable.

To show it is a basis, let \(U\) be open and let \(x\in U\). Choose \(\varepsilon>0\) with \(B(x,\varepsilon)\subset U\). By density choose \(d\in D\cap B(x,\varepsilon/3)\), and choose rational \(q\) satisfying
\[
d(x,d)<q<\varepsilon-d(x,d).
\]
Then \(x\in B(d,q)\), and if \(y\in B(d,q)\),
\[
d(x,y)\le d(x,d)+d(d,y)<d(x,d)+q<\varepsilon.
\]
Hence
\[
x\in B(d,q)\subset B(x,\varepsilon)\subset U.
\]
Therefore \(\mathcal B\) is a countable basis, so \(X\) is second countable.
:::
