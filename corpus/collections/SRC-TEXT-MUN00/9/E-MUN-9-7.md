---
schema: qual/card@1
id: E-MUN-9-7
kind: problem
title: Strict cardinality ordering and iterated power sets
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 9, Exercise 7; the stored statement matches.
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
    Read against Munkres, Topology (2000), §9 Exercise 7, printed p. 61; the four parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 9.7, printed p. 106 (tmp/sources/munkres-solutions-whitman.pdf). His answers are the card's: (a) from Theorem 9.1; (b) by composing injections and contradicting the assumed absence of an injection A -> B; (c) by iterating the power set; (d) by the union of the A_n, whose injection into some A_n would restrict to one from A_{n+1} into A_n. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose into numbered steps; the four arguments are Whitman's (Exercise
    9.7, printed p. 106), as the card cites. Checked: the use of Theorems 9.1 and 7.1, the
    transitivity composition, Cantor's theorem, and the restriction argument, including that
    A_{n+1} is a subset of A. Not checked: the cited page and the printed theorems, because
    tmp/sources holds no copy of the Whitman manual and the Munkres text is not retained in this
    VM.
---

::: {.exercise}

Let $A$ and $B$ be two nonempty sets.
If there is an injection of $B$ into $A$, but no injection of $A$ into $B$, we say that $A$ has greater cardinality than $B$ .

(a) Conclude from Theorem 9.1 that every uncountable set has greater cardinality than $\ZZ_{+}$ .

(b) Show that if $A$ has greater cardinality than $B$, and $B$ has greater cardinality than $C$, then $A$ has greater cardinality than $C$ .

(c) Find a sequence $A_1, A_2, \ldots$ of infinite sets, such that for each $n \in \ZZ_+$, the set $A_{n+1}$ has greater cardinality than $A_n$ .

(d) Find a set that for every $n$ has cardinality greater than $A_{n}$ .
:::

::: {.solution}

The argument is that of the retained published solution: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.7, printed p 106, which the card cites; it is restructured into numbered steps below. The four arguments below are his. Greater cardinality means: an injection of the smaller set into the larger, and no injection of the larger into the smaller; Theorem 9.1 is that every infinite set contains a copy of $\ZZ_+$, and Theorem 7.1 that a set is countable when it injects into $\ZZ_+$.

::: pf

::: {.pf-step #a}

(a) Every uncountable set has greater cardinality than $\ZZ_+$.

::: pf-proof

Let $A$ be uncountable. It is infinite, so Theorem 9.1 gives an injection $\ZZ_+\to A$. There is no injection $A\to\ZZ_+$: such an injection would make $A$ countable by Theorem 7.1, contrary to hypothesis. Hence $A$ has greater cardinality than $\ZZ_+$.

:::

:::

::: {.pf-step #b}

(b) Greater cardinality is transitive.

::: pf-proof

Suppose $A$ has greater cardinality than $B$ and $B$ greater than $C$. Composing the injections $C\to B$ and $B\to A$ gives an injection $C\to A$. If there were an injection $A\to C$, composing it with $C\to B$ would give an injection $A\to B$, which the hypothesis excludes. Hence $A$ has greater cardinality than $C$.

:::

:::

::: {.pf-step #c}

(c) $A_1\coloneqq\ZZ_+$ and $A_{n+1}\coloneqq\mathcal{P}(A_n)$ give a sequence in which each term has greater cardinality than the previous.

::: pf-proof

$a\mapsto\set{a}$ injects $A_n$ into $\mathcal{P}(A_n)=A_{n+1}$, so there is an injection $A_n\to A_{n+1}$; Cantor's theorem says there is no surjection $A_n\to\mathcal{P}(A_n)$, hence no injection $A_{n+1}\to A_n$. Both sets are nonempty, so the definition of greater cardinality applies.

:::

:::

::: {.pf-step #d}

(d) $A\coloneqq\bigcup_{n\geq1}A_n$ has greater cardinality than every $A_n$.

::: pf-proof

Each $A_n$ is contained in $A$, so inclusion is an injection $A_n\to A$. Fix $n$ and suppose there were an injection $A\to A_n$; restricting it to $A_{n+1}\subset A$ would give an injection $A_{n+1}\to A_n$, contradicting step [](#c){.pf-ref}.

:::

:::

:::

:::
