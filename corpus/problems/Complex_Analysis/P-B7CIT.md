---
schema: qual/card@1
id: P-B7CIT
kind: problem
title: Analytic functions of equal modulus differ by a unimodular constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Open Mapping Theorem
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $f$ and $g$ be non-zero analytic functions on a region $\Omega$.
Assume $\abs{f(z)} = \abs{g(z)}$ for all $z$ in $\Omega$.
Show that $f(z) = e^{i \theta} g(z)$ in $\Omega$ for some $0 \leq \theta < 2 \pi$.
:::

::: {.solution}

Here non-zero means not identically zero.

::: pf

::: {.pf-step #define-h}
$h\coloneqq f/g$ extends to a holomorphic function on $\Omega$ with $\abs{h}\equiv1$.

::: pf-proof
$g\not\equiv0$ on the region $\Omega$, so its zeros are isolated and $h$ is holomorphic off them, with $\abs{h}=\abs{f}/\abs{g}=1$ there.
$h$ is bounded near each zero of $g$, so by Riemann's removable singularity theorem it extends holomorphically across it, and $\abs{h}=1$ there by continuity.
:::

:::

::: {.pf-step #h-constant}
$h$ is constant.

::: pf-proof
If $h$ were nonconstant, the open mapping theorem would make $h(\Omega)$ an open subset of $\CC$ contained in the unit circle, which has empty interior.
:::

:::

::: pf-step
$f=e^{i\theta}g$ on $\Omega$ for some $0\le\theta<2\pi$.

::: pf-proof
By steps [](#define-h){.pf-ref} and [](#h-constant){.pf-ref}, $h$ is a constant of modulus $1$, say $e^{i\theta}$ with $0\le\theta<2\pi$.
Then $f=hg$ off the zeros of $g$, and at a zero of $g$ both sides vanish because $\abs{f}=\abs{g}$.
:::

:::

:::

:::
