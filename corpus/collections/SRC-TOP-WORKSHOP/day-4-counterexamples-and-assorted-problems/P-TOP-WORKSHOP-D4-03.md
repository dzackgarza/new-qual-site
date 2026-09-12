---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-03
kind: problem
title: The compact-complement topology is coarser than a Hausdorff topology
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Point-Set Topology
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
(Jan ’04 # A3) Let $(X,\tau)$ be a Hausdorff space and let $$\tau'=\{U\subseteq X\mid X\setminus U\text{ is compact}\}\cup\{\varnothing\}.$$ Show that $\tau'$ is a topology on $X$ and is coarser than $\tau$.
Show that, in general, they need not be equal.
:::

::: {.solution}
We first verify the topology axioms for
\[
\tau'=\{U\subseteq X:X\setminus U\text{ is compact}\}\cup\{\varnothing\}.
\]
Clearly \(\varnothing,X\in\tau'\). If \(U_i\in\tau'\), then
\[
X\setminus\bigcup_iU_i=\bigcap_i(X\setminus U_i).
\]
Choose one nonempty \(U_j\) if there is one. The set on the right is closed in the compact set \(X\setminus U_j\), because each compact subset of a Hausdorff space is closed. Hence it is compact. Thus arbitrary unions lie in \(\tau'\). If \(U_1,\dots,U_n\in\tau'\), then
\[
X\setminus\bigcap_{k=1}^nU_k=\bigcup_{k=1}^n(X\setminus U_k),
\]
a finite union of compact sets, hence compact. Thus \(\tau'\) is a topology.

Since \(X\) is Hausdorff, every compact subset of \(X\) is \(\tau\)-closed. Therefore every nonempty \(U\in\tau'\) is \(\tau\)-open, so \(\tau'\subseteq\tau\).

Equality need not hold. Take \(X=\mathbb R\) with its usual topology. Then \((-1,1)\in\tau\), but
\[
\mathbb R\setminus(-1,1)=(-\infty,-1]\cup[1,\infty)
\]
is not compact. Hence \((-1,1)\notin\tau'\), so \(\tau'\ne\tau\).
:::
