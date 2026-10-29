---
schema: qual/card@1
id: P-BKF77-9
kind: problem
title: Supremum bound from the $L^2$ norm of the derivative
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Applied the fundamental theorem of calculus and Cauchy--Schwarz on [0,x], then used x<=1."
---

::: {.problem}
Let $f:[0,1]\to\RR$ be continuously differentiable with $f(0)=0$. Prove that
\[
\sup_{0\le x\le1}|f(x)|\le\sqrt{\int_0^1(f'(x))^2\,dx}.
\]
:::

::: {.solution}
::: pf

::: {.pf-step #fundamental-theorem}
For every $x\in[0,1]$,
$$
f(x)=\int_0^x f'(t)\,dt.
$$

::: pf-proof
The function $f$ is continuously differentiable and $f(0)=0$, so the
fundamental theorem of calculus gives
$$
f(x)-f(0)=\int_0^x f'(t)\,dt.
$$
:::

:::

::: {.pf-step #cauchy-schwarz-bound}
For every $x\in[0,1]$,
$$
|f(x)|
\le
\sqrt{x}
\left(\int_0^x(f'(t))^2\,dt\right)^{1/2}.
$$

::: pf-proof
By [](#fundamental-theorem){.pf-ref} and Cauchy--Schwarz,
$$
\begin{aligned}
|f(x)|
&=\left|\int_0^x f'(t)\,dt\right|\\
&\le
\left(\int_0^x1^2\,dt\right)^{1/2}
\left(\int_0^x(f'(t))^2\,dt\right)^{1/2}\\
&=
\sqrt{x}
\left(\int_0^x(f'(t))^2\,dt\right)^{1/2}.
\end{aligned}
$$
:::

:::

::: {.pf-step #uniform-bound}
For every $x\in[0,1]$,
$$
|f(x)|
\le
\left(\int_0^1(f'(t))^2\,dt\right)^{1/2}.
$$

::: pf-proof
Since $0\le x\le1$, one has $\sqrt{x}\le1$. Also
$(f'(t))^2\ge0$, so
$$
\int_0^x(f'(t))^2\,dt
\le
\int_0^1(f'(t))^2\,dt.
$$
Substitute these two bounds into [](#cauchy-schwarz-bound){.pf-ref}.
:::

:::

::: pf-step
Therefore
$$
\boxed{
\sup_{0\le x\le1}|f(x)|
\le
\sqrt{\int_0^1(f'(x))^2\,dx}}.
$$

::: pf-proof
The right-hand side in [](#uniform-bound){.pf-ref} is independent of $x$. Taking the
supremum over all $x\in[0,1]$ gives the displayed inequality.
:::

:::

:::

:::
