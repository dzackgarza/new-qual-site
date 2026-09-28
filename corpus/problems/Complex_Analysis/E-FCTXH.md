---
schema: qual/card@1
id: E-FCTXH
kind: problem
title: $f(z)=-\frac12\bigl(z+\frac1z\bigr)$ maps the upper half-disk conformally onto
  the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Geometry
relations: []
review: draft
---

::: {.problem}
Prove that $\displaystyle{f(z)=-\frac{1}{2}\left(z+\frac{1}{z}\right)}$ is a conformal map from the half disc
\[
\{z=x+iy:\ |z|<1,\ y>0\}
\]
to $\HH \da \{z=x+iy:\ y>0\}$.
:::

::: {.solution}
The map $f$ is holomorphic on the half disc, and $f'(z)=-{1\over2}\qty{1-z^{-2}}\neq0$ there since $z\neq\pm1$, so it suffices to show that $f$ maps the half disc bijectively onto $\HH$.
Consider the images of arcs $\gamma_R(t) \da Re^{it}$ for $t\in (0, \pi)$ and $0<R<1$, which partition the upper half disc:
\[
f(Re^{it}) = - {1\over 2}\qty{ \qty{R+\inverseof{R}}\cos(t) + i(R-\inverseof{R})\sin(t) } = H_R\cos(t) + iV_R\sin(t)
,\]
where $H_R \da -{1\over 2}\qty{R+\inverseof{R}}$ and $V_R \da {1\over 2}(\inverseof{R}-R)$. Here $H_R^2-V_R^2=1$, $\abs{H_R}>1$ and $V_R>0$.
So as $t$ ranges through $(0, \pi)$, $f\circ\gamma_R$ traces the upper half of the ellipse $E_R$ with semi-axes $\abs{H_R}$ and $V_R$ and foci $\pm1$, once and injectively.

As $R$ decreases from $1$ to $0$, $V_R$ increases from $0$ to $\infty$.
The confocal ellipses $\theset{E_R}_{0<R<1}$ are pairwise disjoint and their union is $\CC\setminus[-1,1]$: a point $w\notin[-1,1]$ lies on the unique such ellipse with $\abs{w-1}+\abs{w+1}=2\abs{H_R}$.
So each $w\in\HH$ lies on exactly one upper half-ellipse, and has exactly one preimage in the half disc.

:::
