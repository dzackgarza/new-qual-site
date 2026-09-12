---
schema: qual/card@1
id: E-CNWHF
kind: problem
title: Compact metric spaces are complete
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Completeness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
Show that every compact metric space $(X, d)$ is complete (every Cauchy sequence in $X$ converges to a point in $X$).
:::

::: solution
<1>1. Let $(x_n)$ be a Cauchy sequence in the compact metric space $X$. Compactness of a metric space implies sequential compactness, so some subsequence satisfies
\[
x_{n_k}\longrightarrow x\in X.
\]

<1>2. Fix $\varepsilon>0$. Since $(x_n)$ is Cauchy, choose $N$ such that
\[
m,n\ge N\implies d(x_m,x_n)<\varepsilon/2.
\]
Choose $k$ with $n_k\ge N$ and
\[
d(x_{n_k},x)<\varepsilon/2.
\]
Then for every $n\ge N$,
\[
d(x_n,x)\le d(x_n,x_{n_k})+d(x_{n_k},x)<\varepsilon.
\]
Thus $x_n\to x$.

<1>3. Every Cauchy sequence in $X$ therefore converges to a point of $X$, so $X$ is complete.
:::
