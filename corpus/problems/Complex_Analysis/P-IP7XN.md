---
schema: qual/card@1
id: P-IP7XN
kind: problem
title: $z\sin z=a$ has only real solutions
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Trigonometry
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The statement read "Show that z sin(z) = a has only real solutions" with no hypothesis on a. This is false for a < 0 (z = iy with y sinh y = -a) and for a larger than the maximum of x sin x on [0, pi] (the first hump then has no real root and the Rouché count forces non-real roots). The statement now assumes 0 < a <= 1. The earlier solution left the real-root count unproved; it was replaced by a complete proof.'
---

::: {.problem}
Let $0 < a \leq 1$.
Show that $z\sin(z) = a$ has only real solutions.
:::

::: {.solution}
Let $f(z) = z\sin z - a$, and for $m \geq 1$ let $R_m = (2m+\tfrac12)\pi$.

::: pf

::: {.pf-step #circle-bound}
On $\abs{z} = R_m$, $\abs{z\sin z} > 1 \geq a$.

::: pf-proof
Write $z = x+iy$, so $\abs{\sin z}^2 = \sin^2 x + \sinh^2 y$.
If $\abs{y} \geq 1$ then $\abs{\sin z}^2 \geq \sinh^2 1 > 1$.
If $\abs{y} < 1$ then $R_m - \abs{x} \leq R_m - \sqrt{R_m^2 - 1} \leq 1/R_m$, and $\sin^2 R_m = 1$, so $\sin^2 x \geq \cos^2(1/R_m) \geq \cos^2(2/\pi) > \tfrac12$.
In both cases $\abs{z\sin z} \geq R_m/\sqrt2 > 1$.
:::

:::

::: {.pf-step #zero-count}
$f$ has exactly $4m+2$ zeros in $\abs{z} < R_m$, counted with multiplicity.

::: pf-proof
By step [](#circle-bound){.pf-ref} and Rouché's theorem, $f$ and $z\sin z$ have the same number of zeros in $\abs{z} < R_m$.
The zeros of $z\sin z$ there are $0$, of order two, and the simple zeros $k\pi$ for $1 \leq \abs{k} \leq 2m$: $4m+2$ in all.
:::

:::

::: {.pf-step #real-count}
$f$ has at least $4m+2$ distinct real zeros in $(-R_m, R_m)$.

::: pf-proof
Let $g(x) = x\sin x$, which is even, so it suffices to find $2m+1$ distinct zeros of $g - a$ in $(0, R_m)$.
For $0 \leq k \leq m-1$, $g$ vanishes at $2k\pi$ and $(2k+1)\pi$ and $g((2k+\tfrac12)\pi) = (2k+\tfrac12)\pi > 1 \geq a$, so the intermediate value theorem gives a root of $g = a$ in each of $(2k\pi, (2k+\tfrac12)\pi)$ and $((2k+\tfrac12)\pi, (2k+1)\pi)$.
Also $g(2m\pi) = 0 < a < g(R_m)$ gives a root in $(2m\pi, R_m)$.
These $2m+1$ intervals are disjoint, and $0$ is not a root since $a \neq 0$.
:::

:::

::: pf-step
Every solution of $z\sin z = a$ is real.

::: pf-proof
Let $z_0$ be a solution and choose $m$ with $R_m > \abs{z_0}$.
By steps [](#zero-count){.pf-ref} and [](#real-count){.pf-ref}, the $4m+2$ real zeros found are all the zeros of $f$ in $\abs{z} < R_m$, so $z_0$ is one of them.
:::

:::

:::
:::
