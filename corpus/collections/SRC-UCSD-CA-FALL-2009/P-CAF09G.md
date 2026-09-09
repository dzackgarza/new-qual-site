---
schema: qual/card@1
id: P-CAF09G
kind: problem
title: "Zeros of a sum of sin functions at cube roots of unity"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Suppose $\rho$ is a third root of 1 (other than 1). Let $f(z) = \sin(z) + \sin(\rho z) + \sin(\rho^2 z)$.
Prove that $f(z)$ has a zero other than $z = 0$.
:::

::: solution
Since $\rho\ne1$ and $\rho^3=1$,
\[
1+\rho+\rho^2=0.
\]
For any $x+y+w=0$, the identity
\[
\sin x+\sin y+\sin w
=-4\sin\frac x2\sin\frac y2\sin\frac w2
\]
holds. Applying this with
\[
x=z,\qquad y=\rho z,\qquad w=\rho^2z
\]
gives
\[
f(z)
=-4\sin\frac z2\,
\sin\frac{\rho z}{2}\,
\sin\frac{\rho^2 z}{2}.
\]
Thus every nonzero multiple of $2\pi$ is a zero of $f$. In particular,
\[
f(2\pi)=0,
\]
so $f$ has a zero other than the origin.
:::
