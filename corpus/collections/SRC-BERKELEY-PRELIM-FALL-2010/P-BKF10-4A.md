---
schema: qual/card@1
id: P-BKF10-4A
kind: problem
title: Hermitian matrices have real eigenvalues
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded. The argument is Problem 4A, printed p. 2 of the packet, the packet the collection retains,
    transcribed as the paragraph now at the head of the solution says; the card's addition is the
    step structure and the details named there, and no claim of the problem changes. Checked: the
    packet read in its text layer at the pages named, the card's steps compared with it, and
    `qualc.authoring check` on the card. Not checked: no other card of the collection in this pass.
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

The argument is Problem 4A of the retained Berkeley preliminary-exam solution packet, `assets/attachments/f10solutions.pdf`, transcribed: $\overline A=A^T$ says $A$ is Hermitian, and for a unit eigenvector $x$ with eigenvalue $\lambda$ the chain $\lambda=(\lambda x,x)=(Ax,x)=(x,A^{T}x)=(x,Ax)=(x,\lambda x)=\overline\lambda$ forces $\lambda$ real. What the card adds is the step structure and the verification that $A^*=A$ from the hypothesis, not the argument.
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
