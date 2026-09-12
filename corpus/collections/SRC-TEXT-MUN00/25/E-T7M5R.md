---
schema: qual/card@1
id: E-T7M5R
kind: problem
title: The identity component of a topological group is normal
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $G$ be a topological group; let $C$ be the component of $G$ containing the identity element $e$.
Show that $C$ is a normal subgroup of $G$.
[Hint: If $x \in G$, then $xC$ is the component of $G$ containing $x$.]
:::

::: {.solution}
For each $g\in G$, left translation
\[
L_g:G\to G,\qquad L_g(x)=gx,
\]
is a homeomorphism. Therefore it sends components to components. Since $L_g(C)=gC$ contains $g$, it is exactly the component containing $g$. Similarly, right translation gives that $Cg$ is the component containing $g$. Hence
\[
gC=Cg
\]
for every $g\in G$.

First, $C$ is a subgroup. If $x,y\in C$, then $xC=C$, because both are components containing $x$ and $e\in C$ implies $x\in xC$. Thus $xy\in C$. Also inversion is a homeomorphism fixing $e$, so it sends the component $C$ of $e$ to itself; hence $x^{-1}\in C$.

Finally $gC=Cg$ for every $g$ implies
\[
gCg^{-1}=C.
\]
Thus $C$ is a normal subgroup of $G$.
:::
