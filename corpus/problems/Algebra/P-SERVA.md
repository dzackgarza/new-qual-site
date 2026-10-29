---
schema: qual/card@1
id: P-SERVA
kind: problem
title: Cosets of a subgroup all have the same cardinality
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.problem}
Let $H\leq G$ be a subgroup (not necessarily normal).
Prove that any two cosets $xH, yH\in G/H$ have the same cardinality.
:::

::: {.hint}
Left multiplication $m_g\colon G\to G$, $x\mapsto gx$, is a bijection with inverse $m_{g^{-1}}$, and it restricts to a bijection $H\to gH$.
:::

::: {.solution}

Fix $x,y\in G$ and define $\tau\colon xH\to yH$ by $\tau(xh)=yh$ for $h\in H$.

::: pf

::: pf-step

$\tau$ is well defined.

::: pf-proof

Each element of $xH$ is $xh$ for exactly one $h\in H$: if $xh=xh'$, then $h=h'$ by cancellation.

:::

:::

::: pf-qed

By the same argument, $\sigma\colon yH\to xH$, $\sigma(yh)=xh$, is well defined, and $\sigma(\tau(xh))=xh$ and $\tau(\sigma(yh))=yh$ for all $h\in H$. So $\tau$ is a bijection with inverse $\sigma$, and $\abs{xH}=\abs{yH}$.

:::

:::

:::
