---
schema: qual/card@1
id: E-4ZTVF
kind: problem
title: A quotient of a compact space is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Quotient Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that a quotient of a compact space is again compact.
:::

::: {.solution}

Let $X$ be compact and $q: X \to Y$ a quotient map, and let $\{V_\alpha\}_{\alpha \in A}$ be an open cover of $Y$.

::: pf

::: {.pf-step #pullback}

$\{q^{-1}(V_\alpha)\}_{\alpha \in A}$ is an open cover of $X$.

::: pf-proof

A quotient map is continuous, so each $q^{-1}(V_\alpha)$ is open, and $\bigcup_\alpha q^{-1}(V_\alpha) = q^{-1}(Y) = X$.

:::

:::

::: pf-step

Finitely many $V_\alpha$ cover $Y$.

::: pf-proof

By compactness of $X$ and step [](#pullback){.pf-ref}, $X = \bigcup_{i=1}^k q^{-1}(V_{\alpha_i})$ for some $\alpha_1, \ldots, \alpha_k$. Since $q$ is surjective, $q(q^{-1}(V)) = V$ for every $V \subseteq Y$, so
$$
Y = q(X) = \bigcup_{i=1}^k q\big(q^{-1}(V_{\alpha_i})\big) = \bigcup_{i=1}^k V_{\alpha_i}.
$$

:::

:::

:::

:::
