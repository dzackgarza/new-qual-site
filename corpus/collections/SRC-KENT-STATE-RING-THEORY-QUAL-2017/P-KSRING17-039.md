---
schema: qual/card@1
id: P-KSRING17-039
kind: problem
title: An ideal is maximal if and only if the quotient is a field
classification:
  areas: [algebra]
  topics:
  - Maximal Ideals
  - Fields
  - Quotient Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 39 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a non-zero commutative ring with 1. Show that an ideal M of R is maximal if and only if $R / M$ is a field.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assume
$$
M
$$
is a maximal ideal of $R$.
Then
$$
R/M
$$
is a nonzero commutative ring with identity.


::: pf-proof

Because a maximal ideal is proper,
$$
M\ne R.
$$
Hence
$$
1+M\ne0+M,
$$
so the quotient is nonzero. Since $R$ is commutative with identity, so is $R/M$.

:::

:::

::: {.pf-step #s1-2}

Let
$$
r+M
\ne
0+M
$$
in
$$
R/M.
$$
Then
$$
M+(r)=R.
$$


::: pf-proof

The condition
$$
r+M\ne0+M
$$
means
$$
r\notin M.
$$
Thus the ideal
$$
M+(r)
$$
properly contains $M$. Since $M$ is maximal,
$$
M+(r)=R.
$$

:::

:::

::: {.pf-step #s1-3}

Every nonzero element of $R/M$ is invertible.


::: pf-proof

Let
$$
r+M\ne0+M.
$$
By step [](#s1-2){.pf-ref},
$$
1\in M+(r).
$$
Hence there exist
$$
m\in M,
\qquad
a\in R
$$
such that
$$
1=m+ar.
$$
Modulo $M$,
$$
(a+M)(r+M)
=
ar+M
=
1+M.
$$
Thus
$$
a+M
$$
is the inverse of
$$
r+M.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore, if $M$ is maximal, then
$$
\boxed{R/M\text{ is a field}.}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives a nonzero commutative ring with identity, and step [](#s1-3){.pf-ref} shows every nonzero element is invertible.

:::

:::

::: {.pf-step #s1-5}

Conversely, assume
$$
R/M
$$
is a field.
Then $M$ is a proper ideal.


::: pf-proof

A field is nonzero, so
$$
R/M\ne0.
$$
Hence
$$
M\ne R.
$$

:::

:::

::: {.pf-step #s1-6}

Let
$$
I
$$
be an ideal satisfying
$$
M\subsetneq I.
$$
Then
$$
I=R.
$$


::: pf-proof

Choose
$$
r\in I\setminus M.
$$
Then
$$
r+M
$$
is a nonzero element of the field $R/M$, so there exists
$$
s\in R
$$
such that
$$
(s+M)(r+M)
=
1+M.
$$
Thus
$$
sr-1\in M.
$$
Since
$$
M\subseteq I
$$
and
$$
r\in I,
$$
one has
$$
sr\in I
$$
and
$$
sr-1\in I.
$$
Therefore
$$
1
=
sr-(sr-1)
\in I.
$$
Hence
$$
I=R.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore, if $R/M$ is a field, then
$$
\boxed{M\text{ is maximal}.}
$$


::: pf-proof

Step [](#s1-5){.pf-ref} shows that $M$ is proper. Step [](#s1-6){.pf-ref} shows that every ideal properly containing $M$ is the whole ring. This is exactly maximality.

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\boxed{
M\text{ is maximal}
\iff
R/M\text{ is a field}.
}
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required equivalence.

:::

:::

:::
