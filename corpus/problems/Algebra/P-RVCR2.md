---
schema: qual/card@1
id: P-RVCR2
kind: problem
title: Every element of a finite-dimensional $k$-algebra is integral over $k$, and
  a non-zero-divisor is a unit
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Integral Extensions
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $R$ be a commutative ring containing a field $k$ such that $\dim_k(R) = d < \infty$.
Let $a \in R$.
(1) Show that there exist $n \in \mathbb{N}$ with $1 \le n \le d$ and coefficients $c_0, c_1, \dots, c_{n-1} \in k$ such that:
$$a^n + c_{n-1}a^{n-1} + \cdots + c_1 a + c_0 = 0.$$
(2) Suppose such a relation holds. Show that if $c_0 \ne 0$, then $a$ is a unit in $R$.
(3) Show that if $a$ is not a zero-divisor in $R$, then $a$ is invertible in $R$.
:::

::: solution
**Goal:** Prove that elements in finite-dimensional $k$-algebras satisfy monic polynomial relations over $k$, and that non-zero-divisors are units.

<1>1. Part 1: Existence of Monic Polynomial Relation:
    *Proof:*
    <2>1. Let $d = \dim_k(R) < \infty$.
    <2>2. Consider the set of $d + 1$ powers of $a$:
        $$\{1, a, a^2, a^3, \dots, a^d\} \subset R.$$
    <2>3. Since the cardinality of this set is $d + 1 > \dim_k(R)$, these elements must be **linearly dependent over $k$**.
    <2>4. Therefore, there exist scalars $\lambda_0, \lambda_1, \dots, \lambda_d \in k$, not all zero, such that:
        $$\sum_{i=0}^d \lambda_i a^i = 0.$$
    <2>5. Let $n = \max\{i \in \{0, 1, \dots, d\} \mid \lambda_i \ne 0\}$. Since at least one $\lambda_i \ne 0$, $n \ge 0$.
    <2>6. If $n = 0$, $\lambda_0 \cdot 1 = 0 \implies \lambda_0 = 0$ (since $k \subseteq R$), a contradiction. Thus $n \ge 1$.
    <2>7. Dividing by the leading non-zero coefficient $\lambda_n \in k^\times$:
        $$a^n + c_{n-1} a^{n-1} + \cdots + c_1 a + c_0 = 0$$
        where $c_i = \lambda_i / \lambda_n \in k$.

<1>2. Part 2: Invertibility when $c_0 \ne 0$:
    *Proof:*
    <2>1. Suppose $a^n + c_{n-1} a^{n-1} + \cdots + c_1 a + c_0 = 0$ with $c_0 \ne 0$.
    <2>2. Rearranging the equation:
        $$a(a^{n-1} + c_{n-1} a^{n-2} + \cdots + c_1) = -c_0.$$
    <2>3. Since $c_0 \in k \setminus \{0\}$, $-c_0$ is invertible in $k \subseteq R$.
    <2>4. Dividing both sides by $-c_0$:
        $$a \cdot \left[ -\frac{1}{c_0} (a^{n-1} + c_{n-1} a^{n-2} + \cdots + c_1) \right] = 1.$$
    <2>5. Defining $b = -\frac{1}{c_0} (a^{n-1} + c_{n-1} a^{n-2} + \cdots + c_1) \in R$, we have $a b = 1$.
    <2>6. Thus $a \in R^\times$ is a **unit** in $R$, with $a^{-1} = b$.

<1>3. Part 3: Non-Zero-Divisors are Invertible:
    *Proof:*
    <2>1. **Method A (Minimal polynomial argument):**
        - Let $m(x) = x^m + c_{m-1}x^{m-1} + \dots + c_0 \in k[x]$ be the **minimal degree monic polynomial** annihilating $a$ ($m(a) = 0$).
        - Factor out $a$: $a(a^{m-1} + c_{m-1} a^{m-2} + \cdots + c_1) = -c_0$.
        - If $c_0 = 0$, then $a(a^{m-1} + c_{m-1} a^{m-2} + \cdots + c_1) = 0$.
        - By minimality of $m = \deg(m)$, the element $y \coloneqq a^{m-1} + c_{m-1} a^{m-2} + \cdots + c_1 \ne 0$.
        - Then $a \cdot y = 0$ with $y \ne 0$, meaning $a$ is a **zero-divisor** in $R$.
        - Hence, if $a$ is **not a zero-divisor**, we must have $c_0 \ne 0$.
        - By Part 2, $c_0 \ne 0 \implies a \in R^\times$.
    <2>2. **Method B (Linear map dimension argument):**
        - Consider the $k$-linear multiplication map $L_a: R \to R$ given by $L_a(x) = a x$.
        - $\ker(L_a) = \{x \in R \mid a x = 0\}$.
        - Since $a$ is not a zero-divisor, $\ker(L_a) = \{0\}$, so $L_a$ is **injective**.
        - For a linear operator on a **finite-dimensional vector space** ($R$), injectivity implies **surjectivity** (Rank-Nullity Theorem).
        - Therefore, $L_a$ is surjective, so there exists $b \in R$ such that $L_a(b) = a b = 1$.
        - Thus $a$ is invertible in $R$.

<1>4. Conclusion:
    Every element in a finite-dimensional algebra satisfies a monic polynomial over $k$, and every non-zero-divisor is invertible. Q.E.D.
:::
