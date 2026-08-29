---
schema: qual/card@1
id: P-HJBTY
kind: problem
title: Rational canonical forms of $3\times 3$ matrices over $\QQ$ annihilated by
  $(x^2+2)(x-1)^3$
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Minimal and Characteristic Polynomials
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What $3 \times 3$ matrices over $\mathbb{Q}$ (up to similarity) satisfy $f(A) = 0$, where $f(x) = (x^2 + 2)(x - 1)^3$?
List all possible invariant factor lists and rational canonical forms.
:::

::: solution
**Goal:** Classify all similarity classes (Rational Canonical Forms) of $3 \times 3$ matrices $A \in M_3(\mathbb{Q})$ such that the minimal polynomial $\mu_A(x)$ divides $f(x) = (x^2 + 2)(x - 1)^3$.

<1>1. Algebraic Constraints on Invariant Factors over $\mathbb{Q}$:
    *Proof:*
    <2>1. The invariant factors $d_1(x) \mid d_2(x) \mid \cdots \mid d_k(x)$ are monic polynomials in $\mathbb{Q}[x]$ such that:
        - The product $d_1(x) \cdots d_k(x) = \chi_A(x)$ is the characteristic polynomial of degree 3.
        - The largest invariant factor $d_k(x) = \mu_A(x)$ is the minimal polynomial.
        - $\mu_A(x)$ must divide $f(x) = (x^2 + 2)(x - 1)^3$.
    <2>2. Note that $x^2 + 2$ is irreducible over $\mathbb{Q}$ (no rational roots, degree 2).
    <2>3. The irreducible factors of $f(x)$ in $\mathbb{Q}[x]$ are $(x^2 + 2)$ and $(x - 1)$.
    <2>4. The possible characteristic polynomials $\chi_A(x)$ of degree 3 factoring over $\mathbb{Q}$ are:
        - **Type I:** $\chi_A(x) = (x^2 + 2)(x - 1) = x^3 - x^2 + 2x - 2$.
        - **Type II:** $\chi_A(x) = (x - 1)^3 = x^3 - 3x^2 + 3x - 1$.

<1>2. Case 1: $\chi_A(x) = (x^2 + 2)(x - 1)$:
    *Proof:*
    <2>1. Since $x^2 + 2$ and $x - 1$ are coprime irreducible factors, $\mu_A(x)$ must contain both factors, so $\mu_A(x) = (x^2 + 2)(x - 1) = \chi_A(x)$.
    <2>2. Thus there is only 1 invariant factor: $d_1(x) = x^3 - x^2 + 2x - 2$.
    <2>3. **Rational Canonical Form 1:**
        $$C(x^3 - x^2 + 2x - 2) = \begin{pmatrix} 0 & 0 & 2 \\ 1 & 0 & -2 \\ 0 & 1 & 1 \end{pmatrix} \quad \text{or in block form } \begin{pmatrix} 0 & -2 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$

<1>3. Case 2: $\chi_A(x) = (x - 1)^3$:
    *Proof:*
    <2>1. The invariant factors must be powers of $(x - 1)$ whose degrees sum to 3 and divide the next.
    <2>2. **Subcase 2A: $\mu_A(x) = x - 1$:**
        - Invariant factors: $d_1(x) = x - 1, \, d_2(x) = x - 1, \, d_3(x) = x - 1$.
        - **Rational Canonical Form 2:**
            $$A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3.$$
    <2>3. **Subcase 2B: $\mu_A(x) = (x - 1)^2 = x^2 - 2x + 1$:**
        - Invariant factors: $d_1(x) = x - 1, \, d_2(x) = x^2 - 2x + 1$.
        - **Rational Canonical Form 3:**
            $$\operatorname{diag}(C(x-1), C(x^2-2x+1)) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 2 \end{pmatrix}.$$
    <2>4. **Subcase 2C: $\mu_A(x) = (x - 1)^3 = x^3 - 3x^2 + 3x - 1$:**
        - Invariant factor: $d_1(x) = x^3 - 3x^2 + 3x - 1$.
        - **Rational Canonical Form 4:**
            $$C(x^3 - 3x^2 + 3x - 1) = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & -3 \\ 0 & 1 & 3 \end{pmatrix}.$$

<1>4. Summary Table of Similarity Classes:
    $$\begin{array}{|c|c|c|c|}
    \hline
    \text{No.} & \text{Invariant Factors} & \mu_A(x) & \text{Rational Canonical Form} \\
    \hline
    1 & x^3 - x^2 + 2x - 2 & (x^2+2)(x-1) & \begin{pmatrix} 0 & 0 & 2 \\ 1 & 0 & -2 \\ 0 & 1 & 1 \end{pmatrix} \\
    2 & x-1, x-1, x-1 & x-1 & \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\
    3 & x-1, x^2-2x+1 & (x-1)^2 & \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 2 \end{pmatrix} \\
    4 & x^3 - 3x^2 + 3x - 1 & (x-1)^3 & \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & -3 \\ 0 & 1 & 3 \end{pmatrix} \\
    \hline
    \end{array}$$

<1>5. Conclusion:
    There are exactly 4 similarity classes over $\mathbb{Q}$. Q.E.D.
:::
