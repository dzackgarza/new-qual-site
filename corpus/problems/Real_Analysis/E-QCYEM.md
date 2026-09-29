---
schema: qual/card@1
id: E-QCYEM
kind: problem
title: $\|f\ast\phi_t-f\|_1\to 0$ as $t\to 0$ for an approximate identity $\phi$
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
---

::: {.exercise}
- Show that if $\phi$ is an approximate identity, then $$\norm{f\ast \phi_t - f}_1 \converges{t\to 0}\to 0.$$
:::

::: {.solution}
Let $f \in L^1(\RR^n)$, let $\phi \in L^1(\RR^n)$ with $\int \phi = 1$, and put $\phi_t(x) = t^{-n}\phi(x/t)$. For $h \in \RR^n$ let $\omega(h) \coloneqq \int \abs{f(x - h) - f(x)}\,dx$.

::: pf

::: {.pf-step #s1}

$f \ast \phi_t(x) - f(x) = \int \phi(y)\big(f(x - ty) - f(x)\big)\,dy$ for a.e. $x$.

::: pf-proof

Substituting $u = ty$ in $f \ast \phi_t(x) = \int f(x - u)\phi_t(u)\,du$ gives $\int f(x - ty)\phi(y)\,dy$, and $f(x) = \int f(x)\phi(y)\,dy$ because $\int \phi = 1$.

:::

:::

::: {.pf-step #s2}

$\|f \ast \phi_t - f\|_1 \le \int |\phi(y)|\,\omega(ty)\,dy$.

::: pf-proof

Take absolute values in step [](#s1){.pf-ref}, integrate in $x$, and exchange the order of integration by Tonelli's theorem.

:::

:::

::: {.pf-step #s3}

$\omega(h) \le 2\|f\|_1$ for every $h$, and $\omega(h) \to 0$ as $h \to 0$.

::: pf-proof

The bound is the triangle inequality with translation invariance of the integral. The limit is continuity of translation in $L^1$.

:::

:::

::: {.pf-step #s4}

$\int |\phi(y)|\,\omega(ty)\,dy \to 0$ as $t \to 0$.

::: pf-proof

For each $y$, $\omega(ty) \to 0$ as $t \to 0$ by step [](#s3){.pf-ref}, and $|\phi(y)|\,\omega(ty) \le 2\|f\|_1|\phi(y)|$, which is integrable. The dominated convergence theorem applies along every sequence $t_k \to 0$.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::
