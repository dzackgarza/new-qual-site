---
title: Commuting limiting operations
order: 50
topics:
- Uniform Convergence
- Convergence of Functions
---

# Commuting limiting operations

[[PR-LCV2V]]

[[FE-5JE3Z]]

[[PR-SCTER]]

[[FE-MDTXW]]

[[PR-DWOXP]]

[[FE-73BWZ]] [[FE-GN3CF]]

[[FE-2UZDB]]

[[PR-UZVC3]]

## Double limits

::: {.example title="Iterated limits of a double sequence need not agree"}
For $a_{mn}\coloneqq\frac{n}{n+m}$,
$$
\lim_{m\to \infty}\lim_{n\to\infty} \frac{n}{n + m} = 1 \neq 0 =
\lim_{n\to \infty}\lim_{m\to\infty} \frac{n}{n + m}.
$$

:::

## Suprema and limits

::: {.example title="The limit of the suprema need not be the supremum of the limit"}
For $f_n\coloneqq\chi_{[n,n+1]}$ on $\RR$, $\lim_n\sup_x\abs{f_n(x)} = 1$ and $\sup_x\abs{\lim_nf_n(x)} = 0$.

:::

::: {.example title="A pointwise limit of bounded functions need not be bounded"}
On $(0,1)$, $f_n(x)\coloneqq\min(n,1/x)$ is bounded by $n$ and converges pointwise to $1/x$, which is unbounded.

:::

## Continuity

::: {.example title="A pointwise limit of continuous functions need not be continuous"}
For $f_n(x) \coloneqq x^n$ on $[0,1]$ and $x_k\in[0,1)$ with $x_k\to 1$,
$$
\begin{aligned}
\lim_{k\to\infty}\lim_{n\to\infty} x_k^n
&= \lim_{k\to \infty } 0
= 0, \\
\lim_{n\to\infty } \lim_{k\to\infty } x_k^n
&= \lim_{n\to\infty} 1^n
= 1,
\end{aligned}
$$
so $\lim_nf_n = \chi_{\theset1}$ is not continuous at $1$.

:::

## Differentiability

::: {.example title="A uniform limit of differentiable functions need not be differentiable"}
$f_n(x) \coloneqq \sqrt{x^2 + {1\over n}}$ is differentiable on $\RR$ and converges uniformly to $\abs{x}$, which is not differentiable at $0$.

:::

::: {.example title="The limit of the derivatives need not be the derivative of the limit"}
Let $f_n(x) \coloneqq \frac{x}{1 + nx^2}$ on $\RR$.
The maximum of $\abs{f_n}$ is $f_n(1/\sqrt n) = \frac{1}{2\sqrt n}$, so $f_n\to 0$ uniformly and the limit has derivative $0$.
But
$$
f_n'(x) = \frac{1-nx^2}{\qty{1 + nx^2}^2},
$$
so $f_n'(0) = 1$ for all $n$.

Likewise, for $0<c<1$, $g_n(x)\coloneqq n^{-c}\sin(nx)\to0$ uniformly, while $g_n'(x) = n^{1-c}\cos(nx)$ is unbounded in $n$ at $x=0$.

:::

::: {.remark}
If $f_n$ are differentiable on an interval, $f_n'$ converges uniformly, and $f_n(x_0)$ converges for one $x_0$, then $f_n$ converges uniformly on bounded subintervals to a differentiable $f$ with $f' = \lim_n f_n'$.
Without uniform convergence of the derivatives, a uniform limit of polynomials can be any continuous function on $[a,b]$ by the Weierstrass approximation theorem, for example a nowhere differentiable one such as the Weierstrass function.

:::

::: {.example title="A differentiable function need not have a continuous derivative"}
$f(x)\coloneqq x^2\sin(1/x)$ for $x\neq0$ and $f(0)\coloneqq0$ is differentiable on $\RR$, and $f'(x) = 2x\sin(1/x)-\cos(1/x)$ has no limit at $0$.
Conversely, $\abs x$ is continuous and not differentiable at $0$, and the Weierstrass function is continuous and differentiable nowhere.

:::

## Integrals

::: {.example title="The limit of the integrals need not be the integral of the limit"}
On $[0,1]$, $f_n\coloneqq n\chi_{(0,1/n)}\to0$ pointwise while $\int_0^1f_n = 1$.

:::

::: {.example title="A pointwise limit of Riemann integrable functions need not be Riemann integrable"}
Let $(q_n)$ enumerate $\QQ\cap[0,1]$ and $f_N\coloneqq\sum_{n\leq N}\chi_{\theset{q_n}}$.
Each $f_N$ has finitely many discontinuities and $\int_0^1 f_N = 0$, but $f_N\to\chi_{\QQ\cap[0,1]}$ pointwise, which is not Riemann integrable.

:::
