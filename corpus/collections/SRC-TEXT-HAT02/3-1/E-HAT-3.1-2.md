---
schema: qual/card@1
id: E-HAT-3.1-2
kind: problem
title: Hatcher Section 3.1 Exercise 2
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.1, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the resolution and Hom-complex calculations directly from the definitions.
---

# E-HAT-3.1-2

Show that the maps $G \xrightarrow{n} G$ and $H \xrightarrow{n} H$ multiplying each element by the integer $n$ induce multiplication by $n$ in $\operatorname{Ext}(H, G)$.

::: {.solution}
Choose a free resolution
\[
\cdots\longrightarrow F_1\xrightarrow{d_1}F_0\longrightarrow H\longrightarrow0.
\]
Then
\[
\operatorname{Ext}(H,G)=H^1(\operatorname{Hom}(F_\bullet,G)).
\]

<1>1. Multiplication by $n$ on $G$ induces multiplication by $n$ on $\operatorname{Ext}(H,G)$.
::: {.proof}
The map
\[
[n]_G:G\to G,\qquad g\mapsto ng
\]
induces on every cochain group the map
\[
\operatorname{Hom}(F_i,G)\to\operatorname{Hom}(F_i,G),
\qquad \varphi\mapsto [n]_G\circ\varphi=n\varphi.
\]
Thus the induced cochain map is literally multiplication by $n$ in every degree. Its map on cohomology, in particular on $H^1=\operatorname{Ext}(H,G)$, is therefore multiplication by $n$.
:::

<1>2. Multiplication by $n$ on $H$ also induces multiplication by $n$ on $\operatorname{Ext}(H,G)$.
::: {.proof}
The endomorphism $[n]_H:H\to H$ lifts to the chain endomorphism $[n]_{F_i}:F_i\to F_i$ given by multiplication by $n$ in each degree, since all differentials are homomorphisms and hence commute with multiplication by $n$. Because $\operatorname{Ext}$ is contravariant in its first variable, the resulting cochain map is precomposition:
\[
\varphi\longmapsto \varphi\circ[n]_{F_i}=n\varphi.
\]
Again this is multiplication by $n$ on every cochain group, so it induces multiplication by $n$ on cohomology.
:::

Hence both endomorphisms specified in the problem induce
\[
\boxed{n\cdot\operatorname{id}_{\operatorname{Ext}(H,G)}}.
\]
:::
