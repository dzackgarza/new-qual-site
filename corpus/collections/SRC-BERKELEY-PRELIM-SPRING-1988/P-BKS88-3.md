---
schema: qual/card@1
id: P-BKS88-3
kind: problem
title: Rational solutions of rational homogeneous linear systems
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 1988 preliminary examination.
---

::: {.problem}
If a finite homogeneous system of linear equations with rational coefficients has a nontrivial complex solution, need it have a nontrivial rational solution?
Give a proof or a counterexample.
:::

::: {.solution}
Write the system as $Ax=0$, where $A$ is an $m\times n$ matrix with entries in $\QQ$.

::: pf

::: pf-step
If $Ax=0$ has a nonzero solution in $\CC^n$, then the reduced row-echelon form of $A$ has at least one free column.

::: pf-proof
Perform Gaussian elimination on $A$ using rational row operations. The resulting reduced row-echelon matrix $R$ has rational entries and defines the same homogeneous system over both $\QQ$ and $\CC$. If every column were a pivot column, then $Rx=0$ would have only the zero solution over every field containing $\QQ$, contradicting the assumed nonzero complex solution. Hence at least one column is free.
:::

:::

::: pf-step
The system $Ax=0$ has a nonzero solution in $\QQ^n$.

::: pf-proof
Choose one free variable in $Rx=0$ to be $1$ and all other free variables to be $0$. Back-substitution expresses every pivot variable as a rational linear combination of these chosen rational values, because all entries of $R$ are rational. Thus one obtains a vector $q\in\QQ^n$ satisfying $Rq=0$. The chosen free coordinate of $q$ is $1$, so $q\neq 0$. Since row operations preserve the solution set of a homogeneous system, $Aq=0$ as well.
:::

:::

:::

:::
