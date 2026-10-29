---
schema: qual/card@1
id: P-UCLAB12W-08
kind: problem
title: Approximation by diagonalizable matrices with simple spectrum
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Let $A$ be an $n\times n$ complex matrix.
Prove that there are sequences of matrices $(B_i)$ and $(L_i)$ such that each $L_i$ is diagonal with distinct eigenvalues and
$$
B_iL_iB_i^{-1}\longrightarrow A
$$
entrywise as $i\to\infty$.
:::

::: {.solution}

::: pf

::: pf-step

There is an invertible matrix $S$ such that
$$
T=S^{-1}AS
$$
is upper triangular.


::: pf-proof

This is proved by induction on $n$ without using a canonical-form theorem. For $n=1$ it is immediate. Suppose $n>1$. Since the characteristic polynomial of $A$ has a root over $\CC$, $A$ has an eigenvector $v_1\ne0$. Extend $v_1$ to a basis of $\CC^n$. In this basis the first column of the matrix of $A$ is $(\lambda,0,\ldots,0)^t$, so the matrix has block form
$$
\begin{pmatrix}
\lambda&*\\
0&C
\end{pmatrix}
$$
for some $(n-1)\times(n-1)$ matrix $C$. By the induction hypothesis, after changing only the last $n-1$ basis vectors, $C$ becomes upper triangular. The full matrix is then upper triangular. The resulting change-of-basis matrix is the required $S$.

:::

:::

::: {.pf-step #s1-2}

For every positive integer $i$, one can choose pairwise distinct complex numbers
$$
\lambda_{i,1},\ldots,\lambda_{i,n}
$$
such that
$$
\abs{\lambda_{i,j}-T_{jj}}<\frac1i
$$
for every $j$.


::: pf-proof

For fixed $i$, choose the numbers successively. The open disk of radius $1/i$ about $T_{11}$ is nonempty, so choose $\lambda_{i,1}$ in it. Having chosen $\lambda_{i,1},\ldots,\lambda_{i,j-1}$, the open disk of radius $1/i$ about $T_{jj}$ contains infinitely many complex numbers, while only finitely many are forbidden. Choose $\lambda_{i,j}$ in that disk and distinct from all earlier choices.

:::

:::

::: {.pf-step #s1-3}

Let $T_i$ be the upper-triangular matrix obtained from $T$ by replacing its diagonal entries $T_{jj}$ with $\lambda_{i,j}$ and leaving all off-diagonal entries unchanged. Then
$$
T_i\longrightarrow T
$$
entrywise.


::: pf-proof

Every off-diagonal entry of $T_i-T$ is zero. By step [](#s1-2){.pf-ref}, the $j$-th diagonal entry satisfies
$$
\abs{(T_i)_{jj}-T_{jj}}<\frac1i.
$$
Thus every matrix entry converges to the corresponding entry of $T$.

:::

:::

::: {.pf-step #s1-4}

Each $T_i$ has $n$ distinct eigenvalues, namely
$$
\lambda_{i,1},\ldots,\lambda_{i,n}.
$$


::: pf-proof

For an upper-triangular matrix,
$$
\det(zI-T_i)
=
\prod_{j=1}^n(z-\lambda_{i,j}).
$$
By step [](#s1-2){.pf-ref}, the diagonal entries are pairwise distinct, so these are $n$ distinct eigenvalues.

:::

:::

::: {.pf-step #s1-5}

Each $T_i$ is diagonalizable. Thus there are an invertible matrix $C_i$ and a diagonal matrix $L_i$ with distinct diagonal entries such that
$$
T_i=C_iL_iC_i^{-1}.
$$


::: pf-proof

Choose a nonzero eigenvector for each of the $n$ distinct eigenvalues from step [](#s1-4){.pf-ref}. Eigenvectors belonging to distinct eigenvalues are linearly independent, so these $n$ vectors form a basis of $\CC^n$. Let $C_i$ have these eigenvectors as columns and let $L_i$ be the diagonal matrix of their eigenvalues. Then
$$
T_iC_i=C_iL_i,
$$
which is equivalent to the displayed identity. The diagonal entries of $L_i$ are distinct by step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Define
$$
B_i=SC_i.
$$
Then
$$
B_iL_iB_i^{-1}=ST_iS^{-1}.
$$


::: pf-proof

Using step [](#s1-5){.pf-ref},
$$
B_iL_iB_i^{-1}
=SC_iL_iC_i^{-1}S^{-1}
=ST_iS^{-1}.
$$

:::

:::

::: {.pf-step #s1-7}

One has
$$
B_iL_iB_i^{-1}\longrightarrow A
$$
entrywise.


::: pf-proof

By step [](#s1-3){.pf-ref}, $T_i\to T$ entrywise. Since $S$ and $S^{-1}$ are fixed, every entry of
$$
ST_iS^{-1}
$$
is a fixed finite linear combination of entries of $T_i$, so
$$
ST_iS^{-1}\longrightarrow STS^{-1}=A
$$
entrywise. Apply step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref} construct the required matrices $B_i$ and diagonal matrices $L_i$ with distinct eigenvalues and prove the required convergence.

:::

:::

:::
