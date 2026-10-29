---
schema: qual/card@1
id: P-TIRTE
kind: problem
title: Contractible if and only if the identity is nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source problem block held a worked answer to both directions, with 'Main Idea' paragraphs, rather than the question; the statement now poses the equivalence that answer proves."
---

::: {.problem}
Show that a space $X$ is contractible, that is, homotopy equivalent to a point, if and only if the identity map $\id_X$ is nullhomotopic.
:::

::: {.solution}

::: pf

::: pf-step
If $\id_X$ is homotopic to a constant map $c_{x_0}$, then $X$ is contractible.

::: pf-proof
Let $p\colon X\to\{x_0\}$ be the unique map and $i\colon\{x_0\}\hookrightarrow X$ the inclusion.
Then $p i=\id_{\{x_0\}}$ and $ip=c_{x_0}\simeq\id_X$, so $p$ and $i$ are homotopy inverses.
:::

:::

::: pf-step
If $X$ is contractible, then $\id_X$ is nullhomotopic.

::: pf-proof
A homotopy equivalence $X\simeq\{*\}$ supplies maps $p\colon X\to\{*\}$ and $i\colon\{*\}\to X$ with $ip\simeq\id_X$, and $ip$ is the constant map with value $i(*)$.
:::

:::

:::

:::
