---
schema: qual/card@1
id: P-UCLARA18S-07
kind: problem
title: Holomorphy of $F(z,z)$ for separately holomorphic continuous $F$
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Formula
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $F:\CC\times\CC\to\CC$ be jointly continuous and holomorphic in each variable separately. Show that
$$
z\mapsto F(z,z)
$$
is holomorphic.
:::

::: {.solution}

Define
$$
f(z)=F(z,z).
$$

::: pf

::: {.pf-step #s1-1}

Fix $z_0\in\CC$ and $R>0$. For every
$$
a,b\in D(z_0,R),
$$
one has
$$
\boxed{
F(a,b)
=
\frac1{(2\pi i)^2}
\int_{\abs{\zeta-z_0}=R}
\int_{\abs{\xi-z_0}=R}
\frac{F(\zeta,\xi)}
{(\zeta-a)(\xi-b)}
\,d\xi\,d\zeta}.
$$


::: pf-proof

For fixed $b$, the map
$$
\zeta\longmapsto F(\zeta,b)
$$
is entire. Cauchy's formula gives
$$
F(a,b)
=
\frac1{2\pi i}
\int_{\abs{\zeta-z_0}=R}
\frac{F(\zeta,b)}{\zeta-a}\,d\zeta.
$$

For each fixed $\zeta$ on the outer contour, the map
$$
\xi\longmapsto F(\zeta,\xi)
$$
is entire, so
$$
F(\zeta,b)
=
\frac1{2\pi i}
\int_{\abs{\xi-z_0}=R}
\frac{F(\zeta,\xi)}{\xi-b}\,d\xi.
$$
Substituting this identity into the first formula gives the displayed
iterated integral. Joint continuity ensures that the integrand is continuous
on the compact product of the two contour circles, so the iterated contour
integral is well-defined.

:::

:::

::: {.pf-step #s1-2}

For every $z\in D(z_0,R)$,
$$
\boxed{
f(z)
=
\frac1{(2\pi i)^2}
\int_{\abs{\zeta-z_0}=R}
\int_{\abs{\xi-z_0}=R}
\frac{F(\zeta,\xi)}
{(\zeta-z)(\xi-z)}
\,d\xi\,d\zeta}.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} with
$$
a=b=z.
$$

:::

:::

::: {.pf-step #s1-3}

For every $0<r<R$, the integrand in step [](#s1-2){.pf-ref} and its derivative
with respect to $z$ are uniformly bounded for
$$
\abs{z-z_0}\le r
$$
and
$$
\abs{\zeta-z_0}=\abs{\xi-z_0}=R.
$$


::: pf-proof

On the compact contour product,
$$
M_R
=
\max
\abs{F(\zeta,\xi)}
<\infty
$$
by joint continuity. If $\abs{z-z_0}\le r$, then
$$
\abs{\zeta-z}
\ge
R-r,
\qquad
\abs{\xi-z}
\ge
R-r.
$$
Thus
$$
\abs{
\frac{F(\zeta,\xi)}
{(\zeta-z)(\xi-z)}
}
\le
\frac{M_R}{(R-r)^2}.
$$
Differentiating the rational kernel gives
$$
\frac{\partial}{\partial z}
\frac1{(\zeta-z)(\xi-z)}
=
\frac1{(\zeta-z)^2(\xi-z)}
+
\frac1{(\zeta-z)(\xi-z)^2},
$$
whose absolute value is at most
$$
\frac{2}{(R-r)^3}.
$$
Multiplying by $M_R$ gives a uniform bound for the differentiated
integrand.

:::

:::

::: {.pf-step #s1-4}

The function $f$ is holomorphic on $D(z_0,R)$.


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, differentiation under the two contour integrals is
valid on every smaller closed disk
$$
\overline{D(z_0,r)}
\subset D(z_0,R).
$$
Therefore
$$
\begin{aligned}
f'(z)
=
\frac1{(2\pi i)^2}
\int_{\abs{\zeta-z_0}=R}
\int_{\abs{\xi-z_0}=R}
F(\zeta,\xi)
\left[
\frac1{(\zeta-z)^2(\xi-z)}
+
\frac1{(\zeta-z)(\xi-z)^2}
\right]
d\xi\,d\zeta.
\end{aligned}
$$
Thus the complex derivative exists at every $z\in D(z_0,R)$.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{z\longmapsto F(z,z)\text{ is entire}}.
$$


::: pf-proof

The center $z_0$ was arbitrary, and one may choose any $R>0$. Step
[](#s1-4){.pf-ref} therefore proves holomorphy in a neighborhood of every point of
$\CC$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
