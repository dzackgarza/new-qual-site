---
schema: qual/card@1
id: P-AGXVARTANGENTDIM
kind: problem
title: The tangent space has dimension equal to $\dim X$ exactly at smooth points
classification:
  areas:
  - algebraic-geometry
  topics:
  - Tangent Spaces
  - Smoothness
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Definitions 6.1 and the first clause of Exercises 6.2 in
    the recorded source. Over k=C, the source defines T_pX as the kernel of
    the Jacobian differential and asks that its dimension equal d exactly at
    smooth points.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the affine embedding X subset A^n_C and the source field explicit.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Combined rank-nullity for the Jacobian differential with the source
    definition that smoothness means Jacobian rank n-d.
---

::: {.problem}
Let
$$
X\subseteq\AA^n_\CC
$$
be an affine variety of dimension $d$, and let $p\in X$. Show that
$$
\dim_\CC T_pX=d
$$
if $p$ is smooth, while
$$
\dim_\CC T_pX>d
$$
if $p$ is singular.
:::

::: {.solution}
Choose generators
$$
I(X)=(f_1,\ldots,f_m)
$$
and let
$$
F=(f_1,\ldots,f_m):\AA^n_\CC\longrightarrow\AA^m_\CC.
$$
Write
$$
r=\rank J_F(p),
$$
where $J_F(p)$ is the Jacobian matrix at $p$.

<1>1. The Zariski tangent space satisfies
$$
T_pX=\ker dF(p)
$$
and therefore
$$
\boxed{\dim_\CC T_pX=n-r.}
$$

::: {.proof}
The Zariski tangent space at $p$ is the kernel of the differentials of
generators of $I(X)$, that is, $T_pX=\ker dF(p)$. The linear map
$$
dF(p):\CC^n\longrightarrow\CC^m
$$
has matrix $J_F(p)$ and rank $r$. Rank-nullity gives
$$
\dim_\CC\ker dF(p)
=
n-r.
$$
:::

<1>2. If $p$ is smooth, then
$$
\dim_\CC T_pX=d.
$$

::: {.proof}
By the Jacobian criterion,
$$
p\text{ smooth}
\quad\Longleftrightarrow\quad
r=n-d.
$$
Substituting this into step <1>1 gives
$$
\dim_\CC T_pX
=
n-(n-d)
=
d.
$$
:::

<1>3. If $p$ is singular, then
$$
\dim_\CC T_pX>d.
$$

::: {.proof}
At a singular point the Jacobian rank is strictly smaller than the
codimension:
$$
r<n-d.
$$
Hence
$$
n-r
>
n-(n-d)
=
d.
$$
Step <1>1 identifies the left-hand side with $\dim_\CC T_pX$.
:::

<1>4. Therefore
$$
\boxed{
p\text{ is smooth}
\quad\Longleftrightarrow\quad
\dim_\CC T_pX=d.
}
$$

::: {.proof}
Step <1>2 gives equality at smooth points, while step <1>3 shows that every
singular point has strictly larger tangent dimension.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove both assertions.
:::
:::
