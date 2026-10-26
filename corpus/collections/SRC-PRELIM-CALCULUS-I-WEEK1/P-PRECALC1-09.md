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

::: pf

::: pf-step

Rewrite the quotient as
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


::: pf-proof

Multiply the three factors on the right and cancel \(2x\).

:::

:::

::: pf-step

The first factor satisfies
\[
\boxed{
\lim_{x\to0}
\frac{\sin(2x)}{2x}
=
1}.
\]


::: pf-proof

Set \(u=2x\). Then \(u\to0\), and use the standard limit
\[
\frac{\sin u}{u}\to1.
\]

:::

:::

::: pf-step

The logarithmic factor satisfies
\[
\boxed{
\lim_{x\to0}
\frac{x}{\ln(1+x)}
=
1}.
\]


::: pf-proof

The standard limit
\[
\frac{\ln(1+x)}{x}\to1
\]
holds as \(x\to0\). Taking reciprocals gives the displayed limit.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\lim_{x\to0}
\frac{2x}{\ln(1+x)}
=
2}.
\]


::: pf-proof

Multiply the limit in step <1>3 by \(2\).

:::

:::

::: pf-step

The final factor satisfies
\[
\boxed{
\lim_{x\to0}
\frac1{1+x}
=
1}.
\]


::: pf-proof

The function \(1/(1+x)\) is continuous at \(x=0\).

:::

:::

::: pf-step

Hence
\[
\boxed{
\lim_{x\to0}
\frac{\sin(2x)}{(1+x)\ln(1+x)}
=
1\cdot2\cdot1
=
2}.
\]


::: pf-proof

Apply the product law for limits to steps <1>1--<1>5.

:::

:::

::: pf-qed

Step <1>6 is the requested limit.

:::

:::
