---
schema: qual/card@1
id: P-GAA3C
kind: problem
title: Closed versus compact subsets of Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Closure
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "Source text (Topology Week 1 Preliminaries workshop sheet): 'Does the converse hold?', following 'Show that a compact subset of a Hausdorff space is closed.' The statement now names the converse."
---

::: {.problem}
A compact subset of a Hausdorff space is closed. Is every closed subset of a Hausdorff space compact?
:::

::: {.solution}

::: pf

::: pf-step

No: the closed subset $\RR$ of the Hausdorff space $\RR$ is not compact.

::: pf-proof

The space $\RR$ is a metric space, hence Hausdorff, and $\RR$ is closed in itself. The open cover $\{(-n,n)\}_{n\ge1}$ of $\RR$ has no finite subcover, since a finite subfamily is contained in one $(-N,N)$, which misses $N$.

:::

:::

:::

:::
