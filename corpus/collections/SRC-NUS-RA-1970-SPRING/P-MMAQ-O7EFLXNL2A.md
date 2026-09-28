---
schema: qual/card@1
id: P-MMAQ-O7EFLXNL2A
kind: problem
title: Layer-cake formula $\int f^p=\int_0^\infty p t^{p-1}\,m(\{f>t\})\,dt$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
If $f$ is a nonnegative measurable function on $\mathbb{R}$ and $p > 0$, show that $$\int f^p ~dx = \int_0^{\infty} p t^{p-1} \abs{\{x : f(x) > t\}} ~dt$$ where $\abs{\{x : f(x) > t\}}$ is the Lebesgue measure of the set $\{x : f(x) > t\}$.
:::

::: {.solution}
Both sides may equal $+\infty$. Write $\abs{\cdot}$ for Lebesgue measure and $\chi_{\{t < f(x)\}}$ for the indicator of $\{(x,t) \in \RR \times (0,\infty) : t < f(x)\}$.

<1>1. For every $x$, $f(x)^p = \int_0^\infty p t^{p-1} \chi_{\{t < f(x)\}} ~dt$.

::: {.proof}
For $a \geq 0$, $\int_0^a p t^{p-1} ~dt = \left[t^p\right]_0^a = a^p$ for every $p > 0$; when $0 < p < 1$ the integrand $t^{p-1}$ is integrable on $(0,a)$. Take $a = f(x)$ and write $\int_0^{f(x)}$ as $\int_0^\infty$ against $\chi_{\{t < f(x)\}}$.
:::

<1>2. The integrand $(x,t) \mapsto p t^{p-1} \chi_{\{t < f(x)\}}$ is nonnegative and measurable on $\RR \times (0,\infty)$.

::: {.proof}
$f$ is measurable, so $\{(x,t) : t < f(x)\} = f^{-1}((t, \infty))$ is a measurable subset of $\RR^2$; $t^{p-1}$ is measurable on $(0,\infty)$.
:::

<1>3. For each $t > 0$, $\int_\RR \chi_{\{t < f(x)\}} ~dx = \abs{\{x : f(x) > t\}}$.

::: {.proof}
For fixed $t$ the indicator is $1$ exactly on $\{x : f(x) > t\}$.
:::

<1>4. Q.E.D.

::: {.proof}
By step <1>1, $\int f^p ~dx = \int_\RR \int_0^\infty p t^{p-1} \chi_{\{t < f(x)\}} ~dt ~dx$. By step <1>2, Tonelli's theorem allows the order of integration to be exchanged, with both sides possibly $+\infty$. By step <1>3 the inner $x$-integral is $\abs{\{f > t\}}$, so
$$\int f^p ~dx = \int_0^\infty p t^{p-1} \abs{\{x : f(x) > t\}} ~dt.$$
:::
:::
