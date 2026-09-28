---
schema: qual/card@1
id: P-AGXVARSMOOTHMFLD
kind: problem
title: Smooth points are exactly the points where $X$ is locally a submanifold
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smoothness
  - Submanifolds
  - Local Structure
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Definitions 6.1 and the corresponding clause of Exercises
    6.2 in the recorded source. Over k=C it asks that p be smooth exactly when
    X is a smooth submanifold of A^n_C=R^{2n} near p, with the Implicit
    Function Theorem as hint.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the complex ground field, dimension d, and the resulting real
    submanifold dimension 2d explicit on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Used the Jacobian criterion, observed that a complex-linear map of complex
    rank r has real rank 2r, and applied the real/holomorphic Implicit Function
    Theorem in both directions.
---

::: {.problem}
Let
$$
X\subseteq\AA^n_\CC
$$
be an affine variety of complex dimension $d$, and let $p\in X$. Show that
$p$ is smooth if and only if, in a neighborhood of $p$,
$$
X\subseteq\CC^n\cong\RR^{2n}
$$
is a smooth real submanifold of dimension $2d$.
:::

::: {.solution}
Choose generators
$$
I(X)=(f_1,\ldots,f_m)
$$
and write
$$
F=(f_1,\ldots,f_m):\CC^n\longrightarrow\CC^m.
$$
Let
$$
J_\CC(p)
=
\left(
\frac{\partial f_i}{\partial x_j}(p)
\right)
$$
be the complex Jacobian matrix.

<1>1. The point $p$ is algebraically smooth exactly when
$$
\rank_\CC J_\CC(p)=n-d.
$$

::: {.proof}
This is the Jacobian criterion [[PR-MORJAC]] for the affine variety $X$.
:::

<1>2. Viewed as a real map
$$
F_\RR:\RR^{2n}\longrightarrow\RR^{2m},
$$
the differential at $p$ satisfies
$$
\rank_\RR dF_\RR(p)
=
2\rank_\CC J_\CC(p).
$$

::: {.proof}
The differential
$$
dF(p):\CC^n\longrightarrow\CC^m
$$
is complex linear because each $f_i$ is holomorphic. A complex-linear map of
complex rank $r$ has image a complex vector space of complex dimension $r$,
hence a real vector space of dimension $2r$. Therefore its underlying real
linear map has rank $2r$.
:::

<1>3. If $p$ is algebraically smooth, then $X$ is a smooth real submanifold
of dimension $2d$ near $p$.

::: {.proof}
Assume $p$ is smooth. By step <1>1,
$$
\rank_\CC J_\CC(p)=n-d.
$$
Choose $n-d$ of the defining functions whose differentials are complex
linearly independent at $p$, and write
$$
G:\CC^n\longrightarrow\CC^{n-d}
$$
for the resulting submap.

By step <1>2,
$$
\rank_\RR dG_\RR(p)=2(n-d).
$$
The real Implicit Function Theorem therefore makes
$$
G^{-1}(0)
$$
a smooth real submanifold of dimension
$$
2n-2(n-d)=2d
$$
near $p$.

The holomorphic Implicit Function Theorem makes $G^{-1}(0)$, near $p$, a
connected complex submanifold $M$ of dimension $d$. It contains $X$ near $p$,
since the components of $G$ are among the $f_i$. A closed analytic subset of
dimension $d$ of a connected $d$-dimensional complex manifold is the whole
manifold, so $X=M$ near $p$, and $X$ is a smooth real submanifold of
dimension $2d$ there.
:::

<1>4. If $X$ is a smooth real submanifold $M$ of dimension $2d$ near $p$,
then $X$ is a complex submanifold of dimension $d$ near $p$.

::: {.proof}
The smooth points of $X$ are dense in $X$. At a smooth point $q$ near $p$,
step <1>3 makes $X$ a complex submanifold of dimension $d$ equal to $M$ near
$q$, so $T_qM$ is a complex subspace of $\CC^n$. Complex subspaces of real
dimension $2d$ form a closed set, and $T_qM$ depends continuously on $q$, so
$T_pM$ is a complex subspace too.

Let $\pi$ be the complex-linear projection of $\CC^n$ onto $T_pM$ along a
complex complement $N$. Then $d\pi$ is the identity on $T_pM$, so near $p$,
$M$ is the graph of a smooth map $\varphi$ from an open set of $T_pM\cong\CC^d$
to $N$. At a smooth point $q$ of $X$ near $p$, $M$ is a complex submanifold
whose tangent space projects isomorphically to $T_pM$, so $\varphi$ is
holomorphic near $\pi(q)$ by the holomorphic Inverse Function Theorem. So the
derivative of $\varphi$ is complex linear on a dense set, hence everywhere by
continuity, and $\varphi$ is holomorphic. Its graph $M$ is a complex
submanifold of dimension $d$.
:::

<1>5. Under the hypothesis of step <1>4, the point $p$ is algebraically
smooth.

::: {.proof}
By step <1>4 the analytic local ring of $X$ at $p$ is the ring of convergent
power series in $d$ variables. The algebraic local ring $\OO_{X,p}$ and the
analytic local ring have isomorphic completions [@Mum94, §I.10], so
$\widehat{\OO_{X,p}}\cong\CC[[z_1,\ldots,z_d]]$ is regular. A noetherian local
ring is regular exactly when its completion is, so $\OO_{X,p}$ is regular of
dimension $d$, and $p$ is smooth.
:::

<1>6. Therefore
$$
\boxed{
p\text{ is smooth}
\quad\Longleftrightarrow\quad
X\text{ is locally a smooth real }2d\text{-manifold near }p.
}
$$

::: {.proof}
Step <1>3 proves the forward implication, and steps <1>4--<1>5 prove the
converse.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required equivalence.
:::
:::
