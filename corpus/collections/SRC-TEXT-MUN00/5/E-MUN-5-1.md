---
schema: qual/card@1
id: E-MUN-5-1
kind: problem
title: Bijection between $A \times B$ and $B \times A$
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 1; the stored statement matches.
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
    Read against Munkres, Topology (2000), §5 Exercise 1, printed p. 38; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 5.1,
    printed p. 67 (tmp/sources/munkres-solutions-whitman.pdf). He checks injectivity
    and surjectivity of (a,b) -> (b,a) separately and notes the empty case; the card
    observes that the map is its own inverse, which gives both at once. No defect.
---

::: {.exercise}

Show there is a bijective correspondence of $A \times B$ with $B \times A$ .
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.1, printed p. 67** (`tmp/sources/munkres-solutions-whitman.pdf`), which checks injectivity and surjectivity of $(a,b)\mapsto(b,a)$ separately and notes that the case $A\times B=\varnothing$ is vacuous; since the map below is its own inverse, one check gives both.

Define
$$
\tau:A\times B\longrightarrow B\times A,
\qquad
\tau(a,b)=(b,a).
$$
Then $\tau$ is its own inverse:
$$
\tau(\tau(a,b))=(a,b).
$$
Hence $\tau$ is bijective.
:::
