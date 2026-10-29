---
schema: qual/card@1
id: P-UMNCP-F12-03
kind: problem
title: The integral $\int_0^\infty \frac{\log x}{x^2+\alpha^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Fall 2012, 3 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
For $\alpha>0$, evaluate
$$
\int_0^\infty \frac{\log x}{x^2+\alpha^2}\,dx,
$$
carefully justifying all steps.
:::

::: {.solution}

Set
$$
I(\alpha)
\coloneqq
\int_0^\infty
\frac{\log x}{x^2+\alpha^2}
\,dx,
\qquad
\alpha>0.
$$

::: pf

::: {.pf-step #s1-1}

The integral defining $I(\alpha)$ converges absolutely.


::: pf-proof

Near $0$,
$$
\frac{|\log x|}{x^2+\alpha^2}
\le
\frac1{\alpha^2}|\log x|,
$$
and
$$
\int_0^1|\log x|\,dx<\infty.
$$

For $x\ge1$,
$$
\frac{|\log x|}{x^2+\alpha^2}
\le
\frac{\log x}{x^2},
$$
and
$$
\int_1^\infty\frac{\log x}{x^2}\,dx<\infty.
$$
Thus the improper integral is absolutely convergent.

:::

:::

::: {.pf-step #s1-2}

The substitution
$$
x=\alpha t
$$
gives
$$
I(\alpha)
=
\frac1\alpha
\int_0^\infty
\frac{\log\alpha+\log t}
{1+t^2}
\,dt.
$$


::: pf-proof

Since
$$
x=\alpha t,
\qquad
dx=\alpha\,dt,
$$
and
$$
x^2+\alpha^2
=
\alpha^2(1+t^2),
$$
we obtain
$$
\begin{aligned}
I(\alpha)
&=
\int_0^\infty
\frac{\log(\alpha t)}
{\alpha^2(1+t^2)}
\alpha\,dt\\
&=
\frac1\alpha
\int_0^\infty
\frac{\log\alpha+\log t}
{1+t^2}
\,dt.
\end{aligned}
$$
Absolute convergence from step [](#s1-1){.pf-ref} justifies the substitution and separation of terms.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{
\int_0^\infty
\frac{\log t}{1+t^2}
\,dt
=0}.
$$


::: pf-proof

Let
$$
J
\coloneqq
\int_0^\infty
\frac{\log t}{1+t^2}
\,dt.
$$
This integral is absolutely convergent by the same endpoint estimates as in step [](#s1-1){.pf-ref}.

Make the substitution
$$
t=\frac1u,
\qquad
dt=-\frac1{u^2}\,du.
$$
Then
$$
\begin{aligned}
J
&=
\int_\infty^0
\frac{\log(1/u)}
{1+u^{-2}}
\left(
-\frac1{u^2}
\right)
du\\
&=
\int_0^\infty
\frac{-\log u}{1+u^2}
\,du\\
&=
-J.
\end{aligned}
$$
Hence
$$
2J=0,
$$
so $J=0$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\int_0^\infty
\frac{dt}{1+t^2}
=
\frac\pi2.
$$


::: pf-proof

The antiderivative is
$$
\arctan t.
$$
Therefore
$$
\int_0^\infty
\frac{dt}{1+t^2}
=
\lim_{R\to\infty}
\left(
\arctan R-\arctan0
\right)
=
\frac\pi2.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
I(\alpha)
=
\frac{\pi}{2\alpha}\log\alpha}.
$$


::: pf-proof

Split the integral in step [](#s1-2){.pf-ref}:
$$
I(\alpha)
=
\frac{\log\alpha}{\alpha}
\int_0^\infty
\frac{dt}{1+t^2}
+
\frac1\alpha
\int_0^\infty
\frac{\log t}{1+t^2}
\,dt.
$$
Now apply steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required evaluation.

:::

:::

:::
