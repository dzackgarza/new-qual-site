---
schema: qual/card@1
id: E-YBJTZ
kind: problem
title: The one-point compactification of R is the circle
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Show that the one-point compactification of $\mathbb{R}$ is homeomorphic with the circle $S^1$.
:::

::: {.solution}
Identify \(S^1\) with the unit circle in \(\mathbb R^2\), and choose the point \(N=(0,1)\). Stereographic projection
\[
\sigma:S^1\setminus\{N\}\to\mathbb R
\]
is a homeomorphism. Hence \(\sigma^{-1}:\mathbb R\to S^1\setminus\{N\}\) is a homeomorphism.

Extend it by sending the point at infinity in the one-point compactification \(\mathbb R^*=\mathbb R\cup\{\infty\}\) to \(N\). To check continuity at infinity, note that a neighborhood of \(N\) has compact complement in \(S^1\setminus\{N\}\); under stereographic projection this complement corresponds to a compact subset of \(\mathbb R\). Therefore its preimage in \(\mathbb R^*\) is a neighborhood of \(\infty\). The extension is a continuous bijection from compact \(\mathbb R^*\) to Hausdorff \(S^1\), hence a homeomorphism.
:::
