---
schema: qual/card@1
id: P-CAF13B
kind: problem
title: "Evaluation of the integral of cos(x)/(1+x^2) via residues"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Use residues to calculate $\int_{-\infty}^{\infty} \frac{\cos x}{1 + x^2}\,dx$.
:::

::: solution
Integrate
\[
F(z)=\frac{e^{iz}}{1+z^2}
\]
over the upper semicircle of radius $R>1$. On the arc,
$|e^{iz}|=e^{-\operatorname{Im}z}\le1$, while
\[
|1+z^2|\ge R^2-1.
\]
Since the arc has length $\pi R$,
\[
\left|\int_{\text{arc}}F(z)\,dz\right|
\le \frac{\pi R}{R^2-1}\longrightarrow0.
\]

The only pole in the upper half-plane is the simple pole at $z=i$, with
\[
\operatorname{Res}(F,i)
=\frac{e^{ii}}{2i}
=\frac{e^{-1}}{2i}.
\]
Hence
\[
\int_{-\infty}^{\infty}\frac{e^{ix}}{1+x^2}\,dx
=2\pi i\frac{e^{-1}}{2i}
=\frac{\pi}{e}.
\]
Taking real parts gives
\[
\boxed{\displaystyle
\int_{-\infty}^{\infty}\frac{\cos x}{1+x^2}\,dx=\frac{\pi}{e}.}
\]
:::
