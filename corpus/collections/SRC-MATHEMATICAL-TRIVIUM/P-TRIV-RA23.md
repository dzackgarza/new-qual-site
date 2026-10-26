---
schema: qual/card@1
id: P-TRIV-RA23
kind: problem
title: $\int_0^{x_0}\sqrt{1-x^2/x_0^2}\,dx$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 23, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $\int _ { 0 } ^ { x _ { 0 } } { \sqrt { 1 - { \frac { x ^ { 2 } } { x _ { 0 } ^ { 2 } } } } } d x .$
:::

Assume $x_0>0$.

::: pf

::: pf-step

Set
$$
u=\frac{x}{x_0}.
$$
Then
$$
x=x_0u,
\qquad
dx=x_0\,du.
$$


::: pf-proof

This is the linear change of variables $x=x_0u$.

:::

:::

::: pf-step

The limits transform as
$$
x=0\longmapsto u=0,
\qquad
x=x_0\longmapsto u=1.
$$


::: pf-proof

Substitute the endpoints into $u=x/x_0$.

:::

:::

::: pf-step

Therefore
$$
\int_0^{x_0}
\sqrt{1-\frac{x^2}{x_0^2}}\,dx
=
x_0
\int_0^1\sqrt{1-u^2}\,du.
$$


::: pf-proof

Substitute the relations from steps <1>1--<1>2.

:::

:::

::: pf-step

One has
$$
\int_0^1\sqrt{1-u^2}\,du
=
\frac\pi4.
$$


::: pf-proof

The graph
$$
v=\sqrt{1-u^2},
\qquad
0\leq u\leq1,
$$
is the upper-right quarter of the unit circle
$$
u^2+v^2=1.
$$
Hence the integral is the area of a quarter of a unit disk:
$$
\frac14\pi(1)^2
=
\frac\pi4.
$$

:::

:::

::: pf-step

Hence
$$
\boxed{
\int_0^{x_0}
\sqrt{1-\frac{x^2}{x_0^2}}\,dx
=
\frac{\pi x_0}{4}.
}
$$


::: pf-proof

Combine steps <1>3 and <1>4.

:::

:::

::: pf-qed

Step <1>5 is the required value.

:::

:::
