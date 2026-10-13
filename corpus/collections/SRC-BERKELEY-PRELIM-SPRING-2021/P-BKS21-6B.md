---
schema: qual/card@1
id: P-BKS21-6B
kind: problem
title: Diagonalizability over $\RR$ and $\CC$
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
For each statement, give a proof or counterexample.

(a) Every real matrix is diagonalizable over $\RR$.

(b) Every real symmetric matrix is diagonalizable over $\RR$.

(c) Every complex matrix is diagonalizable over $\CC$.

(d) Every complex symmetric matrix is diagonalizable over $\CC$.
:::

::: {.solution}
<1>1. Statement (a) is false.

::: {.proof}
Consider
$$
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
$$
This is a real nonzero matrix with
$$
A^2=0.
$$
Thus its only eigenvalue is $0$. If $A$ were diagonalizable over $\mathbb R$, it would be similar to a diagonal matrix all of whose diagonal entries are $0$, hence to the zero matrix. Similarity to the zero matrix would force $A=0$, a contradiction.
:::

<1>2. Statement (b) is true.

::: {.proof}
The real spectral theorem states that every real symmetric matrix is orthogonally diagonalizable. Thus if $A^T=A$, there exists an orthogonal real matrix $Q$ such that
$$
Q^{-1}AQ=Q^TAQ
$$
is diagonal.
:::

<1>3. Statement (c) is false.

::: {.proof}
The same matrix
$$
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}
$$
is a complex matrix. The argument in step <1>1 is field-independent: $A$ is nonzero, $A^2=0$, and its only eigenvalue is $0$, so it cannot be diagonalizable over $\mathbb C$.
:::

<1>4. Statement (d) is false.

::: {.proof}
Consider the complex symmetric matrix
$$
B=
\begin{pmatrix}
1&i\\
i&-1
\end{pmatrix}.
$$
It is nonzero and satisfies
$$
B^T=B.
$$
Direct multiplication gives
$$
B^2=
\begin{pmatrix}
1+i^2&i-i\\
i-i&i^2+1
\end{pmatrix}
=0.
$$
Hence the only eigenvalue of $B$ is $0$. If $B$ were diagonalizable over $\mathbb C$, it would be similar to the zero diagonal matrix and therefore would itself be zero, contradiction.
:::

<1>5. Therefore the four answers are
$$
\boxed{\text{(a) false,\quad (b) true,\quad (c) false,\quad (d) false}}.
$$

::: {.proof}
Steps <1>1--<1>4 establish the four assertions individually.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested classification with proofs and counterexamples.
:::
:::
