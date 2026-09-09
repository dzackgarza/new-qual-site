---
schema: qual/card@1
id: E-HAT-3.3-25
kind: problem
title: "Torsionfree $H_{k-1}$ implies torsionfree $H_k$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 25; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that if a closed orientable manifold $M$ of dimension $2k$ has $H_{k-1}(M; \mathbb{Z})$ torsionfree, then $H_k(M; \mathbb{Z})$ is also torsionfree.

::: {.solution}
Since $M$ is a closed manifold, all its homology groups are finitely generated. Thus the hypothesis that $H_{k-1}(M;\mathbb Z)$ is torsionfree implies that it is free abelian, and therefore
\[
\operatorname{Ext}(H_{k-1}(M;\mathbb Z),\mathbb Z)=0.
\]
The universal coefficient theorem for cohomology gives
\[
0\to \operatorname{Ext}(H_{k-1}(M),\mathbb Z)
\to H^k(M;\mathbb Z)
\to \operatorname{Hom}(H_k(M),\mathbb Z)\to0,
\]
so
\[
H^k(M;\mathbb Z)\cong\operatorname{Hom}(H_k(M),\mathbb Z).
\]
The group on the right is free abelian.

Poincaré duality for the closed orientable $2k$-manifold $M$ gives
\[
H^k(M;\mathbb Z)\cong H_{2k-k}(M;\mathbb Z)=H_k(M;\mathbb Z).
\]
Hence $H_k(M;\mathbb Z)$ is free abelian, in particular torsionfree.
:::
