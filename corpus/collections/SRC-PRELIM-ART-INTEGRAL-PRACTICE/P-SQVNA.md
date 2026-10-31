---
schema: qual/card@1
id: P-SQVNA
kind: problem
title: Antiderivatives of $x^n\ln x$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Integration by Parts
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $n\ne-1$. Evaluate $\displaystyle\int x^n\ln x\,dx$ for $x>0$, and use it to evaluate:

(a) $\displaystyle\int_1^\infty\frac{\ln x}{x^2}\,dx$;

(b) $\displaystyle\int\sqrt x\,\ln x\,dx$;

(c) $\displaystyle\int x^2\ln x\,dx$;

(d) $\displaystyle\int x\ln x\,dx$.

Then evaluate the excluded case

(e) $\displaystyle\int\frac{\ln x}{x}\,dx$.

:::

::: {.solution}
Take $n \neq -1$ and $x > 0$.

::: pf

::: {.pf-step #s1}
Integrate by parts with $u = \ln x$ and $dv = x^n\,dx$.

::: pf-proof

::: pf-step
$du = \frac{1}{x}\,dx$ and $v = \frac{x^{n+1}}{n+1}$.

::: pf-proof
differentiate $\ln x$ and integrate $x^n$.
:::

:::

::: pf-step
$\int x^n \ln x\,dx = \frac{x^{n+1}}{n+1}\ln x - \int \frac{x^{n+1}}{n+1}\cdot \frac{1}{x}\,dx$.

::: pf-proof
integration by parts: $\int u\,dv = uv - \int v\,du$.
:::

:::

::: pf-step
$= \frac{x^{n+1}}{n+1}\ln x - \frac{1}{n+1}\int x^n\,dx$.

::: pf-proof
$\frac{x^{n+1}}{x} = x^n$.
:::

:::

::: {.pf-step #s1-4}
$= \frac{x^{n+1}}{n+1}\ln x - \frac{x^{n+1}}{(n+1)^2} + C$.

::: pf-proof
$\int x^n\,dx = \frac{x^{n+1}}{n+1}$.
:::

:::

:::

:::

::: {.pf-step #s2}
$\int x^n \ln x\,dx = \frac{x^{n+1}}{n+1}\left(\ln x - \frac{1}{n+1}\right) + C$.

::: pf-proof
Factor out $\frac{x^{n+1}}{n+1}$ in step [](#s1-4){.pf-ref} of step [](#s1){.pf-ref}.
:::

:::

::: pf-qed
Step [](#s2){.pf-ref} is the general formula; the special case $n = -1$ is $\int \frac{\ln x}{x}\,dx = \frac12 \ln^2 x + C$ (substitute $u = \ln x$).
:::

:::
:::
