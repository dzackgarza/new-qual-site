---
schema: qual/card@1
id: T-SB6AV
kind: theorem
title: Recognizing internal semidirect products
classification:
  areas:
  - algebra
  topics:
  - Semidirect Products
  - Normal Subgroups
  - Automorphisms
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a group with subgroups $N \normal G$ and $H\leq G$ such that $G = NH$ and $N\intersect H=\theset{e}$.
Let $\psi\colon H \to \Aut(N)$ be the conjugation action, $\psi(h)=h(\wait)h^{-1}$.
Then $G \cong N \semidirect_\psi H$.
:::

::: {.remark}
If moreover $H\normal G$, then $hnh^{-1}n^{-1}\in N\intersect H=\theset{e}$ for all $n\in N$ and $h\in H$, so $\psi$ is trivial and $G\cong N\times H$.
:::
