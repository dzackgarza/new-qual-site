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

::: pf

::: {.pf-step #characteristic-polynomial}
The characteristic polynomial of $A$ is
$$
\chi_A(t)=(t-2)^2(t-5).
$$

::: pf-proof
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

:::

::: {.pf-step #eigenspace-for-two}
The eigenspace for the eigenvalue $2$ is one-dimensional:
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

::: pf-proof
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

:::

::: {.pf-step #jordan-chain-for-two}
If
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

::: pf-proof
The first identity is step [](#eigenspace-for-two){.pf-ref}. Direct multiplication gives
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

:::

::: {.pf-step #eigenvector-for-five}
The vector
$$
u\coloneqq
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix}
$$
is an eigenvector for the eigenvalue $5$.

::: pf-proof
The third column of $A$ is $(0,0,5)^T$, so
$$
Au=5u.
$$
:::

:::

::: {.pf-step #jordan-form-boxed}
The vectors $v,w,u$ form a basis of $\RR^3$, and in this basis the
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

::: pf-proof
The vectors $v$ and $w$ are linearly independent because
$(A-2I)w=v\ne0$ while $(A-2I)v=0$. Their span is the generalized
$2$-eigenspace. The vector $u$ is a $5$-eigenvector, so it does not lie in
that generalized $2$-eigenspace; hence $v,w,u$ are linearly independent.

By steps [](#jordan-chain-for-two){.pf-ref} and [](#eigenvector-for-five){.pf-ref},
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

:::

::: pf-qed
Step [](#jordan-form-boxed){.pf-ref} is the real Jordan canonical form of $A$.
:::

:::
:::
