---
schema: qual/card@1
id: FF-BOIT5
kind: fact
title: Euler Characteristic -2
prompts:
- Which closed surfaces have $\chi = -2$?
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Surfaces
  - Classification
relations: []
review: draft
---

::: {.fact}
A closed surface with $\chi = -2$ is either the orientable $\Sigma_2$ of genus two, since $\chi(\Sigma_g) = 2-2g$, or the nonorientable $N_4$, since $\chi(N_g) = 2-g$.
The Euler characteristic alone does not determine the surface; orientability is the second invariant the classification needs.
:::

::: {.remark}
Munkres, *Topology*, §77 (the classification theorem); Hatcher, §2.2, Examples 2.36 and 2.37 for the cell structures the characteristics are read from.

$\RP^2$ is $N_1$ and has $\chi = 1$, not $-2$.
:::
