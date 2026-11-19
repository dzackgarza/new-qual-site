---
schema: qual/card@1
id: P-WJTPS
kind: problem
title: Green's theorem for $\int_C xe^x\,dx+(ye^y+x^2)\,dy$ over the upper half of
  $(x-1)^2+y^2=1$
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
  - Green's Theorem
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The evaluation is correct, and there is a quick check of it: the region is the
    upper half of the disk of radius one centred at (1,0), whose centroid lies at
    x = 1 and whose area is pi/2, so the double integral of 2x is pi, which is
    what the polar computation gives. Green's theorem applies since both
    coefficients are smooth, the boundary is a piecewise smooth simple closed
    curve traversed counterclockwise, and the integrand of the double integral is
    dQ/dx - dP/dy = 2x. Nothing was changed. The statement itself was not
    re-read against the scan in this pass: the retained file
    assets/attachments/grad_prelim_Fall14.pdf has no text layer.
---

::: {.problem}
Let $R$ be the region in the first quadrant bounded by the curves $x^2 + y^2 = 2x$ and $y = 0$. Let $C$ be the boundary of the region $R$, oriented counterclockwise. Evaluate the line integral
$$
\int_C x e^x \, dx + (y e^y + x^2)\, dy.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The region is the upper half-disk
$$
R=\theset{(x,y)\suchthat (x-1)^2+y^2\le 1,\ y\ge 0},
$$
and
$$
\int_C x e^x\,dx+(y e^y+x^2)\,dy=\iint_R 2x\,dA.
$$

::: pf-proof

Completing the square, $x^2+y^2=2x$ is the circle $(x-1)^2+y^2=1$ of radius $1$ centered at $(1,0)$, which lies in $x\ge 0$. Together with $y=0$ it bounds the upper half-disk $R$, and $C=\partial R$ is a piecewise smooth simple closed curve oriented counterclockwise.

With $P=xe^x$ and $Q=ye^y+x^2$, both of class $C^1$ on $\RR^2$, Green's theorem gives
$$
\int_C P\,dx+Q\,dy=\iint_R\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA=\iint_R(2x-0)\,dA.
$$

:::

:::

::: {.pf-step #s2}

$$
\iint_R 2x\,dA=\pi.
$$

::: pf-proof

Use polar coordinates centered at $(1,0)$: $x=1+r\cos\theta$, $y=r\sin\theta$ with $0\le r\le 1$, $0\le\theta\le\pi$, and $dA=r\,dr\,d\theta$. Then
$$
\iint_R 2x\,dA
=\int_0^{\pi}\int_0^1 2(1+r\cos\theta)\,r\,dr\,d\theta
=\int_0^{\pi}\left(1+\frac23\cos\theta\right)d\theta
=\pi+\frac23\bigl[\sin\theta\bigr]_0^{\pi}
=\pi.
$$

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref},
$$
\int_C x e^x\,dx+(y e^y+x^2)\,dy=\boxed{\pi}.
$$

:::

:::

:::
