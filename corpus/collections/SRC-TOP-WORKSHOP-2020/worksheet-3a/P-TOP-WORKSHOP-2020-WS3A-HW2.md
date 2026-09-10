---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3A-HW2
kind: problem
title: 'Seifert–van Kampen theorem'
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
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
State the Seifert--van Kampen Theorem.
:::

::: {.solution}
Let \(X=U\cup V\), where \(U,V\subseteq X\) are open and path connected, \(U\cap V\) is path connected, and choose a basepoint \(x_0\in U\cap V\). Let
\[
i_U:U\cap V\hookrightarrow U,
\qquad
i_V:U\cap V\hookrightarrow V
\]
be the inclusions. Then the inclusion maps \(U,V\hookrightarrow X\) induce a surjective homomorphism
\[
\pi_1(U,x_0)*\pi_1(V,x_0)\twoheadrightarrow\pi_1(X,x_0),
\]
and its kernel is the normal closure of all elements
\[
i_{U*}(\omega)i_{V*}(\omega)^{-1},
\qquad
\omega\in\pi_1(U\cap V,x_0).
\]
Equivalently,
\[
\pi_1(X,x_0)
\cong
\pi_1(U,x_0)*_{\pi_1(U\cap V,x_0)}\pi_1(V,x_0),
\]
the pushout (amalgamated free product) of the two induced maps on fundamental groups.
:::
