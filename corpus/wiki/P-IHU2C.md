---
schema: qual/card@1
id: P-IHU2C
kind: problem
title: "How many roots does the following polynomial have in the\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
  - polynomials
relations: []
review: draft
---
:::{.problem title="?"}
How many roots does the following polynomial have in the open disc $\abs{z} < 1$?
\[
f(z) = z^7 - 4z^3 - 1
.\]

:::

:::{.solution}
Big: $M(z) = -4z^3$.
Small: $m(z) = z^7 - 1$.
Then on $\abs{z} = 1$,
\[
\abs{m(z)} = \abs{z^7-1} \leq \abs{z}^7 + 1 = 2 < 4 = \abs{-4z^4}
,\]
so $f$ and $M$ have the same number of zeros: three.
:::

