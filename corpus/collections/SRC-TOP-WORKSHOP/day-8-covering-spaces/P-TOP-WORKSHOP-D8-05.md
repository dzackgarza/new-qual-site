---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-05
kind: problem
title: A pathwise continuity criterion for a lift into a cover
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Continuity
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
(Purdue Aug ’09) Let $p:E\to B$ be a covering map.
Let $Y$ be locally path-connected.
Let $g:Y\to E$ be a function such that

- $p\circ g$ is continuous;

- $g\circ\gamma$ is continuous for every path $\gamma$ in $Y$.

Prove that $g$ is continuous.
:::

::: {.solution}
Let \(h=p\circ g:Y\to B\), which is continuous by hypothesis. Fix \(y_0\in Y\), and choose an evenly covered neighborhood \(U\) of \(h(y_0)\). Let \(V_0\) be the sheet over \(U\) containing \(g(y_0)\), and let
\[
s:U\longrightarrow V_0
\]
be the inverse of \(p|_{V_0}\).

By continuity of \(h\), \(h^{-1}(U)\) is a neighborhood of \(y_0\). Since \(Y\) is locally path connected, choose a path-connected open neighborhood
\[
y_0\in W\subset h^{-1}(U).
\]
We claim that on \(W\),
\[
g=s\circ h.
\]
Take \(y\in W\), and choose a path \(\gamma:[0,1]\to W\) from \(y_0\) to \(y\). By hypothesis \(g\circ\gamma\) is continuous. Both
\[
g\circ\gamma
\quad\text{and}\quad
s\circ h\circ\gamma
\]
are lifts of the same path \(h\circ\gamma\), and they agree at \(0\), since both take the value \(g(y_0)\). Uniqueness of path lifting gives equality on all of \([0,1]\), in particular
\[
g(y)=s(h(y)).
\]
Thus \(g|_W=s\circ h|_W\), which is continuous. Since \(y_0\) was arbitrary, \(g\) is continuous on \(Y\).
:::
