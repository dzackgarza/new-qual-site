---
schema: qual/card@1
id: P-KSRING17-106
kind: problem
title: Units of a polynomial ring over an integral domain are constants
classification:
  areas: [algebra]
  topics:
  - Polynomial Rings
  - Units
  - Integral Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 106 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that if R is an integral domain and $f ( x )$ is a unit in the polynomial ring $R [ x ]$ , then $f ( x )$ is in R.
:::

::: {.solution}

Assume
$$
f(x)\in R[x]
$$
is a unit.

::: pf

::: {.pf-step #s1-1}

There exists
$$
g(x)\in R[x]
$$
such that
$$
f(x)g(x)=1.
$$


::: pf-proof

This is the definition of $f(x)$ being a unit in $R[x]$.

:::

:::

::: {.pf-step #s1-2}

If
$$
u,v\in R[x]
$$
are nonzero, then
$$
\deg(uv)
=
\deg u+\deg v.
$$


::: pf-proof

Write
$$
u
=
a_mx^m+\text{ lower terms},
$$
and
$$
v
=
b_nx^n+\text{ lower terms},
$$
with
$$
a_m,b_n\ne0.
$$
The leading coefficient of $uv$ is
$$
a_mb_n.
$$
Because $R$ is an integral domain,
$$
a_mb_n\ne0.
$$
Hence the leading term of $uv$ has degree
$$
m+n,
$$
so
$$
\deg(uv)
=
m+n
=
\deg u+\deg v.
$$

:::

:::

::: {.pf-step #s1-3}

The polynomials
$$
f
\qquad\text{and}\qquad
g
$$
from step [](#s1-1){.pf-ref} are both nonzero.


::: pf-proof

Their product is
$$
1\ne0.
$$
Hence neither factor can be zero.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\deg f
=
\deg g
=
0.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref},
$$
\begin{aligned}
0
&=
\deg1\\
&=
\deg(fg)\\
&=
\deg f+\deg g.
\end{aligned}
$$
Both degrees are nonnegative integers.
Their sum is zero, so
$$
\deg f=\deg g=0.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
f(x)\in R.
}
$$


::: pf-proof

A polynomial has degree zero exactly when it is a nonzero constant polynomial.
Step [](#s1-4){.pf-ref} gives
$$
\deg f=0.
$$
Thus $f$ belongs to the coefficient ring $R$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
