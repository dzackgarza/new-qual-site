---
schema: qual/card@1
id: E-XXZVG
kind: exercise
title: "Prove the uniform limit theorem for holomorphic functions: if $f_n\\to\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Prove the uniform limit theorem for holomorphic functions: if $f_n\to f$ locally uniformly and each $f_n$ is holomorphic then $f$ is holomorphic.
:::

:::{.solution}
This is S&S Theorem 5.2.
Statement: if $f_n\to f$ uniformly locally uniformly on $\Omega$ then $f$ is holomorphic on $\Omega$.

\envlist

- Let $D \subset \Omega$ with $\bar\DD \subset \Omega$ and $\Delta \subset D$ be a triangle.
- Apply Goursat: $\int_\Delta f_n = 0$.
- $f_n\to f$ uniformly on $\Delta$ since it is closed and bounded and thus compact by Heine-Borel, so $f$ is continuous and
\[
\lim_n \int_\Delta f_n = \int_\Delta \lim_n f_n \da \int_\Delta f
.\]
- Apply Morera's theorem: $\int_\Delta f$ vanishes on every triangle in $\Omega$, so $f$ is holomorphic on $\Omega$.

:::

