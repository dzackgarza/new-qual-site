---
schema: qual/card@1
id: P-WC3HY
kind: problem
title: Group action, orbit, stabilizer, and fixed points
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- State definitions of the following:

  - Group action

  - Orbit

  - Stabilizer

  - Fixed points
:::

::: {.solution}
<1>1. Group action: an action of a group $G$ on a set $X$ is a map $G \times X \to X$, $(g, x) \mapsto g \cdot x$, such that $e \cdot x = x$ and $g \cdot (h \cdot x) = (gh) \cdot x$ for all $g, h \in G$, $x \in X$.
::: {.proof}
definition.
:::

<1>2. Orbit: the orbit of $x \in X$ is $\operatorname{Orb}(x) = \{g \cdot x : g \in G\}$.
::: {.proof}
definition.
:::

<1>3. Stabilizer: the stabilizer of $x \in X$ is $\operatorname{Stab}(x) = \{g \in G : g \cdot x = x\}$.
::: {.proof}
definition.
:::

<1>4. Fixed points: the fixed points of an element $g \in G$ are $\operatorname{Fix}(g) = \{x \in X : g \cdot x = x\}$; the fixed points of the action are $\{x \in X : g \cdot x = x \text{ for all } g \in G\}$.
::: {.proof}
definition.
:::

<1>5. Q.E.D.
::: {.proof}
<1>1–<1>4.
:::
:::
