---
schema: qual/card@1
id: E-2HIKG
kind: problem
title: $\int_0^\infty x^{1/3}/(1+x^2)\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
$$
I\coloneqq \int_0^\infty \frac{x^{1/3}}{1 + x^2} \dx = \frac{\pi}{\sqrt 3}.
$$
:::

::: {.solution}
Let
$$
f(z)=\frac{z^{1/3}}{1+z^2},
$$
using the branch of $z^{1/3}$ with $0\le\Arg z\le\pi$ on the closed upper half-plane minus $0$.
Integrate over the upper semicircle $C_R$ of radius $R>1$, indented by a semicircle $C_\varepsilon$ of radius $\varepsilon<1$ around the branch point $0$.

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-26_20-04-14.png)

::: pf

::: {.pf-step #arcs}
The integrals over $C_R$ and $C_\varepsilon$ tend to $0$ as $R\to\infty$ and $\varepsilon\to0$.

::: pf-proof
On $C_R$,
$$
\abs{\int_{C_R}f(z)\,dz}
\le \pi R\frac{R^{1/3}}{R^2-1}
=O(R^{-2/3}),
$$
and on $C_\varepsilon$ the same estimate gives $\pi\varepsilon\cdot\varepsilon^{1/3}/(1-\varepsilon^2)=O(\varepsilon^{4/3})$.
:::

:::

::: {.pf-step #segments}
The two segments of the real axis contribute $\qty{1+e^{i\pi/3}}I$ in the limit.

::: pf-proof
On the positive real axis $z^{1/3}=x^{1/3}$.
On the negative real axis, $(-x)^{1/3}=e^{i\pi/3}x^{1/3}$ for $x>0$, and the substitution $z=-x$ turns the integral from $-R$ to $-\varepsilon$ into $e^{i\pi/3}\int_\varepsilon^R x^{1/3}/(1+x^2)\dx$.
:::

:::

::: {.pf-step #residue}
$\Res_{z=i}f(z)=\dfrac{e^{i\pi/6}}{2i}$, and $z=i$ is the only pole inside the contour.

::: pf-proof
The poles of $f$ are $\pm i$, and only $i$ lies in the upper half-plane.
It is a simple pole, so the residue is $i^{1/3}/(2i)$, and $i^{1/3}=e^{i\pi/6}$ on the chosen branch.
:::

:::

::: pf-step
$I=\boxed{\pi/\sqrt3}$.

::: pf-proof
By the residue theorem and steps [](#arcs){.pf-ref}--[](#residue){.pf-ref},
$$
\qty{1+e^{i\pi/3}}I
=2\pi i\frac{e^{i\pi/6}}{2i}
=\pi e^{i\pi/6}.
$$
Since $1+e^{i\pi/3}=2e^{i\pi/6}\cos(\pi/6)=\sqrt3\,e^{i\pi/6}$, it follows that $I=\pi/\sqrt3$.
:::

:::

:::

:::
