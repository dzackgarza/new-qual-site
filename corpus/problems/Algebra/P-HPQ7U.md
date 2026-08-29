---
schema: qual/card@1
id: P-HPQ7U
kind: problem
title: When $A^n\to 0$
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Matrices
  - Nilpotence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
When do the powers of a square complex matrix $A \in M_n(\mathbb{C})$ tend to zero ($\lim_{k \to \infty} A^k = 0$)?
:::

::: solution
**Goal:** Prove that $\lim_{k \to \infty} A^k = 0$ if and only if the spectral radius satisfies $\rho(A) < 1$ (every eigenvalue $\lambda \in \mathbb{C}$ of $A$ satisfies $|\lambda| < 1$).

<1>1. Reduction to Jordan Canonical Form:
    *Proof:*
    <2>1. Let $A \in M_n(\mathbb{C})$. There exists an invertible matrix $P \in \operatorname{GL}_n(\mathbb{C})$ such that $A = P J P^{-1}$, where $J = \operatorname{diag}(J_1, \dots, J_m)$ is the Jordan canonical form of $A$.
    <2>2. For every $k \ge 1$, $A^k = P J^k P^{-1}$.
    <2>3. Since matrix multiplication by constant matrices $P, P^{-1}$ is continuous:
        $$\lim_{k \to \infty} A^k = 0 \iff \lim_{k \to \infty} J^k = 0 \iff \lim_{k \to \infty} J_i^k = 0 \quad \text{for each Jordan block } J_i.$$

<1>2. Behavior of powers of a Jordan block $J_i$:
    *Proof:*
    <2>1. Let $J_i = \lambda I_d + N_d$ be a $d \times d$ Jordan block with eigenvalue $\lambda \in \mathbb{C}$, where $N_d$ is the standard nilpotent shift matrix ($N_d^d = 0$).
    <2>2. Since $\lambda I_d$ and $N_d$ commute, by the Binomial Theorem, for $k \ge d$:
        $$J_i^k = (\lambda I_d + N_d)^k = \sum_{j=0}^{d-1} \binom{k}{j} \lambda^{k-j} N_d^j = \begin{pmatrix} \lambda^k & \binom{k}{1}\lambda^{k-1} & \cdots & \binom{k}{d-1}\lambda^{k-d+1} \\ 0 & \lambda^k & \cdots & \binom{k}{d-2}\lambda^{k-d+2} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda^k \end{pmatrix}.$$
    <2>3. For each fixed $j \in \{0, 1, \dots, d-1\}$, consider the scalar sequence $c_j(k) = \binom{k}{j} \lambda^{k-j}$.

<1>3. Analysis of the limit as $k \to \infty$:
    *Proof:*
    <2>1. **If $|\lambda| < 1$:**
        - Write $|\lambda| = 1 - \varepsilon$ for $\varepsilon > 0$.
        - The polynomial growth $\binom{k}{j} \sim \frac{k^j}{j!}$ is strictly dominated by the exponential decay $|\lambda|^{k-j} = (1-\varepsilon)^{k-j}$.
        - By standard calculus / ratio test, $\lim_{k \to \infty} k^j |\lambda|^k = 0$ for every fixed $j \ge 0$.
        - Thus every entry of $J_i^k$ converges to 0 as $k \to \infty$, so $\lim_{k \to \infty} J_i^k = 0$.
    <2>2. **If $|\lambda| \ge 1$:**
        - The diagonal entries of $J_i^k$ are $\lambda^k$.
        - If $|\lambda| > 1$, $|\lambda|^k \to \infty \ne 0$.
        - If $|\lambda| = 1$, $|\lambda^k| = 1 \ne 0$, so $\lambda^k$ does not tend to 0.
        - In either case, $\lim_{k \to \infty} J_i^k \ne 0$.

<1>4. Characterization:
    *Proof:*
    <2>1. All Jordan blocks satisfy $\lim_{k \to \infty} J_i^k = 0$ if and only if every eigenvalue $\lambda$ of $A$ satisfies $|\lambda| < 1$.
    <2>2. The **spectral radius** is defined as $\rho(A) = \max \{|\lambda| \mid \lambda \in \operatorname{spec}(A)\}$.
    <2>3. Thus $\lim_{k \to \infty} A^k = 0 \iff \rho(A) < 1$.

<1>5. Conclusion:
    The powers $A^k \to 0$ as $k \to \infty$ if and only if all eigenvalues of $A$ have absolute value strictly less than 1 ($\rho(A) < 1$). Q.E.D.
:::
