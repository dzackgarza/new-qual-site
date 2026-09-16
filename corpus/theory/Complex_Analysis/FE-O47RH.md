---
schema: qual/card@1
id: FE-O47RH
kind: example
title: $e^z$ is conformal on $\CC$ but not injective
prompts:
- Give a conformal map that is not injective.
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Counterexamples
relations: []
review: draft
---

::: {.example}
A [[FD-GK7JE|conformal map]] need not be injective.
The map $f\colon\CC\to\CC$, $f(z)=e^z$, is holomorphic with $f'(z)=e^z\neq0$ for all $z$, so it is conformal on $\CC$.
It is not injective because it is periodic: $e^{z+2\pi i}=e^z$.
It is also not surjective, since $e^z\neq0$ for all $z\in\CC$.
:::
