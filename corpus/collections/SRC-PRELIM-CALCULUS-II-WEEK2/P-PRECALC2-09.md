---
schema: qual/card@1
id: P-PRECALC2-09
kind: problem
title: Integral of $\frac{\log t}{1+t^2}$ over $(0,\infty)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Compute $\displaystyle \int_{0}^{\infty} \frac{\log(t)}{1 + t^{2}}\, dt$.
:::

::: {.solution}

Let
$$
I
=
\int_0^\infty
\frac{\log t}{1+t^2}\,dt.
$$

::: pf

::: {.pf-step #s1-1}

The improper integral is absolutely convergent.


::: pf-proof

On $(0,1]$,
$$
0<
\frac1{1+t^2}
\le1,
$$
so
$$
\int_0^1
\frac{\abs{\log t}}{1+t^2}\,dt
\le
\int_0^1\abs{\log t}\,dt
=
1.
$$

For $t\ge1$,
$$
\frac{\log t}{1+t^2}
\le
\frac{\log t}{t^2}.
$$
Integration by parts gives
$$
\int_1^\infty\frac{\log t}{t^2}\,dt<\infty.
$$
Thus the original integral converges absolutely.

:::

:::

::: {.pf-step #s1-2}

Split the integral at $1$:
$$
I
=
\int_0^1
\frac{\log t}{1+t^2}\,dt
+
\int_1^\infty
\frac{\log t}{1+t^2}\,dt.
$$


::: pf-proof

Absolute convergence from step [](#s1-1){.pf-ref} justifies splitting the improper
integral.

:::

:::

::: pf-step

In the second integral, set
$$
\boxed{t=\frac1u}.
$$


::: pf-proof

This substitution exchanges the intervals
$$
[1,\infty)
\qquad\text{and}\qquad
(0,1].
$$

:::

:::

::: {.pf-step #s1-4}

Then
$$
dt=-\frac{du}{u^2}
$$
and
$$
1+t^2
=
1+\frac1{u^2}
=
\frac{1+u^2}{u^2}.
$$


::: pf-proof

Differentiate
$$
t=u^{-1}
$$
and simplify the denominator.

:::

:::

::: {.pf-step #s1-5}

Also,
$$
\log t
=
\log\frac1u
=
-\log u.
$$


::: pf-proof

Use
$$
\log(u^{-1})=-\log u
$$
for $u>0$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\int_1^\infty
\frac{\log t}{1+t^2}\,dt
=
-\int_0^1
\frac{\log u}{1+u^2}\,du.
$$


::: pf-proof

Using steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref},
$$
\begin{aligned}
\int_1^\infty
\frac{\log t}{1+t^2}\,dt
&=
\int_1^0
\frac{-\log u}{(1+u^2)/u^2}
\left(-\frac{du}{u^2}\right)\\
&=
\int_1^0
\frac{\log u}{1+u^2}\,du\\
&=
-\int_0^1
\frac{\log u}{1+u^2}\,du.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-7}

Hence the two pieces cancel:
$$
\begin{aligned}
I
&=
\int_0^1
\frac{\log t}{1+t^2}\,dt
-
\int_0^1
\frac{\log t}{1+t^2}\,dt\\
&=
0.
\end{aligned}
$$


::: pf-proof

Substitute step [](#s1-6){.pf-ref} into step [](#s1-2){.pf-ref} and rename the dummy variable $u$ as
$t$.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\int_0^\infty
\frac{\log t}{1+t^2}\,dt
=
0}.
$$


::: pf-proof

This is step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the requested value.

:::

:::

:::
