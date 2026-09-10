---
schema: qual/card@1
id: P-CASP09B
kind: problem
title: "Counting zeros of z^7 + 2z^3 + 4 in the first quadrant"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Find the number of zeros of $f(z) = z^7 + 2z^3 + 4$ in the interior of the first quadrant (all $z = x + iy$ with $x$ and $y$ positive).
:::

::: solution
Let
\[
P(z)=z^7+2z^3+4.
\]
There are no zeros on the positive real or positive imaginary axes: for
$x>0$, $P(x)>0$, while
\[
P(iy)=4-i(y^7+2y^3)\ne0\qquad(y>0).
\]

Apply the argument principle to the boundary of the quarter-disk
\[
Q_R=\{z:|z|<R,\ 0<\arg z<\pi/2\}
\]
for large $R$. Along the positive real segment, the argument of $P$ is constant
equal to $0$.

On the quarter-circle $z=Re^{i\theta}$,
\[
P(z)=z^7\left(1+2z^{-4}+4z^{-7}\right),
\]
so uniformly in $0\le\theta\le\pi/2$ the parenthetical factor tends to $1$ as
$R\to\infty$. Hence the argument change on that arc tends to
\[
7\cdot\frac\pi2=\frac{7\pi}{2}.
\]

On the positive imaginary axis, traversed downward from $iR$ to $0$,
\[
P(iy)=4-i(y^7+2y^3).
\]
Its principal argument increases from a value tending to $-\pi/2$ to $0$.
Using the continuous lift matching the value $7\pi/2$ at the top of the arc,
the argument therefore increases from $7\pi/2$ to $4\pi$, contributing
$\pi/2$.

Thus the total argument variation tends to
\[
\frac{7\pi}{2}+\frac\pi2=4\pi.
\]
For all sufficiently large $R$ the zero count is the integer
$4\pi/(2\pi)=2$. Therefore
\[
\boxed{P\text{ has exactly two zeros in the open first quadrant}.}
\]
:::
