---
schema: qual/card@1
id: P-OTXNQ
kind: problem
title: Open subsets of compact spaces
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Compactness
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source poses this as a follow-up to 'Show that a closed subset $A$ of a compact space $X$ is compact.' and reads only 'Does this hold when $A$ is instead an open subset?'; the statement now names the space and the subset."
---

::: {.problem}
Let $X$ be a compact topological space and let $A \subseteq X$ be an open subset. Must $A$ be compact?
:::

::: {.solution}

::: pf

::: pf-step
No: the open subset $A = (0,1)$ of the compact space $X = [0,1]$ is not compact.

::: pf-proof
The space $[0,1]$ is compact by the Heine--Borel theorem, and $(0,1)$ is open in it.
The sets $U_n = (1/n, 1)$ for $n \geq 2$ form an open cover of $(0,1)$, since every $x \in (0,1)$ satisfies $x > 1/n$ for $n$ large.
A finite subfamily $U_{n_1}, \ldots, U_{n_k}$ has union $U_N$ with $N = \max_i n_i$, which misses the point $1/(2N) \in (0,1)$.
So this cover has no finite subcover.
:::

:::

:::

:::
