---
schema: qual/card@1
id: P-EMHMR
kind: problem
title: Uniqueness of Laurent series coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Prove that if a function $f$ has two Laurent series expansions in an annulus $A = \{z \in \CC \mid r < \abs{z-a} < R\}$:
$$f(z) = \sum_{n=-\infty}^\infty c_n(z-a)^n \quad\text{and}\quad f(z) = \sum_{n=-\infty}^\infty c_n'(z-a)^n$$
then $c_n = c_n'$ for all $n \in \ZZ$.
:::

::: {.solution}

Fix $\rho$ with $r<\rho<R$, let $\gamma(t)\coloneqq a+\rho e^{it}$ for $0\le t\le2\pi$, and for $k\in\ZZ$ let
$$
I_k\coloneqq\frac1{2\pi i}\int_\gamma\frac{f(z)}{(z-a)^{k+1}}\,dz.
$$

::: pf

::: {.pf-step #monomials}
For every $m\in\ZZ$, $\frac1{2\pi i}\int_\gamma(z-a)^m\,dz$ is $1$ if $m=-1$ and $0$ otherwise.

::: pf-proof
$\frac1{2\pi i}\int_0^{2\pi}\rho^{m+1}e^{i(m+1)t}\,i\,dt=\frac{\rho^{m+1}}{2\pi}\int_0^{2\pi}e^{i(m+1)t}\,dt$.
:::

:::

::: {.pf-step #coefficient}
$I_k=c_k$.

::: pf-proof
A Laurent series converges uniformly on each circle in its annulus of convergence, so the first expansion may be integrated term by term on $\gamma$: $I_k=\sum_{n\in\ZZ}c_n\frac1{2\pi i}\int_\gamma(z-a)^{n-k-1}\,dz$.
By step [](#monomials){.pf-ref}, only $n=k$ contributes.
:::

:::

::: pf-step
$c_k=c_k'$ for every $k\in\ZZ$.

::: pf-proof
Step [](#coefficient){.pf-ref} applied to each expansion gives $c_k=I_k=c_k'$.
:::

:::

:::

:::
