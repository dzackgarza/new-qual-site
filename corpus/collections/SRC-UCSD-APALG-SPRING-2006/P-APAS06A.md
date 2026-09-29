---
schema: qual/card@1
id: P-APAS06A
kind: problem
title: Left–right eigenvector orthogonality and algebraic multiplicity
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
(a) Consider $\lambda_i,\lambda_j\in\operatorname{eig}(A)$ such that $\lambda_i\neq\lambda_j$.
Let $(x_i,y_i)$ and $(x_j,y_j)$ denote the right and left eigenvectors of $A$ associated with $\lambda_i$ and $\lambda_j$.
Show that $y_i^*x_j=0$.

(b) Let $x$ denote an eigenvector of $A$ associated with an eigenvalue $\lambda$.
Prove that if $\lambda$ has a left-eigenvector $y$ such that $y^*x=0$, then $\operatorname{am}(\lambda)>1$.
:::

::: {.solution}

**Goal.** (a) Left and right eigenvectors for distinct eigenvalues are orthogonal. (b) A left eigenvector orthogonal to a right eigenvector forces algebraic multiplicity $> 1$.

::: pf

::: {.pf-step #part-a-orthogonality}
(a) $y_i^* x_j = 0$ for $\lambda_i \neq \lambda_j$.

::: pf-proof

::: pf-step
$y_i^* A = \lambda_i y_i^*$ and $A x_j = \lambda_j x_j$.

::: pf-proof
$y_i$ is a left eigenvector and $x_j$ a right eigenvector.
:::

:::

::: pf-step
$\lambda_i y_i^* x_j = y_i^* A x_j = \lambda_j y_i^* x_j$.

::: pf-proof
$y_i^* A x_j = (y_i^* A) x_j = \lambda_i y_i^* x_j$, and also $y_i^* A x_j = y_i^* (A x_j) = \lambda_j y_i^* x_j$.
:::

:::

::: pf-step
Hence $(\lambda_i - \lambda_j) y_i^* x_j = 0$, so $y_i^* x_j = 0$.

::: pf-proof
$\lambda_i \neq \lambda_j$.
:::

:::

:::

:::

::: {.pf-step #part-b-am-greater-than-one}
(b) If $y^* x = 0$ for a left eigenvector $y$ of $\lambda$, then $\operatorname{am}(\lambda) > 1$.

::: pf-proof

::: pf-step
Suppose $\operatorname{am}(\lambda) = 1$.

::: pf-proof
assume for contradiction.
:::

:::

::: pf-step
Then the generalized eigenspace for $\lambda$ is one-dimensional, spanned by $x$.

::: pf-proof
algebraic multiplicity $1$ means the generalized eigenspace has dimension $1$.
:::

:::

::: pf-step
The left generalized eigenspace for $\lambda$ is also one-dimensional, spanned by $y$.

::: pf-proof
the left and right generalized eigenspaces for the same eigenvalue have the same dimension.
:::

:::

::: pf-step
The pairing between the left and right generalized eigenspaces for $\lambda$ is nondegenerate.

::: pf-proof
the left and right generalized eigenspaces for $\lambda$ are dual to each other under the pairing $(y, x) \mapsto y^* x$, and this pairing is nondegenerate.
:::

:::

::: pf-step
Hence $y^* x \neq 0$, contradicting $y^* x = 0$.

::: pf-proof
a nondegenerate pairing on a one-dimensional space cannot vanish on the nonzero pair $(y, x)$.
:::

:::

:::

:::

::: pf-qed
Step [](#part-a-orthogonality){.pf-ref} proves (a); step [](#part-b-am-greater-than-one){.pf-ref} proves (b).
:::

:::

:::
