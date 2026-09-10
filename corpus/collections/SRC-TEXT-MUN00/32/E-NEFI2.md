---
schema: qual/card@1
id: E-NEFI2
kind: problem
title: Regular Lindelof spaces are normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
  - Countability
relations: []
review: draft
---

::: {.exercise}

Show that every regular Lindelöf space is normal.
:::

::: {.solution}
Let \(A,B\subset X\) be disjoint closed sets. Since \(X\) is regular, for each \(a\in A\) choose an open \(U_a\ni a\) with
\[
\overline{U_a}\cap B=\varnothing.
\]
Because closed subspaces of Lindelöf spaces are Lindelöf, \(A\) is Lindelöf. Hence choose a countable family \(U_1,U_2,\dots\) covering \(A\). Similarly choose open sets \(V_1,V_2,\dots\) covering \(B\) with
\[
\overline{V_n}\cap A=\varnothing.
\]

Define
\[
U=\bigcup_{n\ge1}\left(U_n\setminus\bigcup_{i=1}^n\overline{V_i}\right),
\]
\[
V=\bigcup_{n\ge1}\left(V_n\setminus\bigcup_{i=1}^n\overline{U_i}\right).
\]
Each is open. Every \(a\in A\) belongs to some \(U_n\), and \(a\notin\overline{V_i}\) for all \(i\), so \(A\subset U\). Similarly \(B\subset V\).

They are disjoint. If \(x\) belonged to both, choose \(m,n\) such that
\[
x\in U_m\setminus\bigcup_{i\le m}\overline{V_i}
\]
and
\[
x\in V_n\setminus\bigcup_{i\le n}\overline{U_i}.
\]
If \(m\le n\), then \(x\in U_m\subset\overline{U_m}\), contradicting the second membership; if \(n\le m\), then \(x\in V_n\subset\overline{V_n}\), contradicting the first. Thus \(X\) is normal.
:::
