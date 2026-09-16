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
<1>1. Write $f=u+iv$, where $u,v:\Omega\to\mathbb R$.
::: {.proof}
Every complex-valued function has uniquely determined real and imaginary parts.
:::

<1>2. Since $f$ is holomorphic,
\[
\frac{\partial f}{\partial\overline z}=0.
\]
::: {.proof}
For a holomorphic function, the Cauchy-Riemann equations are equivalent to vanishing of the $\overline z$-Wirtinger derivative.
:::

<1>3. Hence $\Delta f=0$.
::: {.proof}
Holomorphic functions are smooth, so the second-order identity from the preceding exercise applies. Thus
\[
\Delta f
=4\frac{\partial}{\partial z}\frac{\partial f}{\partial\overline z}
=4\frac{\partial}{\partial z}(0)
=0.
\]
:::

<1>4. One has
\[
\Delta f=\Delta u+i\Delta v.
\]
::: {.proof}
The Laplacian is real-linear and acts componentwise on $f=u+iv$.
:::

<1>5. Therefore $\Delta u=0$ and $\Delta v=0$ on $\Omega$.
::: {.proof}
By <1>3 and <1>4,
\[
\Delta u+i\Delta v=0.
\]
Both $\Delta u$ and $\Delta v$ are real-valued, so the real and imaginary parts vanish separately. Thus $u$ and $v$ are harmonic.
:::
:::
