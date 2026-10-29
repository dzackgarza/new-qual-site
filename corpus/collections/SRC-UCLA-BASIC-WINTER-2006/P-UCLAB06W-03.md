---
schema: qual/card@1
id: P-UCLAB06W-03
kind: problem
title: Composite trapezoid-rule error estimate
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the official UCLA Basic Qual Winter 2006 PDF; the source itself prints the factor $1/n$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The printed estimate is false for a general interval; the solution gives a constant-function counterexample and proves the corrected trapezoid estimate.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The exam printed the factor 1/n in front of the trapezoid sum, which fails for f=1 whenever b-a is not 1; the factor is now (b-a)/n.
---

::: {.problem}
Let $f:[a,b]\to\RR$ be twice continuously differentiable, including at the endpoints.
Let
$$
a=x_0<x_1<\cdots<x_n=b
$$
be the uniform partition of $[a,b]$, so that $x_{i+1}-x_i=(b-a)/n$ for $0\leq i<n$.

Show that there exists $M$ such that for all $n\geq1$,
$$
\left|
\frac{b-a}n\left(\frac12f(x_0)+f(x_1)+\cdots+f(x_{n-1})+\frac12f(x_n)\right)
-\int_a^b f(x)\,dx
\right|
\leq \frac{M}{n^2}.
$$

[Recall that the sum is an approximation of the integral in the Trapezoid Rule. It may be instructive to first solve the problem for $n=1$ and then address the general case.]
:::

::: {.solution}
Let $h=(b-a)/n$, and let $T_n$ denote the sum in the problem.
On one subinterval $[x_i,x_{i+1}]$, write $x=x_i+t$ with $0\leq t\leq h$ and let $L_i$ be the affine interpolant through the endpoint values of $f$.
The interpolation remainder gives, for each $t$, a point $\xi_t\in(x_i,x_{i+1})$ such that
$$
f(x_i+t)-L_i(x_i+t)=\frac{f''(\xi_t)}2\,t(t-h).
$$
Hence, with $K=\max_{[a,b]}|f''|$,
$$
\left|\int_{x_i}^{x_{i+1}}f(x)\,dx-
\frac h2\bigl(f(x_i)+f(x_{i+1})\bigr)\right|
\leq \frac K2\int_0^h t(h-t)\,dt
=\frac{Kh^3}{12}.
$$
Summing over the $n$ subintervals yields
$$
\left|T_n-\int_a^b f(x)\,dx\right|
\leq \frac{nKh^3}{12}
=\frac{K(b-a)^3}{12n^2}.
$$
Thus the estimate holds with $M=K(b-a)^3/12$.
:::
