---
title: Common inequalities
order: 23
---

# Common inequalities

## Cauchy--Schwarz, Hölder, and Plancherel

[[PR-X5D4Z]]

[[PR-IJOPU]]

[[PR-7BGSE]]

[[FT-GQRV2]]

[[T-4BDE3]]

[[T-5AALA]]

::: {.remark title="Parseval's identity for Fourier series"}
For the orthonormal basis $\theset{e^{ikx}/\sqrt{2\pi}}_{k\in\ZZ}$ of $L^2(-\pi,\pi)$, Parseval's identity ([[T-5AALA]]) reads
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
