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

::: pf

::: {.pf-step #s1-1}

Statement (a) is false.


::: pf-proof

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
Thus its only eigenvalue is $0$. If $A$ were diagonalizable over $\RR$, it would be similar to a diagonal matrix all of whose diagonal entries are $0$, hence to the zero matrix. Similarity to the zero matrix would force $A=0$, a contradiction.

:::

:::

::: {.pf-step #s1-2}

Statement (b) is true.


::: pf-proof

The real spectral theorem states that every real symmetric matrix is orthogonally diagonalizable. Thus if $A^T=A$, there exists an orthogonal real matrix $Q$ such that
$$
Q^{-1}AQ=Q^TAQ
$$
is diagonal.

:::

:::

::: {.pf-step #s1-3}

Statement (c) is false.


::: pf-proof

The same matrix
$$
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}
$$
is a complex matrix. The argument in step [](#s1-1){.pf-ref} is field-independent: $A$ is nonzero, $A^2=0$, and its only eigenvalue is $0$, so it cannot be diagonalizable over $\CC$.

:::

:::

::: {.pf-step #s1-4}

Statement (d) is false.


::: pf-proof

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
Hence the only eigenvalue of $B$ is $0$. If $B$ were diagonalizable over $\CC$, it would be similar to the zero diagonal matrix and therefore would itself be zero, contradiction.

:::

:::

::: {.pf-step #s1-5}

Therefore the four answers are
$$
\boxed{\text{(a) false,\quad (b) true,\quad (c) false,\quad (d) false}}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} establish the four assertions individually.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested classification with proofs and counterexamples.

:::

:::

:::
