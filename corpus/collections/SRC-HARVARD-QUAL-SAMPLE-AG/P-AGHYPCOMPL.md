---
schema: qual/card@1
id: P-AGHYPCOMPL
kind: problem
title: The complement of a hypersurface in $\PP^2$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Hypersurfaces
  - Projective Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Poonen's question about the complement of a hypersurface in projective space.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Is the complement of a hypersurface in $\PP^2$ affine?
:::

::: {.solution}
Yes.

Let
\[
S=k[x_0,x_1,x_2],
\qquad
\mathbb P^2_k=\operatorname{Proj}S,
\]
and let the hypersurface be
\[
H=V_+(F)
\]
for a nonzero homogeneous polynomial $F\in S$ of positive degree.

::: pf

::: {.pf-step #complement-is-dplus}
The complement of $H$ is the standard projective open
\[
\mathbb P^2\setminus H=D_+(F).
\]

::: pf-proof
By definition,
\[
V_+(F)
=\{\mathfrak p\in\operatorname{Proj}S:F\in\mathfrak p\}.
\]
Its complement is therefore
\[
D_+(F)
=\{\mathfrak p\in\operatorname{Proj}S:F\notin\mathfrak p\}.
\]
:::

:::

::: {.pf-step #dplus-affine-chart}
For every homogeneous $F$ of positive degree,
\[
\boxed{
D_+(F)\cong\operatorname{Spec}(S_F)_0,
}
\]
where $(S_F)_0$ is the degree-zero part of the graded localization $S_F$.

::: pf-proof
This is the standard affine-chart construction for $\operatorname{Proj}S$.

Explicitly, a homogeneous prime
\[
\mathfrak p\in D_+(F)
\]
extends to a homogeneous prime $\mathfrak pS_F$ of the localization, and taking its degree-zero part gives a prime ideal of $(S_F)_0$.

Conversely, a prime of $(S_F)_0$ determines the corresponding homogeneous prime of $S$ not containing $F$.  These identifications are inverse and identify the structure sheaves, yielding the displayed isomorphism of schemes.
:::

:::

::: {.pf-step #complement-affine}
Hence
\[
\boxed{
\mathbb P^2_k\setminus H\text{ is affine}.
}
\]

::: pf-proof
By step [](#complement-is-dplus){.pf-ref} the complement is $D_+(F)$, and by step [](#dplus-affine-chart){.pf-ref} this is the spectrum of the ring $(S_F)_0$.
:::

:::

::: {.pf-step #general-hypersurface-complement}
The complement of every hypersurface $V_+(F)$ in $\mathbb P^2_k$ is affine, whether $F$ is irreducible, reducible, or has repeated factors, and whether $V_+(F)$ is smooth or singular.

::: pf-proof
Steps [](#complement-is-dplus){.pf-ref}, [](#dplus-affine-chart){.pf-ref} and [](#complement-affine){.pf-ref} use only that $H$ is cut out scheme-theoretically by one homogeneous equation $F$ of positive degree, so its complement is the standard affine open $D_+(F)$.
:::

:::

::: pf-step
For example, if
\[
H=V_+(x_0),
\]
then
\[
D_+(x_0)\cong\operatorname{Spec}k\!\left[\frac{x_1}{x_0},\frac{x_2}{x_0}\right]
\cong\mathbb A^2_k.
\]

::: pf-proof
Here
\[
(S_{x_0})_0
=k[x_1/x_0,x_2/x_0],
\]
which is the usual affine chart of projective space.
:::

:::

::: pf-qed
Step [](#complement-affine){.pf-ref} answers the question; step [](#general-hypersurface-complement){.pf-ref} records the full generality of the argument.
:::

:::
:::
