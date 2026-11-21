---
schema: qual/card@1
id: P-VPCLD
kind: problem
title: Diagonalize $\begin{pmatrix}4&-6\\3&-5\end{pmatrix}$ by similarity
classification:
  areas:
  - prelim
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it by direct
    computation: det(lambda I - M) = lambda^2 + lambda - 2 with roots 1 and -2, the two
    eigenvector relations M(2,1) = (2,1) and M(1,1) = -2(1,1), det A = 1 with the inverse
    written out, and MA = AB giving M = A B A^{-1} for B = diag(1,-2). The prose asserted
    the eigenvalues and the eigenvectors without computing them. The collection's
    provenance is the examination paper only, so no retained solution set covers the
    exercise and the argument is the card's own.
---

::: {.problem}
Find an invertible matrix $A$ and a diagonal matrix $B$ such that
$$
\begin{pmatrix}4&-6\\3&-5\end{pmatrix}=ABA^{-1}.
$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Write $M\coloneqq\begin{pmatrix}4&-6\\3&-5\end{pmatrix}$.

::: pf

::: {.pf-step #charpoly}
The characteristic polynomial of $M$ is
$$
\det(\lambda I-M)=\lambda^2+\lambda-2=(\lambda-1)(\lambda+2),
$$
so the eigenvalues of $M$ are $1$ and $-2$.

::: pf-proof
$\det(\lambda I-M)=\det\begin{pmatrix}\lambda-4&6\\-3&\lambda+5\end{pmatrix}=(\lambda-4)(\lambda+5)+18=\lambda^2+\lambda-2$, and the quadratic factors as stated.
:::

:::

::: {.pf-step #eigenvectors}
$M\binom21=\binom21$ and $M\binom11=\binom{-2}{-2}=-2\binom11$.

::: pf-proof
Direct computation: $M\binom21=\binom{8-6}{6-5}=\binom21$ and $M\binom11=\binom{4-6}{3-5}=\binom{-2}{-2}$.
:::

:::

::: {.pf-step #invertible}
$A\coloneqq\begin{pmatrix}2&1\\1&1\end{pmatrix}$ is invertible, with $A^{-1}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$.

::: pf-proof
$\det A=2\cdot1-1\cdot1=1\ne0$, and the displayed matrix multiplies with $A$ to the identity in either order.
:::

:::

::: {.pf-step}
$\begin{pmatrix}4&-6\\3&-5\end{pmatrix}=ABA^{-1}$ for $B\coloneqq\begin{pmatrix}1&0\\0&-2\end{pmatrix}$.

::: pf-proof
Taking the two eigenvector relations of step [](#eigenvectors){.pf-ref} as the two columns of one matrix equation gives
$$
MA=\begin{pmatrix}M\binom21&M\binom11\end{pmatrix}=\begin{pmatrix}\binom21&-2\binom11\end{pmatrix}=A\begin{pmatrix}1&0\\0&-2\end{pmatrix}=AB,
$$
so $M=ABA^{-1}$ by step [](#invertible){.pf-ref}.
:::

:::

:::
:::
