---
schema: qual/card@1
id: P-BKF94-3
kind: problem
title: The integral $\int_{-\pi}^{\pi}\frac{\sin n\theta}{\sin\theta}\,d\theta$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Expanded the sine quotient as a finite sum of integer Fourier modes; only
    the zero mode survives integration, and it occurs exactly for odd n.
---

::: {.problem}
Evaluate
\[
\int_{-\pi}^{\pi}\frac{\sin(n\theta)}{\sin\theta}\,d\theta,
\qquad n=1,2,\dots.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $\theta\notin\pi\ZZ$,
$$
\frac{\sin(n\theta)}{\sin\theta}
=
\sum_{j=0}^{n-1}
e^{i(2j-n+1)\theta}.
$$

::: pf-proof

Using the exponential formula for sine,
$$
\begin{aligned}
\frac{\sin(n\theta)}{\sin\theta}
&=
\frac{e^{in\theta}-e^{-in\theta}}
{e^{i\theta}-e^{-i\theta}}\\
&=
e^{-i(n-1)\theta}
\frac{e^{2in\theta}-1}{e^{2i\theta}-1}\\
&=
e^{-i(n-1)\theta}
\sum_{j=0}^{n-1}e^{2ij\theta}\\
&=
\sum_{j=0}^{n-1}e^{i(2j-n+1)\theta}.
\end{aligned}
$$
The singularities of the original quotient at integer multiples of $\pi$
are removable, so this identity determines the same integral over
$[-\pi,\pi]$.

:::

:::

::: {.pf-step #s2}

For every integer $k$,
$$
\int_{-\pi}^{\pi}e^{ik\theta}\,d\theta
=
\begin{cases}
2\pi,&k=0,\\
0,&k\neq0.
\end{cases}
$$

::: pf-proof

For $k=0$ the integrand is $1$. For $k\neq0$,
$$
\int_{-\pi}^{\pi}e^{ik\theta}\,d\theta
=
\left[
\frac{e^{ik\theta}}{ik}
\right]_{-\pi}^{\pi}
=
\frac{e^{ik\pi}-e^{-ik\pi}}{ik}
=0,
$$
because $k$ is an integer.

:::

:::

::: {.pf-step #s3}

The exponent
$$
2j-n+1
$$
vanishes for an integer $j$ with $0\leq j\leq n-1$ if and only if $n$ is
odd.

::: pf-proof

The equation
$$
2j-n+1=0
$$
has the unique solution
$$
j=\frac{n-1}{2}.
$$
This is an integer exactly when $n$ is odd.

:::

:::

::: {.pf-step #s4}

One has
$$
\boxed{
\int_{-\pi}^{\pi}
\frac{\sin(n\theta)}{\sin\theta}\,d\theta
=
\begin{cases}
2\pi,&n\text{ odd},\\
0,&n\text{ even}.
\end{cases}
}
$$

::: pf-proof

Integrate the finite sum in step [](#s1){.pf-ref} term by term. By step [](#s2){.pf-ref}, every
nonzero Fourier mode contributes $0$. By step [](#s3){.pf-ref}, exactly one zero mode is
present when $n$ is odd and none is present when $n$ is even. The zero mode
contributes $2\pi$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested value for every positive integer $n$.

:::

:::

:::
