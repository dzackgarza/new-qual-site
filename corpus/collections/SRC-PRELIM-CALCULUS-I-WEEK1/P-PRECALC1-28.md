---
schema: qual/card@1
id: P-PRECALC1-28
kind: problem
title: Riemann sum limit for $\int_0^3(x^2-x)\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in the limit of Problem 28 on page 6 of Week1_solns.pdf.
---

::: {.problem}
Calculate $\displaystyle\lim_{n \to \infty} \frac{3}{n} \sum_{i=1}^{n} \left[ \left(\frac{3i}{n}\right)^2 - \left(\frac{3i}{n}\right) \right]$.
:::

::: {.solution}
Let
\[
f(x)=x^2-x
\]
on \([0,3]\).

<1>1. Partition \([0,3]\) into \(n\) equal subintervals. Then
\[
\boxed{
\Delta x=\frac3n}.
\]

::: {.proof}
The interval length is \(3-0=3\), so dividing by \(n\) gives the common
width \(3/n\).
:::

<1>2. The right endpoint of the \(i\)th subinterval is
\[
\boxed{
x_i=\frac{3i}{n}}.
\]

::: {.proof}
Starting at \(0\), the \(i\)th right endpoint is
\[
0+i\Delta x
=
\frac{3i}{n}.
\]
:::

<1>3. Therefore the given expression is
\[
\boxed{
\sum_{i=1}^{n}
f(x_i)\,\Delta x}.
\]

::: {.proof}
Using steps <1>1--<1>2,
\[
f(x_i)
=
\left(\frac{3i}{n}\right)^2
-
\left(\frac{3i}{n}\right),
\]
so
\[
\sum_{i=1}^{n}
f(x_i)\Delta x
=
\frac3n
\sum_{i=1}^{n}
\left[
\left(\frac{3i}{n}\right)^2
-
\left(\frac{3i}{n}\right)
\right].
\]
:::

<1>4. Hence, as \(n\to\infty\), the expression converges to
\[
\int_0^3(x^2-x)\,dx.
\]

::: {.proof}
The function \(f\) is continuous on \([0,3]\), so its right-endpoint Riemann
sums converge to its definite integral.
:::

<1>5. An antiderivative is
\[
\boxed{
\frac{x^3}{3}-\frac{x^2}{2}}.
\]

::: {.proof}
Differentiate:
\[
\frac{d}{dx}
\left(
\frac{x^3}{3}-\frac{x^2}{2}
\right)
=
x^2-x.
\]
:::

<1>6. Therefore
\[
\begin{aligned}
\int_0^3(x^2-x)\,dx
&=
\left[
\frac{x^3}{3}-\frac{x^2}{2}
\right]_0^3\\
&=
9-\frac92.
\end{aligned}
\]

::: {.proof}
Substitute the endpoints.
:::

<1>7. Hence
\[
\boxed{
\int_0^3(x^2-x)\,dx
=
\frac92}.
\]

::: {.proof}
\[
9-\frac92
=
\frac{18}{2}-\frac92
=
\frac92.
\]
:::

<1>8. Consequently,
\[
\boxed{
\lim_{n\to\infty}
\frac3n
\sum_{i=1}^{n}
\left[
\left(\frac{3i}{n}\right)^2
-
\left(\frac{3i}{n}\right)
\right]
=
\frac92}.
\]

::: {.proof}
Combine steps <1>3--<1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the requested limit.
:::
:::
