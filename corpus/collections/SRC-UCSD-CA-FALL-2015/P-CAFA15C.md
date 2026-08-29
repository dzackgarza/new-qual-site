---
schema: qual/card@1
id: P-CAFA15C
kind: problem
title: "Polynomial with non-increasing real coefficients has no roots inside the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $a_0, a_1, \dots, a_n$ be a strictly positive, non-increasing sequence of real numbers:
$$a_0 \ge a_1 \ge a_2 \ge \cdots \ge a_n > 0.$$
Prove that the polynomial:
$$P(z) = a_0 + a_1 z + a_2 z^2 + \cdots + a_n z^n$$
has **no roots inside the open unit disk** $|z| < 1$ (Eneström–Kakeya Theorem).
:::

::: solution
**Goal:** Prove that $P(z) \ne 0$ for all $|z| < 1$ by analyzing the auxiliary polynomial $F(z) = (1 - z)P(z)$ via the triangle inequality.

<1>1. Setting and Auxiliary Polynomial $F(z) = (1 - z)P(z)$:
    *Proof:*
    <2>1. Let $P(z) = \sum_{k=0}^n a_k z^k$ with $a_0 \ge a_1 \ge \cdots \ge a_n > 0$.
    <2>2. Consider the polynomial $F(z) \coloneqq (1 - z) P(z)$:
        $$F(z) = (1 - z)(a_0 + a_1 z + a_2 z^2 + \cdots + a_n z^n).$$
    <2>3. Expanding the product:
        $$F(z) = a_0 + (a_1 - a_0) z + (a_2 - a_1) z^2 + \cdots + (a_n - a_{n-1}) z^n - a_n z^{n+1}.$$
    <2>4. Rearranging into the leading term $a_0$ and remaining terms:
        $$F(z) = a_0 - \left[ (a_0 - a_1) z + (a_1 - a_2) z^2 + \cdots + (a_{n-1} - a_n) z^n + a_n z^{n+1} \right].$$

<1>2. Modulus Bound on the Open Unit Disk $|z| < 1$:
    *Proof:*
    <2>1. Let $z \in \mathbb{C}$ with $|z| < 1$.
    <2>2. By the reverse triangle inequality:
        $$|F(z)| \ge a_0 - \left| (a_0 - a_1) z + (a_1 - a_2) z^2 + \cdots + (a_{n-1} - a_n) z^n + a_n z^{n+1} \right|.$$
    <2>3. Applying the triangle inequality to the subtracted term:
        $$\left| \sum_{k=1}^n (a_{k-1} - a_k) z^k + a_n z^{n+1} \right| \le \sum_{k=1}^n |a_{k-1} - a_k| |z|^k + a_n |z|^{n+1}.$$
    <2>4. Since the sequence is non-increasing ($a_{k-1} \ge a_k$), every difference $(a_{k-1} - a_k) \ge 0$, so $|a_{k-1} - a_k| = a_{k-1} - a_k$.
    <2>5. Furthermore, since $|z| < 1$, for all $k \ge 1$ we have $|z|^k < 1$ and $|z|^{n+1} < 1$.
    <2>6. Therefore, since $a_n > 0$ and at least one term is strictly bounded by 1:
        $$\sum_{k=1}^n (a_{k-1} - a_k) |z|^k + a_n |z|^{n+1} < \sum_{k=1}^n (a_{k-1} - a_k) \cdot 1 + a_n \cdot 1.$$
    <2>7. The right-hand side is a **telescoping sum**:
        $$\sum_{k=1}^n (a_{k-1} - a_k) + a_n = (a_0 - a_1) + (a_1 - a_2) + \cdots + (a_{n-1} - a_n) + a_n = a_0.$$
    <2>8. Combining these inequalities:
        $$\left| \sum_{k=1}^n (a_{k-1} - a_k) z^k + a_n z^{n+1} \right| < a_0.$$

<1>3. Non-Vanishing of $P(z)$ for $|z| < 1$:
    *Proof:*
    <2>1. Substituting the strict bound into the modulus of $F(z)$:
        $$|F(z)| > a_0 - a_0 = 0 \quad \text{for all } |z| < 1.$$
    <2>2. Thus $F(z) \ne 0$ for all $z$ with $|z| < 1$.
    <2>3. Since $F(z) = (1 - z) P(z)$, and $(1 - z) \ne 0$ for $|z| < 1$:
        $$P(z) = \frac{F(z)}{1 - z} \ne 0 \quad \text{for all } |z| < 1.$$

<1>4. Conclusion:
    The polynomial $P(z)$ has no roots in the open unit disk $\{z \in \mathbb{C} \mid |z| < 1\}$. Q.E.D.
:::
