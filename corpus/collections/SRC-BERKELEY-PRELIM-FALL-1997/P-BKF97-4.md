---
schema: qual/card@1
id: P-BKF97-4
kind: problem
title: The integral $\int_{-\infty}^{\infty}(1+x^{2n})^{-1}\,dx$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 in the deterministic MinerU Flash extraction assets/attachments/Fall97_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Closed 1/(1+z^(2n)) in the upper half-plane, summed the residues at the
    n upper roots of -1, and evaluated their geometric sum.
---

::: {.problem}
Let $n>0$ be an integer.
Evaluate
\[
\int_{-\infty}^{\infty}\frac{dx}{1+x^{2n}}.
\]
:::

::: {.solution}

Let
$$
F(z)\coloneqq\frac1{1+z^{2n}}.
$$

::: pf

::: {.pf-step #upper-half-plane-poles}
The poles of $F$ in the open upper half-plane are
$$
z_k
=
\exp\left(
\frac{(2k+1)\pi i}{2n}
\right),
\qquad
k=0,\ldots,n-1.
$$

::: pf-proof
The poles are the solutions of
$$
z^{2n}=-1.
$$
These are
$$
\exp\left(
\frac{(2k+1)\pi i}{2n}
\right),
\qquad
k=0,\ldots,2n-1.
$$
Exactly the first $n$ of them have arguments strictly between $0$ and
$\pi$.
:::

:::

::: {.pf-step #residue-at-pole}
For each $k=0,\ldots,n-1$,
$$
\Res_{z=z_k}F
=
-\frac{z_k}{2n}.
$$

::: pf-proof
The poles are simple. Therefore
$$
\Res_{z=z_k}F
=
\frac1{2n\,z_k^{2n-1}}.
$$
Since
$$
z_k^{2n}=-1,
$$
one has
$$
z_k^{2n-1}
=
-\frac1{z_k}.
$$
Substitution gives the formula.
:::

:::

::: {.pf-step #sum-of-poles}
The sum of the upper-half-plane poles is
$$
\sum_{k=0}^{n-1}z_k
=
i\csc\left(\frac{\pi}{2n}\right).
$$

::: pf-proof
Set
$$
\alpha\coloneqq\frac{\pi}{2n}.
$$
Then
$$
z_k=e^{i\alpha}(e^{2i\alpha})^k.
$$
The geometric-series formula gives
$$
\begin{aligned}
\sum_{k=0}^{n-1}z_k
&=
e^{i\alpha}
\frac{1-e^{2in\alpha}}{1-e^{2i\alpha}}\\
&=
e^{i\alpha}
\frac{2}{1-e^{2i\alpha}},
\end{aligned}
$$
because
$$
e^{2in\alpha}=e^{i\pi}=-1.
$$
Also
$$
1-e^{2i\alpha}
=
-2ie^{i\alpha}\sin\alpha.
$$
Hence
$$
\sum_{k=0}^{n-1}z_k
=
\frac{i}{\sin\alpha}
=
i\csc\alpha.
$$
:::

:::

::: {.pf-step #sum-of-residues}
The sum of the residues of $F$ in the upper half-plane is
$$
-\frac{i}{2n}
\csc\left(\frac{\pi}{2n}\right).
$$

::: pf-proof
Combine steps [](#residue-at-pole){.pf-ref} and [](#sum-of-poles){.pf-ref}.
:::

:::

::: {.pf-step #arc-integral-vanishes}
The integral of $F$ over the upper semicircle
$$
\abs z=R
$$
tends to zero as $R\to\infty$.

::: pf-proof
For $R>2$,
$$
\abs{1+z^{2n}}
\geq
R^{2n}-1
$$
on the semicircle. Hence
$$
\abs{F(z)}
\leq
\frac1{R^{2n}-1}.
$$
The arc length is $\pi R$, so the $ML$ estimate bounds the arc integral by
$$
\frac{\pi R}{R^{2n}-1},
$$
which tends to zero because $n\geq1$.
:::

:::

::: {.pf-step #integral-value}
One has
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{dx}{1+x^{2n}}
=
\frac{\pi}{n}
\csc\left(\frac{\pi}{2n}\right)
}.
$$

::: pf-proof
Apply the residue theorem to the upper semicircular contour and let
$R\to\infty$. Step [](#arc-integral-vanishes){.pf-ref} removes the arc contribution, while step [](#sum-of-residues){.pf-ref}
gives
$$
\begin{aligned}
\int_{-\infty}^{\infty}\frac{dx}{1+x^{2n}}
&=
2\pi i
\left(
-\frac{i}{2n}
\csc\frac{\pi}{2n}
\right)\\
&=
\frac{\pi}{n}
\csc\frac{\pi}{2n}.
\end{aligned}
$$
:::

:::

::: pf-qed
Step [](#integral-value){.pf-ref} gives the requested value.
:::

:::

:::
