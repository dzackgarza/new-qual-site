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
<1>1. The smooth plane cubic $C$ is irreducible.

::: {.proof}
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

<1>2. The geometric genus of $C$ is
$$
\boxed{g(C)=1.}
$$

::: {.proof}
For an integral plane curve of degree $d$, the genus formula
[[D-CRVPLSING|gives]]
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

<1>3. The curve $C$ is elliptic.

::: {.proof}
Zaidenberg Definition 20.2 calls a projective curve of geometric genus $1$
an elliptic curve. Step <1>2 gives exactly this condition. Therefore
$$
\boxed{C\text{ is an elliptic curve}.}
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 verifies that the smooth cubic is an integral projective curve,
step <1>2 computes its genus, and step <1>3 applies the source definition of
an elliptic curve.
:::
:::
