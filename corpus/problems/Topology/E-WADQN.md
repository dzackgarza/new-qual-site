---
schema: qual/card@1
id: E-WADQN
kind: problem
title: Extreme value theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $f: X \to \RR$ is continuous and $X$ is a nonempty compact topological space, then $f(X)$ is bounded and $f$ attains its minimum and maximum on $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #image-compact}

$f(X)$ is compact.

::: pf-proof

If $\{V_\alpha\}$ is an open cover of $f(X)$, then $\{f^{-1}(V_\alpha)\}$ is an open cover of $X$. A finite subcover of $X$ gives a finite subcover of $f(X)$.

:::

:::

::: {.pf-step #closed-bounded}

$f(X)$ is closed and bounded.

::: pf-proof

This is the Heine--Borel theorem applied to step [](#image-compact){.pf-ref}.

:::

:::

::: pf-step

There are $x_{\min},x_{\max}\in X$ with $f(x_{\min})=\inf f(X)$ and $f(x_{\max})=\sup f(X)$.

::: pf-proof

Since $X$ is nonempty, $f(X)$ is nonempty, and by step [](#closed-bounded){.pf-ref} it is bounded, so $m=\inf f(X)$ and $M=\sup f(X)$ are real numbers. Both lie in the closure of $f(X)$, which is $f(X)$ by step [](#closed-bounded){.pf-ref}.

:::

:::

:::

:::
