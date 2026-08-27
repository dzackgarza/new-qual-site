---
schema: qual/card@1
id: D-3UY5O
kind: definition
title: Lefschetz Number
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Homology
relations: []
review: draft
---

::: {.definition}
For $f: X\selfmap$ with $X$ a finite simplicial complex, or more generally a retract of one, the **Lefschetz number** is
\[
\tau(f) \da \sum_n (-1)^n \tr\qty{ f_*: H_n(X;\QQ) \to H_n(X;\QQ) }
.\]
Then $\tau(\id_X) = \chi(X)$, and the Lefschetz fixed point theorem says that $\tau(f)\neq 0$ forces $f$ to have a fixed point.
:::

::: {.concept}
See Hatcher, §2.C, Theorem 2C.3, p. 179.
:::
