---
schema: qual/card@1
id: P-TRIV-LA16
kind: problem
title: Reflection matrices in $\RR^3$ across a point, an axis and a plane
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 16, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Construct the matrix that performs a reflection in $\RR ^ { 3 }$

(a) across the origin O,

(b) across the axis $O z .$

(c) across the plane $x O y$
:::

::: {.solution}

::: pf

::: pf-step

Reflection through the origin sends
$$
(x,y,z)
\longmapsto
(-x,-y,-z).
$$


::: pf-proof

The origin is the midpoint of a point and its reflected image, so every
coordinate changes sign.

:::

:::

::: {.pf-step #s1-2}

Therefore the matrix for part (a) is
$$
\boxed{
R_O=
\begin{pmatrix}
-1&0&0\\
0&-1&0\\
0&0&-1
\end{pmatrix}.
}
$$


::: pf-proof

Multiplying a vector by this diagonal matrix negates all three coordinates.

:::

:::

::: {.pf-step #s1-3}

Reflection across the $z$-axis sends
$$
(x,y,z)
\longmapsto
(-x,-y,z).
$$


::: pf-proof

The component parallel to the $z$-axis is fixed, while the perpendicular
component in the $xy$-plane changes sign.

:::

:::

::: {.pf-step #s1-4}

Therefore the matrix for part (b) is
$$
\boxed{
R_{Oz}=
\begin{pmatrix}
-1&0&0\\
0&-1&0\\
0&0&1
\end{pmatrix}.
}
$$


::: pf-proof

This matrix implements exactly the coordinate transformation in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Reflection across the $xy$-plane sends
$$
(x,y,z)
\longmapsto
(x,y,-z).
$$


::: pf-proof

The coordinates tangent to the plane are fixed, while the normal coordinate
$z$ changes sign.

:::

:::

::: {.pf-step #s1-6}

Therefore the matrix for part (c) is
$$
\boxed{
R_{xOy}=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&-1
\end{pmatrix}.
}
$$


::: pf-proof

This matrix implements the transformation in step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref}, and [](#s1-6){.pf-ref} give the three requested reflection matrices.

:::

:::

:::
