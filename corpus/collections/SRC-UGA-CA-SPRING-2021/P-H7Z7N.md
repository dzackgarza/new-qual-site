---
schema: qual/card@1
id: P-H7Z7N
kind: problem
title: A conformal map from a slit right half-plane minus a disc onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
  - Complex Logarithm
relations: []
review: draft
---

::: {.problem}
Let $R$ be the intersection of the right half-plane and the outside of the circle $\abs{z - {1\over 2}} = {1\over 2}$ with the line segment $[1, 2]$ removed, i.e. 
$$
R = \theset{z\in \CC\st \Re(z) > 0,\,\, \abs{z-{1\over 2}} > {1\over 2} } \sm \theset{z \coloneqq x+iy \st 1\leq x\leq 2,\,\, y=0}
.$$
Find a conformal map from $R$ to $\HH$ the upper half-plane.
:::

::: {.concept}
\envlist

- Blow up the point of tangency: inverting through a circle sends inner circles to lines, fixes the real line, and preserves regions between curves.
  E.g. the image of $\abs{z-i/2} =2$ is $\theset{ \Im(z) = 2}$

![attachments/Circle Inversion.gif](../../assets/attachments/Circle%20Inversion.gif)

- So $z\to 1/z$ maps the region onto a slit vertical strip.

:::

::: {.solution}
::: pf

::: {.pf-step #inv}
$w=1/z$ maps $R$ conformally onto the strip $S=\{0<\Re w<1\}$ minus the segment $[\tfrac12,1)$.

::: pf-proof
For $z=x+iy\neq0$, $\Re(1/z)=x/\abs{z}^2$. So $\Re z>0$ if and only if $\Re w>0$, and $\abs{z-\tfrac12}>\tfrac12$, that is $\abs{z}^2>x$, if and only if $\Re w<1$. The inversion is an involution of $\CC\setminus\{0\}$, and it maps $[1,2]$ onto $[\tfrac12,1]$, whose point $1$ is not in $S$.
:::

:::

::: {.pf-step #sin}
$\zeta=\sin\bigl(\pi(w-\tfrac12)\bigr)$ maps the slit strip of step [](#inv){.pf-ref} conformally onto $\Omega=\CC\setminus\bigl((-\infty,-1]\cup[0,\infty)\bigr)$.

::: pf-proof
$w\mapsto\pi(w-\tfrac12)$ maps $S$ onto $\{\abs{\Re s}<\pi/2\}$ and the slit onto $[0,\pi/2)$. The sine maps $\{\abs{\Re s}<\pi/2\}$ conformally onto $\CC\setminus\bigl((-\infty,-1]\cup[1,\infty)\bigr)$, and it maps $[0,\pi/2)$ onto $[0,1)$. Removing the image of the slit leaves $\Omega$.
:::

:::

::: {.pf-step #mob}
$\eta=\zeta/(\zeta+1)$ maps $\Omega$ conformally onto $\CC\setminus[0,\infty)$.

::: pf-proof
This Möbius map sends $-1\mapsto\infty$, $0\mapsto0$ and $\infty\mapsto1$, and it maps $\RR\cup\{\infty\}$ to itself. It maps $[-\infty,-1]$ onto $[1,\infty]$ and $[0,\infty]$ onto $[0,1]$, so the removed set $(-\infty,-1]\cup[0,\infty)\cup\{\infty\}$ goes onto $[0,\infty]$.
:::

:::

::: {.pf-step #root}
The branch of $\sqrt{\eta}$ with argument in $(0,\pi)$ maps $\CC\setminus[0,\infty)$ conformally onto $\HH$.

::: pf-proof
Write $\eta=re^{i\theta}$ with $0<\theta<2\pi$; then $\sqrt\eta=\sqrt r\,e^{i\theta/2}$ with $0<\theta/2<\pi$, and this is a bijection with holomorphic inverse $\omega\mapsto\omega^2$.
:::

:::

::: pf-qed
The composite of steps [](#inv){.pf-ref} to [](#root){.pf-ref} is a conformal map of $R$ onto $\HH$. Since $\sin(\pi/z-\pi/2)=-\cos(\pi/z)$, it is
$$
\boxed{F(z)=\sqrt{\frac{\cos(\pi/z)}{\cos(\pi/z)-1}}}
$$
with the branch of step [](#root){.pf-ref}.
:::

:::

:::
