---
schema: qual/card@1
id: E-5AKU5
kind: exercise
title: "Uniform limit theorem for holomorphic functions"
classification:
  areas:
  - complex-analysis
  topics:
  - morera
  - uniform-convergence
  - sequences-of-functions
  - holomorphic-functions
relations: []
review: draft
solved: true
---
:::{.exercise title="Uniform limit theorem for holomorphic functions"}
Show that if $f_n\to f$ locally uniformly and each $f_n$ is holomorphic then $f$ is holomorphic.

:::

:::{.solution}
This is S&S Theorem 5.2.
Statement: if $f_n\to f$ uniformly locally uniformly on $\Omega$ then $f$ is holomorphic on $\Omega$.

\envlist

- Let $D \subset \Omega$ with $\bar\DD \subset \Omega$ and $\Delta \subset D$ be a triangle.
- Apply Cauchy-Goursat: 
\[
\int_\Delta f_n = 0
.\]
- $f_n\to f$ uniformly on $\Delta$ since it is closed and bounded and thus compact by Heine-Borel, so $f$ is continuous and
\[
\lim_n 0 = \lim_n \int_\Delta f_n = \int_\Delta \lim_n f_n \da \int_\Delta f
.\]
- Apply Morera's theorem: $\displaystyle\int_\Delta f$ vanishes on every triangle in $\Omega$, so $f$ is holomorphic on $\Omega$.

:::

