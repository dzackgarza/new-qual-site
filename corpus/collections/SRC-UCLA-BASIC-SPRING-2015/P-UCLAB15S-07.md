---
schema: qual/card@1
id: P-UCLAB15S-07
kind: problem
title: Negativity of a quadratic form in three variables
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let
\[
f(x,y,z)=9x^2+6y^2+6z^2+12xy-10xz-2yz.
\]
Does there exist a point $(x,y,z)$ such that $f(x,y,z)<0$?
:::

::: {.solution}

No.

::: pf

::: {.pf-step #s1-1}

Complete the square in the variable $x$:
\[
\begin{aligned}
f(x,y,z)
&=
9
\left(
x+\frac23y-\frac59z
\right)^2\\
&\quad+
2y^2
+
\frac{14}{3}yz
+
\frac{29}{9}z^2.
\end{aligned}
\]


::: pf-proof

Expand the square:
\[
\begin{aligned}
9
\left(
x+\frac23y-\frac59z
\right)^2
&=
9x^2+12xy-10xz\\
&\quad+
4y^2
-
\frac{20}{3}yz
+
\frac{25}{9}z^2.
\end{aligned}
\]
Subtracting this from the original quadratic form leaves
\[
2y^2+\frac{14}{3}yz+\frac{29}{9}z^2.
\]

:::

:::

::: {.pf-step #s1-2}

Complete the square in the remaining variables:
\[
2y^2
+
\frac{14}{3}yz
+
\frac{29}{9}z^2
=
2
\left(
y+\frac76z
\right)^2
+
\frac12z^2.
\]


::: pf-proof

Expand:
\[
2
\left(
y+\frac76z
\right)^2
=
2y^2
+
\frac{14}{3}yz
+
\frac{49}{18}z^2.
\]
Adding
\[
\frac12z^2
=
\frac9{18}z^2
\]
gives
\[
2y^2
+
\frac{14}{3}yz
+
\frac{58}{18}z^2
=
2y^2
+
\frac{14}{3}yz
+
\frac{29}{9}z^2.
\]

:::

:::

::: {.pf-step #s1-3}

Therefore
\[
\boxed{
f(x,y,z)
=
9
\left(
x+\frac23y-\frac59z
\right)^2
+
2
\left(
y+\frac76z
\right)^2
+
\frac12z^2.
}
\]


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

One has
\[
f(x,y,z)\ge0
\]
for every
\[
(x,y,z)\in\RR^3.
\]


::: pf-proof

Every term on the right side of step [](#s1-3){.pf-ref} is a nonnegative scalar multiple of a square.
Thus their sum is nonnegative.

:::

:::

::: {.pf-step #s1-5}

Hence there is no point with
\[
f(x,y,z)<0.
\]


::: pf-proof

Step [](#s1-4){.pf-ref} rules out strict negativity everywhere.
Thus the answer is
\[
\boxed{\text{No}.}
\]

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
