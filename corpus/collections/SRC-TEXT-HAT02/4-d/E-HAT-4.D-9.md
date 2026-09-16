---
schema: qual/card@1
id: E-HAT-4.D-9
kind: problem
title: "Torus inclusion in $U(n)$ is nullhomotopic"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that the inclusion $T^n \hookrightarrow U(n)$ of the $n$-torus of diagonal matrices is homotopic to the map $T^n \to U(1) \hookrightarrow U(n)$ sending an $n$-tuple of unit complex numbers $(z_1, \ldots, z_n)$ to the $1 \times 1$ matrix $(z_1 \cdots z_n)$.
Do the same for the diagonal subgroup of $Sp(n)$.
:::

::: {.solution}
We first prove the unitary statement. For two diagonal entries,
\[
\operatorname{diag}(z,w)
=\operatorname{diag}(zw,1)\operatorname{diag}(w^{-1},w).
\]
The second factor is a loop in \(SU(2)\cong S^3\), hence is nullhomotopic. Multiplying a chosen nullhomotopy by \(\operatorname{diag}(zw,1)\) gives a homotopy, natural in \((z,w)\), from
\[
\operatorname{diag}(z,w)
\]
to \(\operatorname{diag}(zw,1)\). Applying this successively to adjacent diagonal entries yields a homotopy
\[
\operatorname{diag}(z_1,\ldots,z_n)
\simeq
\operatorname{diag}(z_1\cdots z_n,1,\ldots,1).
\]
Thus the diagonal inclusion \(T^n\hookrightarrow U(n)\) is homotopic to
\[
T^n\xrightarrow{(z_i)\mapsto\prod z_i}U(1)\hookrightarrow U(n).
\]

For \(Sp(n)\), the diagonal subgroup is \(Sp(1)^n=(S^3)^n\). The same reduction works because
\[
\operatorname{diag}(q_1,q_2)
=\operatorname{diag}(q_1q_2,1)\operatorname{diag}(q_2^{-1},q_2).
\]
The map
\[
S^3\to Sp(2),\qquad q\mapsto\operatorname{diag}(q^{-1},q),
\]
is nullhomotopic: under \(\pi_3(Sp(1))\to\pi_3(Sp(2))\cong\mathbb Z\), the two diagonal blocks represent \(-1\) and \(+1\), so their sum is zero. Iterating gives
\[
\boxed{\operatorname{diag}(q_1,\ldots,q_n)
\simeq\operatorname{diag}(q_1\cdots q_n,1,\ldots,1).}
\]
:::
