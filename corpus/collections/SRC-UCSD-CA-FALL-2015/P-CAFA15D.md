---
schema: qual/card@1
id: P-CAFA15D
kind: problem
title: "Evaluation of the integral of cos(x)/(x^6+1) via residues"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Evaluate $\int_0^{\infty} \frac{\cos x}{x^6 + 1}\,dx$.
:::

::: solution
Integrate
\[
F(z)=\frac{e^{iz}}{z^6+1}
\]
over the upper semicircle. Jordan's lemma gives vanishing of the arc contribution. The poles in the upper half-plane are
\[
\zeta_1=e^{i\pi/6},\qquad \zeta_2=i,\qquad \zeta_3=e^{5i\pi/6},
\]
and each is simple, with
\[
\operatorname{Res}(F,\zeta)=\frac{e^{i\zeta}}{6\zeta^5}.
\]
Hence
\[
\int_{-\infty}^{\infty}\frac{e^{ix}}{x^6+1}\,dx
=2\pi i\sum_{j=1}^3\frac{e^{i\zeta_j}}{6\zeta_j^5}.
\]
Taking real parts and dividing by $2$ gives
\[
\boxed{
\int_0^\infty\frac{\cos x}{x^6+1}\,dx
=\frac{\pi}{6e}
+\frac{\pi}{6\sqrt e}
\left(
\cos\frac{\sqrt3}{2}
+\sqrt3\sin\frac{\sqrt3}{2}
\right).}
\]
:::
