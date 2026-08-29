---
schema: qual/card@1
id: P-CAF13C
kind: problem
title: "A holomorphic map of the unit disk with sup norm ≤ 1 has a unique fixed point"
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
Let $f$ be holomorphic on a neighborhood of the closed unit disk $\overline{\mathbb{D}}$.
Suppose $\sup_{z \in \partial\mathbb{D}} |f(z)| \leq 1$, and that $f$ has no fixed points on the boundary $\partial\mathbb{D}$ ($f(z) \ne z$ for all $|z| = 1$).
Prove that $f$ has **exactly one fixed point** in the open unit disk $\mathbb{D}$.
:::

::: solution
**Goal:** Prove that $f(z) - z$ has exactly one zero in $\mathbb{D}$ using Rouché's Theorem on the boundary circle $|z| = 1$.

<1>1. Setting up Rouché's Theorem:
    *Proof:*
    <2>1. Let $g(z) = -z$ and $F(z) = f(z) - z$.
    <2>2. Both $g$ and $F$ are holomorphic on an open neighborhood $U \supset \overline{\mathbb{D}}$.
    <2>3. Notice that:
        $$F(z) - g(z) = (f(z) - z) - (-z) = f(z).$$
    <2>4. We wish to apply Rouché's Theorem to the functions $F(z)$ and $g(z)$ on the curve $C = \partial\mathbb{D} = \{ |z| = 1 \}$.
    <2>5. The standard strict inequality in Rouché's theorem requires:
        $$|F(z) - g(z)| < |g(z)| + |F(z)| \quad \text{on } \partial\mathbb{D}.$$

<1>2. Verifying the Strict Rouché Condition on $\partial\mathbb{D}$:
    *Proof:*
    <2>1. On the boundary circle $|z| = 1$, we have $|g(z)| = |-z| = 1$.
    <2>2. By hypothesis, $|f(z)| \le 1$ for all $|z| = 1$.
    <2>3. We are also given that $f(z) \ne z$ for all $|z| = 1$, so $|F(z)| = |f(z) - z| > 0$ on $\partial\mathbb{D}$.
    <2>4. Suppose for contradiction that there exists some $z_0 \in \partial\mathbb{D}$ where the strict Rouché inequality fails:
        $$|f(z_0)| = |F(z_0) - g(z_0)| \ge |g(z_0)| + |F(z_0)| = 1 + |f(z_0) - z_0|.$$
    <2>5. But by the triangle inequality:
        $$|f(z_0) - z_0| \ge |z_0| - |f(z_0)| = 1 - |f(z_0)| \ge 0.$$
    <2>6. Adding $1$ to both sides gives $1 + |f(z_0) - z_0| \ge 2 - |f(z_0)|$.
    <2>7. Combining these gives:
        $$|f(z_0)| \ge 1 + |f(z_0) - z_0| \ge 2 - |f(z_0)| \implies 2|f(z_0)| \ge 2 \implies |f(z_0)| \ge 1.$$
    <2>8. Since $|f(z_0)| \le 1$, we must have $|f(z_0)| = 1$.
    <2>9. Then $|f(z_0) - z_0| \le |f(z_0)| - 1 = 0 \implies f(z_0) = z_0$, which contradicts the hypothesis that $f$ has no fixed points on $\partial\mathbb{D}$!
    <2>10. Therefore, for all $z \in \partial\mathbb{D}$, we strictly have:
        $$|F(z) - g(z)| < |F(z)| + |g(z)|.$$

<1>3. Alternative Direct Homotopy / Argument Principle Proof:
    *Proof:*
    <2>1. For $t \in [0, 1]$, define the homotopy of holomorphic functions:
        $$h_t(z) = t f(z) - z.$$
    <2>2. On $\partial\mathbb{D}$:
        - For $t \in [0, 1)$: $|t f(z)| \le t < 1 = |z|$, so $h_t(z) \ne 0$.
        - For $t = 1$: $h_1(z) = f(z) - z \ne 0$ by the given hypothesis.
    <2>3. Thus $h_t(z) \ne 0$ on $\partial\mathbb{D}$ for all $t \in [0, 1]$.
    <2>4. By the continuous invariance of the winding number (or Rouché's Theorem), the number of zeros of $h_t(z)$ in $\mathbb{D}$ is constant for all $t \in [0, 1]$.
    <2>5. At $t = 0$: $h_0(z) = -z$, which has **exactly one zero** (at $z = 0$) in $\mathbb{D}$.
    <2>6. Therefore, at $t = 1$: $h_1(z) = f(z) - z$ has **exactly one zero** in $\mathbb{D}$.

<1>4. Conclusion:
    $f$ has a unique fixed point in $\mathbb{D}$. Q.E.D.
:::
