---
schema: qual/card@1
id: P-BERK87S-06
kind: problem
title: Derivative bound from $|f(z)|\le C/(1-|z|)$ on the unit disk
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Applied the Cauchy derivative estimate on the circle of radius half the
    distance from z to the unit circle. The growth bound is then at most
    2C/(1-|z|) on that circle, giving the stated factor 4.
---

::: {.problem}
Let $f$ be analytic in the open unit disk and suppose
\[
|f(z)|\le\frac{C}{1-|z|}
\]
for all $z$ in the disk, where $C>0$. Prove that
\[
|f'(z)|\le\frac{4C}{(1-|z|)^2}.
\]
:::

::: {.solution}
Fix $z$ in the open unit disk and set
$$
r\coloneqq\frac{1-\abs{z}}{2}.
$$

::: pf

::: {.pf-step #circle-inside-disk}
If $\abs{w-z}=r$, then
$$
1-\abs{w}\geq r.
$$

::: pf-proof
By the triangle inequality,
$$
\abs{w}
\leq
\abs{z}+\abs{w-z}
=
\abs{z}+r.
$$
Therefore
$$
1-\abs{w}
\geq
1-\abs{z}-r
=
\frac{1-\abs{z}}2
=r.
$$
In particular, the circle $\abs{w-z}=r$ lies inside the open unit disk.
:::

:::

::: {.pf-step #bound-on-circle}
On the circle $\abs{w-z}=r$,
$$
\abs{f(w)}
\leq
\frac{2C}{1-\abs{z}}.
$$

::: pf-proof
By the hypothesis and step [](#circle-inside-disk){.pf-ref},
$$
\abs{f(w)}
\leq
\frac{C}{1-\abs{w}}
\leq
\frac{C}{r}
=
\frac{2C}{1-\abs{z}}.
$$
:::

:::

::: {.pf-step #derivative-bound-boxed}
One has
$$
\boxed{
\abs{f'(z)}
\leq
\frac{4C}{(1-\abs{z})^2}
}.
$$

::: pf-proof
The Cauchy derivative estimate on the circle $\abs{w-z}=r$ gives
$$
\abs{f'(z)}
\leq
\frac{1}{r}
\max_{\abs{w-z}=r}\abs{f(w)}.
$$
Using step [](#bound-on-circle){.pf-ref} and the definition of $r$,
$$
\abs{f'(z)}
\leq
\frac{2}{1-\abs{z}}
\cdot
\frac{2C}{1-\abs{z}}
=
\frac{4C}{(1-\abs{z})^2}.
$$
:::

:::

::: pf-qed
The point $z$ was arbitrary, so step [](#derivative-bound-boxed){.pf-ref} proves the required estimate
throughout the unit disk.
:::

:::
:::
