---
schema: qual/card@1
id: P-RASP11C
kind: problem
title: "Schur-type test: integral kernels bounded on pairings extend to bounded operators"
classification:
  areas:
  - real-analysis
  topics:
  - Integral Operators
  - Schur Test
  - Holder Inequality
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Spring 2011 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $1 \leq p, p' \leq \infty$ be fixed dual indices.
Suppose $K(x, y) \geq 0$ is a Lebesgue measurable function on $\mathbb{R}^n \times \mathbb{R}^n$ such that there exists a constant $0 \leq K_0 < \infty$ with
$$
\iint g(x) K(x, y) f(y) \, dx \, dy \leq K_0 \|g\|_{L^{p'}(\mathbb{R}^n)} \|f\|_{L^p(\mathbb{R}^n)}
$$
for all measurable $f, g \geq 0$ on $\mathbb{R}^n$.
Show that if $f \in L^p(\mathbb{R}^n)$, then the function $Kf(x) := \int_{\mathbb{R}^n} K(x, y) f(y) \, dy$ is well defined for (Lebesgue) a.e. $x \in \mathbb{R}^n$, and one has $\|Kf\|_{L^p(dx)} \leq K_0 \|f\|_{L^p(dx)}$.
:::

::: solution
<1>1. Apply the hypothesis to the nonnegative function $|f|$.
::: proof
Define the extended-valued measurable function
\[
h(x):=\int_{\mathbb R^n}K(x,y)|f(y)|\,dy.
\]
By Tonelli, $h$ is measurable and takes values in $[0,\infty]$. For every nonnegative $g\in L^{p'}$,
\[
\int_{\mathbb R^n}g(x)h(x)\,dx
=\iint g(x)K(x,y)|f(y)|\,dx\,dy
\le K_0\|g\|_{p'}\|f\|_p.
\]
:::

<1>2. Deduce that $h\in L^p$ and estimate its norm.
::: proof
For a nonnegative measurable function $h$, the dual norm formula gives
\[
\|h\|_p
=\sup\left\{\int gh:\ g\ge0,\ g\in L^{p'},\ \|g\|_{p'}\le1\right\},
\]
with the usual endpoint interpretations for $p=1$ and $p=\infty$.

Applying Step 1 to every such $g$ yields
\[
\|h\|_p\le K_0\|f\|_p.
\]
In particular $h(x)<\infty$ for almost every $x$.

For completeness, the endpoint cases are contained in the same argument: if $p=1$, test with bounded nonnegative $g$ approaching $1$ to obtain $\int h\le K_0\|f\|_1$; if $p=\infty$, the estimate against every nonnegative $g\in L^1$ implies
\[
\operatorname*{ess\,sup}h\le K_0\|f\|_\infty.
\]
:::

<1>3. Define $Kf$ almost everywhere and conclude the operator bound.
::: proof
At every $x$ for which $h(x)<\infty$,
\[
\int_{\mathbb R^n}K(x,y)|f(y)|\,dy<\infty.
\]
Hence the integral
\[
Kf(x)=\int_{\mathbb R^n}K(x,y)f(y)\,dy
\]
is absolutely convergent and therefore well defined. Moreover,
\[
|Kf(x)|\le h(x)
\]
almost everywhere. Thus
\[
\boxed{\|Kf\|_p\le\|h\|_p\le K_0\|f\|_p.}
\]
:::
:::
