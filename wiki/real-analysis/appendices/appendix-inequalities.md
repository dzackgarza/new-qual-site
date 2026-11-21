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

This is the case $p=\frac12$ of the subadditivity of $t\mapsto t^p$ on $[0,\infty)$: $(x+y)^p\leq x^p+y^p$ holds for every $0<p\leq1$ and fails for every $p>1$, where subadditivity at $x=y=1$ would read $2^p\leq2$.
For $p\geq1$ the correct companion is the convexity estimate $(x+y)^p\leq2^{p-1}\qty{x^p+y^p}$, which is equality at $p=1$.
Rudin's derivation of $\abs{x+y}\leq\abs x+\abs y$ uses neither: [@Rud76, ch. 1, Theorem 1.35] is the Schwarz inequality, [@Rud76, ch. 1, Theorem 1.37(e)] is the triangle inequality, and its proof squares $\abs{x+y}$ and compares it with $\qty{\abs x+\abs y}^2$.
:::
