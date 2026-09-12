---
schema: qual/card@1
id: P-CAF06E
kind: problem
title: "Counting roots of a polynomial in the right half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
How many roots of the equation $z^4 + 8z^3 + 3z^2 + 8z + 3 = 0$ lie in the right half plane?
Justify your answer.
:::

::: solution
Let
\[
p(z)=z^4+8z^3+3z^2+8z+3.
\]
On the imaginary axis,
\[
p(iy)=\bigl(y^4-3y^2+3\bigr)+8iy(1-y^2).
\]
The real part is always positive, because with $t=y^2$,
\[
t^2-3t+3=\left(t-\frac32\right)^2+\frac34>0.
\]
Hence $p$ has no zeros on the imaginary axis, and as that axis is traversed
from $iR$ down to $-iR$, a continuous choice of $\arg p(iy)$ stays in
$(-\pi/2,\pi/2)$ and has total change tending to $0$ as $R\to\infty$.

Now close the contour by the right semicircle
$z=Re^{i\theta}$, $-\pi/2\le\theta\le\pi/2$. Uniformly on this arc,
\[
\frac{p(z)}{z^4}=1+O(R^{-1}),
\]
so for large $R$ the change of argument of $p$ along the semicircle equals the
change for $z^4$, namely
\[
4\left(\frac\pi2-\left(-\frac\pi2\right)\right)=4\pi.
\]
Thus the total change of argument around the positively oriented boundary of
the right half-disk tends to $4\pi$. By the argument principle, the number of
zeros in the right half-plane is
\[
\frac{4\pi}{2\pi}=\boxed{2}.
\]
:::
