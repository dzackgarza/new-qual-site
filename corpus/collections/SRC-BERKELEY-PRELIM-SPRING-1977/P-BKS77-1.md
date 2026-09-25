---
schema: qual/card@1
id: P-BKS77-1
kind: problem
title: A differential inequality forces positivity to the right of a zero
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Applied the integrating factor e^{-x}; its derivative is strictly
    positive, so the transformed function is strictly increasing from zero.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be differentiable and suppose
\[
f'(x)>f(x)
\]
for every $x\in\mathbb R$. If $f(x_0)=0$, prove that
\[
f(x)>0
\]
for every $x>x_0$.
:::

::: {.solution}
<1>1. Define
$$
g(x)=e^{-x}f(x).
$$
Then $g'(x)>0$ for every $x\in\RR$.

::: {.proof}
By the product rule,
$$
g'(x)
=
e^{-x}\bigl(f'(x)-f(x)\bigr).
$$
The factor $e^{-x}$ is positive, and the hypothesis gives
$f'(x)-f(x)>0$. Hence $g'(x)>0$.
:::

<1>2. The function $g$ is strictly increasing on $\RR$.

::: {.proof}
If $a<b$, the mean value theorem gives some $c\in(a,b)$ such that
$$
g(b)-g(a)=g'(c)(b-a).
$$
By step <1>1, both factors on the right are positive, so $g(b)>g(a)$.
:::

<1>3. If $x>x_0$, then $f(x)>0$.

::: {.proof}
Since
$$
g(x_0)=e^{-x_0}f(x_0)=0,
$$
strict increase from step <1>2 gives $g(x)>0$ whenever $x>x_0$. Therefore
$$
f(x)=e^xg(x)>0.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
