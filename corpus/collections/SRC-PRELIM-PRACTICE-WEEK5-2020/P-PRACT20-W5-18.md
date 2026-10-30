---
schema: qual/card@1
id: P-PRACT20-W5-18
kind: problem
title: Complex numbers with $z^2=\abs{z}^2$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 18).
---

::: {.problem}
What is the set of points $z \in \CC$ such that $z^2 = \abs{z}^2$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $z=0$, then
$$
z^2=\abs{z}^2.
$$


::: pf-proof

Both sides are equal to $0$.

:::

:::

::: {.pf-step #s1-2}

If $z\ne0$ and
$$
z^2=\abs{z}^2,
$$
then $z$ is real.


::: pf-proof

Since
$$
\abs{z}^2=z\overline z,
$$
the equation becomes
$$
z^2=z\overline z.
$$
Because $z\ne0$, division by $z$ gives
$$
z=\overline z.
$$
A complex number equals its conjugate exactly when its imaginary part is
zero, so $z\in\RR$.

:::

:::

::: {.pf-step #s1-3}

Every real number satisfies the equation.


::: pf-proof

If $z=x\in\RR$, then
$$
z^2=x^2=\abs{x}^2=\abs{z}^2.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore the solution set is
$$
\boxed{\RR}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that every solution is real, while step [](#s1-3){.pf-ref} shows
that every real number is a solution.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested set.

:::

:::

:::
