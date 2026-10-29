---
schema: qual/card@1
id: E-NUJ7W
kind: problem
title: Nonzero nilpotent matrices are not diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Diagonalization
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that a nonzero nilpotent matrix $A$ is not diagonalizable over any field.
:::

::: {.hint}
Every eigenvalue of a nilpotent matrix is $0$, so a diagonal form of $A$ would be $0$.
:::

::: {.solution}

::: pf

::: {.pf-step #only-eigenvalue-zero}
The only eigenvalue of a nilpotent matrix is $0$.

::: pf-proof
Choose $N\ge1$ with $A^N=0$. If $Av=\lambda v$ for some nonzero vector $v$, then
$$
0=A^Nv=\lambda^N v.
$$
Since $v\neq0$ and the scalars form a field, $\lambda^N=0$, hence $\lambda=0$.
:::

:::

::: {.pf-step #diagonalizable-implies-zero}
If a nilpotent matrix $A$ is diagonalizable, then $A=0$.

::: pf-proof
If $A$ is diagonalizable, there is an invertible matrix $P$ and a diagonal matrix $D$ such that
$$
A=PDP^{-1}.
$$
The diagonal entries of $D$ are the eigenvalues of $A$. By step [](#only-eigenvalue-zero){.pf-ref} every eigenvalue is $0$, so $D=0$. Therefore
$$
A=P0P^{-1}=0.
$$
:::

:::

::: pf-step
Hence every nonzero nilpotent matrix is not diagonalizable.

::: pf-proof
If a nonzero nilpotent matrix were diagonalizable, step [](#diagonalizable-implies-zero){.pf-ref} would force it to equal $0$, a contradiction.
:::

:::

:::

:::

::: {.remark}
Equivalently, if $r$ is the nilpotency index of a nonzero nilpotent matrix $A$, then $A^r=0$ and $A^{r-1}\neq0$, so the minimal polynomial of $A$ divides $x^r$ but not $x^{r-1}$ and equals $x^r$. Since $A\neq0$, one has $r\ge2$, so the minimal polynomial is not a product of distinct linear factors, and $A$ is not diagonalizable.
:::
