---
schema: qual/card@1
id: P-5DV7Z
kind: problem
title: Evaluate $\int\frac{x}{x^2+9}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
relations: []
review: draft
---

::: problem
12. $\displaystyle \int \frac {x}{x^2+9} ~dx = \color{blue} {\frac 1 2 \ln(x^2 + 9)}$

- **Solution:** $u = x^2 + 9$, $du = 2x ~dx$

- **Solution:** $\frac {x}{x^2+9} ~dx = \frac {1}{2} \cdot \frac {1}{u} ~du$

- **Used 2018**
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Evaluate the indefinite integral $\int \frac{x}{x^2+9} \, dx$.

<1>1. Make the substitution $u = x^2 + 9$.
Then $du = 2x \, dx \implies x \, dx = \frac{1}{2} \, du$.
Proof: $x^2 + 9$ is differentiable for all $x \in \mathbb{R}$, with derivative $2x$.

<1>2. Rewrite and evaluate the integral: $$\int \frac{x}{x^2+9} \, dx = \int \frac{1}{u} \left(\frac{1}{2} \, du\right) = \frac{1}{2} \int \frac{1}{u} \, du = \frac{1}{2} \ln|u| + C.$$ Proof: By the basic integration formula $\int \frac{1}{u} \, du = \ln|u| + C$.

<1>3. Substitute back $u = x^2 + 9$: Since $x^2 + 9 > 0$ for all $x \in \mathbb{R}$, $|u| = x^2 + 9$, so: $$\int \frac{x}{x^2+9} \, dx = \frac{1}{2} \ln(x^2+9) + C.$$ Proof: Follows from <1>1 and <1>2. Q.E.D.
:::
