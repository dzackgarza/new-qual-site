---
schema: qual/card@1
id: E-NKDKF
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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that if $f$ has a primitive $F$ on $\Omega$ then $\int_\gamma f = 0$ for every closed curve $\gamma \subseteq \Omega$.
:::

::: {.solution}

Curves are piecewise smooth.

::: pf

::: {.pf-step #ftc}
If $\gamma$ is a curve in $\Omega$ from $a$ to $b$, then $\int_\gamma f = F(b) - F(a)$.

::: pf-proof
Let $z\colon [t_0,t_n] \to \Omega$ parametrize $\gamma$, smooth on each interval of a partition $t_0 < t_1 < \cdots < t_n$.
By the chain rule, $\ddd{t}F(z(t)) = F'(z(t)) z'(t) = f(z(t)) z'(t)$ on each interval, so
$$
\int_\gamma f = \sum_{j=1}^n \int_{t_{j-1}}^{t_j} \ddd{t}F(z(t))\,dt = \sum_{j=1}^n \big(F(z(t_j)) - F(z(t_{j-1}))\big) = F(b) - F(a),
$$
since the sum telescopes.
:::

:::

::: pf-step
If $\gamma$ is closed, then $\int_\gamma f = 0$.

::: pf-proof
A closed curve has $b = a$, so step [](#ftc){.pf-ref} gives $\int_\gamma f = F(a) - F(a) = 0$.
:::

:::

:::

:::
