---
schema: qual/card@1
id: E-QCYEM
kind: problem
title: $\norm{f\ast\phi_t-f}_1\to 0$ as $t\to 0$ for an approximate identity $\phi$
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
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source leaves f, phi and phi_t undeclared; the statement declares them as the solution used them.
---

::: {.exercise}
Let $f \in L^1(\RR^n)$, let $\phi \in L^1(\RR^n)$ with $\int \phi = 1$, and put $\phi_t(x) = t^{-n}\phi(x/t)$ for $t > 0$. Show that $$\norm{f\ast \phi_t - f}_1 \converges{t\to 0}\to 0.$$
:::

::: {.solution}
For $h \in \RR^n$ let $\omega(h) \coloneqq \int \abs{f(x - h) - f(x)}\,dx$.

::: pf

::: {.pf-step #s1}

$f \ast \phi_t(x) - f(x) = \int \phi(y)\big(f(x - ty) - f(x)\big)\,dy$ for a.e. $x$.

::: pf-proof

Substituting $u = ty$ in $f \ast \phi_t(x) = \int f(x - u)\phi_t(u)\,du$ gives $\int f(x - ty)\phi(y)\,dy$, and $f(x) = \int f(x)\phi(y)\,dy$ because $\int \phi = 1$.

:::

:::

::: {.pf-step #s2}

$\norm{f \ast \phi_t - f}_1 \le \int \abs{\phi(y)}\,\omega(ty)\,dy$.

::: pf-proof

Take absolute values in step [](#s1){.pf-ref}, integrate in $x$, and exchange the order of integration by Tonelli's theorem.

:::

:::

::: {.pf-step #s3}

$\omega(h) \le 2\norm{f}_1$ for every $h$, and $\omega(h) \to 0$ as $h \to 0$.

::: pf-proof

The bound is the triangle inequality with translation invariance of the integral. The limit is continuity of translation in $L^1$.

:::

:::

::: pf-step

$\norm{f \ast \phi_t - f}_1 \to 0$ as $t \to 0$.

::: pf-proof

By step [](#s2){.pf-ref} it suffices that $\int \abs{\phi(y)}\,\omega(ty)\,dy \to 0$. For each $y$, $\omega(ty) \to 0$ as $t \to 0$ by step [](#s3){.pf-ref}, and $\abs{\phi(y)}\,\omega(ty) \le 2\norm{f}_1\abs{\phi(y)}$, which is integrable. The dominated convergence theorem applies along every sequence $t_k \to 0$.

:::

:::

:::

:::
