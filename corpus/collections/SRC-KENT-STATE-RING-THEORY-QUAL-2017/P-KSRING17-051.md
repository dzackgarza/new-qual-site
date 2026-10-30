---
schema: qual/card@1
id: P-KSRING17-051
kind: problem
title: Ideals maximal with respect to missing a multiplicative set are prime
classification:
  areas: [algebra]
  topics:
  - Prime Ideals
  - Multiplicative Sets
  - Zorn's Lemma
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

::: pf

::: {.pf-step #s1-1}

The ideal $P$ is proper.


::: pf-proof

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

:::

::: {.pf-step #s1-2}

Suppose
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


::: pf-proof

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

:::

::: {.pf-step #s1-3}

If also
$$
b\notin P,
$$
then
$$
P+(b)
$$
meets $S$.


::: pf-proof

This is the same argument as in step [](#s1-2){.pf-ref}, with $b$ in place of $a$.

:::

:::

::: {.pf-step #s1-4}

Under the assumptions
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


::: pf-proof

Existence of $s$ and $t$ follows from steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.
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

:::

::: {.pf-step #s1-5}

The product
$$
st
$$
belongs to $P$.


::: pf-proof

Using the expressions from step [](#s1-4){.pf-ref},
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

:::

::: {.pf-step #s1-6}

The product
$$
st
$$
also belongs to $S$.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
s,t\in S.
$$
Since $S$ is multiplicatively closed,
$$
st\in S.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore it is impossible to have
$$
ab\in P
$$
with both
$$
a\notin P
\qquad\text{and}\qquad
b\notin P.
$$


::: pf-proof

Steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} give
$$
st\in P\cap S,
$$
contradicting
$$
P\cap S=\varnothing.
$$

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\boxed{P\text{ is prime}.}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} shows $P$ is proper. Step [](#s1-7){.pf-ref} shows
$$
ab\in P
\implies
a\in P
\text{ or }
b\in P.
$$
These are exactly the defining conditions for a prime ideal.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
