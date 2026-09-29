---
schema: qual/card@1
id: P-7QVGF
kind: problem
title: Continuity of translation in $L^1$ for $f\in C_c(\RR)$, and $L^1$-boundedness
  and convergence of the averages $\mathcal{A}_h f$
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - L¹
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 5 of the official UGA August 2019 Real Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Reviewed the translation-continuity and averaging-operator arguments; clarified the uniform-continuity justification for compactly supported continuous functions.
---

::: {.problem}
(a) Show that if $f \in C_c(\mathbb{R})$ is continuous with compact support on $\mathbb{R}$, then
$$
\lim_{y \to 0} \int_{\mathbb{R}} |f(x - y) - f(x)| \, dx = 0.
$$

(b) Let $f \in L^1(\mathbb{R})$, and for each $h > 0$ define the local average
$$
\mathcal{A}_h f(x) = \frac{1}{2h} \int_{|y| \le h} f(x - y) \, dy.
$$
- Prove that $\|\mathcal{A}_h f\|_{L^1(\mathbb{R})} \le \|f\|_{L^1(\mathbb{R})}$ for all $h > 0$.
- Prove that $\lim_{h \to 0^+} \|\mathcal{A}_h f - f\|_{L^1(\mathbb{R})} = 0$.
:::

::: {.solution}
**Goal:** Prove continuity of translations for $C_c(\mathbb{R})$ functions in (a), and use it along with density in $L^1(\mathbb{R})$ to prove boundedness and $L^1$ convergence of the rolling averages $\mathcal{A}_h f$ in (b).

::: pf

::: pf-step
Part (a): $\lim_{y \to 0} \|\tau_y f - f\|_{L^1} = 0$ for $f \in C_c(\mathbb{R})$.

::: pf-proof

::: pf-step
Since $f$ has compact support, there exists $M > 0$ such that $\operatorname{supp}(f) \subseteq [-M, M]$.

:::

::: pf-step
For any $|y| \le 1$, if $x \notin [-M - 1, M + 1]$, then both $x \notin [-M, M]$ and $x - y \notin [-M, M]$, so $f(x - y) - f(x) = 0 - 0 = 0$.

:::

::: pf-step
Thus $\operatorname{supp}(\tau_y f - f) \subseteq [-M - 1, M + 1]$ for all $|y| \le 1$.

:::

::: pf-step
Since $f \in C_c(\mathbb{R})$, $f$ is uniformly continuous on $\mathbb{R}$.
Indeed, if $\operatorname{supp}(f)\subset[-M,M]$, apply Heine--Cantor on the compact interval $[-M-1,M+1]$; outside that interval, sufficiently nearby points both lie outside the support and $f$ vanishes.

:::

::: pf-step
Let $\varepsilon > 0$. By uniform continuity, there exists $\delta \in (0, 1)$ such that $|y| < \delta$ implies
$$|f(x - y) - f(x)| < \frac{\varepsilon}{2(M + 1)} \quad \text{for all } x \in \mathbb{R}.$$

:::

::: pf-step
For any $|y| < \delta$:
$$\int_\mathbb{R} |f(x - y) - f(x)| \, dx = \int_{-M-1}^{M+1} |f(x - y) - f(x)| \, dx \le \int_{-M-1}^{M+1} \frac{\varepsilon}{2(M + 1)} \, dx = \varepsilon.$$

:::

::: pf-step
Thus $\lim_{y \to 0} \int_\mathbb{R} |f(x - y) - f(x)| \, dx = 0$.

:::

:::

:::

::: pf-step
Part (b), Subpart 1: $\|\mathcal{A}_h f\|_{L^1} \le \|f\|_{L^1}$ for all $h > 0$.

::: pf-proof

::: pf-step
Write out the $L^1$ norm:
$$\|\mathcal{A}_h f\|_{L^1} = \int_\mathbb{R} \left| \frac{1}{2h} \int_{-h}^h f(x - y) \, dy \right| dx.$$

:::

::: pf-step
Apply the integral triangle inequality:
$$\|\mathcal{A}_h f\|_{L^1} \le \frac{1}{2h} \int_\mathbb{R} \left( \int_{-h}^h |f(x - y)| \, dy \right) dx.$$

