---
schema: qual/card@1
id: P-CASP23C
kind: problem
title: "A holomorphic function with |f|>m on the boundary and |f(0)|<m has a zero in D"
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Principle
  - Rouché
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f(z)$ be analytic on an open set containing $\overline{\mathbb{D}}$.
Suppose that $|f(z)| > m$ for $|z| = 1$ and $|f(0)| < m$ for a positive number $m$.
Prove that $f(z)$ has a zero in $\mathbb{D}$.
:::

::: {.solution}
Suppose that $f$ had no zero in $\mathbb D$. Since $f$ is also nonzero on
$|z|=1$ by the boundary hypothesis, the function $1/f$ would be holomorphic
on a neighborhood of $\overline{\mathbb D}$. On the boundary,
\[
\left|\frac1{f(z)}\right|<\frac1m.
\]
The maximum modulus principle would then give
\[
\left|\frac1{f(0)}\right|\le\frac1m,
\]
or $|f(0)|\ge m$, contradicting the hypothesis. Hence $f$ has a zero in
$\mathbb D$.
:::
