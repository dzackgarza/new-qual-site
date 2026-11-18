---
schema: qual/card@1
id: P-BKF09-5B
kind: problem
title: Solution of $xy'+y=y^2$ with $y(1)=2$
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's separation argument into numbered steps and added the verification that
    the separated solution solves the equation, since the divisions in the separation require y !=
    0,1 and x != 0; the resulting function is checked directly. Checked: the factorization of
    1/(y^2-y), the integration, the constant from y(1)=2 and the differentiation of 2x/(2-x). Not
    checked against a printed source: the Berkeley preliminary examinations are not retained in
    tmp/sources and the card records no page.
---

::: {.problem}
Solve the differential equation
$$
xy'+y=y^2
$$
with initial condition $y(1)=2$.
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here the equation is $xy'+y=y^{2}$ with $y(1)=2$; note $xy'+y=(xy)'$, and on an interval where $y\neq0,1$ the separated form is available.

::: pf

::: {.pf-step #deriv}

$(xy)'=y^{2}$.

::: pf-proof

$(xy)'=xy'+y$ by the product rule, and the equation says this equals $y^{2}$.

:::

:::

::: {.pf-step #sep}

Formally separating, $\frac{dy}{y^{2}-y}=\frac{dx}{x}$.

::: pf-proof

From step [](#deriv){.pf-ref}, $x\frac{dy}{dx}=y^{2}-y$; dividing by $x(y^{2}-y)$ gives the displayed form (the division is legitimate where $x\neq0$, $y\neq0,1$).

:::

:::

::: {.pf-step #integrate}

$\int\frac{dy}{y^{2}-y}=\log(y-1)-\log y$, hence $\log x=\log(y-1)-\log y+c$.

::: pf-proof

$\frac{1}{y^{2}-y}=\frac{1}{y-1}-\frac1y$, whose integral is $\log(y-1)-\log y$; integrating both sides of step [](#sep){.pf-ref} gives $\log x$ on the left up to the constant $c$.

:::

:::

::: {.pf-step #solve}

$y=\frac{1}{1-Kx}$ for a constant $K$.

::: pf-proof

Exponentiating step [](#integrate){.pf-ref} gives $x=e^{c}\frac{y-1}{y}$, that is $\frac{y-1}{y}=Kx$ with $K=e^{-c}$; solving, $1-\frac1y=Kx$ and $y=\frac{1}{1-Kx}$.

:::

:::

::: {.pf-step #ivp}

$y(1)=2$ forces $K=\tfrac12$, so $y=\frac{2}{2-x}$.

::: pf-proof

At $x=1$: $2=\frac{1}{1-K}$, so $1-K=\frac12$ and $K=\frac12$; hence $y=\frac{1}{1-x/2}=\frac{2}{2-x}$.

:::

:::

::: {.pf-step #done}

$y=\frac{2}{2-x}$ solves the equation with $y(1)=2$ on the interval containing $1$ where $2-x\neq0$.

::: pf-proof

On that interval $y$ is differentiable, $y(1)=2$ by step [](#ivp){.pf-ref}, and $xy'+y=(xy)'$ with $xy=\frac{2x}{2-x}$, whose derivative is $\frac{2(2-x)+2x}{(2-x)^{2}}=\frac{4}{(2-x)^{2}}=y^{2}$; the computation verifies the separated solution and avoids relying on the divisions of steps [](#sep){.pf-ref} to [](#solve){.pf-ref}.

:::

:::

:::

:::
