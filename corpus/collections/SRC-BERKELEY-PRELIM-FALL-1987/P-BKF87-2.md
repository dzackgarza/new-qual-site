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
<1>1. The limit function $f$ is nondecreasing.

::: {.proof}
If $0\leq x\leq y\leq1$, then
$$
f_n(x)\leq f_n(y)
$$
for every $n$. Passing to the pointwise limit gives
$$
f(x)\leq f(y).
$$
:::

<1>2. Given $\varepsilon>0$, there is a partition
$$
0=x_0<x_1<\cdots<x_m=1
$$
such that
$$
0\leq f(x_i)-f(x_{i-1})<\frac{\varepsilon}{2}
$$
for every $1\leq i\leq m$.

::: {.proof}
Since $f$ is continuous on the compact interval $[0,1]$, it is uniformly continuous. Choose $\delta>0$ such that
$$
\abs{x-y}<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(y)}<\frac{\varepsilon}{2}.
$$
Choose a finite partition with mesh smaller than $\delta$. Step <1>1 shows that the endpoint differences are nonnegative, and uniform continuity bounds them above by $\varepsilon/2$.
:::

<1>3. There is an integer $N$ such that, for every $n\geq N$ and every partition point $x_i$,
$$
\abs{f_n(x_i)-f(x_i)}<\frac{\varepsilon}{2}.
$$

::: {.proof}
For each of the finitely many points $x_0,\ldots,x_m$, pointwise convergence gives an integer after which the displayed inequality holds at that point. Take $N$ to be the maximum of those finitely many integers.
:::

<1>4. If $n\geq N$ and $x\in[0,1]$, then
$$
\abs{f_n(x)-f(x)}<\varepsilon.
$$

::: {.proof}
Choose $i$ such that
$$
x_{i-1}\leq x\leq x_i.
$$
By monotonicity of $f_n$ and step <1>1,
$$
f_n(x_{i-1})\leq f_n(x)\leq f_n(x_i)
$$
and
$$
f(x_{i-1})\leq f(x)\leq f(x_i).
$$
Therefore, using steps <1>2 and <1>3,
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

<1>5. The convergence $f_n\to f$ is uniform on $[0,1]$.

::: {.proof}
For every $\varepsilon>0$, step <1>3 gives an $N$ such that step <1>4 holds simultaneously for every $x\in[0,1]$ whenever $n\geq N$. This is the definition of uniform convergence.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
