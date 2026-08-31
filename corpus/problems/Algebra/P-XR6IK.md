---
schema: qual/card@1
id: P-XR6IK
kind: problem
title: An irreducible polynomial of degree $p$ over $\FF_p$ for each prime $p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
For each prime $p$, give an explicit polynomial of degree $p$ that is irreducible over the finite field $\mathbb{F}_p$, constructed in a uniform way across all primes $p$.
Prove that your polynomial is irreducible over $\mathbb{F}_p$.
:::

::: solution
**Goal:** Prove that the Artin-Schreier polynomial $f(x) = x^p - x - 1 \in \mathbb{F}_p[x]$ is irreducible of degree $p$ over $\mathbb{F}_p$ for every prime $p$.

<1>1. Selection of the Uniform Family:
    *Proof:*
    <2>1. For any prime $p$, consider the **Artin-Schreier polynomial**:
        $$f(x) \coloneqq x^p - x - 1 \in \mathbb{F}_p[x].$$
    <2>2. The degree of $f(x)$ is $\deg(f) = p$: the leading term is $x^p$, whose coefficient is $1 \neq 0$ in $\mathbb{F}_p$.

<1>2. Properties of the Roots of $f(x)$:
    *Proof:*
    <2>1. Let $\alpha$ be a root of $f(x)$ in an algebraic closure $\overline{\mathbb{F}}_p$, so:
        $$\alpha^p - \alpha - 1 = 0 \implies \alpha^p = \alpha + 1.$$
    <2>2. We claim that for every $k \in \mathbb{F}_p = \{0, 1, 2, \dots, p-1\}$, the element $\alpha + k$ is also a root of $f(x)$:
        - Using the Frobenius identity $(\alpha + k)^p = \alpha^p + k^p = \alpha^p + k$ (by Fermat's Little Theorem $k^p = k$ for $k \in \mathbb{F}_p$):
          $$f(\alpha + k) = (\alpha + k)^p - (\alpha + k) - 1 = (\alpha^p + k) - (\alpha + k) - 1 = \alpha^p - \alpha - 1 = 0.$$
    <2>3. Since $\alpha + 0, \alpha + 1, \dots, \alpha + (p-1)$ are $p$ **mutually distinct** elements of $\overline{\mathbb{F}}_p$, the complete set of roots of $f(x)$ is:
        $$\{\alpha, \alpha + 1, \alpha + 2, \dots, \alpha + (p - 1)\}.$$

<1>3. Irreducibility over $\mathbb{F}_p$:
    *Proof:*
    <2>1. Let $g(x) \in \mathbb{F}_p[x]$ be an irreducible factor of $f(x)$ in $\mathbb{F}_p[x]$ with $d = \deg(g) \ge 1$, such that $g(\alpha) = 0$.
    <2>2. The roots of $g(x)$ are a subset of the roots of $f(x)$, so every root of $g(x)$ is of the form $\alpha + k_i$ for some $k_i \in \mathbb{F}_p$.
    <2>3. The coefficient of $x^{d-1}$ in $g(x)$ is the negative sum of its roots:
        $$-\sum_{i=1}^d (\alpha + k_i) = -d \alpha - \sum_{i=1}^d k_i \in \mathbb{F}_p.$$
    <2>4. Since $\sum k_i \in \mathbb{F}_p$, this implies:
        $$d \alpha \in \mathbb{F}_p.$$
    <2>5. We test the two possibilities for $d = \deg(g) \in \{1, 2, \dots, p\}$:
        - If $d < p$: since $p$ is prime, $\gcd(d, p) = 1$, so $d \in \mathbb{F}_p^\times$ is invertible.
          Then $\alpha = d^{-1}(d\alpha) \in \mathbb{F}_p$.
          Evaluating $f$ on any element $c \in \mathbb{F}_p$: $f(c) = c^p - c - 1 = c - c - 1 = -1 \ne 0$.
          Thus $f(x)$ has **no roots in $\mathbb{F}_p$**, so $\alpha \notin \mathbb{F}_p$, a contradiction!
        - Therefore, we must have $d = p$.
    <2>6. Since the irreducible factor $g(x)$ has degree $d = p = \deg(f)$, $f(x)$ must itself be **irreducible over $\mathbb{F}_p$**.

<1>4. Conclusion:
    $f(x) = x^p - x - 1$ is an irreducible polynomial of degree $p$ over $\mathbb{F}_p$ for every prime $p$. Q.E.D.
:::
