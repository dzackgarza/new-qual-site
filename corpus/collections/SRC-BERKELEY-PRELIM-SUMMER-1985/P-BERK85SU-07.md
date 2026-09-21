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
<1>1. For every $x>0$,
$$
f(x)>0.
$$

::: {.proof}
The integrand $e^{-t^2/2}$ is positive for every real $t$, so
$$
\int_x^\infty e^{-t^2/2}\,dt>0.
$$
Multiplication by the positive factor $e^{x^2/2}$ preserves
positivity.
:::

<1>2. For every $x>0$,
$$
f(x)<\frac1x.
$$

::: {.proof}
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

<1>3. Part 1 is
$$
\boxed{0<f(x)<\frac1x}.
$$

::: {.proof}
Combine steps <1>1 and <1>2.
:::

<1>4. The derivative of $f$ is
$$
f'(x)=xf(x)-1.
$$

::: {.proof}
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

<1>5. The function $f$ is strictly decreasing on $(0,\infty)$.

::: {.proof}
Step <1>2 gives $xf(x)<1$ for every $x>0$. Hence step <1>4 gives
$$
f'(x)=xf(x)-1<0.
$$
Therefore $f$ is strictly decreasing.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>3 proves part 1, and step <1>5 proves part 2.
:::
:::
