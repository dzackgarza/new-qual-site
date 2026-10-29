---
schema: qual/card@1
id: E-3OAGD
kind: problem
title: Inner approximation of a finite-measure set by compact subsets
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that if $E\subseteq \RR^n$ is measurable with $m(E) < \infty$, then
$$m(E) = \sup \{ m(K) \mid K \subseteq E \text{ is compact}\}$$
if and only if for all $\varepsilon > 0$, there exists a compact set $K \subseteq E$ such that $m(K) \geq m(E) - \varepsilon$.
:::

::: {.solution}
Let $\mathcal{S} = \{ m(K) \mid K \subseteq E \text{ is compact} \}$.

::: pf

::: {.pf-step #upper}
$\sup\mathcal{S}\le m(E)$.

::: pf-proof
By monotonicity of Lebesgue measure, $m(K)\le m(E)$ for every compact $K\subseteq E$.
:::

:::

::: pf-step
If $m(E)=\sup\mathcal{S}$, then for every $\varepsilon>0$ there is a compact $K\subseteq E$ with $m(K)\ge m(E)-\varepsilon$.

::: pf-proof
Since $m(E)<\infty$, $m(E)-\varepsilon<\sup\mathcal{S}$, so $m(E)-\varepsilon$ is not an upper bound of $\mathcal{S}$, and some $m(K)\in\mathcal{S}$ exceeds it.
:::

:::

::: pf-step
If for every $\varepsilon>0$ there is a compact $K_\varepsilon\subseteq E$ with $m(K_\varepsilon)\ge m(E)-\varepsilon$, then $m(E)=\sup\mathcal{S}$.

::: pf-proof
For each $\varepsilon>0$, $\sup\mathcal{S}\ge m(K_\varepsilon)\ge m(E)-\varepsilon$, so $\sup\mathcal{S}\ge m(E)$. Step [](#upper){.pf-ref} gives the reverse inequality.
:::

:::

:::

:::
