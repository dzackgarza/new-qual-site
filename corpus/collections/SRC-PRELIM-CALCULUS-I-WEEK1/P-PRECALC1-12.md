---
schema: qual/card@1
id: P-PRECALC1-12
kind: problem
title: Comparing $\int_0^1\sqrt{1-x^4}\,dx$, $\int_0^1\sqrt{1+x^4}\,dx$ and $\int_0^1\sqrt{1-x^8}\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\begin{array} { r } { J = \int _ { 0 } ^ { 1 } \sqrt { 1 - x ^ { 4 } } d x , \quad K = \int _ { 0 } ^ { 1 } \sqrt { 1 + x ^ { 4 } } d x , \quad L = \int _ { 0 } ^ { 1 } \sqrt { 1 - x ^ { 8 } } d x } \end{array}$ . Order the numbers $J , K , L , 1$ in increasing order.
:::

::: {.solution}
For \(0<x<1\), one has
\[
0<x^8<x^4<1.
\]

<1>1. Therefore
\[
\boxed{
1-x^4<1-x^8<1}.
\]

::: {.proof}
Subtract the inequalities
\[
x^8<x^4
\]
and
\[
0<x^8
\]
from \(1\).
:::

<1>2. Since all quantities in step <1>1 are nonnegative,
\[
\boxed{
\sqrt{1-x^4}
<
\sqrt{1-x^8}
<
1}.
\]

::: {.proof}
The square-root function is strictly increasing on \([0,\infty)\).
:::

<1>3. Also,
\[
1+x^4>1
\]
for \(0<x<1\).

::: {.proof}
Because
\[
x^4>0.
\]
:::

<1>4. Hence
\[
\boxed{
1<
\sqrt{1+x^4}}.
\]

::: {.proof}
Apply the strictly increasing square-root function to step <1>3.
:::

<1>5. Combining steps <1>2 and <1>4,
\[
\boxed{
\sqrt{1-x^4}
<
\sqrt{1-x^8}
<
1
<
\sqrt{1+x^4}}
\]
for every \(0<x<1\).

::: {.proof}
This is exactly the conjunction of the two preceding comparisons.
:::

<1>6. Integrating the first inequality in step <1>5 over \([0,1]\),
\[
\boxed{J<L}.
\]

::: {.proof}
The integrands are continuous, and the strict inequality holds on the whole
open interval \((0,1)\), which has positive length. Therefore the integral of
the difference is strictly positive.
:::

<1>7. Integrating the second comparison,
\[
\boxed{L<1}.
\]

::: {.proof}
From step <1>5,
\[
\sqrt{1-x^8}<1
\]
for \(0<x<1\). Hence
\[
L
=
\int_0^1\sqrt{1-x^8}\,dx
<
\int_0^1 1\,dx
=
1.
\]
:::

<1>8. Integrating the final comparison,
\[
\boxed{1<K}.
\]

::: {.proof}
From step <1>5,
\[
1<\sqrt{1+x^4}
\]
for \(0<x<1\). Thus
\[
1
=
\int_0^1 1\,dx
<
\int_0^1\sqrt{1+x^4}\,dx
=
K.
\]
:::

<1>9. Therefore the increasing order is
\[
\boxed{
J<L<1<K}.
\]

::: {.proof}
Combine steps <1>6--<1>8.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the requested ordering.
:::
:::
