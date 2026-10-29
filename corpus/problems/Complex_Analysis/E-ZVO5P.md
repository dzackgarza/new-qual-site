---
schema: qual/card@1
id: E-ZVO5P
kind: problem
title: Primitives imply vanishing integral
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Cauchy Integral Theorem
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ has a primitive $F$ on $\Omega$ then $\displaystyle\int_\gamma f = 0$ for every closed curve $\gamma \subseteq \Omega$.

:::

::: {.solution}

Let $z:[a,b]\to\Omega$ be a piecewise-smooth parametrization of $\gamma$, so $z(a)=z(b)$, and let $F'=f$ on $\Omega$.

::: pf

::: {.pf-step #chain-rule}
$\frac{d}{dt}F(z(t)) = f(z(t))\,z'(t)$ at every $t$ where $z$ is differentiable.

::: pf-proof
This is the chain rule, since $F$ is complex differentiable with $F'=f$.
:::

:::

::: pf-step
$\int_\gamma f = 0$.

::: pf-proof
By step [](#chain-rule){.pf-ref} and the fundamental theorem of calculus on each smooth piece,
$$
\int_\gamma f(z)\dz = \int_a^b f(z(t))\,z'(t)\dt = F(z(b))-F(z(a)) = 0.
$$
:::

:::

:::

:::
