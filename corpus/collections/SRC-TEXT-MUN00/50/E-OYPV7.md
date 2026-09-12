---
schema: qual/card@1
id: E-OYPV7
kind: problem
title: The hierarchy of conditions on locally euclidean spaces
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

Consider the following conditions on a locally $m$-euclidean space $X$:

(i) $X$ is compact Hausdorff.

(ii) $X$ is an $m$-manifold.

(iii) $X$ is metrizable.

(iv) $X$ is normal.

(v) $X$ is Hausdorff.

Show that (i) $\Rightarrow$ (ii) $\Rightarrow$ (iii) $\Rightarrow$ (iv) $\Rightarrow$ (v).
:::

::: {.solution}
We prove the implications successively.

\((i)\Rightarrow(ii)\). A compact Hausdorff locally \(m\)-euclidean space has a finite atlas. Each coordinate neighborhood has a countable basis, and the union of finitely many such bases is a countable basis for \(X\). Thus \(X\) is Hausdorff, second-countable, and locally \(m\)-euclidean, hence an \(m\)-manifold.

\((ii)\Rightarrow(iii)\). An \(m\)-manifold is Hausdorff and second-countable, hence regular (indeed locally compact Hausdorff spaces are regular). By the Urysohn metrization theorem, a regular second-countable space is metrizable.

\((iii)\Rightarrow(iv)\). Every metrizable space is normal.

\((iv)\Rightarrow(v)\). Under Munkres's convention, a normal space is \(T_1\); normality therefore implies Hausdorffness (separate the two closed singleton sets).

Hence
\[
(i)\Longrightarrow(ii)\Longrightarrow(iii)\Longrightarrow(iv)\Longrightarrow(v).
\]
:::
