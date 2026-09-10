---
schema: qual/card@1
id: P-CAFA16C
kind: problem
title: "Evaluation of the integral of log(x)/(x^2+1) via residues"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Using the calculus of residues, compute $\int_0^{\infty} \frac{\log x}{x^2 + 1}\,dx$.
:::

::: solution
Use the branch $0<\arg z<2\pi$ of $\Log z$ and integrate
\[
F(z)=\frac{(\Log z)^2}{z^2+1}
\]
around a keyhole contour about the positive real axis.

On the upper side, $\Log x=\log x$; on the lower side, $\Log x=\log x+2\pi i$, and the orientation is reversed. Let
\[
I=\int_0^\infty\frac{\log x}{x^2+1}\,dx.
\]
The two radial sides therefore contribute, in the limit,
\[
\int_0^\infty\frac{(\log x)^2-(\log x+2\pi i)^2}{x^2+1}\,dx
=-4\pi i I+4\pi^2\int_0^\infty\frac{dx}{x^2+1}
=-4\pi i I+2\pi^3.
\]
The circular arcs vanish.

The poles are at $i$ and $-i$. With this branch,
\[
\Log i=\frac{\pi i}{2},\qquad \Log(-i)=\frac{3\pi i}{2}.
\]
Hence
\[
\operatorname{Res}(F,i)=\frac{\pi^2 i}{8},\qquad
\operatorname{Res}(F,-i)=-\frac{9\pi^2 i}{8},
\]
so their sum is $-\pi^2 i$. The residue theorem gives
\[
-4\pi i I+2\pi^3=2\pi i(-\pi^2 i)=2\pi^3.
\]
Therefore
\[
\boxed{I=0}.
\]
:::
