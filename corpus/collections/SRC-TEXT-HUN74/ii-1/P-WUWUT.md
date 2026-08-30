---
schema: qual/card@1
id: P-WUWUT
kind: problem
title: Hungerford 2.1.10
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Free Modules
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
\envlist

1. Show that the additive group of rationals $\mathbb Q$ is not finitely generated.

2. Show that $\mathbb Q$ is not free.

3. Conclude that Exercise 9 is false if the hypothesis "finitely generated" is omitted.
:::

::: {.solution}
<1>1. $\Q$ not finitely generated: any finite set generates subgroup with bounded denominators.
Proof: if $a_i/b_i$ generate, denominator divides $\prod b_i$.

<1>2. $\Q$ not free: any two rationals linearly dependent over $\Z$.
Proof: $a/b, c/d$ satisfy $ad\cdot c/d - cb\cdot a/b=0$.

<1>3. Exercise 9 false without finite generation: $\Q$ is counterexample.
Proof: <1>1 and <1>2.

<1>4. Q.E.D.
Proof: <1>3.
:::
