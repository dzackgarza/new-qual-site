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
T\colon\mathbb C^n\to\mathbb C^n
\]
span $\mathbb C^n$?
Prove your assertion.
:::

::: {.solution}
<1>1. The answer is no in general.

::: {.proof}
It suffices to give one complex linear transformation whose eigenvectors do not span its ambient vector space.
:::

<1>2. Consider
\[
T:\mathbb C^2\to\mathbb C^2
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

::: {.proof}
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

<1>3. The eigenspace for the eigenvalue $1$ is
\[
E_1
=
\operatorname{span}_{\mathbb C}\{(1,0)\}.
\]

::: {.proof}
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
\binom{x}{0}:x\in\mathbb C
\right\}
=
\operatorname{span}_{\mathbb C}\{(1,0)\}.
\]
:::

<1>4. The eigenvectors of $T$ do not span $\mathbb C^2$.

::: {.proof}
Every eigenvector belongs to the one-dimensional eigenspace $E_1$ from step <1>3. Thus the span of all eigenvectors is $E_1$, which has dimension $1$ and is strictly smaller than $\mathbb C^2$.
:::

<1>5. Therefore
\[
\boxed{\text{eigenvectors of a complex linear transformation need not span the space}.}
\]

::: {.proof}
Step <1>4 gives the required counterexample.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 answers the question.
:::
:::
