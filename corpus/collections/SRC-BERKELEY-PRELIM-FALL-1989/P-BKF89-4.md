---
schema: qual/card@1
id: P-BKF89-4
kind: problem
title: A growth bound in the unit disk implies $|f'(0)|\le4$
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
<1>1. For every $0<r<1$,
$$
|f'(0)|
\leq
\frac{1}{r(1-r)}.
$$

::: {.proof}
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

<1>2. The quantity $r(1-r)$ is maximized on $(0,1)$ at
$$
r=\frac12,
$$
with maximum value $1/4$.

::: {.proof}
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

<1>3. Therefore
$$
\boxed{|f'(0)|\leq4}.
$$

::: {.proof}
Substitute $r=1/2$ into step <1>1:
$$
|f'(0)|
\leq
\frac{1}{(1/2)(1/2)}
=
4.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required bound.
:::
:::
