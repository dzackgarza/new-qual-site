---
schema: qual/card@1
id: P-KSRING17-128
kind: problem
title: Contraction of an ideal from a ring of fractions is an ideal
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 128 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a commutative ring with $1$ and $D$ a multiplicative subset of $R$ containing $1$. Let $J$ be an ideal in the ring of fractions $D^{-1}R$ and let
$$
I = \left\{a \in R \st \frac{a}{d} \in J \text{ for some } d \in D\right\}.
$$
Show that $I$ is an ideal of $R$.
:::

::: {.solution}

Let
$$
\iota:R\to D^{-1}R
$$
be the canonical homomorphism
$$
\iota(a)
\coloneqq
\frac a1.
$$

::: pf

::: {.pf-step #s1-1}

If
$$
a\in I,
$$
then
$$
\frac a1
\in
J.
$$


::: pf-proof

By definition of $I$, there exists
$$
d\in D
$$
such that
$$
\frac ad
\in
J.
$$
Since
$$
J
$$
is an ideal of
$$
D^{-1}R,
$$
it is closed under multiplication by arbitrary elements of the localization.
Multiply by
$$
\frac d1:
$$
$$
\frac d1\frac ad
=
\frac a1.
$$
Hence
$$
\frac a1
\in
J.
$$

:::

:::

::: {.pf-step #s1-2}

If
$$
\frac a1
\in
J,
$$
then
$$
a\in I.
$$


::: pf-proof

Since
$$
1\in D,
$$
the definition of $I$ applies with
$$
d=1.
$$
Thus
$$
a\in I.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
I
=
\left\{
a\in R:
\frac a1\in J
\right\}
=
\iota^{-1}(J).
}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} prove the two inclusions.

:::

:::

::: {.pf-step #s1-4}

The element
$$
0
$$
belongs to $I$.


::: pf-proof

Since
$$
J
$$
is an ideal,
$$
0
\in
J.
$$
But
$$
\frac01
=
0.
$$
Thus step [](#s1-3){.pf-ref} gives
$$
0\in I.
$$

:::

:::

::: {.pf-step #s1-5}

If
$$
a,b\in I,
$$
then
$$
a-b\in I.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\frac a1,\frac b1
\in
J.
$$
Since $J$ is an additive subgroup,
$$
\frac a1-\frac b1
=
\frac{a-b}{1}
\in
J.
$$
Applying step [](#s1-3){.pf-ref} again gives
$$
a-b\in I.
$$

:::

:::

::: {.pf-step #s1-6}

If
$$
r\in R
$$
and
$$
a\in I,
$$
then
$$
ra\in I.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\frac a1
\in
J.
$$
The element
$$
\frac r1
\in
D^{-1}R
$$
may multiply elements of the ideal $J$, so
$$
\frac r1\frac a1
=
\frac{ra}{1}
\in
J.
$$
Step [](#s1-3){.pf-ref} then gives
$$
ra\in I.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
I
\trianglelefteq
R.
}
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives nonemptiness, step [](#s1-5){.pf-ref} gives closure under subtraction, and step [](#s1-6){.pf-ref} gives absorption under multiplication by arbitrary elements of $R$.
Thus $I$ is an ideal.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
