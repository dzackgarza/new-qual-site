---
schema: qual/card@1
id: P-TRIV-CA26
kind: problem
title: Saddle-point asymptotics of $\int_{-\infty}^\infty \frac{e^{-t(z^2-1/4)}\cos tz}{1+z^2}\,dz$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 26, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Use the saddle point method to approximate $f ( t ) = \int _ { - \infty } ^ { \infty } \frac { e ^ { - t ( z ^ { 2 } - 1 / 4 ) } \cos t z } { 1 + z ^ { 2 } } \mathrm { d } z$ for $t \gg 1$
:::

::: {.solution}

Define
$$
J(t)
=
\int_{-\infty}^{\infty}
\frac{
e^{-t(z^2-1/4)}e^{itz}
}{
1+z^2
}\,dz.
$$
Then
$$
f(t)=\operatorname{Re}J(t).
$$

::: pf

::: {.pf-step #s1-1}

The exponential phase completes to a square:
$$
-t\left(z^2-\frac14\right)+itz
=
-t\left(z-\frac i2\right)^2.
$$


::: pf-proof

One has
$$
\left(z-\frac i2\right)^2
=
z^2-iz-\frac14.
$$
Multiplying by $-t$ gives the stated identity.

:::

:::

::: pf-step

The saddle point of the phase is
$$
z_0=\frac i2.
$$


::: pf-proof

The phase is
$$
\Phi(z)
=
-\left(z-\frac i2\right)^2.
$$
Hence
$$
\Phi'(z)
=
-2\left(z-\frac i2\right),
$$
which vanishes only at $z=i/2$.

:::

:::

::: pf-step

The contour of integration may be shifted from the real axis to the line
$$
\operatorname{Im}z=\frac12.
$$


::: pf-proof

The only poles of
$$
\frac1{1+z^2}
$$
are at $z=\pm i$, so no pole lies in the strip
$$
0\leq\operatorname{Im}z\leq\frac12.
$$

Integrate around the rectangle with vertices
$$
-R,quad R,quad R+\frac i2,quad -R+\frac i2.
$$
On either vertical side, write
$$
z=\pm R+iy,
\qquad
0\leq y\leq\frac12.
$$
Then
$$
\operatorname{Re}
\left(z-\frac i2\right)^2
=
R^2-\left(y-\frac12\right)^2
\geq
R^2-\frac14.
$$
Thus the exponential factor is bounded by
$$
e^{-t(R^2-1/4)}.
$$
Meanwhile
$$
\abs{1+z^2}
\asymp
R^2
$$
uniformly on the vertical sides. Since those sides have length $1/2$, their
integrals tend to $0$ as $R\to\infty$. Cauchy's theorem therefore gives the
contour shift.

:::

:::

::: {.pf-step #s1-4}

After the shift
$$
z=x+\frac i2,
$$
one obtains
$$
J(t)
=
\int_{-\infty}^{\infty}
\frac{e^{-tx^2}}
{1+(x+i/2)^2}
\,dx.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
z-\frac i2=x
$$
on the shifted contour, so the exponential becomes $e^{-tx^2}$. Also
$dz=dx$.

:::

:::

::: pf-step

The amplitude at the saddle is
$$
\frac1{1+(i/2)^2}
=
\frac43.
$$


::: pf-proof

Since
$$
\left(\frac i2\right)^2
=
-\frac14,
$$
one has
$$
1+\left(\frac i2\right)^2
=
\frac34.
$$
Taking the reciprocal gives $4/3$.

:::

:::

::: {.pf-step #s1-6}

As $t\to\infty$,
$$
J(t)
\sim
\frac43
\int_{-\infty}^{\infty}
e^{-tx^2}\,dx.
$$


::: pf-proof

Set
$$
A(x)
=
\frac1{1+(x+i/2)^2}.
$$
Then $A$ is analytic near $0$ and
$$
A(x)
=
A(0)+O(x)
=
\frac43+O(x).
$$
The Gaussian $e^{-tx^2}$ localizes the integral to a neighborhood of
$x=0$ of width $O(t^{-1/2})$. Equivalently, with $x=u/\sqrt t$,
$$
J(t)
=
\frac1{\sqrt t}
\int_{-\infty}^{\infty}
e^{-u^2}
A\left(\frac{u}{\sqrt t}\right)
\,du.
$$
Since
$$
A\left(\frac{u}{\sqrt t}\right)
\to
\frac43
$$
for each fixed $u$, and the amplitude is bounded on the shifted contour by an
integrable Gaussian majorant after this rescaling, dominated convergence gives
the stated asymptotic.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
J(t)
\sim
\frac43\sqrt{\frac\pi t}.
$$


::: pf-proof

Use the Gaussian integral
$$
\int_{-\infty}^{\infty}e^{-tx^2}\,dx
=
\sqrt{\frac\pi t}
$$
in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

The quantity $J(t)$ is real.


::: pf-proof

From step [](#s1-4){.pf-ref},
$$
J(t)
=
\int_{-\infty}^{\infty}
\frac{e^{-tx^2}}
{x^2+ix+3/4}
\,dx.
$$
The integrand at $-x$ is the complex conjugate of the integrand at $x$.
Therefore the contributions from $x$ and $-x$ have real sum, and the entire
integral is real.

:::

:::

::: {.pf-step #s1-9}

Hence
$$
\boxed{
f(t)
\sim
\frac43\sqrt{\frac\pi t}
}
\qquad
(t\to\infty).
$$


::: pf-proof

By definition,
$$
f(t)=\operatorname{Re}J(t).
$$
Step [](#s1-8){.pf-ref} gives
$$
\operatorname{Re}J(t)=J(t),
$$
and step [](#s1-7){.pf-ref} gives its leading asymptotic.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the saddle-point approximation.

:::

:::

:::
