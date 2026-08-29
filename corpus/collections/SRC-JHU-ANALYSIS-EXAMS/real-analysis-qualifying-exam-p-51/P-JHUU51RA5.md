---
schema: qual/card@1
id: P-JHUU51RA5
kind: problem
title: "L^p norms increase to the L^infinity norm"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space, and let $f \in L^{1}(\mu) \cap L^{\infty}(\mu)$.
Prove that:
$$
\lim_{p \to \infty} \|f\|_p = \|f\|_{\infty}.
$$
:::

::: solution
**Goal:** Prove that for $f \in L^1(\mu) \cap L^\infty(\mu)$, $\lim_{p \to \infty} \|f\|_p = \|f\|_\infty$ using the squeeze theorem with upper and lower bounds.

<1>1. Trivial Case $\|f\|_\infty = 0$:
    *Proof:*
    <2>1. If $\|f\|_\infty = 0$, then $f = 0$ almost everywhere.
    <2>2. For every $p \ge 1$, $\|f\|_p = 0$.
    <2>3. Thus $\lim_{p \to \infty} \|f\|_p = 0 = \|f\|_\infty$.
    <2>4. Henceforth, assume $M \coloneqq \|f\|_\infty > 0$.

<1>2. Upper Bound ($\limsup_{p \to \infty} \|f\|_p \le \|f\|_\infty$):
    *Proof:*
    <2>1. For any $p > 1$:
        $$\int_X |f|^p \, d\mu = \int_X |f|^{p-1} |f| \, d\mu \le \int_X \|f\|_\infty^{p-1} |f| \, d\mu = \|f\|_\infty^{p-1} \|f\|_1.$$
    <2>2. Taking the $p$-th root on both sides:
        $$\|f\|_p = \left( \int_X |f|^p \, d\mu \right)^{1/p} \le \left( \|f\|_\infty^{p-1} \|f\|_1 \right)^{1/p} = \|f\|_\infty^{\frac{p-1}{p}} \|f\|_1^{1/p}.$$
    <2>3. Taking the limit superior as $p \to \infty$:
        - $\lim_{p \to \infty} \frac{p-1}{p} = 1 \implies \lim_{p \to \infty} \|f\|_\infty^{\frac{p-1}{p}} = \|f\|_\infty$.
        - Since $f \in L^1(\mu)$ and $\|f\|_\infty > 0$, $0 < \|f\|_1 < \infty$, so $\lim_{p \to \infty} \|f\|_1^{1/p} = 1$.
    <2>4. Therefore:
        $$\limsup_{p \to \infty} \|f\|_p \le \|f\|_\infty \cdot 1 = \|f\|_\infty.$$

<1>3. Lower Bound ($\liminf_{p \to \infty} \|f\|_p \ge \|f\|_\infty$):
    *Proof:*
    <2>1. Let $\varepsilon \in (0, \|f\|_\infty)$ be arbitrary.
    <2>2. Define the measurable set $E_\varepsilon \coloneqq \{ x \in X \mid |f(x)| > \|f\|_\infty - \varepsilon \}$.
    <2>3. By definition of the essential supremum $\|f\|_\infty$, we have $\mu(E_\varepsilon) > 0$.
    <2>4. Furthermore, since $f \in L^1(\mu)$:
        $$\|f\|_1 \ge \int_{E_\varepsilon} |f| \, d\mu \ge (\|f\|_\infty - \varepsilon) \mu(E_\varepsilon) \implies \mu(E_\varepsilon) \le \frac{\|f\|_1}{\|f\|_\infty - \varepsilon} < \infty.$$
    <2>5. We bound the $L^p$ norm from below by integrating over $E_\varepsilon$:
        $$\|f\|_p = \left( \int_X |f|^p \, d\mu \right)^{1/p} \ge \left( \int_{E_\varepsilon} |f|^p \, d\mu \right)^{1/p} \ge \left( (\|f\|_\infty - \varepsilon)^p \mu(E_\varepsilon) \right)^{1/p} = (\|f\|_\infty - \varepsilon) (\mu(E_\varepsilon))^{1/p}.$$
    <2>6. Since $0 < \mu(E_\varepsilon) < \infty$, we have $\lim_{p \to \infty} (\mu(E_\varepsilon))^{1/p} = 1$.
    <2>7. Taking the limit inferior as $p \to \infty$:
        $$\liminf_{p \to \infty} \|f\|_p \ge (\|f\|_\infty - \varepsilon) \cdot 1 = \|f\|_\infty - \varepsilon.$$
    <2>8. Since this holds for every $\varepsilon > 0$, taking $\varepsilon \to 0^+$ gives:
        $$\liminf_{p \to \infty} \|f\|_p \ge \|f\|_\infty.$$

<1>4. Conclusion:
    Combining the upper and lower bounds:
    $$\|f\|_\infty \le \liminf_{p \to \infty} \|f\|_p \le \limsup_{p \to \infty} \|f\|_p \le \|f\|_\infty \implies \lim_{p \to \infty} \|f\|_p = \|f\|_\infty.$$
    Q.E.D.
:::
