---
schema: qual/card@1
id: T-8NGWE
kind: theorem
title: Runge's approximation theorem
slogan: 'A function holomorphic near a compact set is a uniform limit of rational functions with poles off the set, and of polynomials when the complement is connected.'
prompts:
- State Runge's approximation theorem.
- When can a holomorphic function on a neighborhood of a compact set be approximated by polynomials?
classification:
  areas:
  - complex-analysis
  topics:
  - Runge
  - Approximation
relations: []
review: draft
---

::: {.theorem}
Let $K\subseteq\CC$ be compact and let $f$ be [[D-E7A5W|holomorphic]] on an open set containing $K$.
Then $f$ is the uniform limit on $K$ of rational functions whose poles lie in $\CC\smz K$.
If $\CC\smz K$ is connected, $f$ is the uniform limit on $K$ of polynomials [@SS03, ch. 2, §5.5, Theorem 5.7].
:::

::: {.example title="Connected complement is necessary for polynomials"}
On the unit circle $K = \bd\DD$ the complement is disconnected, and the function $f(z) = 1/z$, holomorphic on a neighborhood of $K$, is not a uniform limit of polynomials: $\int_K p(z)\dz = 0$ for every polynomial $p$ by Cauchy's theorem, whereas $\int_K \dz/z = 2\pi i$, and a uniform limit would carry the vanishing integrals to $2\pi i$ [@SS03, ch. 2, §7, Problem 4], which states the converse of Runge's theorem for a compact set with disconnected complement.
:::
