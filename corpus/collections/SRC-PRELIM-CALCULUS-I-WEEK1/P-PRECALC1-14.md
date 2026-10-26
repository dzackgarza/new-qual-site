---
schema: qual/card@1
id: P-PRECALC1-14
kind: problem
title: Integral of the sign function over $[-1,1]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Define $f ( 0 ) = 0$ and $\begin{array} { r } { f ( x ) = \frac { | x | } { x } } \end{array}$ for $x \neq 0$ . Compute $\int _ { - 1 } ^ { 1 } f ( x ) d x .$
:::

::: pf

::: pf-step

For
\[
x<0,
\]
one has
\[
\boxed{
f(x)=-1}.
\]


::: pf-proof

If \(x<0\), then
\[
|x|=-x,
\]
so
\[
\frac{|x|}{x}
=
\frac{-x}{x}
=
-1.
\]

:::

:::

::: pf-step

For
\[
x>0,
\]
one has
\[
\boxed{
f(x)=1}.
\]


::: pf-proof

If \(x>0\), then
\[
|x|=x,
\]
so
\[
\frac{|x|}{x}=1.
\]

:::

:::

::: pf-step

The value \(f(0)=0\) does not affect the definite integral.


::: pf-proof

Changing the value of a bounded function at a single point does not change
its Riemann or Lebesgue integral.

:::

:::

::: pf-step

Therefore
\[
\int_{-1}^{1}f(x)\,dx
=
\int_{-1}^{0}(-1)\,dx
+
\int_{0}^{1}1\,dx.
\]


::: pf-proof

Use steps <1>1--<1>3 and split the integral at \(0\).

:::

:::

::: pf-step

The first integral is
\[
\boxed{-1}.
\]


::: pf-proof

\[
\int_{-1}^{0}(-1)\,dx
=
-\bigl(0-(-1)\bigr)
=
-1.
\]

:::

:::

::: pf-step

The second integral is
\[
\boxed{1}.
\]


::: pf-proof

\[
\int_0^1 1\,dx=1.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\int_{-1}^{1}f(x)\,dx=0}.
\]


::: pf-proof

Combine steps <1>4--<1>6:
\[
-1+1=0.
\]

:::

:::

::: pf-qed

Step <1>7 is the requested integral.

:::

:::
