---
schema: qual/card@1
id: E-AMD-4WRRHZMI
kind: exercise
title: Polynomial rings over integral domains are integral domains
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Polynomials
  - Rings
relations: []
review: draft
solved: true
---

::: {.exercise}
Prove that if $R$ is an integral domain, then $R[t]$ is again an integral domain.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $R$ be an integral domain (a commutative ring with identity $1 \neq 0$ and no non-zero zero divisors).
Then $R[t]$ is also a commutative ring with identity $1 \in R[t]$ ($1 \neq 0$).

To prove that $R[t]$ is an integral domain, let $f(t), g(t) \in R[t]$ be two non-zero polynomials.
We must show that $f(t)g(t) \neq 0$.

1. **Expressing polynomials in terms of leading coefficients:** Since $f(t) \neq 0$ and $g(t) \neq 0$, we can write:
   $$
   f(t) = a_n t^n + a_{n-1} t^{n-1} + \cdots + a_0, \qquad \text{with } a_n \neq 0 \text{ and } n = \deg(f) \geq 0,
   $$
   $$
   g(t) = b_m t^m + b_{m-1} t^{m-1} + \cdots + b_0, \qquad \text{with } b_m \neq 0 \text{ and } m = \deg(g) \geq 0.
   $$

2. **Computing the product $f(t)g(t)$:** The product polynomial is:
   $$
   f(t)g(t) = c_{n+m} t^{n+m} + c_{n+m-1} t^{n+m-1} + \cdots + c_0,
   $$
   where the leading coefficient of degree $n+m$ is:
   $$
   c_{n+m} = a_n b_m.
   $$

3. **Applying the integral domain property of $R$:** Since $R$ is an integral domain, and $a_n \neq 0$ and $b_m \neq 0$ in $R$, the product of these non-zero elements must be non-zero:
   $$
   c_{n+m} = a_n b_m \neq 0.
   $$

4. **Conclusion:** Since the coefficient of $t^{n+m}$ in $f(t)g(t)$ is non-zero, the polynomial $f(t)g(t)$ is not the zero polynomial:
   $$
   f(t)g(t) \neq 0, \qquad \text{and } \deg(fg) = \deg(f) + \deg(g).
   $$
   Therefore, $R[t]$ has no non-zero zero divisors, which proves that $R[t]$ is an integral domain.
:::
