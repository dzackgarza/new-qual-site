---
schema: qual/card@1
id: E-SS6.EX-1
kind: exercise
title: "SS 6.1: Gauss's limit formula for the Gamma function"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
1. Prove that

$$
\Gamma (s) = \lim _ {n \to \infty} \frac {n ^ {s} n !}{s (s + 1) \cdots (s + n)}
$$

whenever $s \neq 0 , - 1 , - 2 , . . .$

[Hint: Use the product formula for $1 / \Gamma$ , and the definition of the Euler constant γ.]
:::

::: solution
**Goal:** Prove
$$
\Gamma (s)=\lim_{n\to\infty}\frac{n^s n!}{s(s+1)\cdots(s+n)}.
$$

<1> Use the Euler--Weierstrass product for $1/\Gamma$.
    *Proof:*
    <2>1. For $s\notin\{0,-1,-2,\ldots\}$,
        $$\frac1{\Gamma(s)}=s\,e^{\gamma s}\prod_{k=1}^\infty\left(1+\frac{s}{k}\right)e^{-s/k},$$
        where $\gamma=\lim_{n\to\infty}(H_n-\log n)$ and $H_n=\sum_{k=1}^n \frac1k$.
    <2>2. Let
        $$A_n:=\prod_{k=1}^n\left(1+\frac{s}{k}\right)e^{-s/k}.$$
    <2>3. Then
        $$
        A_n = \frac{s(s+1)\cdots(s+n)}{s\,n!}\,e^{- \sum_{k=1}^n s/k}
        = \frac{s(s+1)\cdots(s+n)}{s\,n!}\,e^{-sH_n}.
        $$

<1> Isolate the target expression.
    *Proof:*
    <2>1. Multiply the previous identity by $e^{s\gamma_n}$ with $\gamma_n=H_n-\log n$:
        $$
        e^{s\gamma_n}A_n
        =\frac{s(s+1)\cdots(s+n)}{n^s}.
        $$
    <2>2. The right side is exactly the reciprocal quantity in the claim.

<1> Pass to the limit.
    *Proof:*
    <2>1. By the product formula, $A_n\to e^{-\gamma s}/(s\Gamma(s))$.
    <2>2. Since $\gamma_n\to\gamma$,
        $$\lim_{n\to\infty}e^{s\gamma_n}A_n=e^{s\gamma}\cdot\frac{e^{-\gamma s}}{s\Gamma(s)}=\frac1{s\Gamma(s)}.$$
    <2>3. Therefore
        $$\lim_{n\to\infty}\frac{s(s+1)\cdots(s+n)}{n^s}=\frac1{\Gamma(s)}.$$
    <2>4. Invert both sides:
        $$\Gamma(s)=\lim_{n\to\infty}\frac{n^s n!}{s(s+1)\cdots(s+n)}.$$

Authored by **Codex 5.3 Spark Extra High**.
:::
