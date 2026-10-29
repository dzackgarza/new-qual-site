---
schema: qual/card@1
id: P-CDRT6
kind: problem
title: Diagonalizable does not imply distinct eigenvalues
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Counterexamples
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

::: {.problem}
Does diagonalizable imply distinct eigenvalues?
:::

::: {.solution}

::: pf

::: pf-step

$\boxed{\text{No}}$: the identity matrix $I_2$ is diagonalizable but has the repeated eigenvalue $1$.

::: pf-proof

$I_2$ is diagonal, hence diagonalizable, and its characteristic polynomial is $(x-1)^2$, so its only eigenvalue is $1$, with algebraic multiplicity $2$. Diagonalizability asks for a basis of eigenvectors, not for distinct eigenvalues.

:::

:::

:::

:::
