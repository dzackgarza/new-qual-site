---
schema: qual/card@1
id: P-KSRING17-058
kind: problem
title: A ring in which every ideal is prime is a field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 58 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with 1 in which every ideal is a prime ideal.
Prove that R is a field.
(Hint: For $a \neq 0$ consider the ideals (a) and $( a ^ { 2 } ) . \mathrm { , }$ )
:::

::: {.remark}
Erratum: the literal statement cannot hold under the standard definition of prime ideal, because the improper ideal $R$ itself is never prime. The intended hypothesis is that every proper ideal of $R$ is prime.
:::

Assume the corrected hypothesis that every proper ideal of $R$ is prime.

::: pf

::: pf-step

The zero ideal is prime.


::: pf-proof

If
$$
(0)=R,
$$
then
$$
1=0
$$
and the ring is the zero ring, which is not a field under the usual convention. Thus in the intended nonzero setting,
$$
(0)
\subsetneq
R.
$$
By hypothesis, every proper ideal is prime, so
$$
(0)
$$
is prime.

:::

:::

::: pf-step

The ring $R$ is an integral domain.


::: pf-proof

Since
$$
(0)
$$
is prime by step <1>1, whenever
$$
ab=0,
$$
one has
$$
ab\in(0),
$$
and therefore
$$
a\in(0)
\quad\text{or}\quad
b\in(0).
$$
Thus
$$
a=0
\quad\text{or}\quad
b=0.
$$
Hence $R$ is a domain.

:::

:::

::: pf-step

Let
$$
0\ne a\in R.
$$
If
$$
(a)=R,
$$
then $a$ is a unit.


::: pf-proof

The equality
$$
(a)=R
$$
means
$$
1\in(a).
$$
Hence
$$
1=ar
$$
for some
$$
r\in R.
$$
Thus $a$ is invertible.

:::

:::

::: pf-step

Suppose instead that
$$
(a)
\subsetneq
R.
$$
Then
$$
(a^2)
\subsetneq
R
$$
and therefore
$$
(a^2)
$$
is prime.


::: pf-proof

Since
$$
(a^2)\subseteq(a)
$$
and
$$
(a)\subsetneq R,
$$
the ideal
$$
(a^2)
$$
is proper. By the corrected hypothesis, every proper ideal is prime.

:::

:::

::: pf-step

Under the assumptions of step <1>4,
$$
a\in(a^2).
$$


::: pf-proof

One has
$$
a\cdot a
=
a^2
\in
(a^2).
$$
Since
$$
(a^2)
$$
is prime, primality implies
$$
a\in(a^2).
$$

:::

:::

::: pf-step

The element $a$ is a unit.


::: pf-proof

By step <1>5, there exists
$$
r\in R
$$
such that
$$
a
=
a^2r.
$$
Hence
$$
a(1-ar)=0.
$$
Because $R$ is an integral domain by step <1>2 and
$$
a\ne0,
$$
one must have
$$
1-ar=0.
$$
Thus
$$
ar=1,
$$
so $a$ is invertible.

:::

:::

::: pf-step

Every nonzero element of $R$ is a unit.


::: pf-proof

Let
$$
0\ne a\in R.
$$
If
$$
(a)=R,
$$
step <1>3 gives invertibility. If
$$
(a)\subsetneq R,
$$
steps <1>4--<1>6 give invertibility. Thus every nonzero element is a unit.

:::

:::

::: pf-step

Therefore
$$
\boxed{R\text{ is a field}.}
$$


::: pf-proof

The ring is commutative with identity, and by step <1>7 every nonzero element is invertible.

:::

:::

::: pf-qed

Step <1>8 proves the corrected statement intended by the source.

:::

:::
