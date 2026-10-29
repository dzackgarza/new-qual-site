---
schema: qual/card@1
id: E-DUMQG
kind: problem
title: Laurent series of $\frac{1}{(z-3)(z-1)}$ on the three annuli about $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Principal Parts
  - Residues
relations: []
review: draft
---

::: {.exercise}
Find a Laurent expansion for $f(z) \coloneqq {1\over (z-3)(z-1)}$ on the 3 annular regions centered at $0$ where $f$ is holomorphic.

![](../../assets/Complex_Analysis/010_Basics/figures/2021-12-19_22-39-19.png)

:::

::: {.solution}
The poles of $f$ are $1$ and $3$, so the three annuli centered at $0$ on which $f$ is holomorphic are $0\le\abs z<1$, $1<\abs z<3$ and $3<\abs z<\infty$.

::: pf

::: {.pf-step #partial-fractions}
$f(z)=\frac{-1/2}{z-1}+\frac{1/2}{z-3}$.

::: pf-proof
$\Res_{z=1}f=\frac1{z-3}\evalfrom_{z=1}=-\frac12$ and $\Res_{z=3}f=\frac1{z-1}\evalfrom_{z=3}=\frac12$; $f$ minus these two principal parts is entire and tends to $0$ at $\infty$, so it is $0$ by Liouville's theorem.
:::

:::

::: {.pf-step #term-expansions}
The two terms have the geometric expansions
$$
\begin{aligned}
\frac{-1/2}{z-1}&=\frac12\sum_{k\ge0}z^k && \abs z<1,\\
\frac{-1/2}{z-1}&=-\frac1{2z}\cdot\frac1{1-z^{-1}}=-\frac12\sum_{k\ge0}z^{-k-1} && \abs z>1,\\
\frac{1/2}{z-3}&=-\frac16\cdot\frac1{1-z/3}=-\frac16\sum_{k\ge0}3^{-k}z^k && \abs z<3,\\
\frac{1/2}{z-3}&=\frac1{2z}\cdot\frac1{1-3z^{-1}}=\frac12\sum_{k\ge0}3^kz^{-k-1} && \abs z>3.
\end{aligned}
$$

::: pf-proof
Each is the geometric series $\frac1{1-w}=\sum_{k\ge0}w^k$ for $\abs w<1$.
:::

:::

::: pf-step
The Laurent expansions are
$$
\boxed{
\begin{aligned}
0\le\abs z<1:&\quad f(z)=\frac12\sum_{k\ge0}z^k-\frac16\sum_{k\ge0}3^{-k}z^k,\\
1<\abs z<3:&\quad f(z)=-\frac12\sum_{k\ge0}z^{-k-1}-\frac16\sum_{k\ge0}3^{-k}z^k,\\
3<\abs z<\infty:&\quad f(z)=-\frac12\sum_{k\ge0}z^{-k-1}+\frac12\sum_{k\ge0}3^kz^{-k-1}.
\end{aligned}}
$$

::: pf-proof
On each annulus, substitute into step [](#partial-fractions){.pf-ref} the expansions of step [](#term-expansions){.pf-ref} that converge there.
:::

:::

:::

:::
