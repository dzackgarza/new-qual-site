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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The step that writes $T(v) = bp$ asserted it with no justification; it now derives it by linearity
    from the prescriptions on $L$ and $P$ and from the decomposition that the previous numbered step
    establishes, cited by label. Checked independently: $T(\ell) = 0$ and $T(p) = p$ for the displayed
    matrix, so the matrix is the projection onto $x + 2y = 0$ along $L$. The set is the exam paper of
    the UGA prelim Spring 2006 and retains no solution sheet, so the argument is the card's own. The
    statement is unchanged.
---

::: {.problem}
Let $L \subset \RR^2$ be the line spanned by the vector $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$.
Let $P \subset \RR^2$ be the line defined by the equation $x + 2y = 0$.
Find the standard matrix for the linear transformation $T : \RR^2 \to \RR^2$ such that $T(v) = 0$ for $v \in L$ and $T(v) = v$ for $v \in P$.
:::


::: {.solution}

::: pf

::: {.pf-step #basis}
The vectors
$$
\ell=\begin{pmatrix}1\\2\end{pmatrix},
\qquad
p=\begin{pmatrix}2\\-1\end{pmatrix}
$$
form a basis of $\RR^2$, with $\ell\in L$ and $p\in P$.

::: pf-proof
The vector $p$ satisfies $2+2(-1)=0$, so $p\in P$. Also
$$
\det\begin{pmatrix}1&2\\2&-1\end{pmatrix}=-5\ne0,
$$
so $\ell,p$ are linearly independent.
:::

:::

::: {.pf-step #decomposition}
Every vector $(x,y)^t$ has a unique decomposition
$$
\begin{pmatrix}x\\y\end{pmatrix}
=a\ell+bp,
\qquad
b=\frac{2x-y}{5}.
$$

::: pf-proof
The equations are
$$
x=a+2b,\qquad y=2a-b.
$$
Substituting $a=x-2b$ into the second equation gives
$$
y=2x-5b,
$$
so $b=(2x-y)/5$.
:::

:::

::: {.pf-step #s3}
Since $T$ vanishes on $L$ and is the identity on $P$,
$$
T\begin{pmatrix}x\\y\end{pmatrix}
=b p
=\frac{2x-y}{5}\begin{pmatrix}2\\-1\end{pmatrix}.
$$


::: pf-proof
Step [](#basis){.pf-ref} exhibits $\ell, p$ as a basis, so the vector has exactly one such description. Writing $v = a\ell + bp$ puts $a\ell$ in $L$ and $bp$ in $P$, and $T$ is linear, so $T(v) = aT(\ell) + bT(p) = a \cdot 0 + b p = b p$, with $b = (2x-y)/5$ by step [](#decomposition){.pf-ref}.
:::

:::

::: pf-step
Therefore the standard matrix of $T$ is
$$
\boxed{
[T]=\frac15
\begin{pmatrix}
4&-2\\
-2&1
\end{pmatrix}.}
$$

::: pf-proof
Expanding step [](#s3){.pf-ref} gives
$$
T(x,y)=\left(\frac{4x-2y}{5},\frac{-2x+y}{5}\right),
$$
whose coefficient matrix is the displayed matrix.
:::

:::

:::

:::
