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

The Jacobian criterion at a smooth point says precisely that these
$n-d$ independent equations form a local defining system for the reduced
variety $X$. Equivalently, the holomorphic Implicit Function Theorem
identifies a neighborhood of $p$ in $X$ with an open subset of $\CC^d$.
Thus $X$ itself is a real smooth submanifold of dimension $2d$ near $p$.
:::

<1>4. Conversely, if $X$ is a smooth real submanifold of dimension $2d$
near $p$, then
$$
\rank_\RR dF_\RR(p)=2(n-d).
$$

::: {.proof}
For a reduced complex analytic set which is a smooth submanifold near a
point, the tangent-space form of the Implicit Function Theorem identifies
its real tangent space with the common kernel of the differentials of its
local defining ideal:
$$
T_p^\RR X
=
\ker dF_\RR(p).
$$
By hypothesis,
$$
\dim_\RR T_p^\RR X=2d.
$$
Rank-nullity therefore gives
$$
\rank_\RR dF_\RR(p)
=
2n-2d
=
2(n-d).
$$
:::

<1>5. Under the hypothesis of step <1>4, the point $p$ is algebraically
smooth.

::: {.proof}
By step <1>2 and step <1>4,
$$
2\rank_\CC J_\CC(p)
=
2(n-d).
$$
Hence
$$
\rank_\CC J_\CC(p)=n-d.
$$
Step <1>1 now gives that $p$ is smooth.
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
