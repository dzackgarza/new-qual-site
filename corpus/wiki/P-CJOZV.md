---
schema: qual/card@1
id: P-CJOZV
kind: problem
title: "Find all three-fold covers of the wedge of two copies of $\\RP^2$ .\u2026"
classification:
  areas:
  - topology
  topics:
  - covering-spaces
  - fundamental-group
relations: []
review: draft
solved: true
---

Find all three-fold covers of the wedge of two copies of $\RP^2$ . Justify your answer.

::: {.solution}
::: {.concept}
:::
Note $\pi_1 \RP^2 = \ZZ/2\ZZ$, so $\pi_1 X = (\ZZ/2\ZZ)^2$.

The pullback of any neighborhood of the basepoint needs to be locally homeomorphic to one of

- $S^2 \vee S^2$

- $\RP^2 \vee S^2$

And so *all* possibilities for regular covering spaces are given by

- $\bigvee^{2k} S^2$ "beads" wrapped into a necklace for any $k \geq 1$

- $\RP^2 \vee (\bigvee^k S^2) \vee \RP^2$

- $\vee^\infty S^2$, the universal cover

To get a threefold cover, we want the basepoint to lift to three preimages, so we can take

- $S^2 \vee S^2 \vee S^2$ wrapped

- $\RP^2 \vee S^2 \vee \RP^2$.
:::
