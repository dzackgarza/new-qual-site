---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-13
kind: problem
title: A trigonometric integral limit
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(June 2007 #4b part i) Evaluate $$\lim_{n\to\infty}\int_{\pi/2}^{\pi}\frac{n\sin(x/n)}{x}\,dx$$ and justify your reasoning.
:::

::: {.solution}

::: pf

::: {.pf-step #uniform}

$\dfrac{n\sin(x/n)}{x}\to1$ uniformly on $[\pi/2,\pi]$.

::: pf-proof

Write $t=x/n\in(0,\pi/n]$, so the integrand is $\sin t/t$. Taylor's theorem with remainder gives $t-t^3/6\le\sin t\le t$ for $t\ge0$, hence
$$
0\le1-\frac{\sin t}{t}\le\frac{t^2}{6}\le\frac{\pi^2}{6n^2}
$$
for every $x\in[\pi/2,\pi]$. The bound tends to $0$ and does not depend on $x$.

:::

:::

::: pf-step

$\lim_{n\to\infty}\int_{\pi/2}^{\pi}\frac{n\sin(x/n)}{x}\,dx=\boxed{\pi/2}$.

::: pf-proof

The integrands are continuous on $[\pi/2,\pi]$. By step [](#uniform){.pf-ref},
$$
\abs{\int_{\pi/2}^{\pi}\frac{n\sin(x/n)}{x}\,dx-\int_{\pi/2}^{\pi}1\,dx}\le\frac{\pi}{2}\cdot\frac{\pi^2}{6n^2}\longrightarrow0,
$$
and $\int_{\pi/2}^{\pi}1\,dx=\pi/2$.

:::

:::

:::

:::
