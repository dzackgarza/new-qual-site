---
schema: qual/card@1
id: P-PRECALC1-27
kind: problem
title: Limit of $\int_1^n x^{-n}\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Calculate
\[
\lim_{n\to\infty}\int_1^n\frac{dx}{x^n}.
\]
:::

For integers \(n\ge2\), define
\[
I_n
=
\int_1^n x^{-n}\,dx.
\]

::: pf

::: pf-step

Since \(n\ne1\),
\[
\boxed{
\int x^{-n}\,dx
=
\frac{x^{1-n}}{1-n}}.
\]


::: pf-proof

Differentiate:
\[
\frac{d}{dx}
\left(
\frac{x^{1-n}}{1-n}
\right)
=
x^{-n}.
\]

:::

:::

::: pf-step

Therefore
\[
I_n
=
\left[
\frac{x^{1-n}}{1-n}
\right]_1^n.
\]


::: pf-proof

Apply the fundamental theorem of calculus using step <1>1.

:::

:::

::: pf-step

Hence
\[
I_n
=
\frac{n^{1-n}-1}{1-n}.
\]


::: pf-proof

Substitute the endpoints \(x=n\) and \(x=1\).

:::

:::

::: pf-step

Rewriting,
\[
\boxed{
I_n
=
\frac{1-n^{1-n}}{n-1}}.
\]


::: pf-proof

Multiply numerator and denominator in step <1>3 by \(-1\).

:::

:::

::: pf-step

One has
\[
\boxed{
0<n^{1-n}\le1}
\]
for \(n\ge2\).


::: pf-proof

Since
\[
n^{1-n}
=
\frac1{n^{n-1}},
\]
the denominator is at least \(1\).

:::

:::

::: pf-step

Therefore
\[
0
\le
I_n
\le
\frac1{n-1}.
\]


::: pf-proof

From step <1>5,
\[
0\le1-n^{1-n}\le1.
\]
Divide by the positive number \(n-1\).

:::

:::

::: pf-step

Since
\[
\frac1{n-1}\to0,
\]
the squeeze theorem gives
\[
\boxed{
I_n\to0}.
\]


::: pf-proof

Apply the squeeze theorem to step <1>6.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\lim_{n\to\infty}
\int_1^n\frac{dx}{x^n}
=
0}.
\]


::: pf-proof

This is step <1>7.

:::

:::

::: pf-qed

Step <1>8 is the requested limit.

:::

:::
