---
schema: qual/card@1
id: P-PRECALC1-09
kind: problem
title: Limit of $\frac{\sin 2x}{(1+x)\ln(1+x)}$ as $x\to0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Compute $\operatorname* { l i m } _ { x \to 0 } { \frac { \sin ( 2 x ) } { ( 1 + x ) \ln ( 1 + x ) } } .$
:::

::: {.solution}
<1>1. Rewrite the quotient as
\[
\boxed{
\frac{\sin(2x)}{(1+x)\ln(1+x)}
=
\frac{\sin(2x)}{2x}
\cdot
\frac{2x}{\ln(1+x)}
\cdot
\frac1{1+x}}.
\]

::: {.proof}
Multiply the three factors on the right and cancel \(2x\).
:::

<1>2. The first factor satisfies
\[
\boxed{
\lim_{x\to0}
\frac{\sin(2x)}{2x}
=
1}.
\]

::: {.proof}
Set \(u=2x\). Then \(u\to0\), and use the standard limit
\[
\frac{\sin u}{u}\to1.
\]
:::

<1>3. The logarithmic factor satisfies
\[
\boxed{
\lim_{x\to0}
\frac{x}{\ln(1+x)}
=
1}.
\]

::: {.proof}
The standard limit
\[
\frac{\ln(1+x)}{x}\to1
\]
holds as \(x\to0\). Taking reciprocals gives the displayed limit.
:::

<1>4. Therefore
\[
\boxed{
\lim_{x\to0}
\frac{2x}{\ln(1+x)}
=
2}.
\]

::: {.proof}
Multiply the limit in step <1>3 by \(2\).
:::

<1>5. The final factor satisfies
\[
\boxed{
\lim_{x\to0}
\frac1{1+x}
=
1}.
\]

::: {.proof}
The function \(1/(1+x)\) is continuous at \(x=0\).
:::

<1>6. Hence
\[
\boxed{
\lim_{x\to0}
\frac{\sin(2x)}{(1+x)\ln(1+x)}
=
1\cdot2\cdot1
=
2}.
\]

::: {.proof}
Apply the product law for limits to steps <1>1--<1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested limit.
:::
:::
