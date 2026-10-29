---
schema: qual/card@1
id: P-FOYTY
kind: problem
title: A power series may be re-expanded about any point of its disk of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be a power series centered at the origin.
Prove that $f$ has a power series expansion about any point in its disc of convergence.
:::

::: {.solution}
Suppose $f(z)=\sum_{n=0}^\infty a_nz^n$ has radius of convergence $R>0$, fix $z_0$ with $\abs{z_0}<R$, and set $\rho \coloneqq R-\abs{z_0}$ (with $\rho=\infty$ if $R=\infty$).

::: pf

::: {.pf-step #holomorphic}
$f$ is holomorphic on $\abs z<R$.

::: pf-proof
A power series is holomorphic inside its disk of convergence, and it may be differentiated term by term there.
:::

:::

::: pf-step
For $\abs{z-z_0}<\rho$, $f(z)=\sum_{k=0}^\infty \frac{f^{(k)}(z_0)}{k!}(z-z_0)^k$.

::: pf-proof
Fix $z$ with $\abs{z-z_0}<\rho$ and choose $s$ with $\abs{z-z_0}<s<\rho$. The closed disk $\abs{\zeta-z_0}\leq s$ lies in $\abs\zeta<R$, so by step [](#holomorphic){.pf-ref} and Cauchy's integral formula
$$
f(z) = \frac{1}{2\pi i}\int_{\abs{\zeta-z_0}=s}\frac{f(\zeta)}{\zeta-z}\,d\zeta.
$$
On the circle, $\abs{(z-z_0)/(\zeta-z_0)} = \abs{z-z_0}/s<1$, so
$$
\frac1{\zeta-z} = \sum_{k=0}^\infty \frac{(z-z_0)^k}{(\zeta-z_0)^{k+1}}
$$
converges uniformly in $\zeta$. Integrating term by term and using Cauchy's formula for derivatives, $\frac{1}{2\pi i}\int \frac{f(\zeta)}{(\zeta-z_0)^{k+1}}\,d\zeta = \frac{f^{(k)}(z_0)}{k!}$, gives the expansion.
:::

:::

:::

:::
