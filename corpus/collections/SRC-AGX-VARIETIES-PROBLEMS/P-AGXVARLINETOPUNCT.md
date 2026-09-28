---
schema: qual/card@1
id: P-AGXVARLINETOPUNCT
kind: problem
title: Morphisms from the affine line to the punctured line are constant
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms of Varieties
  - Affine Line
  - Regular Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the corresponding clause of Zaidenberg Exercises 4.4 in the recorded
    source. Over k=C it asks that every morphism A^1 -> A^1* be constant.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the source's standing field k=C explicit on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked that the invertible target coordinate must map to a unit of C[x],
    and proved directly by degree that those units are exactly C^times.
---

::: {.problem}
Show that every morphism
$$
f:\AA^1_\CC\longrightarrow\AA^1_\CC\smz
$$
is constant.
:::

::: {.solution}
Write
$$
\GG_m=\AA^1_\CC\smz.
$$
Then
$$
\mco(\AA^1_\CC)=\CC[x],
\qquad
\mco(\GG_m)=\CC[t,t^{-1}].
$$

<1>1. The units of $\CC[x]$ are exactly the nonzero constants:
$$
\CC[x]^\times=\CC^\times.
$$

::: {.proof}
Let
$$
u,v\in\CC[x]
$$
satisfy
$$
uv=1.
$$
Both polynomials are nonzero, so
$$
\deg(uv)=\deg u+\deg v.
$$
Hence
$$
0=\deg1=\deg u+\deg v.
$$
Since polynomial degrees are nonnegative,
$$
\deg u=\deg v=0.
$$
Thus every unit is a nonzero constant. Conversely every nonzero constant is
a unit.
:::

<1>2. The comorphism of $f$ sends the target coordinate $t$ to a nonzero
constant.

::: {.proof}
The morphism $f$ corresponds to a homomorphism
$$
f^*:\CC[t,t^{-1}]\longrightarrow\CC[x].
$$
The element $t$ is a unit in the source ring, so
$$
f^*(t)
$$
must be a unit in $\CC[x]$. By step <1>1, there is a
$$
c\in\CC^\times
$$
such that
$$
f^*(t)=c.
$$
:::

<1>3. The morphism $f$ is the constant morphism with value $c$.

::: {.proof}
For a point
$$
a\in\AA^1_\CC,
$$
the target coordinate evaluated at $f(a)$ is
$$
t(f(a))
=
(f^*t)(a)
=
c.
$$
Thus
$$
f(a)=c
$$
for every $a$, so $f$ is constant.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 show that every morphism from the affine line to the
punctured affine line has constant image.
:::
:::
