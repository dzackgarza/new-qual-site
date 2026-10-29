---
schema: qual/card@1
id: P-MFWBK
kind: problem
title: $\QQ$ is neither open nor closed in $\RR$
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
  note: "Source text: the bare list item '$\\QQ$' under 'Determine if the following subsets of R are opened, closed, both, or neither' (Topology Week 1 Preliminaries workshop sheet). The lead-in is restored."
---

::: {.problem}
Determine whether $\QQ$ is an open subset of $\RR$, a closed subset, both, or neither.
:::

::: {.solution}

::: pf

::: {.pf-step #not-open}

$\QQ$ is not open in $\RR$.

::: pf-proof

Every interval $(q-\varepsilon,q+\varepsilon)$ around $q\in\QQ$ contains the irrational number $q+\varepsilon/\sqrt2$, so no such interval lies in $\QQ$.

:::

:::

::: {.pf-step #not-closed}

$\QQ$ is not closed in $\RR$.

::: pf-proof

Every interval $(x-\varepsilon,x+\varepsilon)$ around an irrational $x$ contains a rational number, so $\RR\setminus\QQ$ is not open.

:::

:::

::: pf-step

$\QQ$ is $\boxed{\text{neither open nor closed}}$ in $\RR$.

::: pf-proof

Combine steps [](#not-open){.pf-ref} and [](#not-closed){.pf-ref}.

:::

:::

:::

:::
