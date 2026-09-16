---
schema: qual/card@1
id: E-PER08-6.1
kind: problem
title: A locally path connected space that is not semilocally simply connected
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
Find a path connected, locally path connected space which is not semilocally simply connected.
:::

::: {.solution}
The Hawaiian earring is such an example.
Let
\[
X=\bigcup_{n\ge1} C_n\subset\mathbb R^2,
\qquad
C_n=\{(x,y):(x-1/n)^2+y^2=1/n^2\}.
\]
All circles meet at the origin.

<1>1. $X$ is path connected and locally path connected.
::: {.proof}
Every point can be joined to the origin along its circle, so $X$ is path connected.
Away from the origin, sufficiently small neighbourhoods lie in one circle and contain connected arc neighbourhoods.
At the origin, $X\cap B_\varepsilon(0)$ contains all sufficiently small circles together with short arcs from the finitely many larger circles; its component containing the origin is an open path-connected neighbourhood in $X$.
Thus $X$ is locally path connected.
:::

<1>2. $X$ is not semilocally simply connected at the origin.
::: {.proof}
Every neighbourhood of the origin contains some entire circle $C_n$.
The loop going once around $C_n$ is nontrivial in $\pi_1(X,0)$: collapsing all circles other than $C_n$ to the common basepoint gives a continuous retraction $X\to C_n$, so a null-homotopy in $X$ would induce a null-homotopy of the generator of $\pi_1(C_n)\cong\mathbb Z$.
Hence no neighbourhood of the origin has trivial image in $\pi_1(X)$.
:::
:::
