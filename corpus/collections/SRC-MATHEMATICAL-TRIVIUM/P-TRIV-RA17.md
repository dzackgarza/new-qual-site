---
schema: qual/card@1
id: P-TRIV-RA17
kind: problem
title: $\int\frac{x^5+2}{x^2-1}\,dx$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 17, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
$\mathrm { C a l c u l a t e } \int \frac { x ^ { 5 } + 2 } { x ^ { 2 } - 1 } d x$
:::

::: pf

::: pf-step

Polynomial division gives
$$
\frac{x^5+2}{x^2-1}
=
x^3+x
+
\frac{x+2}{x^2-1}.
$$


::: pf-proof

One has
$$
(x^2-1)(x^3+x)
=
x^5-x.
$$
Subtracting from $x^5+2$ leaves the remainder $x+2$.

:::

:::

::: pf-step

The proper rational term decomposes as
$$
\frac{x+2}{x^2-1}
=
\frac{3/2}{x-1}
-
\frac{1/2}{x+1}.
$$


::: pf-proof

Write
$$
\frac{x+2}{(x-1)(x+1)}
=
\frac{A}{x-1}
+
\frac{B}{x+1}.
$$
Then
$$
x+2
=
A(x+1)+B(x-1)
=
(A+B)x+(A-B).
$$
Thus
$$
A+B=1,
\qquad
A-B=2,
$$
so
$$
A=\frac32,
\qquad
B=-\frac12.
$$

:::

:::

::: pf-step

Therefore
$$
\int\frac{x^5+2}{x^2-1}\,dx
=
\int(x^3+x)\,dx
+
\frac32\int\frac{dx}{x-1}
-
\frac12\int\frac{dx}{x+1}.
$$


::: pf-proof

Substitute steps <1>1--<1>2 into the integral and use linearity.

:::

:::

::: pf-step

Hence
$$
\boxed{
\int\frac{x^5+2}{x^2-1}\,dx
=
\frac{x^4}{4}
+
\frac{x^2}{2}
+
\frac32\log|x-1|
-
\frac12\log|x+1|
+
C.
}
$$


::: pf-proof

Integrate each term in step <1>3.

:::

:::

::: pf-qed

Step <1>4 is the required antiderivative on each interval avoiding
$x=\pm1$.

:::

:::
