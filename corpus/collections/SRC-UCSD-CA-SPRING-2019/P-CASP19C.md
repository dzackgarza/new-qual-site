---
schema: qual/card@1
id: P-CASP19C
kind: problem
title: "Analytic function on B(0,1+epsilon) with |f|<1 on |z|=1 has a unique fixed point in D"
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Rouché
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $f$ be an analytic function on the open disk $B(0, 1 + \varepsilon)$ for some $\varepsilon > 0$.
Assume that $|f(z)| < 1$ for all $|z| = 1$.
Prove that there exists a **unique fixed point** $z_0 \in \mathbb{D}$ (i.e. $|z_0| < 1$ and $f(z_0) = z_0$).
:::

::: solution
**Goal:** Prove the existence of a unique solution to $f(z) - z = 0$ in the unit disk $\mathbb{D}$ using Rouché's Theorem.

<1>1. Setting up Rouché's Theorem:
    *Proof:*
    <2>1. A fixed point of $f$ inside the unit disk $\mathbb{D} = \{ z \in \mathbb{C} \mid |z| < 1 \}$ is a root of the equation:
        $$g(z) \coloneqq z - f(z) = 0.$$
    <2>2. Define the auxiliary comparison function:
        $$h(z) \coloneqq z.$$
    <2>3. Both $g(z) - h(z) = -f(z)$ and $h(z) = z$ are holomorphic on $B(0, 1 + \varepsilon)$, which strictly contains the closed unit disk $\overline{\mathbb{D}} = \{ z \in \mathbb{C} \mid |z| \le 1 \}$.
    <2>4. Consider the boundary circle $C = \{ z \in \mathbb{C} \mid |z| = 1 \}$.

<1>2. Boundary Estimate on $|z| = 1$:
    *Proof:*
    <2>1. On the circle $|z| = 1$:
        $$|h(z)| = |z| = 1.$$
    <2>2. By the given hypothesis, for all $z$ with $|z| = 1$:
        $$|f(z)| < 1.$$
    <2>3. Therefore, along the entire boundary circle $|z| = 1$:
        $$|g(z) - h(z)| = |-f(z)| = |f(z)| < 1 = |h(z)|.$$
    <2>4. That is, $|g(z) - h(z)| < |h(z)|$ strictly holds on the simple closed curve $\partial\mathbb{D}$.

<1>3. Application of Rouché's Theorem:
    *Proof:*
    <2>1. By **Rouché's Theorem**, the functions $g(z) = z - f(z)$ and $h(z) = z$ have the **same number of zeros (counted with multiplicity)** inside the open unit disk $\mathbb{D}$.
    <2>2. The function $h(z) = z$ has exactly one simple zero in $\mathbb{D}$ (at $z = 0$).
    <2>3. Therefore, $g(z) = z - f(z)$ has **exactly one zero $z_0$ (counted with multiplicity)** in $\mathbb{D}$.
    <2>4. Hence there is a unique $z_0 \in \mathbb{D}$ such that $z_0 - f(z_0) = 0$, or equivalently $f(z_0) = z_0$.

<1>4. Conclusion:
    $f$ has a unique fixed point in $\mathbb{D} = \{|z| < 1\}$. Q.E.D.
:::
