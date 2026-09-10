---
schema: qual/card@1
id: E-URH71
kind: problem
title: Countable unions of nowhere dense closed sets in compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $X$ be a compact Hausdorff space, let $\ts{A_n}$ be a countable collection of closed sets of $X$.
Show that if each set $A_n$ has empty interior in $X$, then the union $\bigcup A_n$ has empty interior in $X$.
[Hint: Imitate the proof of Theorem 27.7.]

This is a special case of the Baire category theorem, which we shall study in Chapter 8.
:::

::: {.solution}
Suppose toward a contradiction that \(U\subset\bigcup_{n\ge1}A_n\) for some nonempty open set \(U\subset X\). Since compact Hausdorff spaces are regular, we can construct inductively nonempty open sets \(U_n\) such that
\[
\overline{U_n}\subset U_{n-1}\setminus A_n
\]
for \(n\ge1\), starting with \(U_0=U\). Indeed, \(A_n\) has empty interior, so \(U_{n-1}\setminus A_n\) is a nonempty open set; choose a point there and then a nonempty open neighborhood whose closure is still contained in that open set.

The compact sets
\[
K_n=\overline{U_n}
\]
form a nested sequence
\[
K_1\supset K_2\supset\cdots
\]
of nonempty closed subsets of compact \(X\). Hence
\[
\bigcap_{n\ge1}K_n\ne\varnothing.
\]
Choose \(x\) in the intersection. Since \(K_n\subset X\setminus A_n\), we have \(x\notin A_n\) for every \(n\). Also \(K_1\subset U\), so \(x\in U\). This contradicts \(U\subset\bigcup_nA_n\). Therefore \(\bigcup_nA_n\) has empty interior.
:::
