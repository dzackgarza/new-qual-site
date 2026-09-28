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
Let $\phi\in L^1(\RR^n)$ such that $\int \phi = 1$ and define $\phi_t(x) = t^{-n}\phi(t\inv x)$.
Show that if $f$ is bounded and uniformly continuous then $f\ast \phi_t \converges{t\to 0}\to f$ uniformly.
:::
::: {.solution}
If $\|f\|_\infty = 0$ then $f \ast \phi_t = 0 = f$; assume $\|f\|_\infty > 0$.

<1>1. $\int \phi_t = 1$ and $\int|\phi_t| = \|\phi\|_1$ for every $t > 0$.

::: {.proof}
Substitute $y = x/t$.
:::

<1>2. $(f \ast \phi_t)(x) - f(x) = \int \phi_t(y)\,(f(x-y) - f(x))\,dy$.

::: {.proof}
$(f \ast \phi_t)(x) = \int f(x-y)\phi_t(y)\,dy$ and $f(x) = f(x)\int\phi_t$ by step <1>1.
:::

<1>3. Given $\eps > 0$, there are $R > 0$ with $\int_{|z| > R}|\phi(z)|\,dz < \frac{\eps}{4\|f\|_\infty}$ and $\eta > 0$ with $|f(u) - f(v)| < \frac{\eps}{2\|\phi\|_1}$ whenever $|u - v| < \eta$.

::: {.proof}
The first holds because $\phi \in L^1$, by dominated convergence applied to $|\phi|\chi_{\theset{|z| > R}}$ as $R \to \infty$. The second is uniform continuity of $f$.
:::

<1>4. For $0 < t < \eta/R$ and every $x$, $|(f \ast \phi_t)(x) - f(x)| < \eps$.

::: {.proof}
Split the integral of step <1>2 at $|y| = tR$. For $|y| \le tR < \eta$, step <1>3 bounds $|f(x-y) - f(x)|$ by $\frac{\eps}{2\|\phi\|_1}$, and step <1>1 bounds the integral of $|\phi_t|$, so this part is at most $\eps/2$. For $|y| > tR$, bound $|f(x-y) - f(x)|$ by $2\|f\|_\infty$ and substitute $z = y/t$: $\int_{|y| > tR}|\phi_t(y)|\,dy = \int_{|z| > R}|\phi(z)|\,dz$, so this part is less than $\eps/2$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives $\|f\ast\phi_t - f\|_\infty \le \eps$ for $0 < t < \eta/R$.
:::
:::
