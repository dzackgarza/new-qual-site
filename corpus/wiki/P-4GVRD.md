---
schema: qual/card@1
id: P-4GVRD
kind: problem
title: Evaluate $\int\sqrt{4-x}\,dx$
classification:
  areas:
  - prelim
  topics:
  - integrals
  - u-substitution
relations: []
review: draft
solved: true
---

::: problem
10. $\displaystyle \int \sqrt {4-x} ~dx = \color{blue} {- \frac {2}{3}(4-x)^{\frac {3}{2}}}$

- **Solution:** $u = 4 - x$, $du = - ~dx$

- **Solution:** $\sqrt {4-x} ~dx = - u^{\frac {1}{2}} ~du$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Evaluate the indefinite integral $\int \sqrt{4-x} \, dx$ for $x \le 4$.

<1>1. Make the substitution $u = 4 - x$.
Then $du = -dx \implies dx = -du$.
Proof: By the standard substitution rule for indefinite integrals.

<1>2. Transform and evaluate the integral: $$\int \sqrt{4-x} \, dx = \int u^{1/2} (-du) = -\int u^{1/2} \, du = -\frac{2}{3} u^{3/2} + C.$$ Proof: By the power rule for integration $\int u^p \, du = \frac{u^{p+1}}{p+1} + C$ with $p = 1/2$.

<1>3. Substitute back $u = 4-x$: $$\int \sqrt{4-x} \, dx = -\frac{2}{3} (4-x)^{3/2} + C.$$ Proof: Follows directly from <1>1 and <1>2. Q.E.D.
:::
