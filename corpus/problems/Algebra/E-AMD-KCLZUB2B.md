---
schema: qual/card@1
id: E-AMD-KCLZUB2B
kind: problem
title: A linear operator is diagonalizable iff $V$ is the direct sum of its eigenspaces
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that a matrix representing a linear map $T:V\to V$ is diagonalizable iff $V$ is a direct sum of eigenspaces $V = \bigoplus_i \ker(T -\lambda_i I)$.
:::

::: solution
**Goal:** Prove that $T: V \to V$ is diagonalizable if and only if $V = \bigoplus_{i=1}^k E(\lambda_i)$, where $E(\lambda_i) = \ker(T - \lambda_i I)$ ranges over the distinct eigenvalues of $T$.

<1>1. Forward direction (diagonalizable $\implies$ eigenspace decomposition):
    *Proof:*
    <2>1. Suppose $T$ is diagonalizable. Then there exists a basis $\mathcal{B} = \{v_1, \dots, v_n\}$ of $V$ consisting of eigenvectors of $T$.
    <2>2. Let $\lambda_1, \dots, \lambda_k$ be the distinct eigenvalues of $T$.
    <2>3. Partition $\mathcal{B}$ by eigenvalue: $\mathcal{B}_i = \{v \in \mathcal{B} \mid T v = \lambda_i v\}$.
    <2>4. Each $\mathcal{B}_i$ is a basis for $E(\lambda_i)$, and $\mathcal{B} = \mathcal{B}_1 \sqcup \cdots \sqcup \mathcal{B}_k$.
    <2>5. Since $\mathcal{B}$ is a basis for $V$, every $v \in V$ is a unique linear combination of vectors from $\mathcal{B}_1, \dots, \mathcal{B}_k$.
    <2>6. Thus $V = E(\lambda_1) \oplus \cdots \oplus E(\lambda_k)$.

<1>2. Reverse direction (eigenspace decomposition $\implies$ diagonalizable):
    *Proof:*
    <2>1. Suppose $V = \bigoplus_{i=1}^k E(\lambda_i)$.
    <2>2. Choose a basis $\mathcal{B}_i$ for each eigenspace $E(\lambda_i)$.
    <2>3. Since the sum is direct, $\mathcal{B} = \mathcal{B}_1 \cup \cdots \cup \mathcal{B}_k$ is a basis for $V$.
    <2>4. Every vector in $\mathcal{B}$ is an eigenvector of $T$.
    <2>5. The matrix of $T$ with respect to $\mathcal{B}$ is diagonal, with the eigenvalues $\lambda_i$ on the diagonal (each $\lambda_i$ appearing $\dim E(\lambda_i)$ times).

<1>3. Equivalently, the dimension condition:
    *Proof:*
    <2>1. The eigenspaces $E(\lambda_1), \dots, E(\lambda_k)$ are always linearly independent (eigenvectors for distinct eigenvalues are linearly independent).
    <2>2. Thus $\dim(E(\lambda_1) + \cdots + E(\lambda_k)) = \sum_{i=1}^k \dim E(\lambda_i)$.
    <2>3. The decomposition $V = \bigoplus_i E(\lambda_i)$ holds if and only if $\sum_{i=1}^k \dim E(\lambda_i) = \dim V$, i.e. each eigenvalue's geometric multiplicity equals its algebraic multiplicity.

<1>4. Conclusion:
    $T$ is diagonalizable $\iff$ $V = \bigoplus_{i=1}^k \ker(T - \lambda_i I)$. Q.E.D.
:::
