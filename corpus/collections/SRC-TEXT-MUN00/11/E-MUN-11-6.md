---
schema: qual/card@1
id: E-MUN-11-6
kind: problem
title: The Kuratowski lemma implies the Tukey lemma
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
    Read against Munkres, Topology (2000), §11 Exercise 6, printed p. 71; the definition
    of a collection of finite type is printed there and is reproduced on the card.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.6,
    printed p. 125 (tmp/sources/munkres-solutions-whitman.pdf). The step that needs the
    finite-type hypothesis is that the union of a properly-inclusion-ordered
    subcollection lies in A: a finite subset of the union meets finitely many members,
    which are nested, so it lies in the largest of them and hence in A.
---

::: {.exercise}

A collection $\mathcal A$ of subsets of a set $X$ is said to be of finite type provided that a subset $B$ of $X$ belongs to $\mathcal A$ if and only if every finite subset of $B$ belongs to $\mathcal A$. Show that the Kuratowski lemma implies the following:

Lemma (Tukey, 1940). Let $\mathcal A$ be a collection of sets. If $\mathcal A$ is of finite type, then $\mathcal A$ has an element that is properly contained in no other element of $\mathcal A$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.6, printed p. 125** (`tmp/sources/munkres-solutions-whitman.pdf`); the verification that the hypothesis of the Kuratowski lemma holds is his.

Let $\mathcal A$ be of finite type and let $\mathcal B\subset\mathcal A$ be simply ordered by proper inclusion. We show $\bigcup_{B\in\mathcal B}B\in\mathcal A$. By finite type it suffices to show that each finite subset $F$ of the union lies in $\mathcal A$. Such an $F$ meets finitely many members of $\mathcal B$; since these are nested and finite in number, one of them, say $B_0$, contains all the others, and then $F\subset B_0$. Every finite subset of $B_0$ lies in $\mathcal A$ because $B_0\in\mathcal A$ and $\mathcal A$ is of finite type, so $F\in\mathcal A$.

Thus every subcollection simply ordered by proper inclusion has its union in $\mathcal A$, and the Kuratowski lemma of [[E-MUN-11-5]] gives an element of $\mathcal A$ properly contained in no other.
:::
