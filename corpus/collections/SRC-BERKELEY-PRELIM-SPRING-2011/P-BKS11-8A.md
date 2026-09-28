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
<1>1. Assertion (a) is false.

::: {.proof}
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

<1>2. Assertion (b) is true.

::: {.proof}
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

<1>3. Assertion (c) is false.

::: {.proof}
Use the same matrix $N$ as in step <1>1$, now regarded as a complex
matrix. It is still nonzero and nilpotent, so its only eigenvalue over
$\CC$ is $0$. A diagonalizable complex matrix with only eigenvalue $0$
would be the zero matrix. Hence $N$ is not diagonalizable over $\CC$.
:::

<1>4. Assertion (d) is false.

::: {.proof}
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
exactly as in step <1>3, it is not diagonalizable.
:::

<1>5. The four answers are
$$
\boxed{
\text{false},\ \text{true},\ \text{false},\ \text{false}
}.
$$

::: {.proof}
Steps <1>1--<1>4 settle the assertions in order.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 records the required conclusions.
:::
:::
