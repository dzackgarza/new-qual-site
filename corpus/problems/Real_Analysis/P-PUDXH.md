---
schema: qual/card@1
id: P-PUDXH
kind: problem
title: $\int_0^\infty\frac{g(x)}{x}\int_0^x f(y)\,dy\,dx\le AB$ with $A=\int_0^\infty
  f(y)y^{-1/2}\,dy$ and $B=\|g\|_2$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Fubini-Tonelli
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $f, g$ be non-negative measurable functions on $[0, \infty)$ with
\[
A &\definedas \int_0^{\infty } f(y) y^{-1/2} \dy < \infty \\
B &\definedas \qty{ \int_0^{\infty } \abs{ g(y) } }^2 \dy < \infty  
.\]

Show that
\[
\int_0^{\infty } \qty{ \int_0^{\infty } f(y) \dy } {g(x) \over x} \dx \leq AB
.\]
:::

::: {.solution}
We prove $\int_0^\infty \frac{g(x)}{x}\int_0^x f(y)\,dy\,dx \le AB$ with $A = \int_0^\infty f(y)y^{-1/2}\,dy$ and $B = \left(\int_0^\infty g(y)^2\,dy\right)^{1/2}$; see the remark below.

::: pf

::: {.pf-step #s1}

$\int_0^\infty \frac{g(x)}{x}\int_0^x f(y)\,dy\,dx = \int_0^\infty f(y) \int_y^\infty \frac{g(x)}{x}\, dx\, dy$.

::: pf-proof

The integrand $f(y)g(x)x^{-1}\chi_{\theset{y < x}}$ is nonnegative and measurable on $(0,\infty)^2$, so Tonelli's theorem allows exchanging the order of integration.

:::

:::

::: {.pf-step #s2}

For $y > 0$, $\int_y^\infty \frac{g(x)}{x}\, dx \le B y^{-1/2}$.

::: pf-proof

By the Cauchy--Schwarz inequality, $\int_y^\infty \frac{g(x)}{x}\, dx \le \left(\int_y^\infty g^2\right)^{1/2}\left(\int_y^\infty x^{-2}\,dx\right)^{1/2} \le B\,y^{-1/2}$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the left side is at most $\int_0^\infty f(y)\,B y^{-1/2}\, dy = AB$.

:::

:::

:::

::: {.remark}
As printed, the inner integral $\int_0^\infty f(y)\,dy$ does not depend on $x$, and $B$ is written with the square outside the integral. The inequality above takes the inner integral over $[0,x]$ and $B = \|g\|_{L^2}$.
:::
