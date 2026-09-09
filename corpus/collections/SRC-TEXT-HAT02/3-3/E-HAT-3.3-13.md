---
schema: qual/card@1
id: E-HAT-3.3-13
kind: problem
title: "No retraction onto subsurface of high genus"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Rechecked the statement against Hatcher and repaired the existing solution.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced the invalid homological argument with a correct proof.
---

Let $M_h' \subset M_g$ be a compact subsurface of genus $h$ with one boundary circle, so $M_h'$ is homeomorphic to $M_h$ with an open disk removed.
Show there is no retraction $M_g \to M_h'$ if $h > g/2$.

::: {.solution}
Suppose
\[
r:M_g\longrightarrow M_h'
\]
is a retraction, and let
\[
i:M_h'\hookrightarrow M_g
\]
be the inclusion. Since $r\circ i=\operatorname{id}$, on cohomology over a field $F$ one has
\[
i^*r^*=\operatorname{id}_{H^1(M_h';F)}.
\]
Hence
\[
r^*:H^1(M_h';F)\hookrightarrow H^1(M_g;F)
\]
is injective.

Now $M_h'$ is a compact genus-$h$ surface with one boundary component, so
\[
\dim_F H^1(M_h';F)=2h,
\qquad
H^2(M_h';F)=0.
\]
Therefore for all $u,v\in H^1(M_h';F)$,
\[
r^*u\smile r^*v=r^*(u\smile v)=0.
\]
Thus the $2h$-dimensional subspace
\[
V=r^*H^1(M_h';F)\subset H^1(M_g;F)
\]
is isotropic for the cup-product pairing
\[
H^1(M_g;F)\times H^1(M_g;F)\longrightarrow H^2(M_g;F)\cong F.
\]
This pairing is nonsingular and skew-symmetric. Hence an isotropic subspace has dimension at most half of
\[
\dim_F H^1(M_g;F)=2g.
\]
Consequently
\[
2h\le g.
\]
In particular, if $h>g/2$, no retraction $M_g\to M_h'$ can exist.
:::
