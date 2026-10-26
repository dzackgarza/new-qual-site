---
schema: qual/card@1
id: P-UCLAB09S-03
kind: problem
title: Compatibility and uniqueness of quadratic Hermite data
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Problem 3. We seek a quadratic polynomial $P$ satisfying
\[
P(0)=\alpha,\qquad P'(0)=\beta,\qquad P(1)=\gamma,\qquad P'(1)=\delta.
\]

(a) Under what condition on $(\alpha,\beta,\gamma,\delta)$ can these constraints be met?

(b) When they can be met, determine $P$.
Is it unique?
Explain.
:::

Write a general quadratic polynomial as
\[
P(x)=a+bx+cx^2.
\]

::: pf

::: pf-step

The conditions at $x=0$ force
\[
a=\alpha
\qquad\text{and}\qquad
b=\beta.
\]


::: pf-proof

One has
\[
P(0)=a
\]
and
\[
P'(x)=b+2cx,
\]
so
\[
P'(0)=b.
\]
The prescribed values
\[
P(0)=\alpha,
\qquad
P'(0)=\beta
\]
therefore give
\[
a=\alpha,
\qquad
b=\beta.
\]

:::

:::

::: pf-step

The condition
\[
P(1)=\gamma
\]
then forces
\[
\boxed{c=\gamma-\alpha-\beta}.
\]


::: pf-proof

Using step <1>1,
\[
P(1)
=
\alpha+\beta+c.
\]
Setting this equal to $\gamma$ gives
\[
c=\gamma-\alpha-\beta.
\]

:::

:::

::: pf-step

For the polynomial determined by steps <1>1--<1>2,
\[
P'(1)
=
2\gamma-2\alpha-\beta.
\]


::: pf-proof

Since
\[
P'(x)
=
\beta+2cx,
\]
step <1>2 gives
\[
\begin{aligned}
P'(1)
&=
\beta
+
2(\gamma-\alpha-\beta)\\
&=
2\gamma-2\alpha-\beta.
\end{aligned}
\]

:::

:::

::: pf-step

A necessary condition for all four constraints to be satisfied is
\[
\boxed{
\delta
=
2\gamma-2\alpha-\beta
}.
\]


::: pf-proof

Any polynomial satisfying the first three conditions must have the coefficients determined in steps <1>1--<1>2.
For that polynomial, step <1>3 computes
\[
P'(1)=2\gamma-2\alpha-\beta.
\]
The fourth condition
\[
P'(1)=\delta
\]
therefore requires the displayed equality.

:::

:::

::: pf-step

The condition in step <1>4 is also sufficient.


::: pf-proof

Assume
\[
\delta
=
2\gamma-2\alpha-\beta.
\]
Define
\[
\boxed{
P(x)
=
\alpha
+
\beta x
+
(\gamma-\alpha-\beta)x^2
}.
\]
Then
\[
P(0)=\alpha
\]
and
\[
P'(0)=\beta
\]
by inspection.
Also
\[
\begin{aligned}
P(1)
&=
\alpha+\beta+\gamma-\alpha-\beta\\
&=
\gamma.
\end{aligned}
\]
Finally, step <1>3 gives
\[
P'(1)
=
2\gamma-2\alpha-\beta
=
\delta.
\]
Thus all four constraints hold.

:::

:::

::: pf-step

Whenever the constraints are compatible, the polynomial is unique.


::: pf-proof

The first condition forces the constant coefficient
\[
a=\alpha.
\]
The second forces the linear coefficient
\[
b=\beta.
\]
The third then forces the quadratic coefficient
\[
c=\gamma-\alpha-\beta.
\]
Thus there is at most one quadratic polynomial satisfying the first three constraints, and therefore at most one satisfying all four.
Step <1>5 constructs one when the compatibility condition holds.
Hence it is unique.

:::

:::

::: pf-step

Therefore the complete answer is:
\[
\boxed{
\delta=2\gamma-2\alpha-\beta
}
\]
is necessary and sufficient, and in that case
\[
\boxed{
P(x)
=
\alpha+\beta x+(\gamma-\alpha-\beta)x^2
}
\]
is the unique solution.


::: pf-proof

Necessity is step <1>4, sufficiency is step <1>5, and uniqueness is step <1>6.

:::

:::

::: pf-qed

Step <1>7 answers parts (a) and (b).

:::

:::
