---
schema: qual/card@1
id: P-APAF21C
kind: problem
title: Square root and modulus; singular values; PSD characterization; similarity of $|A|$ and $|A^H|$
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Positive Definite Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(a) Define $A^{1/2}$ for a positive semidefinite matrix $A \in M_n(\mathbb{C})$.
(b) Define $|A|$ for any matrix $A \in M_{m,n}(\mathbb{C})$.
(c) Prove that the eigenvalues of $|A|$ are the singular values of $A$.
(d) Prove that a square matrix $A \in M_n(\mathbb{C})$ is positive semidefinite if and only if $|A| = A$.
(e) Prove that $|A|$ and $|A^H|$ have the same non-zero eigenvalues and are similar up to embedding/direct sum with zero blocks.
:::

::: solution
**Goal:** Define positive semidefinite square roots and moduli of matrices, characterize their singular values, PSD fixed points, and spectra.

<1>1. Part (a): Definition of $A^{1/2}$ for $A \ge 0$:
    *Proof:*
    <2>1. Let $A \in M_n(\mathbb{C})$ be a positive semidefinite (PSD) matrix ($A = A^H$ and $\langle A v, v \rangle \ge 0$ for all $v$).
    <2>2. By the **Spectral Theorem for Hermitian matrices**, there exists a unitary matrix $U \in U(n)$ such that:
        $$A = U \Lambda U^H = U \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n) U^H$$
        where all eigenvalues $\lambda_i \ge 0$ are non-negative real numbers.
    <2>3. The unique positive semidefinite square root $A^{1/2}$ is defined by:
        $$A^{1/2} \coloneqq U \operatorname{diag}(\sqrt{\lambda_1}, \sqrt{\lambda_2}, \dots, \sqrt{\lambda_n}) U^H.$$
    <2>4. It satisfies $(A^{1/2})^2 = A$ and $A^{1/2} \ge 0$.

<1>2. Part (b): Definition of the Modulus $|A|$ for $A \in M_{m,n}(\mathbb{C})$:
    *Proof:*
    <2>1. For any matrix $A \in M_{m,n}(\mathbb{C})$, the $n \times n$ matrix $A^H A \in M_n(\mathbb{C})$ is Hermitian and positive semidefinite:
        $$(A^H A)^H = A^H A, \qquad v^H (A^H A) v = (A v)^H (A v) = \|A v\|^2 \ge 0.$$
    <2>2. The **modulus** (or absolute value) $|A| \in M_n(\mathbb{C})$ is defined as the unique PSD square root:
        $$|A| \coloneqq (A^H A)^{1/2}.$$

<1>3. Part (c): Eigenvalues of $|A|$ are the Singular Values of $A$:
    *Proof:*
    <2>1. By definition, the **singular values** $\sigma_i(A)$ of $A$ are the non-negative square roots of the eigenvalues of $A^H A$:
        $$\sigma_i(A) \coloneqq \sqrt{\lambda_i(A^H A)}.$$
    <2>2. By definition of $A^{1/2}$ in Part (a), the eigenvalues of $|A| = (A^H A)^{1/2}$ are precisely $\sqrt{\lambda_i(A^H A)}$.
    <2>3. Therefore, the eigenvalues of $|A|$ are identically the singular values $\sigma_1(A), \dots, \sigma_n(A)$.

<1>4. Part (d): $A \ge 0 \iff |A| = A$:
    *Proof:*
    <2>1. **$(\implies)$:** Suppose $A \ge 0$.
        - Then $A$ is Hermitian, so $A^H = A$.
        - Thus $A^H A = A^2$.
        - Since $A \ge 0$ is a positive semidefinite matrix whose square is $A^2$, by the uniqueness of the PSD square root:
          $$|A| = (A^H A)^{1/2} = (A^2)^{1/2} = A.$$
    <2>2. **$(\impliedby)$:** Suppose $|A| = A$.
        - By definition, $|A| = (A^H A)^{1/2}$ is positive semidefinite ($|A| \ge 0$).
        - Since $A = |A|$, $A$ must be positive semidefinite ($A \ge 0$).

<1>5. Part (e): Moduli $|A| = (A^H A)^{1/2}$ and $|A^H| = (A A^H)^{1/2}$:
    *Proof:*
    <2>1. Let $A = U \Sigma V^H$ be the Singular Value Decomposition (SVD) of $A \in M_{m,n}(\mathbb{C})$, where $U \in U(m), V \in U(n)$, and $\Sigma \in M_{m,n}(\mathbb{R})$.
    <2>2. Then:
        $$|A| = (V \Sigma^T U^H U \Sigma V^H)^{1/2} = (V \Sigma^T \Sigma V^H)^{1/2} = V (\Sigma^T \Sigma)^{1/2} V^H,$$
        $$|A^H| = (U \Sigma V^H V \Sigma^T U^H)^{1/2} = (U \Sigma \Sigma^T U^H)^{1/2} = U (\Sigma \Sigma^T)^{1/2} U^H.$$
    <2>3. The matrices $A^H A$ and $A A^H$ share the exact same non-zero eigenvalues $\sigma_i^2 > 0$ with identical multiplicities.
    <2>4. For square matrices $m = n$, $|A|$ and $|A^H|$ are both Hermitian matrices with identical eigenvalues (the singular values of $A$), so they are **unitarily similar**:
        $$|A^H| = W |A| W^H \quad \text{for } W = U V^H \in U(n).$$

<1>6. Conclusion:
    $A^{1/2}$ is the unique PSD square root, $|A| = (A^HA)^{1/2}$ has eigenvalues $\sigma_i(A)$, fixes PSD matrices $|A|=A$, and $|A| \sim |A^H|$ via SVD. Q.E.D.
:::
