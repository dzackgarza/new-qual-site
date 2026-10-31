---
schema: qual/card@1
id: P-PRECALC1-28
kind: problem
title: Riemann sum limit for $\int_0^3(x^2-x)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Riemann Sums
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in the limit of Problem 28 on page 6 of Week1_solns.pdf.
---

::: {.problem}
Calculate $\displaystyle\lim_{n \to \infty} \frac{3}{n} \sum_{i=1}^{n} \left[ \left(\frac{3i}{n}\right)^2 - \left(\frac{3i}{n}\right) \right]$.
:::

::: {.solution}

Let
$$
f(x)=x^2-x
$$
on $[0,3]$.

::: pf

::: {.pf-step #s1-1}

Partition $[0,3]$ into $n$ equal subintervals. Then
$$
\boxed{
\Delta x=\frac3n}.
$$


::: pf-proof

The interval length is $3-0=3$, so dividing by $n$ gives the common
width $3/n$.

:::

:::

::: {.pf-step #s1-2}

The right endpoint of the $i$th subinterval is
$$
\boxed{
x_i=\frac{3i}{n}}.
$$


::: pf-proof

Starting at $0$, the $i$th right endpoint is
$$
0+i\Delta x
=
\frac{3i}{n}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the given expression is
$$
\boxed{
\sum_{i=1}^{n}
f(x_i)\,\Delta x}.
$$


::: pf-proof

Using steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
f(x_i)
=
\left(\frac{3i}{n}\right)^2
-
\left(\frac{3i}{n}\right),
$$
so
$$
\sum_{i=1}^{n}
f(x_i)\Delta x
=
\frac3n
\sum_{i=1}^{n}
\left[
\left(\frac{3i}{n}\right)^2
-
\left(\frac{3i}{n}\right)
\right].
$$

:::

:::

::: {.pf-step #s1-4}

Hence, as $n\to\infty$, the expression converges to
$$
\int_0^3(x^2-x)\,dx.
$$


::: pf-proof

The function $f$ is continuous on $[0,3]$, so its right-endpoint Riemann
sums converge to its definite integral.

:::

:::

::: {.pf-step #s1-5}

An antiderivative is
$$
\boxed{
\frac{x^3}{3}-\frac{x^2}{2}}.
$$


::: pf-proof

Differentiate:
$$
\frac{d}{dx}
\left(
\frac{x^3}{3}-\frac{x^2}{2}
\right)
=
x^2-x.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\begin{aligned}
\int_0^3(x^2-x)\,dx
&=
\left[
\frac{x^3}{3}-\frac{x^2}{2}
\right]_0^3\\
&=
9-\frac92.
\end{aligned}
$$


::: pf-proof

Substitute the endpoints.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
\int_0^3(x^2-x)\,dx
=
\frac92}.
$$


::: pf-proof

$$
9-\frac92
=
\frac{18}{2}-\frac92
=
\frac92.
$$

:::

:::

::: {.pf-step #s1-8}

Consequently,
$$
\boxed{
\lim_{n\to\infty}
\frac3n
\sum_{i=1}^{n}
\left[
\left(\frac{3i}{n}\right)^2
-
\left(\frac{3i}{n}\right)
\right]
=
\frac92}.
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the requested limit.

:::

:::

:::
