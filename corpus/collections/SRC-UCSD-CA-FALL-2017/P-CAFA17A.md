---
schema: qual/card@1
id: P-CAFA17A
kind: problem
title: "Evaluation of the integral of (log x)^2/(1+x^2) via residues"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Using the calculus of residues, compute $\int_0^{\infty} \frac{\log^2 x}{1 + x^2}\,dx$.

You may wish to use the contour consisting of two half circles in the upper half plane, one of small radius and another of large radius, connected by two line segments along the real axis.
:::

::: {.solution}
Use the branch $0<\arg z<\pi$ of $\Log z$ on the upper half-plane and integrate
\[
F(z)=\frac{(\Log z)^2}{1+z^2}
\]
over the indicated indented upper-half-plane contour.

The small and large semicircular contributions tend to $0$. On the positive real axis, $\Log x=\log x$. On the negative real axis, writing $z=-x$ with $x>0$, we have $\Log(-x)=\log x+i\pi$. Hence the two real-axis pieces tend to
\[
\int_0^\infty\frac{(\log x)^2+(\log x+i\pi)^2}{1+x^2}\,dx.
\]
Let
\[
I_2=\int_0^\infty\frac{\log^2x}{1+x^2}\,dx,
\qquad
I_1=\int_0^\infty\frac{\log x}{1+x^2}\,dx=0.
\]
Since $\int_0^\infty(1+x^2)^{-1}dx=\pi/2$, the boundary integral is
\[
2I_2-\frac{\pi^3}{2}.
\]

The only enclosed pole is $z=i$. Since $\Log i=i\pi/2$,
\[
\operatorname{Res}(F,i)
=\frac{(i\pi/2)^2}{2i}
=\frac{\pi^2 i}{8}.
\]
Thus the residue theorem gives
\[
2I_2-\frac{\pi^3}{2}
=2\pi i\frac{\pi^2 i}{8}
=-\frac{\pi^3}{4}.
\]
Therefore
\[
\boxed{I_2=\frac{\pi^3}{8}}.
\]
:::
