---
schema: qual/card@1
id: P-UCTOP290-S13-9
kind: problem
title: Every map from the sphere to the torus has degree zero
classification:
  areas:
  - topology
  topics:
  - Degree
  - Cohomology Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 13, Problem 9 in its checked-in extraction.
---

::: {.problem}
Use cohomology rings to show that every map
$f:S^2\to T^2$ has degree zero.
:::

::: {.solution}

Choose generators $u,v\in H^1(T^2;\ZZ)$ so that
$u\smile v$ is the orientation class in
$H^2(T^2;\ZZ)$. Since $H^1(S^2;\ZZ)=0$,
$$
f^*u=f^*v=0.
$$
Naturality of the cup product gives
$$
f^*(u\smile v)
=f^*u\smile f^*v
=0.
$$
On top cohomology, $f^*$ multiplies the orientation
class by $\deg f$. Since $H^2(S^2;\ZZ)\cong\ZZ$,
the displayed equality forces $\deg f=0$.

:::
