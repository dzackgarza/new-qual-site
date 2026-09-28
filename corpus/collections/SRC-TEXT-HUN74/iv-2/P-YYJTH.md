---
schema: qual/card@1
id: P-YYJTH
kind: problem
title: $\dim V^m = m\dim V$
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
Let $e_1,\ldots,e_n$ be a basis of $V$, $n=\dim V$, and for $1\le j\le m$ let $\iota_j\colon V\to V^m$ be the inclusion of the $j$th summand.

<1>1. The $mn$ vectors $\iota_j(e_i)$, $1\le i\le n$, $1\le j\le m$, form a basis of $V^m$.

::: {.proof}
An element $(v_1,\ldots,v_m)\in V^m$ equals $\sum_j\iota_j(v_j)$, and writing $v_j=\sum_i c_{ij}e_i$ gives $(v_1,\ldots,v_m)=\sum_{i,j}c_{ij}\iota_j(e_i)$, so the vectors span. If $\sum_{i,j}c_{ij}\iota_j(e_i)=0$, then the $j$th coordinate $\sum_i c_{ij}e_i$ vanishes for each $j$, so every $c_{ij}=0$ by independence of $e_1,\ldots,e_n$.
:::

<1>2. Q.E.D.

::: {.proof}
By step <1>1, $V^m$ has a finite basis of $mn$ elements, so it is finite dimensional and $\dim V^m=m\dim V$.
:::
:::
