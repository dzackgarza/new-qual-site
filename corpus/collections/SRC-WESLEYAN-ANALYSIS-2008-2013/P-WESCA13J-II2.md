---
schema: qual/card@1
id: P-WESCA13J-II2
kind: problem
title: 'Three contour and winding-number calculations'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Evaluate or prove the following.

(a)
$$
\int_{\abs{z}=2}\frac{e^z}{(1+z)^2}\,dz.
$$

(b) For $\gamma(t)=2\cos t+i\sin t$, $0\le t\le2\pi$, evaluate
$$
\int_\gamma\frac{dz}{z^2+2iz}.
$$

(c) If $\gamma$ is a piecewise smooth closed path, verify
$$
n(\overline\gamma,\overline z)=-n(\gamma,z).
$$
:::

::: {.solution}

::: pf

::: pf-step

In part (a), the only singularity inside
$$
\abs{z}=2
$$
is the double pole at
$$
z=-1.
$$


::: pf-proof

The integrand is
$$
\frac{e^z}{(z+1)^2}.
$$
The numerator is entire, and the denominator vanishes only at
$$
z=-1,
$$
which satisfies
$$
\abs{-1}<2.
$$

:::

:::

::: {.pf-step #s1-2}

The integral in part (a) is
$$
\boxed{
\int_{\abs{z}=2}
\frac{e^z}{(1+z)^2}
\,dz
=
\frac{2\pi i}{e}}.
$$


::: pf-proof

Cauchy's differentiation formula states
$$
\int_{\abs{z}=2}
\frac{f(z)}{(z-a)^2}
\,dz
=
2\pi i f'(a)
$$
when
$$
a
$$
lies inside the positively oriented circle.

Take
$$
f(z)=e^z,
\qquad
a=-1.
$$
Then
$$
f'(-1)=e^{-1},
$$
so
$$
\int_{\abs{z}=2}
\frac{e^z}{(z+1)^2}
\,dz
=
2\pi i e^{-1}.
$$

:::

:::

::: pf-step

In part (b), the path
$$
\gamma(t)
=
2\cos t+i\sin t,
\qquad
0\le t\le2\pi,
$$
is the positively oriented ellipse
$$
\frac{x^2}{4}+y^2=1.
$$


::: pf-proof

Writing
$$
z=x+iy,
$$
the parametrization gives
$$
x=2\cos t,
\qquad
y=\sin t,
$$
and therefore
$$
\frac{x^2}{4}+y^2
=
\cos^2t+\sin^2t
=1.
$$
At
$$
t=0,
$$
the point is
$$
2
$$
and
$$
\gamma'(0)=i,
$$
so the traversal initially moves upward from the rightmost point and is counterclockwise.

:::

:::

::: {.pf-step #s1-4}

Of the two poles
$$
0
\quad\text{and}\quad
-2i
$$
of
$$
\frac1{z^2+2iz},
$$
only
$$
0
$$
lies inside
$$
\gamma.
$$


::: pf-proof

Factor the denominator:
$$
z^2+2iz
=
z(z+2i).
$$
The origin satisfies
$$
\frac{0^2}{4}+0^2<1,
$$
so it lies inside the ellipse.

The point
$$
-2i
$$
has coordinates
$$
(0,-2),
$$
and
$$
\frac{0^2}{4}+(-2)^2
=4
>1,
$$
so it lies outside.

:::

:::

::: {.pf-step #s1-5}

The residue at the enclosed pole is
$$
\operatorname{Res}_{z=0}
\frac1{z(z+2i)}
=
\frac1{2i}.
$$


::: pf-proof

The pole at
$$
0
$$
is simple, so
$$
\operatorname{Res}_{z=0}
\frac1{z(z+2i)}
=
\lim_{z\to0}
\frac1{z+2i}
=
\frac1{2i}.
$$

:::

:::

::: {.pf-step #s1-6}

The integral in part (b) is
$$
\boxed{
\int_\gamma
\frac{dz}{z^2+2iz}
=
\pi}.
$$


::: pf-proof

By the residue theorem and steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref},
$$
\int_\gamma
\frac{dz}{z(z+2i)}
=
2\pi i
\left(
\frac1{2i}
\right)
=
\pi.
$$

:::

:::

::: pf-step

For part (c), assume
$$
z\notin\gamma([a,b]).
$$
Then
$$
n(\gamma,z)
=
\frac1{2\pi i}
\int_a^b
\frac{\gamma'(t)}
{\gamma(t)-z}
\,dt.
$$


::: pf-proof

This is the standard integral definition of the winding number of a piecewise smooth closed path about a point outside its image.

:::

:::

::: {.pf-step #s1-8}

The conjugate path satisfies
$$
\overline\gamma'(t)
=
\overline{\gamma'(t)}
$$
at every differentiability point, and hence
$$
\int_{\overline\gamma}
\frac{dw}{w-\overline z}
=
\overline{
\int_\gamma
\frac{d\zeta}{\zeta-z}
}.
$$


::: pf-proof

Parametrize
$$
\overline\gamma
$$
by
$$
t\longmapsto\overline{\gamma(t)}.
$$
Then
$$
\begin{aligned}
\int_{\overline\gamma}
\frac{dw}{w-\overline z}
&=
\int_a^b
\frac{
\overline{\gamma'(t)}
}{
\overline{\gamma(t)}-\overline z
}
\,dt\\
&=
\int_a^b
\overline{
\frac{
\gamma'(t)
}{
\gamma(t)-z
}
}
\,dt\\
&=
\overline{
\int_a^b
\frac{
\gamma'(t)
}{
\gamma(t)-z
}
\,dt
}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-9}

Since
$$
\int_\gamma
\frac{d\zeta}{\zeta-z}
=
2\pi i\,n(\gamma,z),
$$
one has
$$
\overline{
\int_\gamma
\frac{d\zeta}{\zeta-z}
}
=
-2\pi i\,n(\gamma,z).
$$


::: pf-proof

The winding number
$$
n(\gamma,z)
$$
is an integer, hence real. Therefore
$$
\overline{
2\pi i\,n(\gamma,z)
}
=
-2\pi i\,n(\gamma,z).
$$

:::

:::

::: {.pf-step #s1-10}

Consequently,
$$
\boxed{
n(\overline\gamma,\overline z)
=
-n(\gamma,z)}.
$$


::: pf-proof

Using steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref},
$$
\begin{aligned}
n(\overline\gamma,\overline z)
&=
\frac1{2\pi i}
\int_{\overline\gamma}
\frac{dw}{w-\overline z}\\
&=
\frac1{2\pi i}
\left(
-2\pi i\,n(\gamma,z)
\right)\\
&=
-n(\gamma,z).
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} solves part (a), step [](#s1-6){.pf-ref} solves part (b), and step [](#s1-10){.pf-ref} proves part (c).

:::

:::

:::
