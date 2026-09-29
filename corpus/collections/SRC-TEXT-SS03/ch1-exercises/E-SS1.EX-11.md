---
schema: qual/card@1
id: E-SS1.EX-11
kind: problem
title: Real and imaginary parts of holomorphic functions are harmonic
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Use the Wirtinger-operator identity for the Laplacian to prove that if $f$ is holomorphic in an open set $\Omega$, then the real and imaginary parts of $f$ are harmonic; that is, their Laplacians vanish.
:::

::: {.solution}

::: pf

::: pf-step

Write $f=u+iv$, where $u,v:\Omega\to\mathbb R$.

::: pf-proof

Every complex-valued function has uniquely determined real and imaginary parts.

:::

:::

::: pf-step

Since $f$ is holomorphic,
\[
\frac{\partial f}{\partial\overline z}=0.
\]

::: pf-proof

For a holomorphic function, the Cauchy-Riemann equations are equivalent to vanishing of the $\overline z$-Wirtinger derivative.

:::

:::

::: {.pf-step #s3}

Hence $\Delta f=0$.

::: pf-proof

Holomorphic functions are smooth, so the identity $4\partial_z\partial_{\overline z}=\Delta$ of [[E-SS1.EX-10]] applies. Thus
\[
\Delta f
=4\frac{\partial}{\partial z}\frac{\partial f}{\partial\overline z}
=4\frac{\partial}{\partial z}(0)
=0.
\]

:::

:::

::: {.pf-step #s4}

One has
\[
\Delta f=\Delta u+i\Delta v.
\]

::: pf-proof

The Laplacian is real-linear and acts componentwise on $f=u+iv$.

:::

:::

::: pf-step

Therefore $\Delta u=0$ and $\Delta v=0$ on $\Omega$.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
\[
\Delta u+i\Delta v=0.
\]
Both $\Delta u$ and $\Delta v$ are real-valued, so the real and imaginary parts vanish separately. Thus $u$ and $v$ are harmonic.

:::

:::

:::

:::
