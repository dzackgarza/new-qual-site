---
schema: qual/card@1
id: D-TFVPD
kind: definition
title: Mapping Cone
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homotopy
  - Quotient Spaces
relations: []
review: draft
---

::: {.definition}
For a map $f: X\to Y$, the **mapping cone** is the mapping cylinder with the source end collapsed,
\[
C_f \da M_f / \qty{X\cross\ts{0}} = \qty{CX \disjoint Y}/\qty{(x,0)\sim f(x)}
,\]
i.e. $Y$ with the cone on $X$ attached along $f$.
For a CW pair $(X,A)$ one has $X/A \homotopic X \union CA$, the mapping cone of $A\injects X$.
:::

::: {.concept}
See Hatcher, p. 13.
:::
