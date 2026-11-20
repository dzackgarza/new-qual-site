---
schema: qual/card@1
id: P-4GVRD
kind: problem
title: $\int\sqrt{4-x}\,dx$
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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The three sub-steps of the transformation were the card's only steps with no proof body;
    each now carries one: the substitution producing $u^{1/2}(-du)$, the constant-multiple rule
    for the factor $-1$, and the power rule at $p=1/2$ with the division by $3/2$ written out.
    The integrand, the antiderivative $-\\frac23(4-x)^{3/2}+C$ and the statement are unchanged.
---

::: {.problem}
Evaluate
$$
\int\sqrt{4-x}\,dx.
$$
:::

::: {.solution}
Take $x \le 4$.

::: pf

::: {.pf-step #s1}

Make the substitution $u = 4 - x$.
Then $du = -dx \implies dx = -du$.

::: pf-proof

The substitution rule for indefinite integrals states that if $u = g(x)$ is differentiable and $F$ is an antiderivative of $f$, then $\int f(g(x))\, g'(x)\, dx = F(g(x)) + C$. Here $g(x) = 4 - x$ with $g'(x) = -1$, and $f(u) = u^{1/2}$, so the substitution is valid.

:::

:::

::: {.pf-step #s2}

Transform and evaluate the integral: $$\int \sqrt{4-x} \, dx = \int u^{1/2} (-du) = -\int u^{1/2} \, du = -\frac{2}{3} u^{3/2} + C.$$

::: pf-proof

::: pf-step

The substitution $u = 4 - x$ from step [](#s1){.pf-ref} gives $dx = -du$, so $\sqrt{4-x}\,dx = u^{1/2}(-du)$.

::: pf-proof
With $u=4-x$ we have $x=4-u$, so $\sqrt{4-x}=\sqrt{u}=u^{1/2}$, and the differential is $dx=-du$ by step [](#s1){.pf-ref}; substituting both into the integrand gives $\sqrt{4-x}\,dx=u^{1/2}(-du)$.
:::

:::

::: pf-step

The constant factor $-1$ pulls out of the integral: $\int u^{1/2}(-du) = -\int u^{1/2}\,du$.

::: pf-proof
For a constant $c$ and an integrable function $h$, $\int c\,h(u)\,du=c\int h(u)\,du$; take $c=-1$ and $h(u)=u^{1/2}$.
:::

:::

::: pf-step

The power rule $\int u^p\,du = \frac{u^{p+1}}{p+1} + C$ applies with $p = 1/2$, giving $-\frac{u^{3/2}}{3/2} + C = -\frac{2}{3}u^{3/2} + C$.

::: pf-proof
$p=1/2\ne-1$, so the power rule applies with $p+1=3/2$; dividing by $3/2$ is multiplying by $2/3$, and the overall sign is the one carried from step 2.2.
:::

:::

:::

:::

::: pf-step

Substitute back $u = 4-x$: $$\int \sqrt{4-x} \, dx = -\frac{2}{3} (4-x)^{3/2} + C.$$

::: pf-proof

Replacing $u$ by $4 - x$ in the antiderivative $-\frac{2}{3}u^{3/2} + C$ from step [](#s2){.pf-ref} yields $-\frac{2}{3}(4-x)^{3/2} + C$.

:::

:::

:::

:::
