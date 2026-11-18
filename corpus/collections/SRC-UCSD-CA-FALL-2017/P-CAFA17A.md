---
schema: qual/card@1
id: P-CAFA17A
kind: problem
title: '$\int_0^\infty (\log x)^2/(1+x^2)\,dx$ by residues'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Using the calculus of residues, compute $\int_0^{\infty} \frac{\log^2 x}{1 + x^2}\,dx$.

You may wish to use the contour consisting of two half circles in the upper half plane, one of small radius and another of large radius, connected by two line segments along the real axis.
:::

::: {.solution}

The computation is the card's own, on the indented upper-half-plane contour with a branch of the logarithm; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Take the branch $\Log$ of the logarithm on $\CC\setminus[0,\infty)$ given by $0<\arg z<\pi$, so that $\Log x=\log x$ for $x>0$ and $\Log(-x)=\log x+i\pi$ for $x>0$. Put $F(z)=(\Log z)^{2}/(1+z^{2})$ and, for $0<\varepsilon<R$, let $\Gamma$ be the boundary of the region $\{\varepsilon<\abs{z}<R,\ \operatorname{Im}z>0\}$ traversed positively: the segment from $\varepsilon$ to $R$, the large semicircle $C_{R}$, the segment from $-R$ to $-\varepsilon$, and the small semicircle $C_{\varepsilon}$.

::: pf

::: {.pf-step #log-integral}
$\displaystyle I_{1}=\int_{0}^{\infty}\frac{\log x}{1+x^{2}}\,dx=0$ and $\displaystyle\int_{0}^{\infty}\frac{dx}{1+x^{2}}=\frac{\pi}{2}$.

::: pf-proof
The substitution $x=1/t$ gives $dx=-dt/t^{2}$ and $1/(1+x^{2})=t^{2}/(1+t^{2})$, so
$$
I_{1}=\int_{\infty}^{0}\frac{-\log t}{1+t^{2}}\cdot\frac{t^{2}}{t^{2}}\,(-dt)=-\int_{0}^{\infty}\frac{\log t}{1+t^{2}}\,dt=-I_{1},
$$
which forces $I_{1}=0$; the integrand is absolutely integrable since $\abs{\log x}\le x+x^{-1/2}$-type bounds give $\int_{0}^{\infty}\abs{\log x}/(1+x^{2})\,dx<\infty$. The second integral is $\arctan x$ evaluated at $\infty$ and $0$, that is $\pi/2$.
:::

:::

::: {.pf-step #arcs}
The contributions of $C_{R}$ and $C_{\varepsilon}$ to $\int_{\Gamma}F$ tend to $0$.

::: pf-proof
On $C_{R}$ one has $\abs{\Log z}\le\log R+\pi$ and $\abs{1+z^{2}}\ge R^{2}-1$, so $\abs{F}\le(\log R+\pi)^{2}/(R^{2}-1)$ and the integral is bounded by $\pi R(\log R+\pi)^{2}/(R^{2}-1)\to0$. On $C_{\varepsilon}$ one has $\abs{\Log z}\le\abs{\log\varepsilon}+\pi$ and $\abs{1+z^{2}}\ge1-\varepsilon^{2}$, so the integral is bounded by $\pi\varepsilon(\abs{\log\varepsilon}+\pi)^{2}\to0$.
:::

:::

::: {.pf-step #real-axis}
The two real-axis pieces tend to $\displaystyle 2I_{2}-\frac{\pi^{3}}{2}$.

::: pf-proof
On the positive segment $\Log x=\log x$ and the traversal is from $\varepsilon$ to $R$; on the negative segment $z=-x$ with $x$ running from $R$ down to $\varepsilon$, so $\Log z=\log x+i\pi$ and the traversal contributes $-\int_{R}^{\varepsilon}$, that is $+\int_{\varepsilon}^{R}$, of $(\log x+i\pi)^{2}/(1+x^{2})$. Hence the sum of the two pieces is
$$
\int_{\varepsilon}^{R}\frac{(\log x)^{2}+(\log x+i\pi)^{2}}{1+x^{2}}\,dx
=\int_{\varepsilon}^{R}\frac{2\log^{2}x+2i\pi\log x-\pi^{2}}{1+x^{2}}\,dx,
$$
which tends to $2I_{2}+2i\pi I_{1}-\pi^{2}\cdot\frac{\pi}{2}=2I_{2}-\frac{\pi^{3}}{2}$ by step [](#log-integral){.pf-ref}, the integrands being integrable on $(0,\infty)$ and the $\Log$ on the small circle bounded as in step [](#arcs){.pf-ref}.
:::

:::

::: {.pf-step #residue}
$\operatorname{Res}_{z=i}F=\dfrac{\pi^{2}i}{8}$.

::: pf-proof
$1+z^{2}=(z-i)(z+i)$, so $F$ has a simple pole at $i$, the only singularity in the upper half-plane, and
$$
\operatorname{Res}_{z=i}F=\frac{(\Log i)^{2}}{2i}=\frac{(i\pi/2)^{2}}{2i}=\frac{-\pi^{2}/4}{2i}=\frac{\pi^{2}i}{8},
$$
since $1/i=-i$.
:::

:::

::: {.pf-step #answer}
$\displaystyle\int_{0}^{\infty}\frac{\log^{2}x}{1+x^{2}}\,dx=\boxed{\dfrac{\pi^{3}}{8}}$.

::: pf-proof
The residue theorem on $\Gamma$ gives
$$
\int_{\Gamma}F=2\pi i\cdot\frac{\pi^{2}i}{8}=-\frac{\pi^{3}}{4},
$$
and the boundary integral is the sum of the two real-axis pieces with the two semicircles, so by steps [](#arcs){.pf-ref} and [](#real-axis){.pf-ref}, letting $\varepsilon\to0$ and $R\to\infty$,
$$
2I_{2}-\frac{\pi^{3}}{2}=-\frac{\pi^{3}}{4},
$$
whence $2I_{2}=\frac{\pi^{3}}{4}$ and $I_{2}=\frac{\pi^{3}}{8}$.
:::

:::

:::
:::
