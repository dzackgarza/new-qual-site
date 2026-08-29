---
schema: qual/card@1
id: D-KVAI3
kind: definition
title: Homotopy Extension Property
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Cell Complexes
  - Retracts
relations: []
review: draft
---

::: {.definition}
A pair $(X,A)$ has the **homotopy extension property** iff every map $f_0: X\to Y$ together with a homotopy $f_t: A\to Y$ of $\ro{f_0}{A}$ extends to a homotopy $f_t: X\to Y$ of $f_0$.
Equivalently, every pair of maps $X\cross\ts{0}\to Y$ and $A\cross I\to Y$ agreeing on $A\cross\ts{0}$ extends over $X\cross I$; equivalently, $X\cross\ts{0}\union A\cross I$ is a retract of $X\cross I$.
Every CW pair has it.
:::

::: {.concept}
See Hatcher, p. 14; for CW pairs, Proposition 0.16, p. 15.
:::
