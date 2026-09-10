---
schema: qual/card@1
id: E-L77XX
kind: problem
title: A countably locally finite collection that is neither countable nor locally finite
classification:
  areas:
  - topology
  topics:
  - Local Finiteness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Consider $\mathbb{R}^\omega$ in the uniform topology.
Given $n$, let $\mathcal{B}_n$ be the collection of all subsets of $\mathbb{R}^\omega$ of the form $\prod A_i$, where $A_i = \mathbb{R}$ for $i \leq n$ and $A_i$ equals either $\ts{0}$ or $\ts{1}$ otherwise.
Show that the collection $\mathcal{B} = \bigcup \mathcal{B}_n$ is countably locally finite, but neither countable nor locally finite.
:::

::: {.solution}
Give \(\mathbb R^\omega\) the uniform metric
\[
\bar\rho(x,y)=\sup_i\min\{|x_i-y_i|,1\}.
\]
Fix \(n\). A member of \(\mathcal B_n\) is determined by a binary tail
\[
(\epsilon_{n+1},\epsilon_{n+2},\ldots)\in\{0,1\}^{\{i>n\}},
\]
and has the form
\[
B_\epsilon=\mathbb R^n\times\prod_{i>n}\{\epsilon_i\}.
\]

We first show that \(\mathcal B_n\) is locally finite. Fix \(x\in\mathbb R^\omega\) and use the ball \(B_{\bar\rho}(x,1/3)\). If two members \(B_\epsilon,B_\eta\in\mathcal B_n\) both met this ball, choose \(y\in B_\epsilon\) and \(z\in B_\eta\) in the ball. For every \(i>n\),
\[
|\epsilon_i-x_i|<1/3,
\qquad
|\eta_i-x_i|<1/3.
\]
Since \(\epsilon_i,\eta_i\in\{0,1\}\), the intervals of radius \(1/3\) around \(0\) and \(1\) are disjoint, so \(\epsilon_i=\eta_i\) for every \(i>n\). Thus \(B_\epsilon=B_\eta\). Hence this ball meets at most one member of \(\mathcal B_n\), so \(\mathcal B_n\) is locally finite. Therefore
\[
\mathcal B=\bigcup_{n\ge1}\mathcal B_n
\]
is countably locally finite.

The collection is not countable: already \(\mathcal B_1\) is in bijection with the set of all binary sequences indexed by \(i>1\), hence has cardinality \(2^{\aleph_0}\).

It is not locally finite. Let \(0=(0,0,\ldots)\). For each \(n\), the set
\[
C_n=\mathbb R^n\times\prod_{i>n}\{0\}
\]
belongs to \(\mathcal B_n\), contains \(0\), and the \(C_n\)'s are pairwise distinct. Thus every neighborhood of \(0\) meets infinitely many members of \(\mathcal B\). Hence \(\mathcal B\) is not locally finite.
:::
