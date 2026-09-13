---
schema: qual/card@1
id: P-BERK80S-06
kind: problem
title: Contour integral of a square-root branch
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 6 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the chosen exterior branch, its Laurent expansion, and the resulting contour integral.
---

::: {.problem}
Let C denote the positively oriented circle $| z | = 2 , z \in \mathbb { C }$ . Evaluate the integral

$$
\int _ { C } { \sqrt { z ^ { 2 } - 1 } } d z
$$

where the branch of the square root is chosen so that $\sqrt { 2 ^ { 2 } - 1 } > 0$
:::


::: {.solution}
The value of the integral is
\[
\boxed{-\pi i}.
\]

<1>1. Identify the branch selected by the condition at $z=2$.
::: {.proof}
For $|z|>1$, write
\[
\sqrt{z^2-1}=z\sqrt{1-z^{-2}},
\]
where the second square root is the analytic branch near $1$ satisfying $\sqrt1=1$.
Since $|z^{-2}|<1$, the quantity $1-z^{-2}$ lies in the open disk centered at $1$ of radius $1$, so this branch is analytic throughout $|z|>1$.
At $z=2$ it gives
\[
2\sqrt{1-\frac14}=\sqrt3>0,
\]
so it is exactly the branch required in the problem.
:::

<1>2. Compute the coefficient of $z^{-1}$ in its Laurent expansion.
::: {.proof}
For $|z|>1$, the binomial expansion gives
\[
\sqrt{1-z^{-2}}
=1-\frac12z^{-2}-\frac18z^{-4}-\cdots.
\]
Multiplying by $z$,
\[
\sqrt{z^2-1}
=z-\frac1{2z}-\frac1{8z^3}-\cdots.
\]
Hence the coefficient of $z^{-1}$ is $-\tfrac12$.
:::

<1>3. Integrate around $C$.
::: {.proof}
The Laurent series converges on the circle $|z|=2$, so termwise integration around the positively oriented circle gives
\[
\int_C\sqrt{z^2-1}\,dz
=2\pi i\left(-\frac12\right)
=-\pi i.
\]
:::
:::
