---
schema: qual/card@1
id: P-BKS11-8A
kind: problem
title: Diagonalizability of real, complex, and symmetric matrices
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 3 of the retained Spring 2011 solution PDF and independently reviewed the spectral-theorem case and the three counterexamples.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked non-diagonalizability of the nilpotent counterexamples over the relevant fields and orthogonal diagonalization of real symmetric matrices.
---

::: {.problem}
For each of the following 4 statements, give either a counterexample or a reason why it is true.

(a) For every real matrix A there is a real matrix B with $B ^ { - 1 } A B$ diagonal.

(b) For every symmetric real matrix A there is a real matrix B with $B ^ { - 1 } A B$ diagonal.

(c) For every complex matrix A there is a complex matrix B with $B ^ { - 1 } A B$ diagonal.

(d) For every symmetric complex matrix A there is a complex matrix B with $B ^ { - 1 } A B$ diagonal.
:::

::: {.solution}

::: pf

::: {.pf-step #assertion-a-false}
Assertion (a) is false.

::: pf-proof
Consider the real matrix
$$
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
$$
It is nonzero and satisfies
$$
N^2=0.
$$
Thus its only eigenvalue is $0$. If it were diagonalizable over $\RR$,
its diagonal form would have only zeros on the diagonal and therefore
would be the zero matrix, forcing $N=0$. This is a contradiction.
:::

:::

::: {.pf-step #assertion-b-true}
Assertion (b) is true.

::: pf-proof
By the real spectral theorem, every real symmetric matrix $A$ is
orthogonally diagonalizable. Thus there is a real orthogonal matrix $Q$
such that
$$
Q^TAQ
$$
is diagonal. Since
$$
Q^{-1}=Q^T,
$$
taking $B=Q$ gives the required form
$$
B^{-1}AB.
$$
:::

:::

::: {.pf-step #assertion-c-false}
Assertion (c) is false.

::: pf-proof
Use the same matrix $N$ as in step [](#assertion-a-false){.pf-ref}, now regarded as a complex
matrix. It is still nonzero and nilpotent, so its only eigenvalue over
$\CC$ is $0$. A diagonalizable complex matrix with only eigenvalue $0$
would be the zero matrix. Hence $N$ is not diagonalizable over $\CC$.
:::

:::

::: {.pf-step #assertion-d-false}
Assertion (d) is false.

::: pf-proof
Consider
$$
S=
\begin{pmatrix}
1&i\\
i&-1
\end{pmatrix}.
$$
The matrix is symmetric because
$$
S^T=S.
$$
Direct multiplication gives
$$
S^2=0,
$$
while $S\neq0$. Thus $S$ is a nonzero nilpotent complex matrix and,
exactly as in step [](#assertion-c-false){.pf-ref}, it is not diagonalizable.
:::

:::

::: {.pf-step #answer-summary}
The four answers are
$$
\boxed{
\text{false},\ \text{true},\ \text{false},\ \text{false}
}.
$$

::: pf-proof
Steps [](#assertion-a-false){.pf-ref}, [](#assertion-b-true){.pf-ref}, [](#assertion-c-false){.pf-ref} and [](#assertion-d-false){.pf-ref} settle the assertions in order.
:::

:::

::: pf-qed
Step [](#answer-summary){.pf-ref} records the required conclusions.
:::

:::

:::
