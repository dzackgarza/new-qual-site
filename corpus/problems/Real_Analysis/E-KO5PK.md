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
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source asserts the L^p limit for every p and every uniformly continuous f; for p < infinity this fails when f is not in L^p (for f(x) = x the difference is the constant -h). The statement now requires f in L^p for finite p.
---

::: {.exercise}
Let $1 \leq p \leq \infty$ and $\tau_h f(x) \coloneqq f(x-h)$. Prove continuity in $L^p$: if $f\colon \RR^n \to \CC$ is uniformly continuous, and moreover $f \in L^p(\RR^n)$ when $p < \infty$, then $$\norm{\tau_h f - f}_p \converges{h\to 0}\to 0.$$
:::

::: {.solution}
Let $f\colon \RR^n \to \CC$ be uniformly continuous, let $\tau_h f(x) \coloneqq f(x - h)$, and let $\omega(r) \coloneqq \sup\theset{\abs{f(x) - f(y)} : \abs{x - y} \leq r}$. Uniform continuity says $\omega(r) \to 0$ as $r \to 0$.

::: pf

::: {.pf-step #s1}

$\norm{\tau_h f - f}_\infty \leq \omega(\abs h) \to 0$.

::: pf-proof

$\abs{f(x-h) - f(x)} \leq \omega(\abs h)$ for every $x$.

:::

:::

::: pf-step

For $1 \leq p < \infty$, $\norm{\tau_h f - f}_p \to 0$.

::: pf-proof

Fix $\eps > 0$ and choose $R$ with $\int_{\abs x > R} \abs f^p < \eps$. Let $\abs h \leq 1$ and $B = \theset{\abs x \leq R + 1}$. Off $B$, $\abs{x - h} > R$, so by $\abs{a - b}^p \leq 2^{p-1}(\abs a^p + \abs b^p)$,
$$
\int_{\RR^n \setminus B} \abs{f(x-h) - f(x)}^p\,dx \leq 2^{p-1}\left(\int_{\abs y > R}\abs{f(y)}^p\,dy + \int_{\abs x > R}\abs{f(x)}^p\,dx\right) < 2^p\eps.
$$
On $B$, step [](#s1){.pf-ref} gives $\int_B \abs{f(x-h) - f(x)}^p\,dx \leq \omega(\abs h)^p\, m(B)$, which is less than $\eps$ for $\abs h$ small. So $\norm{\tau_h f - f}_p^p < (2^p + 1)\eps$ for $\abs h$ small.

:::

:::

:::

:::
