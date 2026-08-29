---
schema: qual/card@1
id: P-UN3G3
kind: problem
title: The number and sizes of Jordan blocks
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $A \in M_n(\mathbb{C})$ (or an algebraically closed field).
How do you determine the **number** and **sizes** of the blocks in the Jordan Canonical Form of $A$?
:::

::: solution
**Goal:** Determine the Jordan Canonical Form of a matrix $A$ by computing nullities of powers of $(A - \lambda I)$ and identifying elementary divisors/invariant factors.

<1>1. Setting and Terminology:
    *Proof:*
    <2>1. Let $A \in M_n(\mathbb{C})$ have characteristic polynomial $p_A(x) = \prod_{i=1}^k (x - \lambda_i)^{a_i}$, where $\lambda_1, \dots, \lambda_k$ are the distinct eigenvalues with algebraic multiplicities $a_i$.
    <2>2. The Jordan form of $A$ is a block diagonal matrix $J = \bigoplus_{i=1}^k J(\lambda_i)$, where each $J(\lambda_i)$ consists of Jordan blocks $J_m(\lambda_i)$ of size $m \times m$:
        $$J_m(\lambda_i) = \begin{bmatrix} \lambda_i & 1 & 0 & \cdots & 0 \\ 0 & \lambda_i & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_i & 1 \\ 0 & 0 & \cdots & 0 & \lambda_i \end{bmatrix}.$$

<1>2. Sequence of Nullities $d_k(\lambda) = \dim \ker(A - \lambda I)^k$:
    *Proof:*
    <2>1. Fix an eigenvalue $\lambda$. For an individual Jordan block $J_m(\lambda)$, the matrix $N = J_m(\lambda) - \lambda I$ is a nilpotent shift matrix.
    <2>2. The powers $N^k$ have nullities given by:
        $$\dim \ker(N^k) = \min(k, m).$$
    <2>3. Summing across all Jordan blocks $J_{m_1}(\lambda), \dots, J_{m_r}(\lambda)$ associated with eigenvalue $\lambda$, let:
        $$d_k(\lambda) \coloneqq \operatorname{nullity}\left((A - \lambda I)^k\right) = n - \operatorname{rank}\left((A - \lambda I)^k\right).$$
    <2>4. Then $d_0(\lambda) = 0 \le d_1(\lambda) \le d_2(\lambda) \le \dots \le d_m(\lambda) = a_\lambda$.

<1>3. Determining the Total Number of Blocks:
    *Proof:*
    <2>1. Each Jordan block for $\lambda$ contributes exactly 1 to the dimension of the eigenspace $\ker(A - \lambda I)$.
    <2>2. Therefore, the **total number of Jordan blocks** associated with eigenvalue $\lambda$ is the **geometric multiplicity**:
        $$\text{Total number of blocks for } \lambda = \dim \ker(A - \lambda I) = d_1(\lambda) = n - \operatorname{rank}(A - \lambda I).$$

<1>4. Determining the Maximum Block Size:
    *Proof:*
    <2>1. The size of the **largest Jordan block** for $\lambda$ is the smallest integer $m$ such that $\ker(A - \lambda I)^m = \ker(A - \lambda I)^{m+1}$.
    <2>2. This integer $m$ is the multiplicity of $(x - \lambda)$ in the **minimal polynomial** $m_A(x)$.

<1>5. Determining the Number of Blocks of Each Specific Size:
    *Proof:*
    <2>1. The number of Jordan blocks for $\lambda$ of size **at least $k$** is given by the difference of successive nullities:
        $$N_{\ge k}(\lambda) = d_k(\lambda) - d_{k-1}(\lambda) = \operatorname{rank}\left((A - \lambda I)^{k-1}\right) - \operatorname{rank}\left((A - \lambda I)^k\right).$$
    <2>2. The **exact number of Jordan blocks of size $k$** is the second difference (discrete second derivative):
        $$N_k(\lambda) = N_{\ge k}(\lambda) - N_{\ge k+1}(\lambda) = 2 d_k(\lambda) - d_{k-1}(\lambda) - d_{k+1}(\lambda)$$
        $$N_k(\lambda) = \operatorname{rank}\left((A - \lambda I)^{k-1}\right) - 2\operatorname{rank}\left((A - \lambda I)^k\right) + \operatorname{rank}\left((A - \lambda I)^{k+1}\right).$$

<1>6. Conclusion:
    The total number of blocks for $\lambda$ is $\operatorname{nullity}(A - \lambda I)$; the largest block size is the power in $m_A(x)$; and the number of blocks of size $k$ is $2d_k - d_{k-1} - d_{k+1}$. Q.E.D.
:::
