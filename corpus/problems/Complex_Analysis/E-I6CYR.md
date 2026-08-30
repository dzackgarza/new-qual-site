---
schema: qual/card@1
id: E-I6CYR
kind: exercise
title: $B(z,w)=\frac{\Gamma(z)\Gamma(w)}{\Gamma(z+w)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Integrals
  - Convolution
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

:::{.exercise}
Show that
\[
B(z, w) = {\Gamma(z) \Gamma(w) \over \Gamma(z+w)}
.\]

> Hint: find $\mcl(t^{z-1})$ and $\mcl(t^{z-1}\convolve t^{w-1})$.
:::

::: solution
**Goal:** Use the Laplace transform and convolution to identify the Beta integral.

<1> For $\Re z,\Re w>0$, define $f(t)=t^{z-1}\mathbf 1_{[0,1]}(t)$ and $g(t)=t^{w-1}\mathbf 1_{[0,1]}(t)$.
    Their Laplace transforms are
    $$
    \mathcal Lf(s)=\frac{\Gamma(z)}{s^z},\qquad
    \mathcal Lg(s)=\frac{\Gamma(w)}{s^w}.
    $$
    Hence
    $$
    \mathcal L(f*g)(s)=\frac{\Gamma(z)\Gamma(w)}{s^{z+w}}.
    $$

<1> Directly,
    $$
    (f*g)(x)=\int_0^x t^{z-1}(x-t)^{w-1}\mathbf 1_{0<x<2}\,dt
    =x^{z+w-1} B(z,w),
    \qquad 0<x<2.
    $$
    Therefore
    $$
    \mathcal L(f*g)(s)=B(z,w)\int_0^\infty x^{z+w-1}e^{-sx}\,dx
    =B(z,w)\frac{\Gamma(z+w)}{s^{z+w}}.
    $$

<1> Comparing Laplace transforms gives
    $$
    B(z,w)\frac{\Gamma(z+w)}{s^{z+w}}=\frac{\Gamma(z)\Gamma(w)}{s^{z+w}},
    $$
    so
    $$
    B(z,w)=\frac{\Gamma(z)\Gamma(w)}{\Gamma(z+w)}.
    $$

Authored by **Codex 5.3 Spark Extra High**.
:::
