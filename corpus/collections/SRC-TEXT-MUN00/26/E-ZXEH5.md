---
schema: qual/card@1
id: E-ZXEH5
kind: problem
title: Generalized tube lemma for compact rectangles
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
---

::: {.exercise}

Generalize the tube lemma as follows.

Theorem.
Let $A$ and $B$ be subspaces of $X$ and $Y$, respectively; let $N$ be an open set in $X \times Y$ containing $A \times B$.
If $A$ and $B$ are compact, then there exist open sets $U$ and $V$ in $X$ and $Y$, respectively, such that

$$
A \times B \subset U \times V \subset N.
$$
:::

::: {.solution}
For each \(a\in A\), the slice \(\{a\}\times B\) is compact, since it is homeomorphic to compact \(B\), and it is contained in open \(N\). By the tube lemma there exist an open neighborhood \(U_a\) of \(a\) and an open set \(V_a\supset B\) such that
\[
U_a\times V_a\subset N.
\]
The sets \(U_a\) cover compact \(A\), so choose \(a_1,\dots,a_m\) with
\[
A\subset U_{a_1}\cup\cdots\cup U_{a_m}.
\]
Set
\[
U=\bigcup_{i=1}^mU_{a_i},\qquad V=\bigcap_{i=1}^mV_{a_i}.
\]
Then \(U\) and \(V\) are open, \(A\subset U\), and \(B\subset V\). If \((x,y)\in U\times V\), choose \(i\) with \(x\in U_{a_i}\). Since \(y\in V\subset V_{a_i}\), we have \((x,y)\in U_{a_i}\times V_{a_i}\subset N\). Hence
\[
A\times B\subset U\times V\subset N.
\]
:::
