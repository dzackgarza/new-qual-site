---
schema: qual/card@1
id: P-F12PD
kind: problem
title: Diagonalize $\begin{pmatrix}7&-3\\1&3\end{pmatrix}$
classification:
  areas:
  - prelim
  topics:
  - Diagonalization
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
    Restructured the prose solution into a Lamport proof and checked it by direct
    computation: det(lambda I - A) = lambda^2 - 10 lambda + 24 with roots 4 and 6, the
    eigenvector relations A(1,1) = 4(1,1) and A(3,1) = (18,6) = 6(3,1), det P = -2, and
    AP = PD column by column giving P^-1 AP = D. The prose asserted the eigenpairs; they
    are now verified. The statement is true as printed. The collection's provenance is the
    examination paper only, so no retained solution set covers the exercise and the
    argument is the card's own.
---

::: {.problem}
Let $A = \begin{pmatrix} 7 & -3 \\ 1 & 3 \end{pmatrix}$.
Find an invertible matrix $P$ and a diagonal matrix $D$ with $P^{-1}AP = D$.
[You should not have to compute $P^{-1}$.]
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #charpoly}
$\det(\lambda I-A)=\lambda^2-10\lambda+24=(\lambda-4)(\lambda-6)$, so the eigenvalues of $A$ are $4$ and $6$.

::: pf-proof
$\det\begin{pmatrix}\lambda-7&3\\-1&\lambda-3\end{pmatrix}=(\lambda-7)(\lambda-3)+3=\lambda^2-10\lambda+21+3$, and $\lambda^2-10\lambda+24$ factors as displayed.
:::

:::

::: {.pf-step #eigen}
$A\binom11=4\binom11$ and $A\binom31=6\binom31$.

::: pf-proof
$A\binom11=\binom{7-3}{1+3}=\binom44$ and $A\binom31=\binom{21-3}{3+3}=\binom{18}{6}=6\binom31$.
:::

:::

::: {.pf-step #invertible}
$P\coloneqq\begin{pmatrix}1&3\\1&1\end{pmatrix}$ satisfies $\det P=-2\ne0$.

::: pf-proof
$\det P=1\cdot1-3\cdot1=-2$.
:::

:::

::: {.pf-step}
$P^{-1}AP=D$ for $D\coloneqq\begin{pmatrix}4&0\\0&6\end{pmatrix}$.

::: pf-proof
The two relations of step [](#eigen){.pf-ref} are the columns of the matrix identity
$$
AP=\begin{pmatrix}A\binom11&A\binom31\end{pmatrix}=\begin{pmatrix}4\binom11&6\binom31\end{pmatrix}=P\begin{pmatrix}4&0\\0&6\end{pmatrix}=PD,
$$
so $AP=PD$, and multiplying on the left by $P^{-1}$, which exists by step [](#invertible){.pf-ref}, gives $P^{-1}AP=D$.
:::

:::

:::
:::
