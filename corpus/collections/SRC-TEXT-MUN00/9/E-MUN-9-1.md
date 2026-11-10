---
schema: qual/card@1
id: E-MUN-9-1
kind: problem
title: Injective map from $\ZZ_+$ to $X^{\omega}$ without choice
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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §9 Exercise 1, printed p. 61; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 9.1,
    printed pp. 100-101 (tmp/sources/munkres-solutions-whitman.pdf). He uses the
    indicator of a single point, (x_i = 1 iff i = n); the card uses the initial block of
    n ones, which is the same kind of explicit injection and is injective for the stated
    reason.
---

::: {.exercise}

Define an injective map $f: \ZZ_+ \to X^\omega$, where $X$ is the two-element set $\{0, 1\}$, without using the choice axiom.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.1, printed pp. 100--101** (`tmp/sources/munkres-solutions-whitman.pdf`); he uses the indicator of a single point where the card uses an initial block of ones, and both are explicit injections.

For $n\in\ZZ_+$, define
$$
f(n)=(\underbrace{1,\ldots,1}_{n\text{ entries}},0,0,\ldots)\in X^\omega.
$$
If $m<n$, then the $n$-th coordinate of $f(m)$ is $0$, whereas the $n$-th coordinate of $f(n)$ is $1$. Hence $f(m)\ne f(n)$, so $f$ is injective.

The construction is explicit and makes no choices from an arbitrary family of sets, so no form of the axiom of choice is used.
:::
