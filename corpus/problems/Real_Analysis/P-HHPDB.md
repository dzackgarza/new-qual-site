---
schema: qual/card@1
id: P-HHPDB
kind: problem
title: Uniform convergence $f*\phi_t\to f$ as $t\to 0$ for bounded uniformly continuous
  $f$ when $\int\phi=1$
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $\phi\in L^1(\RR^n)$ such that $\int \phi = 1$ and define $\phi_t(x) = t^{-n}\phi(\inverseof{t} x)$.
Show that if $f$ is bounded and uniformly continuous then $f\ast \phi_t \converges{t\to 0}\to f$ uniformly.
:::

::: {.solution}
If $\norm{f}_\infty = 0$ then $f \ast \phi_t = 0 = f$; assume $\norm{f}_\infty > 0$.

::: pf

::: {.pf-step #s1}

$\int \phi_t = 1$ and $\int\abs{\phi_t} = \norm{\phi}_1$ for every $t > 0$.

::: pf-proof

Substitute $y = x/t$.

:::

:::

::: {.pf-step #s2}

$(f \ast \phi_t)(x) - f(x) = \int \phi_t(y)\,(f(x-y) - f(x))\,dy$.

::: pf-proof

$(f \ast \phi_t)(x) = \int f(x-y)\phi_t(y)\,dy$ and $f(x) = f(x)\int\phi_t$ by step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

Given $\eps > 0$, there are $R > 0$ with $\int_{\norm{z} > R}\abs{\phi(z)}\,dz < \frac{\eps}{4\norm{f}_\infty}$ and $\eta > 0$ with $\abs{f(u) - f(v)} < \frac{\eps}{2\norm{\phi}_1}$ whenever $\norm{u - v} < \eta$.

::: pf-proof

The first holds because $\phi \in L^1$, by dominated convergence applied to $\abs{\phi}\chi_{\theset{\norm{z} > R}}$ as $R \to \infty$.
The second is uniform continuity of $f$.

:::

:::

::: {.pf-step #s4}

For $0 < t < \eta/R$ and every $x$, $\abs{(f \ast \phi_t)(x) - f(x)} < \eps$.

::: pf-proof

Split the integral of step [](#s2){.pf-ref} at $\norm{y} = tR$.
For $\norm{y} \le tR < \eta$, step [](#s3){.pf-ref} bounds $\abs{f(x-y) - f(x)}$ by $\frac{\eps}{2\norm{\phi}_1}$, and step [](#s1){.pf-ref} bounds the integral of $\abs{\phi_t}$, so this part is at most $\eps/2$.
For $\norm{y} > tR$, bound $\abs{f(x-y) - f(x)}$ by $2\norm{f}_\infty$ and substitute $z = y/t$: $\int_{\norm{y} > tR}\abs{\phi_t(y)}\,dy = \int_{\norm{z} > R}\abs{\phi(z)}\,dz$, so this part is less than $\eps/2$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives $\norm{f\ast\phi_t - f}_\infty \le \eps$ for $0 < t < \eta/R$.

:::

:::

:::
