---
schema: qual/card@1
id: P-PRECALC1-19
kind: problem
title: Symmetric difference quotient $\frac{f(x_0+h)-f(x_0-h)}{h}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose that f is differentiable at $x = x _ { 0 }$ . What is $\operatorname* { l i m } _ { h \to 0 } { \frac { f ( x _ { 0 } + h ) - f ( x _ { 0 } - h ) } { h } } \ ?$
:::

::: pf

::: pf-step

Add and subtract \(f(x_0)\) in the numerator:
\[
\begin{aligned}
f(x_0+h)-f(x_0-h)
={}&
\bigl(f(x_0+h)-f(x_0)\bigr)\\
&+
\bigl(f(x_0)-f(x_0-h)\bigr).
\end{aligned}
\]


::: pf-proof

The two added terms \(+f(x_0)\) and \(-f(x_0)\) cancel.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\frac{f(x_0+h)-f(x_0-h)}{h}
=
\frac{f(x_0+h)-f(x_0)}{h}
+
\frac{f(x_0-h)-f(x_0)}{-h}}.
\]


::: pf-proof

Divide step <1>1 by \(h\), and rewrite
\[
\frac{f(x_0)-f(x_0-h)}{h}
=
\frac{f(x_0-h)-f(x_0)}{-h}.
\]

:::

:::

::: pf-step

Since \(f\) is differentiable at \(x_0\),
\[
\boxed{
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0)}{h}
=
f'(x_0)}.
\]


::: pf-proof

This is the definition of the derivative.

:::

:::

::: pf-step

Also,
\[
\boxed{
\lim_{h\to0}
\frac{f(x_0-h)-f(x_0)}{-h}
=
f'(x_0)}.
\]


::: pf-proof

Set
\[
k=-h.
\]
Then \(k\to0\) as \(h\to0\), and the quotient becomes
\[
\frac{f(x_0+k)-f(x_0)}{k}.
\]
Apply differentiability.

:::

:::

::: pf-step

Hence
\[
\boxed{
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0-h)}{h}
=
2f'(x_0)}.
\]


::: pf-proof

Take limits in step <1>2 and use steps <1>3--<1>4.

:::

:::

::: pf-qed

Step <1>5 is the requested limit.

:::

:::
