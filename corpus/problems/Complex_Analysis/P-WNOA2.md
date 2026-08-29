---
schema: qual/card@1
id: P-WNOA2
kind: problem
title: Cauchy estimates for a holomorphic function of polynomial growth on a strip
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Suppose that $f$ is holomorphic on the strip $S = \{x+iy \mid x\in \mathbb{R},~ -1<y<1\}$ with $|f(z)| \leq A (1 + |z|)^\nu$ for $\nu \ge 0$ a fixed real number.
Show that for each integer $n\geq 0$ there exists an $A_n \geq 0$ such that $|f^{(n)}(x)| \leq A_n (1 + |x|)^\nu$ for all $x\in \mathbb{R}$.
:::

::: solution
**Goal:** Prove that for each $n \ge 0$, $|f^{(n)}(x)| \le A_n (1 + |x|)^\nu$ for all $x \in \mathbb{R}$.

<1>1. Choice of circle for Cauchy estimates:
    *Proof:*
    <2>1. For any $x \in \mathbb{R}$, consider the closed disk $\overline{D}(x, R)$ centered at $x \in S$ of radius $R = 1/2$.
    <2>2. Since $-1 < y < 1$ on $S$, the disk $\overline{D}(x, 1/2) = \{z \in \mathbb{C} \mid |z - x| \le 1/2\}$ is entirely contained in the strip $S$.
    <2>3. In particular, for every $\zeta \in \partial D(x, 1/2)$, we have $|\operatorname{Im}(\zeta)| \le 1/2 < 1$.

<1>2. Bound on $|f(\zeta)|$ on the circle $\partial D(x, 1/2)$:
    *Proof:*
    <2>1. For $\zeta \in \partial D(x, 1/2)$, we have $|\zeta - x| = 1/2$, so by the triangle inequality:
        $$|\zeta| \le |x| + |\zeta - x| = |x| + \frac{1}{2}.$$
    <2>2. Therefore:
        $$1 + |\zeta| \le 1 + |x| + \frac{1}{2} = \frac{3}{2} + |x| \le \frac{3}{2}(1 + |x|).$$
    <2>3. Since $\nu \ge 0$, $(1 + |\zeta|)^\nu \le (3/2)^\nu (1 + |x|)^\nu$.
    <2>4. Hence on $\partial D(x, 1/2)$:
        $$|f(\zeta)| \le A (1 + |\zeta|)^\nu \le A \left(\frac{3}{2}\right)^\nu (1 + |x|)^\nu.$$

<1>3. Application of Cauchy's estimates:
    *Proof:*
    <2>1. By Cauchy's Integral Formula derivative estimates on $D(x, R)$ with $R = 1/2$:
        $$|f^{(n)}(x)| \le \frac{n!}{R^n} \max_{\zeta \in \partial D(x, R)} |f(\zeta)| = n! \, 2^n \max_{|\zeta - x| = 1/2} |f(\zeta)|.$$
    <2>2. Substituting the bound from step <1>2:
        $$|f^{(n)}(x)| \le n! \, 2^n \cdot A \left(\frac{3}{2}\right)^\nu (1 + |x|)^\nu.$$
    <2>3. Setting $A_n = A \cdot n! \, 2^n \left(\frac{3}{2}\right)^\nu$, we have:
        $$|f^{(n)}(x)| \le A_n (1 + |x|)^\nu \quad \text{for all } x \in \mathbb{R}.$$

<1>4. Conclusion:
    For each $n \ge 0$, the constant $A_n = A n! 2^n (3/2)^\nu$ satisfies the required bound. Q.E.D.
:::
