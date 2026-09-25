---
schema: qual/card@1
id: P-BKF88-9
kind: problem
title: Spectral bounds for a sum of symmetric matrices
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 in the deterministic MinerU Flash extraction assets/attachments/Fall88_extracted.md.
---

::: {.problem}
Let $A,B$ be real symmetric $n\times n$ matrices.
Assume all eigenvalues of $A$ lie in $[a_1,a_2]$ and all eigenvalues of $B$ lie in $[b_1,b_2]$.
Prove that every eigenvalue of $A+B$ lies in
\[
[a_1+b_1,a_2+b_2].
\]
:::

::: {.solution}
<1>1. For every $v\in\RR^n$,
$$
a_1\lVert v\rVert^2
\leq
v^{\mathsf T}Av
\leq
a_2\lVert v\rVert^2.
$$

::: {.proof}
By the spectral theorem, there is an orthonormal basis $u_1,\ldots,u_n$ of eigenvectors of $A$, with corresponding eigenvalues $\lambda_i\in[a_1,a_2]$. Write
$$
v=\sum_{i=1}^n c_i u_i.
$$
Then
$$
v^{\mathsf T}Av
=
\sum_{i=1}^n\lambda_i c_i^2,
\qquad
\lVert v\rVert^2
=
\sum_{i=1}^n c_i^2.
$$
Bounding each $\lambda_i$ between $a_1$ and $a_2$ gives the claimed inequalities.
:::

<1>2. For every $v\in\RR^n$,
$$
b_1\lVert v\rVert^2
\leq
v^{\mathsf T}Bv
\leq
b_2\lVert v\rVert^2.
$$

::: {.proof}
Apply the argument of step <1>1 to the real symmetric matrix $B$ and its eigenvalues in $[b_1,b_2]$.
:::

<1>3. For every $v\in\RR^n$,
$$
(a_1+b_1)\lVert v\rVert^2
\leq
v^{\mathsf T}(A+B)v
\leq
(a_2+b_2)\lVert v\rVert^2.
$$

::: {.proof}
Add the lower bounds in steps <1>1 and <1>2, and separately add their upper bounds, using
$$
v^{\mathsf T}(A+B)v
=
v^{\mathsf T}Av+v^{\mathsf T}Bv.
$$
:::

<1>4. Every eigenvalue $\lambda$ of $A+B$ lies in
$$
\boxed{[a_1+b_1,a_2+b_2]}.
$$

::: {.proof}
The matrix $A+B$ is real symmetric, so let $v\neq0$ be an eigenvector with
$$
(A+B)v=\lambda v.
$$
Then
$$
v^{\mathsf T}(A+B)v
=
\lambda\lVert v\rVert^2.
$$
Substituting this into step <1>3 and dividing by the positive number $\lVert v\rVert^2$ gives
$$
a_1+b_1
\leq
\lambda
\leq
a_2+b_2.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required spectral inclusion.
:::
:::
