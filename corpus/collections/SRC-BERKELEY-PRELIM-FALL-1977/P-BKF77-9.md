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
Let $f:[0,1]\to\mathbb R$ be continuously differentiable with $f(0)=0$. Prove that
\[
\sup_{0\le x\le1}|f(x)|\le\sqrt{\int_0^1(f'(x))^2\,dx}.
\]
:::

::: {.solution}
Fix $x\in[0,1]$. Since $f(0)=0$, the fundamental theorem of calculus gives
$$
f(x)=\int_0^x f'(t)\,dt.
$$
By Cauchy--Schwarz,
$$
\begin{aligned}
|f(x)|
&\le \int_0^x |f'(t)|\,dt\\
&\le \left(\int_0^x1^2\,dt\right)^{1/2}
     \left(\int_0^x(f'(t))^2\,dt\right)^{1/2}\\
&=\sqrt{x}\left(\int_0^x(f'(t))^2\,dt\right)^{1/2}.
\end{aligned}
$$
Because $0\le x\le1$,
$$
\sqrt{x}\le1
$$
and
$$
\int_0^x(f'(t))^2\,dt
\le
\int_0^1(f'(t))^2\,dt.
$$
Hence for every $x\in[0,1]$,
$$
|f(x)|
\le
\left(\int_0^1(f'(t))^2\,dt\right)^{1/2}.
$$
Taking the supremum over $x$ yields
$$
\boxed{
\sup_{0\le x\le1}|f(x)|
\le
\sqrt{\int_0^1(f'(x))^2\,dx}.}
$$
:::
