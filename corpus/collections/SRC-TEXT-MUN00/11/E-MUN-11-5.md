---
schema: qual/card@1
id: E-MUN-11-5
kind: problem
title: Zorn's lemma implies the Kuratowski lemma
classification:
  areas:
  - topology
  topics:
  - Maximum Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §11 Exercise 5, printed p. 71, with Zorn's
    lemma as stated in §11 on p. 69; the stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.5,
    printed p. 125 (tmp/sources/munkres-solutions-whitman.pdf). The upper bound of a
    chain is its union, which the hypothesis puts in A; a maximal element of (A, proper
    inclusion) is the element the Kuratowski lemma asks for.
---

::: {.exercise}

Show that Zorn's lemma implies the following:

Lemma (Kuratowski). Let $\mathcal A$ be a collection of sets. Suppose that for every subcollection $\mathcal B$ of $\mathcal A$ that is simply ordered by proper inclusion, the union of the elements of $\mathcal B$ belongs to $\mathcal A$. Then $\mathcal A$ has an element that is properly contained in no other element of $\mathcal A$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.5, printed p. 125** (`tmp/sources/munkres-solutions-whitman.pdf`); the reduction to Zorn's lemma is his.

Order $\mathcal A$ by proper inclusion, which is a strict partial order on it. Let $\mathcal B\subset\mathcal A$ be simply ordered by that relation. Its union $U=\bigcup_{B\in\mathcal B}B$ lies in $\mathcal A$ by hypothesis, and it is an upper bound: for $B\in\mathcal B$ we have $B\subset U$, so either $B=U$ or $B$ is properly contained in $U$. So every simply ordered subcollection has an upper bound in $\mathcal A$, and Zorn's lemma gives a maximal element $M$: no $A\in\mathcal A$ satisfies $M\subsetneq A$, which is exactly the assertion.
:::
