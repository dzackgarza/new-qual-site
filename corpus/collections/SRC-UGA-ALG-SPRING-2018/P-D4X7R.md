---
schema: qual/card@1
id: P-D4X7R
kind: problem
title: Jordan form of $\begin{pmatrix}0&1&-2\\1&1&-3\\1&2&-4\end{pmatrix}$ and a conjugating
  matrix
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
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude
  date: 2026-11-18
  note: Read against the UGA Algebra Qualifying Exam, Spring 2018, Problem 3; both parts match.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    No retained solution set covers this examination. Structured the card's own computation
    into numbered steps: characteristic polynomial, rank and nullity of $A+I$, the single
    Jordan block, the generalized-eigenvector chain, and verification of the two column
    identities $Av_2=v_1-v_2$, $Av_3=v_2-v_3$ that give $P^{-1}AP=J$. Checked the
    determinant of $P$ and the chain equations independently.
---

::: {.problem}
Let
$$
A=\left[\begin{array}{lll}{0} & {1} & {-2} \\ {1} & {1} & {-3} \\ {1} & {2} & {-4}\end{array}\right] \in M_{3}(\CC)
$$

a. Find the Jordan canonical form $J$ of $A$.

b. Find an invertible matrix $P$ such that $\inverseof{P} AP = J$.

> You should not need to compute $\inverseof{P}$.
:::

::: {.solution}

No retained solution set covers this examination; the computation below is the card's own.

::: pf

::: {.pf-step #charpoly}
$\det(\lambda I-A)=(\lambda+1)^3$, so $-1$ is the only eigenvalue of $A$, with algebraic multiplicity $3$.

::: pf-proof
Expanding along the first column of
$$
\lambda I-A=\begin{pmatrix}\lambda&-1&2\\-1&\lambda-1&3\\-1&-2&\lambda+4\end{pmatrix}
$$
gives
$$
\lambda\bigl[(\lambda-1)(\lambda+4)+6\bigr]-(-1)\bigl[(-1)(\lambda+4)+3\bigr]+(-1)\bigl[(-1)(-2)-(\lambda-1)\bigr],
$$
which simplifies to $(\lambda+1)(\lambda^2+2\lambda+1)=(\lambda+1)^3$. The trace $-3$ and determinant $-1$ agree with $(-1)^3$.
:::
:::

::: {.pf-step #nullity}
$A+I$ has rank $2$, so $\lambda=-1$ has geometric multiplicity $1$ and the Jordan form is a single $3\times3$ block.

::: pf-proof
$$
A+I=\begin{pmatrix}1&1&-2\\1&2&-3\\1&2&-3\end{pmatrix},
$$
whose second and third rows are equal and whose first two rows are independent; hence the rank is $2$ and the nullity is $3-2=1$. A single block in a space of dimension $3$ is forced.
:::
:::

::: {.pf-step #jordan}
$$
J=\begin{pmatrix}-1&1&0\\0&-1&1\\0&0&-1\end{pmatrix}.
$$

::: pf-proof
There is one Jordan block, of size $3$, with eigenvalue $-1$; its standard form is displayed.
:::
:::

::: {.pf-step #chain}
With
$$
v_3=\begin{pmatrix}0\\0\\1\end{pmatrix},\qquad
v_2=(A+I)v_3=\begin{pmatrix}-2\\-3\\-3\end{pmatrix},\qquad
v_1=(A+I)v_2=\begin{pmatrix}1\\1\\1\end{pmatrix},
$$
the vectors satisfy $(A+I)v_1=0$, $(A+I)v_2=v_1$, and $(A+I)v_3=v_2$.

::: pf-proof
The products are computed directly from $A+I$:
$(A+I)v_3$ is the third column, and $(A+I)v_2$ gives each entry $-2-3+6=1$. Then $(A+I)v_1$ gives $1+1-2=0$, $1+2-3=0$, $1+2-3=0$.
:::
:::

::: {.pf-step #conjugating}
The matrix $P=[v_1\mid v_2\mid v_3]$ is invertible and satisfies $P^{-1}AP=J$.

::: pf-proof
$P=\begin{pmatrix}1&-2&0\\1&-3&0\\1&-3&1\end{pmatrix}$ has determinant $-1\ne0$, so it is invertible. The chain identities are equivalent to $Av_1=-v_1$, $Av_2=v_1-v_2$, and $Av_3=v_2-v_3$, which say exactly that the columns of $AP$ are the columns of $PJ$. Hence $AP=PJ$ and $P^{-1}AP=J$.
:::
:::

:::
:::
