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
---

::: {.exercise}

Show that the sets D and E of Exercise 5 have the same cardinality.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.7, printed p. 90** (`tmp/sources/munkres-solutions-whitman.pdf`); the two injections and the appeal to Schroeder--Bernstein are his.

Recall
$$
D=(\ZZ_+)^\omega,
\qquad
E=\{0,1\}^\omega.
$$
There is an injection $E\to D$ given by
$$
(x_n)\mapsto(x_n+1).
$$

For the reverse direction, encode $a=(a_1,a_2,\ldots)\in D$ by the binary sequence
$$
\underbrace{11\cdots1}_{a_1}0\,
\underbrace{11\cdots1}_{a_2}0\,
\underbrace{11\cdots1}_{a_3}0\cdots.
$$
Because every $a_i\ge1$, this sequence contains infinitely many separator zeros, and the lengths of the successive blocks of ones uniquely recover $a_1,a_2,\ldots$. Thus this encoding is injective $D\to E$.

By Schroeder--Bernstein,
$$
\boxed{\cardinality{D}=\cardinality{E}}.
$$
:::
