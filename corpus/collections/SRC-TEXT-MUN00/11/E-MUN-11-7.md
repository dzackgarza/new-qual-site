---
schema: qual/card@1
id: E-MUN-11-7
kind: problem
title: The Tukey lemma implies the Hausdorff maximum principle
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
    Read against Munkres, Topology (2000), §11 Exercise 7, printed p. 71, with the
    maximum principle as stated on p. 68; the stored statement and the hint match.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.7,
    printed p. 126 (tmp/sources/munkres-solutions-whitman.pdf). The collection of
    simply ordered subsets is of finite type because being simply ordered is checked on
    pairs, hence on finite subsets; Tukey then gives a maximal member, which is a maximal
    simply ordered subset.
---

::: {.exercise}

Show that the Tukey lemma implies the Hausdorff maximum principle. [Hint: If $\prec$ is a strict partial order on $A$, let $\mathcal A$ be the collection of all subsets of $A$ that are simply ordered by $\prec$. Show that $\mathcal A$ is of finite type.]
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.7, printed p. 126** (`tmp/sources/munkres-solutions-whitman.pdf`); the finite-type verification is his and follows the book's hint.

Let $\prec$ be a strict partial order on $A$ and let $\mathcal A$ be the collection of subsets of $A$ that are simply ordered by $\prec$.

*$\mathcal A$ is of finite type.* If $B\in\mathcal A$ then every subset of $B$ is simply ordered, being pairwise comparable. Conversely, if every finite subset of $B$ lies in $\mathcal A$, then any two elements $x,y\in B$ are comparable, since $\{x,y\}$ is a finite subset of $B$ and hence simply ordered; so $B$ is simply ordered.

By the Tukey lemma of [[E-MUN-11-6]] the collection $\mathcal A$ has an element $B$ properly contained in no other element of $\mathcal A$. That is, $B$ is simply ordered and no subset of $A$ properly containing $B$ is simply ordered: $B$ is a maximal simply ordered subset of $A$, which is the maximum principle.
:::
