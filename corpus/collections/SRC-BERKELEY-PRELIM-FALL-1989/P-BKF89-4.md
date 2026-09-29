---
schema: qual/card@1
id: P-BKF89-4
kind: problem
title: $\abs{f(z)}\le(1-\abs{z})^{-1}$ on the unit disk implies $\abs{f'(0)}\le4$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f$ be analytic in $|z|<1$ and suppose
\[
|f(z)|\le\frac1{1-|z|}.
\]
Show that
\[
|f'(0)|\le4.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $0<r<1$,
$$
|f'(0)|
\leq
\frac{1}{r(1-r)}.
$$

::: pf-proof

On the circle $|z|=r$, the hypothesis gives
$$
|f(z)|
\leq
\frac1{1-r}.
$$
By Cauchy's estimate for the first derivative at the center,
$$
|f'(0)|
\leq
\frac{1}{r}\max_{|z|=r}|f(z)|
\leq
\frac{1}{r(1-r)}.
$$

:::

:::

::: pf-step

The quantity $r(1-r)$ is maximized on $(0,1)$ at
$$
r=\frac12,
$$
with maximum value $1/4$.

::: pf-proof

Completing the square gives
$$
r(1-r)
=
\frac14-\left(r-\frac12\right)^2
\leq
\frac14.
$$
Equality holds at $r=1/2$.

:::

:::

::: {.pf-step #s3}

Therefore
$$
\boxed{|f'(0)|\leq4}.
$$

::: pf-proof

Substitute $r=1/2$ into step [](#s1){.pf-ref}:
$$
|f'(0)|
\leq
\frac{1}{(1/2)(1/2)}
=
4.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required bound.

:::

:::

:::
