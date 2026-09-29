---
schema: qual/card@1
id: E-KO5PK
kind: problem
title: Translation is continuous in $L^p$ for uniformly continuous functions
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Uniform Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Prove continuity in $L^p$: If $f$ is uniformly continuous then for all $p$, $$\norm{\tau_h f - f}_p \converges{h\to 0}\to 0.$$
:::

::: {.solution}
Let $f\colon \RR^n \to \CC$ be uniformly continuous, let $\tau_h f(x) \coloneqq f(x - h)$, and let $\omega(r) \coloneqq \sup\theset{\abs{f(x) - f(y)} : \abs{x - y} \leq r}$. Uniform continuity says $\omega(r) \to 0$ as $r \to 0$. For $1 \leq p < \infty$ assume $f \in L^p(\RR^n)$, so that $\norm{\tau_h f - f}_p$ is finite.

::: pf

::: {.pf-step #s1}

$\norm{\tau_h f - f}_\infty \leq \omega(\abs h) \to 0$.

::: pf-proof

$\abs{f(x-h) - f(x)} \leq \omega(\abs h)$ for every $x$.

:::

:::

::: {.pf-step #s2}

For $1 \leq p < \infty$, $\norm{\tau_h f - f}_p \to 0$.

::: pf-proof

Fix $\eps > 0$ and choose $R$ with $\int_{\abs x > R} \abs f^p < \eps$. Let $\abs h \leq 1$ and $B = \theset{\abs x \leq R + 1}$. Off $B$, $\abs{x - h} > R$, so by $\abs{a - b}^p \leq 2^{p-1}(\abs a^p + \abs b^p)$,
$$
\int_{\RR^n \setminus B} \abs{f(x-h) - f(x)}^p\,dx \leq 2^{p-1}\left(\int_{\abs y > R}\abs{f(y)}^p\,dy + \int_{\abs x > R}\abs{f(x)}^p\,dx\right) < 2^p\eps.
$$
On $B$, step [](#s1){.pf-ref} gives $\int_B \abs{f(x-h) - f(x)}^p\,dx \leq \omega(\abs h)^p\, m(B)$, which is less than $\eps$ for $\abs h$ small. So $\norm{\tau_h f - f}_p^p < (2^p + 1)\eps$ for $\abs h$ small.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} is the case $p = \infty$ and step [](#s2){.pf-ref} is the case $1 \leq p < \infty$.

:::

:::

:::
