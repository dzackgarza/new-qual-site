---
schema: qual/card@1
id: E-TVBUC
kind: problem
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

::: {.exercise}
Show that if $E \subseteq \mathbb{R}^n$ is a measurable set with finite measure $\mu(E) < \infty$, then for any measurable function $f: E \to \mathbb{C}$,
$$
\lim_{p \to \infty} \|f\|_{L^p(E)} = \|f\|_{L^\infty(E)}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
Upper bound: $\limsup_{p \to \infty} \|f\|_{L^p(E)} \le \|f\|_{L^\infty(E)}$.

::: pf-proof

::: pf-step
If $\|f\|_{L^\infty(E)} = \infty$, the upper bound holds vacuously.

:::

::: pf-step
If $\mu(E) = 0$, then $\|f\|_{L^p(E)} = 0$ for all $p$ and $\|f\|_{L^\infty(E)} = 0$, so the limit is $0$.

:::

::: pf-step
Assume $\|f\|_{L^\infty(E)} < \infty$ and $0 < \mu(E) < \infty$.

:::

::: pf-step
For almost every $x \in E$, $|f(x)| \le \|f\|_{L^\infty(E)}$.

:::

::: pf-step
Integrating over $E$:
$$\|f\|_{L^p(E)} = \left( \int_E |f(x)|^p \, d\mu \right)^{1/p} \le \left( \int_E \|f\|_{L^\infty(E)}^p \, d\mu \right)^{1/p} = \|f\|_{L^\infty(E)} (\mu(E))^{1/p}.$$

:::

::: pf-step
Since $\mu(E) \in (0, \infty)$, $\lim_{p \to \infty} (\mu(E))^{1/p} = 1$.

:::

::: pf-step
Taking the limit superior as $p \to \infty$:
$$\limsup_{p \to \infty} \|f\|_{L^p(E)} \le \|f\|_{L^\infty(E)} \lim_{p \to \infty} (\mu(E))^{1/p} = \|f\|_{L^\infty(E)}.$$

:::

:::

:::

::: {.pf-step #s2}
Lower bound: $\liminf_{p \to \infty} \|f\|_{L^p(E)} \ge \|f\|_{L^\infty(E)}$.

::: pf-proof

::: pf-step
If $\|f\|_{L^\infty(E)} = 0$, then $f = 0$ almost everywhere, so $\|f\|_{L^p(E)} = 0$ for all $p \ge 1$ and the inequality holds.

:::

::: pf-step
Assume $\|f\|_{L^\infty(E)} > 0$. For any real number $M$ with $0 < M < \|f\|_{L^\infty(E)}$, define the superlevel set
$$A_M = \{x \in E : |f(x)| > M\}.$$

:::

::: pf-step
By definition of the essential supremum, $\mu(A_M) > 0$.

:::

::: pf-step
Restricting the integral to $A_M$:
$$\|f\|_{L^p(E)} = \left( \int_E |f(x)|^p \, d\mu \right)^{1/p} \ge \left( \int_{A_M} |f(x)|^p \, d\mu \right)^{1/p} \ge \left( \int_{A_M} M^p \, d\mu \right)^{1/p} = M (\mu(A_M))^{1/p}.$$

:::

::: pf-step
Since $\mu(A_M) \in (0, \infty)$, $\lim_{p \to \infty} (\mu(A_M))^{1/p} = 1$.

:::

::: pf-step
Taking the limit inferior as $p \to \infty$:
$$\liminf_{p \to \infty} \|f\|_{L^p(E)} \ge M \lim_{p \to \infty} (\mu(A_M))^{1/p} = M.$$

:::

::: pf-step
If $\|f\|_{L^\infty(E)} < \infty$, taking the supremum over all $M < \|f\|_{L^\infty(E)}$ yields $\liminf_{p \to \infty} \|f\|_{L^p(E)} \ge \|f\|_{L^\infty(E)}$.

:::

::: pf-step
If $\|f\|_{L^\infty(E)} = \infty$, the bound holds for all $M > 0$, so $\lim_{p \to \infty} \|f\|_{L^p(E)} = \infty = \|f\|_{L^\infty(E)}$.

:::

:::

:::

::: pf-qed
Combining steps [](#s1){.pf-ref} and [](#s2){.pf-ref} gives $\lim_{p \to \infty} \|f\|_{L^p(E)} = \|f\|_{L^\infty(E)}$.
:::

:::

:::
