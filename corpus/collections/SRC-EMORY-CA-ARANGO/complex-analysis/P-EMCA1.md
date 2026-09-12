---
schema: qual/card@1
id: P-EMCA1
kind: problem
title: "Residue computation of cos(x)/(x^2+1)^2"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Use residues to compute the integral
$$
\int_0^\infty \frac{\cos x}{(x^2 + 1)^2}\,dx.
$$
:::

::: solution
Integrate
\[
F(z)=\frac{e^{iz}}{(z^2+1)^2}
\]
over the upper semicircle of radius $R>1$. On the semicircular arc,
$|e^{iz}|=e^{-\operatorname{Im}z}\le 1$, while the denominator has order
$R^4$, so the arc integral tends to $0$ as $R\to\infty$.

The only pole in the upper half-plane is the double pole at $z=i$. Since
\[
F(z)=\frac{e^{iz}}{(z-i)^2(z+i)^2},
\]
its residue is
\[
\begin{aligned}
\operatorname{Res}(F,i)
&=\left.\frac{d}{dz}\frac{e^{iz}}{(z+i)^2}\right|_{z=i}\\
&=\left.e^{iz}\left(\frac{i}{(z+i)^2}-\frac{2}{(z+i)^3}\right)\right|_{z=i}\\
&=-\frac{i}{2e}.
\end{aligned}
\]
Therefore the residue theorem gives
\[
\int_{-\infty}^{\infty}\frac{e^{ix}}{(x^2+1)^2}\,dx
=2\pi i\left(-\frac{i}{2e}\right)
=\frac{\pi}{e}.
\]
Taking real parts,
\[
\int_{-\infty}^{\infty}\frac{\cos x}{(x^2+1)^2}\,dx=\frac{\pi}{e}.
\]
The integrand is even, hence
\[
\boxed{\displaystyle
\int_0^\infty\frac{\cos x}{(x^2+1)^2}\,dx=\frac{\pi}{2e}.}
\]
:::
