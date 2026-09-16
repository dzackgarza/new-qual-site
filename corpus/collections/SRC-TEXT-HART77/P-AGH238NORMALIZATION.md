---
schema: qual/card@1
id: P-AGH238NORMALIZATION
kind: problem
title: Normalization of an integral scheme and its universal property
classification:
  areas:
  - algebraic-geometry
  topics:
  - Integral Schemes
  - Normalization
  - Integral Closure
relations: []
review: draft
---

::: {.problem}
A scheme is **normal** if all of its local rings are integrally closed domains.
Let $X$ be an integral scheme.
For each open affine subset $U = \Spec A$ of $X$, let $\tilde{A}$ be the integral closure of $A$ in its quotient field, and let $\tilde{U} = \Spec \tilde{A}$.

Show that one can glue the schemes $\tilde{U}$ to obtain a normal integral scheme $\tilde{X}$, called the **normalization** of $X$.

Show also that there is a morphism $\tilde{X} \to X$ with the following universal property: for every normal integral scheme $Z$ and every dominant morphism $f: Z \to X$, the morphism $f$ factors uniquely through $\tilde{X}$.
If $X$ is of finite type over a field $k$, then the morphism $\tilde{X} \to X$ is a finite morphism.
:::
