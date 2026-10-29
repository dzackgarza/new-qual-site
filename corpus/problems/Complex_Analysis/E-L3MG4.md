---
schema: qual/card@1
id: E-L3MG4
kind: problem
title: $\int_{-1}^1\sqrt{1-x^2}\,dx$ by a dogbone contour
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
Show that
$$
I\coloneqq \int_{-1}^1 \sqrt{1-x^2} \dx = {\pi \over 2}
.$$

:::

::: {.solution title="Dogbone and residue at $\infty$"}
Let $g$ be the branch of $\sqrt{z^2-1}$ on $\CC\setminus[-1,1]$ with $g(z)=z\sqrt{1-z^{-2}}$ for $\abs z>1$, using the principal square root of $1-z^{-2}$.
Let $\Gamma$ be the dogbone contour around $[-1,1]$, oriented counterclockwise: the upper edge from $1$ to $-1$, a small circle around $-1$, the lower edge from $-1$ to $1$, and a small circle around $1$.

![Dogbone contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-28_01-50-50.png)

::: pf

::: {.pf-step #boundary-values}
For $-1<x<1$, $g(x\pm i0)=\pm i\sqrt{1-x^2}$.

::: pf-proof
$g^2=z^2-1$, so $g(x\pm i0)=\pm i\sqrt{1-x^2}$ for one choice of sign on each edge, constant along the edge by continuity. At $z=iy$ with $y>0$, $g(iy)=iy\sqrt{1+y^{-2}}=i\sqrt{y^2+1}$, which tends to $i$ as $y\to0^+$, and $g(-z)=-g(z)$ fixes the lower edge.
:::

:::

::: {.pf-step #dogbone}
$\int_\Gamma g\,dz\to-2iI$ as $\Gamma$ shrinks to $[-1,1]$.

::: pf-proof
By step [](#boundary-values){.pf-ref}, the upper edge contributes $\int_1^{-1}i\sqrt{1-x^2}\,dx=-iI$ and the lower edge $\int_{-1}^1(-i)\sqrt{1-x^2}\,dx=-iI$. The small circles contribute $0$ in the limit because $g$ is bounded near $\pm1$ and their lengths tend to $0$.
:::

:::

::: {.pf-step #infinity}
$\int_\Gamma g\,dz=-\pi i$.

::: pf-proof
By Cauchy's theorem, $\int_\Gamma g\,dz=\int_{\abs z=R}g\,dz$ for $R>1$. For $\abs z>1$, $g(z)=z\qty{1-\frac1{2z^2}+\bigo(z^{-4})}=z-\frac1{2z}+\bigo(z^{-3})$, so $\int_{\abs z=R}g\,dz=2\pi i\cdot\qty(-\frac12)$.
:::

:::

::: pf-step
$I=\frac\pi2$.

::: pf-proof
Steps [](#dogbone){.pf-ref} and [](#infinity){.pf-ref} give $-2iI=-\pi i$.
:::

:::

:::

:::
