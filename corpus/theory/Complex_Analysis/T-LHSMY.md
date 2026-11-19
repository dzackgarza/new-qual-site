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
