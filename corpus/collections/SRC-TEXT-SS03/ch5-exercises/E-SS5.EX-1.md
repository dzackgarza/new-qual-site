---
schema: qual/card@1
id: E-SS5.EX-1
kind: problem
title: Jensen’s formula via Blaschke factors
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
1. Give another proof of Jensen’s formula in the unit disc using the functions (called Blaschke factors)

$$
\psi_ {\alpha} (z) = \frac {\alpha - z}{1 - \overline {{\alpha}} z}.
$$

[Hint: The function $f / ( \psi _ { z _ { 1 } } \cdot \cdot \cdot \psi _ { z _ { N } } )$ is nowhere vanishing.]
:::

::: {.solution}
Let $f$ be holomorphic in a neighborhood of the closed unit disc, suppose $f(0)\ne0$, and let $z_1,\ldots,z_N$ be its zeros in $\mathbb D$, repeated according to multiplicity. For $|\alpha|<1$, the Blaschke factor
\[
\psi_\alpha(z)=\frac{\alpha-z}{1-\overline\alpha z}
\]
has one simple zero at $\alpha$, no pole in the closed disc, and satisfies
\[
|\psi_\alpha(e^{i\theta})|=1,
\qquad
\psi_\alpha(0)=\alpha.
\]
Indeed, for $|z|=1$,
\[
|\alpha-z|=|z|\,|\overline z\alpha-1|=|1-\overline\alpha z|.
\]

Define
\[
g(z)=\frac{f(z)}{\prod_{j=1}^N\psi_{z_j}(z)}.
\]
The zeros of the denominator cancel exactly the zeros of $f$, so $g$ is holomorphic and nowhere zero in a neighborhood of the closed disc. Hence $\log|g|$ is harmonic in the disc. The mean-value property at $0$ gives
\[
\log|g(0)|=\frac1{2\pi}\int_0^{2\pi}\log|g(e^{i\theta})|\,d\theta.
\]
On the unit circle all Blaschke factors have modulus $1$, so the right side is
\[
\frac1{2\pi}\int_0^{2\pi}\log|f(e^{i\theta})|\,d\theta.
\]
At the origin,
\[
|g(0)|=\frac{|f(0)|}{\prod_{j=1}^N|z_j|}.
\]
Therefore
\[
\boxed{
\log|f(0)|
=\sum_{j=1}^N\log|z_j|
+\frac1{2\pi}\int_0^{2\pi}\log|f(e^{i\theta})|\,d\theta},
\]
which is Jensen's formula in the unit disc.
:::
