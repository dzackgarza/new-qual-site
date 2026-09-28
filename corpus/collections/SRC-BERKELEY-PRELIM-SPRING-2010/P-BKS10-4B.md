---
schema: qual/card@1
id: P-BKS10-4B
kind: problem
title: Four diagonalizability assertions for matrices
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked explicit 2-by-2 counterexamples for parts 1 and 2, the eigenspace decomposition for idempotents, and the similarity argument for part 4.
---

::: {.problem}
Let $A,B$ be complex square matrices of the same size.
Prove or disprove each assertion:

1. If $A$ and $B$ are diagonalizable, then $A+B$ is diagonalizable.

2. If $A$ and $B$ are diagonalizable, then $AB$ is diagonalizable.

3. If $A^2=A$, then $A$ is diagonalizable.

4. If $AB$ is diagonalizable and invertible, then $BA$ is diagonalizable.
:::

::: {.solution}
Let $V\coloneqq\CC^n$ be the common underlying vector space.

<1>1. Assertion 1 is false.

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
eigenvalues $-1$ and $1$, so it is diagonalizable over $\CC$. But
$$
A+B
=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
$$
This matrix is nonzero and nilpotent, so its only eigenvalue is $0$ and it
cannot be diagonalizable.
:::

<1>2. Assertion 2 is false.

::: {.proof}
Set
$$
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
1&0\\
1&-1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&1\\
0&1
\end{pmatrix}.
$$
One has
$$
A^2=I,
$$
so the minimal polynomial of $A$ divides
$$
t^2-1=(t-1)(t+1),
$$
which has distinct roots; hence $A$ is diagonalizable. Also
$$
B^2=B,
$$
so the minimal polynomial of $B$ divides
$$
t(t-1),
$$
which likewise has distinct roots; hence $B$ is diagonalizable.

However,
$$
AB=N.
$$
As in step <1>1, $N$ is a nonzero nilpotent matrix and is not
diagonalizable.
:::

<1>3. Assertion 3 is true.

::: {.proof}
Assume
$$
A^2=A.
$$
For every vector $v$,
$$
v=(v-Av)+Av.
$$
Moreover,
$$
A(v-Av)=Av-A^2v=0,
$$
so $v-Av\in\ker A$, while $Av\in\operatorname{im}A$. Thus
$$
V=\ker A+\operatorname{im}A.
$$
If $w$ lies in the intersection, then $Aw=0$ because $w\in\ker A$, while
$Aw=w$ because $w\in\operatorname{im}A$ and $A$ acts as the identity on
its image. Hence $w=0$, and therefore
$$
V=\ker A\oplus\operatorname{im}A.
$$
A basis adapted to this direct sum consists of eigenvectors with
eigenvalues $0$ and $1$, so $A$ is diagonalizable.
:::

<1>4. Assertion 4 is true.

::: {.proof}
If $AB$ is invertible, then
$$
0\neq\det(AB)=\det(A)\det(B).
$$
Thus both $A$ and $B$ are invertible. Consequently
$$
BA
=
A^{-1}(AB)A.
$$
Hence $BA$ is similar to $AB$. Similarity preserves diagonalizability, so
$BA$ is diagonalizable whenever $AB$ is.
:::

<1>5. The four answers are
$$
\boxed{\text{false},\ \text{false},\ \text{true},\ \text{true}}.
$$

::: {.proof}
Steps <1>1--<1>4 establish the assertions in order.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 records the required conclusions.
:::
:::
