---
schema: qual/card@1
id: E-ML7VU
kind: problem
title: The topologist's sine curve has dimension one
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Show that the topologist's sine curve has dimension 1.
:::

::: {.solution}
Let
\[
T=\{(x,\sin(1/x)):0<x\le1\}\cup(\{0\}\times[-1,1])
\]
be the topologist's sine curve.

For \(n\ge1\), put
\[
A_n=\{(x,\sin(1/x)):1/(n+1)\le x\le1/n\},
\qquad
A_0=\{(x,\sin(1/x)):1/2\le x\le1\},
\]
and let
\[
V=\{0\}\times[-1,1].
\]
(Changing finitely many initial indices clearly does not matter.) Each \(A_n\) is the continuous image of a compact interval under the embedding
\[
x\longmapsto (x,\sin(1/x)),
\]
so it is an arc, hence homeomorphic to a closed interval and therefore has covering dimension \(1\). The set \(V\) is also an arc, so \(\dim V=1\). Each \(A_n\) and \(V\) is compact, hence closed in the metric space \(T\), and
\[
T=V\cup\bigcup_{n\ge0}A_n.
\]

Now apply the Menger--Urysohn--Čech **countable closed-sum theorem for covering dimension**: if a metrizable space is a countable union of closed subspaces of covering dimension at most \(m\), then its covering dimension is at most \(m\). Hence
\[
\dim T\le1.
\]
A standard reference is R. Engelking, *Dimension Theory*, North-Holland/PWN, 1978, in the discussion of the countable sum theorem for covering dimension; see also the Encyclopedia of Mathematics entry “Dimension,” under the Menger--Urysohn--Čech countable closed-sum theorem.

On the other hand, \(T\) is connected, is \(T_1\) (indeed metric), and contains more than one point. By Exercise [[E-KWBI9]], every such space has dimension at least \(1\). Thus
\[
\boxed{\dim T=1}.
\]
:::
