---
schema: qual/card@1
id: E-YGD3Z
kind: problem
title: Properties of the total space of a covering
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
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

Let $p: E \to B$ be a covering map.

(a) If $B$ is Hausdorff, regular, completely regular, or locally compact Hausdorff, then so is $E$.
[Hint: If $\ts{V_\alpha}$ is a partition of $p^{-1}(U)$ into slices, and $C$ is a closed set of $B$ such that $C \subset U$, then $p^{-1}(C) \cap V_\alpha$ is a closed set of $E$.]

(b) If $B$ is compact and $p^{-1}(b)$ is finite for each $b \in B$, then $E$ is compact.
:::

::: {.solution}
(a) Every point \(e\in E\) has an open slice \(V\) such that \(p|_V:V\to U\) is a homeomorphism onto an open subset \(U\subset B\). Thus all local properties in the list transfer immediately; the separation properties require checking globally.

If \(B\) is Hausdorff and \(e_1\ne e_2\), then if \(p(e_1)\ne p(e_2)\), separate their images and pull back the disjoint neighborhoods. If \(p(e_1)=p(e_2)\), choose one evenly covered neighborhood of their common image; the two points lie in distinct disjoint slices. Hence \(E\) is Hausdorff.

Assume next that \(B\) is regular. Let \(e\in E\) and let \(O\) be an open neighborhood of \(e\). Choose a slice \(V\) over an open set \(U\) with \(e\in V\subset O\). Put \(b=p(e)\). Regularity of \(B\) gives an open \(W\) with
\[
b\in W\subset\overline W\subset U.
\]
Then
\[
N=V\cap p^{-1}(W)
\]
is an open neighborhood of \(e\), and
\[
\overline N\subset V\cap p^{-1}(\overline W)\subset V\subset O.
\]
The hinted closedness statement justifies the middle containment: because the slices over \(U\) are disjoint and \(\overline W\subset U\), the set \(V\cap p^{-1}(\overline W)\) is closed in \(E\). Hence \(E\) is regular.

If \(B\) is completely regular, let \(F\subset E\) be closed and \(e\notin F\). Choose a slice \(V\) over \(U\) with \(e\in V\) and then, by regularity already proved, shrink so that an open \(N\ni e\) has \(\overline N\subset V-F\). On the homeomorphic base slice one can separate \(e\) from \(V- N\) by a continuous \([0,1]\)-valued function; extending it by the constant \(1\) outside \(V\) is continuous after choosing the function equal to \(1\) on a neighborhood of the boundary of \(V\). Thus points and closed sets are functionally separable, so \(E\) is completely regular.

If \(B\) is locally compact Hausdorff, choose an evenly covered neighborhood \(U\) of \(p(e)\) and then an open \(W\ni p(e)\) with compact closure \(\overline W\subset U\). In the slice \(V\) containing \(e\),
\[
V\cap p^{-1}(\overline W)
\]
is homeomorphic to the compact space \(\overline W\), hence compact, and contains the open neighborhood \(V\cap p^{-1}(W)\) of \(e\). Thus \(E\) is locally compact Hausdorff.

(b) Let \(\mathcal U\) be an arbitrary open cover of \(E\). Fix \(b\in B\). Since the fiber
\[
p^{-1}(b)=\{e_1,\dots,e_r\}
\]
is finite, choose \(U_j\in\mathcal U\) with \(e_j\in U_j\). Choose one evenly covered neighborhood \(V\) of \(b\), with slices \(V_1,\dots,V_r\) containing \(e_1,\dots,e_r\), respectively. For each \(j\), because \(p|_{V_j}:V_j\to V\) is a homeomorphism and \(U_j\cap V_j\) is a neighborhood of \(e_j\), there is an open neighborhood \(W_j\subset V\) of \(b\) such that
\[
(p|_{V_j})^{-1}(W_j)\subset U_j.
\]
Set \(W_b=\bigcap_{j=1}^rW_j\). Then \(W_b\) is an open neighborhood of \(b\), and
\[
p^{-1}(W_b)\subset U_1\cup\cdots\cup U_r.
\]

The sets \(W_b\) cover the compact space \(B\), so finitely many, say \(W_{b_1},\dots,W_{b_N}\), cover \(B\). For each \(i\), the set \(p^{-1}(W_{b_i})\) is covered by finitely many members of \(\mathcal U\). Taking the union of these finitely many finite subcollections gives a finite subcover of \(E\). Therefore \(E\) is compact.
:::
