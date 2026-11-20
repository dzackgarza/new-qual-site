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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §5 Exercise 1, printed p. 28, and the argument follows the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.1, printed p. 67, who checks injectivity and surjectivity of the swap map separately. The card observes that the map is its own inverse, which gives both at once; the empty case is included because the argument is vacuous there rather than excluded.
---

::: {.exercise}

Show there is a bijective correspondence of $A \times B$ with $B \times A$ .
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.1** (`tmp/sources/munkres-solutions-whitman.pdf`), which checks injectivity and surjectivity of $(a,b)\mapsto(b,a)$ separately and notes that the case $A\times B=\varnothing$ is vacuous; since the map below is its own inverse, one check gives both. The statement is Munkres, *Topology* (2000), §5 Exercise 1.

::: pf

::: {.pf-step #map}
The formula $\tau(a,b)\coloneqq(b,a)$ defines a function $\tau:A\times B\to B\times A$.

::: pf-proof
For $(a,b)\in A\times B$ the pair $(b,a)$ has its first entry in $B$ and its second in $A$, so it lies in $B\times A$; and it is determined by $(a,b)$.
:::
:::

::: {.pf-step #inverse}
$\tau(\tau(a,b))=(a,b)$ for every $(a,b)\in A\times B$, and likewise in the other order.

::: pf-proof
Apply the formula twice: $\tau(\tau(a,b))=\tau(b,a)=(a,b)$. Symmetrically, for $(b,a)\in B\times A$ the same computation gives $(b,a)$ back, so the formula also defines a map $B\times A\to A\times B$ inverse to $\tau$.
:::
:::

::: {.pf-step #bijective}
$\tau$ is bijective.

::: pf-proof
Step [](#inverse){.pf-ref} exhibits a two-sided inverse, so $\tau$ is both injective and surjective. If $A\times B$ is empty the same computation applies vacuously, and both sides are empty.
:::
:::

::: {.pf-step}
There is a bijective correspondence of $A\times B$ with $B\times A$, namely $\tau$.

::: pf-proof
Step [](#map){.pf-ref} gives the function and step [](#bijective){.pf-ref} its bijectivity.
:::
:::

:::
:::
