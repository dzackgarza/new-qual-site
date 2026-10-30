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
Let $f(z)$ be analytic on an open set containing $\overline{\DD}$.
Suppose that $\abs{f(z)} > m$ for $\abs{z} = 1$ and $\abs{f(0)} < m$ for a positive number $m$.
Prove that $f(z)$ has a zero in $\DD$.
:::

::: {.solution}
Suppose that $f$ had no zero in $\DD$. Since $f$ is also nonzero on
$\abs{z}=1$ by the boundary hypothesis, the function $1/f$ would be holomorphic
on a neighborhood of $\overline{\DD}$. On the boundary,
$$
\abs{\frac1{f(z)}}<\frac1m.
$$
The maximum modulus principle would then give
$$
\abs{\frac1{f(0)}}\le\frac1m,
$$
or $\abs{f(0)}\ge m$, contradicting the hypothesis. Hence $f$ has a zero in
$\DD$.
:::
