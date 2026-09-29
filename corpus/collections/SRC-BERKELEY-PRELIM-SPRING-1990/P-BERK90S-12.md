---
schema: qual/card@1
id: P-BERK90S-12
kind: problem
title: Positivity of the spectrum of the discrete one-dimensional Laplacian matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the positive integer n, the diagonal and adjacent entries, and the strict positivity conclusion with Problem 12 in the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Expressed the complex quadratic form as a sum of squared successive differences with zero endpoint coordinates and applied it to an arbitrary eigenvector.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked conjugation in the mixed terms, both boundary contributions, the n=1 case, the zero-vector equality case, and positivity of the eigenvalue quotient.
---

::: {.problem}
Let $n$ be a positive integer, and let $A=(a_{ij})_{i,j=1}^n$ be
the real $n\times n$ matrix with
$$
a_{ii}=2\quad(1\leq i\leq n),
\qquad
a_{i,i+1}=a_{i+1,i}=-1\quad(1\leq i<n),
$$
and all other entries zero. Prove that every eigenvalue of $A$ is a positive real number.
:::

::: {.hint}
For $x=(x_1,\ldots,x_n)^T\in\CC^n$, append the coordinates
$x_0=x_{n+1}=0$ and expand
$$
\sum_{j=0}^n\abs{x_{j+1}-x_j}^2.
$$
Compare the expansion with $\overline{x}^{\,T}Ax$ and determine
when this sum can vanish.
:::

::: {.solution}
For a column vector $x=(x_1,\ldots,x_n)^T\in\CC^n$, write $x^*$
for its conjugate transpose and set $x_0=x_{n+1}=0$.

::: pf

::: {.pf-step #s1}

For every $x\in\CC^n$,
$$
x^*Ax=\sum_{j=0}^n\abs{x_{j+1}-x_j}^2.
$$

::: pf-proof

The entries of $A$ give
$$
x^*Ax
=2\sum_{j=1}^n\abs{x_j}^2
-\sum_{j=1}^{n-1}
\bigl(\overline{x_j}x_{j+1}+\overline{x_{j+1}}x_j\bigr).
$$
On expanding each square in the asserted sum, every
$\abs{x_j}^2$ for $1\leq j\leq n$ appears twice. The mixed terms
at $j=0$ and $j=n$ vanish because $x_0=x_{n+1}=0$, and all the
remaining mixed terms are those in the displayed expression.
Thus the expressions are equal. For $n=1$, the mixed-term sum
is empty and both expressions equal $2\abs{x_1}^2$.

:::

:::

::: {.pf-step #s2}

For every nonzero $x\in\CC^n$, the number $x^*Ax$ is
real and strictly positive.

::: pf-proof

Each summand in step [](#s1){.pf-ref} is a nonnegative real number. Their sum
can be zero only if $x_{j+1}=x_j$ for all $0\leq j\leq n$.
Since $x_0=0$, these equalities force $x_1=\cdots=x_n=0$.
Thus the sum is strictly positive whenever $x\neq0$.

:::

:::

::: {.pf-step #s3}

Every eigenvalue $\lambda\in\CC$ of $A$ is real and
strictly positive.

::: pf-proof

Choose a nonzero eigenvector $x\in\CC^n$ with $Ax=\lambda x$.
Multiplying by $x^*$ gives
$$
\lambda
=\frac{x^*Ax}{x^*x}
=\frac{\displaystyle\sum_{j=0}^n\abs{x_{j+1}-x_j}^2}
       {\displaystyle\sum_{j=1}^n\abs{x_j}^2}.
$$
The numerator is a positive real number by step [](#s2){.pf-ref}. The
denominator is a positive real number because $x\neq0$.
Their quotient is therefore real and strictly positive.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} applies to every eigenvalue of $A$ and proves the
required conclusion.

:::

:::

:::
