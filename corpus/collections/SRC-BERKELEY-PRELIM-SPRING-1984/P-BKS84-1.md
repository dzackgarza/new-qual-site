---
schema: qual/card@1
id: P-BKS84-1
kind: problem
title: The integral $\int_0^\infty \log x/(a^2+x^2)\,dx$
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
    The substitution x=at separates the integral into
    (log a)/a times the arctangent integral and 1/a times
    J=integral_0^infinity log(t)/(1+t^2) dt. Splitting J at 1 and
    substituting t=1/u in its second half shows the two halves cancel,
    so the value is pi log(a)/(2a).
---

::: {.problem}
Let $a>0$. Evaluate
\[
\int_0^\infty\frac{\log x}{a^2+x^2}\,dx.
\]
:::

::: {.solution}
<1>1. The improper integral converges absolutely.

::: {.proof}
On $(0,1]$,
$$
\frac{\abs{\log x}}{a^2+x^2}
\leq
\frac{\abs{\log x}}{a^2},
$$
and
$$
\int_0^1\abs{\log x}\,dx=1.
$$
On $[1,\infty)$,
$$
\frac{\log x}{a^2+x^2}
\leq
\frac{\log x}{x^2},
$$
and integration by parts gives
$$
\int_1^\infty\frac{\log x}{x^2}\,dx=1.
$$
Hence the given integral is absolutely convergent.
:::

<1>2. With
$$
J=\int_0^\infty\frac{\log t}{1+t^2}\,dt,
$$
one has
$$
\int_0^\infty\frac{\log x}{a^2+x^2}\,dx
=
\frac{\pi\log a}{2a}
+
\frac{J}{a}.
$$

::: {.proof}
Set $x=at$. Since $a>0$,
$$
dx=a\,dt
$$
and
$$
a^2+x^2=a^2(1+t^2).
$$
Thus
$$
\begin{aligned}
\int_0^\infty\frac{\log x}{a^2+x^2}\,dx
&=
\frac1a
\int_0^\infty
\frac{\log a+\log t}{1+t^2}\,dt\\
&=
\frac{\log a}{a}
\int_0^\infty\frac{dt}{1+t^2}
+
\frac{J}{a}.
\end{aligned}
$$
Since
$$
\int_0^\infty\frac{dt}{1+t^2}
=
\left[\arctan t\right]_0^\infty
=
\frac\pi2,
$$
the claimed formula follows.
:::

<1>3. One has
$$
J=0.
$$

::: {.proof}
Split
$$
J
=
\int_0^1\frac{\log t}{1+t^2}\,dt
+
\int_1^\infty\frac{\log t}{1+t^2}\,dt.
$$
In the second integral, set $t=1/u$. Then
$$
dt=-\frac{du}{u^2},
$$
and therefore
$$
\int_1^\infty\frac{\log t}{1+t^2}\,dt
=
-\int_0^1\frac{\log u}{1+u^2}\,du.
$$
This cancels the first integral, so $J=0$.
:::

<1>4. Therefore
$$
\boxed{
\int_0^\infty\frac{\log x}{a^2+x^2}\,dx
=
\frac{\pi\log a}{2a}
}.
$$

::: {.proof}
Substitute step <1>3 into the formula of step <1>2.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value.
:::
:::
