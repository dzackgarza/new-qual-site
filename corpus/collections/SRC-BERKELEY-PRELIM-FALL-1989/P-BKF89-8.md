---
schema: qual/card@1
id: P-BKF89-8
kind: problem
title: The integral $\int_0^\infty \log x/(1+x^2)\,dx$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Evaluate
\[
\int_0^\infty\frac{\log x}{1+x^2}\,dx.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The improper integral converges absolutely.

::: pf-proof

On $(0,1]$,
$$
\frac{|\log x|}{1+x^2}
\leq
|\log x|,
$$
and
$$
\int_0^1|\log x|\,dx=1.
$$
On $[1,\infty)$,
$$
\frac{\log x}{1+x^2}
\leq
\frac{\log x}{x^2},
$$
whose integral converges by integration by parts. Hence the original integral is absolutely convergent.

:::

:::

::: {.pf-step #s2}

One has
$$
\int_1^\infty\frac{\log x}{1+x^2}\,dx
=
-\int_0^1\frac{\log t}{1+t^2}\,dt.
$$

::: pf-proof

Use the substitution
$$
x=\frac1t,
\qquad
dx=-\frac{dt}{t^2}.
$$
Then
$$
\begin{aligned}
\int_1^\infty\frac{\log x}{1+x^2}\,dx
&=
\int_1^0
\frac{-\log t}{1+t^{-2}}
\left(-\frac{dt}{t^2}\right)\\
&=
\int_1^0\frac{\log t}{1+t^2}\,dt\\
&=
-\int_0^1\frac{\log t}{1+t^2}\,dt.
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

Therefore
$$
\boxed{
\int_0^\infty\frac{\log x}{1+x^2}\,dx=0.
}
$$

::: pf-proof

By absolute convergence from step [](#s1){.pf-ref}, split at $1$:
$$
\int_0^\infty
=
\int_0^1+\int_1^\infty.
$$
Step [](#s2){.pf-ref} shows that the two contributions cancel.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the requested value.

:::

:::

:::
