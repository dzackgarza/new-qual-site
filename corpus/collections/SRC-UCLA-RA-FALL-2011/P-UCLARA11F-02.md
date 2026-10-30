---
schema: qual/card@1
id: P-UCLARA11F-02
kind: problem
title: 'Fourier transform of surface measure on $S^2$ and an $L^2$ functional'
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - L²
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $d\sigma$ denote surface measure on the unit sphere $S^2\subset\RR^3$, so that $\int_{S^2}d\sigma=4\pi$.

(a) For $\xi\in\RR^3$, compute
$$
\int_{S^2} e^{i x\cdot \xi}\,d\sigma(x).
$$

(b) Using this, or otherwise, show that
$$
f\longmapsto \int_{S^2}\int_{S^2} f(x+y)\,d\sigma(x)\,d\sigma(y)
$$
extends uniquely from $C_c^\infty(\RR^3)$ to a bounded linear functional on $L^2(\RR^3)$.
:::

::: {.solution}

Use the Fourier-transform convention
$$
\widehat \mu(\xi)
=
\int_{\RR^3}e^{ix\cdot\xi}\,d\mu(x)
$$
for finite measures.

## Part (a)

Fix
$$
\xi\in\RR^3,
\qquad
\rho=\norm{\xi}.
$$

::: pf

::: pf-step

By rotational invariance of surface measure, the integral depends only on $\rho$.


::: pf-proof

If $R\in SO(3)$, then
$$
d\sigma(Rx)=d\sigma(x)
$$
and
$$
(Rx)\cdot(R\xi)=x\cdot\xi.
$$
Thus rotating $\xi$ does not change the integral.

:::

:::

::: pf-step

We may therefore assume
$$
\boxed{\xi=(0,0,\rho)}.
$$


::: pf-proof

Choose a rotation sending $\xi/\norm{\xi}$ to the north-pole direction when $\xi\ne0$. The case $\xi=0$ is immediate.

:::

:::

::: pf-step

Parametrize
$$
S^2
$$
by spherical coordinates
$$
x=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta),
$$
with
$$
0\le\theta\le\pi,
\qquad
0\le\phi<2\pi.
$$


::: pf-proof

This is the standard spherical-coordinate parametrization.

:::

:::

::: pf-step

In these coordinates,
$$
x\cdot\xi
=
\rho\cos\theta
$$
and
$$
d\sigma
=
\sin\theta\,d\theta\,d\phi.
$$


::: pf-proof

The dot product uses only the third coordinate, and the standard surface-area element on $S^2$ is $\sin\theta\,d\theta\,d\phi$.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\int_{S^2}e^{ix\cdot\xi}\,d\sigma(x)
=
2\pi
\int_0^\pi
e^{i\rho\cos\theta}\sin\theta\,d\theta.
$$


::: pf-proof

Integrate first in $\phi$, which contributes the factor $2\pi$.

:::

:::

