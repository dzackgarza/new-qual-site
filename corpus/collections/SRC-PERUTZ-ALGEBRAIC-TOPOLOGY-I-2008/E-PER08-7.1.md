---
schema: qual/card@1
id: E-PER08-7.1
kind: problem
title: Perutz Algebraic Topology I Exercise 7.1
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
Show that, in general, Hn(X) = $\\oplus$ Y $\\in$π0(X) Hn(Y ), where π0(X) is the set of path-components of X. Thus H0(X) $\\cong$ Zπ0(X).
:::

::: {.solution}
Every singular simplex has path-connected image, hence its image lies in a unique path component of $X$.
Therefore the singular chain complex decomposes degreewise, compatibly with the boundary maps, as
\[
S_*(X)=\bigoplus_{Y\in\pi_0(X)}S_*(Y).
\]
Kernels and images of a direct sum of chain complexes are the corresponding direct sums, so
\[
H_n(X)\cong\bigoplus_{Y\in\pi_0(X)}H_n(Y).
\]
For every path-connected component $Y$, $H_0(Y)\cong\mathbb Z$.
Hence
\[
H_0(X)\cong\bigoplus_{Y\in\pi_0(X)}\mathbb Z,
\]
the free abelian group on the set $\pi_0(X)$, usually denoted $\mathbb Z[\pi_0(X)]$.
:::
