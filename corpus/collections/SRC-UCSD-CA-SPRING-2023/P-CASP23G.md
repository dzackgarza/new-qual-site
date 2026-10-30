---
schema: qual/card@1
id: P-CASP23G
kind: problem
title: $\frac1{2\pi}\int_0^{2\pi}\cos^{2n}t\,dt$ by a contour integral
classification:
  areas:
  - complex-analysis
  topics:
  - Residue Theorem
  - Integrals
relations: []
review: draft
---

::: {.problem}
By evaluating an appropriate contour integral, show that
$$
\frac{1}{2\pi}\int_0^{2\pi}\cos^{2n}(t)\,dt=\frac{(2n-1)(2n-3)\cdots(3)}{(2n)(2n-2)\cdots(2)}.
$$
:::

::: {.solution}
::: pf

::: {.pf-step #contour}
$\displaystyle\frac{1}{2\pi}\int_0^{2\pi}\cos^{2n}(t)\,dt=\frac{1}{2^{2n}}\cdot\frac{1}{2\pi i}\int_{\abs{z}=1}\Bigl(z+\frac1z\Bigr)^{2n}\frac{dz}{z}$.

::: pf-proof
Parametrize $\abs{z}=1$ by $z=e^{it}$, $0\le t\le2\pi$. Then $dz/z=i\,dt$ and $z+1/z=2\cos t$.
:::

:::

::: {.pf-step #residue}
$\displaystyle\frac{1}{2\pi i}\int_{\abs{z}=1}\Bigl(z+\frac1z\Bigr)^{2n}\frac{dz}{z}=\binom{2n}{n}$.

::: pf-proof
By the binomial theorem, $(z+1/z)^{2n}z^{-1}=\sum_{k=0}^{2n}\binom{2n}{k}z^{2k-2n-1}$. This Laurent polynomial is holomorphic on $\CC\setminus\{0\}$, and its residue at $0$ is the coefficient of $z^{-1}$, from $k=n$. The residue theorem gives the claim.
:::

:::

::: {.pf-step #product}
$\displaystyle\frac{1}{2^{2n}}\binom{2n}{n}=\frac{(2n-1)(2n-3)\cdots(3)}{(2n)(2n-2)\cdots(2)}$.

::: pf-proof
Split $(2n)!$ into its even and odd factors: $(2n)!=\bigl[(2n)(2n-2)\cdots(2)\bigr]\bigl[(2n-1)(2n-3)\cdots(1)\bigr]$, and $(2n)(2n-2)\cdots(2)=2^nn!$. So
$$
\frac{1}{2^{2n}}\binom{2n}{n}=\frac{2^nn!\,(2n-1)(2n-3)\cdots(1)}{2^nn!\cdot2^nn!}=\frac{(2n-1)(2n-3)\cdots(1)}{(2n)(2n-2)\cdots(2)}.
$$
:::

:::

::: pf-qed
Combine steps [](#contour){.pf-ref}, [](#residue){.pf-ref} and [](#product){.pf-ref}.
:::

:::
:::
