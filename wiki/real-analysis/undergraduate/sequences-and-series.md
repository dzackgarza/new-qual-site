---
title: Sequences and series
order: 35
topics:
- Sequences of Numbers
- Series of Numbers
- Series of Functions
- Limits
---

# Sequences and series

## Sequences of functions

A sequence $f_n\colon X\to\RR$ converges pointwise to $f$ if for every $x$ and $\varepsilon>0$ there is $N$, depending on $x$ and $\varepsilon$, with $\abs{f_n(x)-f(x)}<\varepsilon$ for $n\geq N$; it converges uniformly if $N$ can be chosen independently of $x$.
A uniform limit of continuous functions is continuous, and on a space of finite measure a uniform limit of integrable functions has integral equal to the limit of the integrals.

[[D-S2YWR]]

::: {.example title="A continuous sum of a series that does not converge uniformly"}
On $(0,1]$, let
$$
g(x) \coloneqq \sum_{n=1}^{\infty} {1 \over 1 + n^2 x}.
$$
For every $a>0$ the series converges uniformly on $[a,1]$ by comparison with
$\sum_{n\ge1}(n^2a)^{-1}$, so $g$ is continuous on $(0,1]$.
The convergence is not uniform on $(0,1]$: the $n$th summand at $x=1/n^2$ equals $1/2$, so the summands do not converge uniformly to zero.

:::

## Sequences of numbers

::: {.slogan}
$\limsup_n a_n$ is the largest limit of a convergent subsequence of $(a_n)$ in $[-\infty,\infty]$, and $\liminf_n a_n$ is the smallest.

:::

[[PR-4EVYE]]

::: {.proof title="Cauchy condensation test"}
Let $a_1\geq a_2\geq\cdots\geq0$.
The block $2^k\leq n<2^{k+1}$ has $2^k$ terms, each at most $a_{2^k}$, so $\sum_{n\geq1}a_n\leq\sum_{k\geq0}2^ka_{2^k}$.
The block $2^{k-1}<n\leq2^k$ has $2^{k-1}$ terms, each at least $a_{2^k}$, so $2^{k-1}a_{2^k}\leq\sum_{2^{k-1}<n\leq2^k}a_n$ and
$$
\sum_{k\geq0}2^ka_{2^k} \leq a_1 + 2\sum_{n\geq2}a_n.
$$
Hence $\sum_n a_n$ and $\sum_k 2^ka_{2^k}$ converge or diverge together.

:::

[[FF-QLRXX]]

[[FD-D2QPH]]

## Series

A series $\sum_n a_n$ of real numbers converges if and only if for every $\varepsilon>0$ there is $N$ with $\abs{\sum_{n=M}^{M'}a_n}<\varepsilon$ for all $M'\geq M\geq N$ (the Cauchy criterion).
The comparison and $p$-tests give sufficient conditions, and a Taylor series of $f$ converges to $f$ at $x$ exactly when the remainder in Taylor's theorem tends to $0$ at $x$.
For series of functions, the Cauchy criterion in the norm $\norm{\wait}_\infty$ characterizes uniform convergence.

[[PR-P6NHI]]

[[PR-UJ64S]]

[[C-3S4XS]]

[[PR-GT5RS]]

[[PR-H4CYN]]

[[PR-6OHTJ]]

[[PR-LEDI3]]

[[C-VSE32]]

[[PR-4RWAG]]

[[T-2R7PC]]

## Uniform convergence

For bounded $f_n - f$,
$$
f_n\to f \text{ uniformly}
\quad\Longleftrightarrow\quad
\norm{f_n-f}_\infty\to 0.
$$
Uniform convergence is proved by bounding $\sup_x\abs{f_n(x)-f(x)}$ by a quantity independent of $x$ tending to $0$, and disproved by exhibiting $x_n$ and $\varepsilon>0$ with $\abs{f_n(x_n)-f(x_n)}\geq\varepsilon$ for infinitely many $n$.
For a series, the Weierstrass $M$-test reduces uniform convergence to convergence of a numerical series.

[[PR-WUZSG]]

[[FF-I6VGK]]

[[FS-FZL2X]] [[FS-THMMW]]

[[FF-IAUQG]] [[FS-5FKPD]]

::: {.remark title="Negating uniform convergence"}
$f_n\not\to0$ uniformly if and only if there are $\varepsilon>0$, infinitely many $n$, and points $x_n$ with $\abs{f_n(x_n)}\geq\varepsilon$.
$(f_n)$ is not uniformly Cauchy if and only if there are $\varepsilon>0$ and, for every $N$, indices $m,n\geq N$ and a point $x$ with $\abs{f_n(x)-f_m(x)}\geq\varepsilon$.

:::

[[PR-RWROV]]

::: {.proof}
Let $(f_k)$ be Cauchy in $C([0,1])$ with the norm $\norm{\wait}_\infty$.
For each $x$, $\abs{f_k(x) - f_j(x)} \leq \norm{f_k - f_j}_\infty$, so $(f_k(x))$ is Cauchy in $\RR$; let $f(x) \coloneqq \lim_k f_k(x)$.

Given $\varepsilon>0$, choose $N$ with $\norm{f_k-f_j}_\infty<\varepsilon$ for $j,k\geq N$.
For fixed $k\geq N$ and every $x$, letting $j\to\infty$ in $\abs{f_k(x)-f_j(x)}<\varepsilon$ gives $\abs{f_k(x)-f(x)}\leq\varepsilon$, so $\norm{f_k-f}_\infty\leq\varepsilon$.
Thus $f_k\to f$ uniformly, and $f$ is continuous as a uniform limit of continuous functions, so $f\in C([0,1])$.

:::

::: {.remark}
The same argument proves completeness of other spaces of functions with the norm $\norm{\wait}_\infty$, such as the bounded functions on a set or $C_b(X)$ for a metric space $X$, provided the uniform limit is shown to lie in the space.

:::

[[T-3QNBQ]]

[[FT-ITKJU]]
