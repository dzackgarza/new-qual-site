---
schema: qual/card@1
id: E-HAT-3.3-1
kind: exercise
title: "Nonorientable 1-manifolds without Hausdorff"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

Show that there exist nonorientable 1-dimensional manifolds if the Hausdorff condition is dropped from the definition of a manifold.

::: solution
**Theorem.**  
There exists a 1-dimensional manifold that is not orientable when Hausdorffness is not required.

*Proof by example.*

Construct
$$
X=\Bigl((\mathbb R\times\{+\})\sqcup(\mathbb R\times\{-\})\Bigr)\big/\!\!\sim
$$
with the equivalence relation:
$$
(t,+)\sim(t,-)\ \text{for }t>0,\qquad
(t,+)\sim(-t,-)\ \text{for }t<0,
$$
and no identification of $0+$ with $0-$.

Define the quotient map $q$ and denote $0_\pm=q(0,\pm)$ and
$U_\pm=q((-\varepsilon,\varepsilon)\times\{\pm\})$.

1. $X$ is a 1-manifold.
   - For $t\neq0$ each point has a neighborhood inherited from one real line branch, so is homeomorphic to an interval.
   - Near $0_\pm$, the sets $q([-\varepsilon,\varepsilon]\times\{\pm\})$ are intervals, since the quotient only folds the two copies together away from 0.

2. $X$ is not Hausdorff.
   Any neighborhoods of $0_+$ and $0_-$ both contain points identified with small positive real numbers, hence intersect; thus no disjoint neighborhoods separate $0_+$ and $0_-$.

3. Put manifold charts
   $$\phi_+:U_+\to(-1,1),\ \phi_+(q(t,+))=t,$$
   $$\phi_-:U_-\to(-1,1),\ \phi_-(q(t,-))=t.$$
   On overlaps, for points coming from $t<0$ the transition is orientation-preserving on one branch and orientation-reversing on the other branch.
   More precisely, the overlap map is locally $t\mapsto t$ on positive coordinates and $t\mapsto -t$ on negative coordinates.
   Hence no single chart orientation on $U_-$ makes all overlap maps orientation-preserving.

4. Therefore $X$ is nonorientable by definition of orientability for 1-manifolds via compatible orientations on overlaps.

So a non-Hausdorff 1-dimensional manifold can be nonorientable. ∎
:::
