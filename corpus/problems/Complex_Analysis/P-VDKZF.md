---
schema: qual/card@1
id: P-VDKZF
kind: problem
title: An entire function omitting a bounded open set is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Removable Singularities
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source does not require the open set to be nonempty; every function omits the empty set, so the statement now takes $\Omega$ nonempty.'
---

::: {.problem}
Let $f(z)$ be entire and assume values of $f(z)$ lie outside a *bounded* nonempty open set $\Omega$.
Show without using Picard's theorems that $f(z)$ is a constant.
:::

::: {.solution}
Choose $w_0 \in \Omega$ and $\varepsilon > 0$ with $\overline{D_\varepsilon(w_0)} \subseteq \Omega$.

::: pf

::: {.pf-step #g}

The function $g(z) \coloneqq 1/(f(z)-w_0)$ is entire and $\abs{g} \leq 1/\varepsilon$.

::: pf-proof

Since $f(z) \notin \Omega$, $\abs{f(z) - w_0} \geq \varepsilon$ for every $z \in \CC$. So the denominator never vanishes and its modulus is at least $\varepsilon$.

:::

:::

::: pf-step

$f$ is constant.

::: pf-proof

By step [](#g){.pf-ref} and Liouville's theorem, $g$ is a constant, which is nonzero; hence $f = w_0 + 1/g$ is constant.

:::

:::

:::

:::
