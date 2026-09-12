---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-03
kind: problem
title: A local closure condition implies regularity
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Show that for a topological space $X$, if every $x\in X$ has a neighborhood whose closure is a regular space, then $X$ is regular.
:::

::: {.solution}
We use the neighborhood characterization of regularity: for every \(x\in X\) and every open neighborhood \(U
i x\), it is enough to find an open \(V
i x\) with \(\overline V\subset U\).

Fix \(x\in U\). By hypothesis there is a neighborhood \(N\) of \(x\) such that \(\overline N\), with the subspace topology, is regular. Choose an open set \(G\subset X\) with
\[
x\in G\subset N\cap U.
\]
Then \(G\) is open in the subspace \(\overline N\). By regularity of \(\overline N\), there is a set \(W\), open in \(\overline N\), such that
\[
x\in W,
\qquad
\overline W^{\,\overline N}\subset G.
\]
Write \(W=O\cap\overline N\) for some open \(O\subset X\), and set \(V=O\cap G\). Then \(V\) is open in \(X\), contains \(x\), and \(V\subset W\subset\overline N\). Since \(\overline N\) is closed in \(X\),
\[
\overline V^{\,X}\subset \overline W^{\,\overline N}\subset G\subset U.
\]
Thus \(X\) is regular.
:::
