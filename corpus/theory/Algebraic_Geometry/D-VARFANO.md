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

::: {.definition title="Three canonical-class conditions"}
Let $X$ be a smooth complete variety with canonical divisor $K_X$.

- $X$ is \dfn{Fano} if $-K_X$ is ample.

- In the weak $K$-trivial convention, $X$ is \dfn{Calabi--Yau} if $K_X \sim_\QQ 0$.
  A stricter convention requires $\omega_X \cong \OO_X$ together with $h^j(\OO_X)=0$ for $1\leq j\leq\dim X-1$.

- $X$ is of \dfn{general type} if $K_X$ is big.

A \dfn{del Pezzo surface} is a Fano variety of dimension two.
:::

::: {.remark}
In higher dimension there are smooth complete varieties whose canonical class is neither anti-ample, $\QQ$-linearly trivial, nor big.
For smooth projective curves, however, they are exactly the cases $g=0$, $g=1$, and $g\ge2$.
If $X$ is complete and $-K_X$ is ample, a sufficiently large positive multiple of $-K_X$ defines a closed immersion into projective space; hence every Fano variety in this definition is projective.

The two conventions for Calabi--Yau are not equivalent: abelian varieties of dimension at least $2$ have $K_X=0$ but do not satisfy the intermediate-cohomology vanishing, so they satisfy the first convention and not the second.
Over an algebraically closed field, the del Pezzo surfaces are $\PP^1\times\PP^1$ and $\PP^2$ blown up at $r\le8$ points in general position; for the latter, $K^2=9-r$. A smooth cubic surface is the case $r=6$ and contains $27$ lines.
:::
