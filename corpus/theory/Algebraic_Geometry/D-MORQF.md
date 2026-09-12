---
schema: qual/card@1
id: D-MORQF
kind: definition
title: Quasi-finite morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasi-finite Morphisms
  - Fibres
  - Finite Morphisms
relations:
- kind: uses
  target: D-MORFIN
review: draft
prompts:
- What is a quasi-finite morphism?
- Is a morphism with finite fibres finite?
---

::: {.definition title="Quasi-finite"}
$f : X \to Y$ is **locally quasi-finite** if it is locally of finite type with discrete fibres: every point of every fibre $X_y = \fiberprod{X}{Y}{\Spec \kappa(y)}$ is isolated, so $X_y$ is a zero-dimensional scheme.
It is **quasi-finite** if it is in addition quasicompact, equivalently of finite type with finite fibres.
:::

::: {.remark}
Among finite-type morphisms, finite fibres characterise quasi-finiteness, which is weaker than finiteness.
For example, the projection $V(xy-1)\to\AA^1_k$ onto the $x$-coordinate has finite fibres but is not finite: its image $D(x)$ is not closed.
:::
