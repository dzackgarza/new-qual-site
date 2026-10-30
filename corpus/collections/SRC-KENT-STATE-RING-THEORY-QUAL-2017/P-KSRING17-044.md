---
schema: qual/card@1
id: P-KSRING17-044
kind: problem
title: Ideals $I$ with $1+I$ consisting of units lie in the Jacobson radical
classification:
  areas: [algebra]
  topics:
  - Jacobson Radical
  - Maximal Ideals
  - Units
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

::: pf

::: pf-step

Suppose, for contradiction, that
$$
I\nsubseteq M.
$$
Then there exists
$$
a\in I\setminus M.
$$


::: pf-proof

This is exactly the negation of
$$
I\subseteq M.
$$

:::

:::

::: {.pf-step #s1-2}

The ideal
$$
M+(a)
$$
is equal to $R$.


::: pf-proof

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

:::

::: {.pf-step #s1-3}

There exist
$$
m\in M,
\qquad
r\in R
$$
such that
$$
1=m+ra.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
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

:::

::: {.pf-step #s1-4}

The element
$$
m=1-ra
$$
is a unit of $R$.


::: pf-proof

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

:::

::: {.pf-step #s1-5}

No element of a proper ideal can be a unit.


::: pf-proof

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

:::

::: {.pf-step #s1-6}

The assumption
$$
I\nsubseteq M
$$
is impossible.


::: pf-proof

Step [](#s1-3){.pf-ref} gives
$$
m\in M,
$$
while step [](#s1-4){.pf-ref} says that $m$ is a unit. This contradicts step [](#s1-5){.pf-ref}.
Therefore
$$
I\subseteq M.
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
I
\subseteq
\bigcap_{\mathfrak m\in\operatorname{MaxSpec}R}\mathfrak m
=
J(R).
}
$$


::: pf-proof

The maximal ideal $M$ was arbitrary. By step [](#s1-6){.pf-ref},
$$
I\subseteq M
$$
for every maximal ideal $M$ of $R$. Taking the intersection over all such $M$ gives the displayed containment.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is exactly the required conclusion.

:::

:::

:::
