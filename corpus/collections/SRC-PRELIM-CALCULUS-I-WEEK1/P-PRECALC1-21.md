---
schema: qual/card@1
id: P-PRECALC1-21
kind: problem
title: Derivative of $\frac{x^3}{(6x^2+1)\sqrt[3]{(x+3)^4}}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the first derivative of $\begin{array} { r } { f ( x ) = \frac { x ^ { 3 } } { ( 6 x ^ { 2 } + 1 ) \sqrt [ 3 ] { ( x + 3 ) ^ { 4 } } } } \end{array}$ when $x > 0$
:::

::: {.solution}
For \(x>0\), one also has
\[
x+3>0,
\]
so
\[
\sqrt[3]{(x+3)^4}
=
(x+3)^{4/3}.
\]

Thus
\[
f(x)
=
\frac{x^3}
{(6x^2+1)(x+3)^{4/3}}.
\]

<1>1. Since \(f(x)>0\) for \(x>0\), take logarithms:
\[
\boxed{
\log f(x)
=
3\log x
-
\log(6x^2+1)
-
\frac43\log(x+3)}.
\]

::: {.proof}
Apply logarithm rules to the product and powers in the denominator.
:::

<1>2. Differentiate both sides:
\[
\frac{f'(x)}{f(x)}
=
\frac3x
-
\frac{12x}{6x^2+1}
-
\frac{4}{3(x+3)}.
\]

::: {.proof}
Use
\[
\frac{d}{dx}\log f(x)
=
\frac{f'(x)}{f(x)},
\]
together with the chain rule:
\[
\frac{d}{dx}\log(6x^2+1)
=
\frac{12x}{6x^2+1}.
\]
:::

<1>3. Therefore
\[
\boxed{
f'(x)
=
f(x)
\left(
\frac3x
-
\frac{12x}{6x^2+1}
-
\frac{4}{3(x+3)}
\right)}.
\]

::: {.proof}
Multiply the identity in step <1>2 by \(f(x)\).
:::

<1>4. Substituting the original formula for \(f\),
\[
\boxed{
f'(x)
=
\frac{x^3}
{(6x^2+1)(x+3)^{4/3}}
\left(
\frac3x
-
\frac{12x}{6x^2+1}
-
\frac{4}{3(x+3)}
\right)}.
\]

::: {.proof}
Replace \(f(x)\) in step <1>3 by its explicit expression.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested derivative.
:::
:::
