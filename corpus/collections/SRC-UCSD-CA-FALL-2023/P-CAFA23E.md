---
schema: qual/card@1
id: P-CAFA23E
kind: problem
title: "Continuous function analytic off the real line is entire"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $f$ be continuous on $\mathbb{C}$ and analytic on $\mathbb{C} \setminus \mathbb{R}$.
Prove that $f$ is analytic on $\mathbb{C}$.
:::

::: pf

::: pf-step

It is enough to prove that
$$
\int_{\partial T}f(z)\,dz=0
$$
for every triangle $T\subset\CC$.


::: pf-proof

The function $f$ is continuous on all of $\CC$ by hypothesis. Morera's
theorem says that a continuous function on a region is holomorphic if its
integral around the boundary of every triangle contained in that region
vanishes. Thus the displayed assertion implies that $f$ is entire.

:::

:::

::: pf-step

Fix a triangle $T$. For $\varepsilon>0$, put
$$
T^+_\varepsilon=T\cap\{z:\Im z\ge\varepsilon\}.
$$
Whenever this set has nonempty interior,
$$
\int_{\partial T^+_\varepsilon}f(z)\,dz=0.
$$


::: pf-proof

The intersection of a triangle with a closed half-plane is a convex
polygon, possibly empty or degenerate. If it has nonempty interior, its
entire boundary lies in the open upper half-plane because
$\Im z\ge\varepsilon>0$ there. The function $f$ is holomorphic on that
half-plane, so Cauchy's theorem applied to the polygon gives the stated
vanishing integral.

:::

:::

::: pf-step

As $\varepsilon\downarrow0$, the boundary integral in step <1>2
converges to the integral over the portion of $\partial T$ in the closed
upper half-plane together with the real-axis cut, oriented as the boundary
of $T\cap\{\Im z\ge0\}$.


::: pf-proof

There are only finitely many boundary segments involved. The vertices at
which the horizontal line $\Im z=\varepsilon$ meets the sides of $T$
converge to the corresponding intersections with the real axis. Hence each
boundary segment converges in endpoints and parametrization to its limiting
segment.

All these segments remain in one fixed compact neighborhood of $T$.
Continuity of $f$ therefore implies uniform continuity and boundedness on
that compact set. Consequently the line integrals along the moving segments
converge to the line integrals along the limiting segments. Taking the limit
in the equality from step <1>2 gives the asserted upper-half-plane boundary
integral equal to zero.

:::

:::

::: pf-step

The analogous integral for the lower half-plane also vanishes.


::: pf-proof

For $\varepsilon>0$, set
$$
T^-_\varepsilon=T\cap\{z:\Im z\le-\varepsilon\}.
$$
Its nondegenerate instances lie entirely in the open lower half-plane,
where $f$ is holomorphic. Cauchy's theorem gives
$$
\int_{\partial T^-_\varepsilon}f(z)\,dz=0.
$$
The same compactness and continuity argument as in step <1>3 allows
$\varepsilon\downarrow0$, yielding zero for the boundary integral of
$T\cap\{\Im z\le0\}$.

:::

:::

::: pf-step

One has
$$
\int_{\partial T}f(z)\,dz=0.
$$


::: pf-proof

Add the two limiting boundary integrals from steps <1>3 and <1>4. Every
segment lying on the real axis occurs twice with opposite orientations, so
those contributions cancel. The remaining oriented segments are exactly
the boundary of $T$. Therefore their sum is
$$
\int_{\partial T}f(z)\,dz,
$$
and it is zero.

If $T$ lies entirely in one closed half-plane, the same argument applies
with the other intersection empty; if a side or vertex lies on the real
axis, the limiting-segment argument above already includes that case.

:::

:::

::: pf-step

The function $f$ is entire.


::: pf-proof

Step <1>5 proves the triangular integral condition required in step <1>1.
Morera's theorem therefore implies that $f$ is holomorphic on all of
$\CC$.

:::

:::

::: pf-qed

Step <1>6 is exactly the desired conclusion.

:::

:::
