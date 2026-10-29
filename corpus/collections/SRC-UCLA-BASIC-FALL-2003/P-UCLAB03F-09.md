---
schema: qual/card@1
id: P-UCLAB03F-09
kind: problem
title: Completing the eigendata of a symmetric three-by-three matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the official UCLA Basic Exam Fall 2003 PDF.
---

::: {.problem}
Let $A$ be a real symmetric $3\times3$ matrix with determinant $6$.
Suppose
$$
(1,2,3)
\qquad\text{and}\qquad
(0,3,-2)
$$
are eigenvectors with eigenvalues $1$ and $2$, respectively.
Justify your answers to the following.

(a) Give an eigenvector of the form $(1,x,y)$ that is linearly independent of the two vectors above.

(b) What is the eigenvalue of this eigenvector?
:::

::: {.solution}

Let
$$
v_1=(1,2,3),
\qquad
v_2=(0,3,-2).
$$

::: pf

::: pf-step

The vectors $v_1$ and $v_2$ are orthogonal.


::: pf-proof

Direct computation gives
$$
v_1\cdot v_2
=
1\cdot0+2\cdot3+3(-2)
=0.
$$
This is also forced by symmetry of $A$, since eigenvectors of a real symmetric matrix belonging to distinct eigenvalues are orthogonal.

:::

:::

::: pf-step

The vector
$$
w=(-13,2,3)
$$
is orthogonal to both $v_1$ and $v_2$.


::: pf-proof

It is their cross product:
$$
v_1\times v_2
=
\begin{vmatrix}
\mathbf i&\mathbf j&\mathbf k\\
1&2&3\\
0&3&-2
\end{vmatrix}
=
(-13,2,3).
$$
Hence $w$ is orthogonal to both.

:::

:::

::: {.pf-step #s1-3}

The line
$$
L=\operatorname{span}\{w\}
$$
is invariant under $A$.


::: pf-proof

The vectors $v_1,v_2$ are linearly independent, so their orthogonal complement in $\RR^3$ is one-dimensional and equals $L$.

If $z\in L$, then for $i=1,2$,
$$
\langle Az,v_i\rangle
=
\langle z,Av_i\rangle
=
\lambda_i\langle z,v_i\rangle
=0,
$$
because $A$ is symmetric and $z\perp v_i$. Thus $Az$ is orthogonal to both $v_1$ and $v_2$, so $Az\in L$.

:::

:::

::: {.pf-step #s1-4}

The vector
$$
\boxed{\left(1,-\frac2{13},-\frac3{13}\right)}
$$
is an eigenvector of $A$ and is linearly independent of $v_1,v_2$.


::: pf-proof

By step [](#s1-3){.pf-ref}, the nonzero one-dimensional subspace $L$ is $A$-invariant, so every nonzero vector in $L$ is an eigenvector. Dividing $w=(-13,2,3)$ by $-13$ gives the displayed vector. It is orthogonal to $v_1,v_2$, hence cannot lie in their span except as the zero vector, so it is linearly independent of them.

:::

:::

::: {.pf-step #s1-5}

The eigenvalue corresponding to the vector in step [](#s1-4){.pf-ref} is
$$
\boxed{3}.
$$


::: pf-proof

Let the third eigenvalue be $\mu$. By step [](#s1-4){.pf-ref}, the three displayed eigenvectors form a basis of $\RR^3$. Hence in that basis the matrix of $A$ is diagonal with diagonal entries
$$
1,\quad2,\quad\mu.
$$
Similarity preserves determinant, so
$$
6=\det A=1\cdot2\cdot\mu.
$$
Therefore
$$
\mu=3.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} answers part (a), and step [](#s1-5){.pf-ref} answers part (b).

:::

:::

:::
