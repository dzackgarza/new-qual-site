---
schema: qual/card@1
id: E-OSQTJ
kind: problem
title: Compact contractible subsets of the sphere do not separate
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
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

Let $A$ be a compact contractible subspace of $S^2$.
Show that $A$ does not separate $S^2$.
:::

::: {.solution}
Let \(A\subset S^2\) be compact and contractible. Suppose, for contradiction, that \(A\) separates \(S^2\). Choose points \(a,b\) in two distinct components of \(S^2-A\).

Since \(A\) is contractible, the inclusion
\[
i:A\hookrightarrow S^2-\{a,b\}
\]
is nullhomotopic: contract \(A\) to any point \(a_0\in A\), and regard the contraction as taking place inside \(A\subset S^2-\{a,b\}\).

Identify
\[
S^2-\{a,b\}\cong S^1\times\mathbb R.
\]
The Borsuk lemma from this section says that if a compact subset of \(S^2\) separates two points \(a,b\), then its inclusion in the twice-punctured sphere cannot be nullhomotopic; equivalently, a compact set with nullhomotopic inclusion into \(S^2-\{a,b\}\) cannot separate \(a\) from \(b\). This contradicts the preceding paragraph.

Hence \(S^2-A\) is connected: a compact contractible subset of \(S^2\) does not separate the sphere.
:::
