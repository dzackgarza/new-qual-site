---
schema: qual/card@1
id: E-HAT-4.3-21
kind: problem
title: "H-space Postnikov towers"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 21; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

---

::: {.problem}
Show that in the Postnikov tower of an H-space, all the spaces are H-spaces and the maps are H-maps, commuting with the multiplication, up to homotopy.
:::

::: {.solution}
Let $P_nX$ denote the $n$-th Postnikov stage. The Postnikov construction is functorial up to homotopy, and
$$
P_n(X\times X)\simeq P_nX\times P_nX
$$
because both sides have the same homotopy groups through degree $n$ and none above.

If
$$
\mu:X\times X\to X
$$
is an H-space multiplication, apply $P_n$ to obtain
$$
P_n\mu:P_n(X\times X)\to P_nX.
$$
Using the displayed product identification gives a multiplication
$$
\mu_n:P_nX\times P_nX\to P_nX.
$$
The unit homotopies, associativity homotopy, and any inverse homotopy for $\mu$ pass functorially to $P_nX$, so each $P_nX$ is an H-space.

Naturality of Postnikov truncation makes every tower map
$$
P_nX\to P_{n-1}X
$$
commute with these multiplications up to homotopy. Hence
$$
\boxed{\text{all stages are H-spaces and all Postnikov tower maps are H-maps}.}
$$
:::
