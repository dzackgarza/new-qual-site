---
schema: qual/card@1
id: P-VXX34
kind: problem
title: The stabilizer of a point under a group action is a subgroup
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Subgroups
  - Group Actions
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

::: {.problem}
Show that if $G \curvearrowright X$ is a group action, then the stabilizer $G_x = \Stab_G(x)$ of any point $x \in X$ is a subgroup of $G$.
:::

::: {.solution}
Recall that $G_x=\{g\in G:g\cdot x=x\}$.

::: pf

::: pf-step

$e\in G_x$.

::: pf-proof

$e\cdot x=x$ by the axioms of an action.

:::

:::

::: pf-step

If $g,h\in G_x$, then $gh^{-1}\in G_x$.

::: pf-proof

Applying $h^{-1}$ to $h\cdot x=x$ gives $h^{-1}\cdot x=x$. Hence
$$
(gh^{-1})\cdot x
=g\cdot(h^{-1}\cdot x)
=g\cdot x
=x.
$$

:::

:::

::: pf-qed

By the subgroup criterion, $G_x\le G$.

:::

:::

:::
