---
schema: qual/card@1
id: P-UCLARA16S-07
kind: problem
title: Evaluation of $\int_0^\infty\frac{x^{a-1}}{x+z}\,dx$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Determine
$$
\int_0^\infty\frac{x^{a-1}}{x+z}\,dx
$$
for $0<a<1$ and $\operatorname{Re}z>0$. Justify all manipulations.
:::

::: {.solution}

On the right half-plane, use the principal branch
$$
z^{a-1}
\coloneqq
\exp\bigl((a-1)\Log z\bigr).
$$

::: pf

::: {.pf-step #s1-1}

For $x>0$ and $\operatorname{Re}z>0$,
$$
\frac1{x+z}
=
\int_0^\infty e^{-(x+z)t}\,dt.
$$


::: pf-proof

Since
$$
\operatorname{Re}(x+z)=x+\operatorname{Re}z>0,
$$
the exponential tends to $0$ as $t\to\infty$, and direct integration gives
$$
\int_0^\infty e^{-(x+z)t}\,dt
=
\left[
-\frac{e^{-(x+z)t}}{x+z}
\right]_{t=0}^{t=\infty}
=
\frac1{x+z}.
$$

:::

:::

::: {.pf-step #s1-2}

The function
$$
(x,t)
\longmapsto
x^{a-1}e^{-(x+z)t}
$$
is absolutely integrable on $(0,\infty)^2$.


::: pf-proof

Writing $\sigma=\operatorname{Re}z>0$ and using Tonelli's theorem for the nonnegative absolute value,
$$
\begin{aligned}
\int_0^\infty\int_0^\infty
x^{a-1}e^{-xt}e^{-\sigma t}\,dx\,dt
&=
\int_0^\infty
e^{-\sigma t}
\left(
\int_0^\infty x^{a-1}e^{-tx}\,dx
\right)dt\\
&=
\Gamma(a)
\int_0^\infty
t^{-a}e^{-\sigma t}\,dt\\
&=
\Gamma(a)\Gamma(1-a)\sigma^{a-1}.
\end{aligned}
$$
The last quantity is finite because $0<a<1$ and $\sigma>0$.

:::

:::

::: {.pf-step #s1-3}

For $\operatorname{Re}z>0$,
$$
\int_0^\infty
t^{-a}e^{-zt}\,dt
=
\Gamma(1-a)z^{a-1}.
$$


::: pf-proof

Define
$$
H(z)
\coloneqq
\int_0^\infty t^{-a}e^{-zt}\,dt
\qquad
(\operatorname{Re}z>0).
$$
On every compact subset of the right half-plane there is a number $\sigma_0>0$ such that $\operatorname{Re}z\ge\sigma_0$. The integrand and its $z$-derivative are then dominated respectively by
$$
t^{-a}e^{-\sigma_0t}
\qquad\text{and}\qquad
t^{1-a}e^{-\sigma_0t},
$$
both integrable on $(0,\infty)$. Differentiation under the integral sign therefore shows that $H$ is holomorphic on the right half-plane.

For positive real $z$, the change of variables $s=zt$ gives
$$
H(z)
=
z^{a-1}
\int_0^\infty s^{-a}e^{-s}\,ds
=
\Gamma(1-a)z^{a-1}.
$$
Both sides are holomorphic on the connected right half-plane and agree on the positive real axis, which has accumulation points in that domain. The identity theorem gives the formula for every $\operatorname{Re}z>0$.

:::

:::

::: {.pf-step #s1-4}

The integral equals
$$
\boxed{
\int_0^\infty\frac{x^{a-1}}{x+z}\,dx
=
\frac{\pi z^{a-1}}{\sin(\pi a)}
}.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, Fubini's theorem applies:
$$
\begin{aligned}
\int_0^\infty\frac{x^{a-1}}{x+z}\,dx
&=
\int_0^\infty\int_0^\infty
x^{a-1}e^{-(x+z)t}\,dt\,dx\\
&=
\int_0^\infty
e^{-zt}
\left(
\int_0^\infty x^{a-1}e^{-tx}\,dx
\right)dt\\
&=
\Gamma(a)
\int_0^\infty t^{-a}e^{-zt}\,dt.
\end{aligned}
$$
Step [](#s1-3){.pf-ref} gives
$$
\Gamma(a)\Gamma(1-a)z^{a-1}.
$$
Euler's reflection formula
$$
\Gamma(a)\Gamma(1-a)
=
\frac{\pi}{\sin(\pi a)}
$$
then yields the boxed expression.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value, while steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} justify the integral representation, interchange of integrals, and complex Gamma integral used to obtain it.

:::

:::

:::
