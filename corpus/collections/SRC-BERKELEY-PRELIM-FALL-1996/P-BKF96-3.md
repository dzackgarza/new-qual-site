---
schema: qual/card@1
id: P-BKF96-3
kind: problem
title: The integral $\int_0^\infty \sqrt{x}/(1+x^2)\,dx$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used a keyhole contour for z^(1/2)/(1+z^2) with branch argument in
    (0,2pi); the two banks contribute equally and the residues at plus/minus
    i give the value pi/sqrt(2).
---

::: {.problem}
Evaluate
\[
\int_0^\infty\frac{\sqrt{x}}{1+x^2}\,dx.
\]
:::

::: {.solution}
Let
$$
F(z)\coloneqq\frac{z^{1/2}}{1+z^2},
$$
where
$$
z^{1/2}
=
\exp\left(\frac12(\log\abs z+i\arg z)\right),
\qquad
0<\arg z<2\pi.
$$
Thus the branch cut is the positive real axis.

<1>1. On the upper bank of the positive real axis,
$$
F(x)=\frac{\sqrt{x}}{1+x^2},
$$
while on the lower bank,
$$
F(x)=-\frac{\sqrt{x}}{1+x^2}.
$$

::: {.proof}
On the upper bank, $\arg x=0$, so
$$
x^{1/2}=\sqrt x.
$$
On the lower bank, the branch has $\arg x=2\pi$, so
$$
x^{1/2}
=
\sqrt x\,e^{i\pi}
=
-\sqrt x.
$$
:::

<1>2. On a keyhole contour with outer radius $R$ and inner radius
$\varepsilon$, the two circular-arc integrals tend to zero as
$$
R\to\infty
\qquad\text{and}\qquad
\varepsilon\to0.
$$

::: {.proof}
On $\abs z=R$ with $R>2$,
$$
\abs{F(z)}
\leq
\frac{R^{1/2}}{R^2-1},
$$
while the arc length is at most $2\pi R$. Hence the outer-arc integral has
absolute value
$$
O(R^{-1/2})
\longrightarrow0.
$$

On $\abs z=\varepsilon<1/2$,
$$
\abs{F(z)}
\leq
\frac{\varepsilon^{1/2}}{1-\varepsilon^2},
$$
and the arc length is at most $2\pi\varepsilon$. Hence the inner-arc
integral is
$$
O(\varepsilon^{3/2})
\longrightarrow0.
$$
:::

<1>3. The poles inside the keyhole contour are $i$ and $-i$, with
$$
\Res_{z=i}F
=
\frac{e^{i\pi/4}}{2i}
$$
and
$$
\Res_{z=-i}F
=
-\frac{e^{3i\pi/4}}{2i}.
$$

::: {.proof}
Both poles are simple. At $i$, the chosen branch has
$$
i^{1/2}=e^{i\pi/4},
$$
so
$$
\Res_{z=i}F
=
\frac{i^{1/2}}{2i}
=
\frac{e^{i\pi/4}}{2i}.
$$
At $-i$, the chosen argument is $3\pi/2$, hence
$$
(-i)^{1/2}=e^{3i\pi/4}.
$$
Since the derivative of $1+z^2$ at $-i$ is $-2i$,
$$
\Res_{z=-i}F
=
\frac{e^{3i\pi/4}}{-2i}.
$$
:::

<1>4. The sum of the residues is
$$
\Res_{z=i}F+\Res_{z=-i}F
=
-\frac{i}{\sqrt2}.
$$

::: {.proof}
Using
$$
e^{i\pi/4}
=
\frac{1+i}{\sqrt2}
\qquad\text{and}\qquad
e^{3i\pi/4}
=
\frac{-1+i}{\sqrt2},
$$
one obtains
$$
\begin{aligned}
\Res_{z=i}F+\Res_{z=-i}F
&=
\frac{
e^{i\pi/4}-e^{3i\pi/4}
}{2i}\\
&=
\frac{\sqrt2}{2i}\\
&=
-\frac{i}{\sqrt2}.
\end{aligned}
$$
:::

<1>5. If
$$
I\coloneqq
\int_0^\infty\frac{\sqrt{x}}{1+x^2}\,dx,
$$
then
$$
2I=\sqrt2\,\pi.
$$

::: {.proof}
The upper bank is traversed from $\varepsilon$ to $R$ and contributes
$$
\int_\varepsilon^R
\frac{\sqrt{x}}{1+x^2}\,dx.
$$
By step <1>1, the lower-bank integrand has the opposite sign, but that bank
is traversed from $R$ back to $\varepsilon$. It therefore contributes the
same quantity. By step <1>2, the circular arcs vanish in the limit.

The residue theorem and step <1>4 consequently give
$$
2I
=
2\pi i
\left(
-\frac{i}{\sqrt2}
\right)
=
\sqrt2\,\pi.
$$
:::

<1>6. Therefore
$$
\boxed{
\int_0^\infty\frac{\sqrt{x}}{1+x^2}\,dx
=
\frac{\pi}{\sqrt2}
}.
$$

::: {.proof}
Divide the identity in step <1>5 by $2$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the requested value.
:::
:::
