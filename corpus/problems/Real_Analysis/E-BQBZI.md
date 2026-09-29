---
schema: qual/card@1
id: E-BQBZI
kind: problem
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

::: {.exercise}
Show that if $X \subseteq \mathbb{R}$ is a measurable set with finite measure $\mu(X) < \infty$, then for any measurable function $f: X \to \mathbb{C}$,
$$
\lim_{p \to \infty} \|f\|_{L^p(X)} = \|f\|_{L^\infty(X)}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
Upper bound: $\limsup_{p \to \infty} \|f\|_{L^p} \le \|f\|_{L^\infty}$.

::: pf-proof

::: pf-step
If $\|f\|_{L^\infty} = \infty$, the upper bound $\limsup_{p \to \infty} \|f\|_{L^p} \le \infty$ holds vacuously.

:::

::: pf-step
If $\mu(X) = 0$, then $\|f\|_{L^p} = 0$ for all $p$ and $\|f\|_{L^\infty} = 0$, so the limit is $0$.

:::

::: pf-step
Assume $\|f\|_{L^\infty} < \infty$ and $0 < \mu(X) < \infty$.

:::

::: pf-step
For almost every $x \in X$, $|f(x)| \le \|f\|_{L^\infty}$.

:::

::: pf-step
Integrating over $X$:
$$\|f\|_{L^p} = \left( \int_X |f(x)|^p \, d\mu \right)^{1/p} \le \left( \int_X \|f\|_{L^\infty}^p \, d\mu \right)^{1/p} = \|f\|_{L^\infty} (\mu(X))^{1/p}.$$

:::

::: pf-step
Since $\mu(X) \in (0, \infty)$, $\lim_{p \to \infty} (\mu(X))^{1/p} = 1$.

:::

::: pf-step
Taking the limit superior as $p \to \infty$:
$$\limsup_{p \to \infty} \|f\|_{L^p} \le \|f\|_{L^\infty} \lim_{p \to \infty} (\mu(X))^{1/p} = \|f\|_{L^\infty}.$$

:::

:::

:::

::: {.pf-step #s2}
Lower bound: $\liminf_{p \to \infty} \|f\|_{L^p} \ge \|f\|_{L^\infty}$.

::: pf-proof

::: pf-step
If $\|f\|_{L^\infty} = 0$, then $f = 0$ almost everywhere, so $\|f\|_{L^p} = 0$ for all $p \ge 1$ and the inequality holds.

:::

::: pf-step
Assume $\|f\|_{L^\infty} > 0$. For any real number $\alpha$ satisfying $0 < \alpha < \|f\|_{L^\infty}$, define the superlevel set
$$A_\alpha = \{x \in X : |f(x)| \ge \alpha\}.$$

:::

::: pf-step
By definition of the essential supremum, $\mu(A_\alpha) > 0$.

:::

::: pf-step
Restricting the integral to $A_\alpha$:
$$\|f\|_{L^p} = \left( \int_X |f(x)|^p \, d\mu \right)^{1/p} \ge \left( \int_{A_\alpha} |f(x)|^p \, d\mu \right)^{1/p} \ge \left( \int_{A_\alpha} \alpha^p \, d\mu \right)^{1/p} = \alpha (\mu(A_\alpha))^{1/p}.$$

:::

::: pf-step
Since $\mu(A_\alpha) \in (0, \infty)$, $\lim_{p \to \infty} (\mu(A_\alpha))^{1/p} = 1$.

:::

::: pf-step
Taking the limit inferior as $p \to \infty$:
$$\liminf_{p \to \infty} \|f\|_{L^p} \ge \alpha \lim_{p \to \infty} (\mu(A_\alpha))^{1/p} = \alpha.$$

:::

::: pf-step
If $\|f\|_{L^\infty} < \infty$, taking the supremum over all $\alpha < \|f\|_{L^\infty}$ gives $\liminf_{p \to \infty} \|f\|_{L^p} \ge \|f\|_{L^\infty}$.

:::

::: pf-step
If $\|f\|_{L^\infty} = \infty$, the bound $\liminf_{p \to \infty} \|f\|_{L^p} \ge \alpha$ holds for arbitrarily large $\alpha > 0$, so $\lim_{p \to \infty} \|f\|_{L^p} = \infty = \|f\|_{L^\infty}$.

:::

:::

:::

::: pf-qed
Combining steps [](#s1){.pf-ref} and [](#s2){.pf-ref} gives $\lim_{p \to \infty} \|f\|_{L^p} = \|f\|_{L^\infty}$.
:::

:::

:::
