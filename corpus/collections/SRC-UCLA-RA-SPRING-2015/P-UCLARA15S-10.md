---
schema: qual/card@1
id: P-UCLARA15S-10
kind: problem
title: Evaluation of $\int_{\RR}\frac{dy}{(1+y^2)(1+(x-y)^2)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Determine
$$
\int_{-\infty}^{\infty}\frac{dy}{(1+y^2)(1+(x-y)^2)}
$$
for all $x\in\RR$.
Justify all manipulations.
:::

::: {.solution}

Let
$$
h(y)
\coloneqq
\frac1{1+y^2}.
$$
Use the Fourier transform convention
$$
\widehat h(\xi)
\coloneqq
\int_{\RR}h(y)e^{-i\xi y}\,dy.
$$

::: pf

::: {.pf-step #s1}

The integral in the problem is
$$
(h*h)(x).
$$


::: pf-proof

By definition of convolution,
$$
(h*h)(x)
=
\int_{\RR}
h(y)h(x-y)\,dy
=
\int_{\RR}
\frac{dy}
{(1+y^2)(1+(x-y)^2)}.
$$
Since $h\in L^1(\RR)$, the convolution is absolutely convergent for almost every $x$; in the present case the displayed integrand is continuous and decays like $\abs{y}^{-4}$, so it is absolutely integrable for every fixed $x$.

:::

:::

::: {.pf-step #s2}

For every $\xi\in\RR$,
$$
\widehat h(\xi)
=
\pi e^{-\abs{\xi}}.
$$


::: pf-proof

::: {.pf-step #s2-1}

If $\xi>0$, then
$$
\widehat h(\xi)
=
\pi e^{-\xi}.
$$


::: pf-proof

Integrate
$$
F_\xi(z)
=
\frac{e^{-i\xi z}}{1+z^2}
$$
over the contour consisting of $[-R,R]$ and the lower semicircle, oriented clockwise. On the lower semicircle,
$$
\abs{e^{-i\xi z}}
=
e^{\xi\operatorname{Im}z}
\le1,
$$
while
$$
\abs{1+z^2}
\ge
R^2-1.
$$
Thus the semicircle integral has absolute value at most
$$
\frac{\pi R}{R^2-1}
\longrightarrow0.
$$

The only enclosed pole is $z=-i$, with residue
$$
\operatorname*{Res}_{z=-i}F_\xi
=
\frac{e^{-i\xi(-i)}}{-2i}
=
\frac{e^{-\xi}}{-2i}.
$$
Because the contour is clockwise, the residue theorem gives
$$
\int_{-\infty}^{\infty}
\frac{e^{-i\xi y}}{1+y^2}\,dy
=
-2\pi i
\frac{e^{-\xi}}{-2i}
=
\pi e^{-\xi}.
$$

:::

:::

::: pf-step

If $\xi<0$, then
$$
\widehat h(\xi)
=
\pi e^{\xi}.
$$


::: pf-proof

Use the upper semicircle instead. Since $\xi<0$ and $\operatorname{Im}z\ge0$ there,
$$
\abs{e^{-i\xi z}}
=
e^{\xi\operatorname{Im}z}
\le1,
$$
so the semicircle contribution again tends to zero. The enclosed pole is $z=i$, whose residue is
$$
\operatorname*{Res}_{z=i}F_\xi
=
\frac{e^{-i\xi i}}{2i}
=
\frac{e^{\xi}}{2i}.
$$
The positively oriented residue theorem gives
$$
\widehat h(\xi)
=
2\pi i
\frac{e^{\xi}}{2i}
=
\pi e^{\xi}.
$$

:::

:::

::: {.pf-step #s2-3}

If $\xi=0$, then
$$
\widehat h(0)=\pi.
$$


::: pf-proof

Directly,
$$
\widehat h(0)
=
\int_{-\infty}^{\infty}
\frac{dy}{1+y^2}
=
\left[\arctan y\right]_{-\infty}^{\infty}
=
\pi.
$$

:::

:::

::: pf-qed

Steps [](#s2-1){.pf-ref} through [](#s2-3){.pf-ref} combine to give
$$
\widehat h(\xi)
=
\pi e^{-\abs{\xi}}
$$
for all real $\xi$.

:::

:::

:::

::: {.pf-step #s3}

The Fourier transform of the convolution is
$$
\widehat{h*h}(\xi)
=
\pi^2e^{-2\abs{\xi}}.
$$


::: pf-proof

Since $h\in L^1(\RR)$, Fubini's theorem applies to the convolution-transform calculation and gives
$$
\widehat{h*h}
=
\widehat h\,\widehat h.
$$
Apply step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

For every $x\in\RR$,
$$
(h*h)(x)
=
\frac1{2\pi}
\int_{\RR}
\pi^2e^{-2\abs{\xi}}
e^{ix\xi}\,d\xi.
$$


::: pf-proof

The function $h*h$ belongs to $L^1(\RR)$ because $h\in L^1$, and step [](#s3){.pf-ref} gives
$$
\widehat{h*h}(\xi)
=
\pi^2e^{-2\abs{\xi}}
\in
L^1(\RR).
$$
Fourier inversion therefore gives the displayed formula at every point of continuity of $h*h$. Convolution of two $L^1$ functions is continuous, so the formula holds for every real $x$.

:::

:::

::: {.pf-step #s5}

One has
$$
\int_{\RR}
e^{-2\abs{\xi}}
e^{ix\xi}\,d\xi
=
\frac4{x^2+4}.
$$


::: pf-proof

Using symmetry,
$$
\begin{aligned}
\int_{\RR}
e^{-2\abs{\xi}}
e^{ix\xi}\,d\xi
&=
2\operatorname{Re}
\int_0^\infty
e^{-(2-ix)\xi}\,d\xi\\
&=
2\operatorname{Re}
\frac1{2-ix}\\
&=
2\cdot
\frac2{4+x^2}\\
&=
\frac4{x^2+4}.
\end{aligned}
$$
The integral is absolutely convergent because $e^{-2\abs{\xi}}\in L^1$.

:::

:::

::: {.pf-step #s6}

Therefore
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{dy}
{(1+y^2)(1+(x-y)^2)}
=
\frac{2\pi}{x^2+4}
}
\qquad
(x\in\RR).
$$


::: pf-proof

By steps [](#s1){.pf-ref} and [](#s4){.pf-ref}, and [](#s5){.pf-ref},
$$
\begin{aligned}
(h*h)(x)
&=
\frac{\pi^2}{2\pi}
\frac4{x^2+4}\\
&=
\frac{2\pi}{x^2+4}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} gives the requested value for every real $x$, and the preceding steps justify the contour, Fubini, convolution, and Fourier inversion manipulations.

:::

:::

:::
