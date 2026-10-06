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
Compute $\int _ { 0 } ^ { \infty } \frac { \log ( t ) } { 1 + t ^ { 2 } } d t .$
:::

::: {.solution}
Let
\[
I
=
\int_0^\infty
\frac{\log t}{1+t^2}\,dt.
\]

<1>1. The improper integral is absolutely convergent.

::: {.proof}
On \((0,1]\),
\[
0<
\frac1{1+t^2}
\le1,
\]
so
\[
\int_0^1
\frac{|\log t|}{1+t^2}\,dt
\le
\int_0^1|\log t|\,dt
=
1.
\]

For \(t\ge1\),
\[
\frac{\log t}{1+t^2}
\le
\frac{\log t}{t^2}.
\]
Integration by parts gives
\[
\int_1^\infty\frac{\log t}{t^2}\,dt<\infty.
\]
Thus the original integral converges absolutely.
:::

<1>2. Split the integral at \(1\):
\[
I
=
\int_0^1
\frac{\log t}{1+t^2}\,dt
+
\int_1^\infty
\frac{\log t}{1+t^2}\,dt.
\]

::: {.proof}
Absolute convergence from step <1>1 justifies splitting the improper
integral.
:::

<1>3. In the second integral, set
\[
\boxed{t=\frac1u}.
\]

::: {.proof}
This substitution exchanges the intervals
\[
[1,\infty)
\qquad\text{and}\qquad
(0,1].
\]
:::

<1>4. Then
\[
dt=-\frac{du}{u^2}
\]
and
\[
1+t^2
=
1+\frac1{u^2}
=
\frac{1+u^2}{u^2}.
\]

::: {.proof}
Differentiate
\[
t=u^{-1}
\]
and simplify the denominator.
:::

<1>5. Also,
\[
\log t
=
\log\frac1u
=
-\log u.
\]

::: {.proof}
Use
\[
\log(u^{-1})=-\log u
\]
for \(u>0\).
:::

<1>6. Therefore
\[
\int_1^\infty
\frac{\log t}{1+t^2}\,dt
=
-\int_0^1
\frac{\log u}{1+u^2}\,du.
\]

::: {.proof}
Using steps <1>4--<1>5,
\[
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
\]
:::

<1>7. Hence the two pieces cancel:
\[
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
\]

::: {.proof}
Substitute step <1>6 into step <1>2 and rename the dummy variable \(u\) as
\(t\).
:::

<1>8. Therefore
\[
\boxed{
\int_0^\infty
\frac{\log t}{1+t^2}\,dt
=
0}.
\]

::: {.proof}
This is step <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the requested value.
:::
:::
