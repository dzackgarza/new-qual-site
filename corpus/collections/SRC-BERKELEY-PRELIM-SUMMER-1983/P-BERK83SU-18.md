---
schema: qual/card@1
id: P-BERK83SU-18
kind: problem
title: $C^1$ solutions of $xy'+y=x$ across the singular point $x=0$
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

::: pf

::: {.pf-step #s1}

Every $C^1$ solution satisfies
$$
(xy)'=x
$$
on $(-1,1)$.

::: pf-proof

By the product rule,
$$
(xy)'=xy'+y.
$$
The differential equation therefore gives $(xy)'=x$ at every point
of the interval, including $x=0$.

:::

:::

::: {.pf-step #s2}

There is a constant $C\in\RR$ such that
$$
xy(x)=\frac{x^2}{2}+C
$$
for every $x\in(-1,1)$.

::: pf-proof

By step [](#s1){.pf-ref},
$$
\left(xy(x)-\frac{x^2}{2}\right)'=0
$$
on the connected interval $(-1,1)$. Hence the expression in
parentheses is constant.

:::

:::

::: {.pf-step #s3}

The constant in step [](#s2){.pf-ref} is $C=0$.

::: pf-proof

Substituting $x=0$ into the identity from step [](#s2){.pf-ref} gives
$$
0=C.
$$

:::

:::

::: {.pf-step #s4}

Every solution is
$$
\boxed{y(x)=\frac{x}{2}}
$$
on $(-1,1)$.

::: pf-proof

For $x\neq0$, steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give
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

:::

::: {.pf-step #s5}

The function $y(x)=x/2$ is indeed a $C^1$ solution.

::: pf-proof

It is $C^1$ on $(-1,1)$, and
$$
x\left(\frac12\right)+\frac{x}{2}=x.
$$

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} show that the displayed function is the unique
$C^1$ solution.

:::

:::

:::
