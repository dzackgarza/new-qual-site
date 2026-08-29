---
schema: qual/card@1
id: P-YOLB7
kind: problem
title: Cayley-Hamilton theorem
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
State and prove the Cayley–Hamilton Theorem for an $n \times n$ matrix $A$ over a commutative ring $R$.
:::

::: solution
**Goal:** Prove the Cayley–Hamilton Theorem: if $\chi_A(t) = \det(t I_n - A)$ is the characteristic polynomial of $A \in M_n(R)$, then $\chi_A(A) = 0$.

<1>1. Setting and Classical Adjugate Formula:
    *Proof:*
    <2>1. Let $R$ be a commutative ring and $A \in M_n(R)$.
    <2>2. Consider the polynomial ring $R[t]$ and the matrix $M(t) = t I_n - A \in M_n(R[t])$.
    <2>3. The characteristic polynomial is $p(t) = \chi_A(t) = \det(t I_n - A) \in R[t]$, which expands as:
        $$p(t) = t^n + c_{n-1} t^{n-1} + \cdots + c_1 t + c_0 \quad (c_i \in R).$$
    <2>4. By Cramer's Rule / properties of the classical adjugate (adjugate matrix):
        $$M(t) \operatorname{adj}(M(t)) = \det(M(t)) I_n = p(t) I_n.$$

<1>2. Expansion of the Adjugate Matrix:
    *Proof:*
    <2>1. Each entry of the adjugate matrix $\operatorname{adj}(M(t))$ is an $(n-1) \times (n-1)$ cofactor determinant of entries linear in $t$.
    <2>2. Therefore, each entry is a polynomial in $R[t]$ of degree at most $n-1$.
    <2>3. We can write $\operatorname{adj}(M(t))$ as a polynomial in $t$ with matrix coefficients $B_k \in M_n(R)$:
        $$\operatorname{adj}(t I_n - A) = B_{n-1} t^{n-1} + B_{n-2} t^{n-2} + \cdots + B_1 t + B_0.$$

<1>3. Coefficient Matching and Telescoping Sum:
    *Proof:*
    <2>1. Substitute this expansion into $(t I_n - A) \operatorname{adj}(t I_n - A) = p(t) I_n$:
        $$(t I_n - A)(B_{n-1} t^{n-1} + B_{n-2} t^{n-2} + \cdots + B_0) = (t^n + c_{n-1} t^{n-1} + \cdots + c_0) I_n.$$
    <2>2. Expanding the left-hand side:
        $$B_{n-1} t^n + (B_{n-2} - A B_{n-1}) t^{n-1} + (B_{n-3} - A B_{n-2}) t^{n-2} + \cdots + (B_0 - A B_1) t - A B_0.$$
    <2>3. Equating matrix coefficients of like powers of $t$:
        $$\begin{aligned}
        t^n: &\quad B_{n-1} = I_n \\
        t^{n-1}: &\quad B_{n-2} - A B_{n-1} = c_{n-1} I_n \\
        t^{n-2}: &\quad B_{n-3} - A B_{n-2} = c_{n-2} I_n \\
        &\quad \vdots \\
        t^1: &\quad B_0 - A B_1 = c_1 I_n \\
        t^0: &\quad -A B_0 = c_0 I_n.
        \end{aligned}$$
    <2>4. Multiply the equation for $t^k$ on the left by $A^k$ for each $k \in \{0, 1, \dots, n\}$:
        $$\begin{aligned}
        A^n B_{n-1} &= A^n \\
        A^{n-1} B_{n-2} - A^n B_{n-1} &= c_{n-1} A^{n-1} \\
        A^{n-2} B_{n-3} - A^{n-1} B_{n-2} &= c_{n-2} A^{n-2} \\
        &\quad \vdots \\
        A B_0 - A^2 B_1 &= c_1 A \\
        -A B_0 &= c_0 I_n.
        \end{aligned}$$
    <2>5. Summing all $n+1$ equations, the left-hand side telescopes completely to $0$:
        $$\text{LHS} = 0.$$
    <2>6. The right-hand side sums to:
        $$\text{RHS} = A^n + c_{n-1} A^{n-1} + c_{n-2} A^{n-2} + \cdots + c_1 A + c_0 I_n = p(A) = \chi_A(A).$$
    <2>7. Therefore, $\chi_A(A) = 0$.

<1>4. Conclusion:
    Every square matrix satisfies its own characteristic polynomial: $\chi_A(A) = 0$. Q.E.D.
:::
