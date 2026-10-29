---
schema: qual/card@1
id: P-UCLAB08F-08
kind: problem
title: Eigenvectors need not span a complex vector space
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
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
Must the eigenvectors of a linear transformation
\[
T\colon\CC^n\to\CC^n
\]
span $\CC^n$?
Prove your assertion.
:::

::: {.solution}

::: pf

::: pf-step

The answer is no in general.


::: pf-proof

It suffices to give one complex linear transformation whose eigenvectors do not span its ambient vector space.

:::

:::

::: pf-step

Consider
\[
T:\CC^2\to\CC^2
\]
with matrix
\[
A=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]
Its only eigenvalue is $1$.


::: pf-proof

The characteristic polynomial is
\[
\det(\lambda I-A)
=
\det
\begin{pmatrix}
\lambda-1&-1\\
0&\lambda-1
\end{pmatrix}
=
(\lambda-1)^2.
\]
Thus the only eigenvalue is $1$.

:::

:::

::: {.pf-step #s1-3}

The eigenspace for the eigenvalue $1$ is
\[
E_1
=
\operatorname{span}_{\CC}\{(1,0)\}.
\]


::: pf-proof

One has
\[
A-I
=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
\]
Hence
\[
(A-I)
\binom{x}{y}
=
\binom{y}{0},
\]
which vanishes exactly when $y=0$. Therefore
\[
\ker(A-I)
=
\left\{
\binom{x}{0}:x\in\CC
\right\}
=
\operatorname{span}_{\CC}\{(1,0)\}.
\]

:::

:::

::: {.pf-step #s1-4}

The eigenvectors of $T$ do not span $\CC^2$.


::: pf-proof

Every eigenvector belongs to the one-dimensional eigenspace $E_1$ from step [](#s1-3){.pf-ref}. Thus the span of all eigenvectors is $E_1$, which has dimension $1$ and is strictly smaller than $\CC^2$.

:::

:::

::: {.pf-step #s1-5}

Therefore
\[
\boxed{\text{eigenvectors of a complex linear transformation need not span the space}.}
\]


::: pf-proof

Step [](#s1-4){.pf-ref} gives the required counterexample.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} answers the question.

:::

:::

:::