:::

::: pf-step
By Tonelli's Theorem, interchange the order of integration:
$$\|\mathcal{A}_h f\|_{L^1} \le \frac{1}{2h} \int_{-h}^h \left( \int_\mathbb{R} |f(x - y)| \, dx \right) dy.$$

:::

::: pf-step
By translation invariance of Lebesgue measure, $\int_\mathbb{R} |f(x - y)| \, dx = \|f\|_{L^1}$ for each fixed $y$.

:::

::: pf-step
Thus
$$\|\mathcal{A}_h f\|_{L^1} \le \frac{1}{2h} \int_{-h}^h \|f\|_{L^1} \, dy = \frac{1}{2h} (2h) \|f\|_{L^1} = \|f\|_{L^1}.$$

:::

:::

:::

::: {.pf-step #s3}
Part (b), Lemma: Continuity of translations in $L^1(\mathbb{R})$ for all $f \in L^1(\mathbb{R})$.

::: pf-proof

::: pf-step
Let $f \in L^1(\mathbb{R})$ and $\varepsilon > 0$.

:::

::: pf-step
Since $C_c(\mathbb{R})$ is dense in $L^1(\mathbb{R})$, choose $g \in C_c(\mathbb{R})$ such that $\|f - g\|_{L^1} < \varepsilon / 3$.

:::

::: pf-step
By translation invariance of the $L^1$ norm, $\|\tau_y f - \tau_y g\|_{L^1} = \|f - g\|_{L^1} < \varepsilon / 3$ for all $y \in \mathbb{R}$.

:::

::: pf-step
By Part (a), choose $\delta > 0$ such that $|y| < \delta \implies \|\tau_y g - g\|_{L^1} < \varepsilon / 3$.

:::

::: pf-step
By the triangle inequality, for all $|y| < \delta$:
$$\|\tau_y f - f\|_{L^1} \le \|\tau_y f - \tau_y g\|_{L^1} + \|\tau_y g - g\|_{L^1} + \|g - f\|_{L^1} < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$

:::

::: pf-step
Thus $\lim_{y \to 0} \|\tau_y f - f\|_{L^1} = 0$ for all $f \in L^1(\mathbb{R})$.

:::

:::

:::

::: pf-step
Part (b), Subpart 2: $\lim_{h \to 0^+} \|\mathcal{A}_h f - f\|_{L^1} = 0$.

::: pf-proof

::: pf-step
Using $\frac{1}{2h} \int_{-h}^h 1 \, dy = 1$, write
$$\mathcal{A}_h f(x) - f(x) = \frac{1}{2h} \int_{-h}^h (f(x - y) - f(x)) \, dy.$$

:::

::: pf-step
Take the $L^1$ norm and apply Tonelli's Theorem:
$$\|\mathcal{A}_h f - f\|_{L^1} \le \frac{1}{2h} \int_{-h}^h \left( \int_\mathbb{R} |f(x - y) - f(x)| \, dx \right) dy = \frac{1}{2h} \int_{-h}^h \|\tau_y f - f\|_{L^1} \, dy.$$

:::

::: pf-step
Bound the average by the supremum on $[-h, h]$:
$$\|\mathcal{A}_h f - f\|_{L^1} \le \sup_{|y| \le h} \|\tau_y f - f\|_{L^1}.$$

:::

::: pf-step
By step [](#s3){.pf-ref}, $\lim_{h \to 0^+} \sup_{|y| \le h} \|\tau_y f - f\|_{L^1} = 0$.

:::

::: pf-step
Therefore $\lim_{h \to 0^+} \|\mathcal{A}_h f - f\|_{L^1} = 0$.

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$C_c(\mathbb{R})$ functions have continuous translations, $\mathcal{A}_h$ is an $L^1$-contraction ($\|\mathcal{A}_h f\|_1 \le \|f\|_1$), and $\mathcal{A}_h f \to f$ in $L^1(\mathbb{R})$ as $h \to 0^+$.
:::

:::

:::

:::
