---
schema: qual/card@1
id: P-TRIV-CA29
kind: problem
title: Stirling's approximation from the Gamma integral
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 29, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find Stirling's approximation: consider $\begin{array} { r } { n ! = \Gamma ( n + 1 ) = \int _ { 0 } ^ { \infty } x ^ { n } e ^ { - x } d x } \end{array}$ for $n \gg 1$
:::

::: {.solution}
<1>1. With the substitution
$$
x=ny,
$$
one has
$$
n!
=
n^{n+1}
\int_0^\infty
e^{n(\log y-y)}
\,dy.
$$

::: {.proof}
Since
$$
dx=n\,dy
$$
and
$$
x^ne^{-x}
=
n^ny^ne^{-ny}
=
n^n e^{n(\log y-y)},
$$
the formula follows.
:::

<1>2. The phase
$$
\phi(y)=\log y-y
$$
has a unique maximum at
$$
y_0=1.
$$

::: {.proof}
One has
$$
\phi'(y)
=
\frac1y-1,
$$
which vanishes only at $y=1$. Also
$$
\phi''(y)
=
-\frac1{y^2}<0
$$
for every $y>0$. Thus $y=1$ is the unique maximum.
:::

<1>3. At the saddle,
$$
\phi(1)=-1,
\qquad
\phi''(1)=-1.
$$

::: {.proof}
Direct substitution gives the two values.
:::

<1>4. Near $y=1$,
$$
\phi(y)
=
-1
-
\frac{(y-1)^2}{2}
+
O((y-1)^3).
$$

::: {.proof}
This is the Taylor expansion at $y=1$, using step <1>3 and
$$
\phi'(1)=0.
$$
:::

<1>5. The integral in step <1>1 satisfies
$$
\int_0^\infty
e^{n\phi(y)}
\,dy
\sim
e^{-n}
\sqrt{\frac{2\pi}{n}}.
$$

::: {.proof}
The unique maximum in step <1>2 is nondegenerate. Put
$$
y
=
1+\frac{u}{\sqrt n}.
$$
Then step <1>4 gives
$$
n\phi(y)
=
-n
-
\frac{u^2}{2}
+
O\left(\frac{|u|^3}{\sqrt n}\right).
$$
Thus the mass of the integral is concentrated in a neighborhood of width
$O(n^{-1/2})$ around $1$, and Laplace's method gives
$$
\int_0^\infty
e^{n\phi(y)}
\,dy
\sim
\frac{e^{-n}}{\sqrt n}
\int_{-\infty}^{\infty}
e^{-u^2/2}
\,du.
$$
The Gaussian integral equals $\sqrt{2\pi}$.
:::

<1>6. Therefore
$$
n!
\sim
n^{n+1}
e^{-n}
\sqrt{\frac{2\pi}{n}}.
$$

::: {.proof}
Substitute step <1>5 into step <1>1.
:::

<1>7. Hence Stirling's approximation is
$$
\boxed{
n!
\sim
\sqrt{2\pi n}
\left(\frac ne\right)^n
}
$$
as $n\to\infty$.

::: {.proof}
Simplify the expression in step <1>6:
$$
n^{n+1}e^{-n}
\sqrt{\frac{2\pi}{n}}
=
\sqrt{2\pi n}
\,n^ne^{-n}.
$$
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is Stirling's formula.
:::
:::
