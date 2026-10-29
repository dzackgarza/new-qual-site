---
schema: qual/card@1
id: P-UCLAB16S-01
kind: problem
title: Continuity along the diagonal under separate monotonicity
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $a<b$ be real numbers, and let
$$
f:[a,b]\times[a,b]\to\RR
$$
satisfy:

1. for each $y\in[a,b]$, the map $x\mapsto f(x,y)$ is non-increasing and continuous on $[a,b]$;

2. for each $x\in[a,b]$, the map $y\mapsto f(x,y)$ is non-decreasing and continuous on $[a,b]$.

Prove that $g(x):=f(x,x)$ is continuous on $[a,b]$.
:::

::: {.solution}

Fix
$$
x_0\in[a,b].
$$

::: pf

::: {.pf-step #s1-1}

If
$$
x\ge x_0,
$$
then
$$
\boxed{
f(x,x_0)
\le
g(x)
\le
f(x_0,x).
}
$$


::: pf-proof

Because
$$
y\longmapsto f(x,y)
$$
is non-decreasing,
$$
f(x,x_0)
\le
f(x,x)
=
g(x).
$$

Because
$$
x\longmapsto f(x,x)
$$
with the second coordinate fixed at $x$ is non-increasing in its first variable and
$$
x\ge x_0,
$$
one has
$$
f(x,x)
\le
f(x_0,x).
$$
Thus the displayed inequalities hold.

:::

:::

::: {.pf-step #s1-2}

As
$$
x\to x_0^+,
$$
one has
$$
f(x,x_0)\to f(x_0,x_0)
$$
and
$$
f(x_0,x)\to f(x_0,x_0).
$$


::: pf-proof

For the first limit, hold the second coordinate equal to $x_0$ and use continuity of
$$
x\longmapsto f(x,x_0).
$$
For the second, hold the first coordinate equal to $x_0$ and use continuity of
$$
y\longmapsto f(x_0,y).
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\lim_{x\to x_0^+}g(x)
=
g(x_0).
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
f(x,x_0)
\le
g(x)
\le
f(x_0,x).
$$
Both outer terms converge to
$$
f(x_0,x_0)
=
g(x_0)
$$
by step [](#s1-2){.pf-ref}.
Apply the squeeze theorem.

:::

:::

::: {.pf-step #s1-4}

If
$$
x\le x_0,
$$
then
$$
\boxed{
f(x_0,x)
\le
g(x)
\le
f(x,x_0).
}
$$


::: pf-proof

Because
$$
x\longmapsto f(x,x)
$$
is non-increasing in its first variable and
$$
x\le x_0,
$$
one has
$$
f(x_0,x)
\le
f(x,x)
=
g(x).
$$

Because
$$
y\longmapsto f(x,y)
$$
is non-decreasing and
$$
x\le x_0,
$$
one has
$$
f(x,x)
\le
f(x,x_0).
$$

:::

:::

::: {.pf-step #s1-5}

As
$$
x\to x_0^-,
$$
one has
$$
f(x_0,x)\to f(x_0,x_0)
$$
and
$$
f(x,x_0)\to f(x_0,x_0).
$$


::: pf-proof

These are the same separate-continuity statements used in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\lim_{x\to x_0^-}g(x)
=
g(x_0).
$$


::: pf-proof

Use the inequalities from step [](#s1-4){.pf-ref} and the limits from step [](#s1-5){.pf-ref}, then apply the squeeze theorem.

:::

:::

::: {.pf-step #s1-7}

Hence $g$ is continuous at $x_0$.


::: pf-proof

At an interior point,
$$
x_0\in(a,b),
$$
steps [](#s1-3){.pf-ref} and [](#s1-6){.pf-ref} give the right- and left-hand limits, both equal to
$$
g(x_0).
$$
At the endpoint $a$, only the right-hand limit is required and step [](#s1-3){.pf-ref} applies.
At the endpoint $b$, only the left-hand limit is required and step [](#s1-6){.pf-ref} applies.

:::

:::

::: {.pf-step #s1-8}

Since $x_0$ was arbitrary,
$$
\boxed{g\in C([a,b])}.
$$


::: pf-proof

Step [](#s1-7){.pf-ref} proves continuity at every point of the interval.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
