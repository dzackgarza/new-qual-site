---
schema: qual/card@1
id: P-AGXVARSMOOTHCUBIC
kind: problem
title: Smooth plane cubics are elliptic curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plane Curves
  - Elliptic Curves
  - Genus
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Definitions 20.2 and the corresponding clause of Exercises
    20.3 in the recorded source. The source defines an elliptic curve as a
    projective curve of geometric genus 1 and asks that every smooth plane
    cubic be elliptic.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the algebraically closed ground field explicit on the standalone
    card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked that a reducible plane cubic would have a singular intersection
    point, then applied the plane-curve genus formula with no singularity
    corrections to obtain genus 1.
---

::: {.problem}
Let
$$
C\subseteq\PP^2_k
$$
be a smooth plane cubic over the algebraically closed ground field $k$.
Show that $C$ is an elliptic curve.
:::

::: {.solution}

::: pf

::: {.pf-step #c-irreducible}
The smooth plane cubic $C$ is irreducible.

::: pf-proof
Let
$$
C=V(F),
$$
where $F$ is a homogeneous cubic. Suppose that $F$ were reducible. Then
$$
F=GH
$$
with $G$ and $H$ nonconstant homogeneous polynomials of positive degree.

Over the algebraically closed field $k$, the projective plane curves
$$
V(G)
\qquad\text{and}\qquad
V(H)
$$
have a common point $P$ by Bézout's theorem. At such a point,
$$
G(P)=H(P)=0.
$$
For every homogeneous coordinate $x_i$,
$$
\frac{\partial F}{\partial x_i}
=
H\frac{\partial G}{\partial x_i}
+
G\frac{\partial H}{\partial x_i},
$$
so
$$
\frac{\partial F}{\partial x_i}(P)=0.
$$
Thus $P$ is singular on $C$, contradicting smoothness. Therefore $F$ is
irreducible and $C$ is an integral projective curve.
:::

:::

::: {.pf-step #genus-one}
The geometric genus of $C$ is
$$
\boxed{g(C)=1.}
$$

::: pf-proof
For an integral plane curve of degree $d$, the genus formula
[[D-CRVPLSING]] gives
$$
g
=
\binom{d-1}{2}
-
\sum_{p\in\operatorname{Sing}(C)}\delta_p.
$$
Here
$$
d=3
$$
and $C$ is smooth, so the singularity sum is empty. Hence
$$
g(C)
=
\binom{2}{2}
=
1.
$$
:::

:::

::: {.pf-step #c-elliptic}
The curve $C$ is elliptic.

::: pf-proof
An elliptic curve is a projective curve of geometric genus $1$, and step
[](#genus-one){.pf-ref} gives this condition. Therefore
$$
\boxed{C\text{ is an elliptic curve}.}
$$
:::

:::

::: pf-qed
Step [](#c-irreducible){.pf-ref} verifies that the smooth cubic is an integral projective curve,
step [](#genus-one){.pf-ref} computes its genus, and step [](#c-elliptic){.pf-ref} concludes that it is an elliptic
curve.
:::

:::

:::
