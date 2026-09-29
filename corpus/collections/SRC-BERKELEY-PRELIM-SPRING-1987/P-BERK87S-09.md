---
schema: qual/card@1
id: P-BERK87S-09
kind: problem
title: Rational linear systems solvable over $\mathbb C$ are solvable over $\mathbb Q$
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
    Row-reduced the augmented matrix using rational elementary operations.
    Existence of a complex solution excludes an inconsistent row; setting
    the free variables to zero leaves rational pivot variables, producing a
    rational solution.
---

::: {.problem}
Let $A$ be an $m\times n$ matrix with rational entries and let $b\in\mathbb Q^m$. Prove or disprove: if
\[
Ax=b
\]
has a solution $x\in\mathbb C^n$, then it has a solution $x\in\mathbb Q^n$.
:::

::: {.solution}
::: pf

::: {.pf-step #reduction-in-q}
Elementary row reduction of the augmented matrix
$$
[A\mid b]
$$
can be performed entirely inside $\QQ$.

::: pf-proof
All entries of $A$ and $b$ lie in $\QQ$. The elementary row operations
used in Gaussian elimination are:

- interchange two rows;
- multiply a row by a nonzero entry's inverse; and
- add a rational multiple of one row to another.

The field $\QQ$ is closed under these operations. Hence the resulting
row-echelon matrix still has rational entries.
:::

:::

::: {.pf-step #no-inconsistent-row}
The row-echelon form of $[A\mid b]$ contains no row of the form
$$
\begin{pmatrix}
0&\cdots&0&\mid&c
\end{pmatrix},
\qquad
c\neq0.
$$

::: pf-proof
Elementary row operations do not change the solution set of a linear
system over any field containing $\QQ$, in particular over $\CC$.
Such a row would represent the impossible equation
$$
0=c.
$$
Since the original system has a solution in $\CC^n$ by hypothesis, no
such row can occur.
:::

:::

::: {.pf-step #rational-solution-of-reduced-system}
The row-echelon system has a solution all of whose coordinates
lie in $\QQ$.

::: pf-proof
Assign the value $0$ to every free variable. Starting from the bottom
pivot row and proceeding upward, each pivot variable is then determined
by an equation whose coefficients and right-hand side are rational and
whose already determined variables are rational. Division by the
nonzero rational pivot therefore gives a rational value for the pivot
variable.

Thus the resulting solution vector belongs to $\QQ^n$.
:::

:::

::: {.pf-step #rational-solution-of-original}
The original system $Ax=b$ has a rational solution.

::: pf-proof
The vector constructed in step [](#rational-solution-of-reduced-system){.pf-ref} solves the row-echelon system.
Because elementary row operations are reversible and preserve the
solution set, it also solves the original system.
:::

:::

::: {.pf-step #true-boxed}
Therefore the assertion in the problem is
$$
\boxed{\text{true}}.
$$

::: pf-proof
Step [](#rational-solution-of-original){.pf-ref} constructs a solution in $\QQ^n$ whenever a solution in
$\CC^n$ exists.
:::

:::

::: pf-qed
Step [](#true-boxed){.pf-ref} is the required determination and proof.
:::

:::
:::
