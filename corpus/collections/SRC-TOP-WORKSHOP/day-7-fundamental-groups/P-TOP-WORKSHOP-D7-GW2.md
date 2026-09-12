---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-GW2
kind: problem
title: Nonhomeomorphic spaces with isomorphic nontrivial fundamental groups (warm-up)
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homeomorphisms
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Find two spaces $X$ and $Y$ such that $\pi_1(X)\cong\pi_1(Y)$ and are non-trivial, and are NOT homeomorphic.
:::

::: {.solution}
Take
\[
X=S^1,\qquad Y=S^1\vee S^2.
\]
By van Kampen, since \(S^2\) is simply connected,
\[
\pi_1(Y)\cong\pi_1(S^1)*\pi_1(S^2)\cong\mathbb Z\cong\pi_1(X),
\]
so the common fundamental group is nontrivial.

The spaces are not homeomorphic. Indeed,
\[
H_2(S^1)=0,
\qquad
H_2(S^1\vee S^2)\cong H_2(S^2)\cong\mathbb Z.
\]
Homeomorphic spaces have isomorphic singular homology groups, so \(X\not\cong Y\).
:::
