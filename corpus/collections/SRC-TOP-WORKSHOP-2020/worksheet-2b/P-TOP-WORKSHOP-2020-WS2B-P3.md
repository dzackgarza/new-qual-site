---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2B-P3
kind: problem
title: Homotopy is compatible with composition, but cancellation can fail
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Counterexamples
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
(January 2019) Show that if $f,g:(X,\mathcal T)\to(Y,\mathcal T')$ and $h,k:(Y,\mathcal T')\to(Z,\mathcal T'')$ are continuous and $f\simeq g$ and $h\simeq k$, then $h\circ f\simeq k\circ g$.
Show, however, that the converse ($h\circ f\simeq k\circ g$ implies $f\simeq g$ and $h\simeq k$) need not be true.
:::

::: {.solution}
Let
\[
F:X\times I\to Y
\]
be a homotopy from \(f\) to \(g\), and let
\[
H:Y\times I\to Z
\]
be a homotopy from \(h\) to \(k\). Define
\[
K:X\times I\to Z,
\qquad
K(x,t)=H(F(x,t),t).
\]
This is continuous, and
\[
K(x,0)=H(f(x),0)=h(f(x)),
\qquad
K(x,1)=H(g(x),1)=k(g(x)).
\]
Hence
\[
h\circ f\simeq k\circ g.
\]

The converse fails. Take
\[
X=Y=S^1,\qquad Z=\{*\},
\]
let \(f=\operatorname{id}_{S^1}\), let \(g:S^1\to S^1\) be constant, and let \(h=k:S^1\to\{*\}\) be the unique map. Then
\[
h\circ f=k\circ g
\]
identically. However \(f\not\simeq g\), since \(f_*\) is the identity on
\[
\pi_1(S^1)\cong\mathbb Z,
\]
while \(g_*=0\). Thus homotopy of the composites does not imply homotopy of the individual factors.
:::
