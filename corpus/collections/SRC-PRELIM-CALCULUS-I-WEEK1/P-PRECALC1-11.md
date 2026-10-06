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

::: {.solution}
Let
\[
f(x)=x^{2+\sin x},
\qquad
x>0.
\]

<1>1. Since \(x>0\),
\[
\boxed{
f(x)=e^{(2+\sin x)\log x}}.
\]

::: {.proof}
Use
\[
x^a=e^{a\log x}
\]
for positive \(x\).
:::

<1>2. Differentiate the exponent:
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

::: {.proof}
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

<1>3. By the chain rule,
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

::: {.proof}
Differentiate the exponential expression from step <1>1 using step <1>2.
:::

<1>4. Therefore
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

::: {.proof}
Replace the exponential factor in step <1>3 by \(x^{2+\sin x}\) using
step <1>1.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested derivative.
:::
:::
