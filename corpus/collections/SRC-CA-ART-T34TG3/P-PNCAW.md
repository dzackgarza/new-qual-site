---
schema: qual/card@1
id: P-PNCAW
kind: problem
title: $\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+a^2}\,dx=\pi e^{-a}$ for $a>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: problem
Show that
\[
\int_{-\infty}^{\infty} \frac{x \sin x}{x^{2}+a^{2}} d x=\pi e^{-a}, \quad \text { for all } a>0
.\]
:::

::: solution
Let
\[
F(z)=\frac{ze^{iz}}{z^2+a^2},
\qquad a>0,
\]
and integrate over the upper semicircle of radius $R>a$. The only pole in the upper half-plane is at $z=ia$, and
\[
\operatorname{Res}(F,ia)
=\frac{ia\,e^{-a}}{2ia}
=\frac{e^{-a}}2.
\]

On the semicircular arc $z=Re^{i\theta}$,
\[
|e^{iz}|=e^{-R\sin\theta},
\]
and, for large $R$,
\[
\left|\frac{z}{z^2+a^2}\right|\le \frac{C}{R}.
\]
Hence the arc integral is bounded by
\[
C\int_0^\pi e^{-R\sin\theta}\,d\theta.
\]
Using $\sin\theta\ge 2\theta/\pi$ on $0\le\theta\le\pi/2$ and symmetry about $\pi/2$, this is $O(R^{-1})$, so the arc contribution tends to zero.

Therefore the residue theorem gives
\[
\int_{-\infty}^{\infty}
\frac{x e^{ix}}{x^2+a^2}\,dx
=2\pi i\cdot\frac{e^{-a}}2
=\pi i e^{-a}.
\]
Taking imaginary parts yields
\[
\boxed{
\int_{-\infty}^{\infty}
\frac{x\sin x}{x^2+a^2}\,dx
=\pi e^{-a}.}
\]
:::
