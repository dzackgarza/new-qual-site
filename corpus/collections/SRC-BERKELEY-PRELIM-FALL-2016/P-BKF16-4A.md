---
schema: qual/card@1
id: P-BKF16-4A
kind: problem
title: Evaluation of $\int_{-\infty}^{\infty}\sin^3 x/x^3\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet. Its small
    semicircle discussion incorrectly calls -3z^2 the leading term of
    e^(3iz)-3e^(iz), whose actual constant term is -2; that omitted
    -2/z^3 contribution integrates to zero on the symmetric indentation.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked absolute convergence of the target integral, both semicircle
    limits with orientation, and the imaginary-part relation yielding
    3*pi/4.
---

::: {.problem}
Find

$$
\int _ { - \infty } ^ { \infty } { \frac { \sin ^ { 3 } ( x ) } { x ^ { 3 } } } d x .
$$
:::

::: {.solution}
Set
$$
F(z)
\coloneqq
\frac{e^{3iz}-3e^{iz}}{z^3}.
$$

::: pf

::: {.pf-step #s1}

For real $x\ne0$,
$$
\operatorname{Im}F(x)
=
-4\frac{\sin^3x}{x^3}.
$$

::: pf-proof

The triple-angle identity gives
$$
\sin(3x)-3\sin x
=
-4\sin^3x.
$$
Since
$$
\operatorname{Im}(e^{3ix}-3e^{ix})
=
\sin(3x)-3\sin x,
$$
division by the real number $x^3$ gives the claim.

:::

:::

::: {.pf-step #s2}

The integral
$$
I
\coloneqq
\int_{-\infty}^{\infty}
\frac{\sin^3x}{x^3}\,dx
$$
is absolutely convergent.

::: pf-proof

As $x\to0$,
$$
\frac{\sin^3x}{x^3}
=
\left(\frac{\sin x}{x}\right)^3
\longrightarrow
1,
$$
so the integrand is bounded near $0$. For $\abs{x}\ge1$,
$$
\left|
\frac{\sin^3x}{x^3}
\right|
\le
\frac1{\abs{x}^3},
$$
whose integral over the two tails converges.

:::

:::

::: {.pf-step #s3}

For $0<r<R$, let $C_{r,R}$ be the positively oriented boundary
of the upper half-annulus
$$
\{z:r<\abs z<R,\ \operatorname{Im}z>0\}.
$$
Then
$$
\int_{C_{r,R}}F(z)\,dz=0.
$$

::: pf-proof

The contour consists of the real intervals
$$
[-R,-r]
\qquad\text{and}\qquad
[r,R],
$$
the upper semicircle of radius $R$ traversed counterclockwise, and the
upper semicircle of radius $r$ traversed clockwise.

The only possible singularity of $F$ is at $0$, which lies outside
the half-annular region bounded by the contour. Hence $F$ is
holomorphic on and inside $C_{r,R}$, so Cauchy's theorem gives the
displayed integral.

:::

:::

::: {.pf-step #s4}

The contribution from the outer semicircle tends to $0$ as
$R\to\infty$.

::: pf-proof

On the upper semicircle $\abs z=R$,
$$
\abs{e^{3iz}}
\le
1,
\qquad
\abs{e^{iz}}
\le
1.
$$
Therefore
$$
\abs{F(z)}
\le
\frac4{R^3}.
$$
The arc has length $\pi R$, so the estimation lemma gives
$$
\left|
\int_{\abs z=R,\ \operatorname{Im}z\ge0}
F(z)\,dz
\right|
\le
\frac{4\pi}{R^2}
\longrightarrow
0.
$$

:::

:::

::: {.pf-step #s5}

The contribution from the clockwise inner semicircle tends to
$$
3\pi i
$$
as $r\downarrow0$.

::: pf-proof

The Taylor expansion at $0$ is
$$
e^{3iz}-3e^{iz}
=
-2-3z^2-4iz^3+O(z^4).
$$
Hence
$$
F(z)
=
-\frac2{z^3}
-\frac3z
-4i
+O(z).
$$

Let $\gamma_r$ be the upper semicircle from $-r$ to $r$, so
$$
z=re^{i\theta},
\qquad
\pi\ge\theta\ge0.
$$
First,
$$
\int_{\gamma_r}-\frac2{z^3}\,dz
=
\left[\frac1{z^2}\right]_{-r}^{r}
=
0.
$$
Second,
$$
\int_{\gamma_r}-\frac3z\,dz
=
-3i\int_\pi^0d\theta
=
3\pi i.
$$
The remaining term
$$
-4i+O(z)
$$
is bounded uniformly on $\gamma_r$ for small $r$, while the arc length
is $\pi r$, so its integral tends to $0$. Thus the whole inner-arc
integral tends to $3\pi i$.

:::

:::

::: {.pf-step #s6}

Taking imaginary parts in the contour identity and then letting
$$
r\downarrow0,
\qquad
R\to\infty
$$
gives
$$
-4I+3\pi=0.
$$

::: pf-proof

By step [](#s3){.pf-ref}, the sum of the two real-axis integrals and the two arc
integrals is $0$. Step [](#s4){.pf-ref} makes the outer-arc contribution vanish,
and step [](#s5){.pf-ref} makes the imaginary part of the inner-arc contribution
tend to $3\pi$.

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the imaginary parts of the real-axis integrals
converge absolutely to
$$
\int_{-\infty}^{\infty}\operatorname{Im}F(x)\,dx
=
-4I.
$$
Taking imaginary parts and passing to the limits therefore yields the
displayed equation.

:::

:::

::: {.pf-step #s7}

The value of the integral is
$$
\boxed{\frac{3\pi}{4}}.
$$

::: pf-proof

Solve the equation in step [](#s6){.pf-ref} for $I$.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the requested value.

:::

:::

:::
