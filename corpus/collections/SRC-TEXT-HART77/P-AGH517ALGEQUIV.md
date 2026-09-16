---
schema: qual/card@1
id: P-AGH517ALGEQUIV
kind: problem
title: Algebraic equivalence of divisors implies numerical equivalence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
  - Picard Group
relations: []
review: draft
---

::: {.problem}
Let $X$ be a surface.
Recall that we have defined an algebraic family of effective divisors on $X$, parametrized by a nonsingular curve $T$, to be an effective Cartier divisor $D$ on $X \times T$, flat over $T$ (III, 9.8.5). In this case, for any two closed points $0,1 \in T$, we say the corresponding divisors $D_0, D_1$ on $X$ are prealgebraically equivalent.

Two arbitrary divisors are prealgebraically equivalent if they are differences of prealgebraically equivalent effective divisors.
Two divisors $D, D^{\prime}$ are algebraically equivalent if there is a finite sequence $D=D_0, D_1, \ldots, D_n=D^{\prime}$ with $D_i$ and $D_{i+1}$ prealgebraically equivalent for each $i$.

a. Show that the divisors algebraically equivalent to 0 form a subgroup of $\Div X$.

b. Show that linearly equivalent divisors are algebraically equivalent.

Hint: If $(f)$ is a principal divisor on $X$, consider the principal divisor $(t f-u)$ on $X \times \PP^1$, where $t, u$ are the homogeneous coordinates on $\PP^1$.

c. Show that algebraically equivalent divisors are numerically equivalent.

Hint: Use (III, 9.9) to show that for any very ample $H$, if $D$ and $D^{\prime}$ are algebraically equivalent, then $D . H=D^{\prime} . H$.

Note.
The theorem of Néron and Severi states that the group of divisors modulo algebraic equivalence, called the Néron-Severi group, is a finitely generated abelian group.
Over $\CC$ this can be proved easily by transcendental methods (App.
B, §5) or as in (Ex.
1.8) below.
Over a field of arbitrary characteristic, see Lang and Néron [1] for a proof, and Hartshorne [6] for further discussion.
Since $\Num X$ is a quotient of the Néron-Severi group, it is also finitely generated, and hence free, since it is torsion-free by construction.
:::
