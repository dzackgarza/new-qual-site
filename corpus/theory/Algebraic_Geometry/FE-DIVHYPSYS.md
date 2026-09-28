---
schema: qual/card@1
id: FE-DIVHYPSYS
kind: example
title: The linear system of hyperplane sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Hyperplane Sections
  - Bertini Theorem
relations:
- kind: uses
  target: D-DIVAMPLE
- kind: uses
  target: T-BERTINI
review: draft
prompts:
- Show that the hyperplane sections of a projective variety form a base-point-free linear system of effective divisors.
- When is a general hyperplane section smooth and reduced?
---

::: {.proposition}
Let $X \subseteq \PP^n$ be a projective variety over an algebraically closed field.

1. The hyperplane sections $X \cap H$, for hyperplanes $H \not\supseteq X$, form a base-point-free linear system of effective Cartier divisors on $X$.

2. A general hyperplane section is smooth at every point where $X$ is smooth.
   So it is smooth if $X$ is smooth, and also if the singular locus of $X$ is finite, since a general hyperplane misses finitely many points.
:::

::: {.example}
Normality of $X$ does not make a general hyperplane section smooth.
The cone $X = V(x_0 x_1 - x_2^2) \subseteq \PP^4$ is a normal threefold singular along the line $L = V(x_0, x_1, x_2)$.
Every hyperplane meets $L$, and $X \cap H$ is singular at the point $L \cap H$ whenever $H \not\supseteq L$: in the plane $\PP^3 \cong H$ it is again a quadric cone.
:::
