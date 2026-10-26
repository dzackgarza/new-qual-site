---
schema: qual/card@1
id: P-PRECALC1-11
kind: problem
title: Derivative of $x^{2+\sin x}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f ( x ) = x ^ { 2 + \sin ( x ) }$ for $x > 0$ . Find $f ^ { \prime } ( x )$
:::

Let
\[
f(x)=x^{2+\sin x},
\qquad
x>0.
\]

::: pf

::: pf-step

Since \(x>0\),
\[
\boxed{
f(x)=e^{(2+\sin x)\log x}}.
\]


::: pf-proof

Use
\[
x^a=e^{a\log x}
\]
for positive \(x\).

:::

:::

::: pf-step

Differentiate the exponent:
\[
\frac{d}{dx}
\left(
(2+\sin x)\log x
\right)
=
\cos x\,\log x
+
\frac{2+\sin x}{x}.
\]


::: pf-proof

Apply the product rule:
\[
(2+\sin x)'\log x
+
(2+\sin x)(\log x)'.
\]
Now
\[
(2+\sin x)'=\cos x
\]
and
\[
(\log x)'=\frac1x.
\]

:::

:::

::: pf-step

By the chain rule,
\[
f'(x)
=
e^{(2+\sin x)\log x}
\left(
\cos x\,\log x
+
\frac{2+\sin x}{x}
\right).
\]


::: pf-proof

Differentiate the exponential expression from step <1>1 using step <1>2.

:::

:::

::: pf-step

Therefore
\[
\boxed{
f'(x)
=
x^{2+\sin x}
\left(
\cos x\,\log x
+
\frac{2+\sin x}{x}
\right)}.
\]


::: pf-proof

Replace the exponential factor in step <1>3 by \(x^{2+\sin x}\) using
step <1>1.

:::

:::

::: pf-qed

Step <1>4 is the requested derivative.

:::

:::
