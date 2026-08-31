---
schema: qual/card@1
id: E-BQBZI
kind: exercise
title: $\|f\|_p\to\|f\|_\infty$ as $p\to\infty$ on finite measure spaces
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
Show that if $X \subseteq \mathbb{R}$ is a measurable set with finite measure $\mu(X) < \infty$, then for any measurable function $f: X \to \mathbb{C}$,
$$
\lim_{p \to \infty} \|f\|_{L^p(X)} = \|f\|_{L^\infty(X)}.
$$
:::

::: solution
**Goal:** Prove that on a finite measure space $(X, \mu)$ with $\mu(X) < \infty$, $\lim_{p \to \infty} \|f\|_{L^p(X)} = \|f\|_{L^\infty(X)}$ for any measurable function $f$.

<1>1. Upper bound: $\limsup_{p \to \infty} \|f\|_{L^p} \le \|f\|_{L^\infty}$.
    *Proof:*
    <2>1. If $\|f\|_{L^\infty} = \infty$, the upper bound $\limsup_{p \to \infty} \|f\|_{L^p} \le \infty$ holds vacuously.
    <2>2. If $\mu(X) = 0$, then $\|f\|_{L^p} = 0$ for all $p$ and $\|f\|_{L^\infty} = 0$, so the limit is trivially 0.
    <2>3. Assume $\|f\|_{L^\infty} < \infty$ and $0 < \mu(X) < \infty$.
    <2>4. For almost every $x \in X$, $|f(x)| \le \|f\|_{L^\infty}$.
    <2>5. Integrating over $X$:
    $$\|f\|_{L^p} = \left( \int_X |f(x)|^p \, d\mu \right)^{1/p} \le \left( \int_X \|f\|_{L^\infty}^p \, d\mu \right)^{1/p} = \|f\|_{L^\infty} (\mu(X))^{1/p}.$$
    <2>6. Since $\mu(X) \in (0, \infty)$, $\lim_{p \to \infty} (\mu(X))^{1/p} = 1$.
    <2>7. Taking the limit superior as $p \to \infty$:
    $$\limsup_{p \to \infty} \|f\|_{L^p} \le \|f\|_{L^\infty} \lim_{p \to \infty} (\mu(X))^{1/p} = \|f\|_{L^\infty}.$$

<1>2. Lower bound: $\liminf_{p \to \infty} \|f\|_{L^p} \ge \|f\|_{L^\infty}$.
    *Proof:*
    <2>1. If $\|f\|_{L^\infty} = 0$, then $f = 0$ almost everywhere, so $\|f\|_{L^p} = 0$ for all $p \ge 1$ and the inequality holds trivially.
    <2>2. Assume $\|f\|_{L^\infty} > 0$. For any real number $\alpha$ satisfying $0 < \alpha < \|f\|_{L^\infty}$, define the superlevel set
    $$A_\alpha = \{x \in X : |f(x)| \ge \alpha\}.$$
    <2>3. By definition of the essential supremum, $\mu(A_\alpha) > 0$.
    <2>4. Restricting the integral to $A_\alpha$:
    $$\|f\|_{L^p} = \left( \int_X |f(x)|^p \, d\mu \right)^{1/p} \ge \left( \int_{A_\alpha} |f(x)|^p \, d\mu \right)^{1/p} \ge \left( \int_{A_\alpha} \alpha^p \, d\mu \right)^{1/p} = \alpha (\mu(A_\alpha))^{1/p}.$$
    <2>5. Since $\mu(A_\alpha) \in (0, \infty)$, $\lim_{p \to \infty} (\mu(A_\alpha))^{1/p} = 1$.
    <2>6. Taking the limit inferior as $p \to \infty$:
    $$\liminf_{p \to \infty} \|f\|_{L^p} \ge \alpha \lim_{p \to \infty} (\mu(A_\alpha))^{1/p} = \alpha.$$
    <2>7. If $\|f\|_{L^\infty} < \infty$, taking the supremum over all $\alpha < \|f\|_{L^\infty}$ gives $\liminf_{p \to \infty} \|f\|_{L^p} \ge \|f\|_{L^\infty}$.
    <2>8. If $\|f\|_{L^\infty} = \infty$, the bound $\liminf_{p \to \infty} \|f\|_{L^p} \ge \alpha$ holds for arbitrarily large $\alpha > 0$, so $\lim_{p \to \infty} \|f\|_{L^p} = \infty = \|f\|_{L^\infty}$.

<1>3. Conclusion:
    *Proof:*
    Combining <1>1 and <1>2 gives $\lim_{p \to \infty} \|f\|_{L^p} = \|f\|_{L^\infty}$.
:::
