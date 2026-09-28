---
schema: qual/card@1
id: P-BKS82-9
kind: problem
title: Real Jordan canonical form of a $3\times3$ matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained PDF; the extracted markdown contains a different Problem 9.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the characteristic polynomial, the eigenspace dimensions, and an explicit Jordan chain for the eigenvalue $2$.
---

::: {.problem}
Find the Jordan canonical form over $\mathbb R$ of
\[
\begin{pmatrix}
4&1&0\\
-4&0&0\\
19&17&5
\end{pmatrix}.
\]
:::

::: {.solution}
Let
$$
A=
\begin{pmatrix}
4&1&0\\
-4&0&0\\
19&17&5
\end{pmatrix}.
$$

<1>1. The characteristic polynomial of $A$ is
$$
\chi_A(t)=(t-2)^2(t-5).
$$

::: {.proof}
The matrix $tI-A$ is block lower triangular with upper-left block
$$
\begin{pmatrix}
t-4&-1\\
4&t
\end{pmatrix}
$$
and lower-right entry $t-5$. Hence
$$
\begin{aligned}
\chi_A(t)
&=
(t-5)
\det
\begin{pmatrix}
t-4&-1\\
4&t
\end{pmatrix}\\
&=
(t-5)\bigl(t(t-4)+4\bigr)\\
&=
(t-5)(t-2)^2.
\end{aligned}
$$
:::

<1>2. The eigenspace for the eigenvalue $2$ is one-dimensional:
$$
\ker(A-2I)
=
\operatorname{span}
\left\{
\begin{pmatrix}
1\\
-2\\
5
\end{pmatrix}
\right\}.
$$

::: {.proof}
One has
$$
A-2I
=
\begin{pmatrix}
2&1&0\\
-4&-2&0\\
19&17&3
\end{pmatrix}.
$$
The equation $(A-2I)(x,y,z)^T=0$ gives
$$
2x+y=0
$$
and
$$
19x+17y+3z=0.
$$
Thus $y=-2x$ and $z=5x$, giving the stated one-dimensional eigenspace.
:::

<1>3. If
$$
v\coloneqq
\begin{pmatrix}
1\\
-2\\
5
\end{pmatrix}
\qquad\text{and}\qquad
w\coloneqq
\begin{pmatrix}
0\\
1\\
-4
\end{pmatrix},
$$
then
$$
(A-2I)v=0
\qquad\text{and}\qquad
(A-2I)w=v.
$$

::: {.proof}
The first identity is step <1>2. Direct multiplication gives
$$
(A-2I)w
=
\begin{pmatrix}
1\\
-2\\
5
\end{pmatrix}
=v.
$$
Thus $(v,w)$ is a Jordan chain of length $2$ for the eigenvalue $2$.
:::

<1>4. The vector
$$
u\coloneqq
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix}
$$
is an eigenvector for the eigenvalue $5$.

::: {.proof}
The third column of $A$ is $(0,0,5)^T$, so
$$
Au=5u.
$$
:::

<1>5. The vectors $v,w,u$ form a basis of $\RR^3$, and in this basis the
matrix of $A$ is
$$
\boxed{
\begin{pmatrix}
2&1&0\\
0&2&0\\
0&0&5
\end{pmatrix}
}.
$$

::: {.proof}
The vectors $v$ and $w$ are linearly independent because
$(A-2I)w=v\ne0$ while $(A-2I)v=0$. Their span is the generalized
$2$-eigenspace. The vector $u$ is a $5$-eigenvector, so it does not lie in
that generalized $2$-eigenspace; hence $v,w,u$ are linearly independent.

By steps <1>3 and <1>4,
$$
Av=2v,
\qquad
Aw=v+2w,
\qquad
Au=5u.
$$
Therefore the columns of the matrix of $A$ in the ordered basis
$(v,w,u)$ are $(2,0,0)^T$, $(1,2,0)^T$, and $(0,0,5)^T$, respectively,
which gives the displayed Jordan matrix.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the real Jordan canonical form of $A$.
:::
:::
