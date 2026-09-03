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

:::{.proof}
Reduce to $z\in\DD$.
For fixed $z$ and any $w\in S^1$,
\[
{1\over w-z} = {1\over w} \qty{ 1 + \qty{z\over w} + \qty{z\over w}^2 + \cdots}
,\]
which converges uniformly on $S^1$, so the integral formula may be expanded term by term:
\[
f(z)=\frac{1}{2 \pi i} \int_{S^{1}} \frac{f(w) }{w-z} \dw
= \sum z^{k} \frac{1}{2 \pi i} \int_{S^{1}} \frac{f(w)}{w^{k+1}} \dw
=\sum c_{k} z^{k}
.\]

:::

:::{.proof title="Holomorphic implies analytic, alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-53-51.png)

:::

[[T-K66DJ]]

[[C-7S2CO]]

:::{.remark title="The coefficient formula"}
By the integral formula, for $f$ holomorphic on $D_R(z_0)$, all $k\geq 0$ and all $0<r<R$:
\[
c_k = {1\over 2\pi r^k} \int_0^{2\pi} f(z_0 + re^{i\theta}) e^{-ik\theta}\dtheta
.\]
Bounding this integrand is exactly the [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy estimate]], and letting the expansion run to negative $k$ is the [[complex-analysis/singularities/laurent-series|Laurent series]].

:::

[[PR-4BVDD]]

:::{.proof}
Estimate
\[
\abs{e^z} \leq \sum {\abs {z}^n \over n!} = e^{\abs{z}}
,\]
and apply the $M\dash$test: $\abs z \leq R < \infty$ gives $\abs{\sum {z^n/ n!}} \leq e^R < \infty$.

:::

## Abel's theorem

[[L-TVIDY]]

:::{.proof}
Use summation by parts.
For $\sum a_k b_k$, write
\[
\sum_{n=1}^m x_n Y_n + \sum_{n=1}^m X_n y_{n+1} = X_m Y_{m+1}
,\]
setting $x_n \da a_n$ and $y_n \da b_n - b_{n-1}$, so $X_n = A_n$ and $Y_n = b_n$ telescopes.
All $y_n$ are negative, so $\abs{y_n} = b_{n-1} - b_n$, and $a_n b_n = x_n Y_n$.
Then
\[
\sum_{n\geq 1} a_n b_n
&= \lim_{N\to\infty} \sum_{n\leq N} x_n Y_n \\
&= \lim_{N\to\infty} \sum_{n\leq N} X_N Y_N - \sum_{n\leq N} X_n y_{n+1} \\
&= - \sum_{n\geq 1} X_n y_{n+1}
,\]
using $\abs{X_N} = \abs{A_N}\leq M$, so $\abs{X_N Y_N} \leq M b_{N+1}\to 0$.
It remains to bound
\[
\sum_{k\geq n}\abs{ X_k y_{k+1} }
&\leq M \sum_{k\geq 1} \abs{y_{k+1}}\\
&\leq M \sum_{k\geq 1} b_{k} - b_{k+1} \\
&\leq 2M(b_1 - b_{n+1})\\
&\leq 2M b_1
.\]

:::

[[T-B7YTE]]

[[L-MYZOX]]

:::{.example title="An application"}
What is the alternating harmonic series?
Integrating a geometric series gives
\[
\sum {(-1)^k z^k \over k} = \log(z+1), \qquad \abs z < 1
.\]
Since $c_k \da (-1)^k/k \decreasesto 0$, the series converges at $z=1$, and Abel gives the value $\log 2$.

:::

:::{.remark title="The converse fails"}
Take $f(z) = \sum (-z)^n = 1/(1+z)$.
At $z=1$ the series $1-1+1-\cdots$ diverges, while $\lim_{x\to 1^-} f(x) = 1/2$.
So a radial limit can exist without the series converging there, which is why Abel's theorem is stated in only one direction.

:::

[[PR-6GL7M]]

:::{.proof}
Define $A_n \da \sum_{k\leq n} a_k$, use $a_k = A_k - A_{k-1}$, reindex, and peel off the top and bottom terms:
\[
\sum_{m\leq k \leq n} a_k b_k
&= \sum_{m\leq k \leq n} (A_k - A_{k-1}) b_k \\
&= \sum_{m\leq k \leq n} A_kb_k - \sum_{m-1\leq k \leq n-1} A_{k} b_{k+1} \\
&= A_nb_n - A_{m-1} b_{m} + \sum_{m\leq k \leq n-1} A_k(b_k - b_{k+1}) \\
&= A_nb_n - A_{m-1} b_{m} - \sum_{m\leq k \leq n-1} A_k(b_{k+1} - b_{k})
.\]

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
