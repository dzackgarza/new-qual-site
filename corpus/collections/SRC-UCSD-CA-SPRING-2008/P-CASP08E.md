---
schema: qual/card@1
id: P-CASP08E
kind: problem
title: '$\int_0^\infty x\sin x/(x^2+a^2)\,dx$ by residues'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
For $a \in \RR$ compute the integral $$\int_0^{\infty} \frac{x\sin x}{x^2 + a^2}\,dx.$$ Be sure to show all your work and justify any limits.
:::

::: {.solution}

The computation is the card's own, by the standard semicircular contour with Jordan's lemma; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

The integrand extends to an even function of $x$ on $\RR$, so the integral over $[0,\infty)$ is half the integral over $\RR$. Let $a\ne0$, put $b=\abs{a}>0$ and $F(z)=\dfrac{ze^{iz}}{z^{2}+b^{2}}$; the case $a=0$ is treated separately at the end.

::: pf

::: {.pf-step #pole}
$F$ has a simple pole at $z=ib$ with $\operatorname{Res}_{z=ib}F=\tfrac12e^{-b}$, and no other pole in the upper half-plane.

::: pf-proof
$z^{2}+b^{2}=(z-ib)(z+ib)$, so the only poles of $F$ are $\pm ib$, and both are simple because the numerator does not vanish there: $ib\ne0$ and $-ib\ne0$. Only $ib$ lies in the upper half-plane. For a simple pole the residue is $\lim_{z\to ib}(z-ib)F(z)=\dfrac{ib\,e^{i\cdot ib}}{2ib}=\tfrac12e^{-b}$, since $e^{i\cdot ib}=e^{-b}$.
:::

:::

::: {.pf-step #arc}
$\displaystyle\lim_{R\to\infty}\int_{C_{R}}F(z)\,dz=0$, where $C_{R}$ is the upper semicircle of radius $R$ about $0$.

::: pf-proof
On $C_{R}$ one has $\abs{e^{iz}}=e^{-\operatorname{Im}z}\le1$ and
$$
\abs{\frac{z}{z^{2}+b^{2}}}\le\frac{R}{R^{2}-b^{2}}=:M_{R}
$$
for $R>b$, since $\abs{z^{2}+b^{2}}\ge\abs{z}^{2}-b^{2}$. As $M_{R}\to0$, Jordan's lemma (the form for a factor $e^{iz}$ with a bound $M_{R}\to0$ on the arc) gives $\abs{\int_{C_{R}}F}\le\pi M_{R}\to0$.
:::

:::

::: {.pf-step #line}
$\displaystyle\int_{-\infty}^{\infty}\frac{x\sin x}{x^{2}+b^{2}}\,dx=\pi e^{-b}$.

::: pf-proof
For $R>b$ the residue theorem on the positively oriented boundary of the upper half-disc gives
$$
\int_{-R}^{R}F(x)\,dx+\int_{C_{R}}F(z)\,dz=2\pi i\cdot\tfrac12e^{-b}=\pi ie^{-b},
$$
and step [](#arc){.pf-ref} lets $R\to\infty$, so $\int_{-\infty}^{\infty}\frac{xe^{ix}}{x^{2}+b^{2}}dx=\pi ie^{-b}$. Taking imaginary parts, the imaginary part of the left side being $\int_{-\infty}^{\infty}\frac{x\sin x}{x^{2}+b^{2}}dx$ and that of $\pi ie^{-b}$ being $\pi e^{-b}$, gives the display.
:::

:::

::: {.pf-step #answer}
$\displaystyle\int_{0}^{\infty}\frac{x\sin x}{x^{2}+a^{2}}\,dx=\boxed{\dfrac{\pi}{2}e^{-\abs{a}}}$ for every $a\in\RR$.

::: pf-proof
For $a\ne0$ the integrand is even, so the integral over $[0,\infty)$ is half the value of step [](#line){.pf-ref} with $b=\abs{a}$, giving $\frac{\pi}{2}e^{-\abs{a}}$. For $a=0$ the integrand is $\sin x/x$, and $\int_{0}^{\infty}\frac{\sin x}{x}dx=\frac{\pi}{2}$ is the Dirichlet integral, which is the value $\frac{\pi}{2}e^{0}$ predicted by the formula.
:::

:::

:::
:::
