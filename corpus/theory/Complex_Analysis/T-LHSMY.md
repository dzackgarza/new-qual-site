---
schema: qual/card@1
id: T-LHSMY
kind: theorem
title: Morera's theorem
slogan: 'Continuous plus zero integral around every triangle forces holomorphicity.'
prompts:
- State Morera's theorem.
classification:
  areas:
  - complex-analysis
  topics:
  - Morera
  - Holomorphic Functions
relations: []
review: draft
---

::: {.theorem ref="Morera"}
Let $\Omega\subseteq\CC$ be open and let $f\colon\Omega\to\CC$ be continuous.
If $\int_{\bd T}f(z)\dz=0$ for every closed triangle $T\subseteq\Omega$, then $f$ is [[D-E7A5W|holomorphic]] on $\Omega$ [@SS03, Theorem 5.1 (p. 53), stated there for a disc].
:::

::: {.corollary}
If $f\colon\Omega\to\CC$ is continuous and $\int_{\bd R}f(z)\dz=0$ for every closed rectangle $R\subseteq\Omega$ whose sides are parallel to the axes, then $f$ is holomorphic on $\Omega$.
:::

::: {.proof}
A diagonal splits $R$ into two closed triangles contained in $\Omega$, and $\int_{\bd R}f$ is the sum of the two boundary integrals over them, so the hypothesis of the theorem holds for every triangle.
:::
