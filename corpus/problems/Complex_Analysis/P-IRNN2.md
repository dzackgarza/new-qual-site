---
schema: qual/card@1
id: P-IRNN2
kind: problem
title: $\int_C \frac{dz}{f(z)-f(z_0)}=\frac{2\pi i}{f'(z_0)}$ for a small circle about
  a noncritical point
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Argument Principle
  - Zeros
  - Biholomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f$ be analytic on a region $R$ and suppose $f'(z_0) \neq 0$ for some $z_0 \in R$.
Show that if $C$ is a circle of sufficiently small radius centered at $z_0$, then
$$
\frac{2 \pi i}{f^{\prime}\left(z_{0}\right)}=\int_{C} \frac{d z}{f(z)-f\left(z_{0}\right)}
.$$
:::

::: {.hint}
Use the inverse function theorem.
:::

::: {.solution}
::: pf

::: {.pf-step #injective}
There is $r > 0$ with $\overline{D}(z_0, r) \subset R$ such that $z_0$ is the only zero of $f(z) - f(z_0)$ in $\overline{D}(z_0, r)$.

::: pf-proof
Since $f'(z_0) \neq 0$, the inverse function theorem gives a neighbourhood $U$ of $z_0$ on which $f$ is injective.
Take $r$ with $\overline{D}(z_0, r) \subset U$.
:::

:::

::: {.pf-step #residue}
$\frac{1}{f(z) - f(z_0)}$ has a simple pole at $z_0$ with residue $\frac{1}{f'(z_0)}$.

::: pf-proof
$f(z) - f(z_0) = (z - z_0)h(z)$ with $h$ holomorphic and $h(z_0) = f'(z_0) \neq 0$, so the residue is $1/h(z_0)$.
:::

:::

::: pf-step
For $C = \partial D(z_0, \rho)$ with $0 < \rho \leq r$, positively oriented,
$$
\int_{C} \frac{dz}{f(z)-f(z_0)} = \frac{2\pi i}{f'(z_0)}.
$$

::: pf-proof
By step [](#injective){.pf-ref} the integrand is holomorphic on a neighbourhood of $\overline{D}(z_0, \rho)$ except at $z_0$; the residue theorem and step [](#residue){.pf-ref} give the value.
:::

:::

:::
:::
