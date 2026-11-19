---
schema: qual/card@1
id: D-6RZQN
kind: definition
title: Primitive
prompts:
- What is a primitive of a holomorphic function on an open set?
classification:
  areas:
  - complex-analysis
  topics:
  - Primitives
  - Contour Integration
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open and let $f\colon\Omega\to\CC$ be a function.
A \dfn{primitive} of $f$ on $\Omega$ is a [[D-E7A5W|holomorphic]] function $F$ on $\Omega$ with $F'(z) = f(z)$ for all $z\in\Omega$ [@SS03, p. 22].
:::

::: {.remark title="Integrals of functions with a primitive"}
If $f$ is continuous on $\Omega$ and has a primitive $F$ there, then $\int_\gamma f\dz = F(w_2)-F(w_1)$ for every piecewise $C^1$ curve $\gamma$ in $\Omega$ from $w_1$ to $w_2$, so the integral of $f$ over a closed curve vanishes [@SS03, Theorem 3.2 of Chapter 1 (p. 22)].
The function $1/z$ has no primitive on $\CC\smz$, since its integral over the unit circle is $2\pi i$; it has one on every disc that misses $0$.
:::
