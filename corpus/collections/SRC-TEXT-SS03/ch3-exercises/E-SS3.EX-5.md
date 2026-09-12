---
schema: qual/card@1
id: E-SS3.EX-5
kind: problem
title: "SS 3.5: The Fourier transform of (1+x^2)^-2"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
5. Use contour integration to show that

$$
\int_ {- \infty} ^ {\infty} \frac {e ^ {- 2 \pi i x \xi}}{(1 + x ^ {2}) ^ {2}} d x = \frac {\pi}{2} (1 + 2 \pi | \xi |) e ^ {- 2 \pi | \xi |}
$$

for all ξ real.
:::

::: solution
Let
\[
I(\xi)=\int_{-\infty}^{\infty}\frac{e^{-2\pi i x\xi}}{(1+x^2)^2}\,dx.
\]
First assume $\xi>0$. Close the contour in the lower half-plane, where
\[
|e^{-2\pi i z\xi}|=e^{2\pi\xi\operatorname{Im}z}
\]
decays. The only enclosed pole is the double pole at $z=-i$. Since the contour is clockwise,
\[
I(\xi)=-2\pi i\operatorname{Res}_{z=-i}
\frac{e^{-2\pi i z\xi}}{(z-i)^2(z+i)^2}.
\]
The residue is
\[
\left.\frac{d}{dz}\frac{e^{-2\pi i z\xi}}{(z-i)^2}\right|_{z=-i}
=e^{-2\pi\xi}
\left(\frac{-2\pi i\xi}{(-2i)^2}-\frac{2}{(-2i)^3}\right)
=\frac{i}{4}(1+2\pi\xi)e^{-2\pi\xi}.
\]
Therefore
\[
I(\xi)=\frac\pi2(1+2\pi\xi)e^{-2\pi\xi}
\qquad(\xi>0).
\]

For $\xi<0$, close in the upper half-plane; the analogous residue at $z=i$ gives
\[
I(\xi)=\frac\pi2(1-2\pi\xi)e^{2\pi\xi}
=\frac\pi2(1+2\pi|\xi|)e^{-2\pi|\xi|}.
\]
At $\xi=0$, either evaluate directly or let $\xi\to0$; in both cases $I(0)=\pi/2$. Thus for every real $\xi$,
\[
\boxed{I(\xi)=\frac\pi2(1+2\pi|\xi|)e^{-2\pi|\xi|}}.
\]
:::
