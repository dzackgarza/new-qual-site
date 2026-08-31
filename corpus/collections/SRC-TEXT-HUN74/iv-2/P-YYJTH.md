---
schema: qual/card@1
id: P-YYJTH
kind: problem
title: Hungerford 4.2.8
classification:
  areas:
  - algebra
  topics:
  - Vector Spaces
  - Bases
  - Direct Products
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
If $V$ is a finite dimensional vector space and $$V^m \coloneqq V \oplus V \oplus \cdots \oplus V \quad \text{($m$ summands)},$$ then for each $m\geq 1$, $V^m$ is finite dimensional and $\dim V^m = m(\dim V)$.
:::

::: {.solution}
<1>1. $\dim V^m = m\dim V$.
::: {.proof}
if $\{e_i\}$ basis of $V$, then $\{(e_i\text{ in }j\text{th summand})\}$ is basis of $V^m$, of size $m\dim V$.
:::

<1>2. Q.E.D.
::: {.proof}
<1>1.
:::
:::
