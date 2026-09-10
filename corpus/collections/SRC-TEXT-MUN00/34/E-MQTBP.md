---
schema: qual/card@1
id: E-MQTBP
kind: problem
title: Locally metrizable compact Hausdorff spaces are metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Compactness
relations: []
review: draft
---

::: {.exercise}

A space $X$ is locally metrizable if each point $x$ of $X$ has a neighborhood that is metrizable in the subspace topology.
Show that a compact Hausdorff space $X$ is metrizable if it is locally metrizable.
[Hint: Show that $X$ is a finite union of open subspaces, each of which has a countable basis.]
:::

::: {.solution}
Since \(X\) is compact Hausdorff, it is regular. For each \(x\in X\), choose a metrizable neighborhood \(N_x\). Choose an open \(U_x\) with \(x\in U_x\subset N_x\), and by regularity choose an open \(V_x\) with
\[
x\in V_x\subset\overline{V_x}\subset U_x.
\]
The closed subspace \(\overline{V_x}\) is compact and metrizable, hence second countable. Therefore the open subspace \(V_x\) has a countable basis.

Compactness of \(X\) gives finitely many such open sets
\[
V_{x_1},\dots,V_{x_m}
\]
covering \(X\). The union of countable bases for these finitely many open subspaces is a countable basis for \(X\). Since compact Hausdorff spaces are regular, the Urysohn metrization theorem now implies \(X\) is metrizable.
:::
