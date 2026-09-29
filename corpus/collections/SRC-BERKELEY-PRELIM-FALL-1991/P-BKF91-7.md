---
schema: qual/card@1
id: P-BKF91-7
kind: problem
title: Exponential norm bound for a time-dependent linear system
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Differentiated the squared norm and applied an integrating factor, avoiding
    division by the norm at possible zeros of the solution.
---

::: {.problem}
Consider
\[
x'(t)=A(t)x(t),
\]
where $A$ is a smooth real $n\times n$ matrix-valued function. Assume that
\[
\langle A(t)y,y\rangle\le c\|y\|^2
\]
for all $y\in\mathbb R^n$ and all $t$, where $c\in\mathbb R$ is fixed. Prove that every solution satisfies
\[
\|x(t)\|\le e^{ct}\|x(0)\|
\qquad(t>0).
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function
$$
u(t)\coloneqq\norm{x(t)}^2
$$
satisfies
$$
u'(t)\le2c\,u(t).
$$

::: pf-proof

Using the differential equation,
$$
\begin{aligned}
u'(t)
&=2\langle x'(t),x(t)\rangle\\
&=2\langle A(t)x(t),x(t)\rangle\\
&\le2c\norm{x(t)}^2\\
&=2c\,u(t).
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The function
$$
v(t)\coloneqq e^{-2ct}u(t)
$$
is nonincreasing for $t\ge0$.

::: pf-proof

By step [](#s1){.pf-ref},
$$
\begin{aligned}
v'(t)
&=e^{-2ct}\bigl(u'(t)-2c\,u(t)\bigr)\\
&\le0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

For every $t>0$,
$$
\norm{x(t)}^2\le e^{2ct}\norm{x(0)}^2.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
e^{-2ct}\norm{x(t)}^2=v(t)\le v(0)=\norm{x(0)}^2.
$$
Multiply by $e^{2ct}>0$.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{\norm{x(t)}\le e^{ct}\norm{x(0)}}
\qquad(t>0).
$$

::: pf-proof

Both sides in step [](#s3){.pf-ref} are nonnegative. Taking square roots gives the stated inequality.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required estimate.

:::

:::

:::
