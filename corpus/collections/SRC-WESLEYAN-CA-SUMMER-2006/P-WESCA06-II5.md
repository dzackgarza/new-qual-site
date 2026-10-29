---
schema: qual/card@1
id: P-WESCA06-II5
kind: problem
title: "Evaluate an integral involving $\\Log(z+e)$"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Problems, problem 5 (August 9, 2006) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Evaluate
\[
\int_{|z|=1}\frac{\Log(z+e)}{z^2}\,dz.
\]
:::

::: {.solution}

Let
\[
h(z)
\coloneqq
\Log(z+e).
\]

::: pf

::: pf-step

The function $h$ is holomorphic on a neighborhood of the closed unit
disk
\[
\overline{\DD}.
\]


::: pf-proof

If
\[
|z|\le1,
\]
then
\[
\operatorname{Re}(z+e)
\ge
e-|z|
\ge
e-1
>
0.
\]
Thus
\[
z+e
\]
lies in the open right half-plane.

The principal logarithm is holomorphic on
\[
\CC\setminus(-\infty,0],
\]
which contains the closed right-half-plane neighborhood just described.
Hence
\[
h(z)=\Log(z+e)
\]
is holomorphic on a neighborhood of
\[
\overline{\DD}.
\]

:::

:::

::: {.pf-step #s1-2}

One has
\[
h'(z)
=
\frac1{z+e}.
\]
In particular,
\[
h'(0)
=
\frac1e.
\]


::: pf-proof

Differentiate the logarithm:
\[
\frac{d}{dz}\Log(z+e)
=
\frac1{z+e}.
\]
Evaluation at
\[
z=0
\]
gives the stated value.

:::

:::

::: {.pf-step #s1-3}

By Cauchy's integral formula for derivatives,
\[
\int_{|z|=1}
\frac{h(z)}{z^2}
\,dz
=
2\pi i\,h'(0).
\]


::: pf-proof

The derivative form of Cauchy's formula says
\[
h'(0)
=
\frac1{2\pi i}
\int_{|z|=1}
\frac{h(z)}
{(z-0)^2}
\,dz.
\]
Rearrange.

:::

:::

::: {.pf-step #s1-4}

Therefore
\[
\boxed{
\int_{|z|=1}
\frac{\Log(z+e)}{z^2}
\,dz
=
\frac{2\pi i}{e}.
}
\]


::: pf-proof

Substitute
\[
h'(0)=\frac1e
\]
from step [](#s1-2){.pf-ref} into step [](#s1-3){.pf-ref}.

:::

:::

::: pf-step

The value is unchanged if one uses any other analytic branch of
the logarithm on the relevant right-half-plane neighborhood.


::: pf-proof

Any two analytic logarithm branches on a connected domain differ by a
constant
\[
2\pi i k,
\qquad
k\in\ZZ.
\]
The corresponding change in the integral is
\[
2\pi i k
\int_{|z|=1}
\frac{dz}{z^2}.
\]
But
\[
\int_{|z|=1}
\frac{dz}{z^2}
=
0,
\]
since the residue of
\[
z^{-2}
\]
at $0$ is zero.
Thus the answer is branch-independent whenever the branch is analytic on
the needed neighborhood.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required value.

:::

:::

:::
