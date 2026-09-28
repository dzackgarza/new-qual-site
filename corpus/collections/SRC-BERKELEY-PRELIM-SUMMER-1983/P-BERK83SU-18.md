---
schema: qual/card@1
id: P-BERK83SU-18
kind: problem
title: Solve $xy'+y=x$ by $C^1$ functions across the singular point
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The equation is exactly (xy)'=x on the whole interval. Hence
    xy=x^2/2+C. Evaluating at x=0 forces C=0, so y=x/2 away from zero,
    and continuity gives the same value at zero.
---

::: {.problem}
Find all real-valued $C^1$ solutions $y$ on $(-1,1)$ of
\[
x\frac{dy}{dx}+y=x.
\]
:::

::: {.solution}
<1>1. Every $C^1$ solution satisfies
$$
(xy)'=x
$$
on $(-1,1)$.

::: {.proof}
By the product rule,
$$
(xy)'=xy'+y.
$$
The differential equation therefore gives $(xy)'=x$ at every point
of the interval, including $x=0$.
:::

<1>2. There is a constant $C\in\RR$ such that
$$
xy(x)=\frac{x^2}{2}+C
$$
for every $x\in(-1,1)$.

::: {.proof}
By step <1>1,
$$
\left(xy(x)-\frac{x^2}{2}\right)'=0
$$
on the connected interval $(-1,1)$. Hence the expression in
parentheses is constant.
:::

<1>3. The constant in step <1>2 is $C=0$.

::: {.proof}
Substituting $x=0$ into the identity from step <1>2 gives
$$
0=C.
$$
:::

<1>4. Every solution is
$$
\boxed{y(x)=\frac{x}{2}}
$$
on $(-1,1)$.

::: {.proof}
For $x\neq0$, steps <1>2 and <1>3 give
$$
xy(x)=\frac{x^2}{2},
$$
so $y(x)=x/2$. Since $y$ is continuous,
$$
y(0)
=
\lim_{x\to0}y(x)
=
0,
$$
which is also the value of $x/2$ at $0$.
:::

<1>5. The function $y(x)=x/2$ is indeed a $C^1$ solution.

::: {.proof}
It is $C^1$ on $(-1,1)$, and
$$
x\left(\frac12\right)+\frac{x}{2}=x.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>4 and <1>5 show that the displayed function is the unique
$C^1$ solution.
:::
:::
