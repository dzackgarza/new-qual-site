---
schema: qual/card@1
id: E-QIADW
kind: problem
title: Locally compact connected topological groups are paracompact
classification:
  areas:
  - topology
  topics:
  - Paracompactness
  - Topological Groups
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

Let $G$ be a locally compact, connected topological group.
Show that $G$ is paracompact.
[Hint: Let $U_1$ be a neighborhood of $e$ having compact closure. In general, define $U_{n+1} = \overline{U}_n \cdot U_1$. Show the union of the sets $\overline{U}_n$ is both open and closed in $G$.]

This result holds without assuming $G$ is connected, but the proof requires more effort.
:::

::: {.solution}
Because \(G\) is locally compact Hausdorff, choose a symmetric open neighborhood \(U\) of the identity \(e\) whose closure
\[
K=\overline U
\]
is compact. Replacing \(U\) by \(U\cap U^{-1}\) if necessary preserves compact closure and makes \(K=K^{-1}\).

Set
\[
H=\bigcup_{n\ge1}K^n.
\]
Each \(K^n\) is compact, since multiplication \(G^n\to G\) is continuous. Also \(H\) is a subgroup: \(e\in K\), products send \(K^mK^n\) into \(K^{m+n}\), and symmetry of \(K\) gives closure under inverses. Since \(U\subset K\subset H\), the subgroup \(H\) contains an open neighborhood of the identity, hence \(H\) is open. Every open subgroup of a topological group is also closed, since its other cosets are open. Connectedness of \(G\) therefore forces \(H=G\).

Thus
\[
G=\bigcup_{n\ge1}K^n
\]
is \(\sigma\)-compact. Hausdorff topological groups are regular, so Exercise `E-KVFCT` applies: every regular \(\sigma\)-compact space is paracompact. Hence \(G\) is paracompact.
:::
