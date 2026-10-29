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

Show that the one-point compactification of $\RR$ is homeomorphic with the circle $S^1$.
:::

::: {.solution}
Identify \(S^1\) with the unit circle in \(\RR^2\), and choose the point \(N=(0,1)\). Stereographic projection
\[
\sigma:S^1\setminus\{N\}\to\RR
\]
is a homeomorphism. Hence \(\sigma^{-1}:\RR\to S^1\setminus\{N\}\) is a homeomorphism.

Extend it by sending the point at infinity in the one-point compactification \(\RR^*=\RR\cup\{\infty\}\) to \(N\). To check continuity at infinity, note that a neighborhood of \(N\) has compact complement in \(S^1\setminus\{N\}\); under stereographic projection this complement corresponds to a compact subset of \(\RR\). Therefore its preimage in \(\RR^*\) is a neighborhood of \(\infty\). The extension is a continuous bijection from compact \(\RR^*\) to Hausdorff \(S^1\), hence a homeomorphism.
:::
