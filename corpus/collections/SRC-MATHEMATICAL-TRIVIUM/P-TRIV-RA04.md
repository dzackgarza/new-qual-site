---
schema: qual/card@1
id: P-TRIV-RA04
kind: problem
title: $f^{(100)}(0)$ for $f(x)=(x^{100}+x)e^{100x}$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $f ^ { ( 1 0 0 ) } ( 0 )$ , if $f ( x ) = ( x ^ { 1 0 0 } + x ) e ^ { 1 0 0 x }$
:::

::: pf

::: pf-step

Expand
$$
e^{100x}
=
\sum_{k=0}^{\infty}
\frac{100^k}{k!}x^k.
$$


::: pf-proof

This is the Taylor series of the exponential function.

:::

:::

::: pf-step

The coefficient of $x^{100}$ in
$$
x^{100}e^{100x}
$$
is $1$.


::: pf-proof

To obtain degree $100$, one must multiply $x^{100}$ by the constant term $1$
of the exponential series.

:::

:::

::: pf-step

The coefficient of $x^{100}$ in
$$
x e^{100x}
$$
is
$$
\frac{100^{99}}{99!}.
$$


::: pf-proof

To obtain degree $100$, the factor $x$ must be multiplied by the $x^{99}$ term
of the exponential series, whose coefficient is $100^{99}/99!$.

:::

:::

::: pf-step

Therefore the coefficient of $x^{100}$ in $f(x)$ is
$$
1+\frac{100^{99}}{99!}.
$$


::: pf-proof

Add the contributions from steps <1>2--<1>3.

:::

:::

::: pf-step

Hence
$$
f^{(100)}(0)
=
100!
\left(
1+\frac{100^{99}}{99!}
\right).
$$


::: pf-proof

For a Taylor series
$$
f(x)=\sum_{k=0}^{\infty}a_kx^k,
$$
one has
$$
f^{(100)}(0)=100!a_{100}.
$$
Apply step <1>4.

:::

:::

::: pf-step

Thus
$$
\boxed{f^{(100)}(0)=100!+100^{100}}.
$$


::: pf-proof

Since
$$
\frac{100!}{99!}=100,
$$
the second term in step <1>5 is
$$
100\cdot100^{99}=100^{100}.
$$

:::

:::

::: pf-qed

Step <1>6 is the required value.

:::

:::
