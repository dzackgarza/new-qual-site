---
schema: qual/card@1
id: P-TRIV-LA45
kind: problem
title: Positive definiteness of $9x_1^2+6x_1x_2+6x_2^2+8x_2x_3+4x_3^2$
classification:
  areas: [prelim]
  topics:
  - Quadratic Forms
  - Positive Definite Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 45, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find if the quadratic form $f(\vec{x}) = 9x_1^2 + 6x_1x_2 + 6x_2^2 + 8x_2x_3 + 4x_3^2$ is positive definite or not.
:::

::: {.solution}

::: pf

::: pf-step

The symmetric matrix of the quadratic form is
$$
Q=
\begin{pmatrix}
9&3&0\\
3&6&4\\
0&4&4
\end{pmatrix}.
$$


::: pf-proof

For a symmetric quadratic form
$$
x^TQx,
$$
the coefficient of $x_ix_j$ for $i\neq j$ is $2q_{ij}$. Hence
$$
q_{12}=3,
\qquad
q_{23}=4,
\qquad
q_{13}=0,
$$
with the diagonal entries read directly from the square terms.

:::

:::

::: {.pf-step #s1-2}

The first leading principal minor is
$$
\Delta_1=9>0.
$$


::: pf-proof

This is the upper-left $1\times1$ determinant.

:::

:::

::: {.pf-step #s1-3}

The second leading principal minor is
$$
\Delta_2
=
\det
\begin{pmatrix}
9&3\\
3&6
\end{pmatrix}
=
45>0.
$$


::: pf-proof

Compute
$$
9\cdot6-3\cdot3
=
54-9
=45.
$$

:::

:::

::: {.pf-step #s1-4}

The third leading principal minor is
$$
\Delta_3
=
\det Q
=
36>0.
$$


::: pf-proof

Expand along the first row:
$$
\begin{aligned}
\det Q
&=
9
\det
\begin{pmatrix}
6&4\\
4&4
\end{pmatrix}
-
3
\det
\begin{pmatrix}
3&4\\
0&4
\end{pmatrix}\\
&=
9(24-16)-3(12)\\
&=
72-36\\
&=36.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

By Sylvester's criterion, the quadratic form is positive definite.


::: pf-proof

For a real symmetric matrix, Sylvester's criterion states that the associated
quadratic form is positive definite exactly when all leading principal minors
are positive. Steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} verify this condition.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{f\text{ is positive definite}.}
$$


::: pf-proof

This is step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
