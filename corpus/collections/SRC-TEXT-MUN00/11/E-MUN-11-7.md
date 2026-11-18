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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose into numbered steps; the finite-type verification is Whitman's
    (Exercise 11.7, printed p. 126), as the card cites. Checked: both halves of the finite-type
    condition, the application of the Tukey lemma, and the identification of the resulting element
    with a maximal simply ordered subset. Not checked: the cited page and the printed forms of the
    Tukey lemma and the maximum principle, because tmp/sources holds no copy of the Whitman manual
    and the Munkres text is not retained in this VM.
---

::: {.exercise}

Show that the Tukey lemma implies the Hausdorff maximum principle. [Hint: If $\prec$ is a strict partial order on $A$, let $\mathcal A$ be the collection of all subsets of $A$ that are simply ordered by $\prec$. Show that $\mathcal A$ is of finite type.]
:::

::: {.solution}

The argument is that of the retained published solution: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.7, printed p 126, which the card cites; it is restructured into numbered steps below. The finite-type verification is his and follows the book's hint. The Tukey lemma is that a collection of finite type has an element contained in no other, and the Hausdorff maximum principle is that a strict partial order on $A$ has a maximal simply ordered subset.

::: pf

::: {.pf-step #down}

If $B\in\mathcal{A}$ then every subset of $B$ is in $\mathcal{A}$.

::: pf-proof

$B$ is simply ordered by $\prec$, and any subset of a simply ordered set is simply ordered: any two of its elements are comparable in $B$.

:::

:::

::: {.pf-step #up}

If every finite subset of $B$ lies in $\mathcal{A}$, then $B\in\mathcal{A}$.

::: pf-proof

Let $x,y\in B$. The set $\set{x,y}$ is a finite subset of $B$, hence in $\mathcal{A}$, hence simply ordered, so $x$ and $y$ are comparable; thus $B$ is simply ordered.

:::

:::

::: {.pf-step #ft}

$\mathcal{A}$ is of finite type.

::: pf-proof

'Of finite type' means exactly that $B$ lies in the collection whenever all its finite subsets do, and that every subset of a member lies in it; these are steps [](#up){.pf-ref} and [](#down){.pf-ref}.

:::

:::

::: {.pf-step #tukey}

$\mathcal{A}$ has an element contained in no other element of $\mathcal{A}$.

::: pf-proof

The Tukey lemma applied to the collection of finite type of step [](#ft){.pf-ref}.

:::

:::

::: {.pf-step #done}

The Hausdorff maximum principle holds.

::: pf-proof

An element $B\in\mathcal{A}$ contained in no other element of $\mathcal{A}$ is a subset of $A$ simply ordered by $\prec$ that is contained in no other such subset; that is a maximal simply ordered subset, which is the principle.

:::

:::

:::

:::
