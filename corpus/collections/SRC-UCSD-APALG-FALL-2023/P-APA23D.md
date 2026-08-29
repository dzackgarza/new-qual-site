---
schema: qual/card@1
id: P-APA23D
kind: problem
title: Rayleigh quotient bounds; $p$-norm of a diagonal matrix; $\|aa^H\|_2$ and a block companion
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex entries, and $x^H$ denotes the Hermitian transpose of $x$.

(a) Consider any Hermitian $A \in M_n$ with eigenvalues ordered so that $\lambda_n(A) \le \cdots \le \lambda_2(A) \le \lambda_1(A)$.
Prove that:
$$\lambda_n(A) \le \frac{x^H A x}{x^H x} \le \lambda_1(A) \quad \text{for all nonzero } x \in \mathbb{C}^n.$$

(b) Suppose that $D \in M_n$ with $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$.
Prove that for all $1 \le p \le \infty$, the induced operator $p$-norm of $D$ is given by $\|D\|_p = \max_{1 \le i \le n} |d_i|$.

(c) Given $a \in \mathbb{C}^n$, find $\|A\|_2$ for the matrices:
$$A_1 = a a^H \quad \text{and} \quad A_2 = \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix}.$$
:::

::: solution
**Goal:** Prove the Rayleigh quotient inequalities for Hermitian matrices, compute induced $p$-norms of diagonal matrices, and evaluate the spectral 2-norm of rank-one and symmetric block companion matrices.

<1>1. Part (a): Rayleigh Quotient Bounds for Hermitian Matrices:
    *Proof:*
    <2>1. By the **Spectral Theorem**, there exists an orthonormal eigenbasis $\{u_1, u_2, \dots, u_n\}$ of $\mathbb{C}^n$ such that $A u_i = \lambda_i(A) u_i$ and $u_i^H u_j = \delta_{ij}$.
    <2>2. Write any non-zero vector $x \in \mathbb{C}^n \setminus \{0\}$ as $x = \sum_{i=1}^n c_i u_i$ with $c_i = u_i^H x \in \mathbb{C}$.
    <2>3. Then:
        $$x^H x = \sum_{i=1}^n |c_i|^2 > 0, \qquad x^H A x = \sum_{i=1}^n \lambda_i(A) |c_i|^2.$$
    <2>4. Since $\lambda_n(A) \le \lambda_i(A) \le \lambda_1(A)$ for each $i \in \{1, \dots, n\}$:
        $$\lambda_n(A) \sum_{i=1}^n |c_i|^2 \le \sum_{i=1}^n \lambda_i(A) |c_i|^2 \le \lambda_1(A) \sum_{i=1}^n |c_i|^2.$$
    <2>5. Dividing by $x^H x = \sum_{i=1}^n |c_i|^2$:
        $$\lambda_n(A) \le \frac{x^H A x}{x^H x} \le \lambda_1(A).$$

<1>2. Part (b): $p$-Norm of a Diagonal Matrix $\|D\|_p = \max_i |d_i|$:
    *Proof:*
    <2>1. Let $M = \max_{1 \le i \le n} |d_i|$.
    <2>2. For any $x \in \mathbb{C}^n$ and $1 \le p < \infty$:
        $$\|D x\|_p^p = \sum_{i=1}^n |d_i x_i|^p = \sum_{i=1}^n |d_i|^p |x_i|^p \le \sum_{i=1}^n M^p |x_i|^p = M^p \sum_{i=1}^n |x_i|^p = M^p \|x\|_p^p.$$
        Taking $p$-th roots gives $\|D x\|_p \le M \|x\|_p$, so $\|D\|_p \le M$.
        (For $p = \infty$: $\|D x\|_\infty = \max_i |d_i x_i| \le M \max_i |x_i| = M \|x\|_\infty$).
    <2>3. To show attainment, choose index $k$ such that $|d_k| = M = \max_i |d_i|$.
    <2>4. Let $e_k = (0, \dots, 0, 1, 0, \dots, 0)^T$ be the $k$-th standard basis vector.
    <2>5. $\|e_k\|_p = 1$, and $D e_k = d_k e_k$, so $\|D e_k\|_p = |d_k| \|e_k\|_p = M$.
    <2>6. Therefore:
        $$\|D\|_p = \sup_{x \ne 0} \frac{\|D x\|_p}{\|x\|_p} = M = \max_{1 \le i \le n} |d_i|.$$

<1>3. Part (c): Evaluation of $\|A\|_2$ (Spectral Norm):
    *Proof:*
    <2>1. The matrix 2-norm is the largest singular value: $\|A\|_2 = \sigma_1(A) = \sqrt{\lambda_1(A^H A)}$.
    <2>2. **For $A_1 = a a^H$ (where $a \in \mathbb{C}^n$):**
        - If $a = 0$, $\|A_1\|_2 = 0 = \|a\|_2^2$.
        - If $a \ne 0$, $A_1 a = (a a^H) a = a (a^H a) = \|a\|_2^2 a$, so $a$ is an eigenvector with eigenvalue $\|a\|_2^2$.
        - For any $v \perp a$, $A_1 v = a (a^H v) = 0$.
        - Since $A_1$ is Hermitian and rank 1, its eigenvalues are $\|a\|_2^2$ (multiplicity 1) and $0$ (multiplicity $n - 1$).
        - Thus:
          $$\|A_1\|_2 = \lambda_1(A_1) = \|a\|_2^2.$$
    <2>3. **For $A_2 = \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} \in M_{n+1}(\mathbb{C})$:**
        - We compute $A_2^H A_2 = A_2^2$ (since $A_2$ is Hermitian):
          $$A_2^2 = \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} = \begin{pmatrix} a^H a & 0 \\ 0 & a a^H \end{pmatrix} = \begin{pmatrix} \|a\|_2^2 & 0 \\ 0 & a a^H \end{pmatrix}.$$
        - The eigenvalues of the block diagonal matrix $A_2^2$ are:
          - From top block $1 \times 1$: $\|a\|_2^2$.
          - From bottom block $n \times n$: eigenvalues of $a a^H$, which are $\|a\|_2^2$ and $0$.
        - Thus the largest eigenvalue of $A_2^2$ is $\lambda_{\max}(A_2^2) = \|a\|_2^2$.
        - Taking the square root gives the spectral norm:
          $$\|A_2\|_2 = \sqrt{\lambda_{\max}(A_2^2)} = \sqrt{\|a\|_2^2} = \|a\|_2.$$

<1>4. Conclusion:
    The Rayleigh quotient is bounded by $\lambda_n \le \frac{x^HAx}{x^Hx} \le \lambda_1$, $\|D\|_p = \max_i |d_i|$, $\|a a^H\|_2 = \|a\|_2^2$, and $\left\| \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} \right\|_2 = \|a\|_2$. Q.E.D.
:::
