---
schema: qual/card@1
id: D-VARFANO
kind: definition
title: Fano, Calabi--Yau, and general type
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fano Varieties
  - Calabi-Yau Varieties
  - Canonical Divisor
relations:
- kind: related-to
  target: D-5PQ5W
review: draft
prompts:
- What is a Fano variety?
- What is a del Pezzo surface?
- What is a Calabi--Yau variety?
---

::: {.definition title="The trichotomy by canonical class"}
Let $X$ be a smooth complete variety with canonical divisor $K_X$.

- $X$ is \dfn{Fano} if $-K_X$ is ample.

- $X$ is **Calabi--Yau** if $K_X \sim_\QQ 0$; the stricter convention demands $\omega_X \cong \OO_X$ together with $h^j(\OO_X) = 0$ for $1 \leq j \leq \dim X - 1$.

- $X$ is of **general type** if $K_X$ is big.

A **del Pezzo surface** is a Fano variety of dimension two.
:::

::: {.remark}
The sign of $K_X$ is the organising invariant of birational classification, and for curves the three cases are exactly $g = 0$, $g = 1$, $g \geq 2$.
A Fano variety is automatically projective, since $-K_X$ is an ample divisor to embed by, so "complete" in the definition costs nothing.

The two conventions for Calabi--Yau are not equivalent and the difference is asked about: abelian varieties have $K_X = 0$ but do not satisfy the vanishing, so they are Calabi--Yau in the first sense and not the second.
The del Pezzo surfaces are $\PP^1 \times \PP^1$ and $\PP^2$ blown up at $r \leq 8$ general points, with $K^2 = 9 - r$; the cubic surface is the case $r = 6$, and the $27$ lines on it are what that classification is usually asked for.
:::
