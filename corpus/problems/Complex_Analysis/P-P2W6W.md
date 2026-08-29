---
schema: qual/card@1
id: P-P2W6W
kind: problem
title: A continuous function vanishing at $\pm\infty$ is uniformly continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Suppose $f: \mathbb{R} \to \mathbb{R}$ is continuous and $\lim_{x \to \pm \infty} f(x) = 0$.
Prove that $f$ is uniformly continuous on $\mathbb{R}$.
:::

::: solution
**Goal:** Prove that a continuous function on $\mathbb{R}$ vanishing at $\pm\infty$ is uniformly continuous on $\mathbb{R}$.

<1>1. Strategy: 3-epsilon argument partitioning $\mathbb{R}$ into compact and infinite pieces:
    *Proof:*
    <2>1. Let $\varepsilon > 0$ be given.
    <2>2. We seek $\delta > 0$ such that for all $x, y \in \mathbb{R}$, $|x - y| < \delta \implies |f(x) - f(y)| < \varepsilon$.

<1>2. Step 1: Controlling the tails using $\lim_{x \to \pm \infty} f(x) = 0$:
    *Proof:*
    <2>1. Because $\lim_{x \to +\infty} f(x) = 0$, there exists $M_1 > 0$ such that:
        $$x > M_1 \implies |f(x)| < \frac{\varepsilon}{3}.$$
    <2>2. Because $\lim_{x \to -\infty} f(x) = 0$, there exists $M_2 > 0$ such that:
        $$x < -M_2 \implies |f(x)| < \frac{\varepsilon}{3}.$$
    <2>3. Let $M = \max(M_1, M_2) > 0$. Then:
        $$|x| \ge M \implies |f(x)| < \frac{\varepsilon}{3}.$$

<1>3. Step 2: Uniform continuity on the compact interval $[-M-1, M+1]$ (Heine–Cantor):
    *Proof:*
    <2>1. Consider the closed, bounded interval $K = [-M-1, M+1]$.
    <2>2. Since $K$ is compact and $f$ is continuous on $K$, by the Heine–Cantor Theorem, $f$ is uniformly continuous on $K$.
    <2>3. Therefore, there exists $\delta_1 > 0$ such that for all $x, y \in K$:
        $$|x - y| < \delta_1 \implies |f(x) - f(y)| < \frac{\varepsilon}{3}.$$
    <2>4. Define $\delta = \min(\delta_1, 1) > 0$.

<1>4. Step 3: Verifying $|f(x) - f(y)| < \varepsilon$ for all $x, y \in \mathbb{R}$ with $|x - y| < \delta$:
    *Proof:*
    <2>1. Let $x, y \in \mathbb{R}$ with $|x - y| < \delta \le 1$.
    <2>2. **Case A: Both $x, y \in K = [-M-1, M+1]$.**
        - Since $x, y \in K$ and $|x - y| < \delta_1$, by Step 2:
            $$|f(x) - f(y)| < \frac{\varepsilon}{3} < \varepsilon.$$
    <2>3. **Case B: At least one of $x, y$ lies outside $[-M, M]$ (say $|x| \ge M$).**
        - Since $|x - y| < \delta \le 1$ and $|x| \ge M$, by the triangle inequality:
            $$|y| \ge |x| - |x - y| > M - 1 \quad \text{(so } y \in K \text{ if } |x| \le M+1\text{)}.$$
        - If $|y| \ge M$, then both $|x| \ge M$ and $|y| \ge M$, so:
            $$|f(x) - f(y)| \le |f(x)| + |f(y)| < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \frac{2\varepsilon}{3} < \varepsilon.$$
        - If $|y| < M$, then since $|x - y| < 1$, we have $|x| < M + 1$. Thus both $x, y \in [-M-1, M+1] = K$, which falls under Case A!

<1>5. Conclusion:
    In all cases, $|x - y| < \delta \implies |f(x) - f(y)| < \varepsilon$. Thus $f$ is uniformly continuous on $\mathbb{R}$. Q.E.D.
:::
