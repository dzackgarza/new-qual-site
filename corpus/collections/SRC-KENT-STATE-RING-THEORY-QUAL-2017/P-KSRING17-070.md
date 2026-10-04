---
schema: qual/card@1
id: P-KSRING17-070
kind: problem
title: Commutative rings with exactly three ideals
classification:
  areas: [algebra]
  topics: []
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
<1>1. Let
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

::: {.proof}
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

<1>2. Therefore
$$
(a)=R.
$$

::: {.proof}
By hypothesis, the only ideals of $R$ are
$$
(0),
\qquad
I,
\qquad
R.
$$
Step <1>1 excludes the first two possibilities for
$$
(a),
$$
so the only remaining possibility is
$$
(a)=R.
$$
:::

<1>3. Hence every
$$
a\notin I
$$
is a unit.

::: {.proof}
From step <1>2,
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

<1>4. Let
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

::: {.proof}
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

<1>5. Under the assumption of step <1>4, there exists
$$
r\in R
$$
such that
$$
a=abr.
$$

::: {.proof}
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

<1>6. One has
$$
1-br\notin I.
$$

::: {.proof}
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

<1>7. The element
$$
1-br
$$
is a unit.

::: {.proof}
This follows immediately from step <1>3 and step <1>6.
:::

<1>8. The assumption
$$
ab\ne0
$$
is impossible.

::: {.proof}
By step <1>5,
$$
a=abr,
$$
so
$$
a(1-br)=0.
$$
By step <1>7,
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

<1>9. Therefore
$$
\boxed{
a,b\in I
\implies
ab=0.
}
$$

::: {.proof}
Step <1>8 rules out the only alternative.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), and step <1>9 proves part (b).
:::
:::
