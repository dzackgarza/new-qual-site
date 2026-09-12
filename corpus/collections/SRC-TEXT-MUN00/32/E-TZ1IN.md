---
schema: qual/card@1
id: E-TZ1IN
kind: problem
title: Complete normality characterized by separated sets
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
---

::: {.exercise}

A space $X$ is said to be completely normal if every subspace of $X$ is normal.
Show that $X$ is completely normal if and only if for every pair $A, B$ of separated sets in $X$ (that is, sets such that $\overline{A} \cap B = \varnothing$ and $A \cap \overline{B} = \varnothing$), there exist disjoint open sets containing them.
[Hint: If $X$ is completely normal, consider $X - (\overline{A} \cap \overline{B})$.]
:::

::: {.solution}
Suppose first that \(X\) is completely normal, and let \(A,B\subset X\) be separated:
\[
\overline A\cap B=\varnothing,
\qquad
A\cap\overline B=\varnothing.
\]
Set
\[
Y=X\setminus(\overline A\cap\overline B).
\]
The subspace \(Y\) is normal. In \(Y\), the sets
\[
A'=\overline A\cap Y,
\qquad
B'=\overline B\cap Y
\]
are closed and disjoint, because their intersection is
\[
(\overline A\cap\overline B)\cap Y=\varnothing.
\]
Also \(A\subset A'\) and \(B\subset B'\) by separatedness. Normality of \(Y\) gives disjoint sets \(U',V'\) open in \(Y\) with \(A'\subset U'\) and \(B'\subset V'\). Since \(Y\) is open in \(X\), the sets \(U',V'\) are open in \(X\) as well, and they are disjoint neighborhoods of \(A\) and \(B\).

Conversely, suppose every pair of separated subsets of \(X\) has disjoint open neighborhoods. Let \(Y\subset X\), and let \(A,B\subset Y\) be disjoint closed subsets of \(Y\). Since \(A\) is closed in \(Y\),
\[
Y\cap\overline_X A=A,
\]
so \(B\cap\overline_X A=\varnothing\). Similarly \(A\cap\overline_X B=\varnothing\). Thus \(A\) and \(B\) are separated in \(X\). By hypothesis there are disjoint open sets \(U,V\subset X\) with \(A\subset U\), \(B\subset V\). Then \(U\cap Y\) and \(V\cap Y\) are disjoint open neighborhoods of \(A,B\) in \(Y\). Hence every subspace \(Y\) is normal, so \(X\) is completely normal.
:::
