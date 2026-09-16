---
title: Undergraduate counterexamples
order: 90
---

# Undergraduate counterexamples

## A continuous limit without uniform convergence

::: {.example title="A series of continuous functions that converges non-uniformly to a continuous function"}
For $x>0$ let
$$
g(x) \coloneqq \sum_{n\geq1} {1 \over 1 + n^2 x}.
$$
On $[\delta,\infty)$ each term is at most $1/(n^2\delta)$, so the series converges uniformly there by the Weierstrass $M$-test, and $g$ is continuous on $(0,\infty)$.
The convergence is not uniform on $(0,\infty)$: at $x = 1/N^2$ the $N$th term equals $1/2$, so the tails $\sum_{n\geq N} (1+n^2x)^{-1}$ are not uniformly small.

:::

## Variations on the Dirichlet function

For each function below, the discontinuity set $D_f$, the set $D_f'$ of points where $f$ is not differentiable, and Riemann and Lebesgue integrability are recorded.
Every function $f\colon\RR\to\RR$ has $D_f$ an $F_\sigma$ set, since $D_f = \bigcup_{k\geq1}\theset{x \st \operatorname{osc}_f(x)\geq 1/k}$ and each of these sets is closed.

::: {.example title="The Dirichlet function"}
$$
f(x) \coloneqq \chi_\QQ(x) = \begin{cases}
1, & x\in \QQ, \\
0, & x\notin\QQ.
\end{cases}
$$
Every interval contains rationals and irrationals, so $f$ is continuous nowhere and differentiable nowhere.
On $[0,1]$ every upper Darboux sum is $1$ and every lower Darboux sum is $0$, so $f$ is not Riemann integrable.
Since $f=0$ almost everywhere, $f$ is Lebesgue integrable with $\int_\RR f = 0$.

:::

::: {.example title="A Dirichlet-type function continuous at exactly one point"}
$$
f(x) \coloneqq x\chi_\QQ(x) = \begin{cases}
x, & x\in \QQ, \\
0, & x\notin\QQ.
\end{cases}
$$
Since $\abs{f(x)}\leq\abs x$, $f$ is continuous at $0$; at $x_0\neq0$, rationals and irrationals approaching $x_0$ give limits $x_0$ and $0$, so $D_f = \RR\smz$.
At $0$ the difference quotient $f(h)/h = \chi_\QQ(h)$ has no limit, so $f$ is differentiable nowhere.
On $[0,1]$ the upper Darboux integral is $\int_0^1 x\dx = 1/2$ and the lower Darboux integral is $0$, so $f$ is not Riemann integrable; $f=0$ almost everywhere, so $f$ is Lebesgue integrable with $\int_\RR \abs f = 0$.

:::

::: {.example title="A Dirichlet-type function differentiable at exactly one point"}
$$
f(x) \coloneqq x^2\chi_\QQ(x) = \begin{cases}
x^2, & x\in \QQ, \\
0, & x\notin\QQ.
\end{cases}
$$
As before $D_f = \RR\smz$.
At $0$, $\abs{f(h)/h}\leq\abs h\to0$, so $f'(0)=0$, and $f$ is not differentiable at any point of discontinuity, so $D_f'=\RR\smz$.
The Darboux integrals on $[0,1]$ are $1/3$ and $0$, so $f$ is not Riemann integrable; $f=0$ almost everywhere, so $\int_\RR\abs f=0$.

:::

::: {.example title="A Dirichlet-type function taking two values of opposite sign"}
$$
f(x) \coloneqq x\qty{\chi_\QQ(x) - \chi_{\RR\setminus\QQ}(x)} = \begin{cases}
x, & x\in \QQ, \\
-x, & x\notin\QQ.
\end{cases}
$$
Since $\abs{f(x)} = \abs x$, $f$ is continuous at $0$, and $D_f = \RR\smz$.
At $0$ the difference quotient $f(h)/h = \pm1$ according to whether $h$ is rational, so $f$ is differentiable nowhere.
Since $\abs f = \abs x$ everywhere, $f$ is not Lebesgue integrable on $\RR$.

