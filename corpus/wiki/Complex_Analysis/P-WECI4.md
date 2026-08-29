---
schema: qual/card@1
id: P-WECI4
kind: problem
title: Arbitrary Rouché, $R\mathbb{D}$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
---

:::{.exercise}
Find the number of zeros in $\abs{z} < R$ of 
\[
p(z) \da z^d + a_1z^{d-1} + \cdots + a_d
,\]
supposing that
$\abs{a_k}< {R^k \over d}$ for every $k$ (noting the strict inequality).

:::

:::{.solution}
Strategy: bound the difference.
Find the big and small term:

- Big: $F(z) = z^d$, so $\abs{F(z)} = R^d$ on $\abs{z} = R$.
- Small: $g(z) = p(z) - F(z) = a_1 z^{d-1} + \cdots + a_d$, so
\[
\abs{g(z)} 
&\leq \abs{a_1} R^{d-1} + \abs{a_2} R^{d-2} + \cdots + \abs{a_d} \\
&< {R\over d} \cdot R^{d-1} + {R^2 \over d} \cdot R^{d-2} + \cdots + {R^{d-1} \over d} \cdot R + {R^{d} \over d} \\
&= d {R^d\over d} = R^d
,\]
so $\abs{g} < R^d = \abs{F}$, meaning $Z_{p-F} = Z_F = d$ in $R\DD$.

:::
