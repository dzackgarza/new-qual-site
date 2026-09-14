---
schema: qual/card@1
id: P-WESRA04-P3
kind: problem
title: Absolutely continuous functions map null sets to null sets
classification:
  areas: [real-analysis]
  topics: [Absolute Continuity, Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.3, problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $g:[0,1]\to\mathbb R$ be absolutely continuous and let $E\subset[0,1]$ have Lebesgue measure zero.
Prove that $g(E)$ has Lebesgue measure zero.
:::

::: solution
Fix $\varepsilon>0$.
By absolute continuity of $g$, there exists $\delta>0$ such that for every finite family of pairwise disjoint intervals $(a_j,b_j)\subset[0,1]$ satisfying
\[
\sum_j(b_j-a_j)<\delta,
\]
one has
\[
\sum_j|g(b_j)-g(a_j)|<\varepsilon.
\]

Since $m(E)=0$, choose an open set $U\subset\mathbb R$ with
\[
E\subset U
\qquad\text{and}\qquad
m(U\cap[0,1])<\delta.
\]
Write the relatively open set $U\cap[0,1]$ as a countable disjoint union of intervals $I_k$.
For each $k$, the oscillation of $g$ on $I_k$ is at most the total variation of $g$ on $I_k$.
For any finite set of indices and any finite partitions of the corresponding $I_k$, the total length of all partition intervals is less than $\delta$; absolute continuity therefore gives
\[
\sum_k V(g;I_k)\le\varepsilon,
\]
where the sum is understood as the supremum of its finite partial sums.

Because $g(I_k)$ is an interval (possibly with endpoints omitted) and
\[
m^*(g(I_k))\le \operatorname{diam} g(I_k)\le V(g;I_k),
\]
we obtain
\[
m^*(g(E))
\le \sum_k m^*(g(I_k))
\le \sum_k V(g;I_k)
\le\varepsilon.
\]
Since $\varepsilon>0$ was arbitrary,
\[
\boxed{m(g(E))=0.}
\]
:::
