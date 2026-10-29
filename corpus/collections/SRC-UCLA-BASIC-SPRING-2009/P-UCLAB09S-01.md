---
schema: qual/card@1
id: P-UCLAB09S-01
kind: problem
title: Convergence of a nested-radical recurrence
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Set $a_1=0$ and define
$$
a_{n+1}=\sqrt{6+a_n}\qquad(n\ge1).
$$
Show that $(a_n)$ converges and determine its limit.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $n\ge1$,
$$
0\le a_n<3.
$$


::: pf-proof

The initial value satisfies
$$
a_1=0<3.
$$
Assume
$$
0\le a_n<3.
$$
Then
$$
6\le6+a_n<9,
$$
so
$$
0<a_{n+1}
=
\sqrt{6+a_n}
<
3.
$$
Thus the claim follows by induction.

:::

:::

::: {.pf-step #s1-2}

The sequence $(a_n)$ is increasing.


::: pf-proof

We prove
$$
a_{n+1}\ge a_n.
$$
Since both sides are nonnegative, this is equivalent to
$$
6+a_n\ge a_n^2.
$$
Now
$$
6+a_n-a_n^2
=
(3-a_n)(a_n+2).
$$
By step [](#s1-1){.pf-ref},
$$
3-a_n>0
\qquad\text{and}\qquad
a_n+2>0.
$$
Hence
$$
6+a_n-a_n^2>0,
$$
so in fact
$$
a_{n+1}>a_n.
$$

:::

:::

::: {.pf-step #s1-3}

The sequence $(a_n)$ converges.


::: pf-proof

By step [](#s1-2){.pf-ref}, $(a_n)$ is increasing.
By step [](#s1-1){.pf-ref}, it is bounded above by $3$.
The monotone convergence theorem for real sequences therefore gives a limit
$$
L=\lim_{n\to\infty}a_n.
$$

:::

:::

::: {.pf-step #s1-4}

The limit $L$ satisfies
$$
L=\sqrt{6+L}.
$$


::: pf-proof

The recurrence gives
$$
a_{n+1}=\sqrt{6+a_n}.
$$
Both $a_n$ and $a_{n+1}$ converge to $L$.
Continuity of the square-root function yields
$$
L=\sqrt{6+L}.
$$

:::

:::

::: {.pf-step #s1-5}

The only possible nonnegative solution is
$$
\boxed{L=3}.
$$


::: pf-proof

Squaring the equation from step [](#s1-4){.pf-ref} gives
$$
L^2-L-6=0.
$$
Factor:
$$
(L-3)(L+2)=0.
$$
Thus
$$
L=3
\quad\text{or}\quad
L=-2.
$$
By step [](#s1-1){.pf-ref}, every $a_n$ is nonnegative, so
$$
L\ge0.
$$
Hence
$$
L=3.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{a_n\to3}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} proves existence of the limit, and step [](#s1-5){.pf-ref} identifies it.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
