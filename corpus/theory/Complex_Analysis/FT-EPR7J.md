---
schema: qual/card@1
id: FT-EPR7J
kind: theorem
title: Rouché's theorem, symmetric form
prompts:
- State Rouche's theorem in its symmetric form.
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
relations: []
review: draft
---

::: {.theorem}
Let $D=\theset{z : \abs{z-z_0}<R}$, and let $f,g$ be [[D-E7A5W|holomorphic]] on an open set containing $\overline D$.
If
$$
\abs{f(z) - g(z)} < \abs{f(z)} + \abs{g(z)} \quad\text{for all } z\in\bd D,
$$
then $f$ and $g$ have no [[D-65VIK|zeros]] on $\bd D$ and have the same number of zeros in $D$, counted with multiplicity.
:::
