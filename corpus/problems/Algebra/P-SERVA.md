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

::: problem
- Let $H\leq G$ be a subgroup (not necessarily normal).
  Prove that any two cosets $xH, yH\in G/H$ have the same cardinality.

  > Define a map $m_g: G\to G$ where $x\mapsto gx$, restrict to $m_h:H\surjects gH$, inverse $(m_g)\inv = m_{g\inv}$
:::

::: solution
**Theorem.**  
Any two left cosets of a subgroup have equal cardinality.

*Proof.*

1. Fix $x,y\in G$. Define $\tau:xH\to yH$ by $\tau(xh)=yh$ for $h\in H$.
2. $\tau$ is well defined since multiplying $h$ by an element of $H$ gives another element of $H$.
3. For $u\in H$, define $\tau^{-1}(yu)=xu$; then $\tau^{-1}(yu)\in xH$ and
   \[
   \tau(\tau^{-1}(yu))=y u,\qquad
   \tau^{-1}(\tau(xh))=x h.
   \]
   So $\tau^{-1}$ is an inverse.
4. Hence $\tau$ is a bijection and $|xH|=|yH|$.
:::
