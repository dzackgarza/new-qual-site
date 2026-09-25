---
schema: qual/card@1
id: P-BKF93-7
kind: problem
title: Critical points of the determinant map on real matrices
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Expressed the differential of det through cofactors and identified its
    vanishing with the vanishing of every (n-1)-minor, equivalently rank at
    most n-2.
---

::: {.problem}
Identify $M_n(\mathbb R)$ with $\mathbb R^{n^2}$ and let
\[
F:M_n(\mathbb R)\to\mathbb R,
\qquad
F(X)=\det X.
\]
For $n\ge2$, find all critical points of $F$, i.e. all matrices $X$ such that
\[
DF(X)=0.
\]
:::

::: {.solution}
For $1\leq i,j\leq n$, let $C_{ij}(X)$ denote the $(i,j)$-cofactor of
$X$.

<1>1. For every $H=(h_{ij})\in M_n(\RR)$,
$$
DF(X)[H]
=
\sum_{i=1}^n\sum_{j=1}^n C_{ij}(X)h_{ij}.
$$

::: {.proof}
The determinant is a polynomial in the matrix entries. Its partial derivative
with respect to the $(i,j)$ entry is the corresponding cofactor:
$$
\frac{\partial\det}{\partial x_{ij}}(X)=C_{ij}(X).
$$
Therefore the differential in the direction
$H=(h_{ij})$ is the displayed linear combination.
:::

<1>2. One has
$$
DF(X)=0
$$
if and only if
$$
C_{ij}(X)=0
\qquad\text{for every }i,j.
$$

::: {.proof}
If every cofactor vanishes, step <1>1 gives $DF(X)[H]=0$ for every $H$.
Conversely, if $DF(X)=0$, apply step <1>1 to the matrix unit $E_{ij}$.
Then
$$
0
=
DF(X)[E_{ij}]
=
C_{ij}(X),
$$
so every cofactor vanishes.
:::

<1>3. Every cofactor of $X$ vanishes if and only if
$$
\operatorname{rank}X\leq n-2.
$$

::: {.proof}
Up to sign, the cofactors $C_{ij}(X)$ are exactly the determinants of the
$(n-1)\times(n-1)$ minors obtained by deleting one row and one column. Thus
all cofactors vanish exactly when every $(n-1)\times(n-1)$ minor vanishes.
By the minor characterization of matrix rank, this is equivalent to
$\operatorname{rank}X<n-1$, hence to
$\operatorname{rank}X\leq n-2$.
:::

<1>4. The set of critical points of $F$ is
$$
\boxed{\{X\in M_n(\RR):\operatorname{rank}X\leq n-2\}}.
$$

::: {.proof}
By step <1>2, $X$ is critical exactly when all of its cofactors vanish. Step
<1>3 identifies that condition with $\operatorname{rank}X\leq n-2$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives all critical points.
:::
:::
