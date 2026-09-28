---
schema: qual/card@1
id: P-BKS15-1A
kind: problem
title: Evaluate an integral and bound $22/7-\pi$
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
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the polynomial division, exact integral, positivity, and the 1/256 pointwise bound.
---

::: {.problem}
(a) Evaluate
\[
\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx.
\]
(b) Prove that
\[
0<\frac{22}{7}-\pi<\frac1{256}.
\]
:::

::: {.solution}
<1>1. One has the identity
$$
\frac{x^4(1-x)^4}{1+x^2}
=
x^6-4x^5+5x^4-4x^2+4
-
\frac4{1+x^2}.
$$

::: {.proof}
Multiplying the right-hand side by $1+x^2$ gives
$$
\begin{aligned}
&(1+x^2)
\left(
x^6-4x^5+5x^4-4x^2+4
\right)
-4\\
&\qquad=
x^8-4x^7+6x^6-4x^5+x^4\\
&\qquad=
x^4(1-x)^4.
\end{aligned}
$$
Divide by $1+x^2$.
:::

<1>2. The polynomial part integrates to
$$
\int_0^1
\left(
x^6-4x^5+5x^4-4x^2+4
\right)\,dx
=
\frac{22}{7}.
$$

::: {.proof}
Termwise integration gives
$$
\begin{aligned}
&\frac17
-
\frac46
+
\frac55
-
\frac43
+
4\\
&\qquad=
\frac17-\frac23+1-\frac43+4\\
&\qquad=
\frac17+3
=
\frac{22}{7}.
\end{aligned}
$$
:::

<1>3. One has
$$
4\int_0^1\frac{dx}{1+x^2}
=
\pi.
$$

::: {.proof}
Since
$$
\frac{d}{dx}\arctan x
=
\frac1{1+x^2},
$$
one obtains
$$
4\int_0^1\frac{dx}{1+x^2}
=
4\left(\arctan1-\arctan0\right)
=
4\cdot\frac\pi4
=
\pi.
$$
:::

<1>4. Therefore
$$
\boxed{
\int_0^1
\frac{x^4(1-x)^4}{1+x^2}\,dx
=
\frac{22}{7}-\pi
}.
$$

::: {.proof}
Integrate the identity in step <1>1 and apply steps <1>2 and <1>3. This
proves part (a).
:::

<1>5. For every $x\in[0,1]$,
$$
0
\leq
x(1-x)
\leq
\frac14.
$$

::: {.proof}
Complete the square:
$$
x(1-x)
=
\frac14
-
\left(x-\frac12\right)^2.
$$
Nonnegativity follows from $0\leq x\leq1$.
:::

<1>6. For every $x\in[0,1]$,
$$
0
\leq
\frac{x^4(1-x)^4}{1+x^2}
<
\frac1{256},
$$
and the integrand is positive for $0<x<1$.

::: {.proof}
By step <1>5,
$$
x^4(1-x)^4
=
\bigl(x(1-x)\bigr)^4
\leq
\frac1{4^4}
=
\frac1{256}.
$$
Also
$$
1+x^2\geq1.
$$
The upper inequality is strict: equality in the numerator bound requires
$x=1/2$, where $1+x^2>1$; at the points where the denominator equals
$1$, the numerator is $0$. Positivity on $(0,1)$ is immediate.
:::

<1>7. Consequently,
$$
\boxed{
0
<
\frac{22}{7}-\pi
<
\frac1{256}
}.
$$

::: {.proof}
By step <1>4,
$$
\frac{22}{7}-\pi
$$
is the integral of the function in step <1>6 over an interval of length
$1$. Its strict positivity gives the left inequality, while its strict
pointwise upper bound gives
$$
\frac{22}{7}-\pi
<
\int_0^1\frac1{256}\,dx
=
\frac1{256}.
$$
This proves part (b).
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>4 proves part (a), and step <1>7 proves part (b).
:::
:::
