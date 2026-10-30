---
schema: qual/card@1
id: P-UCLAB11S-09
kind: problem
title: A nonnegative continuous function with zero integral vanishes
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Spring 2011.
---

::: {.problem}
Let $f:[a,b]\to\RR$ be continuous and nonnegative.
Prove that
$$
\int_a^b f(x)\,dx=0
$$
implies $f\equiv0$.
:::

::: {.solution}

Assume the standard nondegenerate-interval convention
$$
a<b.
$$

::: pf

::: pf-step

Suppose, for contradiction, that
$$
f(x_0)>0
$$
for some
$$
x_0\in[a,b].
$$


::: pf-proof

This is the negation of the desired conclusion, because $f$ is assumed nonnegative.

:::

:::

::: {.pf-step #s1-2}

There exist
$$
\delta>0
$$
and
$$
\eta>0
$$
such that
$$
f(x)\ge\eta
$$
for every
$$
x\in[a,b]\cap(x_0-\delta,x_0+\delta).
$$


::: pf-proof

Take
$$
\eta=\frac12f(x_0)>0.
$$
By continuity at $x_0$, there exists $\delta>0$ such that
$$
\abs{f(x)-f(x_0)}
<
\frac12f(x_0)
$$
whenever
$$
\abs{x-x_0}<\delta.
$$
Then
$$
f(x)
>
\frac12f(x_0)
=
\eta.
$$

:::

:::

::: pf-step

The set
$$
I=[a,b]\cap(x_0-\delta,x_0+\delta)
$$
contains a nondegenerate interval.


::: pf-proof

Since
$$
x_0\in[a,b]
$$
and
$$
a<b,
$$
the intersection contains an interval of positive length.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\int_a^b f(x)\,dx>0.
$$


::: pf-proof

By nonnegativity,
$$
\int_a^b f(x)\,dx
\ge
\int_I f(x)\,dx.
$$
By step [](#s1-2){.pf-ref},
$$
f(x)\ge\eta>0
$$
on $I$.
Thus
$$
\int_I f(x)\,dx
\ge
\eta\,\setmeasure{I}
>
0,
$$
where $\setmeasure{I}$ denotes the positive length of the interval.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{f\equiv0}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} contradicts the hypothesis
$$
\int_a^b f(x)\,dx=0.
$$
Hence no point $x_0$ can satisfy
$$
f(x_0)>0.
$$
Since $f\ge0$, one must have
$$
f(x)=0
$$
for every $x\in[a,b]$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
