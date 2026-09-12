---
schema: qual/card@1
id: E-YZWG5
kind: problem
title: Separating disjoint compact sets in a Hausdorff space
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
---

::: {.exercise}

Let $A$ and $B$ be disjoint compact subspaces of the Hausdorff space $X$.
Show that there exist disjoint open sets $U$ and $V$ containing $A$ and $B$, respectively.
:::

::: {.solution}
For each \(a\in A\) and \(b\in B\), Hausdorffness gives disjoint open sets \(U_{a,b}\ni a\) and \(V_{a,b}\ni b\). Fix \(a\). The sets \(V_{a,b}\) cover compact \(B\), so choose \(b_1,\dots,b_m\) with
\[
B\subset V_{a,b_1}\cup\cdots\cup V_{a,b_m}.
\]
Set
\[
U_a=\bigcap_{j=1}^m U_{a,b_j},\qquad V_a=\bigcup_{j=1}^m V_{a,b_j}.
\]
Then \(U_a\) is an open neighborhood of \(a\), \(V_a\) is an open neighborhood of \(B\), and \(U_a\cap V_a=\varnothing\).

The sets \(U_a\) cover compact \(A\), so choose \(a_1,\dots,a_r\) with \(A\subset\bigcup_iU_{a_i}\). Define
\[
U=\bigcup_{i=1}^rU_{a_i},\qquad V=\bigcap_{i=1}^rV_{a_i}.
\]
Then \(U\) and \(V\) are open, contain \(A\) and \(B\), respectively, and are disjoint: if \(x\in U\), then \(x\in U_{a_i}\) for some \(i\), while \(V\subset V_{a_i}\), so \(x\notin V\).
:::
