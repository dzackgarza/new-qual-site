---
schema: qual/card@1
id: P-PRACT20-W5-18
kind: problem
title: Complex numbers with $z^2=|z|^2$
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
<1>1. If $z=0$, then
\[
z^2=|z|^2.
\]

::: {.proof}
Both sides are equal to $0$.
:::

<1>2. If $z\ne0$ and
\[
z^2=|z|^2,
\]
then $z$ is real.

::: {.proof}
Since
\[
|z|^2=z\overline z,
\]
the equation becomes
\[
z^2=z\overline z.
\]
Because $z\ne0$, division by $z$ gives
\[
z=\overline z.
\]
A complex number equals its conjugate exactly when its imaginary part is
zero, so $z\in\mathbb R$.
:::

<1>3. Every real number satisfies the equation.

::: {.proof}
If $z=x\in\mathbb R$, then
\[
z^2=x^2=|x|^2=|z|^2.
\]
:::

<1>4. Therefore the solution set is
\[
\boxed{\mathbb R}.
\]

::: {.proof}
Steps <1>1 and <1>2 show that every solution is real, while step <1>3 shows
that every real number is a solution.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested set.
:::
:::
