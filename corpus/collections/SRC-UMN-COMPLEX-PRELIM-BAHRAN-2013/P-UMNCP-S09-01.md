---
schema: qual/card@1
id: P-UMNCP-S09-01
kind: problem
title: Sublinear square-root growth forces an entire function to be constant
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
  note: Checked against Spring 2009, 1 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Suppose $f$ is entire and
$$
\frac{f(z)}{1+|z|^{1/2}}
$$
is bounded as $|z|\to\infty$. Prove that $f$ is constant.
:::

::: {.solution}

By hypothesis, there exist constants
$$
C>0
$$
and
$$
R_0>0
$$
such that
$$
|f(z)|
\le
C\left(
1+|z|^{1/2}
\right)
$$
whenever
$$
|z|\ge R_0.
$$

::: pf

::: {.pf-step #s1-1}

For every
$$
R\ge R_0,
$$
one has
$$
\max_{|z|=R}|f(z)|
\le
C(1+R^{1/2}).
$$


::: pf-proof

This is the growth hypothesis restricted to the circle
$$
|z|=R.
$$

:::

:::

::: {.pf-step #s1-2}

For every integer
$$
m\ge1,
$$
one has
$$
\boxed{f^{(m)}(0)=0}.
$$


::: pf-proof

Fix
$$
m\ge1.
$$
Cauchy's estimate on the circle
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
Cm!
\left(
R^{-m}
+R^{1/2-m}
\right).
$$
Since
$$
m\ge1,
$$
both exponents
$$
-m
\quad\text{and}\quad
\frac12-m
$$
are negative. Letting
$$
R\to\infty
$$
forces the right-hand side to tend to zero. Hence
$$
f^{(m)}(0)=0.
$$

:::

:::

::: {.pf-step #s1-3}

The Taylor series of $f$ at $0$ is constant.


::: pf-proof

Because $f$ is entire,
$$
f(z)
=
\sum_{m=0}^{\infty}
\frac{f^{(m)}(0)}{m!}z^m.
$$
By step [](#s1-2){.pf-ref}, every coefficient with
$$
m\ge1
$$
vanishes. Therefore
$$
f(z)=f(0)
$$
for every $z$.

:::

:::

::: {.pf-step #s1-4}

Thus
$$
\boxed{f\text{ is constant}.}
$$


::: pf-proof

This is exactly the conclusion of step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the claim.

:::

:::

:::
