---
schema: qual/card@1
id: P-AGSEPDEF
kind: problem
title: Separated morphisms, defined
classification:
  areas:
  - algebraic-geometry
  topics:
  - Separated Morphisms
  - Diagonal
  - Definitions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; the source asks for the definition of a separated morphism.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Define separated morphism.
:::

::: {.solution}
Let
\[
f:X\longrightarrow Y
\]
be a morphism of schemes.

::: pf

::: pf-step
The relative diagonal is the morphism
\[
\Delta_{X/Y}:X\longrightarrow X\times_YX,
\qquad
x\longmapsto(x,x).
\]

::: pf-proof
The two composites
\[
X\xrightarrow{\Delta_{X/Y}}X\times_YX
\rightrightarrows X
\]
with the two projections are both the identity on $X$.  By the universal property of the fibre product, these two identity maps determine the diagonal uniquely.
:::

:::

::: {.pf-step #separated-definition}
The morphism $f$ is separated if and only if
\[
\boxed{
\Delta_{X/Y}:X\longrightarrow X\times_YX
\text{ is a closed immersion}.
}
\]

::: pf-proof
This is the definition of a separated morphism.
:::

:::

::: pf-step
A scheme $X$ is called separated over a base scheme $S$ when its structure morphism
\[
X\longrightarrow S
\]
is separated.

::: pf-proof
Applying step [](#separated-definition){.pf-ref} to the structure morphism says precisely that
\[
\Delta_{X/S}:X\longrightarrow X\times_SX
\]
is a closed immersion.
:::

:::

::: pf-step
The definition is the scheme-theoretic analogue of the Hausdorff condition.

::: pf-proof
For an ordinary topological space $T$, Hausdorffness is equivalent to the diagonal
\[
T\longrightarrow T\times T
\]
being closed.  For schemes the diagonal lands in the fibre product $X\times_YX$, whose underlying space is not the product of the underlying spaces, and the Zariski topology of an irreducible scheme of positive dimension is not Hausdorff.  Separatedness imposes the diagonal condition scheme-theoretically: $\Delta_{X/Y}$ is a closed immersion into $X\times_YX$.
:::

:::

::: pf-qed
Step [](#separated-definition){.pf-ref} is the requested definition.
:::

:::
:::
