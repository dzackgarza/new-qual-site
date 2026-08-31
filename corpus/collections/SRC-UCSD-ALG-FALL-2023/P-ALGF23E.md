---
schema: qual/card@1
id: P-ALGF23E
kind: problem
title: "Jordan form of a matrix with minimal polynomial t^p - 1 over C and F_p"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Suppose $p$ is a prime number and the minimal polynomial of $a \in M_p(F)$ is $t^p - 1$.

(a) Find the Jordan form of $a$ if $F = \mathbb{C}$.
Justify your answer.

(b) Find the Jordan form of $a$ if $F = \mathbb{F}_p$.
Justify your answer.
:::

::: solution
**Goal:** Determine the Jordan canonical form of an operator $a \in M_p(F)$ whose minimal polynomial is $m_a(t) = t^p - 1$ over $F = \mathbb{C}$ and $F = \mathbb{F}_p$.

<1>1. Part (a): Jordan canonical form over $\mathbb{C}$.
    *Proof:*
    <2>1. In $\mathbb{C}[t]$, the polynomial $t^p - 1$ splits completely into $p$ distinct linear factors:
    $$t^p - 1 = \prod_{k=0}^{p-1} (t - \zeta_p^k), \qquad \zeta_p = e^{2\pi i / p}.$$
    <2>2. Since the minimal polynomial $m_a(t)$ has degree $p$, divides the characteristic polynomial $\chi_a(t)$ of degree $p$, and both polynomials are monic of degree $p$, we have
    $$\chi_a(t) = m_a(t) = \prod_{k=0}^{p-1} (t - \zeta_p^k).$$
    <2>3. Each root $\zeta_p^k$ is a root of multiplicity 1 in both $\chi_a(t)$ and $m_a(t)$.
    <2>4. The size of the largest Jordan block corresponding to an eigenvalue $\lambda$ equals its multiplicity in the minimal polynomial, which is 1 for every eigenvalue $\zeta_p^k$.
    <2>5. Thus every Jordan block has size 1, so the matrix $a$ is diagonalizable.
    <2>6. Up to permutation of diagonal blocks, the Jordan canonical form of $a$ over $\mathbb{C}$ is
    $$J(a) = \operatorname{diag}\left(1, \zeta_p, \zeta_p^2, \dots, \zeta_p^{p-1}\right) = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & \zeta_p & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \zeta_p^{p-1} \end{bmatrix}.$$

<1>2. Part (b): Jordan canonical form over $\mathbb{F}_p$.
    *Proof:*
    <2>1. In characteristic $p$, the Frobenius binomial theorem gives $(t - 1)^p = t^p - 1^p = t^p - 1$ in $\mathbb{F}_p[t]$.
    <2>2. Thus the minimal polynomial is $m_a(t) = (t - 1)^p$.
    <2>3. The only eigenvalue of $a$ in $\mathbb{F}_p$ (and in its algebraic closure) is $\lambda = 1$.
    <2>4. The size of the largest Jordan block corresponding to the eigenvalue 1 equals the exponent of $(t - 1)$ in the minimal polynomial, which is $p$.
    <2>5. Since $a \in M_p(\mathbb{F}_p)$ is a $p \times p$ matrix, the sum of all Jordan block sizes is $p$.
    <2>6. Therefore there is exactly one Jordan block of size $p$ corresponding to eigenvalue 1.
    <2>7. The Jordan canonical form of $a$ over $\mathbb{F}_p$ is the single $p \times p$ Jordan block
    $$J(a) = J_p(1) = \begin{bmatrix}
    1 & 1 & 0 & \cdots & 0 \\
    0 & 1 & 1 & \cdots & 0 \\
    0 & 0 & 1 & \ddots & 0 \\
    \vdots & \vdots & \vdots & \ddots & 1 \\
    0 & 0 & 0 & \cdots & 1
    \end{bmatrix} \in M_p(\mathbb{F}_p).$$

<1>3. Conclusion:
    *Proof:*
    Over $\mathbb{C}$, the Jordan form is the diagonal matrix of distinct $p$-th roots of unity. Over $\mathbb{F}_p$, the Jordan form is the single $p \times p$ Jordan block $J_p(1)$.
:::
