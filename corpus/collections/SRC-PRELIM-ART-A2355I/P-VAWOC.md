---
schema: qual/card@1
id: P-VAWOC
kind: problem
title: Taylor series of $\ln x$ at $1$, approximating $\ln 1.1$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Derived the logarithmic Taylor series from the geometric series, justified the radius of convergence, and bounded the alternating-series remainder to obtain the two-decimal approximation."
---

::: {.problem}
Work out the Taylor series for $f(x) = \ln x$ around $x=1$ and use it to approximate $\ln(1.1)$ accurate to 2 decimal places.
:::

::: {.solution}
The Taylor series about $x=1$ is
$$
\boxed{\ln x=\sum_{n=1}^{\infty}(-1)^{n+1}\frac{(x-1)^n}{n},\qquad |x-1|<1.}
$$
In particular,
$$
\boxed{\ln(1.1)\approx 0.10}
$$
to two decimal places.

<1>1. Derive the series from the geometric series.
::: {.proof}
For $|t|<1$,
$$
\frac1{1+t}=\sum_{n=0}^{\infty}(-1)^n t^n.
$$
The power series converges uniformly on every closed interval
$[-r,r]$ with $0<r<1$, so it may be integrated term by term.
Thus, for $|u|<1$,
$$
\ln(1+u)
=\int_0^u\frac{dt}{1+t}
=\sum_{n=0}^{\infty}(-1)^n\frac{u^{n+1}}{n+1}
=\sum_{n=1}^{\infty}(-1)^{n+1}\frac{u^n}{n}.
$$
Setting $u=x-1$ gives the displayed Taylor series. Its radius of
convergence is one because the geometric series used above has radius one.
:::

<1>2. Evaluate at $x=1.1$ and control the error.
::: {.proof}
Putting $u=0.1$ gives the alternating series
$$
\ln(1.1)=0.1-\frac{0.1^2}{2}+\frac{0.1^3}{3}-\cdots.
$$
Its terms decrease in absolute value to zero. Using the first two terms,
$$
S_2=0.1-0.005=0.095.
$$
The alternating-series remainder satisfies
$$
|\ln(1.1)-S_2|\leq\frac{0.1^3}{3}=\frac1{3000}<0.00034.
$$
Hence
$$
0.09466<\ln(1.1)<0.09534,
$$
so rounding to two decimal places gives $0.10$.
:::
:::
