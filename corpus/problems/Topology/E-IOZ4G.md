---
schema: qual/card@1
id: E-IOZ4G
kind: problem
title: Every indiscrete space is separable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
Show that any topological space $X$ equipped with the indiscrete (trivial) topology is separable.
:::

::: solution
If $X=\varnothing$, then $X$ itself is a countable dense subset. Assume $X\ne\varnothing$ and choose $x\in X$.

<1>1. In the indiscrete topology, the only nonempty open set is $X$.

<1>2. Hence every nonempty subset of $X$ meets every nonempty open set, so every nonempty subset is dense.

<1>3. In particular, the singleton $\{x\}$ is finite and dense. Therefore $X$ is separable.
:::
