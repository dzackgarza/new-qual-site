---
schema: qual/card@1
id: P-MUABR
kind: problem
title: $L/F$ is algebraic if $K/F$ and $L/K$ are algebraic
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $F \subseteq K \subseteq L$ be a tower of field extensions. Prove that if $K/F$ is algebraic and $L/K$ is algebraic, then $L/F$ is algebraic.
:::

::: solution
**Goal:** Prove the transitivity of algebraic field extensions: $L/K$ algebraic and $K/F$ algebraic $\implies L/F$ algebraic.

<1>1. Target and Element Selection:
    *Proof:*
    <2>1. Let $\alpha \in L$ be an arbitrary element.
    <2>2. We must show that $\alpha$ is algebraic over $F$.

<1>2. Finite generation of intermediate extension:
    *Proof:*
    <2>1. Since $L/K$ is algebraic, $\alpha$ is algebraic over $K$.
    <2>2. Thus there exists a non-zero monic polynomial $p(x) \in K[x]$ such that $p(\alpha) = 0$.
    <2>3. Let $p(x) = x^n + c_{n-1} x^{n-1} + \cdots + c_1 x + c_0$ where the coefficients $c_0, c_1, \dots, c_{n-1} \in K$.
    <2>4. Consider the subfield $E = F(c_0, c_1, \dots, c_{n-1}) \subseteq K$ obtained by adjoining these finitely many coefficients to $F$.

<1>3. Tower Degree and Finite Extension:
    *Proof:*
    <2>1. Since $K/F$ is algebraic, each coefficient $c_i$ is algebraic over $F$.
    <2>2. The extension $E = F(c_0, c_1, \dots, c_{n-1})$ is generated over $F$ by finitely many algebraic elements, so $[E : F] < \infty$ is a **finite extension**.
    <2>3. The polynomial $p(x)$ has all its coefficients in $E$, so $p(x) \in E[x]$ and $p(\alpha) = 0$.
    <2>4. Therefore, $\alpha$ is algebraic over $E$, and the simple extension $E(\alpha)/E$ has finite degree:
        $$[E(\alpha) : E] \le \deg(p) = n < \infty.$$
    <2>5. By the Tower Law for field degrees:
        $$[E(\alpha) : F] = [E(\alpha) : E] \cdot [E : F] < \infty.$$
    <2>6. Thus $E(\alpha)$ is a finite field extension of $F$.

<1>4. Finite extensions are algebraic:
    *Proof:*
    <2>1. Since $[E(\alpha) : F] = m < \infty$, the $m+1$ elements $\{1, \alpha, \alpha^2, \dots, \alpha^m\}$ in $E(\alpha)$ must be linearly dependent over $F$.
    <2>2. Thus there exist $a_0, a_1, \dots, a_m \in F$, not all zero, such that:
        $$a_m \alpha^m + \cdots + a_1 \alpha + a_0 = 0.$$
    <2>3. This shows that $\alpha$ is algebraic over $F$.
    <2>4. Since $\alpha \in L$ was arbitrary, every element of $L$ is algebraic over $F$.

<1>5. Conclusion:
    $L/F$ is an algebraic extension. Q.E.D.
:::
