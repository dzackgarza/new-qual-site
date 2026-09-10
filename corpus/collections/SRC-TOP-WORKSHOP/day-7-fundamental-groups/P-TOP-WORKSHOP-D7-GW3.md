---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-GW3
kind: problem
title: Fundamental group of the torus $T^2=S^1\times S^1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
  - van Kampen
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
Find $\pi_1(T^2)$, where $T^2=S^1\times S^1$ is the standard two torus, in TWO different ways.
:::

::: {.solution}
First, use the product theorem for fundamental groups:
\[
\pi_1(S^1\times S^1,(1,1))
\cong \pi_1(S^1,1)\times\pi_1(S^1,1)
\cong \mathbb Z\times\mathbb Z.
\]

Second, use the standard square CW structure on the torus. After identifying opposite edges, there is one \(0\)-cell, two \(1\)-cells \(a,b\), and one \(2\)-cell whose attaching map follows the boundary word
\[
aba^{-1}b^{-1}.
\]
Van Kampen therefore gives
\[
\pi_1(T^2)\cong\langle a,b\mid aba^{-1}b^{-1}=1\rangle.
\]
The single relation says exactly that \(a\) and \(b\) commute, so this group is
\[
\mathbb Z^2.
\]
Thus both methods give
\[
\boxed{\pi_1(T^2)\cong\mathbb Z\oplus\mathbb Z}.
\]
:::
