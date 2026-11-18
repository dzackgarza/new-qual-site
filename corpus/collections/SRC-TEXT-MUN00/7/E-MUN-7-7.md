---
schema: qual/card@1
id: E-MUN-7-7
kind: problem
title: Equal cardinality of $\{0,1\}^{\omega}$ subsets
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 7; the stored statement matches.
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
    Read against Munkres, Topology (2000), §7 Exercise 7, printed p. 52; the reference is
    to the D and E of Exercise 5, which are stored on E-MUN-7-5.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.7,
    printed p. 90 (tmp/sources/munkres-solutions-whitman.pdf). The two injections and the
    appeal to Schroeder-Bernstein are his; the card's encoding of a positive-integer
    sequence as blocks of 1s separated by 0s is the injection D -> E, and the recovery of
    the block lengths is what makes it injective. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose into numbered steps; the two injections and the appeal to
    Schroeder-Bernstein are Whitman's (Exercise 7.7, printed p. 90), as the card cites. Checked:
    that both maps land in the stated set and are injective, including the separation of blocks by
    the zeros. Not checked: the cited page, because tmp/sources holds no copy of the Whitman
    manual and the Munkres text is not retained in this VM.
---

::: {.exercise}

Show that the sets D and E of Exercise 5 have the same cardinality.
:::

::: {.solution}

The argument is that of the retained published solution: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.7, printed p 90, which the card cites; it is restructured into numbered steps below. Here, as in Exercise 5, $D=(\ZZ_+)^{\omega}$ is the set of sequences of positive integers and $E=\set{0,1}^{\omega}$ the set of binary sequences; the criterion is the Schroeder--Bernstein theorem.

::: pf

::: {.pf-step #intoD}

$(x_n)\mapsto(x_n+1)$ is an injection $E\to D$.

::: pf-proof

Each $x_n+1$ is a positive integer, so the image lies in $(\ZZ_+)^{\omega}$; and $x_n+1=y_n+1$ for all $n$ gives $x_n=y_n$, so the map is injective.

:::

:::

::: {.pf-step #intoE}

The encoding $a\mapsto1^{a_1}0\,1^{a_2}0\cdots$ is an injection $D\to E$.

::: pf-proof

Every $a_i\geq1$, so each block $1^{a_i}$ is nonempty and the sequence produced is a binary sequence with a $0$ at the end of every block, hence in $E$. If two sequences $a\neq a'$ differ first at index $j$, the encodings agree up to the $j-1$ separator zeros and then have blocks of ones of different lengths, since $a_j\neq a'_j$; so the encodings differ.

:::

:::

::: {.pf-step #done}

$\cardinality{D}=\cardinality{E}$.

::: pf-proof

Schroeder--Bernstein: injections in both directions give a bijection.

:::

:::

:::

:::
