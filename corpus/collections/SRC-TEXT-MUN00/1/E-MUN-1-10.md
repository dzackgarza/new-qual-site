---
schema: qual/card@1
id: E-MUN-1-10
kind: problem
title: Cartesian products as subsets of $\RR \times \RR$
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 10; the stored statement matches.
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
    Read against Munkres, Topology (2000), §1 Exercise 10, printed p. 14; the five
    subsets (a)-(e) are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.10,
    printed p. 10 (tmp/sources/munkres-solutions-whitman.pdf). His verdicts are the
    card's, and so are the witnesses: for (c) the points (0,1) and (1,2) forcing
    1 to lie in both factors; for (e) the two axis points (0.9,0) and (0,0.9) forcing
    (0.9,0.9) into the product while it lies outside the disc.
---

::: {.exercise}

Let $\RR$ denote the set of real numbers.
For each of the following subsets of $\RR \times \RR$, determine whether it is equal to the cartesian product of two subsets of $\RR$ .

(a) $\{(x, y) \mid x \text{ is an integer}\}$ .

(b) $\{(x, y) \mid 0 < y \leq 1\}$ .

(c) $\{(x, y) \mid y > x\}$ .

(d) $\{(x, y) \mid x \text{ is not an integer and } y \text{ is an integer}\}$ .

(e) $\{(x, y) \mid x^{2} + y^{2} < 1\}$ .
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.10, printed p. 10** (`tmp/sources/munkres-solutions-whitman.pdf`); the five verdicts and the witnesses for (c) and (e) below are his.

(a) Yes. The set is
$$
\ZZ\times\RR.
$$

(b) Yes. It is
$$
\RR\times(0,1].
$$

(c) No. If the set were $A\times B$, then since $(0,1)$ and $(1,2)$ both satisfy $y>x$, we would have
$$
0,1\in A,\qquad 1,2\in B.
$$
Hence $(1,1)\in A\times B$, contradicting $1\not>1$.

(d) Yes. It is
$$
(\RR-\ZZ)\times\ZZ.
$$

(e) No. If the open unit disk were $A\times B$, then from
$$
(0.9,0),\ (0,0.9)
$$
being in the disk we would obtain $0.9,0\in A$ and $0,0.9\in B$. Thus $(0.9,0.9)\in A\times B$, but
$$
0.9^2+0.9^2=1.62>1,
$$
so this point is not in the disk, a contradiction.
:::
