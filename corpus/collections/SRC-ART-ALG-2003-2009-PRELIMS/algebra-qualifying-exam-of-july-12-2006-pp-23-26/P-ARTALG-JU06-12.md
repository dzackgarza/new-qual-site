---
schema: qual/card@1
id: P-ARTALG-JU06-12
kind: problem
title: Rational canonical form over Q
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all nine matrix entries with July 2006 Rings and modules 12 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified the characteristic polynomial, determinant of the cyclic-basis matrix, and the complete exact matrix identity AP=PC."
---

::: {.problem}
Find the rational canonical form over $\mathbb{Q}$ of the following matrix:

$$\begin{pmatrix} 3 & -1 & 10 \\ 0 & 2 & 5 \\ 0 & 0 & 3 \end{pmatrix}.$$
:::

::: {.solution}
Let $A$ denote the given matrix. Its rational canonical form is
$$
C=\begin{pmatrix}
0&0&18\\
1&0&-21\\
0&1&8
\end{pmatrix},
$$
with the single invariant factor
$f(T)=(T-3)^2(T-2)=T^3-8T^2+21T-18$.
We use the companion-matrix convention with ones on the subdiagonal.

<1>1. The vector $v=(0,0,1)^t$ is cyclic for $A$.

::: {.proof}
Because $A$ is upper triangular,
$$
\det(TI-A)=(T-3)^2(T-2)=f(T).
$$
Direct multiplication gives
$$
Av=\begin{pmatrix}10\\5\\3\end{pmatrix},\qquad
A^2v=\begin{pmatrix}55\\25\\9\end{pmatrix}.
$$
The matrix with columns $v,Av,A^2v$ is
$$
P=\begin{pmatrix}0&10&55\\0&5&25\\1&3&9\end{pmatrix},
\qquad \det P=10\cdot25-55\cdot5=-25\ne0.
$$
Thus these three vectors form a basis of $\mathbb Q^3$.
:::

<1>2. In that basis, $A$ has the displayed companion matrix $C$.

::: {.proof}
The exact matrix products are
$$
AP=PC=
\begin{pmatrix}
10&55&230\\
5&25&95\\
3&9&27
\end{pmatrix}.
$$
Since $P$ is invertible, this proves $P^{-1}AP=C$.
Equivalently, the last column states
$A^3v=18v-21Av+8A^2v$, while the first two columns advance
along the cyclic basis. A cyclic module with this degree-three
relation has the single invariant factor $f$, and its rational
canonical form is the companion matrix $C$ [@DF04].
:::
:::
