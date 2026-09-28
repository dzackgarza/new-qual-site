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

::: {.definition title="Fano, Calabi--Yau, and general type"}
Let $X$ be a smooth complete variety with canonical divisor $K_X$.

- $X$ is \dfn{Fano} if $-K_X$ is ample.

- $X$ is \dfn{Calabi--Yau} if $K_X \sim_\QQ 0$; the stricter convention demands $\omega_X \cong \OO_X$ together with $h^j(\OO_X) = 0$ for $1 \leq j \leq \dim X - 1$.

- $X$ is of \dfn{general type} if $K_X$ is big.

A \dfn{del Pezzo surface} is a Fano variety of dimension two.
:::

::: {.remark}
A smooth projective curve of genus $g$ is Fano if and only if $g = 0$, Calabi--Yau if and only if $g = 1$, and of general type if and only if $g \geq 2$, since $\deg K=2g-2$.
A complete variety with an ample divisor is projective, so every Fano variety is projective.

The two conventions for Calabi--Yau are not equivalent: abelian varieties have $K_X=0$ but do not satisfy the intermediate-cohomology vanishing, so they satisfy the first convention and not the second.
The del Pezzo surfaces are $\PP^1\times\PP^1$ and $\PP^2$ blown up at $r\le8$ general points, with $K^2=9-r$; the cubic surface is the case $r=6$ and contains $27$ lines.
:::
