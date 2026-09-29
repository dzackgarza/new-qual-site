---
schema: qual/card@1
id: P-BERK79S-15
kind: problem
title: Convergence of $\sum_n z/(1+z^2)^n$ outside the lemniscate $\abs{1+z^2}=1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Outside the lemniscate means |1+z^2|>1. Factoring out z leaves a
    geometric series with ratio 1/(1+z^2), whose modulus is then strictly
    less than one. Hence the series converges absolutely; summing the
    geometric series gives (1+z^2)/z, with z≠0 automatically outside the
    lemniscate.
---

::: {.problem}
Show that
\[
\sum_{n=0}^{\infty}\frac{z}{(1+z^2)^n}
\]
converges for every complex number $z$ exterior to the lemniscate
\[
|1+z^2|=1.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $z$ is exterior to the lemniscate, then
$$
\abs{1+z^2}>1.
$$

::: pf-proof

The lemniscate is the level set
$$
\abs{1+z^2}=1.
$$
Its exterior is the region where the defining modulus is greater than
$1$.

:::

:::

::: {.pf-step #s2}

For such a point $z$,
$$
\abs{
\frac1{1+z^2}
}
<
1.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
\abs{1+z^2}>1.
$$
Taking reciprocals of positive real numbers gives
$$
\frac1{\abs{1+z^2}}<1.
$$
Since
$$
\abs{
\frac1{1+z^2}
}
=
\frac1{\abs{1+z^2}},
$$
the result follows.

:::

:::

::: {.pf-step #s3}

The series can be written as
$$
z
\sum_{n=0}^{\infty}
\left(
\frac1{1+z^2}
\right)^n.
$$

::: pf-proof

For each $n$,
$$
\frac{z}{(1+z^2)^n}
=
z
\left(
\frac1{1+z^2}
\right)^n.
$$
Factoring the constant $z$ from the sum gives the displayed expression.

:::

:::

::: {.pf-step #s4}

The series converges absolutely for every point exterior to the
lemniscate.

::: pf-proof

By step [](#s2){.pf-ref}, the ratio
$$
q=\frac1{1+z^2}
$$
satisfies
$$
\abs q<1.
$$
Therefore the geometric series
$$
\sum_{n=0}^{\infty}q^n
$$
converges absolutely. Multiplication by the fixed complex number $z$
preserves absolute convergence. Hence
$$
\boxed{
\sum_{n=0}^{\infty}
\frac{z}{(1+z^2)^n}
\text{ converges absolutely.}
}
$$

:::

:::

::: pf-step

In fact, at every such point,
$$
\sum_{n=0}^{\infty}
\frac{z}{(1+z^2)^n}
=
\frac{1+z^2}{z}.
$$

::: pf-proof

The exterior region does not contain $z=0$, because
$$
\abs{1+0^2}=1.
$$
Thus division by $z$ is valid. Using the geometric-series sum and step
[](#s3){.pf-ref},
$$
\begin{aligned}
z
\sum_{n=0}^{\infty}
\left(
\frac1{1+z^2}
\right)^n
&=
z
\frac1{
1-\frac1{1+z^2}
}\\
&=
z
\frac{1+z^2}{z^2}\\
&=
\frac{1+z^2}{z}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the required convergence.

:::

:::

:::
