---
schema: qual/card@1
id: P-AGXVARPROJPROPER
kind: problem
title: Projection along a projective factor is proper and closed
classification:
  areas:
  - algebraic-geometry
  topics:
  - Properness
  - Projective Varieties
  - Closed Maps
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the corresponding clause of Zaidenberg Exercises 8.5 in the recorded
    source. It asks that for projective X and complex affine Y, the projection
    X x Y -> Y be proper and Zariski closed.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Base-changed a projective embedding X -> P^n_C to a closed immersion
    X x Y -> P^n_Y, making the projection projective. Applied projective
    implies proper and proper implies universally closed.
---

::: {.problem}
Show that if $X$ is projective and $Y$ is affine over $k = \CC$, then the projection $\pi_2: X\cross Y\to Y$ is proper and closed in the Zariski topology.
:::

::: {.solution}
Choose a projective embedding
$$
i:X\hookrightarrow\PP^n_\CC.
$$

<1>1. The product embedding
$$
i\cross\id_Y:
X\cross Y
\hookrightarrow
\PP^n_\CC\cross Y
=
\PP^n_Y
$$
is a closed immersion.

::: {.proof}
The map $i$ is a closed immersion because $X$ is projective. Closed
immersions are preserved by arbitrary base change. Base-changing $i$ along
$$
Y\longrightarrow\Spec\CC
$$
gives exactly
$$
i\cross\id_Y:
X\cross Y\hookrightarrow\PP^n_Y.
$$
Hence this map is a closed immersion.
:::

<1>2. The projection
$$
\pi_2:X\cross Y\longrightarrow Y
$$
is projective.

::: {.proof}
By step <1>1, $\pi_2$ factors as
$$
X\cross Y
\hookrightarrow
\PP^n_Y
\longrightarrow
Y,
$$
where the first map is a closed immersion and the second is the standard
projective-space projection. This is precisely the definition of a
projective morphism in [[D-MORPROJ]].
:::

<1>3. The projection $\pi_2$ is proper.

::: {.proof}
Projective morphisms over a Noetherian base are proper by [[D-MORPROJ]].
The affine variety $Y$ is Noetherian, so step <1>2 implies that $\pi_2$ is
proper.
:::

<1>4. The projection $\pi_2$ is a closed map in the Zariski topology.

::: {.proof}
A proper morphism is universally closed by definition ([[D-8XX95]]). In
particular, without any further base change, it sends closed subsets to
closed subsets. Step <1>3 therefore implies that $\pi_2$ is closed.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove properness, and step <1>4 proves Zariski closedness.
:::
:::
