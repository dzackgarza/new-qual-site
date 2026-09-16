---
schema: qual/card@1
id: FT-ZJQ2T
kind: theorem
title: Rouché's theorem on a closed disc
prompts:
- State Rouche's theorem on a closed disc $\abs{z - z_0} \leq R$.
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
Let $z_0\in\CC$ and $R>0$, and let $f$ and $g$ be [[D-E7A5W|holomorphic]] on an open set containing the closed disc $\abs{z-z_0} \leq R$.
Suppose $f$ and $g$ have no zeros on the circle $\abs{z-z_0} = R$ and
$$
\abs{f(z)-g(z)} < \abs{f(z)} + \abs{g(z)} \quad\text{for all } z \text{ with } \abs{z-z_0}=R.
$$
Then $f$ and $g$ have the same number of [[D-65VIK|zeros]] in the open disc $\abs{z-z_0}<R$, counted with multiplicity.
:::
