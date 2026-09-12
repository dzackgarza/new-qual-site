---
schema: qual/card@1
id: P-APAF18A
kind: problem
title: Jordan form of a $4\times 4$ unipotent upper-triangular matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
For the following matrix
\[
A=\begin{bmatrix}
1 & 2 & 3 & 4 \\
0 & 1 & 2 & 3 \\
0 & 0 & 1 & 2 \\
0 & 0 & 0 & 1
\end{bmatrix},
\]
determine its Jordan canonical form (JCF) and find a nonsingular matrix $P$ such that $P^{-1}AP$ gives the JCF.
:::

::: {.solution}
Let
\[
N=A-I=
\begin{bmatrix}
0&2&3&4\\
0&0&2&3\\
0&0&0&2\\
0&0&0&0
\end{bmatrix}.
\]

<1>1. The nilpotent matrix $N$ has nilpotency index $4$.
::: {.proof}
Take $e_4=(0,0,0,1)^T$. Then
\[
Ne_4=\begin{bmatrix}4\\3\\2\\0\end{bmatrix},
\qquad
N^2e_4=\begin{bmatrix}12\\4\\0\\0\end{bmatrix},
\qquad
N^3e_4=\begin{bmatrix}8\\0\\0\\0\end{bmatrix}\ne0.
\]
Since $N$ is strictly upper triangular of size $4$, one has $N^4=0$. Hence the nilpotency index is exactly $4$.
:::

<1>2. Therefore the Jordan canonical form of $A$ is a single Jordan block
\[
J=J_4(1)=
\begin{bmatrix}
1&1&0&0\\
0&1&1&0\\
0&0&1&1\\
0&0&0&1
\end{bmatrix}.
\]
::: {.proof}
The only eigenvalue of the upper-triangular matrix $A$ is $1$, with algebraic multiplicity $4$. The Jordan blocks of $A$ are obtained by adding $1$ to the Jordan blocks of $N=A-I$. A nilpotent $4\times4$ matrix has nilpotency index equal to the size of its largest Jordan block. By <1>1 that largest block has size $4$, so there can be only one block.
:::

<1>3. Define
\[
v_4=e_4,
\quad
v_3=Nv_4=\begin{bmatrix}4\\3\\2\\0\end{bmatrix},
\quad
v_2=Nv_3=\begin{bmatrix}12\\4\\0\\0\end{bmatrix},
\quad
v_1=Nv_2=\begin{bmatrix}8\\0\\0\\0\end{bmatrix}.
\]
Then
\[
Nv_1=0,\qquad Nv_2=v_1,\qquad Nv_3=v_2,\qquad Nv_4=v_3.
\]
::: {.proof}
The displayed vectors are obtained by direct multiplication by $N$. The last three identities hold by construction, and $Nv_1=0$ because $v_1$ is a multiple of $e_1$ and the first column of $N$ is zero.
:::

<1>4. Let
\[
P=[v_1\ v_2\ v_3\ v_4]
=
\begin{bmatrix}
8&12&4&0\\
0&4&3&0\\
0&0&2&0\\
0&0&0&1
\end{bmatrix}.
\]
Then $P$ is nonsingular and
\[
P^{-1}AP=J_4(1).
\]
::: {.proof}
The matrix $P$ is upper triangular with
\[
\det P=8\cdot4\cdot2\cdot1=64\ne0,
\]
so $P$ is invertible. Since $A=I+N$, the chain identities in <1>3 give
\[
Av_1=v_1,
\qquad
Av_2=v_1+v_2,
\qquad
Av_3=v_2+v_3,
\qquad
Av_4=v_3+v_4.
\]
Thus the coordinate matrix of $A$ in the ordered basis $(v_1,v_2,v_3,v_4)$ is exactly $J_4(1)$, equivalently $P^{-1}AP=J_4(1)$.
:::
:::
