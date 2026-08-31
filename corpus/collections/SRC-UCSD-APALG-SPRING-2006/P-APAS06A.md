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

::: problem
(a) Consider $\lambda_i,\lambda_j\in\operatorname{eig}(A)$ such that $\lambda_i\neq\lambda_j$.
Let $(x_i,y_i)$ and $(x_j,y_j)$ denote the right and left eigenvectors of $A$ associated with $\lambda_i$ and $\lambda_j$.
Show that $y_i^*x_j=0$.

(b) Let $x$ denote an eigenvector of $A$ associated with an eigenvalue $\lambda$.
Prove that if $\lambda$ has a left-eigenvector $y$ such that $y^*x=0$, then $\operatorname{am}(\lambda)>1$.
:::

::: {.solution}
**Goal.** (a) Left and right eigenvectors for distinct eigenvalues are orthogonal. (b) A left eigenvector orthogonal to a right eigenvector forces algebraic multiplicity $> 1$.

<1>1. (a) $y_i^* x_j = 0$ for $\lambda_i \neq \lambda_j$.
<2>1. $y_i^* A = \lambda_i y_i^*$ and $A x_j = \lambda_j x_j$.
::: {.proof}
$y_i$ is a left eigenvector and $x_j$ a right eigenvector.
:::
<2>2. $\lambda_i y_i^* x_j = y_i^* A x_j = \lambda_j y_i^* x_j$.
::: {.proof}
$y_i^* A x_j = (y_i^* A) x_j = \lambda_i y_i^* x_j$, and also $y_i^* A x_j = y_i^* (A x_j) = \lambda_j y_i^* x_j$.
:::
<2>3. Hence $(\lambda_i - \lambda_j) y_i^* x_j = 0$, so $y_i^* x_j = 0$.
::: {.proof}
$\lambda_i \neq \lambda_j$.
:::

<1>2. (b) If $y^* x = 0$ for a left eigenvector $y$ of $\lambda$, then $\operatorname{am}(\lambda) > 1$.
<2>1. Suppose $\operatorname{am}(\lambda) = 1$.
::: {.proof}
assume for contradiction.
:::
<2>2. Then the generalized eigenspace for $\lambda$ is one-dimensional, spanned by $x$.
::: {.proof}
algebraic multiplicity $1$ means the generalized eigenspace has dimension $1$.
:::
<2>3. The left generalized eigenspace for $\lambda$ is also one-dimensional, spanned by $y$.
::: {.proof}
the left and right generalized eigenspaces for the same eigenvalue have the same dimension.
:::
<2>4. The pairing between the left and right generalized eigenspaces for $\lambda$ is nondegenerate.
::: {.proof}
the left and right generalized eigenspaces for $\lambda$ are dual to each other under the pairing $(y, x) \mapsto y^* x$, and this pairing is nondegenerate.
:::
<2>5. Hence $y^* x \neq 0$, contradicting $y^* x = 0$.
::: {.proof}
a nondegenerate pairing on a one-dimensional space cannot vanish on the nonzero pair $(y, x)$.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 proves (a); <1>2 proves (b).
:::
:::
