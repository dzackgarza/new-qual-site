---
schema: qual/card@1
id: P-UGAP09F-08
kind: problem
title: Uniform convergence permits passage of the limit through an integral
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f:[0,1]\to\mathbb R$ and $f_n:[0,1]\to\mathbb R$ be continuous functions, and suppose $f_n\to f$ uniformly.

Give the definition of uniform convergence and, using basic properties of integrals and absolute values, show that
\[
\lim_{n\to\infty}\int_0^1 f_n(x)\,dx
=
\int_0^1 f(x)\,dx.
\]
:::

::: {.solution}
<1>1. The sequence $(f_n)$ converges uniformly to $f$ on $[0,1]$ if for every $\varepsilon>0$ there is an integer $N$ such that for every $n\ge N$ and every $x\in[0,1]$,
$$
|f_n(x)-f(x)|<\varepsilon.
$$

::: {.proof}
This is the definition of uniform convergence on $[0,1]$: the same index $N$ works simultaneously for every point of the domain.
:::

<1>2. For every $n$,
$$
\left|
\int_0^1 f_n(x)\,dx-
\int_0^1 f(x)\,dx
\right|
\le
\int_0^1 |f_n(x)-f(x)|\,dx.
$$

::: {.proof}
By linearity of the integral and the triangle inequality for integrals,
$$
\begin{aligned}
\left|
\int_0^1 f_n(x)\,dx-
\int_0^1 f(x)\,dx
\right|
&=
\left|\int_0^1 (f_n(x)-f(x))\,dx\right|\\
&\le
\int_0^1 |f_n(x)-f(x)|\,dx.
\end{aligned}
$$
:::

<1>3. One has
$$
\boxed{
\lim_{n\to\infty}\int_0^1 f_n(x)\,dx
=
\int_0^1 f(x)\,dx.
}
$$

::: {.proof}
Let $\varepsilon>0$. By uniform convergence, choose $N$ as in step <1>1. For every $n\ge N$ and every $x\in[0,1]$,
$$
|f_n(x)-f(x)|<\varepsilon.
$$
Therefore step <1>2 gives
$$
\left|
\int_0^1 f_n(x)\,dx-
\int_0^1 f(x)\,dx
\right|
\le
\int_0^1 |f_n(x)-f(x)|\,dx
<
\int_0^1\varepsilon\,dx
=\varepsilon.
$$
This is exactly the definition of convergence of the sequence of integrals to $\int_0^1 f(x)\,dx$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 gives the requested definition, and step <1>3 proves the desired interchange of limit and integral.
:::
:::
