---
schema: qual/card@1
id: P-YLMKZ
kind: problem
title: Can a polynomial over a division ring have more roots than its degree?
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Rings
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Can a polynomial over a division ring (skew-field) have more roots than its degree?
:::

::: solution
**Goal:** Show that polynomials over non-commutative division rings can have infinitely many roots, even for degree 2 polynomials.

<1>1. Answer:
    **Yes**, a polynomial of degree $n$ over a non-commutative division ring $D$ can have strictly more than $n$ roots, and in fact can have infinitely (uncountably) many roots.

<1>2. Concrete Counterexample in the Hamilton Quaternions $\mathbb{H}$:
    *Proof:*
    <2>1. Let $D = \mathbb{H} = \{a + bi + cj + dk \mid a, b, c, d \in \mathbb{R}\}$ be the real division algebra of Hamilton quaternions.
    <2>2. Consider the degree 2 polynomial:
        $$P(x) = x^2 + 1 \in \mathbb{H}[x].$$
    <2>3. Let $q = bi + cj + dk$ be any pure imaginary quaternion (with real part zero) such that:
        $$b^2 + c^2 + d^2 = 1.$$
    <2>4. Compute $q^2$:
        $$\begin{aligned}
        q^2 &= (bi + cj + dk)^2 \\
        &= b^2 i^2 + c^2 j^2 + d^2 k^2 + bc(ij+ji) + bd(ik+ki) + cd(jk+kj) \\
        &= -b^2 - c^2 - d^2 + 0 + 0 + 0 \\
        &= -(b^2 + c^2 + d^2) = -1.
        \end{aligned}$$
    <2>5. Therefore:
        $$P(q) = q^2 + 1 = -1 + 1 = 0.$$
    <2>6. Every point on the 2-dimensional sphere $S^2 = \{(b, c, d) \in \mathbb{R}^3 \mid b^2 + c^2 + d^2 = 1\}$ gives a distinct root of $x^2 + 1$.
    <2>7. Thus, the quadratic polynomial $x^2 + 1$ has **uncountably infinitely many roots** in $\mathbb{H}$, far exceeding its degree $n = 2$.

<1>3. Reason for failure of the classical root-bound theorem:
    *Proof:*
    <2>1. Over a commutative field $F$, if $\alpha$ is a root of $P(x)$, then $P(x) = Q(x)(x - \alpha)$. If $\beta \ne \alpha$ is another root, $0 = P(\beta) = Q(\beta)(\beta - \alpha)$, and since $F$ has no zero divisors and multiplication is commutative, $Q(\beta) = 0$, reducing degree by 1 per root.
    <2>2. Over a division ring $D$, right division gives $P(x) = Q(x)(x - \alpha) + R$. While $P(\alpha) = 0 \implies P(x) = Q(x)(x - \alpha)$, evaluating at another element $\beta$ gives:
        $$P(\beta) = Q(\beta)(\beta - \alpha)$$
        only if $\beta$ commutes with all coefficients of $Q(x)$. In general, $(\beta - \alpha)$ is not a zero divisor, but $Q(\beta)$ does not need to vanish because $\beta$ and the coefficients do not commute!
    <2>3. **Gordon–Motzkin Theorem:** The roots of a polynomial of degree $n$ over a division ring $D$ fall into at most $n$ conjugacy classes. In the example $x^2 + 1$, the infinite family of roots forms a single conjugacy class (the sphere of pure unit quaternions conjugate to $i$).

<1>4. Conclusion:
    Yes; $x^2 + 1$ in $\mathbb{H}$ has an entire 2-sphere of roots $\{bi+cj+dk \mid b^2+c^2+d^2=1\}$. Q.E.D.
:::
