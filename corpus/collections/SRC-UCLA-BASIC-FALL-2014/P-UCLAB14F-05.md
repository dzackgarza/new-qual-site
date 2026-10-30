---
schema: qual/card@1
id: P-UCLAB14F-05
kind: problem
title: Convergence of the nested-radical recurrence
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
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Consider the sequence
$$
a_1=\sqrt2,
\qquad
a_{n+1}=\sqrt{2+a_n}\quad(n\geq1).
$$
Prove that this sequence converges and find its limit.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
0<a_n<2
$$
for every $n$.


::: pf-proof

The initial term satisfies
$$
0<a_1=\sqrt2<2.
$$
Assume
$$
0<a_n<2.
$$
Then
$$
2<a_n+2<4,
$$
so
$$
0<a_{n+1}=\sqrt{2+a_n}<2.
$$
The claim follows by induction.

:::

:::

::: {.pf-step #s1-2}

The sequence $(a_n)$ is increasing.


::: pf-proof

It is enough to prove
$$
a_{n+1}>a_n.
$$
Since both sides are positive, this is equivalent to
$$
2+a_n>a_n^2.
$$
Rearranging,
$$
2+a_n-a_n^2
=(2-a_n)(a_n+1).
$$
By step [](#s1-1){.pf-ref},
$$
2-a_n>0
\qquad\text{and}\qquad
a_n+1>0.
$$
Hence
$$
2+a_n-a_n^2>0,
$$
which proves
$$
a_{n+1}>a_n.
$$

:::

:::

::: {.pf-step #s1-3}

The sequence $(a_n)$ converges.


::: pf-proof

By step [](#s1-2){.pf-ref}, $(a_n)$ is increasing.
By step [](#s1-1){.pf-ref}, it is bounded above by $2$.
The monotone convergence theorem for real sequences therefore gives convergence to some limit
$$
L\le2.
$$

:::

:::

::: {.pf-step #s1-4}

The limit satisfies
$$
L=\sqrt{2+L}.
$$


::: pf-proof

From the recurrence,
$$
a_{n+1}=\sqrt{2+a_n}.
$$
Both $a_n$ and $a_{n+1}$ converge to $L$.
The square-root function is continuous on $[0,\infty)$, so passing to the limit gives
$$
L=\sqrt{2+L}.
$$

:::

:::

::: {.pf-step #s1-5}

The only possible positive solution of the equation in step [](#s1-4){.pf-ref} is
$$
\boxed{L=2}.
$$


::: pf-proof

Squaring
$$
L=\sqrt{2+L}
$$
gives
$$
L^2-L-2=0,
$$
so
$$
(L-2)(L+1)=0.
$$
Thus
$$
L=2
\quad\text{or}\quad
L=-1.
$$
Step [](#s1-1){.pf-ref} gives $L\ge0$, so only $L=2$ is possible.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{a_n\to2}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives existence of the limit, and step [](#s1-5){.pf-ref} identifies it.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
