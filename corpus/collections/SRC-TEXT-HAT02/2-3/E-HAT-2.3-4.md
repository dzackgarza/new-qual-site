---
schema: qual/card@1
id: E-HAT-2.3-4
kind: problem
title: Wedge axiom follows from other axioms for finite wedge sums
classification:
  areas:
  - topology
  topics:
  - Homology
  - Axiomatic Homology
  - Wedge Sums
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.3, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that the wedge axiom for homology theories follows from the other axioms in the case of finite wedge sums.


::: {.solution}
It suffices to prove the binary case and then induct.

Let $X\vee Y$ be the wedge at the common basepoint $*$. Regard $X$ as a subcomplex of $X\vee Y$. Then
\[
(X\vee Y)/X\cong Y.
\]

<1>1. The long exact sequence of the pair $(X\vee Y,X)$ splits into short exact sequences
\[
0\longrightarrow\widetilde h_n(X)
\longrightarrow\widetilde h_n(X\vee Y)
\longrightarrow\widetilde h_n(Y)\longrightarrow0.
\]
::: {.proof}
By excision,
\[
\widetilde h_n(X\vee Y,X)\cong\widetilde h_n(Y,* )\cong\widetilde h_n(Y).
\]
The retraction $r:X\vee Y\to X$ collapsing $Y$ to the wedge point satisfies $r\circ i=\mathrm{id}_X$. Hence $i_*:\widetilde h_n(X)\to\widetilde h_n(X\vee Y)$ is split injective. Exactness then forces the connecting map from the relative group to $\widetilde h_{n-1}(X)$ to vanish, giving the displayed short exact sequence.
:::

<1>2. The sequence splits naturally, so
\[
\widetilde h_n(X\vee Y)\cong
\widetilde h_n(X)\oplus\widetilde h_n(Y).
\]
::: {.proof}
The retraction $X\vee Y\to Y$ collapsing $X$ supplies a section of the quotient-induced map to the relative group. Equivalently, the two inclusions induce the direct-sum map, and the two retractions give its inverse.
:::

Iterating the binary isomorphism gives the wedge axiom for every finite wedge.
:::
