---
schema: qual/card@1
id: P-PYCCN
kind: problem
title: A conformal map from the lens $|z-1|<2\cap|z+1|<2$ onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Find a conformal  map from $\theset{\abs{z-1} < 2} \intersect \theset{\abs{z+1} < 2}$ to $\HH$.
:::

::: {.solution}
Write $L$ for the lens and set
$$
T(z)\coloneqq\frac{z-i\sqrt3}{z+i\sqrt3}.
$$

::: pf

::: {.pf-step #corners}

The boundary circles $\abs{z-1}=2$ and $\abs{z+1}=2$ meet exactly at $z=\pm i\sqrt3$.

::: pf-proof

Subtracting the equations $\abs{z\mp1}^2=4$ gives $\Re z=0$, and then $1+y^2=4$ gives $y=\pm\sqrt3$.

:::

:::

::: {.pf-step #sector}

$T$ maps $L$ biholomorphically onto the sector $\theset{w : 2\pi/3<\arg w<4\pi/3}$.

::: pf-proof

By step [](#corners){.pf-ref}, $T$ sends the two corners of $L$ to $0$ and $\infty$, so it sends each boundary circle to a line through $0$ and each boundary arc of $L$ to a ray from $0$. The point $-1$ lies on $\abs{z-1}=2$ and the point $1$ on $\abs{z+1}=2$, and
$$
T(-1)=\frac{-1-i\sqrt3}{-1+i\sqrt3}=e^{2\pi i/3},
\qquad
T(1)=\frac{1-i\sqrt3}{1+i\sqrt3}=e^{4\pi i/3}.
$$
So the boundary arcs go to the rays of argument $2\pi/3$ and $4\pi/3$. Since $0\in L$ and $T(0)=-1$, the image of $L$ is the sector between these rays that contains $-1$.

:::

:::

::: pf-step

$$
\boxed{\Phi(z)=\left(e^{-2\pi i/3}\,\frac{z-i\sqrt3}{z+i\sqrt3}\right)^{3/2}},
$$
with the branch of $w^{3/2}$ satisfying $0<\arg(w^{3/2})<\pi$ on $\theset{0<\arg w<2\pi/3}$, is a conformal bijection from $L$ onto $\HH$.

::: pf-proof

By step [](#sector){.pf-ref}, $z\mapsto e^{-2\pi i/3}T(z)$ maps $L$ biholomorphically onto the sector $\theset{0<\arg w<2\pi/3}$, and the stated branch of $w\mapsto w^{3/2}$ maps this sector biholomorphically onto $\theset{0<\arg\zeta<\pi}=\HH$.

:::

:::

:::

:::
