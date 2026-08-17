---
schema: qual/card@1
id: P-FAGTL
kind: problem
title: "Explicit Rouch\u00e9, $\\mathbb{D}$"
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
  - polynomials
relations: []
review: draft
solved: true
---
:::{.exercise title="Explicit Rouché, $\mathbb{D}$"}
Find the number of zeros in $\abs{z} < 1$ of
\[
p(z) \da z^6 + 9z^4 + z^3 + 2z + 4
.\]

:::

:::{.solution}
Strategy: bound the difference.
Find the big and small term:

- Big: $F(z) = 9z^4$, so $\abs{F(z)} = 9$ on the boundary
- Small: $g(z) = p(z) - F(z) = z^6 + z^3 + 2z + 4$, so $\abs{g(z)}\leq 1+1+2+4=8$ on the boundary.

So $\abs{p-F} \leq \abs{F}$ on $\abs{z} = 2$, meaning $Z_{p} = Z_F = 4$.

:::
