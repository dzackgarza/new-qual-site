---
schema: qual/card@1
id: P-63VGL
kind: problem
title: $\int_T f=0$ if $f$ is holomorphic and bounded near a puncture inside the triangle
  $T$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Morera
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
Suppose that $f$ is holomorphic on a punctured open set $\Omega\setminus\theset{w_0}$ and let $T\subset \Omega$ be a triangle containing $w_0$.
Prove that if $f$ is bounded near $w_0$, then $\int_T f(z) ~dz = 0$.
:::

::: {.solution}
Here $T$ is a closed solid triangle in $\Omega$, $\int_T$ is the integral over its positively oriented boundary, and $\abs{f}\le M$ on $0<\abs{z-w_0}<r$.
By Goursat's theorem, $\int_{T'} f\,dz=0$ for every closed solid triangle $T'\subset\Omega\setminus\theset{w_0}$.

::: pf

::: {.pf-step #vertex}
If $w_0$ is a vertex of a closed solid triangle $T'\subset\Omega$, then $\int_{T'} f\,dz=0$.

::: pf-proof
Let $T'$ have vertices $w_0,b,c$.
For $0<t<1$ let $b_t = w_0+t(b-w_0)$ and $c_t=w_0+t(c-w_0)$.
The triangle $T'$ is the union of the triangles $T_t=(w_0,b_t,c_t)$, $(b_t,b,c)$ and $(b_t,c,c_t)$, and the integrals over the shared edges cancel, so
$$
\int_{T'} f\,dz = \int_{T_t} f\,dz + \int_{(b_t,b,c)} f\,dz + \int_{(b_t,c,c_t)} f\,dz.
$$
The last two triangles do not contain $w_0$, so their integrals vanish by Goursat's theorem.
For $t$ small, $T_t\setminus\theset{w_0}$ lies in $0<\abs{z-w_0}<r$, so
$$
\abs{\int_{T'} f\,dz}=\abs{\int_{T_t} f\,dz}\le M\cdot t\cdot\operatorname{perimeter}(T'),
$$
which tends to $0$ as $t\to0$.
:::

:::

::: pf-step
$\int_T f\,dz=0$.

::: pf-proof
Join $w_0$ to the vertices of $T$ by segments.
This divides $T$ into at most three closed solid triangles, each with $w_0$ as a vertex (a triangle degenerate because $w_0$ lies on a side is omitted).
The integrals over the interior segments cancel, so $\int_T f\,dz$ is the sum of the integrals over these triangles, each zero by step [](#vertex){.pf-ref}.
:::

:::

:::

:::
