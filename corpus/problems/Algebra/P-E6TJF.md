---
schema: qual/card@1
id: P-E6TJF
kind: problem
title: Stabilizers of points in the same orbit are conjugate
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Conjugacy
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: "The source statement was a bullet item, 'Show that if $x, y$ are in the same orbit, then their stabilizers are conjugate.', that declared no group or set; the action of a group $G$ on a set $X$ is now stated."
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Let a group $G$ act on a set $X$.
Show that if $x, y\in X$ are in the same orbit, then their stabilizers are conjugate.
:::

::: {.solution}
Suppose $y=g\cdot x$ with $g\in G$, and write $G_x$, $G_y$ for the stabilizers.

::: pf

::: {.pf-step #sub}
$gG_xg^{-1}\subseteq G_y$.

::: pf-proof
If $h\in G_x$, then $(ghg^{-1})\cdot y=gh\cdot x=g\cdot x=y$.
:::

:::

::: {.pf-step #sup}
$G_y\subseteq gG_xg^{-1}$.

::: pf-proof
If $k\in G_y$, then $(g^{-1}kg)\cdot x=g^{-1}k\cdot y=g^{-1}\cdot y=x$, so $g^{-1}kg\in G_x$ and $k\in gG_xg^{-1}$.
:::

:::

::: pf-qed
By steps [](#sub){.pf-ref} and [](#sup){.pf-ref}, $G_y=gG_xg^{-1}$, so the stabilizers are conjugate.
:::

:::

:::
