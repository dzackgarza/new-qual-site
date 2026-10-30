---
schema: qual/card@1
id: P-UCLAB14F-01
kind: problem
title: Existence of a global minimum off the diagonal
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
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 1. Show that the function
$$
H(x,y)=x^2+y^2+\abs{x-y}^{-1}
$$
achieves its global minimum somewhere on the set
$$
\{(x,y)\in\RR^2:x\neq y\}.
$$
:::

::: {.solution}

Let
$$
D=\{(x,y)\in\RR^2:x\ne y\}.
$$
The function $H$ is continuous on $D$.

::: pf

::: {.pf-step #s1-1}

The value
$$
H(0,1)=2.
$$


::: pf-proof

Direct substitution gives
$$
H(0,1)
=
0^2+1^2+\abs{0-1}^{-1}
=
1+1
=2.
$$

:::

:::

::: {.pf-step #s1-2}

Define
$$
K=\{(x,y)\in D:H(x,y)\le2\}.
$$
Then $K$ is nonempty.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
(0,1)\in K.
$$

:::

:::

::: {.pf-step #s1-3}

Every $(x,y)\in K$ satisfies
$$
x^2+y^2\le2.
$$


::: pf-proof

All terms in $H$ are nonnegative, so
$$
x^2+y^2
\le
H(x,y)
\le2.
$$

:::

:::

::: {.pf-step #s1-4}

Every $(x,y)\in K$ satisfies
$$
\abs{x-y}\ge\frac12.
$$


::: pf-proof

Again,
$$
\abs{x-y}^{-1}
\le
H(x,y)
\le2.
$$
Since $\abs{x-y}>0$ on $D$, taking reciprocals gives
$$
\abs{x-y}\ge\frac12.
$$

:::

:::

::: {.pf-step #s1-5}

The set $K$ is compact in $\RR^2$.


::: pf-proof

Step [](#s1-3){.pf-ref} shows that $K$ is bounded.

By step [](#s1-4){.pf-ref},
$$
K
\subseteq
\left\{(x,y):\abs{x-y}\ge\frac12\right\}.
$$
On this closed set, the formula defining $H$ is continuous. Therefore
$$
K
=
\left\{
(x,y):
\abs{x-y}\ge\frac12,
H(x,y)\le2
\right\}
$$
is closed in $\RR^2$.
Thus $K$ is closed and bounded, hence compact by Heine--Borel.

:::

:::

::: {.pf-step #s1-6}

The restriction
$$
H\restrict_K
$$
attains a minimum at some
$$
(x_0,y_0)\in K.
$$


::: pf-proof

The set $K$ is nonempty and compact by steps [](#s1-2){.pf-ref} and [](#s1-5){.pf-ref}, and $H$ is continuous on $K$.
The extreme value theorem therefore gives a minimizing point.

:::

:::

::: {.pf-step #s1-7}

The point $(x_0,y_0)$ from step [](#s1-6){.pf-ref} is a global minimizer of $H$ on $D$.


::: pf-proof

Because $(0,1)\in K$,
$$
H(x_0,y_0)
\le
H(0,1)
=2.
$$
If
$$
(x,y)\in D\setminus K,
$$
then by definition of $K$,
$$
H(x,y)>2.
$$
Thus no point outside $K$ has smaller value than $(x_0,y_0)$, while step [](#s1-6){.pf-ref} gives minimality on $K$.
Hence $(x_0,y_0)$ is a global minimizer on $D$.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves that $H$ achieves its global minimum somewhere off the diagonal.

:::

:::

:::
