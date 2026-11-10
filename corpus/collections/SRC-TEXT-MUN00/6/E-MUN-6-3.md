---
schema: qual/card@1
id: E-MUN-6-3
kind: problem
title: Binary sequences are in bijection with a proper subset
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 3; the stored statement matches.
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
    Read against Munkres, Topology (2000), §6 Exercise 3, printed p. 44; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.3,
    printed p. 76 (tmp/sources/munkres-solutions-whitman.pdf). He uses the same proper
    subset, the sequences beginning with 0, and the map that shifts the input one place
    to the right behind a leading 0; the card writes that map and its inverse and checks
    both composites. No defect found.
---

::: {.exercise}

Let $X$ be the two-element set $\{0,1\}$ . Find a bijective correspondence between $X^{\omega}$ and a proper subset of itself.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.3, printed p. 76** (`tmp/sources/munkres-solutions-whitman.pdf`); the proper subset and the one-place shift with a leading $0$ are his.

Let
$$
P=\{(y_1,y_2,\dots)\in X^\omega:y_1=0\}.
$$
This is a proper subset of $X^\omega$, since for example $(1,0,0,\dots)\notin P$.

Define
$$
F:X^\omega\longrightarrow P,
\qquad
F(x_1,x_2,x_3,\dots)=(0,x_1,x_2,x_3,\dots).
$$
The inverse map is the left shift
$$
G(0,y_2,y_3,\dots)=(y_2,y_3,\dots).
$$
Then $GF=\mathrm{id}_{X^\omega}$ and $FG=\mathrm{id}_P$. Thus $F$ is a bijection of $X^\omega$ with the proper subset $P$.
:::
