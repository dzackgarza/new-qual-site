---
schema: qual/card@1
id: E-HAT-4.1-17
kind: problem
title: "Connectivity of products and smash products"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 17; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Show that if $X$ and $Y$ are CW complexes with $X$ $m$-connected and $Y$ $n$-connected, then $(X \times Y, X \vee Y)$ is $(m+n+1)$-connected, as is the smash product $X \wedge Y$.
:::

::: {.solution}
By the CW version of the relative Hurewicz/cellular approximation argument, an \(m\)-connected CW complex is homotopy equivalent to a CW complex with one \(0\)-cell and no cells in dimensions \(1,\dots,m\). Likewise, replace \(Y\) by a CW model with no positive-dimensional cells below dimension \(n+1\). This replacement does not change the connectivity assertion.

Give \(X\times Y\) the product CW structure. Relative to
\[
X\vee Y=(X\times\{y_0\})\cup(\{x_0\}\times Y),
\]
the cells are precisely products
\[
e^p\times e^q
\]
with \(p,q>0\). By the chosen CW structures,
\[
p\ge m+1,
\qquad q\ge n+1,
\]
so every relative cell has dimension at least
\[
(m+1)+(n+1)=m+n+2.
\]
Hence the relative CW pair
\[
(X\times Y,X\vee Y)
\]
has no relative cells in dimensions at most \(m+n+1\). Cellular approximation therefore gives
\[
\pi_i(X\times Y,X\vee Y)=0
\qquad(i\le m+n+1).
\]
Thus the pair is \((m+n+1)\)-connected.

Since \(X\vee Y\hookrightarrow X\times Y\) is a cofibration, the quotient map identifies relative homotopy with the homotopy of the quotient in this range, and
\[
(X\times Y)/(X\vee Y)=X\wedge Y.
\]
Equivalently, the quotient CW structure on \(X\wedge Y\) has no positive-dimensional cells below dimension \(m+n+2\). Therefore
\[
\pi_i(X\wedge Y)=0
\qquad(i\le m+n+1),
\]
so
\[
\boxed{(X\times Y,X\vee Y)\text{ and }X\wedge Y\text{ are }(m+n+1)\text{-connected}.}
\]
:::
