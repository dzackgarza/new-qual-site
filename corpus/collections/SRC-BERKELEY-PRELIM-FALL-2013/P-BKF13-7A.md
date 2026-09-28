---
schema: qual/card@1
id: P-BKF13-7A
kind: problem
title: Diagonalizability of sums, products, idempotents and square roots of matrices
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 7A in the retained Fall 2013 Berkeley prelim exam
    and independently reviewed the retained solution packet F13_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked explicit 2-by-2 counterexamples for statements 1, 2, and 4 and
    the squarefree minimal-polynomial argument for statement 3.
---

::: {.problem}
Let $A$ and $B$ be $n\times n$ complex matrices.
Prove or disprove each of the following statements:

1. If $A$ and $B$ are diagonalizable, so is $A+B$.

2. If $A$ and $B$ are diagonalizable, so is $AB$.

3. If $A^2=A$, then $A$ is diagonalizable.

4. If $A^2$ is diagonalizable, then $A$ is diagonalizable.
:::

::: {.solution}
Let
$$
J\coloneqq
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
$$
The matrix $J$ is not diagonalizable: its only eigenvalue is $0$, so a
diagonalizable matrix similar to it would have to be the zero matrix,
whereas $J\ne0$.

<1>1. Statement 1 is false.

::: {.proof}
Take
$$
A=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
-1&1\\
0&1
\end{pmatrix}.
$$
The matrix $A$ is diagonal. The matrix $B$ has the two distinct
eigenvalues $-1$ and $1$, so it is diagonalizable. However,
$$
A+B
=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}
=J,
$$
which is not diagonalizable.
:::

<1>2. Statement 2 is false.

::: {.proof}
Take
$$
A=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&1\\
0&1
\end{pmatrix}.
$$
Again $A$ is diagonal. The characteristic polynomial of $B$ is
$$
t(t-1),
$$
so $B$ has distinct eigenvalues $0$ and $1$ and is diagonalizable.
But
$$
AB
=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}
=J,
$$
which is not diagonalizable.
:::

<1>3. Statement 3 is true.

::: {.proof}
If $A^2=A$, then
$$
A(A-I)=0.
$$
Hence the minimal polynomial of $A$ divides
$$
t(t-1).
$$
This polynomial splits over $\CC$ and has no repeated root. Therefore
the minimal polynomial of $A$ also splits with no repeated root, which
is equivalent to diagonalizability.
:::

<1>4. Statement 4 is false.

::: {.proof}
Take $A=J$. Then
$$
A^2=0,
$$
which is diagonalizable, while $A=J$ itself is not diagonalizable.
:::

<1>5. Thus the answers are
$$
\boxed{\text{false},\ \text{false},\ \text{true},\ \text{false}}.
$$

::: {.proof}
This is exactly the content of steps <1>1--<1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 answers all four parts.
:::
:::
