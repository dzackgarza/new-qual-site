---
schema: qual/card@1
id: P-KSRING17-039
kind: problem
title: An ideal is maximal if and only if the quotient is a field
classification:
  areas: [algebra]
  topics: []
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
<1>1. Assume
$$
M
$$
is a maximal ideal of $R$.
Then
$$
R/M
$$
is a nonzero commutative ring with identity.

::: {.proof}
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

<1>2. Let
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

::: {.proof}
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

<1>3. Every nonzero element of $R/M$ is invertible.

::: {.proof}
Let
$$
r+M\ne0+M.
$$
By step <1>2,
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

<1>4. Therefore, if $M$ is maximal, then
$$
\boxed{R/M\text{ is a field}.}
$$

::: {.proof}
Step <1>1 gives a nonzero commutative ring with identity, and step <1>3 shows every nonzero element is invertible.
:::

<1>5. Conversely, assume
$$
R/M
$$
is a field.
Then $M$ is a proper ideal.

::: {.proof}
A field is nonzero, so
$$
R/M\ne0.
$$
Hence
$$
M\ne R.
$$
:::

<1>6. Let
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

::: {.proof}
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

<1>7. Therefore, if $R/M$ is a field, then
$$
\boxed{M\text{ is maximal}.}
$$

::: {.proof}
Step <1>5 shows that $M$ is proper. Step <1>6 shows that every ideal properly containing $M$ is the whole ring. This is exactly maximality.
:::

<1>8. Hence
$$
\boxed{
M\text{ is maximal}
\iff
R/M\text{ is a field}.
}
$$

::: {.proof}
Combine steps <1>4 and <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required equivalence.
:::
:::
