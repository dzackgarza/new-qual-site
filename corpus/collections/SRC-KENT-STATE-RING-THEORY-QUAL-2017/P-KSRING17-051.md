---
schema: qual/card@1
id: P-KSRING17-051
kind: problem
title: Ideals maximal with respect to missing a multiplicative set are prime
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 51 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a non-zero commutative ring with 1 and S a multiplicative subset of R not containing 0. Show that if P is maximal in the set of ideals of R not intersecting S, then P is a prime ideal.
:::

::: {.solution}
Assume
$$
P\cap S=\varnothing
$$
and that $P$ is maximal among ideals with this property.

<1>1. The ideal $P$ is proper.

::: {.proof}
By the standard definition of a multiplicative subset,
$$
1\in S.
$$
If
$$
P=R,
$$
then
$$
1\in P\cap S,
$$
contradicting
$$
P\cap S=\varnothing.
$$
Thus
$$
P\ne R.
$$
:::

<1>2. Suppose
$$
ab\in P
$$
and
$$
a\notin P.
$$
Then
$$
P+(a)
$$
meets $S$.

::: {.proof}
Since
$$
a\notin P,
$$
one has
$$
P\subsetneq P+(a).
$$
If
$$
(P+(a))\cap S=\varnothing,
$$
then $P+(a)$ would be an ideal disjoint from $S$ properly containing $P$, contradicting maximality of $P$.
Therefore
$$
(P+(a))\cap S\ne\varnothing.
$$
:::

<1>3. If also
$$
b\notin P,
$$
then
$$
P+(b)
$$
meets $S$.

::: {.proof}
This is the same argument as in step <1>2, with $b$ in place of $a$.
:::

<1>4. Under the assumptions
$$
ab\in P,
\qquad
a\notin P,
\qquad
b\notin P,
$$
choose
$$
s\in(P+(a))\cap S
$$
and
$$
t\in(P+(b))\cap S.
$$
Then there exist
$$
p,q\in P,
\qquad
r,u\in R
$$
such that
$$
s=p+ra,
\qquad
t=q+ub.
$$

::: {.proof}
Existence of $s$ and $t$ follows from steps <1>2--<1>3.
Membership in
$$
P+(a)
$$
and
$$
P+(b)
$$
gives the displayed decompositions.
:::

<1>5. The product
$$
st
$$
belongs to $P$.

::: {.proof}
Using the expressions from step <1>4,
$$
\begin{aligned}
st
&=
(p+ra)(q+ub)\\
&=
pq
+
pub
+
raq
+
ruab.
\end{aligned}
$$
Because
$$
p,q\in P
$$
and $P$ is an ideal,
$$
pq,pub,raq\in P.
$$
Also
$$
ab\in P,
$$
so
$$
ruab\in P.
$$
Thus
$$
st\in P.
$$
:::

<1>6. The product
$$
st
$$
also belongs to $S$.

::: {.proof}
By step <1>4,
$$
s,t\in S.
$$
Since $S$ is multiplicatively closed,
$$
st\in S.
$$
:::

<1>7. Therefore it is impossible to have
$$
ab\in P
$$
with both
$$
a\notin P
\qquad\text{and}\qquad
b\notin P.
$$

::: {.proof}
Steps <1>5--<1>6 give
$$
st\in P\cap S,
$$
contradicting
$$
P\cap S=\varnothing.
$$
:::

<1>8. Hence
$$
\boxed{P\text{ is prime}.}
$$

::: {.proof}
Step <1>1 shows $P$ is proper. Step <1>7 shows
$$
ab\in P
\implies
a\in P
\text{ or }
b\in P.
$$
These are exactly the defining conditions for a prime ideal.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required conclusion.
:::
:::
