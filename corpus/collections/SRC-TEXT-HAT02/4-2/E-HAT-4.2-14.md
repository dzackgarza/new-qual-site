---
schema: qual/card@1
id: E-HAT-4.2-14
kind: problem
title: "Inclusion of $S^n$ subcomplex is injective on $\\pi_n$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
If an $n$-dimensional CW complex $X$ contains a subcomplex $Y$ homotopy equivalent to $S^n$, show that the map $\pi_n(Y) \to \pi_n(X)$ induced by inclusion is injective.
:::

::: {.solution}
Let \(i:Y\hookrightarrow X\), where \(X\) is \(n\)-dimensional and \(Y\simeq S^n\).

Assume first \(n\ge2\). Since \(X\) has no \((n+1)\)-cells, an \(n\)-cycle in the cellular chain complex cannot become a boundary after inclusion in \(X\). Thus the inclusion induces an injection
\[
i_*:H_n(Y;\mathbb Z)\hookrightarrow H_n(X;\mathbb Z).
\]
The Hurewicz map
\[
\pi_n(Y)\xrightarrow{\cong}H_n(Y;\mathbb Z)
\]
is an isomorphism because \(Y\simeq S^n\). If \(\alpha\in\pi_n(Y)\) maps to zero in \(\pi_n(X)\), naturality of Hurewicz gives
\[
i_*h(\alpha)=h(i_*\alpha)=0.
\]
Injectivity on \(H_n\) implies \(h(\alpha)=0\), hence \(\alpha=0\). Therefore \(i_*:\pi_n(Y)\to\pi_n(X)\) is injective.

For \(n=1\), \(X\) is a graph, so \(\pi_1(X)\) is free and hence torsionfree. The generator of \(\pi_1(Y)\cong\mathbb Z\) has nonzero image in \(H_1(X)\) by the same cellular-chain argument, so its image in \(\pi_1(X)\) is nontrivial and therefore has infinite order. Thus \(\mathbb Z\to\pi_1(X)\) is injective.

Hence in all cases
\[
\boxed{\pi_n(Y)\hookrightarrow\pi_n(X).}
\]
:::
