---
schema: qual/card@1
id: P-BKF10-4A
kind: problem
title: Hermitian matrices have real eigenvalues
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 4A of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the equivalence with A*=A and the quadratic-form calculation
    showing each eigenvalue equals its complex conjugate.
---

::: {.problem}
If the complex conjugate of a complex matrix is equal to its transpose, prove that all its eigenvalues are real.
:::

::: {.solution}
Let $A$ be the matrix in the problem.

::: pf

::: {.pf-step #s1}

The hypothesis implies that $A$ is Hermitian:
$$
A^*=A.
$$

::: pf-proof

The conjugate transpose is $A^*=(\overline A)^T$. The hypothesis
$\overline A=A^T$ therefore gives
$$
A^*=(\overline A)^T=(A^T)^T=A.
$$

:::

:::

::: {.pf-step #s2}

For every vector $v$, the scalar $v^*Av$ is real.

::: pf-proof

By step [](#s1){.pf-ref},
$$
\overline{v^*Av}
=(v^*Av)^*
=v^*A^*v
=v^*Av.
$$
A complex number equal to its conjugate is real.

:::

:::

::: {.pf-step #s3}

Every eigenvalue $\lambda$ of $A$ is real.

::: pf-proof

Let $v\ne0$ satisfy $Av=\lambda v$. Multiplying on the left by $v^*$
gives
$$
v^*Av=\lambda v^*v.
$$
By step [](#s2){.pf-ref}, the left-hand side is real, while
$$
v^*v=\sum_j\abs{v_j}^2>0
$$
is a positive real number. Hence
$$
\lambda=\frac{v^*Av}{v^*v}\in\RR.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves that all eigenvalues of $A$ are real.

:::

:::

:::
