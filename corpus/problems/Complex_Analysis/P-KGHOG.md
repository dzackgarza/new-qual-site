---
schema: qual/card@1
id: P-KGHOG
kind: problem
title: The Fourier transform of a compactly supported continuous function is entire
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Integrals
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Suppose that $f: \RR\to\RR$ is a continuous function that vanishes outside of some finite interval.
For each $z\in \CC$, define
$$
g(z) = \int_{-\infty}^\infty f(t) e^{-izt} \,dt
.$$

Show that $g$ is entire.
:::

::: {.solution}
Choose $R>0$ with $f(t)=0$ for $\abs{t}>R$, and let $A = \int_{-R}^R \abs{f(t)}\,dt$.

::: pf

::: {.pf-step #series}
For every $z \in \CC$,
$$
g(z)=\sum_{n=0}^\infty c_n z^n, \qquad c_n = \frac{(-i)^n}{n!}\int_{-R}^R t^n f(t)\,dt.
$$

::: pf-proof
For fixed $z$, the series $e^{-izt} = \sum_n \frac{(-izt)^n}{n!}$ converges uniformly in $t \in [-R,R]$, by the Weierstrass M-test with bounds $\frac{(\abs{z}R)^n}{n!}$.
So it may be multiplied by the bounded function $f$ and integrated term by term over $[-R,R]$.
:::

:::

::: pf-step
$g$ is entire.

::: pf-proof
$\abs{c_n} \leq \frac{R^n A}{n!}$, so the power series of step [](#series){.pf-ref} has infinite radius of convergence.
:::

:::

:::
:::
