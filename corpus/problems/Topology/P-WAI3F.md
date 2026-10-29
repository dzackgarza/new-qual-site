---
schema: qual/card@1
id: P-WAI3F
kind: problem
title: The antipodal map on $S^n$ is homotopic to the identity when $n$ is odd
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homotopy
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source problem block held a worked answer opening 'Main Idea: Linear homotopy fails continuity without the condition from (2)', which refers to a part not on this card; the statement now poses the claim that answer proves."
---

::: {.problem}
Let $n$ be odd. Show that the antipodal map $f\colon S^n \to S^n$, $f(x) = -x$, is homotopic to the identity.
:::

::: {.solution}
Since $n$ is odd, $n + 1 = 2m$ for an integer $m \geq 1$; identify $\RR^{n+1}$ with $\CC^m$, so that $S^n$ is the unit sphere $\{z \in \CC^m : \norm{z} = 1\}$.

::: pf

::: pf-step
The map $H\colon S^n \times [0,1] \to S^n$, $H(z,t) = e^{\pi i t} z$, is a homotopy from $\id_{S^n}$ to $f$.

::: pf-proof
$H$ is continuous, and it takes values in $S^n$ because $\norm{e^{\pi i t} z} = \abs{e^{\pi i t}}\,\norm{z} = \norm{z} = 1$.
Moreover $H(z,0) = z$ and $H(z,1) = e^{\pi i} z = -z$.
:::

:::

:::

:::
