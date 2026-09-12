---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-05
kind: problem
title: Completely normal spaces and normal subsets
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Subspace Topology
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
Two subsets $A,B\subseteq X$ of the space $(X,\tau)$ are called *separated* if there are $U,V\in\tau$ with $A\subseteq U\subseteq X\setminus B$ and $B\subseteq V\subseteq X\setminus A$.
We say that $X$ is *completely normal* if $X$ is $T_1$ and if for every pair of separated subsets $A,B$ there are $U,V\in\tau$ so that $A\subseteq U$, $B\subseteq V$, and $U\cap V=\varnothing$.
Show that a space $(X,\tau)$ is completely normal if and only if every subset of $X$ is normal.
:::

::: {.solution}
Suppose first that \(X\) is completely normal, and let \(Y\subset X\). Since \(X\) is \(T_1\), so is \(Y\). Let \(C,D\subset Y\) be disjoint closed subsets of \(Y\). Then
\[
\overline C^{\,X}\cap D=\varnothing,
\qquad
C\cap\overline D^{\,X}=\varnothing,
\]
because \(C=Y\cap\overline C^{\,X}\) and \(D=Y\cap\overline D^{\,X}\). Thus \(C\) and \(D\) are separated subsets of \(X\). Complete normality gives disjoint open sets \(U,V\subset X\) with \(C\subset U\) and \(D\subset V\). Then \(U\cap Y\) and \(V\cap Y\) separate \(C\) and \(D\) in \(Y\). Hence every subspace \(Y\) is normal.

Conversely, suppose every subset of \(X\), with its subspace topology, is normal. In particular \(X\) itself is normal and hence \(T_1\). Let \(A,B\subset X\) be separated in the sense of the problem. Equivalently,
\[
\overline A\cap B=\varnothing,
\qquad
A\cap\overline B=\varnothing.
\]
Set
\[
Y=X\setminus(\overline A\cap\overline B).
\]
Then \(A,B\subset Y\), and within \(Y\) the sets
\[
\overline A\cap Y,\qquad \overline B\cap Y
\]
are disjoint closed sets containing \(A\) and \(B\), respectively. Since \(Y\) is normal, there are disjoint sets \(U_Y,V_Y\), open in \(Y\), containing these two closed sets. Because \(Y\) is open in \(X\), \(U_Y\) and \(V_Y\) are open in \(X\). They are disjoint and contain \(A\) and \(B\). Therefore \(X\) is completely normal.
:::
