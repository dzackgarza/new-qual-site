---
schema: qual/card@1
id: P-WESCA04-P5
kind: problem
title: "Uniform convergence on the boundary controls a holomorphic sequence inside"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.3, problem 5 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md. Flash drops the closure bar from the continuity domain, while the same sentence requires boundary values on $\partial D$; the card normalizes that concrete extraction defect to $\overline D$.
---

::: {.problem}
Let $D\subset\CC$ be a bounded domain.
Suppose each $f_n$ is continuous on $\overline D$ and analytic on $D$.
If $(f_n)$ converges uniformly on $\partial D$, prove that it converges uniformly on $\overline D$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since
\[
f_n|_{\partial D}
\]
converges uniformly, the sequence is uniformly Cauchy on
\[
\partial D.
\]


::: pf-proof

Uniform convergence in the supremum norm implies the Cauchy property:
for every
\[
\varepsilon>0
\]
there exists
\[
N
\]
such that for
\[
m,n\ge N,
\]
\[
\sup_{z\in\partial D}
|f_n(z)-f_m(z)|
<
\varepsilon.
\]

:::

:::

::: {.pf-step #s1-2}

For fixed $m,n$, define
\[
h_{m,n}
\coloneqq
f_n-f_m.
\]
Then $h_{m,n}$ is continuous on
\[
\overline D
\]
and holomorphic on $D$.


::: pf-proof

Both properties are preserved under subtraction.

:::

:::

::: {.pf-step #s1-3}

For every $m,n$,
\[
\boxed{
\sup_{z\in\overline D}
|h_{m,n}(z)|
\le
\sup_{z\in\partial D}
|h_{m,n}(z)|.
}
\]


::: pf-proof

Because $D$ is bounded,
\[
\overline D
\]
is compact.
Since $h_{m,n}$ is continuous on $\overline D$,
\[
|h_{m,n}|
\]
attains its maximum there.

If a positive strict maximum occurred at a point of the interior $D$, the
maximum modulus principle would force $h_{m,n}$ to be constant on the
connected domain $D$.
In that constant case the same modulus occurs on the boundary as well.

Thus in all cases the supremum on the closure is bounded by the supremum on
the boundary.

:::

:::

::: {.pf-step #s1-4}

The sequence
\[
(f_n)
\]
is uniformly Cauchy on
\[
\overline D.
\]


::: pf-proof

Fix
\[
\varepsilon>0.
\]
Choose
\[
N
\]
from step [](#s1-1){.pf-ref}.
For
\[
m,n\ge N,
\]
step [](#s1-3){.pf-ref} gives
\[
\begin{aligned}
\sup_{z\in\overline D}
|f_n(z)-f_m(z)|
&=
\sup_{z\in\overline D}
|h_{m,n}(z)|\\
&\le
\sup_{z\in\partial D}
|h_{m,n}(z)|\\
&<
\varepsilon.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-5}

There exists a continuous function
\[
f:\overline D\to\CC
\]
such that
\[
f_n\longrightarrow f
\]
uniformly on
\[
\overline D.
\]


::: pf-proof

The compact space
\[
\overline D
\]
has a complete supremum-norm function space
\[
C(\overline D).
\]
Step [](#s1-4){.pf-ref} says
\[
(f_n)
\]
is Cauchy in this Banach space.
Hence it converges in the supremum norm to some
\[
f\in C(\overline D).
\]

:::

:::

::: {.pf-step #s1-6}

In particular,
\[
\boxed{
f_n\to f
\text{ uniformly on }\overline D.
}
\]


::: pf-proof

This is exactly the conclusion of step [](#s1-5){.pf-ref}.

:::

:::

::: pf-step

Moreover, the limit $f$ is holomorphic on $D$.


::: pf-proof

Uniform convergence on
\[
\overline D
\]
implies locally uniform convergence on $D$.
By the Weierstrass theorem on locally uniform limits of holomorphic
functions,
\[
f|_D
\]
is holomorphic.
This extra conclusion is not required for the uniform-convergence claim.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-6){.pf-ref} prove the required uniform convergence on the closure.

:::

:::

:::
