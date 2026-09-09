---
schema: qual/card@1
id: P-RAF20F
kind: problem
title: "Pointwise absolute summability against every functional implies uniform boundedness"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
  - Uniform Boundedness Principle
  - Dual Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the official UCSD Fall 2020 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $X$ be a real Banach space and $x_k \in X$ ($k = 1, 2, \ldots$). Assume that $\sum_{k=1}^\infty |f(x_k)| < \infty$ for any $f \in X^*$.
Prove that there exists a constant $\gamma \geq 0$ such that $\sum_{k=1}^\infty |f(x_k)| \leq \gamma \|f\|$ for any $f \in X^*$.
:::

::: solution
<1>1. Package the partial sums as bounded operators.
::: proof
For $N\ge1$, define
\[
T_N:X^*\to\mathbb R^N,
\qquad
T_N(f)=(f(x_1),\ldots,f(x_N)),
\]
where $\mathbb R^N$ is equipped with the $\ell^1$ norm. Then
\[
\|T_N(f)\|_1
=\sum_{k=1}^N|f(x_k)|
\le \left(\sum_{k=1}^N\|x_k\|\right)\|f\|,
\]
so each $T_N$ is a bounded linear operator.
:::

<1>2. Apply the Uniform Boundedness Principle.
::: proof
For every fixed $f\in X^*$, the hypothesis gives
\[
\sup_N\|T_N(f)\|_1
=\sup_N\sum_{k=1}^N|f(x_k)|
=\sum_{k=1}^\infty|f(x_k)|
<\infty.
\]
The dual space $X^*$ is Banach. Hence the Uniform Boundedness Principle yields
\[
\gamma:=\sup_N\|T_N\|<\infty.
\]
Therefore, for every $f\in X^*$ and every $N$,
\[
\sum_{k=1}^N|f(x_k)|
=\|T_N(f)\|_1
\le\gamma\|f\|.
\]
Letting $N\to\infty$ gives
\[
\boxed{\sum_{k=1}^\infty|f(x_k)|\le\gamma\|f\|}
\]
for every $f\in X^*$.
:::
:::
