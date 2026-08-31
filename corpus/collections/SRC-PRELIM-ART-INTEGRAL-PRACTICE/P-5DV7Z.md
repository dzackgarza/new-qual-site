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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
12. $\displaystyle \int \frac {x}{x^2+9} ~dx = \color{blue} {\frac 1 2 \ln(x^2 + 9)}$

- **Solution:** $u = x^2 + 9$, $du = 2x ~dx$

- **Solution:** $\frac {x}{x^2+9} ~dx = \frac {1}{2} \cdot \frac {1}{u} ~du$

- **Used 2018**
:::

::: {.solution}
**Goal:** Evaluate the indefinite integral $\int \frac{x}{x^2+9} \, dx$.

<1>1. Make the substitution $u = x^2 + 9$.
Then $du = 2x \, dx \implies x \, dx = \frac{1}{2} \, du$.
::: {.proof}
The substitution rule for indefinite integrals states that if $u = g(x)$ is differentiable and $F$ is an antiderivative of $f$, then $\int f(g(x))\, g'(x)\, dx = F(g(x)) + C$. Here $g(x) = x^2 + 9$ is differentiable for all $x$ with $g'(x) = 2x$, and $f(u) = 1/u$ with antiderivative $F(u) = \ln|u|$, so the substitution $u = x^2 + 9$ is valid.
:::

<1>2. Rewrite and evaluate the integral: $$\int \frac{x}{x^2+9} \, dx = \int \frac{1}{u} \left(\frac{1}{2} \, du\right) = \frac{1}{2} \int \frac{1}{u} \, du = \frac{1}{2} \ln|u| + C.$$
::: {.proof}
<2>1. From <1>1, $x\,dx = \frac{1}{2}\,du$, so $\frac{x}{x^2+9}\,dx = \frac{1}{u}\cdot\frac{1}{2}\,du$.
<2>2. The constant factor $\frac{1}{2}$ pulls out of the integral.
<2>3. The antiderivative of $\frac{1}{u}$ is $\ln|u|$, so $\frac{1}{2}\int\frac{1}{u}\,du = \frac{1}{2}\ln|u| + C$.
:::

<1>3. Substitute back $u = x^2 + 9$: Since $x^2 + 9 > 0$ for all $x \in \mathbb{R}$, $|u| = x^2 + 9$, so: $$\int \frac{x}{x^2+9} \, dx = \frac{1}{2} \ln(x^2+9) + C.$$
::: {.proof}
<2>1. Replacing $u$ by $x^2 + 9$ in $\frac{1}{2}\ln|u| + C$ gives $\frac{1}{2}\ln(x^2+9) + C$.
<2>2. The absolute value is dropped because $x^2 + 9 > 0$ for every real $x$.
:::
:::
