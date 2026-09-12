---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-HW2
kind: problem
title: Separate consecutive separation axioms by examples (warm-up)
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Pick an $n\in\{0,1,2,3\}$, and give an example of a space that is $T_n$, but not $T_{n+1}$.
:::

::: {.solution}
Take \(n=0\). Let
\[
X=\{0,1\},\qquad \tau=\{\varnothing,\{1\},X\},
\]
the Sierpiński topology.

The space is \(T_0\): the open set \(\{1\}\) contains \(1\) but not \(0\), so the two points are topologically distinguishable.

It is not \(T_1\): the singleton \(\{1\}\) is not closed, since its complement \(\{0\}\) is not open. Equivalently, there is no open neighborhood of \(0\) that omits \(1\), because the only open neighborhood of \(0\) is \(X\).

Hence this is a \(T_0\) space that is not \(T_1\).
:::
