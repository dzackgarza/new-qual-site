---
schema: qual/card@1
id: D-WSFYS
kind: definition
title: Free product with amalgamation
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Groups
  - Fundamental Group
relations: []
review: draft
---

::: {.definition}
For homomorphisms $i: C\to A$ and $j: C\to B$, the **amalgamated free product** is
\[
A \ast_C B \da \qty{A \ast B} / N
,\]
where $N$ is the normal closure of $\ts{ i(c) j(c)\inv \st c\in C }$.
It is the pushout in $\Grp$.
Van Kampen: if $X = U_1 \union U_2$ with $U_1, U_2, U_1\intersect U_2$ open, path-connected, and containing the basepoint, then
\[
\pi_1(X) \cong \pi_1(U_1) \ast_{\pi_1(U_1 \intersect U_2)} \pi_1(U_2)
.\]
:::

::: {.concept}
See Hatcher, §1.B, p. 92; van Kampen is Theorem 1.20, p. 43.
:::