:::

::: {.proposition title="Non-integrability of $x\qty{\chi_\QQ - \chi_{\RR\setminus\QQ}}$ on $[0,1]$"}
For $f(x) \coloneqq x\qty{\chi_\QQ(x) - \chi_{\RR\setminus\QQ}(x)}$, the upper Darboux integral of $f$ on $[0,1]$ is $1/2$ and the lower Darboux integral is $-1/2$.

:::

::: {.proof}
Let $0=x_0<x_1<\cdots<x_n=1$ be a partition.
Each $[x_{i-1},x_i]$ contains rationals arbitrarily close to $x_i$ and irrationals arbitrarily close to $x_i$, and $\abs{f(x)}\leq x\leq x_i$ there, so $\sup_{[x_{i-1},x_i]} f = x_i$ and $\inf_{[x_{i-1},x_i]} f = -x_i$.
Hence the upper sum is $\sum_i x_i(x_i-x_{i-1})$ and the lower sum is its negative.
These are right-endpoint Riemann sums of $x\mapsto x$, which are at least $\int_0^1 x\dx = 1/2$ and tend to $1/2$ as the mesh tends to $0$.
So the upper Darboux integral is $1/2$ and the lower Darboux integral is $-1/2$.

:::

## The Thomae function

::: {.example title="The Thomae function"}
$$
f(x) \coloneqq \begin{cases}
\frac 1 q, & x = \frac p q \in \QQ \text{ in lowest terms with } q\geq1, \\
0, & x\notin\QQ.
\end{cases}
$$
For $\varepsilon>0$, only finitely many rationals in a bounded interval have denominator at most $1/\varepsilon$, so $f(x)\to0$ as $x\to x_0$ for every $x_0$.
Hence $f$ is continuous exactly on $\RR\setminus\QQ$ and $D_f=\QQ$.
$f$ is differentiable nowhere.
Since $D_f$ is countable, hence null, and $f$ is bounded, $f$ is Riemann integrable on every $[a,b]$ by the Lebesgue criterion, with $\int_a^b f = 0$; it is also Lebesgue integrable on $\RR$ with integral $0$.

:::

## The Weierstrass function

::: {.example title="The Weierstrass function"}
For $a \in (0, 1)$ and an odd integer $b\geq1$ with $ab > 1 + {3\pi \over 2}$, let
$$
f(x)\coloneqq\sum_{n=0}^{\infty} a^{n} \cos \left(b^{n} \pi x\right).
$$
The $n$th term is bounded by $a^n$, so the series converges uniformly by the Weierstrass $M$-test, $f$ is continuous, and $\abs f\leq(1-a)^{-1}$.
Weierstrass's theorem states that $f$ is differentiable nowhere.
$f$ is Riemann integrable on every compact interval, and not Lebesgue integrable on $\RR$, since it is continuous, $2$-periodic, and not almost everywhere zero.

:::

## Summary

| Function | Bounded | $D_f$ | $D'_f$ | Riemann integrable on $[0,1]$ | Lebesgue integrable on $\RR$ |
| --- | --- | --- | --- | --- | --- |
| $\chi_\QQ$ | Yes, $\abs{f} \leq 1$ | $\RR$ | $\RR$ | No | Yes, $\int f=0$ |
| $x\chi_\QQ$ | No | $\RR\smz$ | $\RR$ | No | Yes, $\int \abs f=0$ |
| $x^2\chi_\QQ$ | No | $\RR\smz$ | $\RR\smz$ | No | Yes, $\int \abs f=0$ |
| $x\qty{\chi_\QQ - \chi_{\RR\setminus\QQ}}$ | No | $\RR\smz$ | $\RR$ | No | No, $\abs{f}=\abs{x}$ |
| Thomae | Yes | $\QQ$ | $\RR$ | Yes, $\int f = 0$ | Yes, $\int f=0$ |
| Weierstrass | Yes, $\abs f\le (1-a)^{-1}$ | $\emptyset$ | $\RR$ | Yes | No |
