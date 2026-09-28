---
schema: qual/card@1
id: E-HAT-4.2-25
kind: problem
title: "Hurewicz cokernel for spaces with few nonzero $\\pi_i$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 25; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
For $X$ a connected CW complex with $\pi_i(X) = 0$ for $1 < i < n$ for some $n \geq 2$, show that $H_n(X) / h\bigl(\pi_n(X)\bigr) \approx H_n\bigl(K(\pi_1(X), 1)\bigr)$, where $h$ is the Hurewicz map.
:::

::: {.solution}
Let \(G=\pi_1(X)\). Since
\[
\pi_i(X)=0\qquad(1<i<n),
\]
we can construct a \(K(G,1)\) from \(X\) by first attaching \((n+1)\)-cells along representatives of elements of \(\pi_n(X)\), killing \(\pi_n\), and then attaching cells of dimensions at least \(n+2\) to kill all remaining higher homotopy groups. Denote the resulting space by \(K\).

The relative cellular chain complex \(C_*(K,X)\) has no generators below degree \(n+1\). Hence the long exact sequence of the pair gives
\[
H_{n+1}(K,X)\xrightarrow{\partial}H_n(X)
\longrightarrow H_n(K)\longrightarrow0.
\]
The relative \((n+1)\)-cells are attached precisely along representatives of \(\pi_n(X)\). Under the connecting map, the class of such a cell goes to the homology class of its attaching map, namely its Hurewicz image. Consequently
\[
\operatorname{im}\partial=h(\pi_n(X)).
\]
Since \(K\simeq K(G,1)\), exactness yields
\[
\boxed{H_n(X)/h(\pi_n(X))\cong H_n(K(\pi_1(X),1)).}
\]
:::
