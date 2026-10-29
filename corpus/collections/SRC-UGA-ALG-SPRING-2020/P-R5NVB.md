---
schema: qual/card@1
id: P-R5NVB
kind: problem
title: Jordan form, conjugating matrix, and minimal polynomial of $\begin{pmatrix}2&0&0\\4&6&1\\-16&-16&-2\end{pmatrix}$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Minimal and Characteristic Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let
$$
A=\left[\begin{array}{ccc}
2 & 0 & 0 \\
4 & 6 & 1 \\
-16 & -16 & -2
\end{array}\right] \in M_{3}(\mathrm{C})
.$$

a.
Find the Jordan canonical form $J$ of $A$.

b.
Find an invertible matrix $P$ such that $\inverseof{P} A P = J$.

c.
Write down the minimal polynomial of $A$.

> You should not need to compute $\inverseof{P}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The characteristic polynomial of $A$ is $(x-2)^3$, while its minimal polynomial is
$$
\boxed{m_A(x)=(x-2)^2}.
$$


::: pf-proof

The characteristic polynomial is
$$
\chi_A(x)=(x-2)^3.
$$
Moreover
$$
A-2I=
\begin{bmatrix}
0&0&0\\
4&4&1\\
-16&-16&-4
\end{bmatrix}
\neq0,
\qquad
(A-2I)^2=0.
$$
Thus the minimal polynomial is
$$
m_A(x)=(x-2)^2.
$$
Since $A-2I\neq0$ but $(A-2I)^2=0$, the minimal polynomial is exactly $(x-2)^2$.

:::

:::

::: {.pf-step #s1-2}

The Jordan canonical form of $A$ is
$$
\boxed{J=\begin{pmatrix}2&1&0\\0&2&0\\0&0&2\end{pmatrix}}.
$$


::: pf-proof

Consequently the Jordan form has one block of size $2$ and one block of size $1$:
$$
J=
\begin{bmatrix}
2&1&0\\
0&2&0\\
0&0&2
\end{bmatrix}.
$$
By step [](#s1-1){.pf-ref}, these are precisely the block sizes compatible with the minimal and characteristic polynomials.

:::

:::

::: {.pf-step #s1-3}

An invertible conjugating matrix is
$$
\boxed{P=\begin{pmatrix}0&1&-1\\4&0&1\\-16&0&0\end{pmatrix}}.
$$


::: pf-proof

One suitable change-of-basis matrix is
$$
P=
\begin{bmatrix}
0&1&-1\\
4&0&1\\
-16&0&0
\end{bmatrix}.
$$
Its determinant is $-16\ne0$, and direct multiplication gives
$$
AP=PJ,
$$
so $P^{-1}AP=J$.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-1){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::
