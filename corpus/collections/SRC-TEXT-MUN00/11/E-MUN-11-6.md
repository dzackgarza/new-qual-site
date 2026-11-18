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

::: pf

::: {.pf-step #finite}

Every finite subset of $\bigcup_{B\in\mathcal{B}}B$ lies in $\mathcal{A}$.

::: pf-proof

Let $F$ be a finite subset of the union and let $\mathcal{B}$ be simply ordered by proper inclusion; each $x\in F$ lies in some $B_{x}\in\mathcal{B}$, and only finitely many such $B_{x}$ occur. A finite simply ordered family has a largest member: inducting on the number of members, the largest of the first $k$ and the $(k+1)$-st are comparable, and the greater is the largest of the first $k+1$. So some $B_{0}\in\mathcal{B}$ contains every $B_{x}$, hence contains $F$. Now $B_{0}\in\mathcal{A}$ and $\mathcal{A}$ is of finite type, so every finite subset of $B_{0}$ belongs to $\mathcal{A}$; in particular $F\in\mathcal{A}$.

:::

:::

::: {.pf-step #union}

The union $\bigcup_{B\in\mathcal{B}}B$ itself lies in $\mathcal{A}$.

::: pf-proof

$\mathcal{A}$ is of finite type, so a set lies in $\mathcal{A}$ exactly when all its finite subsets do. By step [](#finite){.pf-ref} every finite subset of the union lies in $\mathcal{A}$, hence the union does.

:::

:::

::: {.pf-step #kuratowski}

The Kuratowski lemma applies and gives an element of $\mathcal{A}$ properly contained in no other.

::: pf-proof

The Kuratowski lemma says that if every subcollection of $\mathcal{A}$ simply ordered by proper inclusion has its union in $\mathcal{A}$, then $\mathcal{A}$ has an element properly contained in no other element of $\mathcal{A}$. Step [](#union){.pf-ref} verifies that hypothesis for every such subcollection $\mathcal{B}$. Therefore there is $A_{0}\in\mathcal{A}$ such that no $A\in\mathcal{A}$ contains $A_{0}$ properly:
$$
\boxed{\mathcal{A}\ \text{of finite type}\implies\exists A_{0}\in\mathcal{A}\ \text{maximal under proper inclusion (Tukey's lemma).}}
$$

:::

:::

:::

:::