::: {.pf-step #s1-6}

With
$$
u=\cos\theta,
$$
one obtains
$$
2\pi
\int_{-1}^{1}
e^{i\rho u}\,du.
$$


::: pf-proof

Since
$$
du=-\sin\theta\,d\theta,
$$
the bounds $\theta=0,\pi$ become $u=1,-1$, and reversing them removes the minus sign.

:::

:::

::: {.pf-step #s1-7}

If $\rho>0$,
$$
\int_{-1}^{1}e^{i\rho u}\,du
=
\frac{e^{i\rho}-e^{-i\rho}}{i\rho}
=
\frac{2\sin\rho}{\rho}.
$$


::: pf-proof

Integrate the exponential explicitly.

:::

:::

::: {.pf-step #s1-8}

Therefore, for $\xi\ne0$,
$$
\boxed{
\int_{S^2}e^{ix\cdot\xi}\,d\sigma(x)
=
4\pi\frac{\sin\norm{\xi}}{\norm{\xi}}}.
$$


::: pf-proof

Combine steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

At $\xi=0$,
$$
\boxed{
\int_{S^2}1\,d\sigma=4\pi}.
$$


::: pf-proof

This is the normalization of surface measure given in the problem.

:::

:::

::: {.pf-step #s1-10}

Thus, with the continuous value at the origin,
$$
\boxed{
\widehat\sigma(\xi)
=
4\pi
\frac{\sin\norm{\xi}}{\norm{\xi}}}.
$$


::: pf-proof

Since
$$
\frac{\sin r}{r}\to1
$$
as $r\to0$, the formula from step [](#s1-8){.pf-ref} extends continuously to the value $4\pi$ in step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

For every
$$
f\in C_c^\infty(\RR^3),
$$
the functional in the problem equals
$$
\boxed{
\int_{\RR^3}f(z)\,d\nu(z)}.
$$


::: pf-proof

By the definition of convolution of finite measures,
$$
\int f(z)\,d(\sigma*\sigma)(z)
=
\int_{S^2}\int_{S^2}
f(x+y)\,d\sigma(x)\,d\sigma(y).
$$

:::

:::

::: pf-step

The Fourier transform of $\nu$ is
$$
\boxed{
\widehat\nu(\xi)
=
\widehat\sigma(\xi)^2}.
$$


::: pf-proof

Fourier transform converts convolution of finite measures into pointwise multiplication:
$$
\widehat{\sigma*\sigma}
=
\widehat\sigma\,\widehat\sigma.
$$

:::

:::

::: {.pf-step #s1-13}

By part (a),
$$
\abs{\widehat\nu(\xi)}^2
=
(4\pi)^4
\frac{\sin^4\norm{\xi}}{\norm{\xi}^4}.
$$


::: pf-proof

Square
$$
\widehat\nu
=
\widehat\sigma^2
$$
and use step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

In polar coordinates on $\RR^3$,
$$
\int_{\RR^3}
\abs{\widehat\nu(\xi)}^2\,d\xi
=
C
\int_0^\infty
\frac{\sin^4 r}{r^2}\,dr
$$
for a positive constant $C$.


::: pf-proof

The Euclidean volume element is
$$
d\xi=4\pi r^2\,dr
$$
after integrating over the unit sphere. Combine this with the factor $r^{-4}$ from step [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

The integral
$$
\int_0^1
\frac{\sin^4 r}{r^2}\,dr
$$
converges.


::: pf-proof

For $0<r\le1$,
$$
\abs{\sin r}\le r,
$$
so
$$
0\le
\frac{\sin^4 r}{r^2}
\le
r^2,
$$
and $\int_0^1r^2\,dr<\infty$.

:::

:::

::: {.pf-step #s1-16}

The integral
$$
\int_1^\infty
\frac{\sin^4 r}{r^2}\,dr
$$
also converges.


::: pf-proof

Since
$$
\abs{\sin r}\le1,
$$
$$
0\le
\frac{\sin^4 r}{r^2}
\le
\frac1{r^2},
$$
and $\int_1^\infty r^{-2}\,dr<\infty$.

:::

:::

::: pf-step

Hence
$$
\boxed{
\widehat\nu\in L^2(\RR^3)}.
$$


::: pf-proof

Combine steps [](#s1-14){.pf-ref} through [](#s1-16){.pf-ref}.

:::

:::

::: {.pf-step #s1-18}

By Plancherel, there exists
$$
g\in L^2(\RR^3)
$$
whose Fourier transform is $\widehat\nu$.


::: pf-proof

The Fourier transform is an isomorphism of $L^2(\RR^3)$ onto itself up to the usual normalization constant.

:::

:::

::: {.pf-step #s1-19}

As tempered distributions,
$$
\boxed{\nu=g\,dx}.
$$


::: pf-proof

The finite measure $\nu$ defines a tempered distribution whose Fourier transform is $\widehat\nu$. The $L^2$ function $g$ defines a tempered distribution with the same Fourier transform by step [](#s1-18){.pf-ref}. Fourier transform is injective on tempered distributions, so the two distributions are equal.

:::

:::

::: {.pf-step #s1-20}

Therefore, for
$$
f\in C_c^\infty(\RR^3),
$$
the functional is
$$
\boxed{
\Lambda(f)
=
\int_{\RR^3}f(z)g(z)\,dz}.
$$


::: pf-proof

Combine steps [](#s1-11){.pf-ref} and [](#s1-19){.pf-ref}.

:::

:::

::: {.pf-step #s1-21}

By Cauchy--Schwarz,
$$
\boxed{
\abs{\Lambda(f)}
\le
\norm{g}_{L^2}\,
\norm{f}_{L^2}}.
$$


::: pf-proof

Apply the $L^2$ Cauchy--Schwarz inequality to step [](#s1-20){.pf-ref}.

:::

:::

::: pf-step

Hence $\Lambda$ is bounded with respect to the $L^2$-norm on $C_c^\infty(\RR^3)$.


::: pf-proof

Step [](#s1-21){.pf-ref} gives a uniform linear bound.

:::

:::

::: {.pf-step #s1-23}

Since
$$
C_c^\infty(\RR^3)
$$
is dense in $L^2(\RR^3)$, $\Lambda$ extends uniquely to a bounded linear functional on $L^2(\RR^3)$.


::: pf-proof

Every bounded linear functional on a dense subspace extends uniquely and continuously to the completion.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} proves part (a), and step [](#s1-23){.pf-ref} proves part (b).

:::

:::

:::
