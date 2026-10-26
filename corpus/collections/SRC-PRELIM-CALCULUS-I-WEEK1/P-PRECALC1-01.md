---
schema: qual/card@1
id: P-PRECALC1-01
kind: problem
title: Tangent line to $y=x+e^x$ at $x=0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
What is the tangent line to the graph of $y = x + e ^ { x }$ at $x = 0 ?$
:::

Let
\[
f(x)=x+e^x.
\]

::: pf

::: pf-step

The point on the graph at
\[
x=0
\]
is
\[
\boxed{(0,1)}.
\]


::: pf-proof

\[
f(0)=0+e^0=1.
\]

:::

:::

::: pf-step

The derivative is
\[
\boxed{
f'(x)=1+e^x}.
\]


::: pf-proof

Differentiate term by term:
\[
\frac{d}{dx}x=1,
\qquad
\frac{d}{dx}e^x=e^x.
\]

:::

:::

::: pf-step

The slope of the tangent line at \(x=0\) is
\[
\boxed{f'(0)=2}.
\]


::: pf-proof

Substitute \(x=0\) into step <1>2:
\[
f'(0)=1+e^0=2.
\]

:::

:::

::: pf-step

Using point-slope form,
\[
y-1=2(x-0).
\]


::: pf-proof

The tangent line passes through \((0,1)\) by step <1>1 and has slope \(2\)
by step <1>3.

:::

:::

::: pf-step

Therefore the tangent line is
\[
\boxed{y=2x+1}.
\]


::: pf-proof

Simplify the equation in step <1>4.

:::

:::

::: pf-qed

Step <1>5 is the requested tangent line.

:::

:::
