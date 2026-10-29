---
schema: qual/card@1
id: P-4GWVV
kind: problem
title: A conformal map from the upper half-plane onto $\{-\pi/2<\Re w<\pi/2,\,\Im
  w>0\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Trigonometry
relations: []
review: draft
---

::: {.problem}
Find the conformal map that takes the upper half-plane conformally
onto the half-strip $\{
w=x+iy:\ -\pi/2<x<\pi/2,\ y>0\}$.
:::

::: {.solution}

Let $S\coloneqq\theset{w=x+iy\st -\frac\pi2<x<\frac\pi2,\ y>0}$.

::: pf

::: {.pf-step #into}
$\sin$ maps $S$ into $\HH$.

::: pf-proof
For $w=x+iy$, $\Im\sin w=\cos x\sinh y$, which is positive when $\abs{x}<\pi/2$ and $y>0$.
:::

:::

::: {.pf-step #injective}
$\sin$ is injective on $S$.

::: pf-proof
$\sin w_1=\sin w_2$ holds iff $w_1-w_2\in2\pi\ZZ$ or $w_1+w_2\in\pi+2\pi\ZZ$, because $\sin w_1-\sin w_2=2\cos\frac{w_1+w_2}2\sin\frac{w_1-w_2}2$.
For $w_1,w_2\in S$, $\Re(w_1+w_2)$ and $\Re(w_1-w_2)$ lie in $(-\pi,\pi)$, so only $w_1=w_2$ is possible.
:::

:::

::: {.pf-step #onto}
$\sin$ maps $S$ onto $\HH$.

::: pf-proof
Let $\zeta\in\HH$.
Since $\sin w-\zeta=\frac{1}{2i}e^{-iw}\qty(e^{2iw}-2i\zeta e^{iw}-1)$, if $u$ is a root of $u^2-2i\zeta u-1$, which is nonzero since the product of the roots is $-1$, and $w_0\coloneqq-i\log u$ for any logarithm of $u$, then $e^{iw_0}=u$ and $\sin w_0=\zeta$.
The solutions of $\sin w=\zeta$ include $w_0+2\pi k$ and $\pi-w_0+2\pi k$ for $k\in\ZZ$, and one of these has real part in $[-\pi/2,\pi/2]$: if $\Re w_0\in(-\pi,\pi]$, take $w_0$ when $\abs{\Re w_0}\leq\pi/2$, $\pi-w_0$ when $\Re w_0\in(\pi/2,\pi]$, and $-\pi-w_0$ when $\Re w_0\in(-\pi,-\pi/2)$.
For that solution $w=x+iy$, $\cos x\sinh y=\Im\zeta>0$ with $\cos x\geq0$, so $\cos x>0$ and $y>0$, that is, $w\in S$.
:::

:::

::: pf-step
The required map is $\boxed{z\mapsto\arcsin z}$, the inverse of $\sin\colon S\to\HH$: the branch of $\arcsin$ on $\HH$ with $-\pi/2<\Re\arcsin z<\pi/2$ and $\Im\arcsin z>0$.

::: pf-proof
By steps [](#into){.pf-ref}, [](#injective){.pf-ref} and [](#onto){.pf-ref}, $\sin\colon S\to\HH$ is a holomorphic bijection, so its inverse is holomorphic and maps $\HH$ conformally onto $S$.
:::

:::

:::

:::
