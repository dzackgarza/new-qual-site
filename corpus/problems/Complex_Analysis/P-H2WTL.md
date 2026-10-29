---
schema: qual/card@1
id: P-H2WTL
kind: problem
title: Integrals of $z^n$ and $1/((z-a)(z-b))$ on circles, without Cauchy's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Winding Number
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source listed the parts as 1., 2., 3. while part 2 referred to "(a)"; the parts are now labelled (a)-(c). Part (b) read "any circle not containing the origin"; for n<0 the integral is undefined when the origin lies on the circle, so it now asks for a circle whose closed disk does not contain the origin. Part (c) printed the integrand as "dz/((z-a)(z-b)) dz"; the duplicated dz is removed.
---

::: {.problem}
The question provides some insight into Cauchy's theorem.
Solve the problem without using the Cauchy theorem.

(a) Evaluate the integral $\displaystyle{\int_{\gamma} z^n dz}$ for all integers $n$.
Here $\gamma$ is any circle centered at the origin with the positive (counterclockwise) orientation.

(b) Same question as (a), but with $\gamma$ any circle whose closed disk does not contain the origin.

(c) Show that if $\abs{a}<r<\abs{b}$, then $\displaystyle{\int_{\gamma}\frac{dz}{(z-a)(z-b)}=\frac{2\pi i}{a-b}}$.
Here $\gamma$ denotes the circle centered at the origin, of radius $r$, with the positive orientation.
:::

::: {.solution}
::: pf

::: {.pf-step #part-a}
(a) For the circle $\gamma$ of radius $R>0$ centered at $0$, $\displaystyle\int_\gamma z^n\,dz=\boxed{\begin{cases}2\pi i, & n=-1,\\ 0, & n\neq -1.\end{cases}}$

::: pf-proof
Parametrize $\gamma(t)=Re^{it}$, $t\in[0,2\pi]$, so $dz = iRe^{it}\,dt$ and
$$
\int_\gamma z^n\,dz = iR^{n+1}\int_0^{2\pi}e^{i(n+1)t}\,dt.
$$
For $n=-1$ the integrand is $1$ and the integral is $2\pi i$. For $n\neq-1$, $\int_0^{2\pi}e^{i(n+1)t}\,dt = \frac{e^{2\pi i(n+1)}-1}{i(n+1)} = 0$.
:::

:::

::: pf-step
(b) If the closed disk bounded by $\gamma$ does not contain $0$, then $\displaystyle\int_\gamma z^n\,dz=\boxed{0}$ for every $n\in\ZZ$.

::: pf-proof
For $n\neq -1$, $z^{n+1}/(n+1)$ is a primitive of $z^n$ on $\CC\setminus\theset{0}$, which contains $\gamma$; the integral of a derivative over a closed curve is $0$.
For $n=-1$, the closed disk lies in a half-plane $H$ not containing $0$ (a disk and a point outside it can be separated by a line). A branch of $\log z$ is holomorphic on $H$ with derivative $1/z$, so $\int_\gamma dz/z = 0$ for the same reason.
:::

:::

::: {.pf-step #partial-fractions}
$\dfrac{1}{(z-a)(z-b)} = \dfrac{1}{a-b}\qty{\dfrac{1}{z-a} - \dfrac{1}{z-b}}$.

::: pf-proof
Combine the right side over the common denominator: $(z-b)-(z-a) = a-b$.
:::

:::

::: {.pf-step #inner}
$\displaystyle\int_\gamma\frac{dz}{z-a} = 2\pi i$.

::: pf-proof
On $\gamma$, $\abs{a/z} = \abs a/r<1$, so $\frac1{z-a} = \sum_{k\ge 0}a^kz^{-(k+1)}$ uniformly on $\gamma$. Integrating term by term, step [](#part-a){.pf-ref} gives $2\pi i$ for $k=0$ and $0$ for $k\geq 1$.
:::

:::

::: {.pf-step #outer}
$\displaystyle\int_\gamma\frac{dz}{z-b} = 0$.

::: pf-proof
On $\gamma$, $\abs{z/b} = r/\abs b<1$, so $\frac1{z-b} = -\sum_{k\ge 0}z^k/b^{k+1}$ uniformly on $\gamma$. Integrating term by term, step [](#part-a){.pf-ref} gives $0$ for every $k\geq 0$.
:::

:::

::: pf-step
(c) $\displaystyle\int_\gamma\frac{dz}{(z-a)(z-b)} = \frac{2\pi i}{a-b}$.

::: pf-proof
By step [](#partial-fractions){.pf-ref} and linearity, the integral equals $\frac{1}{a-b}$ times the difference of the integrals in steps [](#inner){.pf-ref} and [](#outer){.pf-ref}, that is, $\frac{2\pi i - 0}{a-b}$.
:::

:::

:::

:::
