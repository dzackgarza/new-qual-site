---
schema: qual/card@1
id: P-RAF18C
kind: problem
title: "Dilation of L^1 function vanishes a.e."
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f \in L^1(\mathbb{R}, m)$.
Prove that $\lim_{n \to \infty} f(n^2 x) = 0$ for almost every $x \in \mathbb{R}$.
:::

::: solution
<1>1. Estimate the exceptional sets at a fixed threshold.
::: proof
Fix $\varepsilon>0$ and define
\[
E_n(\varepsilon):=\{x\in\mathbb R:|f(n^2x)|>\varepsilon\}.
\]
With the change of variables $u=n^2x$,
\[
m(E_n(\varepsilon))
=\frac1{n^2}m\bigl(\{|f|>\varepsilon\}\bigr).
\]
Since $f\in L^1$, Chebyshev's inequality gives
\[
m\bigl(\{|f|>\varepsilon\}\bigr)
\le\frac{\|f\|_1}{\varepsilon}<\infty.
\]
Therefore
\[
\sum_{n=1}^\infty m(E_n(\varepsilon))
\le
m\bigl(\{|f|>\varepsilon\}\bigr)
\sum_{n=1}^\infty\frac1{n^2}
<\infty.
\]
:::

<1>2. Apply Borel--Cantelli at a countable family of thresholds.
::: proof
By the Borel--Cantelli lemma, for each positive integer $j$, almost every $x$ belongs to only finitely many sets
\[
E_n(1/j).
\]
Intersecting these full-measure sets over $j\ge1$, we obtain a full-measure set of points $x$ such that for every $j$ there is $N_j(x)$ with
\[
|f(n^2x)|\le\frac1j
\]
for all $n\ge N_j(x)$.

Hence, for almost every $x$,
\[
\boxed{f(n^2x)\longrightarrow0.}
\]
:::
:::
