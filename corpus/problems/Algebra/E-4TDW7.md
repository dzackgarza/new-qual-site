---
schema: qual/card@1
id: E-4TDW7
kind: problem
title: $K(a)=K(a^{2})$ when $a$ is algebraic of odd degree over $K$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $F/K$ be a field extension, and let $a \in F$ be algebraic over $K$ of odd degree $[K(a) : K] = 2m + 1$.
Prove that $a^2$ is algebraic over $K$, that $[K(a^2) : K]$ is odd, and that $K(a) = K(a^2)$.
:::

::: solution
**Goal:** Prove that $K(a) = K(a^2)$ and $[K(a^2) : K]$ is odd when $[K(a) : K]$ is odd.

<1>1. Subfield Inclusion and Tower Law:
    *Proof:*
    <2>1. Since $a^2 = a \cdot a \in K(a)$, the field $K(a^2)$ is an intermediate field in the extension $K(a)/K$:
        $$K \subseteq K(a^2) \subseteq K(a).$$
    <2>2. Since $a$ is algebraic over $K$, $a^2 \in K(a)$ is also algebraic over $K$.
    <2>3. By the Tower Law for field degrees:
        $$[K(a) : K] = [K(a) : K(a^2)] \cdot [K(a^2) : K].$$
    <2>4. Let $n = [K(a) : K]$. By assumption, $n$ is an **odd integer**.

<1>2. Degree of the step $[K(a) : K(a^2)]$:
    *Proof:*
    <2>1. Consider the polynomial $g(x) = x^2 - a^2 \in K(a^2)[x]$.
    <2>2. The element $a$ satisfies $g(a) = a^2 - a^2 = 0$, so $a$ is a root of a quadratic polynomial with coefficients in $K(a^2)$.
    <2>3. Therefore, the minimal polynomial of $a$ over $K(a^2)$ divides $x^2 - a^2$.
    <2>4. Thus:
        $$[K(a) : K(a^2)] \le \deg(g) = 2.$$
    <2>5. Consequently, $[K(a) : K(a^2)] \in \{1, 2\}$.

<1>3. Divisibility and Conclusion $K(a) = K(a^2)$:
    *Proof:*
    <2>1. From the Tower Law:
        $$[K(a) : K(a^2)] \text{ divides } [K(a) : K] = n.$$
    <2>2. Since $n$ is odd, $n$ has no even divisors.
    <2>3. Therefore, $[K(a) : K(a^2)]$ cannot be 2.
    <2>4. This forces:
        $$[K(a) : K(a^2)] = 1.$$
    <2>5. A field extension of degree 1 is an equality of fields, so:
        $$K(a) = K(a^2).$$
    <2>6. Substituting $[K(a) : K(a^2)] = 1$ back into the Tower Law gives:
        $$[K(a^2) : K] = [K(a) : K] = n,$$
        which is odd.

<1>4. Conclusion:
    $a^2$ is algebraic of odd degree $[K(a^2) : K] = [K(a) : K]$, and $K(a) = K(a^2)$. Q.E.D.
:::
