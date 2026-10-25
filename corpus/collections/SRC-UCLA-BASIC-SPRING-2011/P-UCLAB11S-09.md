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
Let $f:[a,b]\to\mathbb R$ be continuous and nonnegative.
Prove that
\[
\int_a^b f(x)\,dx=0
\]
implies $f\equiv0$.
:::

::: {.solution}
Assume the standard nondegenerate-interval convention
\[
a<b.
\]

<1>1. Suppose, for contradiction, that
\[
f(x_0)>0
\]
for some
\[
x_0\in[a,b].
\]

::: {.proof}
This is the negation of the desired conclusion, because $f$ is assumed nonnegative.
:::

<1>2. There exist
\[
\delta>0
\]
and
\[
\eta>0
\]
such that
\[
f(x)\ge\eta
\]
for every
\[
x\in[a,b]\cap(x_0-\delta,x_0+\delta).
\]

::: {.proof}
Take
\[
\eta=\frac12f(x_0)>0.
\]
By continuity at $x_0$, there exists $\delta>0$ such that
\[
|f(x)-f(x_0)|
<
\frac12f(x_0)
\]
whenever
\[
|x-x_0|<\delta.
\]
Then
\[
f(x)
>
\frac12f(x_0)
=
\eta.
\]
:::

<1>3. The set
\[
I=[a,b]\cap(x_0-\delta,x_0+\delta)
\]
contains a nondegenerate interval.

::: {.proof}
Since
\[
x_0\in[a,b]
\]
and
\[
a<b,
\]
the intersection contains an interval of positive length.
:::

<1>4. One has
\[
\int_a^b f(x)\,dx>0.
\]

::: {.proof}
By nonnegativity,
\[
\int_a^b f(x)\,dx
\ge
\int_I f(x)\,dx.
\]
By step <1>2,
\[
f(x)\ge\eta>0
\]
on $I$.
Thus
\[
\int_I f(x)\,dx
\ge
\eta\,|I|
>
0,
\]
where $|I|$ denotes the positive length of the interval.
:::

<1>5. Therefore
\[
\boxed{f\equiv0}.
\]

::: {.proof}
Step <1>4 contradicts the hypothesis
\[
\int_a^b f(x)\,dx=0.
\]
Hence no point $x_0$ can satisfy
\[
f(x_0)>0.
\]
Since $f\ge0$, one must have
\[
f(x)=0
\]
for every $x\in[a,b]$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
