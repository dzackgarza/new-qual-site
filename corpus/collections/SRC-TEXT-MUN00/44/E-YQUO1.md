---
schema: qual/card@1
id: E-YQUO1
kind: problem
title: Peano spaces and the Hahn-Mazurkiewicz theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
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

(a) Let $X$ be a Hausdorff space.
Show that if there is a continuous surjective map $f: I \to X$, then $X$ is compact, connected, weakly locally connected, and metrizable.
[Hint: Show $f$ is a perfect map.]

(b) The converse of the result in (a) is a famous theorem of point-set topology called the Hahn-Mazurkiewicz theorem (see [H-Y], p. 129). Assuming this theorem, show there is a continuous surjective map $f: I \to I^\omega$.

A Hausdorff space that is the continuous image of the closed unit interval is often called a Peano space.
:::

::: {.solution}
(a) Let \(f:I\to X\) be continuous and surjective, with \(X\) Hausdorff. Since \(I\) is compact, \(X=f(I)\) is compact. Since \(I\) is connected, \(X\) is connected.

The map \(f\) is closed: a closed subset of \(I\) is compact, and its image is compact, hence closed in the Hausdorff space \(X\). Its fibers are closed subsets of \(I\), hence compact. Thus \(f\) is a perfect quotient map.

The interval \(I\) is locally connected, and quotient maps preserve local connectedness as proved in §25. Hence \(X\) is locally connected, and therefore weakly locally connected.

Finally, \(I\) is second countable, and perfect maps preserve second countability by §31. Thus \(X\) is second countable. A compact Hausdorff space is regular, so the Urysohn metrization theorem implies that \(X\) is metrizable.

Therefore every Hausdorff continuous image of \(I\) is compact, connected, weakly locally connected, and metrizable.

(b) The Hilbert cube
\[
I^\omega=\prod_{n\ge1}I
\]
is compact by the Tychonoff theorem, connected because a product of connected spaces is connected, and metrizable because it is a countable product of metrizable spaces. It is also locally connected: a basic product neighborhood restricts only finitely many coordinates, and in those coordinates we can choose connected open intervals; the resulting product is connected and gives a connected neighborhood basis.

Hence \(I^\omega\) satisfies the hypotheses of the Hahn--Mazurkiewicz theorem. Therefore there exists a continuous surjection
\[
I\twoheadrightarrow I^\omega.
\]
:::
