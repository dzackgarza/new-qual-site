---
schema: qual/card@1
id: P-RKKCE
kind: problem
title: $\int_{-\infty}^{\infty}\frac{e^{-2\pi ix\xi}}{\cosh\pi x}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Hyperbolic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Compute the Fourier transform integral:
$$I(\xi) = \int_{-\infty}^{\infty} \frac{e^{-2\pi i x \xi}}{\cosh(\pi x)} \, dx$$
where $\xi \in \mathbb{R}$ and $\cosh z = \frac{e^z + e^{-z}}{2}$.
:::

::: solution
Let
\[
F(z)=\frac{e^{-2\pi i\xi z}}{\cosh(\pi z)}.
\]
Integrate over the rectangle with vertices $-R,R,R+i,-R+i$. The only pole in $0<\Im z<1$ is $z=i/2$, and
\[
\operatorname{Res}_{z=i/2}F
=
\frac{e^{\pi\xi}}{\pi\sinh(i\pi/2)}
=
\frac{e^{\pi\xi}}{i\pi}.
\]
Hence the contour integral equals
\[
2\pi i\operatorname{Res}_{i/2}F=2e^{\pi\xi}.
\]

On the top edge, using
\[
\cosh(\pi(x+i))=-\cosh(\pi x),
\]
and its reversed orientation,
\[
\int_{R+i}^{-R+i}F(z)\,dz
=e^{2\pi\xi}
\int_{-R}^{R}\frac{e^{-2\pi i\xi x}}{\cosh(\pi x)}\,dx.
\]
The vertical-edge integrals tend to $0$ as $R\to\infty$, since for $z=\pm R+iy$, $0\le y\le1$,
\[
|e^{-2\pi i\xi z}|\le e^{2\pi|\xi|},
\qquad
|\cosh(\pi z)|\ge \sinh(\pi R).
\]
Therefore
\[
(1+e^{2\pi\xi})I(\xi)=2e^{\pi\xi}.
\]
Thus
\[
I(\xi)=\frac{2e^{\pi\xi}}{1+e^{2\pi\xi}}
=rac1{\cosh(\pi\xi)}.
\]
:::
