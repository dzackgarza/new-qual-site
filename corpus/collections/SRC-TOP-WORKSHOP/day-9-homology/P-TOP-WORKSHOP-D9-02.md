---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-02
kind: problem
title: Fundamental group and homology of the mapping torus of $z\mapsto z^4$ on $S^1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Quotient Spaces
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
(Michigan Jan ’10) Let $S^1=\{z\in\mathbb C\mid |z|=1\}$.
Let $X$ be obtained from the space $S^1\times[0,1]$ by identifying every point $(z,0)$ with the point $(z^4,1)$, with the quotient topology.
Compute the fundamental group and homology of $X$.
:::

::: {.solution}
Let \(a\) denote the loop around the \(S^1\)-fiber and \(t\) the loop obtained by moving once in the \([0,1]\)-direction and using the endpoint identification. The identification has degree \(4\) on the circle, so van Kampen gives the Baumslag--Solitar presentation
\[
\pi_1(X)\cong\langle a,t\mid tat^{-1}=a^4\rangle.
\]

For homology, use the Wang exact sequence for the mapping torus of the degree-\(4\) map \(f:S^1\to S^1\):
\[
\cdots\to H_n(S^1)\xrightarrow{1-f_*}H_n(S^1)\to H_n(X)
\to H_{n-1}(S^1)\xrightarrow{1-f_*}H_{n-1}(S^1)\to\cdots.
\]
On \(H_1(S^1)=\mathbb Z\), \(1-f_*\) is multiplication by \(1-4=-3\), while on \(H_0(S^1)=\mathbb Z\) it is \(0\). Therefore
\[
H_2(X)=\ker(\mathbb Z\xrightarrow{-3}\mathbb Z)=0,
\]
and the degree-one part gives
\[
0\to\mathbb Z/3\to H_1(X)\to\mathbb Z\to0.
\]
Since \(\mathbb Z\) is free, this splits, so
\[
H_1(X)\cong\mathbb Z\oplus\mathbb Z/3.
\]
Also \(H_0(X)=\mathbb Z\), and \(H_n(X)=0\) for \(n\ge2\). Equivalently, \(H_1\) is the abelianization of the displayed fundamental-group presentation: the relation becomes \(3a=0\), while \(t\) remains infinite cyclic.
:::
