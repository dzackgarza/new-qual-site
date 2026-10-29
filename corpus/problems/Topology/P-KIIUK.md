---
schema: qual/card@1
id: P-KIIUK
kind: problem
title: Non-surjective maps into $S^n$ are nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "Source text: 'Show that if X ->f X^n is not surjective, then f is nullhomotopic.' The target X^n is undefined and the claim is false for general targets; it is read as the sphere S^n, the standard form of this exercise."
---

::: {.problem}
Let $X$ be a topological space. Show that if a continuous map $f:X\to S^n$ is not surjective, then $f$ is nullhomotopic.
:::

::: {.solution}

::: pf

::: pf-step

$f$ is nullhomotopic.

::: pf-proof

Choose $p\in S^n\setminus f(X)$. Then $f$ factors as $X\to S^n\setminus\{p\}\hookrightarrow S^n$. Stereographic projection from $p$ gives $S^n\setminus\{p\}\cong\RR^n$, which is contractible, so the corestriction $X\to S^n\setminus\{p\}$ is homotopic to a constant map. Composing that homotopy with the inclusion shows $f$ is nullhomotopic.

:::

:::

:::

:::
