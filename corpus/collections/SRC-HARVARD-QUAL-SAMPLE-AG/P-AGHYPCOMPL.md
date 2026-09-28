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

<1>1. The complement of $H$ is the standard projective open
\[
\mathbb P^2\setminus H=D_+(F).
\]
::: {.proof}
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

<1>2. For every homogeneous $F$ of positive degree,
\[
\boxed{
D_+(F)\cong\operatorname{Spec}(S_F)_0,
}
\]
where $(S_F)_0$ is the degree-zero part of the graded localization $S_F$.
::: {.proof}
This is the standard affine-chart construction for $\operatorname{Proj}S$.

Explicitly, a homogeneous prime
\[
\mathfrak p\in D_+(F)
\]
extends to a homogeneous prime $\mathfrak pS_F$ of the localization, and taking its degree-zero part gives a prime ideal of $(S_F)_0$.

Conversely, a prime of $(S_F)_0$ determines the corresponding homogeneous prime of $S$ not containing $F$.  These identifications are inverse and identify the structure sheaves, yielding the displayed isomorphism of schemes.
:::

<1>3. Hence
\[
\boxed{
\mathbb P^2_k\setminus H\text{ is affine}.
}
\]
::: {.proof}
By <1>1 the complement is $D_+(F)$, and by <1>2 this is the spectrum of the ring $(S_F)_0$.
:::

<1>4. The conclusion does not require $H$ to be smooth, reduced, or irreducible.
::: {.proof}
The proof used only that $H$ is cut out scheme-theoretically by one homogeneous equation $F$.  Repeated factors or a factorization of $F$ do not affect the fact that its complement is the standard affine open $D_+(F)$.
:::

<1>5. For example, if
\[
H=V_+(x_0),
\]
then
\[
D_+(x_0)\cong\operatorname{Spec}k\!\left[\frac{x_1}{x_0},\frac{x_2}{x_0}\right]
\cong\mathbb A^2_k.
\]
::: {.proof}
Here
\[
(S_{x_0})_0
=k[x_1/x_0,x_2/x_0],
\]
which is the usual affine chart of projective space.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>3 answers the question; step <1>4 records the full generality of the argument.
:::
:::
