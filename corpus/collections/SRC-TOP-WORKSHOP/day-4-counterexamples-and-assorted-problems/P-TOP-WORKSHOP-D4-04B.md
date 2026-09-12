---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-04B
kind: problem
title: The unit sphere quotient by height fibers is an interval
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Homeomorphisms
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
(June ’04 # A2) Let $X$ be the unit sphere in $\mathbb R^3$ and define an equivalence relation on $X$ by $$ (x,y,z)\sim(x',y',z')\Longleftrightarrow z=z'.$$ Let $Z=X/\sim$ be the quotient space under this equivalence relation, with the quotient topology.
Show that $Z$ is homeomorphic to the interval $[-1,1]$.
:::

::: {.solution}
Let \(q:X\to Z=X/\!\sim\) be the quotient map and define
\[
h:X\to[-1,1],\qquad h(x,y,z)=z.
\]
The map \(h\) is continuous and constant exactly on the equivalence classes, so by the universal property of the quotient there is a unique continuous map
\[
\bar h:Z\to[-1,1]
\]
with \(h=\bar h\circ q\).

The map \(\bar h\) is bijective: every \(t\in[-1,1]\) occurs as the height of a point of the sphere, and two points of \(X\) have the same image under \(h\) exactly when they are equivalent.

The sphere \(X=S^2\) is compact, so its quotient \(Z\) is compact. The interval \([-1,1]\) is Hausdorff. Therefore the continuous bijection
\[
\bar h:Z\longrightarrow[-1,1]
\]
from a compact space to a Hausdorff space is a homeomorphism.
:::
