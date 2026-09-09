---
schema: qual/card@1
id: P-5YUW6
kind: problem
title: Orbit-stabilizer theorem
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
- State the orbit-stabilizer theorem
:::


::: {.solution}
Let a group $G$ act on a set $X$, and let $x\in X$. Write
\[
G_x=\{g\in G:g\cdot x=x\}
\]
for the stabilizer and $G\cdot x$ for the orbit.

<1>1. The map
\[
\Phi:G/G_x\longrightarrow G\cdot x,
\qquad
gG_x\longmapsto g\cdot x
\]
is a bijection.
::: {.proof}
It is well-defined: if $gG_x=hG_x$, then $h^{-1}g\in G_x$, so
\[
g\cdot x=h(h^{-1}g)\cdot x=h\cdot x.
\]
It is surjective by the definition of the orbit. If $g\cdot x=h\cdot x$, then
\[
h^{-1}g\cdot x=x,
\]
so $h^{-1}g\in G_x$ and therefore $gG_x=hG_x$. Hence it is injective.
:::

<1>2. Therefore
\[
|G\cdot x|=[G:G_x]
\]
whenever these cardinalities are finite.
::: {.proof}
By <1>1, the orbit is in bijection with the left coset space $G/G_x$.
:::

<1>3. If $G$ is finite, then
\[
|G|=|G\cdot x|\,|G_x|.
\]
::: {.proof}
By Lagrange's theorem,
\[
|G|=[G:G_x]|G_x|.
\]
Substitute <1>2. This is the orbit--stabilizer theorem.
:::
:::
