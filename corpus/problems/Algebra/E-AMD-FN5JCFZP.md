---
schema: qual/card@1
id: E-AMD-FN5JCFZP
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
  date: 2026-08-29
---

::: {.exercise}
Prove the Cayley-Hamilton theorem.
:::

::: solution
**Goal:** Prove the Cayley-Hamilton Theorem: every square matrix $A \in M_n(R)$ over a commutative ring $R$ satisfies its own characteristic equation, $p(A) = 0$, where $p(t) = \det(t I_n - A)$.

<1>1. Adjugate matrix identity in $M_n(R[t])$:
    *Proof:*
    <2>1. Let $M(t) = t I_n - A \in M_n(R[t])$.
    <2>2. The characteristic polynomial is $p(t) = \det(M(t)) = \sum_{k=0}^n c_k t^k \in R[t]$.
    <2>3. By the fundamental adjugate property for matrices over any commutative ring, $M(t) \operatorname{adj}(M(t)) = \det(M(t)) I_n$.
    <2>4. Thus:
        $$(t I_n - A) \operatorname{adj}(t I_n - A) = p(t) I_n.$$

<1>2. Matrix coefficient expansion:
    *Proof:*
    <2>1. Each entry of $\operatorname{adj}(t I_n - A)$ is an $(n-1) \times (n-1)$ cofactor of $t I_n - A$, which is a polynomial in $t$ of degree at most $n-1$.
    <2>2. Therefore, $\operatorname{adj}(t I_n - A)$ can be expanded as a polynomial in $t$ with matrix coefficients $B_i \in M_n(R)$:
        $$\operatorname{adj}(t I_n - A) = \sum_{i=0}^{n-1} B_i t^i = B_0 + B_1 t + \dots + B_{n-1} t^{n-1}.$$

<1>3. Coefficient matching and telescoping sum:
    *Proof:*
    <2>1. Substituting the expansion into the adjugate identity:
        $$(t I_n - A) \left( \sum_{i=0}^{n-1} B_i t^i \right) = \sum_{k=0}^n c_k I_n t^k.$$
    <2>2. Expanding the left side:
        $$\sum_{i=0}^{n-1} B_i t^{i+1} - \sum_{i=0}^{n-1} A B_i t^i = c_0 I_n + c_1 I_n t + \dots + c_n I_n t^n.$$
    <2>3. Equating matrix coefficients of powers $t^k$:
        $$\begin{aligned}
        -A B_0 &= c_0 I_n, \\
        B_0 - A B_1 &= c_1 I_n, \\
        B_1 - A B_2 &= c_2 I_n, \\
        &\;\;\vdots \\
        B_{n-2} - A B_{n-1} &= c_{n-1} I_n, \\
        B_{n-1} &= c_n I_n.
        \end{aligned}$$
    <2>4. Multiplying the $k$-th equation on the left by $A^k$:
        $$\begin{aligned}
        -A B_0 &= c_0 I_n, \\
        A B_0 - A^2 B_1 &= c_1 A, \\
        A^2 B_1 - A^3 B_2 &= c_2 A^2, \\
        &\;\;\vdots \\
        A^{n-1} B_{n-2} - A^n B_{n-1} &= c_{n-1} A^{n-1}, \\
        A^n B_{n-1} &= c_n A^n.
        \end{aligned}$$
    <2>5. Summing all $n+1$ equations telescopes the left-hand side to $0$:
        $$0 = \sum_{k=0}^n c_k A^k = p(A).$$

<1>4. Conclusion:
    $p(A) = 0$. Q.E.D.
:::
