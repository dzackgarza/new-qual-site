---
schema: qual/card@1
id: P-KSRING17-070
kind: problem
title: Commutative rings with exactly three ideals
classification:
  areas: [algebra]
  topics:
  - Ideals
  - Local Rings
  - Units
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 70 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with identity that has exactly three ideals, {0}, I, and R.

(a) Show that if $a \not \in I ,$ then a is a unit of R.

(b) Show that if $a , b \in I$ then $a b = 0$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
a\notin I.
$$
Then the principal ideal
$$
(a)
$$
is neither
$$
(0)
$$
nor
$$
I.
$$


::: pf-proof

Since
$$
0\in I,
$$
the condition
$$
a\notin I
$$
implies
$$
a\ne0.
$$
Hence
$$
(a)\ne(0).
$$
Also
$$
a\in(a)
$$
but
$$
a\notin I,
$$
so
$$
(a)\ne I.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
(a)=R.
$$


::: pf-proof

By hypothesis, the only ideals of $R$ are
$$
(0),
\qquad
I,
\qquad
R.
$$
Step [](#s1-1){.pf-ref} excludes the first two possibilities for
$$
(a),
$$
so the only remaining possibility is
$$
(a)=R.
$$

:::

:::

::: {.pf-step #s1-3}

Hence every
$$
a\notin I
$$
is a unit.


::: pf-proof

From step [](#s1-2){.pf-ref},
$$
1\in(a).
$$
Thus there exists
$$
r\in R
$$
such that
$$
ar=1.
$$
Since $R$ is commutative, $r$ is a two-sided inverse of $a$.
Therefore
$$
\boxed{
a\notin I
\implies
a\in R^\times.
}
$$

:::

:::

::: {.pf-step #s1-4}

Let
$$
a,b\in I.
$$
Suppose, for contradiction, that
$$
ab\ne0.
$$
Then
$$
(ab)=I.
$$


::: pf-proof

Because
$$
ab\in I
$$
and $I$ is an ideal,
$$
(ab)\subseteq I.
$$
Since
$$
ab\ne0,
$$
the ideal
$$
(ab)
$$
is nonzero.
The only nonzero proper ideal is $I$, so
$$
(ab)=I.
$$

:::

:::

::: {.pf-step #s1-5}

Under the assumption of step [](#s1-4){.pf-ref}, there exists
$$
r\in R
$$
such that
$$
a=abr.
$$


::: pf-proof

Because
$$
a\in I
=
(ab),
$$
the element $a$ is a multiple of $ab$:
$$
a=(ab)r
$$
for some
$$
r\in R.
$$

:::

:::

::: {.pf-step #s1-6}

One has
$$
1-br\notin I.
$$


::: pf-proof

Since
$$
b\in I
$$
and $I$ is an ideal,
$$
br\in I.
$$
If
$$
1-br\in I,
$$
then
$$
1
=
(1-br)+br
\in I,
$$
which would imply
$$
I=R,
$$
contradicting the hypothesis that $I$ is the proper middle ideal.
Therefore
$$
1-br\notin I.
$$

:::

:::

::: {.pf-step #s1-7}

The element
$$
1-br
$$
is a unit.


::: pf-proof

This follows immediately from step [](#s1-3){.pf-ref} and step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

The assumption
$$
ab\ne0
$$
is impossible.


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
a=abr,
$$
so
$$
a(1-br)=0.
$$
By step [](#s1-7){.pf-ref},
$$
1-br
$$
is a unit.
Multiplying by its inverse gives
$$
a=0.
$$
But then
$$
ab=0,
$$
contradicting the assumption
$$
ab\ne0.
$$

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{
a,b\in I
\implies
ab=0.
}
$$


::: pf-proof

Step [](#s1-8){.pf-ref} rules out the only alternative.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-9){.pf-ref} proves part (b).

:::

:::

:::
