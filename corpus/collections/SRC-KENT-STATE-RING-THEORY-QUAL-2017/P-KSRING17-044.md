---
schema: qual/card@1
id: P-KSRING17-044
kind: problem
title: Ideals $I$ with $1+I$ consisting of units lie in the Jacobson radical
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 44 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a non-zero commutative ring with 1. Show that if I is an ideal of R such that $1 + a$ is a unit in R for all $a \in I ,$ , then I is contained in every maximal ideal of R.
:::

::: {.solution}
Let
$$
M
$$
be an arbitrary maximal ideal of $R$.

<1>1. Suppose, for contradiction, that
$$
I\nsubseteq M.
$$
Then there exists
$$
a\in I\setminus M.
$$

::: {.proof}
This is exactly the negation of
$$
I\subseteq M.
$$
:::

<1>2. The ideal
$$
M+(a)
$$
is equal to $R$.

::: {.proof}
Since
$$
a\notin M,
$$
the ideal
$$
M+(a)
$$
properly contains $M$. By maximality of $M$,
$$
M+(a)=R.
$$
:::

<1>3. There exist
$$
m\in M,
\qquad
r\in R
$$
such that
$$
1=m+ra.
$$

::: {.proof}
By step <1>2,
$$
1\in M+(a).
$$
Thus
$$
1=m+ra
$$
for suitable
$$
m\in M,
\qquad
r\in R.
$$
:::

<1>4. The element
$$
m=1-ra
$$
is a unit of $R$.

::: {.proof}
Since
$$
a\in I
$$
and $I$ is an ideal,
$$
-ra\in I.
$$
The hypothesis says that
$$
1+c
$$
is a unit for every
$$
c\in I.
$$
Apply this with
$$
c=-ra.
$$
Then
$$
1-ra=m
$$
is a unit.
:::

<1>5. No element of a proper ideal can be a unit.

::: {.proof}
If
$$
u\in M
$$
were a unit, then
$$
1
=
u^{-1}u
\in M
$$
because $M$ is an ideal. This would imply
$$
M=R,
$$
contradicting maximality.
:::

<1>6. The assumption
$$
I\nsubseteq M
$$
is impossible.

::: {.proof}
Step <1>3 gives
$$
m\in M,
$$
while step <1>4 says that $m$ is a unit. This contradicts step <1>5.
Therefore
$$
I\subseteq M.
$$
:::

<1>7. Hence
$$
\boxed{
I
\subseteq
\bigcap_{\mathfrak m\in\operatorname{MaxSpec}R}\mathfrak m
=
J(R).
}
$$

::: {.proof}
The maximal ideal $M$ was arbitrary. By step <1>6,
$$
I\subseteq M
$$
for every maximal ideal $M$ of $R$. Taking the intersection over all such $M$ gives the displayed containment.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is exactly the required conclusion.
:::
:::
