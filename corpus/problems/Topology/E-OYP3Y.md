---
schema: qual/card@1
id: E-OYP3Y
kind: problem
title: Continuous maps between compact Hausdorff spaces are proper
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source reads "any map"; a discontinuous map need not be proper, so the statement now says "any continuous map".
---

::: {.exercise}
Show that any continuous map between compact Hausdorff spaces must be proper.
:::

::: {.solution}

Let $f\colon X\to Y$ be continuous with $X$ and $Y$ compact Hausdorff, and let $K\subseteq Y$ be compact.

::: pf

::: {.pf-step #closed}

$f^{-1}(K)$ is closed in $X$.

::: pf-proof

A compact subset of the Hausdorff space $Y$ is closed, and preimages of closed sets under a continuous map are closed.

:::

:::

::: pf-step

$f^{-1}(K)$ is compact, so $f$ is proper.

::: pf-proof

By step [](#closed){.pf-ref}, $f^{-1}(K)$ is a closed subset of the compact space $X$, hence compact.

:::

:::

:::

:::
