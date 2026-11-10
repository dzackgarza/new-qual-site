---
schema: qual/card@1
id: E-QBVO3
kind: problem
title: Normality of topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Normal Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked against Munkres, Topology (2000), Section 32 Exercise 10, printed p. 207, and against
    Exercise 32.9 of the same section and Theorem 19.6 (a map into a product is continuous iff its
    components are, printed p. 117), which gives continuity of the group operations of R^J
    coordinatewise. No published solution was located: Orellana's Section 32 stops at Exercise 5, "Doug's
    World" stops at Problem 32.7, and the other retained sets do not reach Chapter 4; the search is
    recorded in the COMPLAINTS.md entry for this batch. What was corrected: the card attributed the
    Stone theorem to "the first exercise of this section", and it is Exercise 9.
---

::: {.exercise}

Is every topological group normal?
:::

::: {.solution}
No. Let $J$ be uncountable. The product group
$$
G=\RR^J
$$
with coordinatewise addition and the product topology is a topological group. By the Stone theorem proved in Exercise 9 of this section, $\RR^J$ is not normal. Therefore not every topological group is normal.
:::
