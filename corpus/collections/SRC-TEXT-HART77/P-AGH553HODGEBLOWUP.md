---
schema: qual/card@1
id: P-AGH553HODGEBLOWUP
kind: problem
title: Change of $H^1(X, \Omega_X)$ under a monoidal transformation
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Blowups
  - Birational Geometry
relations: []
review: draft
---

::: problem
If $\pi: \tilde{X} \rightarrow X$ is a monoidal transformation with center $P$, show that $H^1\left(\tilde{X}, \Omega_{\tilde{X}}\right) \cong H^1\left(X, \Omega_X\right) \oplus k$. This gives another proof of (5.8).

Hints: Use the projection formula (III, Ex. 8.3) and (III, Ex. 8.1) to show that $H^i\left(X, \Omega_X\right) \cong H^i\left(\tilde{X}, \pi^* \Omega_X\right)$ for each $i$. Next use the exact sequence
\[
0 \rightarrow \pi^* \Omega_X \rightarrow \Omega_{\tilde{X}} \rightarrow \Omega_{\tilde{X} / X} \rightarrow 0
\]
and a local calculation with coordinates to show that there is a natural isomorphism $\Omega_{\tilde{X} / X} \cong \Omega_E$, where $E$ is the exceptional curve. Now use the cohomology sequence of the above sequence (you will need every term) and Serre duality to get the result.
:::
