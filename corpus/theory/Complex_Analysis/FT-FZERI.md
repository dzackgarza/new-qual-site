---
schema: qual/card@1
id: FT-FZERI
kind: theorem
title: Rouché's theorem
prompts:
- What does Rouche's theorem conclude about the zero counts of $f$ and $g$?
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
If $\abs{f(z) - g(z)} < \abs{f(z)} + \abs{g(z)}$ for all $z\in\bd D$, then $f$ and $g$ are nonvanishing on $\bd D$ and have the same number of [[D-65VIK|zeros]] in $D$, counted with multiplicity.
:::
