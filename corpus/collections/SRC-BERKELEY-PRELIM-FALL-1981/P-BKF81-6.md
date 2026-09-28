---
schema: qual/card@1
id: P-BKF81-6
kind: problem
title: Averaging a periodic function against rapid oscillations
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
  note: "Partitioned [0,1] into n cells, used periodicity after rescaling each cell, and proved the resulting shifted Riemann sums converge uniformly in the shift."
---

::: {.problem}
Let $f,g$ be continuous $1$-periodic functions on $\mathbb R$. Prove that
\[
\lim_{n\to\infty}\int_0^1 f(x)g(nx)\,dx
=\left(\int_0^1f\right)\left(\int_0^1g\right).
\]
:::

::: {.solution}
Partition $[0,1]$ into the intervals
$$
\left[\frac jn,\frac{j+1}{n}\right],
\qquad j=0,\ldots,n-1.
$$

<1>1. Rewrite the integral using periodicity of $g$.
::: {.proof}
On the $j$th interval set
$$
x=\frac{j+t}{n},
\qquad 0\le t\le1.
$$
Then $dx=dt/n$ and, because $g$ is $1$-periodic,
$$
g(nx)=g(j+t)=g(t).
$$
Therefore
$$
\begin{aligned}
\int_0^1 f(x)g(nx)\,dx
&=\sum_{j=0}^{n-1}\frac1n
\int_0^1 f\left(\frac{j+t}{n}\right)g(t)\,dt\\
&=\int_0^1 g(t)A_n(t)\,dt,
\end{aligned}
$$
where
$$
A_n(t)=\frac1n\sum_{j=0}^{n-1}
f\left(\frac{j+t}{n}\right).
$$
:::

<1>2. The shifted Riemann sums $A_n(t)$ converge uniformly in $t$ to $\int_0^1f$.
::: {.proof}
Because $f$ is continuous and $1$-periodic, it is uniformly continuous on
$\mathbb R$. Let
$$
\omega_f(\delta)
=\sup\{|f(x)-f(y)|:|x-y|\le\delta\}.
$$
Then
$$
\omega_f(\delta)\to0
$$
as $\delta\to0$.

For $0\le t\le1$,
$$
\left|\frac{j+t}{n}-\frac jn\right|\le\frac1n,
$$
so
$$
\left|A_n(t)-\frac1n\sum_{j=0}^{n-1}f(j/n)\right|
\le\omega_f(1/n).
$$
The ordinary left-endpoint Riemann sums satisfy
$$
\frac1n\sum_{j=0}^{n-1}f(j/n)
\longrightarrow\int_0^1f(x)\,dx.
$$
The displayed bound is independent of $t$, hence
$$
A_n(t)\longrightarrow\int_0^1f(x)\,dx
$$
uniformly for $t\in[0,1]$.
:::

<1>3. Pass to the limit in the integral.
::: {.proof}
Since $g$ is continuous on $[0,1]$, it is bounded. Uniform convergence from
step <1>2 gives
$$
\begin{aligned}
\lim_{n\to\infty}\int_0^1 f(x)g(nx)\,dx
&=\int_0^1g(t)
\left(\int_0^1f(x)\,dx\right)dt\\
&=\left(\int_0^1f(x)\,dx\right)
\left(\int_0^1g(t)\,dt\right).
\end{aligned}
$$
This is the desired formula.
:::
:::
