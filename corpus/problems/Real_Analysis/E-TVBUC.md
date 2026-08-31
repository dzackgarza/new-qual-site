---
schema: qual/card@1
id: E-TVBUC
kind: exercise
title: $\lim_{p\to\infty}\|f\|_p=\|f\|_\infty$ on a finite-measure space
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
Show that if $E \subseteq \mathbb{R}^n$ is a measurable set with finite measure $\mu(E) < \infty$, then for any measurable function $f: E \to \mathbb{C}$,
$$
\lim_{p \to \infty} \|f\|_{L^p(E)} = \|f\|_{L^\infty(E)}.
$$
:::

::: solution
**Goal:** Prove that on a set $E \subseteq \mathbb{R}^n$ with $\mu(E) < \infty$, $\lim_{p \to \infty} \|f\|_{L^p(E)} = \|f\|_{L^\infty(E)}$.

<1>1. Upper bound: $\limsup_{p \to \infty} \|f\|_{L^p(E)} \le \|f\|_{L^\infty(E)}$.
    *Proof:*
    <2>1. If $\|f\|_{L^\infty(E)} = \infty$, the upper bound holds vacuously.
    <2>2. If $\mu(E) = 0$, then $\|f\|_{L^p(E)} = 0$ for all $p$ and $\|f\|_{L^\infty(E)} = 0$, so the limit is trivially 0.
    <2>3. Assume $\|f\|_{L^\infty(E)} < \infty$ and $0 < \mu(E) < \infty$.
    <2>4. For almost every $x \in E$, $|f(x)| \le \|f\|_{L^\infty(E)}$.
    <2>5. Integrating over $E$:
    $$\|f\|_{L^p(E)} = \left( \int_E |f(x)|^p \, d\mu \right)^{1/p} \le \left( \int_E \|f\|_{L^\infty(E)}^p \, d\mu \right)^{1/p} = \|f\|_{L^\infty(E)} (\mu(E))^{1/p}.$$
    <2>6. Since $\mu(E) \in (0, \infty)$, $\lim_{p \to \infty} (\mu(E))^{1/p} = 1$.
    <2>7. Taking the limit superior as $p \to \infty$:
    $$\limsup_{p \to \infty} \|f\|_{L^p(E)} \le \|f\|_{L^\infty(E)} \lim_{p \to \infty} (\mu(E))^{1/p} = \|f\|_{L^\infty(E)}.$$

<1>2. Lower bound: $\liminf_{p \to \infty} \|f\|_{L^p(E)} \ge \|f\|_{L^\infty(E)}$.
    *Proof:*
    <2>1. If $\|f\|_{L^\infty(E)} = 0$, then $f = 0$ almost everywhere, so $\|f\|_{L^p(E)} = 0$ for all $p \ge 1$ and the inequality holds trivially.
    <2>2. Assume $\|f\|_{L^\infty(E)} > 0$. For any real number $M$ with $0 < M < \|f\|_{L^\infty(E)}$, define the superlevel set
    $$A_M = \{x \in E : |f(x)| > M\}.$$
    <2>3. By definition of the essential supremum, $\mu(A_M) > 0$.
    <2>4. Restricting the integral to $A_M$:
    $$\|f\|_{L^p(E)} = \left( \int_E |f(x)|^p \, d\mu \right)^{1/p} \ge \left( \int_{A_M} |f(x)|^p \, d\mu \right)^{1/p} \ge \left( \int_{A_M} M^p \, d\mu \right)^{1/p} = M (\mu(A_M))^{1/p}.$$
    <2>5. Since $\mu(A_M) \in (0, \infty)$, $\lim_{p \to \infty} (\mu(A_M))^{1/p} = 1$.
    <2>6. Taking the limit inferior as $p \to \infty$:
    $$\liminf_{p \to \infty} \|f\|_{L^p(E)} \ge M \lim_{p \to \infty} (\mu(A_M))^{1/p} = M.$$
    <2>7. If $\|f\|_{L^\infty(E)} < \infty$, taking the supremum over all $M < \|f\|_{L^\infty(E)}$ yields $\liminf_{p \to \infty} \|f\|_{L^p(E)} \ge \|f\|_{L^\infty(E)}$.
    <2>8. If $\|f\|_{L^\infty(E)} = \infty$, the bound holds for all $M > 0$, so $\lim_{p \to \infty} \|f\|_{L^p(E)} = \infty = \|f\|_{L^\infty(E)}$.

<1>3. Conclusion:
    *Proof:*
    Combining <1>1 and <1>2 gives $\lim_{p \to \infty} \|f\|_{L^p(E)} = \|f\|_{L^\infty(E)}$.
:::
