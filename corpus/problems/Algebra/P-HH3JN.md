---
schema: qual/card@1
id: P-HH3JN
kind: problem
title: Spectral theorem for real symmetric matrices
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Prove that every real symmetric matrix $A \in M_n(\mathbb{R})$ has **real eigenvalues** and can be **orthogonally diagonalized**: there exists an orthogonal matrix $Q \in O(n)$ such that $Q^T A Q = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ (The Real Spectral Theorem).
:::

::: solution
**Goal:** Prove that real symmetric matrices have all real eigenvalues and an orthonormal basis of eigenvectors in $\mathbb{R}^n$.

<1>1. Real Eigenvalues:
    *Proof:*
    <2>1. Let $A \in M_n(\mathbb{R})$ with $A^T = A$.
    <2>2. Viewed as a complex matrix $A \in M_n(\mathbb{C})$, $A$ is Hermitian: $A^* = \bar{A}^T = A^T = A$.
    <2>3. By the **Fundamental Theorem of Algebra**, the characteristic polynomial $p_A(\lambda) = \det(\lambda I - A)$ has at least one complex root $\lambda \in \mathbb{C}$.
    <2>4. Let $v \in \mathbb{C}^n \setminus \{0\}$ be a corresponding non-zero eigenvector, so $A v = \lambda v$.
    <2>5. Consider the scalar $v^* A v$:
        $$v^* A v = v^* (\lambda v) = \lambda (v^* v) = \lambda \|v\|^2.$$
    <2>6. Taking conjugate transposes (using that $v^* A v \in \mathbb{C}$ is a $1 \times 1$ scalar):
        $$(v^* A v)^* = v^* A^* v = v^* A v = \bar{\lambda} \|v\|^2.$$
    <2>7. Thus $\lambda \|v\|^2 = \bar{\lambda} \|v\|^2$.
    <2>8. Since $v \ne 0$, $\|v\|^2 > 0$, so $\lambda = \bar{\lambda}$, which proves $\lambda \in \mathbb{R}$.
    <2>9. Since $\lambda \in \mathbb{R}$, $(A - \lambda I) \in M_n(\mathbb{R})$ is a real singular matrix, so there exists a **real non-zero eigenvector** $u_1 \in \mathbb{R}^n$ with $A u_1 = \lambda u_1$.

<1>2. Orthogonality of Eigenvectors and Invariant Subspaces:
    *Proof:*
    <2>1. Normalize $u_1$ so that $\|u_1\|_2 = 1$.
    <2>2. Let $W = (\operatorname{span}(u_1))^\perp = \{ x \in \mathbb{R}^n \mid u_1^T x = 0 \}$ be the orthogonal complement of $u_1$ in $\mathbb{R}^n$, which has dimension $n - 1$.
    <2>3. We claim that $W$ is **$A$-invariant**: $A(W) \subseteq W$.
    <2>4. Let $w \in W$. We compute the inner product of $A w$ with $u_1$:
        $$u_1^T (A w) = (u_1^T A) w = (A^T u_1)^T w = (A u_1)^T w = (\lambda_1 u_1)^T w = \lambda_1 (u_1^T w) = \lambda_1 \cdot 0 = 0.$$
    <2>5. Thus $A w \in W$, confirming $A(W) \subseteq W$.

<1>3. Induction on Dimension $n$:
    *Proof:*
    <2>1. **Base Case $n = 1$:** Any $1 \times 1$ real matrix is already diagonal, so $Q = [1]$ diagonalizes it.
    <2>2. **Inductive Hypothesis:** Assume every $(n-1) \times (n-1)$ real symmetric matrix has an orthonormal basis of eigenvectors.
    <2>3. **Inductive Step:**
        - Choose an orthonormal basis $\{q_2, \dots, q_n\}$ for the $(n-1)$-dimensional subspace $W$.
        - The restriction $A|_W: W \to W$ is a symmetric linear operator on $W$ with the standard inner product.
        - By the inductive hypothesis, $W$ possesses an orthonormal basis $\{u_2, \dots, u_n\}$ of eigenvectors of $A|_W$ (hence of $A$), with real eigenvalues $\lambda_2, \dots, \lambda_n \in \mathbb{R}$.
        - Since each $u_i \in W = u_1^\perp$, we have $u_1^T u_i = 0$ for all $i \ge 2$.
        - Thus $\{u_1, u_2, \dots, u_n\}$ is an **orthonormal basis of $\mathbb{R}^n$ consisting of eigenvectors of $A$**.

<1>4. Orthogonal Diagonalization Matrix $Q$:
    *Proof:*
    <2>1. Form the matrix $Q = [u_1 \mid u_2 \mid \cdots \mid u_n] \in M_n(\mathbb{R})$.
    <2>2. Since the columns are orthonormal, $Q^T Q = I_n$, so $Q \in O(n)$ is an orthogonal matrix.
    <2>3. We compute $A Q$:
        $$A Q = [A u_1 \mid \cdots \mid A u_n] = [\lambda_1 u_1 \mid \cdots \mid \lambda_n u_n] = Q \operatorname{diag}(\lambda_1, \dots, \lambda_n).$$
    <2>4. Multiplying on the left by $Q^T = Q^{-1}$:
        $$Q^T A Q = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n).$$

<1>5. Conclusion:
    Every real symmetric matrix has real eigenvalues $\lambda = \bar{\lambda}$ and is orthogonally diagonalizable: $Q^T A Q = \Lambda$. Q.E.D.
:::
