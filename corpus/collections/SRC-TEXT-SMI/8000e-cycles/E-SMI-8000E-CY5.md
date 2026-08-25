---
schema: qual/card@1
id: E-SMI-8000E-CY5
kind: exercise
title: The sign homomorphism from the Vandermonde polynomial
classification:
  areas:
  - algebra
  topics:
  - Symmetric Group
relations: []
review: draft
---

::: {.exercise title="Smith 8000e cycles 5"}
Let

$$
f(X) = \prod_{i < j} (X_i - X_j),
$$

and let $S(n)$ act on $\ZZ[X_1, \ldots, X_n]$ by permuting the indices of the variables.
For example, if $n = 3$, $(12)$ sends

$$
f(X) = (X_1 - X_2)(X_1 - X_3)(X_2 - X_3)
$$

to $(X_2 - X_1)(X_2 - X_3)(X_1 - X_3) = -f(X)$.
Deduce that every permutation $m$ takes $f$ to either $f$ or $-f$, and that setting $\operatorname{sgn}(m) = c$, where $m(f) = c \cdot f$, defines a surjective homomorphism $S(n) \to \ts{\pm 1}$ whose kernel consists of those permutations which can be written as a product of an even number of 2-cycles.
Call that subgroup $A(n)$.
:::
