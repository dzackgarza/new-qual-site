---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS1-P1
kind: problem
title: Closure of a product equals the product of closures
classification:
  areas:
  - topology
  topics:
  - Closure
  - Product Topology
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
(May 2016) Given any topological space $Z$ and subset $D\subseteq Z$, let $\operatorname{Cl}_Z(D)$ denote the closure of $D$ in $Z$.
Show that if $X$ and $Y$ are topological spaces and $A\subseteq X$, $B\subseteq Y$, then $$\operatorname{Cl}_{X\times Y}(A\times B)=\operatorname{Cl}_X(A)\times\operatorname{Cl}_Y(B).$$
:::

::: {.solution}
We prove both inclusions by the neighborhood characterization of closure.

Suppose \((x,y)\in\operatorname{Cl}_{X\times Y}(A\times B)\). If \(U\subset X\) is any open neighborhood of \(x\), then \(U\times Y\) is an open neighborhood of \((x,y)\), so it meets \(A\times B\). Hence \(U\cap A\ne\varnothing\). Thus \(x\in\operatorname{Cl}_X(A)\). Similarly, using \(X\times V\), we get \(y\in\operatorname{Cl}_Y(B)\). Therefore
\[
\operatorname{Cl}_{X\times Y}(A\times B)
\subseteq
\operatorname{Cl}_X(A)\times\operatorname{Cl}_Y(B).
\]

Conversely, suppose \(x\in\operatorname{Cl}_X(A)\) and \(y\in\operatorname{Cl}_Y(B)\). Let \(W\) be any open neighborhood of \((x,y)\) in \(X\times Y\). There are open sets \(U\ni x\) and \(V\ni y\) with
\[
(x,y)\in U\times V\subseteq W.
\]
Since \(x\in\overline A\) and \(y\in\overline B\), choose \(a\in U\cap A\) and \(b\in V\cap B\). Then
\[
(a,b)\in W\cap(A\times B).
\]
Thus every neighborhood of \((x,y)\) meets \(A\times B\), so \((x,y)\in\overline{A\times B}\). Hence equality holds.
:::
