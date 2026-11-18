---
schema: qual/card@1
id: P-F10AT
kind: problem
title: $x-x^3/3 \le \arctan x \le x$ for $x\ge 0$
classification:
  areas:
  - prelim
  topics:
  - Inequalities
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the pointwise
    pair 1 - t^2 <= 1/(1+t^2) <= 1 (the left by t^4/(1+t^2)), the integral identity
    arctan x = int_0^x dt/(1+t^2), monotonicity of the integral, and the resulting
    two-sided bound for x >= 0. The identity used for the middle term and the monotonicity
    step were implicit in the prose. The collection's provenance is the examination paper
    only, so no retained solution set covers the exercise and the argument is the card's
    own.
---

::: {.problem}
Prove that $x - \frac{x^3}{3} \le \arctan x \le x$ for all $x \ge 0$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #pointwise}
For every $t\ge0$,
$$
1-t^2\le\frac{1}{1+t^2}\le1 .
$$

::: pf-proof
The right inequality holds because $1+t^2\ge1$, both sides being positive. For the left one,
$$
\frac{1}{1+t^2}-(1-t^2)=\frac{1-(1-t^4)}{1+t^2}=\frac{t^4}{1+t^2}\ge0 .
$$
:::

:::

::: {.pf-step #arctan-integral}
$\arctan x=\int_0^x\frac{dt}{1+t^2}$ for every $x\ge0$.

::: pf-proof
The integrand is continuous on $[0,x]$, and $\arctan$ is its antiderivative vanishing at $0$, so the fundamental theorem of calculus gives the identity.
:::

:::

::: {.pf-step #monotonicity}
If $p(t)\le q(t)$ for all $t$ in $[0,x]$ with $x\ge0$, then $\int_0^xp\le\int_0^xq$.

::: pf-proof
The function $t\mapsto q(t)-p(t)$ is nonnegative on the interval, and the integral of a nonnegative function over an interval is nonnegative.
:::

:::

::: {.pf-step}
For every $x\ge0$,
$$
x-\frac{x^3}{3}\le\arctan x\le x .
$$

::: pf-proof
Integrate the two inequalities of step [](#pointwise){.pf-ref} over $[0,x]$, which step [](#monotonicity){.pf-ref} permits for $x\ge0$:
$$
\int_0^x(1-t^2)\,dt\le\int_0^x\frac{dt}{1+t^2}\le\int_0^x1\,dt ,
$$
that is
$$
\boxed{x-\frac{x^3}{3}\le\arctan x\le x},
$$
the middle term being $\arctan x$ by step [](#arctan-integral){.pf-ref} and the outer two being $x-\frac{x^3}{3}$ and $x$.
:::

:::

:::
:::
