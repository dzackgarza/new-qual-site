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

::: {.example title="Parseval's identity for Fourier series"}
For the orthonormal basis $\theset{e^{ikx}/\sqrt{2\pi}}_{k\in\ZZ}$ of $L^2(-\pi,\pi)$, Parseval's identity ([[T-5AALA]]) reads
$$
{1\over 2\pi} \int_{(-\pi, \pi)} \abs{f}^2 = \sum_{k\in \ZZ} \abs{c_k}^2, \qquad c_k \coloneqq {1\over 2\pi } \int_{(-\pi, \pi)} f(x) e^{-ikx} \dx.
$$

:::

[[PR-JCZKL]]

## Chebyshev, Minkowski, and Young

[[PR-YO7MV]]

[[PR-XUVZY]]

For $p=\infty$, the triangle inequality is the statement that $\norm{\cdot}_\infty$ is a norm on $L^\infty$ [@Fol99, Theorem 6.8(b)].

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

The inequality is the argument displayed, and it is also the case $p=2$ of the subadditivity of $t\mapsto t^p$ on $[0,\infty)$ for $p\geq1$; it is the comparison Rudin uses when he proves $\abs{x+y}\le\abs x+\abs y$ from the Schwarz inequality, [@Rud76, ch. 1, Theorem 1.35].
:::
