---
schema: qual/card@1
id: P-UCTOP290-S13-8
kind: problem
title: A simply connected closed three-manifold is a homology sphere
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Homology
  - Poincaré Duality
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 13, Problem 8 in its checked-in extraction.
---

::: {.problem}
Show that a closed connected simply connected $3$-manifold
has the same integral homology groups as $S^3$.
:::

::: {.solution}

Since $M$ is connected, $H_0(M;\ZZ)=\ZZ$.
Since it is simply connected,
$$
H_1(M;\ZZ)\cong\Ab(\pi_1(M))=0.
$$
The orientation character
$\pi_1(M)\to\ZZ/2$ is trivial, so $M$ is orientable.
Poincaré duality gives
$$
H_3(M;\ZZ)\cong H^0(M;\ZZ)\cong\ZZ
$$
and
$$
H_2(M;\ZZ)\cong H^1(M;\ZZ)=0.
$$
The last equality follows from the universal coefficient
theorem, since $H_1(M)=0$ and $H_0(M)=\ZZ$.
All homology above degree $3$ vanishes. These are exactly
the integral homology groups of $S^3$.

:::
