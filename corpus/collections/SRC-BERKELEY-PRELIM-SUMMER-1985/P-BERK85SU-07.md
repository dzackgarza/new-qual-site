---
schema: qual/card@1
id: P-BERK85SU-07
kind: problem
title: Monotonicity and a reciprocal bound for a Gaussian-tail ratio
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Positivity is immediate. Since t/x>1 for t>x,
    integral_x^infty e^{-t^2/2}dt < x^{-1} integral_x^infty
    t e^{-t^2/2}dt = x^{-1}e^{-x^2/2}, giving f(x)<1/x.
    Differentiation yields f'(x)=xf(x)-1<0.
---

::: {.problem}
For $x>0$, let
\[
f(x)=e^{x^2/2}\int_x^\infty e^{-t^2/2}\,dt.
\]

1. Prove that
\[
0<f(x)<\frac1x.
\]
2. Prove that $f$ is strictly decreasing on $(0,\infty)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $x>0$,
$$
f(x)>0.
$$

::: pf-proof

The integrand $e^{-t^2/2}$ is positive for every real $t$, so
$$
\int_x^\infty e^{-t^2/2}\,dt>0.
$$
Multiplication by the positive factor $e^{x^2/2}$ preserves
positivity.

:::

:::

::: {.pf-step #s2}

For every $x>0$,
$$
f(x)<\frac1x.
$$

::: pf-proof

For $t>x>0$ one has $t/x>1$. Hence
$$
\begin{aligned}
\int_x^\infty e^{-t^2/2}\,dt
&<
\frac1x
\int_x^\infty t e^{-t^2/2}\,dt\\
&=
\frac1x e^{-x^2/2}.
\end{aligned}
$$
Multiplying by $e^{x^2/2}$ gives
$$
f(x)<\frac1x.
$$

:::

:::

::: {.pf-step #s3}

Part 1 is
$$
\boxed{0<f(x)<\frac1x}.
$$

::: pf-proof

Combine steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The derivative of $f$ is
$$
f'(x)=xf(x)-1.
$$

::: pf-proof

Differentiate
$$
f(x)=e^{x^2/2}\int_x^\infty e^{-t^2/2}\,dt.
$$
By the product rule and the fundamental theorem of calculus,
$$
\begin{aligned}
f'(x)
&=
xe^{x^2/2}
\int_x^\infty e^{-t^2/2}\,dt
-e^{x^2/2}e^{-x^2/2}\\
&=
xf(x)-1.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

The function $f$ is strictly decreasing on $(0,\infty)$.

::: pf-proof

Step [](#s2){.pf-ref} gives $xf(x)<1$ for every $x>0$. Hence step [](#s4){.pf-ref} gives
$$
f'(x)=xf(x)-1<0.
$$
Therefore $f$ is strictly decreasing.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part 1, and step [](#s5){.pf-ref} proves part 2.

:::

:::

:::
