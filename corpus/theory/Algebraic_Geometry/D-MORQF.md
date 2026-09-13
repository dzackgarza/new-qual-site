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
Quasi-finite is what "finite fibres" actually buys, and the whole point is that it is weaker than finite.
Finite is a condition on the ring map; quasi-finite is a condition on the fibres alone, and it cannot see whether the source is missing points.
The hyperbola supplies the gap.
:::
