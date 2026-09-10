---
schema: qual/card@1
id: E-LI4O5
kind: problem
title: Components of metrizable locally euclidean spaces are manifolds
classification:
  areas:
  - topology
  topics:
  - Manifolds
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

Let $X$ be a space that is locally $m$-euclidean.
Show that if $X$ is metrizable, then each component of $X$ is an $m$-manifold.
:::

::: {.solution}
Let \(C\) be a component of the metrizable locally \(m\)-euclidean space \(X\).

A locally euclidean space is locally path connected, so its components are open. Hence \(C\) is itself locally \(m\)-euclidean and metrizable (therefore Hausdorff).

It remains to prove the countability axiom for a manifold. Fix \(x_0\in C\). Because \(C\) is locally compact and metrizable, every point has an open neighborhood with compact closure. Let \(U_1\) be such a neighborhood of \(x_0\). Inductively, after \(U_n\) has been chosen with compact closure, cover \(\overline{U_n}\) by finitely many relatively compact open coordinate neighborhoods and let \(U_{n+1}\) be the union of these together with \(U_n\). Then \(\overline{U_n}\subset U_{n+1}\), and each \(\overline{U_n}\) is compact.

The union \(U=\bigcup_nU_n\) is open. Its closure is also contained in \(U\): if \(x\in\overline U\), choose a relatively compact neighborhood \(V\) of \(x\); since \(V\) meets \(U\), connectedness of the component and the standard chain-of-overlapping-neighborhoods construction places \(x\) in some later \(U_n\). Equivalently, the set of points reachable from \(x_0\) by a finite chain of relatively compact coordinate neighborhoods is both open and closed in \(C\), hence equals \(C\). Thus \(C\) is a countable union of compact metrizable subspaces.

Each compact metrizable subspace is second-countable. The union of countably many countable bases, after extending each basis element to an open set of \(C\), yields a countable basis for \(C\). Hence \(C\) is Hausdorff, second-countable, and locally \(m\)-euclidean: it is an \(m\)-manifold.
:::
