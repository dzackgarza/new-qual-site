---
schema: qual/card@1
id: P-UCLAB17S-08
kind: problem
title: A trapezoid-rule error estimate by the second derivative
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Show that there is a constant $C$ such that every $C^2$ function $f:\RR\to\RR$ satisfies
\[
\left|\frac{f(0)+f(1)}2-\int_0^1f(x)\,dx\right|\le C\int_0^1|f''(x)|\,dx.
\]
:::

::: {.solution}

Define
\[
K(x)=\frac{x(1-x)}2.
\]

::: pf

::: pf-step

One has
\[
K(0)=K(1)=0,
\]
\[
K'(x)=\frac{1-2x}{2},
\]
and
\[
K''(x)=-1.
\]


::: pf-proof

These follow by direct differentiation of
\[
K(x)=\frac{x-x^2}{2}.
\]

:::

:::

::: {.pf-step #s1-2}

Integration by parts gives
\[
\int_0^1K(x)f''(x)\,dx
=
-
\int_0^1K'(x)f'(x)\,dx.
\]


::: pf-proof

Since
\[
K(0)=K(1)=0,
\]
\[
\begin{aligned}
\int_0^1Kf''
&=
\bigl[Kf'\bigr]_0^1
-
\int_0^1K'f'\\
&=
-
\int_0^1K'f'.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-3}

A second integration by parts gives
\[
\boxed{
\int_0^1K(x)f''(x)\,dx
=
\frac{f(0)+f(1)}2
-
\int_0^1f(x)\,dx.
}
\]


::: pf-proof

Starting from step [](#s1-2){.pf-ref},
\[
\begin{aligned}
-\int_0^1K'f'
&=
-
\bigl[K'f\bigr]_0^1
+
\int_0^1K''f.
\end{aligned}
\]
Now
\[
K'(0)=\frac12,
\qquad
K'(1)=-\frac12,
\]
so
\[
\bigl[K'f\bigr]_0^1
=
-\frac12f(1)
-
\frac12f(0).
\]
Therefore
\[
-
\bigl[K'f\bigr]_0^1
=
\frac{f(0)+f(1)}2.
\]
Also
\[
K''=-1,
\]
so
\[
\int_0^1K''f
=
-
\int_0^1f.
\]
Combine the terms.

:::

:::

::: {.pf-step #s1-4}

On the interval $[0,1]$,
\[
0\le K(x)\le\frac18.
\]


::: pf-proof

The quadratic
\[
K(x)=\frac{x(1-x)}2
\]
is nonnegative on $[0,1]$.
Its maximum occurs at
\[
x=\frac12,
\]
where
\[
K\left(\frac12\right)
=
\frac{(1/2)(1/2)}2
=
\frac18.
\]

:::

:::

::: {.pf-step #s1-5}

Hence
\[
\left|
\int_0^1K(x)f''(x)\,dx
\right|
\le
\frac18
\int_0^1|f''(x)|\,dx.
\]


::: pf-proof

By the triangle inequality and step [](#s1-4){.pf-ref},
\[
\begin{aligned}
\left|
\int_0^1Kf''
\right|
&\le
\int_0^1
|K(x)|\,|f''(x)|
\,dx\\
&\le
\frac18
\int_0^1|f''(x)|\,dx.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-6}

Therefore
\[
\boxed{
\left|
\frac{f(0)+f(1)}2
-
\int_0^1f(x)\,dx
\right|
\le
\frac18
\int_0^1|f''(x)|\,dx.
}
\]


::: pf-proof

Use the identity from step [](#s1-3){.pf-ref} and the estimate from step [](#s1-5){.pf-ref}.
Thus the desired inequality holds with
\[
\boxed{C=\frac18}.
\]

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required estimate.

:::

:::

:::
