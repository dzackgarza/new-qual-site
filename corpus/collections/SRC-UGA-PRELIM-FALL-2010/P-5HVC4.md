---
schema: qual/card@1
id: P-5HVC4
kind: problem
title: Diagonalizability of $\begin{pmatrix}0&1\\6&-1\end{pmatrix}$ and a closed form
  for $A^k\begin{pmatrix}1\\7\end{pmatrix}$
classification:
  areas:
  - prelim
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Matrices
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
    Lamport structure. Mixed the characteristic polynomial out, checked both eigenvectors against A (Av_2 = 2 v_2 and Av_{-3} = -3 v_{-3}), checked the coordinate decomposition (1,7) = 2(1,2) - (1,-3), and checked the closed form at k = 0 against the identity vector and at k = 1 against A(1,7) = (7,-1). The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair; the matrix, the eigenvalues, the eigenvectors and the closed form are all correct as written.
---

::: {.problem}
Let $A = \begin{bmatrix} 0 & 1 \\ 6 & -1 \end{bmatrix}$.
Prove that $A$ is diagonalizable and find a closed-form expression for $A^k \begin{bmatrix} 1 \\ 7 \end{bmatrix}$, $k \in \NN$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own. Write $A=\begin{bmatrix}0&1\\6&-1\end{bmatrix}$ and $w=\binom17$.

::: pf

::: {.pf-step #charpoly}
$\det(\lambda I-A)=\lambda^2+\lambda-6=(\lambda-2)(\lambda+3)$.

::: pf-proof
$\lambda I-A=\begin{bmatrix}\lambda&-1\\-6&\lambda+1\end{bmatrix}$, whose determinant is $\lambda(\lambda+1)-(-1)(-6)=\lambda^2+\lambda-6$; and $\lambda^2+\lambda-6=(\lambda-2)(\lambda+3)$ because the roots of $x^2+x-6$ are $2$ and $-3$ (their sum is $-1$ and their product $-6$).
:::

:::

::: {.pf-step #diagonalizable}
$A$ is diagonalizable over $\RR$.

::: pf-proof
$A$ is a real $2\times2$ matrix whose characteristic polynomial has the two distinct real roots $2$ and $-3$, by step [](#charpoly){.pf-ref}. A matrix whose characteristic polynomial splits into distinct linear factors over the field is diagonalizable.
:::

:::

::: {.pf-step #eigenvectors}
$v_2=\binom12$ spans the eigenspace for $2$ and $v_{-3}=\binom1{-3}$ spans the eigenspace for $-3$.

::: pf-proof
$Av_2=\binom{0\cdot1+1\cdot2}{6\cdot1-1\cdot2}=\binom26=2v_2$, and $Av_{-3}=\binom{0-3}{6+3}=\binom{-3}{9}=-3v_{-3}$; a nonzero eigenvector for a simple root spans its eigenspace.
:::

:::

::: {.pf-step #coordinates}
$w=2v_2-v_{-3}$.

::: pf-proof
$2\binom12-\binom1{-3}=\binom{2-1}{4+3}=\binom17$.
:::

:::

::: {.pf-step #closedform}
For $k\ge0$, $A^kw=2^{k+1}v_2-(-3)^kv_{-3}=\binom{2^{k+1}-(-3)^k}{2^{k+2}+3(-3)^k}$.

::: pf-proof
By step [](#eigenvectors){.pf-ref}, $A^kv_\lambda=\lambda^kv_\lambda$ for $\lambda\in\{2,-3\}$; so from step [](#coordinates){.pf-ref},
$$
A^kw=2A^kv_2-A^kv_{-3}=2\cdot2^k\binom12-(-3)^k\binom1{-3}=\binom{2^{k+1}-(-3)^k}{2^{k+2}+3(-3)^k},
$$
since $-(-3)^k\cdot(-3)=3(-3)^k$. For $k=0$ this reads $\binom17$, and at $k=1$ the matrix product $Aw=\binom{7}{-1}$ agrees with $\binom{4+3}{8-9}$.
:::

:::

:::
:::
