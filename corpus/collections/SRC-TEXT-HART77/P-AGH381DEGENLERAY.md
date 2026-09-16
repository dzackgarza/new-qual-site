---
schema: qual/card@1
id: P-AGH381DEGENLERAY
kind: problem
title: Vanishing higher direct images give isomorphic cohomology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Higher Direct Images
  - Leray Spectral Sequence
  - Sheaf Cohomology
relations: []
review: draft
---

::: {.problem}
Let $f: X \to Y$ be a continuous map of topological spaces. Let $\mcf$ be a sheaf of abelian groups on $X$, and assume that $R^i f_*(\mcf) = 0$ for all $i > 0$. Show that there are natural isomorphisms, for each $i \geq 0$,
\[
H^i(X, \mcf) \cong H^i(Y, f_* \mcf)
.\]

This is a degenerate case of the Leray spectral sequence; see Godement [1, II, 4.17.1].
:::
