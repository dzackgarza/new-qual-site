---
schema: qual/card@1
id: P-JMOGT
kind: problem
title: $\lim_{x\to 0}\int_{\RR}|f(y-x)-f(y)|\,dy=0$ for $f\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Continuity
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the TAMU Real Variables qualifying examination dated August 7, 2016, in the preserved Texas solution compilation.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Existing solution is correct; it improves on the preserved source by using uniform continuity of a compactly supported continuous approximant rather than an inapplicable appeal to Dini's theorem. Normalized the solution block so repository tooling recognizes the card as solved.
---

::: {.problem}
Let $f \in L^1(\mathbb{R})$. Show that
$$
\lim_{x \to 0} \int_{\mathbb{R}} |f(y - x) - f(y)| \, dy = 0.
$$
:::

::: {.solution}
**Goal:** Prove the continuity of translations in $L^1(\mathbb{R})$ using the density of $C_c(\mathbb{R})$ in $L^1(\mathbb{R})$ and the uniform continuity of compactly supported continuous functions.

::: pf

::: {.pf-step #s1}
Approximation by compactly supported continuous functions:

::: pf-proof

::: pf-step
Let $\varepsilon > 0$.
:::

::: pf-step
Since $C_c(\mathbb{R})$ (continuous functions with compact support) is dense in $L^1(\mathbb{R})$, there exists a function $g \in C_c(\mathbb{R})$ such that
$$\|f - g\|_{L^1} = \int_{\mathbb{R}} |f(y) - g(y)| \, dy < \frac{\varepsilon}{3}.$$
:::

::: pf-step
Since $g$ has compact support, choose $M > 0$ such that $\operatorname{supp}(g) \subseteq [-M, M]$.
:::

:::

:::

::: {.pf-step #s2}
Translation invariance of the $L^1$ norm:

::: pf-proof

::: pf-step
For any $x \in \mathbb{R}$, by the translation invariance of the Lebesgue integral (substituting $u = y - x$):
$$\int_{\mathbb{R}} |f(y - x) - g(y - x)| \, dy = \int_{\mathbb{R}} |f(u) - g(u)| \, du = \|f - g\|_{L^1} < \frac{\varepsilon}{3}.$$
:::

:::

:::

::: {.pf-step #s3}
Splitting the integral via the triangle inequality:

::: pf-proof

::: pf-step
For any $x \in \mathbb{R}$:
$$|f(y - x) - f(y)| \le |f(y - x) - g(y - x)| + |g(y - x) - g(y)| + |g(y) - f(y)|.$$
:::

::: pf-step
Integrating over $\mathbb{R}$ and applying step [](#s1){.pf-ref} and step [](#s2){.pf-ref}:
$$\int_{\mathbb{R}} |f(y - x) - f(y)| \, dy \le \frac{\varepsilon}{3} + \int_{\mathbb{R}} |g(y - x) - g(y)| \, dy + \frac{\varepsilon}{3} = \frac{2\varepsilon}{3} + \int_{\mathbb{R}} |g(y - x) - g(y)| \, dy.$$
:::

:::

:::

::: {.pf-step #s4}
Bounding the translation error for $g$:

::: pf-proof

::: pf-step
Since $g$ is continuous with compact support on $\mathbb{R}$, $g$ is uniformly continuous on $\mathbb{R}$.
:::

::: pf-step
For any $|x| \le 1$, if $y \notin [-M - 1, M + 1]$, then $y \notin [-M, M]$ and $y - x \notin [-M, M]$, so $g(y) = 0$ and $g(y - x) = 0$.
:::

::: pf-step
Thus $\operatorname{supp}(g(\cdot - x) - g(\cdot)) \subseteq [-M - 1, M + 1]$ for all $|x| \le 1$.
:::

::: pf-step
By uniform continuity, there exists $\delta \in (0, 1)$ such that for all $|x| < \delta$ and all $y \in \mathbb{R}$:
$$|g(y - x) - g(y)| < \frac{\varepsilon}{3(2M + 2)}.$$
:::

::: pf-step
Integrating over $[-M - 1, M + 1]$:
$$\int_{\mathbb{R}} |g(y - x) - g(y)| \, dy = \int_{-M - 1}^{M + 1} |g(y - x) - g(y)| \, dy \le \frac{\varepsilon}{3(2M + 2)} \cdot (2M + 2) = \frac{\varepsilon}{3}.$$
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof

::: pf-step
For all $|x| < \delta$, combining step [](#s3){.pf-ref} and step [](#s4){.pf-ref}:
$$\int_{\mathbb{R}} |f(y - x) - f(y)| \, dy < \frac{2\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$
:::

::: pf-step
Since $\varepsilon > 0$ was arbitrary, $\lim_{x \to 0} \int_{\mathbb{R}} |f(y - x) - f(y)| \, dy = 0$.
:::

:::

:::

:::
:::
