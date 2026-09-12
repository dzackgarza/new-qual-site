---
schema: qual/card@1
id: E-PROOB
kind: problem
title: Manifolds have dimension at most m
classification:
  areas:
  - topology
  topics:
  - Dimension
  - Manifolds
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Corollary.
Every $m$-manifold has topological dimension at most $m$.
:::

::: {.solution}
Let \(M\) be an \(m\)-manifold. It is Hausdorff and second-countable, hence locally compact and \(\sigma\)-compact.

Let \(K\subset M\) be compact. Cover \(K\) by finitely many coordinate neighborhoods and shrink them so that there are compact sets
\[
K=K_1\cup\cdots\cup K_r
\]
with each \(K_i\) contained in one coordinate chart. Under that chart, \(K_i\) is homeomorphic to a compact, hence closed, subspace of \(\mathbb R^m\). Since \(\dim\mathbb R^m\le m\) and dimension does not increase on closed subspaces,
\[
\dim K_i\le m.
\]
The finite closed-union theorem for dimension then gives \(\dim K\le m\).

Thus every compact subspace of \(M\) has dimension at most \(m\). Applying the preceding \(\sigma\)-compact theorem yields
\[
\boxed{\dim M\le m}.
\]
:::
