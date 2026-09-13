---
schema: qual/card@1
id: P-AGH2118ADJOINT
kind: problem
title: Inverse image is left adjoint to direct image
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Adjoint Functors
  - Direct Image
relations: []
review: draft
---

::: problem
Let $f: X \to Y$ be a continuous map of topological spaces.
Show that for any sheaf $\mcf$ on $X$ there is a natural map $f\inv f_* \mcf \to \mcf$, and for any sheaf $\mcg$ on $Y$ there is a natural map $\mcg \to f_* f\inv \mcg$.

Use these maps to show that there is a natural bijection of sets, for any sheaves $\mcf$ on $X$ and $\mcg$ on $Y$,
\[
\Hom_X(f\inv \mcg, \mcf) = \Hom_Y(\mcg, f_* \mcf).
\]
Hence $f\inv$ is a **left adjoint** of $f_*$, and $f_*$ is a **right adjoint** of $f\inv$.
:::
