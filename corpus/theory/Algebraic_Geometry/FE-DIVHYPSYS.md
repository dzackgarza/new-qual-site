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

1. The hyperplane sections $X \cap H$, for hyperplanes $H \not\supseteq X$, form a base-point-free linear system of effective Cartier divisors on $X$: the sections $x_0,\ldots,x_n$ of $\OO_{\PP^n}(1)$ have no common zero on $\PP^n$, so the system has no base points [@Har77, §II.7, the definition of a very ample invertible sheaf].

2. A general hyperplane section is smooth at every point where $X$ is smooth, over a field of characteristic $0$ unless $X$ itself is smooth.
   So it is smooth if $X$ is smooth, in any characteristic, and also if the singular locus of $X$ is finite, since a general hyperplane misses finitely many points.
   The first sentence is [@Har77, Theorem II.8.18], whose hypotheses are exactly those of this proposition: $X$ a nonsingular closed subvariety of $\PP^n_k$ over an algebraically closed field, with no condition on the characteristic.
   For a singular $X$ the corresponding statement over a field of characteristic $0$ is [@Har77, Corollary III.10.9], Bertini for a linear system without base points on a nonsingular projective variety, applied to the nonsingular open subset of $X$; that corollary requires characteristic $0$.
:::

::: {.example}
Normality of $X$ does not make a general hyperplane section smooth.
The cone $X = V(x_0 x_1 - x_2^2) \subseteq \PP^4$ is a normal threefold singular along the line $L = V(x_0, x_1, x_2)$.
Every hyperplane meets $L$, and $X \cap H$ is singular at the point $L \cap H$ whenever $H \not\supseteq L$: in the plane $\PP^3 \cong H$ it is again a quadric cone.
:::
