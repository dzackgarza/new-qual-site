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
Show that there is a constant $C$ such that every $C^2$ function $f:\mathbb R\to\mathbb R$ satisfies
\[
\left|\frac{f(0)+f(1)}2-\int_0^1f(x)\,dx\right|\le C\int_0^1|f''(x)|\,dx.
\]
:::

::: {.solution}
Define
\[
K(x)=\frac{x(1-x)}2.
\]

<1>1. One has
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

::: {.proof}
These follow by direct differentiation of
\[
K(x)=\frac{x-x^2}{2}.
\]
:::

<1>2. Integration by parts gives
\[
\int_0^1K(x)f''(x)\,dx
=
-
\int_0^1K'(x)f'(x)\,dx.
\]

::: {.proof}
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

<1>3. A second integration by parts gives
\[
\boxed{
\int_0^1K(x)f''(x)\,dx
=
\frac{f(0)+f(1)}2
-
\int_0^1f(x)\,dx.
}
\]

::: {.proof}
Starting from step <1>2,
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

<1>4. On the interval $[0,1]$,
\[
0\le K(x)\le\frac18.
\]

::: {.proof}
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

<1>5. Hence
\[
\left|
\int_0^1K(x)f''(x)\,dx
\right|
\le
\frac18
\int_0^1|f''(x)|\,dx.
\]

::: {.proof}
By the triangle inequality and step <1>4,
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

<1>6. Therefore
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

::: {.proof}
Use the identity from step <1>3 and the estimate from step <1>5.
Thus the desired inequality holds with
\[
\boxed{C=\frac18}.
\]
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required estimate.
:::
:::
