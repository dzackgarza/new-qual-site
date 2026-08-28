---
schema: qual/card@1
id: P-SP3SQ
kind: problem
title: The formula $\sum_{i=1}^n i^2 = n(n+1)(2n+1)/6$
classification:
  areas:
  - prelim
  topics:
  - Induction
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
Prove the formula $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$.
:::

::: solution
**Goal:** Prove by mathematical induction that for all integers $n \ge 1$,
$$\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}.$$

<1>1. Base case ($n = 1$):
    For $n = 1$, the left-hand side is $\sum_{i=1}^1 i^2 = 1^2 = 1$.
    The right-hand side is $\frac{1(1+1)(2(1)+1)}{6} = \frac{1 \cdot 2 \cdot 3}{6} = 1$.
    Thus the base case holds.

<1>2. Induction hypothesis:
    Assume that for some integer $k \ge 1$,
    $$\sum_{i=1}^k i^2 = \frac{k(k+1)(2k+1)}{6}.$$

<1>3. Induction step ($n = k + 1$):
    $$\sum_{i=1}^{k+1} i^2 = \frac{(k+1)((k+1)+1)(2(k+1)+1)}{6} = \frac{(k+1)(k+2)(2k+3)}{6}.$$
    *Proof:*
    <2>1. Split the sum into the first $k$ terms and the $(k+1)$-th term:
        $$\sum_{i=1}^{k+1} i^2 = \left(\sum_{i=1}^k i^2\right) + (k+1)^2.$$
    <2>2. Substitute the induction hypothesis <1>2:
        $$\sum_{i=1}^{k+1} i^2 = \frac{k(k+1)(2k+1)}{6} + (k+1)^2.$$
    <2>3. Factor out the common term $(k+1)$:
        $$\sum_{i=1}^{k+1} i^2 = (k+1)\left[\frac{k(2k+1)}{6} + (k+1)\right] = (k+1)\left[\frac{2k^2 + k + 6k + 6}{6}\right] = (k+1)\left[\frac{2k^2 + 7k + 6}{6}\right].$$
    <2>4. Factor the quadratic polynomial $2k^2 + 7k + 6 = (k+2)(2k+3)$:
        $$\sum_{i=1}^{k+1} i^2 = \frac{(k+1)(k+2)(2k+3)}{6}.$$

<1>4. Conclusion:
    By mathematical induction, the formula holds for all integers $n \ge 1$. Q.E.D.
:::
