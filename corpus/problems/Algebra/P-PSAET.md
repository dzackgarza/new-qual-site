---
schema: qual/card@1
id: P-PSAET
kind: problem
title: Orders of $\GL_n(\FF_p)$ and $\SL_n(\FF_p)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Determinants
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

::: problem
Determine the orders $|\operatorname{GL}_n(\mathbb{F}_p)|$ and $|\operatorname{SL}_n(\mathbb{F}_p)|$ for any prime $p$ and integer $n \ge 1$.
:::

::: solution
An invertible $n\times n$ matrix over $\mathbb F_p$ is exactly an ordered basis of $\mathbb F_p^n$ written as columns. The first column has $p^n-1$ choices, the second has $p^n-p$ choices, and in general the $(k+1)$-st column has $p^n-p^k$ choices. Hence
\[
\boxed{|\operatorname{GL}_n(\mathbb F_p)|=\prod_{k=0}^{n-1}(p^n-p^k).}
\]
Equivalently,
\[
|\operatorname{GL}_n(\mathbb F_p)|
=p^{n(n-1)/2}\prod_{j=1}^n(p^j-1).
\]

The determinant map
\[
\det:\operatorname{GL}_n(\mathbb F_p)\to\mathbb F_p^\times
\]
is surjective, because
\[
\det\operatorname{diag}(a,1,\dots,1)=a
\]
for every $a\in\mathbb F_p^\times$. Its kernel is $\operatorname{SL}_n(\mathbb F_p)$. Therefore
\[
\boxed{|\operatorname{SL}_n(\mathbb F_p)|=
\frac1{p-1}\prod_{k=0}^{n-1}(p^n-p^k).}
\]
:::
