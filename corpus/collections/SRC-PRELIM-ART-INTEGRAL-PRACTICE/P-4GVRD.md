---
schema: qual/card@1
id: P-4GVRD
kind: problem
title: Evaluate $\int\sqrt{4-x}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
10. $\displaystyle \int \sqrt {4-x} ~dx = \color{blue} {- \frac {2}{3}(4-x)^{\frac {3}{2}}}$

- **Solution:** $u = 4 - x$, $du = - ~dx$

- **Solution:** $\sqrt {4-x} ~dx = - u^{\frac {1}{2}} ~du$
:::

::: {.solution}
**Goal:** Evaluate the indefinite integral $\int \sqrt{4-x} \, dx$ for $x \le 4$.

<1>1. Make the substitution $u = 4 - x$.
Then $du = -dx \implies dx = -du$.
::: {.proof}
The substitution rule for indefinite integrals states that if $u = g(x)$ is differentiable and $F$ is an antiderivative of $f$, then $\int f(g(x))\, g'(x)\, dx = F(g(x)) + C$. Here $g(x) = 4 - x$ with $g'(x) = -1$, and $f(u) = u^{1/2}$, so the substitution is valid.
:::

<1>2. Transform and evaluate the integral: $$\int \sqrt{4-x} \, dx = \int u^{1/2} (-du) = -\int u^{1/2} \, du = -\frac{2}{3} u^{3/2} + C.$$
::: {.proof}
<2>1. The substitution $u = 4 - x$ from <1>1 gives $dx = -du$, so $\sqrt{4-x}\,dx = u^{1/2}(-du)$.
<2>2. The constant factor $-1$ pulls out of the integral: $\int u^{1/2}(-du) = -\int u^{1/2}\,du$.
<2>3. The power rule $\int u^p\,du = \frac{u^{p+1}}{p+1} + C$ applies with $p = 1/2$, giving $-\frac{u^{3/2}}{3/2} + C = -\frac{2}{3}u^{3/2} + C$.
:::

<1>3. Substitute back $u = 4-x$: $$\int \sqrt{4-x} \, dx = -\frac{2}{3} (4-x)^{3/2} + C.$$
::: {.proof}
Replacing $u$ by $4 - x$ in the antiderivative $-\frac{2}{3}u^{3/2} + C$ from <1>2 yields $-\frac{2}{3}(4-x)^{3/2} + C$.
:::
:::
