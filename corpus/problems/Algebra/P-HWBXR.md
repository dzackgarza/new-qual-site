---
schema: qual/card@1
id: P-HWBXR
kind: problem
title: A polynomial of degree $2$ or $3$ in $k[x]$ is irreducible iff it has no root
  in $k$
classification:
  areas:
  - algebra
  topics:
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
Let $k$ be a field and let $f(x) \in k[x]$ be a polynomial of degree $\deg(f) \in \{2, 3\}$.
Prove that $f(x)$ is irreducible in $k[x]$ if and only if $f(x)$ has no roots in $k$.
:::

::: solution
**Goal:** Prove that for polynomials of degree 2 or 3 over a field $k$, irreducibility is equivalent to having no root in $k$.

<1>1. Direction $(\implies)$: $f$ irreducible $\implies f$ has no roots in $k$:
    *Proof:*
    <2>1. Suppose, for contradiction, that $f(x)$ has a root $\alpha \in k$, so $f(\alpha) = 0$.
    <2>2. By the Factor Theorem in the polynomial ring $k[x]$, $f(x) = (x - \alpha) g(x)$ for some polynomial $g(x) \in k[x]$.
    <2>3. By additivity of polynomial degrees:
        $$\deg(f) = \deg(x - \alpha) + \deg(g) = 1 + \deg(g).$$
    <2>4. Since $\deg(f) \in \{2, 3\}$, we have $\deg(g) = \deg(f) - 1 \in \{1, 2\}$.
    <2>5. Since both factors $(x - \alpha)$ and $g(x)$ have degree $\ge 1$ and $< \deg(f)$, neither factor is a unit (constant in $k^\times$).
    <2>6. Thus $f(x) = (x - \alpha) g(x)$ is a non-trivial factorization of $f(x)$ in $k[x]$.
    <2>7. This contradicts the assumption that $f(x)$ is irreducible.
    <2>8. Thus $f(x)$ has no roots in $k$.

<1>2. Direction $(\impliedby)$: $f$ has no roots in $k \implies f$ is irreducible:
    *Proof:*
    <2>1. Suppose, for contradiction, that $f(x)$ is reducible in $k[x]$.
    <2>2. Then there exists a non-trivial factorization $f(x) = g(x) h(x)$ with $\deg(g) \ge 1$, $\deg(h) \ge 1$, and $\deg(g) + \deg(h) = \deg(f)$.
    <2>3. **Case 1: $\deg(f) = 2$:**
        - $\deg(g) + \deg(h) = 2 \implies \deg(g) = 1$ and $\deg(h) = 1$.
        - The linear polynomial $g(x) = a x + b$ with $a \ne 0$ has root $-b a^{-1} \in k$.
        - Therefore, $f(-b a^{-1}) = g(-b a^{-1}) h(-b a^{-1}) = 0 \cdot h(-b a^{-1}) = 0$.
        - Thus $f$ has a root in $k$, a contradiction.
    <2>4. **Case 2: $\deg(f) = 3$:**
        - $\deg(g) + \deg(h) = 3$ with $\deg(g), \deg(h) \ge 1$.
        - The only integer partitions of 3 into two positive integers are $1 + 2$ and $2 + 1$.
        - Thus at least one of the factors, say $g(x)$, must have degree exactly 1.
        - As in Case 1, a linear factor $g(x) = a x + b$ in $k[x]$ has a root in $k$.
        - Thus $f(x)$ has a root in $k$, a contradiction.
    <2>5. In either case, the reducibility of $f(x)$ forces $f(x)$ to have a root in $k$.
    <2>6. By contrapositive, if $f(x)$ has no roots in $k$, then $f(x)$ is irreducible in $k[x]$.

<1>3. Remark on failure for $\deg \ge 4$:
    *Proof:*
    <2>1. For $\deg(f) \ge 4$, a polynomial can factor into irreducible factors of degree $\ge 2$ without having any roots in $k$.
    <2>2. For example, $f(x) = (x^2 + 1)^2 = x^4 + 2x^2 + 1 \in \mathbb{R}[x]$ has no real roots, but is reducible in $\mathbb{R}[x]$.

<1>4. Conclusion:
    For $\deg(f) \in \{2, 3\}$, $f(x)$ is irreducible in $k[x]$ if and only if $f(x)$ has no roots in $k$. Q.E.D.
:::
