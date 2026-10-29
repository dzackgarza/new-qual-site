---
schema: qual/card@1
id: P-IF6H2
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx$ for $0<a<n$ and $\int_0^\infty\frac{\log
  x}{(1+x^2)^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---


::: {.problem}
Compute the following integrals:

(a) $\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$, $0< a < n$

(b) $\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2}\, dx$
:::

::: {.solution}
::: pf

::: {.pf-step #mellin}
For $0<s<1$, $\displaystyle\int_0^\infty\frac{u^{s-1}}{1+u}\,du = \frac{\pi}{\sin\pi s}$.

::: pf-proof
Integrate $z^{s-1}/(1+z)$, with $0<\arg z<2\pi$, over a keyhole contour around the positive real axis. The small and large arcs contribute $0$ in the limit because $0<s<1$, the two banks contribute $(1-e^{2\pi i s})$ times the integral, and the residue at $-1$ is $e^{i\pi(s-1)}$. Hence the integral is $\frac{2\pi i e^{i\pi(s-1)}}{1-e^{2\pi is}} = \frac{\pi}{\sin\pi s}$.
:::

:::

::: pf-step
(a) $\displaystyle\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx = \boxed{\frac{\pi}{n\sin(\pi a/n)}}$.

::: pf-proof
The substitution $u=x^n$ gives $\frac1n\int_0^\infty\frac{u^{a/n-1}}{1+u}\,du$, and $0<a/n<1$; apply step [](#mellin){.pf-ref} with $s=a/n$.
:::

:::

::: pf-step
(b) $\displaystyle\int_0^\infty\frac{\log x}{(1+x^2)^2}\,dx = \boxed{-\frac\pi4}$.

::: pf-proof
Call the integral $J$; it converges absolutely. The substitution $x=1/t$ gives $J=-\int_0^\infty\frac{t^2\log t}{(1+t^2)^2}\,dt$. Adding the two expressions,
$$
2J=\int_0^\infty\log x\,\frac{1-x^2}{(1+x^2)^2}\,dx.
$$
Since $\frac{d}{dx}\frac{x}{1+x^2}=\frac{1-x^2}{(1+x^2)^2}$, integration by parts gives
$$
2J=\left[\frac{x\log x}{1+x^2}\right]_0^\infty-\int_0^\infty\frac{dx}{1+x^2}=-\frac\pi2,
$$
because the boundary term vanishes at both endpoints.
:::

:::

:::

:::
