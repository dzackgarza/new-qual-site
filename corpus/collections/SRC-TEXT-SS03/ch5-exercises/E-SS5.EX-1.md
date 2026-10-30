---
schema: qual/card@1
id: E-SS5.EX-1
kind: problem
title: Jensen's formula via Blaschke factors
classification:
  areas:
  - complex-analysis
  topics:
  - Jensen's Formula
  - Blaschke Factors
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Give another proof of Jensen's formula in the unit disc using the functions (called Blaschke factors)
$$
\psi_\alpha(z) = \frac{\alpha - z}{1 - \overline{\alpha} z}.
$$
[Hint: The function $f/(\psi_{z_1} \cdots \psi_{z_N})$ is nowhere vanishing.]
:::

::: {.solution}
Let $f$ be holomorphic in a neighborhood of the closed unit disc, suppose $f(0)\ne0$, and let $z_1,\ldots,z_N$ be its zeros in $\DD$, repeated according to multiplicity. For $\abs{\alpha}<1$, the Blaschke factor
$$
\psi_\alpha(z)=\frac{\alpha-z}{1-\overline\alpha z}
$$
has one simple zero at $\alpha$, no pole in the closed disc, and satisfies
$$
\abs{\psi_\alpha(e^{i\theta})}=1,
\qquad
\psi_\alpha(0)=\alpha.
$$
Indeed, for $\abs{z}=1$,
$$
\abs{\alpha-z}=\abs{z}\,\abs{\overline z\alpha-1}=\abs{1-\overline\alpha z}.
$$

Define
$$
g(z)=\frac{f(z)}{\prod_{j=1}^N\psi_{z_j}(z)}.
$$
The zeros of the denominator cancel exactly the zeros of $f$, so $g$ is holomorphic and nowhere zero in a neighborhood of the closed disc. Hence $\log\abs{g}$ is harmonic in the disc. The mean-value property at $0$ gives
$$
\log\abs{g(0)}=\frac1{2\pi}\int_0^{2\pi}\log\abs{g(e^{i\theta})}\,d\theta.
$$
On the unit circle all Blaschke factors have modulus $1$, so the right side is
$$
\frac1{2\pi}\int_0^{2\pi}\log\abs{f(e^{i\theta})}\,d\theta.
$$
At the origin,
$$
\abs{g(0)}=\frac{\abs{f(0)}}{\prod_{j=1}^N\abs{z_j}}.
$$
Therefore
$$
\boxed{
\log\abs{f(0)}
=\sum_{j=1}^N\log\abs{z_j}
+\frac1{2\pi}\int_0^{2\pi}\log\abs{f(e^{i\theta})}\,d\theta},
$$
which is Jensen's formula in the unit disc.
:::
