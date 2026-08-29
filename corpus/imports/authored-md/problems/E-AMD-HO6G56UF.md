---
schema: qual/card@1
id: E-AMD-HO6G56UF
kind: exercise
title: Commuting diagonalizable matrices are simultaneously diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that if $A,B$ are diagonalizable and $[A, B] = 0$, then $A$ and $B$ are simultaneously diagonalizable.
:::

::: solution
**Goal:** Prove that two commuting diagonalizable linear operators $A, B$ on a finite-dimensional vector space $V = F^n$ admit a common eigenbasis.

<1>1. Eigenspace decomposition of $V$ under $A$:
    *Proof:*
    <2>1. Because $A$ is diagonalizable, $V$ decomposes into a direct sum of the eigenspaces of $A$:
        $$V = \bigoplus_{i=1}^k E_A(\lambda_i),$$
        where $\lambda_1, \dots, \lambda_k \in F$ are the distinct eigenvalues of $A$, and $E_A(\lambda_i) = \ker(A - \lambda_i I)$.

<1>2. Invariance of each eigenspace $E_A(\lambda_i)$ under $B$:
    *Proof:*
    <2>1. Let $v \in E_A(\lambda_i)$.
    <2>2. Using the commutation hypothesis $A B = B A$:
        $$A(B v) = (A B) v = (B A) v = B(A v) = B(\lambda_i v) = \lambda_i (B v).$$
    <2>3. Thus $B v \in E_A(\lambda_i)$, proving that $E_A(\lambda_i)$ is a $B$-invariant subspace:
        $$B(E_A(\lambda_i)) \subseteq E_A(\lambda_i).$$

<1>3. Diagonalizability of the restricted operator $B|_{E_A(\lambda_i)}$:
    *Proof:*
    <2>1. Since $B$ is diagonalizable on $V$, its minimal polynomial $m_B(x) \in F[x]$ is squarefree (splits into distinct linear factors).
    <2>2. The restriction $B_i = B|_{E_A(\lambda_i)}$ satisfies $m_B(B_i) = 0$, so the minimal polynomial $m_{B_i}(x)$ divides $m_B(x)$.
    <2>3. Because any factor of a squarefree polynomial is squarefree, $m_{B_i}(x)$ is squarefree.
    <2>4. An operator is diagonalizable if and only if its minimal polynomial is squarefree, so $B_i$ is diagonalizable on $E_A(\lambda_i)$.

<1>4. Construction of a common eigenbasis:
    *Proof:*
    <2>1. For each $i \in \{1, \dots, k\}$, choose an eigenbasis $\mathcal{B}_i$ of $E_A(\lambda_i)$ for the operator $B_i$.
    <2>2. Every vector $v \in \mathcal{B}_i$ is:
        - An eigenvector of $A$ with eigenvalue $\lambda_i$, and
        - An eigenvector of $B$ with some eigenvalue $\mu \in F$.
    <2>3. Since $V = \bigoplus_{i=1}^k E_A(\lambda_i)$, the union $\mathcal{B} = \bigcup_{i=1}^k \mathcal{B}_i$ is a basis of $V$.
    <2>4. In the basis $\mathcal{B}$, both $A$ and $B$ are represented by diagonal matrices.

<1>5. Conclusion:
    $A$ and $B$ are simultaneously diagonalizable. Q.E.D.
:::
