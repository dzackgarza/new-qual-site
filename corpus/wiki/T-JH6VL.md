---
schema: qual/card@1
id: T-JH6VL
kind: theorem
title: "Green's Theorem"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.theorem title="Green's Theorem"}
If $\Omega \subseteq \CC$ is bounded with $\bd \Omega$ piecewise smooth and $f, g\in C^1(\bar \Omega)$, then
$$\int_{\bd \Omega} f\, dx + g\, dy = \iint_{\Omega} \qty{ \dd{g}{x} - \dd{f}{y} } \, \dA.$$
In vector form,
\[
\int_\gamma F\cdot \dr = \iint_R \curl F \dA
.\]
:::
