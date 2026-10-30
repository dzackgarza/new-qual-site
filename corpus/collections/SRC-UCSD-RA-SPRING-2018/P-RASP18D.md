---
schema: qual/card@1
id: P-RASP18D
kind: problem
title: "Riemann-Lebesgue lemma for derivatives of dilated functions"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Spring 2018 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing integration-by-parts and density proof reviewed as correct; normalized the legacy solution block.
---

::: {.problem}
Let $\varphi : \RR \to \RR$ be a $C^1$-function such that $M := \sup_{x \in \RR} [\abs{\varphi(x)} + \abs{\varphi'(x)}] < \infty$.

1. If $f \in C_c^1(\RR)$, show
$$
\abs{\int_{\RR} f(x) \varphi'(\lambda x)\,dx} \leq M \cdot \norm{f'}_{L^1(\RR, m)} \abs{\lambda}^{-1} \quad \text{for all } \lambda > 0.
$$

2. If $f \in L^1(\RR, m)$, show
$$
\lim_{\lambda \to \infty} \int_{\RR} f(x) \varphi'(\lambda x)\,dx = 0.
$$
:::

::: {.solution}

::: pf

::: pf-step
Part 1: Bound for $f \in C_c^1(\RR)$ via integration by parts:

::: pf-proof

::: pf-step
Since $f \in C_c^1(\RR)$, $f$ and $f'$ have compact support contained in some interval $[-R, R]$.
Using integration by parts with $u = f(x)$ and $dv = \varphi'(\lambda x)\,dx$ (so $v = \frac{1}{\lambda} \varphi(\lambda x)$):
$$
\int_{-\infty}^\infty f(x) \varphi'(\lambda x) \, dx = \left[ \frac{1}{\lambda} f(x) \varphi(\lambda x) \right]_{-\infty}^\infty - \frac{1}{\lambda} \int_{-\infty}^\infty f'(x) \varphi(\lambda x) \, dx.
$$
:::

::: pf-step
The boundary term vanishes because $f(x) = 0$ outside $[-R, R]$ and $\varphi$ is bounded:
$$
\left[ \frac{1}{\lambda} f(x) \varphi(\lambda x) \right]_{-\infty}^\infty = 0.
$$
:::

::: pf-step
Taking absolute values and using $\abs{\varphi(y)} \le M$:
$$
\abs{ \int_{-\infty}^\infty f(x) \varphi'(\lambda x) \, dx } \le \frac{1}{\lambda} \int_{-\infty}^\infty \abs{f'(x)} \abs{\varphi(\lambda x)} \, dx \le \frac{M}{\lambda} \int_{-\infty}^\infty \abs{f'(x)} \, dx = M \norm{f'}_{L^1(\RR)} \lambda^{-1}.
$$
:::

:::

:::

::: pf-step
Part 2: Limit for $f \in L^1(\RR)$ via density of $C_c^1(\RR)$:

::: pf-proof

::: pf-step
Let $\varepsilon > 0$ be given.
By the density of $C_c^1(\RR)$ in $L^1(\RR)$, there exists a function $g \in C_c^1(\RR)$ such that:
$$
\norm{f - g}_{L^1(\RR)} < \frac{\varepsilon}{2M}.
$$
:::

::: pf-step
For any $\lambda > 0$, decompose the integral:
$$
\int_\RR f(x) \varphi'(\lambda x) \, dx = \int_\RR (f(x) - g(x)) \varphi'(\lambda x) \, dx + \int_\RR g(x) \varphi'(\lambda x) \, dx.
$$
:::

::: pf-step
Bound the approximation error:
$$
\abs{ \int_\RR (f(x) - g(x)) \varphi'(\lambda x) \, dx } \le \sup_{y \in \RR} \abs{\varphi'(y)} \norm{f - g}_{L^1} \le M \cdot \frac{\varepsilon}{2M} = \frac{\varepsilon}{2}.
$$
:::

::: pf-step
By Part 1, for the $C_c^1$ function $g$:
$$
\abs{ \int_\RR g(x) \varphi'(\lambda x) \, dx } \le \frac{M \norm{g'}_{L^1}}{\lambda}.
$$
Choosing $\Lambda = \frac{2 M \norm{g'}_{L^1}}{\varepsilon}$, for all $\lambda > \Lambda$ we have:
$$
\abs{ \int_\RR g(x) \varphi'(\lambda x) \, dx } < \frac{\varepsilon}{2}.
$$
:::

::: pf-step
Combining bounds for all $\lambda > \Lambda$:
$$
\abs{ \int_\RR f(x) \varphi'(\lambda x) \, dx } \le \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
$$
Since $\varepsilon > 0$ was arbitrary, $\lim_{\lambda \to \infty} \int_\RR f(x) \varphi'(\lambda x) \, dx = 0$.
:::

:::

:::

::: pf-qed
Conclusion:
Both parts 1 and 2 are proven.
:::

:::
:::
