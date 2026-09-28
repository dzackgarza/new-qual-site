---
schema: qual/card@1
id: P-BKS03-8A
kind: problem
title: Integral of $e^{-x^2}\cos(x^2)$ over $(0,\infty)$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Evaluate
\[
\int_0^{\infty}e^{-x^2}\cos(x^2)\,dx.
\]
:::

::: {.solution}
It is the real part of

$$
I\coloneqq\int_0^\infty e^{-(1+i)x^2}\,dx=\int_0^\infty e^{-\sqrt2e^{i\pi/4}x^2}\,dx=\int_0^\infty e^{-\sqrt2(e^{i\pi/8}x)^2}\,dx.
$$

Let $C$ denote the wedge-shaped closed contour consisting of the straight path from $0$ to $R>0$, the arc $\gamma$ given by $e^{it}R$ as $t$ goes from $0$ to $\pi/8$, and the straight path from $e^{i\pi/8}R$ to $0$. By Cauchy's theorem, $\int_Ce^{-\sqrt2z^2}\,dz=0$. But $\int_\gamma e^{-\sqrt2z^2}\,dz\to0$ as $R\to\infty$, since the integrand is bounded in absolute value by $\abs{e^{-\sqrt2e^{i\pi/4}R^2}}=e^{-R^2}$ along $\gamma$, while the length of $\gamma$ is $O(R)$. Thus $\int_Ce^{-\sqrt2z^2}\,dz=0$ implies

$$
0=\int_0^\infty e^{-\sqrt2z^2}\,dz-\int_0^\infty e^{-\sqrt2(e^{i\pi/8}x)^2}\,d(e^{i\pi/8}x)
$$

or equivalently,

$$
0=2^{-1/4}\int_0^\infty e^{-u^2}\,du-e^{i\pi/8}I,
$$

so $I=2^{-1/4}e^{-i\pi/8}\frac{\sqrt\pi}{2}$. Thus the answer, which is the real part of $I$, is

$$
2^{-5/4}\left(\cos\frac\pi8\right)\sqrt\pi.
$$
:::
