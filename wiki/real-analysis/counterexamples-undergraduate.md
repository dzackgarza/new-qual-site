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

The uniform convergence on $[\delta,\infty)$ is the Weierstrass $M$-test of [@Rud76, ch. 7, Theorem 7.10], and the failure on $(0,\infty)$ is the uniform Cauchy criterion of [@Rud76, ch. 7, Theorem 7.8] read negatively.
:::

## Variations on the Dirichlet function

For $f\colon\RR\to\RR$, $D_f$ denotes the set of points where $f$ is discontinuous and $D_f'$ the set of points where $f$ is not differentiable.
Every function $f\colon\RR\to\RR$ has $D_f$ an $F_\sigma$ set, since $D_f = \bigcup_{k\geq1}\theset{x \st \operatorname{osc}_f(x)\geq 1/k}$ and each of these sets is closed ([[FF-AVBFU]]).

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

This is the first function of [@Rud76, ch. 4, Example 4.27], which computes its discontinuity set; the failure of Riemann integrability is [@Rud76, ch. 11, Theorem 11.33(b)], since a Riemann integrable function is continuous almost everywhere and this one is continuous nowhere, and the Lebesgue integral is $0$ because $f$ vanishes off a null set.
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

This is the second function of [@Rud76, ch. 4, Example 4.27], continuous at $0$ and at no other point; the Darboux values are computed above and the Lebesgue statement is again $f=0$ almost everywhere.
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

This is the variant of the second function of [@Rud76, ch. 4, Example 4.27] with $x$ replaced by $x^2$; the discrepancy $D_f=\RR\smz$, the derivative $f'(0)=0$ and the Darboux values are computed above.
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

This is a further variant of the family of [@Rud76, ch. 4, Example 4.27]; the sign convention is what makes $\abs f=\abs x$, and the non-integrability is $\int_\RR\abs x\,\dx=\infty$.
:::

::: {.proposition title="The Darboux integrals of $x\qty{\chi_\QQ - \chi_{\RR\setminus\QQ}}$ on $[0,1]$"}
For $f(x) \coloneqq x\qty{\chi_\QQ(x) - \chi_{\RR\setminus\QQ}(x)}$, the upper Darboux integral of $f$ on $[0,1]$ is $1/2$ and the lower Darboux integral is $-1/2$.

The upper and lower integrals it computes are those of [@Rud76, ch. 6, Definition 6.1].

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

$f$ is differentiable nowhere, that is, $D_f'=\RR$.
At a rational $x_0$ it is not even continuous.
At an irrational $x$ we have $f(x)=0$, and for every $N\geq1$ the pigeonhole principle gives integers $p$ and $q$ with $1\leq q\leq N$ and $\abs{x-p/q}<1/(qN)$.
Writing $q'$ for the denominator of $p/q$ in lowest terms, $q'\mid q$, so $f(p/q)=1/q'\geq1/q$ and
$$
\abs{\frac{f(p/q)-f(x)}{p/q-x}} = \frac{f(p/q)}{\abs{p/q-x}} > \frac1q\cdot qN = N ,
$$
while along irrationals $y\to x$ the difference quotient is $0$.
So the quotient is unbounded and has no limit, and $f$ is not differentiable at $x$.

Since $D_f$ is countable, hence null, and $f$ is bounded, $f$ is Riemann integrable on every $[a,b]$ by the [[PR-TDH2A|Lebesgue criterion]], with $\int_a^b f = 0$; it is also Lebesgue integrable on $\RR$ with integral $0$.

This is Thomae's function: the continuity and differentiability sets are computed above, and the Riemann integrability is the Lebesgue criterion of [@Rud76, ch. 11, Theorem 11.33(b)], since the set of discontinuities is countable and hence of measure zero.

:::

## The Weierstrass function

::: {.example title="A Weierstrass-type function that is differentiable nowhere"}
Let $\varphi\colon\RR\to\RR$ be the $2$-periodic function with $\varphi(x)=\abs x$ for $-1\leq x\leq1$, and let
$$
f(x)\coloneqq\sum_{n=0}^{\infty}\qty({3\over4})^{n}\varphi(4^{n}x).
$$
Since $0\leq\varphi\leq1$, the series converges uniformly by the Weierstrass $M$-test [@Rud76, Theorem 7.10], so $f$ is continuous, and $\abs f\leq 4$.
By [@Rud76, Theorem 7.18], whose function (37) is this one with its $\varphi$, $f$ is differentiable nowhere.
$f$ is Riemann integrable on every compact interval, and not Lebesgue integrable on $\RR$, since it is continuous, $2$-periodic, and $f(1/2)=1/2$.

:::

## Summary

| Function | Bounded | $D_f$ | $D'_f$ | Riemann integrable on $[0,1]$ | Lebesgue integrable on $\RR$ |
| --- | --- | --- | --- | --- | --- |
| $\chi_\QQ$ | Yes, $\abs{f} \leq 1$ | $\RR$ | $\RR$ | No | Yes, $\int f=0$ |
| $x\chi_\QQ$ | No | $\RR\smz$ | $\RR$ | No | Yes, $\int \abs f=0$ |
| $x^2\chi_\QQ$ | No | $\RR\smz$ | $\RR\smz$ | No | Yes, $\int \abs f=0$ |
| $x\qty{\chi_\QQ - \chi_{\RR\setminus\QQ}}$ | No | $\RR\smz$ | $\RR$ | No | No, $\abs{f}=\abs{x}$ |
| Thomae | Yes | $\QQ$ | $\RR$ | Yes, $\int f = 0$ | Yes, $\int f=0$ |
| Weierstrass | Yes, $\abs f\le 4$ | $\emptyset$ | $\RR$ | Yes | No |
