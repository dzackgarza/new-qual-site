---
schema: qual/card@1
id: P-CCHG2
kind: problem
title: Let $f$ be a non-negative measurable function on $[0, 1]$. Show that
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - convergence-of-integrals
  - lp-spaces
  - norms
relations: []
review: draft
---

::: problem
Let $f$ be a non-negative measurable function on $[0, 1]$.

Show that
$$
\lim _{p \rightarrow \infty}\left(\int_{[0,1]} f(x)^{p} d x\right)^{\frac{1}{p}}=\|f\|_{\infty}.
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $M = \|f\|_\infty$.

**Case 1: $M = 0$.**
Then $f = 0$ almost everywhere on $[0, 1]$, so $\int_{[0, 1]} f^p = 0$ for all $p \geq 1$, and the limit is $0 = M$.

**Case 2: $0 < M < \infty$.**

1. **Upper bound:**
   Since $f(x) \leq M$ almost everywhere on $[0, 1]$:
   $$
   \int_{[0, 1]} f(x)^p \, dx \leq \int_{[0, 1]} M^p \, dx = M^p \cdot m([0, 1]) = M^p.
   $$
   Taking the $p$-th root gives:
   $$
   \|f\|_p = \left( \int_{[0, 1]} f(x)^p \, dx \right)^{1/p} \leq M = \|f\|_\infty \quad \text{for all } p \geq 1.
   $$
   Therefore:
   $$
   \limsup_{p \to \infty} \|f\|_p \leq \|f\|_\infty.
   $$

2. **Lower bound:**
   For any $\varepsilon \in (0, M)$, let $E_\varepsilon = \{x \in [0, 1] : f(x) > M - \varepsilon\}$.
   By the definition of essential supremum, $m(E_\varepsilon) > 0$.
   Then:
   $$
   \int_{[0, 1]} f(x)^p \, dx \geq \int_{E_\varepsilon} f(x)^p \, dx \geq (M - \varepsilon)^p m(E_\varepsilon).
   $$
   Taking the $p$-th root:
   $$
   \|f\|_p \geq (M - \varepsilon) \cdot m(E_\varepsilon)^{1/p}.
   $$
   Since $m(E_\varepsilon) > 0$, we have $\lim_{p \to \infty} m(E_\varepsilon)^{1/p} = 1$. Thus:
   $$
   \liminf_{p \to \infty} \|f\|_p \geq M - \varepsilon.
   $$
   Since $\varepsilon > 0$ was arbitrary, letting $\varepsilon \to 0$ yields:
   $$
   \liminf_{p \to \infty} \|f\|_p \geq M = \|f\|_\infty.
   $$

Combining the upper and lower bounds gives:
$$
\lim_{p \to \infty} \|f\|_p = \|f\|_\infty.
$$

**Case 3: $M = \infty$.**
For any $K > 0$, the set $E_K = \{x \in [0, 1] : f(x) > K\}$ has measure $m(E_K) > 0$.
Then $\|f\|_p \geq K \cdot m(E_K)^{1/p} \to K$ as $p \to \infty$, so $\liminf_{p \to \infty} \|f\|_p \geq K$. Since $K$ is arbitrary, $\lim_{p \to \infty} \|f\|_p = \infty = \|f\|_\infty$.
:::
