---
schema: qual/card@1
id: D-T5Q3V
kind: definition
title: Loop Space
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Function Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.definition}
For a based space $(X, x_0)$, the **loop space** is
\[
\Omega X \da \ts{ \gamma: (S^1, s_0)\to (X, x_0) }
\]
with the compact-open topology, based at the constant loop.
Then $\pi_n(\Omega X) \cong \pi_{n+1}(X)$, and $\Omega$ is right adjoint to reduced suspension:
\[
[\Sigma X, Y]_* \cong [X, \Omega Y]_*
.\]
:::

::: {.concept}
See Hatcher, §4.3, p. 395.
:::
