---
schema: qual/card@1
id: P-YSJO3
kind: problem
title: "Explicit Rouche, $2\\mathbb{D}$"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Explicit Rouche, $2\mathbb{D}$"}
Find the number of zeros in $\abs{z} < 2$ of
\[
h(z) \da z^5 + 3z + 1
.\]

:::

:::{.solution}
Strategy: bound the difference.

- Big: $F(z) \da z^5$ so $\abs{F(z)} = 2^5 = 32$ on $\abs{z} = 2$
- Small: $g(z) \da p(z) - F(z) = 3z+1$, so $\abs{g(z)} \leq 3\abs{z}+ 1 = 7$ on $\abs{z} = 2$.

Then $\abs{g}\leq \abs{F}$ on $\abs{z} = 2$, $Z_{p} = Z_F = 5$.
:::
