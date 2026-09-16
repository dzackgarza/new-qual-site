---
title: Power series
order: 30
topics:
- Power Series
- Taylor Series
- Radius of Convergence
- Convergence Tests
- Series of Functions
- Series of Numbers
- Sequences of Functions
- Uniform Convergence
---

# Power series

Holomorphic and analytic are equivalent: the Cauchy integral formula gives the power-series expansion, and the coefficient formula gives the Cauchy estimates.

![](../../../../assets/assets/figures/2021-10-28_21-22-12.png)

![](../../../../assets/assets/figures/2021-10-28_21-22-35.png)

[[D-V6UQJ]]

[[T-GROTS]]

[[PR-QNDSD]]

## Holomorphic implies analytic

[[T-SRY2V]]

::: {.proof}
After translating and rescaling, $p=0$ and $f$ is holomorphic on a neighborhood of $\overline{\DD}$; fix $z\in\DD$.
For $w\in S^1$,
$$
{1\over w-z} = {1\over w} \qty{ 1 + \qty{z\over w} + \qty{z\over w}^2 + \cdots}
,$$
which converges uniformly in $w\in S^1$ because $\abs{z/w} = \abs z < 1$, so the Cauchy integral formula may be expanded term by term:
$$
f(z)=\frac{1}{2 \pi i} \int_{S^{1}} \frac{f(w) }{w-z} \dw
= \sum z^{k} \frac{1}{2 \pi i} \int_{S^{1}} \frac{f(w)}{w^{k+1}} \dw
=\sum c_{k} z^{k}
.$$

:::

::: {.proof title="Holomorphic implies analytic, alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-53-51.png)

:::

[[T-K66DJ]]

[[C-7S2CO]]

::: {.remark title="The coefficient formula"}
By the integral formula, for $f$ holomorphic on $D_R(z_0)$, all $k\geq 0$ and all $0<r<R$:
$$
c_k = {1\over 2\pi r^k} \int_0^{2\pi} f(z_0 + re^{i\theta}) e^{-ik\theta}\dtheta
.$$
Bounding the integrand gives the [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy estimate]], and the same formula for $k<0$ on an annulus gives the coefficients of the [[complex-analysis/singularities/laurent-series|Laurent series]].

:::

[[PR-4BVDD]]

::: {.proof}
On the disc $\abs z\leq R$, the terms of $e^z = \sum_{n\geq 0} z^n/n!$ satisfy $\abs{z^n/n!}\leq R^n/n!$, and $\sum_{n\geq 0} R^n/n! = e^R < \infty$.
By the Weierstrass $M\dash$test, the series converges uniformly on $\abs z\leq R$.

:::

## Abel's theorem

[[L-EAZX6]]

::: {.proof}
Let $A_n \coloneqq \sum_{k=1}^n a_k$ and $A_0\coloneqq 0$, and choose $M$ with $\abs{A_n}\leq M$ for all $n$.
Summation by parts ([[PR-6GL7M]] with $m=1$) gives
$$
\sum_{k=1}^n a_k b_k = A_n b_n + \sum_{k=1}^{n-1} A_k (b_k - b_{k+1})
.$$
Since $\abs{A_n b_n}\leq M b_n \to 0$, the first term tends to $0$.
Since $b_k$ is decreasing, $b_k - b_{k+1}\geq 0$, so
$$
\sum_{k=1}^{n-1} \abs{A_k (b_k - b_{k+1})} \leq M\sum_{k=1}^{n-1}(b_k - b_{k+1}) = M(b_1 - b_n) \leq M b_1
,$$
and the series $\sum_{k\geq 1} A_k(b_k - b_{k+1})$ converges absolutely.
Hence the partial sums $\sum_{k=1}^n a_k b_k$ converge.

:::

[[T-B7YTE]]

[[L-MYZOX]]

::: {.example title="The alternating harmonic series"}
Integrating the geometric series $\sum_{k\geq 0}(-z)^k = 1/(1+z)$ term by term gives
$$
\sum_{k\geq 1} {(-1)^{k+1} z^k \over k} = \log(1+z), \qquad \abs z < 1
.$$
The series converges at $z=1$ by the alternating series test, so Abel's theorem gives $\sum_{k\geq1}(-1)^{k+1}/k = \lim_{x\to 1^-}\log(1+x) = \log 2$.

:::

::: {.example title="The converse of Abel's theorem fails"}
Take $f(z) = \sum (-z)^n = 1/(1+z)$.
At $z=1$ the series $1-1+1-\cdots$ diverges, while $\lim_{x\to 1^-} f(x) = 1/2$.
So a radial limit can exist at a point where the series diverges, and the converse of Abel's theorem is false.

:::

[[PR-6GL7M]]

::: {.proof}
Define $A_n \coloneqq \sum_{k\leq n} a_k$, use $a_k = A_k - A_{k-1}$, reindex, and peel off the top and bottom terms:
$$
\begin{aligned}
\sum_{m\leq k \leq n} a_k b_k
&= \sum_{m\leq k \leq n} (A_k - A_{k-1}) b_k \\
&= \sum_{m\leq k \leq n} A_kb_k - \sum_{m-1\leq k \leq n-1} A_{k} b_{k+1} \\
&= A_nb_n - A_{m-1} b_{m} + \sum_{m\leq k \leq n-1} A_k(b_k - b_{k+1}) \\
&= A_nb_n - A_{m-1} b_{m} - \sum_{m\leq k \leq n-1} A_k(b_{k+1} - b_{k})
\end{aligned}.$$

:::

[[PR-NZZ2C]]

The standard series and the factorial notation are collected on [[complex-analysis/basics/series-reference|Series: Reference]].

## Exercises

[[E-EG3W7]]
[[E-SKD7P]] [[E-EMISN]] [[E-QLRNW]]
[[E-ZQGR5]] [[E-FS7GZ]] [[E-VWVTY]]
[[FE-LAN3V]] [[FE-VWNUI]] [[FE-EUOB2]]
[[E-BUVLS]] [[E-VCLTY]] [[E-DUMQG]] [[E-AHBVF]] [[E-SQ4GJ]] [[E-ENJAF]] [[E-GMGFS]] [[E-XOCPO]] [[E-QCVGX]]
[[E-ZWNTH]] [[E-THK2Z]] [[E-ORJPT]]
[[E-TVJFL]] [[E-3QAC4]] [[E-SS1.EX-13]] [[E-FMLK2]] [[E-I26BF]]
