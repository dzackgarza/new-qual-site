---
schema: qual/card@1
id: P-KSRING17-125
kind: problem
title: Extension of prime ideals to a localization of a domain
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 125 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be an integral domain, S a multiplicative set, and let $\begin{array} { r } { S ^ { - 1 } R = \{ \frac { r } { s } \ | \ r \in R , \ s \in S \} } \end{array}$ (contained in the field of fractions of R). Show that if P is a prime ideal of R, then $S ^ { - 1 } P$ is either a prime ideal of $S ^ { - 1 } R$ or else equals $S ^ { - 1 } R$
:::

::: {.solution}
Recall
$$
S^{-1}P
\coloneqq
\left\{
\frac ps:
p\in P,\ s\in S
\right\}.
$$

<1>1. If
$$
P\cap S\ne\varnothing,
$$
then
$$
S^{-1}P
=
S^{-1}R.
$$

::: {.proof}
Choose
$$
s\in P\cap S.
$$
Then
$$
\frac ss
=
1
$$
belongs to
$$
S^{-1}P.
$$
Any ideal containing the identity is the whole ring.
Therefore
$$
S^{-1}P
=
S^{-1}R.
$$
:::

<1>2. Assume now that
$$
P\cap S=\varnothing.
$$
If
$$
\frac as
\in
S^{-1}P,
$$
then
$$
a\in P.
$$

::: {.proof}
Membership in
$$
S^{-1}P
$$
means there exist
$$
p\in P,
\qquad
t\in S
$$
such that
$$
\frac as
=
\frac pt
$$
in the field of fractions of $R$.
Because $R$ is a domain,
$$
at=ps.
$$
The right-hand side lies in $P$, so
$$
at\in P.
$$
Since
$$
t\in S
$$
and
$$
P\cap S=\varnothing,
$$
one has
$$
t\notin P.
$$
Primality of $P$ therefore forces
$$
a\in P.
$$
:::

<1>3. Conversely, if
$$
a\in P
$$
and
$$
s\in S,
$$
then
$$
\frac as
\in
S^{-1}P.
$$

::: {.proof}
This is immediate from the definition of
$$
S^{-1}P.
$$
:::

<1>4. Under the assumption
$$
P\cap S=\varnothing,
$$
one has
$$
\boxed{
\frac as\in S^{-1}P
\iff
a\in P.
}
$$

::: {.proof}
Combine steps <1>2 and <1>3.
:::

<1>5. Under the same assumption,
$$
S^{-1}P
$$
is proper.

::: {.proof}
The identity is
$$
1=\frac11.
$$
Since
$$
P
$$
is proper,
$$
1\notin P.
$$
By step <1>4,
$$
\frac11
\notin
S^{-1}P.
$$
Thus
$$
S^{-1}P
\ne
S^{-1}R.
$$
:::

<1>6. Let
$$
\frac as,\frac bt
\in
S^{-1}R
$$
and suppose
$$
\frac as\frac bt
\in
S^{-1}P.
$$
Then
$$
ab\in P.
$$

::: {.proof}
The product is
$$
\frac{ab}{st}.
$$
Since
$$
s,t\in S,
$$
one has
$$
st\in S.
$$
By step <1>4,
$$
\frac{ab}{st}
\in
S^{-1}P
$$
implies
$$
ab\in P.
$$
:::

<1>7. Under the assumptions of step <1>6,
$$
a\in P
\quad\text{or}\quad
b\in P.
$$

::: {.proof}
Step <1>6 gives
$$
ab\in P.
$$
Since
$$
P
$$
is prime,
$$
a\in P
\quad\text{or}\quad
b\in P.
$$
:::

<1>8. Therefore
$$
\frac as
\in
S^{-1}P
\quad\text{or}\quad
\frac bt
\in
S^{-1}P.
$$

::: {.proof}
Apply step <1>4 to the conclusion of step <1>7.
:::

<1>9. Hence, if
$$
P\cap S=\varnothing,
$$
then
$$
\boxed{
S^{-1}P
\text{ is a prime ideal of }S^{-1}R.
}
$$

::: {.proof}
Step <1>5 gives properness.
Steps <1>6--<1>8 give the prime-product condition.
:::

<1>10. Consequently,
$$
\boxed{
S^{-1}P
\text{ is either prime or equal to }S^{-1}R.
}
$$

::: {.proof}
If
$$
P\cap S\ne\varnothing,
$$
step <1>1 gives the whole ring.
If
$$
P\cap S=\varnothing,
$$
step <1>9 gives a prime ideal.
These are the two exhaustive cases.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the required conclusion.
:::
:::
