---
schema: qual/card@1
id: P-JLPVR
kind: problem
title: The projection onto the line $x+2y=0$ along $\operatorname{span}\{(1,2)\}$
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $L \subset \mathbb{R}^2$ be the line spanned by the vector $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$.
Let $P \subset \mathbb{R}^2$ be the line defined by the equation $x + 2y = 0$.
Find the standard matrix for the linear transformation $T : \mathbb{R}^2 \to \mathbb{R}^2$ such that $T(v) = 0$ for $v \in L$ and $T(v) = v$ for $v \in P$.
:::


::: solution
<1>1. The vectors
\[
\ell=\begin{pmatrix}1\\2\end{pmatrix},
\qquad
p=\begin{pmatrix}2\\-1\end{pmatrix}
\]
form a basis of $\mathbb R^2$, with $\ell\in L$ and $p\in P$.
::: {.proof}
The vector $p$ satisfies $2+2(-1)=0$, so $p\in P$. Also
\[
\det\begin{pmatrix}1&2\\2&-1\end{pmatrix}=-5\ne0,
\]
so $\ell,p$ are linearly independent.
:::

<1>2. Every vector $(x,y)^t$ has a unique decomposition
\[
\begin{pmatrix}x\\y\end{pmatrix}
=a\ell+bp,
\qquad
b=\frac{2x-y}{5}.
\]
::: {.proof}
The equations are
\[
x=a+2b,\qquad y=2a-b.
\]
Substituting $a=x-2b$ into the second equation gives
\[
y=2x-5b,
\]
so $b=(2x-y)/5$.
:::

<1>3. Since $T$ vanishes on $L$ and is the identity on $P$,
\[
T\begin{pmatrix}x\\y\end{pmatrix}
=b p
=\frac{2x-y}{5}\begin{pmatrix}2\\-1\end{pmatrix}.
\]
:::

<1>4. Therefore the standard matrix of $T$ is
\[
\boxed{
[T]=\frac15
\begin{pmatrix}
4&-2\\
-2&1
\end{pmatrix}.}
\]
::: {.proof}
Expanding <1>3 gives
\[
T(x,y)=\left(\frac{4x-2y}{5},\frac{-2x+y}{5}\right),
\]
whose coefficient matrix is the displayed matrix.
:::
:::
