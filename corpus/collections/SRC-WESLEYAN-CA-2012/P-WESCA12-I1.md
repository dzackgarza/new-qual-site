---
schema: qual/card@1
id: P-WESCA12-I1
kind: problem
title: 'Three equivalent characterizations of analyticity'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Basic facts, item 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Give three equivalent characterizations of analyticity of a complex-valued function $f$ on a domain $D\subset\CC$.
:::

::: {.solution}

Let
\[
f:D\to\CC.
\]
The following are equivalent.

::: pf

::: {.pf-step #s1-1}

**Complex differentiability at every point.**

For every
\[
z_0\in D,
\]
the limit
\[
f'(z_0)
=
\lim_{z\to z_0}
\frac{f(z)-f(z_0)}{z-z_0}
\]
exists.


::: pf-proof

This is the usual definition that $f$ is holomorphic on $D$.
In one complex variable, “holomorphic” and “analytic” are equivalent.

:::

:::

::: {.pf-step #s1-2}

**Local power-series representation.**

For every
\[
z_0\in D,
\]
there is
\[
r>0
\]
with
\[
B(z_0,r)\subseteq D
\]
and coefficients
\[
a_0,a_1,a_2,\dots\in\CC
\]
such that
\[
f(z)
=
\sum_{n=0}^{\infty}
a_n(z-z_0)^n
\qquad
(|z-z_0|<r).
\]


::: pf-proof

If $f$ is holomorphic, Cauchy's integral formula gives
\[
a_n
=
\frac{f^{(n)}(z_0)}{n!},
\]
and the Taylor series converges to $f$ on every sufficiently small disk.

Conversely, a convergent power series may be differentiated term-by-term
inside its radius of convergence, so it defines a holomorphic function.

:::

:::

::: {.pf-step #s1-3}

**Morera's criterion.**

The function $f$ is continuous on $D$ and
\[
\oint_{\partial T}
f(z)\,dz
=
0
\]
for every closed triangle
\[
T\subset D.
\]


::: pf-proof

If $f$ is holomorphic, Cauchy's theorem gives vanishing of the integral
around every triangle.

Conversely, Morera's theorem says that a continuous function whose integral
around every triangle vanishes is holomorphic.

:::

:::

::: {.pf-step #s1-4}

Therefore each of the three statements
\[
\boxed{
\begin{array}{c}
f\text{ is complex differentiable at every point of }D,\\
f\text{ is locally represented by a convergent power series},\\
f\text{ is continuous and has zero integral around every triangle}
\end{array}}
\]
is equivalent to analyticity on $D$.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give the three standard equivalent characterizations.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} answers the prompt.

:::

:::

:::
