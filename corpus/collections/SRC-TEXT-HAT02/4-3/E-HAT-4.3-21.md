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
---

::: {.problem}
Show that in the Postnikov tower of an H-space, all the spaces are H-spaces and the maps are H-maps, commuting with the multiplication, up to homotopy.
:::

::: {.solution}
Let \(P_nX\) denote the \(n\)-th Postnikov stage. The Postnikov construction is functorial up to homotopy, and
\[
P_n(X\times X)\simeq P_nX\times P_nX
\]
because both sides have the same homotopy groups through degree \(n\) and none above.

If
\[
\mu:X\times X\to X
\]
is an H-space multiplication, apply \(P_n\) to obtain
\[
P_n\mu:P_n(X\times X)\to P_nX.
\]
Using the displayed product identification gives a multiplication
\[
\mu_n:P_nX\times P_nX\to P_nX.
\]
The unit homotopies, associativity homotopy, and any inverse homotopy for \(\mu\) pass functorially to \(P_nX\), so each \(P_nX\) is an H-space.

Naturality of Postnikov truncation makes every tower map
\[
P_nX\to P_{n-1}X
\]
commute with these multiplications up to homotopy. Hence
\[
\boxed{\text{all stages are H-spaces and all Postnikov tower maps are H-maps}.}
\]
:::
