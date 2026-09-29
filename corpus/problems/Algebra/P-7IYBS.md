---
schema: qual/card@1
id: P-7IYBS
kind: problem
title: Matrices satisfying $A^2=A$ are diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
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
Let $A\in M_n(F)$ satisfy $A^2=A$. Prove that $A$ is diagonalizable over $F$, and determine its possible diagonal form.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The minimal polynomial of $A$ divides
\[
x^2-x=x(x-1).
\]

::: pf-proof

The relation $A^2=A$ is exactly
\[
A(A-I)=0,
\]
so the polynomial $x(x-1)$ annihilates $A$. Hence the minimal polynomial divides it.

:::

:::

::: {.pf-step #s2}

The polynomial $x(x-1)$ has no repeated root over any field.

::: pf-proof

Its roots are $0$ and $1$, which are distinct in every field. Thus every divisor of $x(x-1)$ is squarefree.

:::

:::

::: {.pf-step #s3}

Therefore $A$ is diagonalizable.

::: pf-proof

A linear operator is diagonalizable over $F$ if and only if its minimal polynomial splits over $F$ as a product of distinct linear factors. By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the minimal polynomial of $A$ has this form.

:::

:::

::: pf-step

In a suitable basis,
\[
A\sim\operatorname{diag}(\underbrace{1,\ldots,1}_{r},\underbrace{0,\ldots,0}_{n-r})
\]
for some $0\le r\le n$.

::: pf-proof

By step [](#s3){.pf-ref} the only possible eigenvalues are the roots $0$ and $1$ of the annihilating polynomial. Hence a diagonal form consists only of $0$'s and $1$'s. The number $r$ of $1$'s is
\[
r=\operatorname{rank}(A)=\dim\operatorname{im}(A),
\]
while the number of $0$'s is $n-r=\dim\ker A$.

:::

:::

:::

:::
