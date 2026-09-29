---
schema: qual/card@1
id: P-BKF87-2
kind: problem
title: Pointwise convergence of monotone functions to a continuous limit is uniform
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f_n:[0,1]\to[0,1]$ be nondecreasing functions. Suppose $f_n(x)\to f(x)$ pointwise and $f$ is continuous. Prove that $f_n\to f$ uniformly on $[0,1]$. The functions $f_n$ need not be continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The limit function $f$ is nondecreasing.

::: pf-proof

If $0\leq x\leq y\leq1$, then
$$
f_n(x)\leq f_n(y)
$$
for every $n$. Passing to the pointwise limit gives
$$
f(x)\leq f(y).
$$

:::

:::

::: {.pf-step #s2}

Given $\varepsilon>0$, there is a partition
$$
0=x_0<x_1<\cdots<x_m=1
$$
such that
$$
0\leq f(x_i)-f(x_{i-1})<\frac{\varepsilon}{2}
$$
for every $1\leq i\leq m$.

::: pf-proof

Since $f$ is continuous on the compact interval $[0,1]$, it is uniformly continuous. Choose $\delta>0$ such that
$$
\abs{x-y}<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(y)}<\frac{\varepsilon}{2}.
$$
Choose a finite partition with mesh smaller than $\delta$. Step [](#s1){.pf-ref} shows that the endpoint differences are nonnegative, and uniform continuity bounds them above by $\varepsilon/2$.

:::

:::

::: {.pf-step #s3}

There is an integer $N$ such that, for every $n\geq N$ and every partition point $x_i$,
$$
\abs{f_n(x_i)-f(x_i)}<\frac{\varepsilon}{2}.
$$

::: pf-proof

For each of the finitely many points $x_0,\ldots,x_m$, pointwise convergence gives an integer after which the displayed inequality holds at that point. Take $N$ to be the maximum of those finitely many integers.

:::

:::

::: {.pf-step #s4}

If $n\geq N$ and $x\in[0,1]$, then
$$
\abs{f_n(x)-f(x)}<\varepsilon.
$$

::: pf-proof

Choose $i$ such that
$$
x_{i-1}\leq x\leq x_i.
$$
By monotonicity of $f_n$ and step [](#s1){.pf-ref},
$$
f_n(x_{i-1})\leq f_n(x)\leq f_n(x_i)
$$
and
$$
f(x_{i-1})\leq f(x)\leq f(x_i).
$$
Therefore, using steps [](#s2){.pf-ref} and [](#s3){.pf-ref},
$$
\begin{aligned}
f_n(x)-f(x)
&\leq
f_n(x_i)-f(x_{i-1})\\
&=
\bigl(f_n(x_i)-f(x_i)\bigr)
+
\bigl(f(x_i)-f(x_{i-1})\bigr)\\
&<
\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
=
\varepsilon.
\end{aligned}
$$
Similarly,
$$
\begin{aligned}
f(x)-f_n(x)
&\leq
f(x_i)-f_n(x_{i-1})\\
&=
\bigl(f(x_i)-f(x_{i-1})\bigr)
+
\bigl(f(x_{i-1})-f_n(x_{i-1})\bigr)\\
&<
\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
=
\varepsilon.
\end{aligned}
$$
Thus $\abs{f_n(x)-f(x)}<\varepsilon$.

:::

:::

::: {.pf-step #s5}

The convergence $f_n\to f$ is uniform on $[0,1]$.

::: pf-proof

For every $\varepsilon>0$, step [](#s3){.pf-ref} gives an $N$ such that step [](#s4){.pf-ref} holds simultaneously for every $x\in[0,1]$ whenever $n\geq N$. This is the definition of uniform convergence.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
