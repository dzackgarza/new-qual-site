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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §9 Exercise 1, printed p. 61, and the explicit injection is transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.1, printed pp. 100--101, who uses the indicator of a single point where the card uses an initial block of ones. Checked: every value lies in $X^\omega$, distinct indices give distinct values, and the formula names no arbitrary choice.
---

::: {.exercise}

Define an injective map $f: \ZZ_+ \to X^\omega$, where $X$ is the two-element set $\{0, 1\}$, without using the choice axiom.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.1** (`tmp/sources/munkres-solutions-whitman.pdf`); he uses the indicator of a single point where the card uses an initial block of ones, and both are explicit injections. The statement is Munkres, *Topology* (2000), §9 Exercise 1.

::: pf

::: {.pf-step #definition}
For $n\in\ZZ_+$ the formula $f(n)\coloneqq(1,\dots,1,0,0,\dots)$, with $n$ entries equal to $1$, defines an element of $X^\omega=\{0,1\}^\omega$.

::: pf-proof
The sequence has a definite value in $\{0,1\}$ at every coordinate: $1$ at coordinates $1,\dots,n$ and $0$ at every coordinate greater than $n$. Hence it is a function $\ZZ_+\to X$, that is, a point of $X^\omega$.
:::
:::

::: {.pf-step #injective}
$f(m)\neq f(n)$ for $m\neq n$.

::: pf-proof
Let $m<n$. The $n$-th coordinate of $f(m)$ is $0$, because $n>m$, while the $n$-th coordinate of $f(n)$ is $1$. Two sequences differing in some coordinate are different points.
:::
:::

::: {.pf-step #no-choice}
The definition uses no choice.

::: pf-proof
Each value $f(n)$ is given by an explicit rule from $n$ alone; no selection from a family of nonempty sets is made, and no well-ordering is invoked. So the map is produced in Zermelo--Fraenkel set theory without the axiom of choice.
:::
:::

::: {.pf-step}
There is an explicit injection $\ZZ_+\to X^\omega$ for $X=\{0,1\}$.

::: pf-proof
Steps [](#definition){.pf-ref}, [](#injective){.pf-ref} and [](#no-choice){.pf-ref} give the map, its injectivity and the absence of choice.
:::
:::

:::
:::
