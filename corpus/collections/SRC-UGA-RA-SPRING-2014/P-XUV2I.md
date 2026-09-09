---
schema: qual/card@1
id: P-XUV2I
kind: problem
title: $\sum a_nb_n<\infty$ for all $b\in\ell^2$ implies $\sum a_n^2<\infty$
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Functional Analysis
  - Series of Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the recorded UGA Spring 2014 real-analysis exam source. The prior card lacked a canonical problem block and incorrectly typed the partial-sum functionals as maps into ell^1.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $(a_n)$ be a sequence of nonnegative real numbers such that for every nonnegative sequence $(b_n)\in\ell^2(\mathbb N)$,
\[
\sum_{n=1}^\infty a_n b_n<\infty.
\]
Show that
\[
\sum_{n=1}^\infty a_n^2<\infty.
\]
:::

::: solution
<1>1. Define the partial-sum functionals.
::: proof
For each $N\ge1$, define
\[
T_N:\ell^2(\mathbb N)\to\mathbb R,
\qquad
T_N(b)=\sum_{n=1}^N a_n b_n.
\]
Each $T_N$ is a bounded linear functional, represented by the finite vector
\[
(a_1,\dots,a_N,0,0,\dots)\in\ell^2.
\]
Hence
\[
\|T_N\|=\left(\sum_{n=1}^N a_n^2\right)^{1/2}.
\]
:::

<1>2. Prove pointwise boundedness.
::: proof
Fix $b\in\ell^2(\mathbb N)$. By replacing $b$ with $|b|$, it is enough to consider nonnegative sequences. The hypothesis says
\[
\sum_{n=1}^\infty a_n|b_n|<\infty.
\]
Therefore
\[
|T_N(b)|
\le \sum_{n=1}^N a_n|b_n|
\le \sum_{n=1}^\infty a_n|b_n|,
\]
so
\[
\sup_N|T_N(b)|<\infty
\]
for every $b\in\ell^2$.
:::

<1>3. Apply the Uniform Boundedness Principle.
::: proof
Since $\ell^2$ is Banach and the family $(T_N)$ is pointwise bounded, the Uniform Boundedness Principle gives
\[
\sup_N\|T_N\|<\infty.
\]
Using Step 1,
\[
\sup_N\sum_{n=1}^N a_n^2<\infty.
\]
The partial sums are increasing, so they converge to a finite limit. Hence
\[
\boxed{\sum_{n=1}^\infty a_n^2<\infty.}
\]
:::
:::
