---
schema: qual/card@1
id: E-2KJEL
kind: problem
title: Jordan form of $\begin{pmatrix}5&-1\\9&-1\end{pmatrix}\oplus\begin{pmatrix}7&-2\\12&-3\end{pmatrix}$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Matrices
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Determine $\operatorname{JCF}(B)$ for
$$
B \coloneqq
\begin{pmatrix}
5 & -1 & 0 & 0 \\
9 & -1 & 0 & 0 \\
0 & 0 & 7 & -2 \\
0 & 0 & 12 & -3
\end{pmatrix}
.$$

:::

::: {.solution}
Write
$$
B=B_1\oplus B_2,
\qquad
B_1=\begin{pmatrix}5&-1\\9&-1\end{pmatrix},
\quad
B_2=\begin{pmatrix}7&-2\\12&-3\end{pmatrix}.
$$

::: pf

::: {.pf-step #block-1}
$B_1$ has Jordan form $J_2(2)$.

::: pf-proof
$\chi_{B_1}(t)=(t-5)(t+1)+9=(t-2)^2$, and
$$
B_1-2I=\begin{pmatrix}3&-1\\9&-3\end{pmatrix}
$$
has rank $1$, so the eigenspace for $2$ is one-dimensional and there is one Jordan block.
:::

:::

::: {.pf-step #block-2}
$B_2$ has Jordan form $\operatorname{diag}(1,3)$.

::: pf-proof
$\chi_{B_2}(t)=(t-7)(t+3)+24=t^2-4t+3=(t-1)(t-3)$ has distinct roots, so $B_2$ is diagonalizable.
:::

:::

::: pf-step
Up to the order of the Jordan blocks,
$$
\boxed{
\operatorname{JCF}(B)=
\begin{pmatrix}
2&1&0&0\\
0&2&0&0\\
0&0&1&0\\
0&0&0&3
\end{pmatrix}.}
$$

::: pf-proof
The Jordan form of a block-diagonal matrix is the direct sum of the Jordan forms of its blocks, given by steps [](#block-1){.pf-ref} and [](#block-2){.pf-ref}.
:::

:::

:::

:::
