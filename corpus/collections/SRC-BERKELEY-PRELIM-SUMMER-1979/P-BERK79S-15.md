---
schema: qual/card@1
id: P-BERK79S-15
kind: problem
title: Convergence outside the lemniscate of a geometric rational series
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
<1>1. If $z$ is exterior to the lemniscate, then
$$
\abs{1+z^2}>1.
$$

::: {.proof}
The lemniscate is the level set
$$
\abs{1+z^2}=1.
$$
Its exterior is the region where the defining modulus is greater than
$1$.
:::

<1>2. For such a point $z$,
$$
\abs{
\frac1{1+z^2}
}
<
1.
$$

::: {.proof}
By step <1>1,
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

<1>3. The series can be written as
$$
z
\sum_{n=0}^{\infty}
\left(
\frac1{1+z^2}
\right)^n.
$$

::: {.proof}
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

<1>4. The series converges absolutely for every point exterior to the
lemniscate.

::: {.proof}
By step <1>2, the ratio
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

<1>5. In fact, at every such point,
$$
\sum_{n=0}^{\infty}
\frac{z}{(1+z^2)^n}
=
\frac{1+z^2}{z}.
$$

::: {.proof}
The exterior region does not contain $z=0$, because
$$
\abs{1+0^2}=1.
$$
Thus division by $z$ is valid. Using the geometric-series sum and step
<1>3,
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

<1>6. Q.E.D.

::: {.proof}
Step <1>4 proves the required convergence.
:::
:::
