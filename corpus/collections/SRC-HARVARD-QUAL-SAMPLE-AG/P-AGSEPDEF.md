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

<1>1. The relative diagonal is the morphism
\[
\Delta_{X/Y}:X\longrightarrow X\times_YX,
\qquad
x\longmapsto(x,x).
\]
::: {.proof}
The two composites
\[
X\xrightarrow{\Delta_{X/Y}}X\times_YX
\rightrightarrows X
\]
with the two projections are both the identity on $X$.  By the universal property of the fibre product, these two identity maps determine the diagonal uniquely.
:::

<1>2. The morphism $f$ is separated if and only if
\[
\boxed{
\Delta_{X/Y}:X\longrightarrow X\times_YX
\text{ is a closed immersion}.
}
\]
::: {.proof}
This is the definition of a separated morphism.
:::

<1>3. A scheme $X$ is called separated over a base scheme $S$ when its structure morphism
\[
X\longrightarrow S
\]
is separated.
::: {.proof}
Applying <1>2 to the structure morphism says precisely that
\[
\Delta_{X/S}:X\longrightarrow X\times_SX
\]
is a closed immersion.
:::

<1>4. The definition is the scheme-theoretic analogue of the Hausdorff condition.
::: {.proof}
For an ordinary topological space $T$, Hausdorffness is equivalent to the diagonal
\[
T\longrightarrow T\times T
\]
being closed.  In algebraic geometry the Zariski topology itself is usually far from Hausdorff, so the correct replacement is to require the diagonal to be a closed **subscheme** of the fibre product.
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>2 is the requested definition.
:::
:::
