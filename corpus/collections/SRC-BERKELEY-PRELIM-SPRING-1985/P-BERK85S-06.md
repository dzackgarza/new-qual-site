---
schema: qual/card@1
id: P-BERK85S-06
kind: problem
title: Spectral interval bound for the sum of two Hermitian matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Applied the spectral theorem to bound the Rayleigh quotients of A and B,
    then evaluated the Rayleigh quotient of A+B at an eigenvector.
---

::: {.problem}
Let $A,B$ be Hermitian $n\times n$ matrices. Suppose every eigenvalue of $A$ lies in $[a,a']$ and every eigenvalue of $B$ lies in $[b,b']$. Prove that every eigenvalue of $A+B$ lies in
\[
[a+b,a'+b'].
\]
:::

::: {.solution}
<1>1. For every $v\in\CC^n$,
$$
a\norm{v}^2
\leq
v^*Av
\leq
a'\norm{v}^2.
$$

::: {.proof}
By the spectral theorem, there is an orthonormal eigenbasis
$e_1,\ldots,e_n$ for $A$, with corresponding eigenvalues
$\lambda_j\in[a,a']$. Write
$$
v=\sum_{j=1}^n c_je_j.
$$
Then
$$
v^*Av
=
\sum_{j=1}^n\lambda_j\abs{c_j}^2,
\qquad
\norm{v}^2
=
\sum_{j=1}^n\abs{c_j}^2.
$$
Bounding every $\lambda_j$ between $a$ and $a'$ gives the claim.
:::

<1>2. For every $v\in\CC^n$,
$$
b\norm{v}^2
\leq
v^*Bv
\leq
b'\norm{v}^2.
$$

::: {.proof}
Apply the argument of step <1>1 to the Hermitian matrix $B$, whose
eigenvalues lie in $[b,b']$.
:::

<1>3. For every $v\in\CC^n$,
$$
(a+b)\norm{v}^2
\leq
v^*(A+B)v
\leq
(a'+b')\norm{v}^2.
$$

::: {.proof}
Add the inequalities from steps <1>1 and <1>2 and use
$$
v^*(A+B)v=v^*Av+v^*Bv.
$$
:::

<1>4. Every eigenvalue $\lambda$ of $A+B$ satisfies
$$
\boxed{a+b\leq\lambda\leq a'+b'}.
$$

::: {.proof}
The matrix $A+B$ is Hermitian, so its eigenvalues are real. Let
$v\neq0$ satisfy
$$
(A+B)v=\lambda v.
$$
Then
$$
v^*(A+B)v
=
\lambda\norm{v}^2.
$$
Apply step <1>3 and divide by the positive number $\norm{v}^2$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required spectral interval bound.
:::
:::
