---
schema: qual/card@1
id: P-AGH351EULERCHAR
kind: problem
title: Additivity of the Euler characteristic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Euler Characteristic
  - Coherent Sheaves
  - Projective Schemes
relations: []
review: draft
---

::: problem
Let $X$ be a projective scheme over a field $k$, and let $\mcf$ be a coherent sheaf on $X$. We define the Euler characteristic of $\mcf$ by
\[
\chi(\mcf)=\sum_i (-1)^i \dim_k H^i(X, \mcf).
\]
If
\[
0 \to \mcf' \to \mcf \to \mcf'' \to 0
\]
is a short exact sequence of coherent sheaves on $X$, show that $\chi(\mcf)=\chi(\mcf')+\chi(\mcf'')$.
:::
