---
schema: qual/card@1
id: P-KH5ZV
kind: problem
title: Absolute continuity of $\int_E\abs{f}$ for $f\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - L¹
  - Measure Theory
relations: []
review: draft
---

::: {.problem}
Let $f \in L^1(\RR)$. Prove that for every $\varepsilon > 0$, there exists $\delta > 0$ such that for every Lebesgue measurable set $E \subseteq \RR$ with $m(E) < \delta$,
$$
\int_E \abs{f(x)} \, dx < \varepsilon.
$$
:::

::: {.solution}
**Goal:** Prove the absolute continuity of the Lebesgue integral by truncating $\abs{f}$ by height $N$ and applying the Monotone Convergence Theorem.

::: pf

::: pf-step
Pointwise convergence and monotonicity of truncations:

::: pf-proof

::: pf-step
For each integer $N \ge 1$, define the truncated function:
$$f_N(x) = \min(\abs{f(x)}, N) = \begin{cases} \abs{f(x)} & \text{if } \abs{f(x)} \le N, \\ N & \text{if } \abs{f(x)} > N. \end{cases}$$

:::

::: pf-step
For every $x \in \RR$, $0 \le f_N(x) \le f_{N+1}(x)$ and $\lim_{N \to \infty} f_N(x) = \abs{f(x)}$.

:::

::: pf-step
Each $f_N$ is measurable and bounded by $N$.

:::

:::

:::

::: {.pf-step #s2}
Approximation of $\abs{f}$ by $f_N$ in $L^1(\RR)$:

::: pf-proof

::: pf-step
By the Monotone Convergence Theorem:
$$\lim_{N \to \infty} \int_{\RR} f_N(x) \, dx = \int_{\RR} \abs{f(x)} \, dx.$$

:::

::: pf-step
Since $f \in L^1(\RR)$, $\int_{\RR} \abs{f(x)} \, dx < \infty$.

:::

::: pf-step
Thus:
$$\lim_{N \to \infty} \int_{\RR} (\abs{f(x)} - f_N(x)) \, dx = \int_{\RR} \abs{f(x)} \, dx - \lim_{N \to \infty} \int_{\RR} f_N(x) \, dx = 0.$$

:::

::: pf-step
Let $\varepsilon > 0$. There exists an integer $N_0 \ge 1$ such that
$$\int_{\RR} (\abs{f(x)} - f_{N_0}(x)) \, dx < \frac{\varepsilon}{2}.$$

:::

:::

:::

::: pf-step
Choice of $\delta > 0$ and integration bound:

::: pf-proof

::: pf-step
Define $\delta = \frac{\varepsilon}{2 N_0} > 0$.

:::

::: pf-step
Let $E \subseteq \RR$ be any measurable set with $m(E) < \delta$.

:::

::: pf-step
Decompose the integral over $E$:
$$\int_E \abs{f(x)} \, dx = \int_E (\abs{f(x)} - f_{N_0}(x)) \, dx + \int_E f_{N_0}(x) \, dx.$$

:::

::: pf-step
Bound the first term using non-negativity and step [](#s2){.pf-ref}:
$$\int_E (\abs{f(x)} - f_{N_0}(x)) \, dx \le \int_{\RR} (\abs{f(x)} - f_{N_0}(x)) \, dx < \frac{\varepsilon}{2}.$$

:::

::: pf-step
Bound the second term using the bound $0 \le f_{N_0}(x) \le N_0$:
$$\int_E f_{N_0}(x) \, dx \le \int_E N_0 \, dx = N_0 \cdot m(E) < N_0 \cdot \delta = N_0 \cdot \frac{\varepsilon}{2 N_0} = \frac{\varepsilon}{2}.$$

:::

::: pf-step
Combining the two estimates:
$$\int_E \abs{f(x)} \, dx < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
For any $\varepsilon > 0$, choosing $\delta = \frac{\varepsilon}{2 N_0}$ ensures $\int_E \abs{f} < \varepsilon$ whenever $m(E) < \delta$.
:::

:::

:::

:::

