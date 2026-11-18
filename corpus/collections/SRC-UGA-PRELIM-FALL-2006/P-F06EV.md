---
schema: qual/card@1
id: P-F06EV
kind: problem
title: Eigenvalues and eigenvectors of $\begin{pmatrix}1&-2\\3&-4\end{pmatrix}$
classification:
  areas:
  - prelim
  topics:
  - Eigenvalues
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's computation into numbered steps; the characteristic polynomial, the two
    kernels and the description of the eigenvectors are unchanged. Checked: the determinant
    expansion, the factorization, and both kernel computations. Not checked against a printed
    source: the UGA preliminary examinations are not retained in tmp/sources and the card records
    no page.
---

::: {.problem}
Find the eigenvalues and eigenvectors of the matrix $A = \begin{bmatrix} 1 & -2 \\ 3 & -4 \end{bmatrix}$.
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $A=\begin{bmatrix}1&-2\\3&-4\end{bmatrix}$ acts on $\RR^{2}$, the characteristic polynomial is $\det(A-\lambda I)$, and the eigenspace for $\lambda$ is $\ker(A-\lambda I)$.

::: pf

::: {.pf-step #charpoly}

$\det(A-\lambda I)=\lambda^{2}+3\lambda+2=(\lambda+1)(\lambda+2)$.

::: pf-proof

$\det\begin{bmatrix}1-\lambda&-2\\3&-4-\lambda\end{bmatrix}=(1-\lambda)(-4-\lambda)-(-2)(3)=\lambda^{2}+3\lambda-4+6=\lambda^{2}+3\lambda+2$, which factors as displayed.

:::

:::

::: {.pf-step #eigen}

The eigenvalues are $-1$ and $-2$.

::: pf-proof

The eigenvalues are the roots of the characteristic polynomial, which by step [](#charpoly){.pf-ref} are $-1$ and $-2$.

:::

:::

::: {.pf-step #first}

$\ker(A+I)=\operatorname{span}\theset{(1,1)^{t}}$.

::: pf-proof

$A+I=\begin{bmatrix}2&-2\\3&-3\end{bmatrix}$, whose kernel is the solution set of $2x-2y=0$ and $3x-3y=0$, that is $x=y$; this is the line spanned by $(1,1)^{t}$.

:::

:::

::: {.pf-step #second}

$\ker(A+2I)=\operatorname{span}\theset{(2,3)^{t}}$.

::: pf-proof

$A+2I=\begin{bmatrix}3&-2\\3&-2\end{bmatrix}$, whose two rows give the single equation $3x-2y=0$, whose solutions are the multiples of $(2,3)^{t}$.

:::

:::

::: {.pf-step #done}

The eigenvectors for $-1$ are the nonzero multiples of $(1,1)^{t}$, and those for $-2$ the nonzero multiples of $(2,3)^{t}$.

::: pf-proof

An eigenvector for $\lambda$ is a nonzero element of $\ker(A-\lambda I)$; steps [](#first){.pf-ref} and [](#second){.pf-ref} identify the two kernels, and an eigenvector must be nonzero.

:::

:::

:::

:::
