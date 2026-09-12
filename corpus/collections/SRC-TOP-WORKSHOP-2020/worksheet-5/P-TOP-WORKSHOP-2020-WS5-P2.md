---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS5-P2
kind: problem
title: Compact subspace of a Hausdorff space is closed, and compact Hausdorff implies normal
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Separation Axioms
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
(May 2013)

(a) Prove that every compact subspace of a Hausdorff space is closed.
Show by example that the Hausdorff hypothesis cannot be removed.

(b) Prove that every compact Hausdorff space is normal.
:::

::: {.solution}
(a) Let \(K\subseteq X\) be compact and \(X\) Hausdorff. Fix \(x\in X\setminus K\). For each \(y\in K\), choose disjoint open neighborhoods
\[
x\in U_y,\qquad y\in V_y.
\]
The sets \(V_y\) cover \(K\), so compactness gives \(y_1,\dots,y_n\) with \(K\subseteq\bigcup_iV_{y_i}\). Then
\[
U=\bigcap_{i=1}^nU_{y_i}
\]
is an open neighborhood of \(x\) disjoint from \(K\). Thus \(X\setminus K\) is open and \(K\) is closed.

Hausdorffness is necessary. In the Sierpiński space
\[
X=\{0,1\},\qquad\tau=\{\varnothing,\{1\},X\},
\]
the singleton \(\{1\}\) is compact but not closed.

(b) Let \(A,B\subseteq X\) be disjoint closed subsets of a compact Hausdorff space. They are compact. For each \(a\in A\) and \(b\in B\), choose disjoint open sets \(U_{a,b}\ni a\), \(V_{a,b}\ni b\). For fixed \(a\), compactness of \(B\) gives \(b_1,\dots,b_m\) with \(B\subseteq\bigcup_jV_{a,b_j}\). Set
\[
U_a=\bigcap_jU_{a,b_j},
\qquad
V_a=\bigcup_jV_{a,b_j}.
\]
Then \(a\in U_a\), \(B\subseteq V_a\), and \(U_a\cap V_a=\varnothing\). Compactness of \(A\) gives \(a_1,\dots,a_r\) with \(A\subseteq\bigcup_iU_{a_i}\). Finally set
\[
U=\bigcup_iU_{a_i},
\qquad
V=\bigcap_iV_{a_i}.
\]
Then \(U,V\) are disjoint open sets containing \(A,B\), respectively. Hence \(X\) is normal.
:::
