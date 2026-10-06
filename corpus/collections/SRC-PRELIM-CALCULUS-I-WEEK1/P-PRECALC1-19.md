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

::: {.solution}
<1>1. Add and subtract \(f(x_0)\) in the numerator:
\[
\begin{aligned}
f(x_0+h)-f(x_0-h)
={}&
\bigl(f(x_0+h)-f(x_0)\bigr)\\
&+
\bigl(f(x_0)-f(x_0-h)\bigr).
\end{aligned}
\]

::: {.proof}
The two added terms \(+f(x_0)\) and \(-f(x_0)\) cancel.
:::

<1>2. Therefore
\[
\boxed{
\frac{f(x_0+h)-f(x_0-h)}{h}
=
\frac{f(x_0+h)-f(x_0)}{h}
+
\frac{f(x_0-h)-f(x_0)}{-h}}.
\]

::: {.proof}
Divide step <1>1 by \(h\), and rewrite
\[
\frac{f(x_0)-f(x_0-h)}{h}
=
\frac{f(x_0-h)-f(x_0)}{-h}.
\]
:::

<1>3. Since \(f\) is differentiable at \(x_0\),
\[
\boxed{
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0)}{h}
=
f'(x_0)}.
\]

::: {.proof}
This is the definition of the derivative.
:::

<1>4. Also,
\[
\boxed{
\lim_{h\to0}
\frac{f(x_0-h)-f(x_0)}{-h}
=
f'(x_0)}.
\]

::: {.proof}
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

<1>5. Hence
\[
\boxed{
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0-h)}{h}
=
2f'(x_0)}.
\]

::: {.proof}
Take limits in step <1>2 and use steps <1>3--<1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the requested limit.
:::
:::
