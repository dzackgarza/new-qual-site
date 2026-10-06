---
schema: qual/card@1
id: P-PRECALC1-07
kind: problem
title: Quadratic $3x^2+bx+c$ with a double root at $2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose that $f ( x ) = 3 x ^ { 2 } + b x + c$ has a non-simple root at $x = 2$ . What is $f ( 5 ) ?$
:::

::: {.solution}
<1>1. Since \(x=2\) is a non-simple root of the quadratic \(f\), it is a
double root.

::: {.proof}
A quadratic polynomial has total root multiplicity \(2\). Thus any root of
multiplicity greater than \(1\) has multiplicity exactly \(2\).
:::

<1>2. Therefore
\[
f(x)
=
A(x-2)^2
\]
for some constant \(A\).

::: {.proof}
A quadratic with a double root at \(2\) is a scalar multiple of
\[
(x-2)^2.
\]
:::

<1>3. Comparing leading coefficients gives
\[
\boxed{A=3}.
\]

::: {.proof}
The leading coefficient of
\[
A(x-2)^2
\]
is \(A\), while the given polynomial
\[
3x^2+bx+c
\]
has leading coefficient \(3\).
:::

<1>4. Hence
\[
\boxed{
f(x)=3(x-2)^2}.
\]

::: {.proof}
Substitute step <1>3 into step <1>2.
:::

<1>5. Evaluating at \(x=5\),
\[
\boxed{
f(5)=3(5-2)^2=27}.
\]

::: {.proof}
\[
5-2=3,
\qquad
3\cdot3^2
=
27.
\]
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the requested value.
:::
:::
