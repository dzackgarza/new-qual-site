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

::: pf

::: {.pf-step #s1}

For every $v\in\RR^n$,
$$
a_1\lVert v\rVert^2
\leq
v^{\mathsf T}Av
\leq
a_2\lVert v\rVert^2.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

For every $v\in\RR^n$,
$$
b_1\lVert v\rVert^2
\leq
v^{\mathsf T}Bv
\leq
b_2\lVert v\rVert^2.
$$

::: pf-proof

Apply the argument of step [](#s1){.pf-ref} to the real symmetric matrix $B$ and its eigenvalues in $[b_1,b_2]$.

:::

:::

::: {.pf-step #s3}

For every $v\in\RR^n$,
$$
(a_1+b_1)\lVert v\rVert^2
\leq
v^{\mathsf T}(A+B)v
\leq
(a_2+b_2)\lVert v\rVert^2.
$$

::: pf-proof

Add the lower bounds in steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, and separately add their upper bounds, using
$$
v^{\mathsf T}(A+B)v
=
v^{\mathsf T}Av+v^{\mathsf T}Bv.
$$

:::

:::

::: {.pf-step #s4}

Every eigenvalue $\lambda$ of $A+B$ lies in
$$
\boxed{[a_1+b_1,a_2+b_2]}.
$$

::: pf-proof

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
Substituting this into step [](#s3){.pf-ref} and dividing by the positive number $\lVert v\rVert^2$ gives
$$
a_1+b_1
\leq
\lambda
\leq
a_2+b_2.
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required spectral inclusion.

:::

:::

:::
