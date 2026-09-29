---
schema: qual/card@1
id: E-AMD-WQANMZED
kind: problem
title: Stabilizers of group actions are subgroups
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
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that if $G \actson X$ is a group action, then the stabilizer $G_x$ of a point is a subgroup.
:::


::: {.solution}
Fix $x\in X$ and write
\[
G_x=\{g\in G:g\cdot x=x\}.
\]

::: pf

::: {.pf-step #identity-in-gx}
The identity belongs to $G_x$.

::: pf-proof
By the identity axiom for a group action, $e\cdot x=x$.
:::

:::

::: {.pf-step #closed-under-quotient}
If $g,h\in G_x$, then $gh^{-1}\in G_x$.

::: pf-proof
Since $h\cdot x=x$, applying $h^{-1}$ gives $h^{-1}\cdot x=x$. Hence
\[
(gh^{-1})\cdot x
=g\cdot(h^{-1}\cdot x)
=g\cdot x
=x.
\]
Thus $gh^{-1}\in G_x$.
:::

:::

::: pf-step
Therefore $G_x\le G$.

::: pf-proof
By step [](#identity-in-gx){.pf-ref}, $G_x$ is nonempty, and by step [](#closed-under-quotient){.pf-ref} it satisfies the one-step subgroup criterion. Hence it is a subgroup of $G$.
:::

:::

:::

:::
