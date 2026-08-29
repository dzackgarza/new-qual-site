---
schema: qual/card@1
id: P-TVSSR
kind: problem
title: Galois group of $x^3+6x+3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Compute the Galois group of the cubic polynomial $f(x) = x^3 + 6x + 3$ over $\mathbb{Q}$.
:::

::: solution
**Goal:** Prove that $\operatorname{Gal}(f/\mathbb{Q}) \cong S_3$.

<1>1. Irreducibility of $f(x)$ over $\mathbb{Q}$:
    *Proof:*
    <2>1. Consider the polynomial $f(x) = x^3 + 6x + 3 \in \mathbb{Z}[x]$.
    <2>2. We test for irreducibility using **Eisenstein's Criterion** with the prime $p = 3$:
        - $3 \nmid 1$ (the leading coefficient).
        - $3 \mid 6$ (the linear coefficient).
        - $3 \mid 3$ (the constant coefficient).
        - $3^2 = 9 \nmid 3$ (the constant term is not divisible by $p^2$).
    <2>3. By Eisenstein's Criterion, $f(x)$ is **irreducible over $\mathbb{Q}$**.
    <2>4. Therefore, the degree of the splitting field $L$ over $\mathbb{Q}$ is divisible by $[K(u) : \mathbb{Q}] = 3$, so $\operatorname{Gal}(f/\mathbb{Q})$ is a transitive subgroup of $S_3$.
    <2>5. Thus:
        $$\operatorname{Gal}(f/\mathbb{Q}) \cong A_3 \cong \mathbb{Z}_3 \quad \text{or} \quad \operatorname{Gal}(f/\mathbb{Q}) \cong S_3.$$

<1>2. Computation of the Discriminant $\Delta(f)$:
    *Proof:*
    <2>1. For the depressed cubic $x^3 + px + q$ where $p = 6$ and $q = 3$, the discriminant formula is:
        $$\Delta = -4 p^3 - 27 q^2.$$
    <2>2. Substituting $p = 6$ and $q = 3$:
        $$\Delta = -4(6^3) - 27(3^2) = -4(216) - 27(9) = -864 - 243 = -1107.$$
    <2>3. Factoring $-1107$:
        $$-1107 = -9 \times 123 = -3^2 \times 3 \times 41 = -3^3 \times 41.$$
    <2>4. Since $\Delta = -1107 < 0$, $\Delta$ is **negative**, so $\Delta \notin (\mathbb{Q}^\times)^2$ (in fact $\sqrt{-1107} = 3i\sqrt{123} \notin \mathbb{Q}$).

<1>3. Determination of the Galois Group:
    *Proof:*
    <2>1. For an irreducible cubic polynomial over $\mathbb{Q}$:
        $$\operatorname{Gal}(f/\mathbb{Q}) \cong \begin{cases} A_3 \cong \mathbb{Z}_3 & \text{if } \Delta \in (\mathbb{Q}^\times)^2, \\ S_3 & \text{if } \Delta \notin (\mathbb{Q}^\times)^2. \end{cases}$$
    <2>2. Since $\Delta = -1107$ is not a square in $\mathbb{Q}$, the square root of the discriminant generates a quadratic extension $\mathbb{Q}(\sqrt{-1107}) = \mathbb{Q}(i\sqrt{123}) \subset L$.
    <2>3. The splitting field degree is $[L : \mathbb{Q}] = 3 \times 2 = 6$.
    <2>4. Therefore:
        $$\operatorname{Gal}(f/\mathbb{Q}) \cong S_3.$$

<1>4. Real Roots Confirmation:
    *Proof:*
    <2>1. $f'(x) = 3x^2 + 6 > 0$ for all $x \in \mathbb{R}$, so $f(x)$ is strictly increasing.
    <2>2. Thus $f(x)$ has exactly $1$ real root and $2$ complex conjugate non-real roots.
    <2>3. Complex conjugation restricts to a transposition in $\operatorname{Gal}(f/\mathbb{Q})$.
    <2>4. A transitive subgroup of $S_3$ containing a transposition must be all of $S_3$.

<1>5. Conclusion:
    $\operatorname{Gal}(x^3 + 6x + 3 / \mathbb{Q}) \cong S_3$. Q.E.D.
:::
