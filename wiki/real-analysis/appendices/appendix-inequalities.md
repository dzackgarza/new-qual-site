---
title: Common inequalities
order: 23
---

# Common inequalities

## Cauchy--Schwarz, Hölder, and Plancherel

[[PR-X5D4Z]]

::: {.remark title="Cauchy--Schwarz in coordinates and in $L^2$"}
For $a,b\in\RR^n$ and for $f,g\in L^2(\RR^n)$, the inequality reads
$$
\begin{aligned}
\left(\sum_{k=1}^{n} a_{k} b_{k}\right)^{2}
&\leq\left(\sum_{k=1}^{n} a_{k}^{2}\right)\left(\sum_{k=1}^{n} b_{k}^{2}\right), \\
\abs{\int_{\RR^{n}} f(x) \overline{g(x)} \dx}^{2}
&\leq \int_{\RR^{n}}\abs{f(x)}^{2} \dx \int_{\RR^{n}}\abs{g(x)}^{2} \dx.
\end{aligned}
$$

:::

[[PR-IJOPU]]

[[PR-7BGSE]]

[[FT-GQRV2]]

[[T-4BDE3]]

[[T-5AALA]]

::: {.remark title="Parseval's identity for Fourier series"}
For $f\in L^2(-\pi,\pi)$ and the orthonormal basis $\theset{e^{ikx}/\sqrt{2\pi}}_{k\in\ZZ}$, Parseval's identity reads
$$
{1\over 2\pi} \int_{(-\pi, \pi)} \abs{f}^2 = \sum_{k\in \ZZ} \abs{c_k}^2, \qquad c_k \coloneqq {1\over 2\pi } \int_{(-\pi, \pi)} f(x) e^{-ikx} \dx.
$$

:::

[[PR-JCZKL]]

## Chebyshev, Minkowski, and Young

[[PR-YO7MV]]

[[PR-XUVZY]]

::: {.remark}
For $p=\infty$, $\abs{f+g}\leq\norm f_\infty+\norm g_\infty$ almost everywhere, so $\norm{f+g}_\infty\leq\norm f_\infty+\norm g_\infty$.
Together with the case $1\leq p<\infty$, Minkowski's inequality is the triangle inequality for $\norm{\wait}_p$, so $L^p$ is a normed space for $1\leq p\leq\infty$.

:::

[[PR-2C3SZ]]

::: {.remark title="Special cases of Young's convolution inequality"}
For conjugate exponents $p,q$ and $1\leq p\leq\infty$,
$$
\begin{aligned}
\norm{f\ast g}_1      & \leq \norm{f}_1 \norm{g}_1, \\
\norm{f\ast g}_p      & \leq \norm{f}_1 \norm{g}_p, \\
\norm{f\ast g}_\infty & \leq \norm{f}_p \norm{g}_q, \\
\norm{f\ast g}_\infty & \leq \norm{f}_2 \norm{g}_2.
\end{aligned}
$$

:::

## Elementary inequalities

[[PR-IQYTA]]

[[PR-W4ICW]]

[[PR-BPOH2]]

[[PR-7KTA6]]

[[FF-Z3E3C]]

[[PR-CHY3F]]

::: {.fact}
For $x,y\geq0$, $\sqrt{x + y} \leq \sqrt{x} + \sqrt{y}$, since $\qty{\sqrt x+\sqrt y}^2 = x+y+2\sqrt{xy}\geq x+y$.

:::
