---
schema: qual/card@1
id: P-7ENEI
kind: problem
title: $\lim_{n\to\infty}c_n=-\lim_{z\to 1}(z-1)f(z)$ for a simple pole at $z=1$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
  - Laurent Series
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Suppose that $f$ is holomorphic in an open set containing the closed unit disc, except for a simple pole at $z=1$. Let $f(z)=\sum_{n=1}^{\infty} c_{n} z^{n}$ denote the power series in the open unit disc. Show that 
\[
\lim _{n \rightarrow \infty} c_{n}=-\lim _{z \rightarrow 1}(z-1) f(z)
.\]
:::

:::{.solution}
Compute the series expansion of the RHS:
\[
(z-1) f(z) 
&= (z-1) \sum_{n\geq 1} c_n z^k \\
&= -c_1z + \sum_{n\geq 2} (c_{n-1} - c_n) z^n \\
&\convergesto{z\to 1} -c_1 + \sum_{n\geq 2} c_{n-1} - c_n \\
&\da \lim_{N\to\infty} -c_1 z + \sum_{n=2}^N c_{n-1} - c_n \\
&= \lim_{N\to\infty} -c_N
,\]
where we've used that the sum is telescoping.
:::

