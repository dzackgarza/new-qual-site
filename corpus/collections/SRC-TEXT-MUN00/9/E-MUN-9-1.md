---
schema: qual/card@1
id: E-MUN-9-1
kind: problem
title: Injective map from $\mathbb{Z}_+$ to $X^{\omega}$ without choice
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 9, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Define an injective map $f: \mathbb{Z}_+ \to X^\omega$, where $X$ is the two-element set $\{0, 1\}$, without using the choice axiom.
:::

::: {.solution}
For \(n\in\mathbb Z_+\), define
\[
f(n)=(\underbrace{1,\ldots,1}_{n\text{ entries}},0,0,\ldots)\in X^\omega.
\]
If \(m<n\), then the \(n\)-th coordinate of \(f(m)\) is \(0\), whereas the \(n\)-th coordinate of \(f(n)\) is \(1\). Hence \(f(m)\ne f(n)\), so \(f\) is injective.

The construction is explicit and makes no choices from an arbitrary family of sets, so no form of the axiom of choice is used.
:::
