---
schema: qual/card@1
id: P-WESCA06-II5
kind: problem
title: "Evaluate an integral involving $\\Log(z+e)$"
classification:
  areas: [complex-analysis]
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Problems, problem 5 (August 9, 2006) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Two structural corrections on 2026-11-19, no argument changed. The
    branch-independence argument stood as the last step of the proof, while the step
    that boxes the value of the integral stood before it and a pf-qed closed by
    announcing that earlier step, which STYLE-08 does not allow: the branch
    observation is now a remark after the solution, and the step that boxes
    2 pi i / e is the QED step. The item was read on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf, PDF p. 15, the Complex Analysis
    Preliminary Examination of August 9, 2006, Section 2 item 5, which reads
    "Find the value of the integral \int_{|z|=1} Log(z+e)/z^2 dz"; the statement on
    the card is the printed one and is unchanged.

---

::: {.problem}
Evaluate
$$
\int_{\abs{z}=1}\frac{\Log(z+e)}{z^2}\,dz.
$$
:::

::: {.solution}

Let
$$
h(z)
\coloneqq
\Log(z+e).
$$

::: pf

::: pf-step

The function $h$ is holomorphic on a neighborhood of the closed unit
disk
$$
\overline{\DD}.
$$


::: pf-proof

If
$$
\abs{z}\le1,
$$
then
$$
\operatorname{Re}(z+e)
\ge
e-\abs{z}
\ge
e-1
>
0.
$$
Thus
$$
z+e
$$
lies in the open right half-plane.

The principal logarithm is holomorphic on
$$
\CC\setminus(-\infty,0],
$$
which contains the closed right-half-plane neighborhood just described.
Hence
$$
h(z)=\Log(z+e)
$$
is holomorphic on a neighborhood of
$$
\overline{\DD}.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
h'(z)
=
\frac1{z+e}.
$$
In particular,
$$
h'(0)
=
\frac1e.
$$


::: pf-proof

Differentiate the logarithm:
$$
\frac{d}{dz}\Log(z+e)
=
\frac1{z+e}.
$$
Evaluation at
$$
z=0
$$
gives the stated value.

:::

:::

::: {.pf-step #s1-3}

By Cauchy's integral formula for derivatives,
$$
\int_{\abs{z}=1}
\frac{h(z)}{z^2}
\,dz
=
2\pi i\,h'(0).
$$


::: pf-proof

The derivative form of Cauchy's formula says
$$
h'(0)
=
\frac1{2\pi i}
\int_{\abs{z}=1}
\frac{h(z)}
{(z-0)^2}
\,dz.
$$
Rearrange.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\int_{\abs{z}=1}
\frac{\Log(z+e)}{z^2}
\,dz
=
\frac{2\pi i}{e}.
}
$$


::: pf-proof

Substitute
$$
h'(0)=\frac1e
$$
from step [](#s1-2){.pf-ref} into step [](#s1-3){.pf-ref}.

:::

:::


:::

:::


::: {.remark title="Branch independence"}
The value is unchanged if one uses any other analytic branch of the logarithm on the
right-half-plane neighbourhood of $\overline{\DD}$: two such branches differ by a constant
$2\pi i k$ with $k\in\ZZ$, and the corresponding change in the integral is
$2\pi i k\int_{\abs z=1}dz/z^2=0$, since $z^{-2}$ has zero residue at $0$.
:::
