---
schema: qual/card@1
id: E-MUN-6-5
kind: exercise
title: Finiteness of Cartesian products
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

If $A \times B$ is finite, does it follow that $A$ and $B$ are finite?

::: solution
**Goal:** Show $A$ and $B$ are finite from finiteness of $A\times B$.

<1>1. If $A$ is empty or $B$ is empty, then $A\times B=\varnothing$ is finite and both $A$ and $B$ are finite.

<1>2. Assume both $A$ and $B$ are nonempty.
    <2>1. Choose $b_0\in B$.
    <2>2. The map
    $$\iota:A\to A\times\{b_0\},\qquad a\mapsto(a,b_0),$$
    is injective.
    <2>3. Since $A\times\{b_0\}\subseteq A\times B$, the set $A$ injects into a finite set.
    <2>4. Therefore $A$ is finite.

<1>3. Symmetrically, choose $a_0\in A$ and use
    $$\jmath:B\to\{a_0\}\times B,\qquad b\mapsto(a_0,b),$$
    to conclude $B$ is finite.
:::
:::
