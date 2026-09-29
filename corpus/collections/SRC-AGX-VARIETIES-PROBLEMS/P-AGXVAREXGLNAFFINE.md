---
schema: qual/card@1
id: P-AGXVAREXGLNAFFINE
kind: problem
title: $\GL_n(\CC)$ is an affine variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Varieties
  - Distinguished Opens
  - Linear Algebraic Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 4.2 in the recorded source. Its hint realizes
    GL(n,C) as the hypersurface t det(A)=1 in M_n(C) x A^1.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the hypersurface realization, the inverse projection map, and the
    coordinate-ring identification with the localization at det.
---

::: {.problem}
Show that $\GL_n(\CC)$ is an affine variety.
:::

::: {.solution}
Let
$$
M_n(\CC)\cong\AA^{n^2}_\CC
$$
have coordinate functions
$$
x_{ij},
\qquad
1\leq i,j\leq n,
$$
and write
$$
\Delta=\det(x_{ij}).
$$

::: pf

::: {.pf-step #y-is-affine}
The subset
$$
Y
=
V(t\Delta-1)
\subseteq
\AA^{n^2+1}_\CC
$$
is an affine variety.

::: pf-proof
Its coordinate ring is
$$
\CC[x_{ij},t]/(t\Delta-1).
$$
The homomorphism
$$
\CC[x_{ij},t]
\longrightarrow
\CC[x_{ij}]_\Delta
$$
defined by
$$
x_{ij}\longmapsto x_{ij},
\qquad
t\longmapsto\Delta^{-1}
$$
is surjective and has kernel $(t\Delta-1)$. Therefore
$$
\CC[Y]
\cong
\CC[x_{ij}]_\Delta.
$$
The localization of the domain $\CC[x_{ij}]$ is again a domain, so
$(t\Delta-1)$ is prime. Hence $Y$ is an affine variety.
:::

:::

::: {.pf-step #pi-bijective}
Projection to the matrix coordinates gives a bijection
$$
\pi:Y\longrightarrow\GL_n(\CC).
$$

::: pf-proof
If
$$
(A,t)\in Y,
$$
then
$$
t\det A=1,
$$
so $\det A\neq0$ and $A\in\GL_n(\CC)$.

Conversely, if $A\in\GL_n(\CC)$, then
$$
\left(A,\frac1{\det A}\right)\in Y.
$$
The value of $t$ is uniquely determined by $A$, so $\pi$ is bijective.
:::

:::

::: {.pf-step #pi-isomorphism}
The bijection in step [](#pi-bijective){.pf-ref} is an isomorphism of varieties.

::: pf-proof
The projection
$$
\pi:Y\longrightarrow M_n(\CC)
$$
is the restriction of a coordinate projection, hence is a morphism.

Its inverse is
$$
\GL_n(\CC)\longrightarrow Y,
\qquad
A\longmapsto
\left(A,\frac1{\det A}\right).
$$
Now
$$
\GL_n(\CC)
=
D(\Delta)
\subseteq
\AA^{n^2}_\CC,
$$
and $\Delta^{-1}$ is a regular function on the distinguished open set
$D(\Delta)$. Hence the inverse is a morphism.
Therefore
$$
Y\cong\GL_n(\CC).
$$
:::

:::

::: {.pf-step #gln-affine-conclusion}
Consequently,
$$
\boxed{
\GL_n(\CC)\text{ is an affine variety}
}
$$
with coordinate ring
$$
\boxed{
\CC[\GL_n]
\cong
\CC[x_{ij},\Delta^{-1}].
}
$$

::: pf-proof
Step [](#y-is-affine){.pf-ref} shows that $Y$ is affine, and step [](#pi-isomorphism){.pf-ref} identifies $Y$ with
$\GL_n(\CC)$. The coordinate-ring description is the isomorphism established
in step [](#y-is-affine){.pf-ref}.
:::

:::

::: pf-qed
Step [](#gln-affine-conclusion){.pf-ref} is the required conclusion.
:::

:::

:::
