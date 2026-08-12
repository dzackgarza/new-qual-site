---
schema: qual/card@1
id: T-5JNUU
kind: theorem
title: "Rouch\u00e9's Theorem"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.theorem title="Rouché's Theorem" ref="Rouche"}
If

- $f, g$ are meromorphic on $\Omega$
- $\gamma \subset \Omega$ is a toy contour winding about each zero/pole of $f, g$ exactly once,
- $\abs{g} < \abs{f}$ on $\gamma$

then
\[
\Ind_{z=0}(f\circ \gamma)(z) = \Ind_{z=0}((f+g)\circ \gamma)(z) \implies Z_f - P_f = Z_{f+g} - P_{f+g}
.\]
In particular, if $f, g$ are holomorphic, they have the same number of zeros in $\Omega$.

:::
