---
schema: qual/card@1
id: P-4GMLL
kind: problem
title: Jordan form of $\begin{pmatrix}-3&3&-2\\-7&6&-3\\1&-1&2\end{pmatrix}$ and a
  conjugating matrix
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let
\[
A=\left(\begin{array}{ccc}
-3 & 3 & -2 \\
-7 & 6 & -3 \\
1 & -1 & 2
\end{array}\right) \in M_{3}(\mathrm{C})
.\]

a.
Find the Jordan canonical form $J$ of $A$.

b.
Find an invertible matrix $P$ such that $P\inv A P = J$.
You do not need to compute $P\inv$.
:::

::: {.solution}
<1>1. The characteristic polynomial of $A$ is $(t-1)(t-2)^2$, and the eigenspace for $2$ has dimension one.

::: {.proof}
Direct expansion gives $\det(tI-A)=t^3-5t^2+8t-4=(t-1)(t-2)^2$. Moreover,
\[
A-2I=\begin{pmatrix}-5&3&-2\\-7&4&-3\\1&-1&0\end{pmatrix}.
\]
Its upper-left $2\times2$ minor is $-20+21=1\neq0$, whereas its determinant vanishes because $2$ is an eigenvalue. Thus $\operatorname{rank}(A-2I)=2$ and $\dim\ker(A-2I)=1$.
:::

<1>2. The Jordan canonical form is
\[
\boxed{J=\begin{pmatrix}1&0&0\\0&2&1\\0&0&2\end{pmatrix}}.
\]

::: {.proof}
The eigenvalue $1$ has algebraic multiplicity one, giving one block of size one. The eigenvalue $2$ has algebraic multiplicity two but geometric multiplicity one by step <1>1, giving one block of size two.
:::

<1>3. An invertible conjugating matrix is
\[
\boxed{P=\begin{pmatrix}
1&\tfrac12&\tfrac12\\
2&\tfrac12&1\\
1&-\tfrac12&0
\end{pmatrix}},\qquad P^{-1}AP=J.
\]

::: {.proof}
Write the columns of $P$ as $v_1,v_2,v_3$. Direct multiplication gives $Av_1=v_1$, $(A-2I)v_2=0$, and $(A-2I)v_3=v_2$. Hence $AP=PJ$. Also $\det P=\tfrac14\neq0$, so $P$ is invertible; multiplication by $P^{-1}$ yields $P^{-1}AP=J$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 answer parts (a) and (b).
:::
:::
