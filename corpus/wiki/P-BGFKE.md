---
schema: qual/card@1
id: P-BGFKE
kind: problem
title: Roots of $z^3+2z+4$ lie outside the unit disk
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Prove that the following polynomial has its roots outside of the unit circle:
\[
p(z) = z^3 + 2z + 4
.\]

> Hint: What is the maximum value of the modulus of the first two terms if $\abs{z} \leq 1$?

:::

:::{.solution}
Big: $M(z) = 4$
Small: $m(z) = z^3 + 2z$.
On $\abs{z} = 1$,
\[
\abs{m(z)} \leq \abs{z}^3 + 2\abs{z} = 1+2=3 < 4 = \abs{M(z)}
,\]
so $0 = Z_M = Z_{M+m} = Z_f$ in $\DD$.
:::

