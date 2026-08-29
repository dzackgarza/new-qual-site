---
schema: qual/card@1
id: P-AA27R
kind: problem
title: Irreducibility of $(x^p-1)/(x-1)$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Roots of Unity
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Why is $\Phi_p(x) = \frac{x^p - 1}{x - 1} = x^{p-1} + x^{p-2} + \cdots + x + 1$ irreducible over $\mathbb{Q}$ for $p$ prime?
:::

::: solution
**Goal:** Prove the irreducibility of the $p$-th cyclotomic polynomial $\Phi_p(x)$ over $\mathbb{Q}$ using Eisenstein's criterion on $\Phi_p(y+1)$.

<1>1. Algebraic transformation via substitution $x = y + 1$:
    *Proof:*
    <2>1. Consider the polynomial $g(y) = \Phi_p(y+1) \in \mathbb{Z}[y]$.
    <2>2. Using the binomial expansion for $(y+1)^p$:
        $$g(y) = \frac{(y+1)^p - 1}{(y+1) - 1} = \frac{1}{y} \left( \sum_{k=0}^p \binom{p}{k} y^k - 1 \right) = \frac{1}{y} \sum_{k=1}^p \binom{p}{k} y^k = \sum_{k=1}^p \binom{p}{k} y^{k-1}.$$
    <2>3. Expanding the terms explicitly:
        $$g(y) = y^{p-1} + \binom{p}{p-1} y^{p-2} + \cdots + \binom{p}{2} y + \binom{p}{1} = y^{p-1} + p y^{p-2} + \binom{p}{p-2} y^{p-3} + \cdots + \binom{p}{2} y + p.$$

<1>2. Application of Eisenstein's Criterion:
    *Proof:*
    <2>1. Let $g(y) = a_{p-1} y^{p-1} + a_{p-2} y^{p-2} + \cdots + a_1 y + a_0$, where $a_k = \binom{p}{k+1}$ for $0 \le k \le p-2$ and $a_{p-1} = 1$.
    <2>2. **Leading coefficient:** $a_{p-1} = 1$, which is not divisible by $p$.
    <2>3. **Intermediate and constant coefficients:** For each $k \in \{0, 1, \dots, p-2\}$, the coefficient is $a_k = \binom{p}{k+1}$ with $1 \le k+1 \le p-1$.
        Since $\binom{p}{m} = \frac{p!}{m!(p-m)!}$ and $p$ is prime with $1 \le m \le p-1$, $p$ divides the numerator $p!$ but not the denominator $m!(p-m)!$.
        Therefore, $p \mid a_k$ for all $k \in \{0, 1, \dots, p-2\}$.
    <2>4. **Constant term divisibility by $p^2$:** The constant term is $a_0 = \binom{p}{1} = p$.
        Since $p^2 \nmid p$, we have $p^2 \nmid a_0$.
    <2>5. By Eisenstein's Criterion at the prime $p$, the polynomial $g(y)$ is irreducible in $\mathbb{Z}[y]$, and by Gauss's Lemma, irreducible in $\mathbb{Q}[y]$.

<1>3. Irreducibility of $\Phi_p(x)$:
    *Proof:*
    <2>1. If $\Phi_p(x)$ were reducible over $\mathbb{Q}$, say $\Phi_p(x) = h_1(x) h_2(x)$ with $\deg(h_1), \deg(h_2) \ge 1$, then:
        $$g(y) = \Phi_p(y+1) = h_1(y+1) h_2(y+1)$$
        would be a non-trivial factorization of $g(y)$ over $\mathbb{Q}$.
    <2>2. This contradicts the irreducibility of $g(y)$.
    <2>3. Thus $\Phi_p(x) = \frac{x^p-1}{x-1}$ is irreducible over $\mathbb{Q}$.

<1>4. Conclusion:
    $\Phi_p(x)$ is irreducible over $\mathbb{Q}$ for every prime $p$. Q.E.D.
:::
