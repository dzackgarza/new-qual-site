---
schema: qual/card@1
id: P-DFHS3
kind: problem
title: $\int_0^\infty\frac{dx}{(1+x^2)(1+9x^2)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.problem}
Calculate
$$
\int_0^\infty {dx \over (1+x^2)(1+9x^2)}.
$$
:::

::: {.solution}

Let $F(z)\coloneqq\frac{1}{(1+z^2)(1+9z^2)}$.

::: pf

::: {.pf-step #residues}
$\Res_{z=i}F=\frac{i}{16}$ and $\Res_{z=i/3}F=-\frac{3i}{16}$, and these are the only poles in the upper half-plane.

::: pf-proof
The poles are $\pm i$ and $\pm i/3$, all simple.
$\Res_{z=i}F=\frac{1}{(2i)(1-9)}=\frac{i}{16}$, and since $1+9z^2=9(z-i/3)(z+i/3)$, $\Res_{z=i/3}F=\frac{1}{(1-1/9)\cdot 9\cdot(2i/3)}=-\frac{3i}{16}$.
:::

:::

::: {.pf-step #full-line}
$\int_{-\infty}^\infty F(x)\,dx=\frac\pi4$.

::: pf-proof
Integrate over the boundary of the upper half-disc of radius $R>1$.
The arc integral is $O(R\cdot R^{-4})\to0$, so the residue theorem and step [](#residues){.pf-ref} give $2\pi i\left(\frac{i}{16}-\frac{3i}{16}\right)=\frac\pi4$.
:::

:::

::: pf-step
$\int_0^\infty F(x)\,dx=\boxed{\pi/8}$.

::: pf-proof
$F$ is even on $\RR$; apply step [](#full-line){.pf-ref}.
:::

:::

:::

:::
