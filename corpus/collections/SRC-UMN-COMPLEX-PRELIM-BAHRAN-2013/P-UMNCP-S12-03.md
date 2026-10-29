---
schema: qual/card@1
id: P-UMNCP-S12-03
kind: problem
title: Polynomial growth forces an entire function to be a polynomial
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Spring 2012, 3 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let \(f\) be entire.
Suppose there are positive real numbers \(a,b,k\) such that
\[
|f(z)|\le a+b|z|^k
\]
for every \(z\in\CC\). Prove that \(f\) is a polynomial.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every
$$
R>0,
$$
one has
$$
\max_{|z|=R}|f(z)|
\le
a+bR^k.
$$


::: pf-proof

This is the assumed growth estimate restricted to the circle
$$
|z|=R.
$$

:::

:::

::: {.pf-step #s1-2}

Fix an integer
$$
m>k.
$$
Then
$$
\boxed{f^{(m)}(0)=0}.
$$


::: pf-proof

Cauchy's estimate for the $m$th derivative on the circle
$$
|z|=R
$$
gives
$$
|f^{(m)}(0)|
\le
\frac{m!}{R^m}
\max_{|z|=R}|f(z)|.
$$
Using step [](#s1-1){.pf-ref},
$$
|f^{(m)}(0)|
\le
m!
\left(
\frac a{R^m}
+bR^{k-m}
\right).
$$
Since
$$
m>k,
$$
both exponents
$$
-m
\quad\text{and}\quad
k-m
$$
are negative. Letting
$$
R\to\infty
$$
forces the right-hand side to tend to $0$. Hence
$$
f^{(m)}(0)=0.
$$

:::

:::

::: {.pf-step #s1-3}

Every Taylor coefficient of degree strictly larger than $k$ vanishes.


::: pf-proof

The coefficient of
$$
z^m
$$
in the Taylor expansion of $f$ at the origin is
$$
\frac{f^{(m)}(0)}{m!}.
$$
Step [](#s1-2){.pf-ref} shows that this is zero for every integer
$$
m>k.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
f
$$
is a polynomial of degree at most
$$
\boxed{\lfloor k\rfloor}.
$$


::: pf-proof

Since $f$ is entire, its Taylor series at $0$ converges everywhere:
$$
f(z)
=
\sum_{m=0}^{\infty}
\frac{f^{(m)}(0)}{m!}z^m.
$$
By step [](#s1-3){.pf-ref}, all terms with
$$
m>k
$$
vanish. The largest possible integer exponent that remains is
$$
\lfloor k\rfloor.
$$
Thus the series is finite.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the required polynomiality, with the sharper degree bound.

:::

:::

:::
