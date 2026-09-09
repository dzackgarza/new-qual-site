---
schema: qual/card@1
id: P-CAFA19A
kind: problem
title: "Evaluation of the integral of x^2/(x^4+5x^2+4) via residues"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Compute the integral $\int_0^{\infty} \frac{x^2}{x^4 + 5x^2 + 4}\,dx$.
:::

::: solution
Factor
\[
x^4+5x^2+4=(x^2+1)(x^2+4).
\]
For
\[
F(z)=\frac{z^2}{(z^2+1)(z^2+4)},
\]
integrate over the upper semicircle. Since $F(z)=O(|z|^{-2})$, the arc
integral tends to $0$. The poles in the upper half-plane are $i$ and $2i$,
with residues
\[
\operatorname{Res}(F,i)
=\frac{i^2}{(2i)(i^2+4)}=\frac{i}{6},
\]
and
\[
\operatorname{Res}(F,2i)
=\frac{(2i)^2}{((2i)^2+1)(4i)}=-\frac{i}{3}.
\]
Hence
\[
\int_{-\infty}^{\infty}\frac{x^2}{x^4+5x^2+4}\,dx
=2\pi i\left(-\frac{i}{6}\right)=\frac{\pi}{3}.
\]
The integrand is even, so
\[
\boxed{\displaystyle \int_0^\infty\frac{x^2}{x^4+5x^2+4}\,dx=\frac{\pi}{6}.}
\]
:::
