---
schema: qual/card@1
id: E-MUN-6-7
kind: problem
title: Finiteness of function sets between finite sets
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

If $A$ and $B$ are finite, show that the set of all functions $f: A \to B$ is finite.
:::

::: {.solution}
Let \(|A|=n\) and \(|B|=m\). After choosing a bijection
\[
A\cong\{1,\dots,n\},
\]
a function \(f:A\to B\) is uniquely determined by the \(n\)-tuple
\[
(f(1),\dots,f(n))\in B^n.
\]
Thus the set \(B^A\) of all functions \(A\to B\) is in bijection with \(B^n\). A finite cartesian product of finite sets is finite, so \(B^n\), and hence \(B^A\), is finite.

More precisely, when \(n,m>0\),
\[
|B^A|=m^n.
\]
If \(A=\varnothing\), there is exactly one function \(A\to B\); if \(B=\varnothing\) and \(A\ne\varnothing\), there are none. These cases are finite as well.
:::
