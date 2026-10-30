---
schema: qual/card@1
id: P-KSRING17-066
kind: problem
title: Irreducible ideals, prime ideals and nilpotents
classification:
  areas: [algebra]
  topics:
  - Irreducible Ideals
  - Prime Ideals
  - Nilpotent Elements
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 66 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a commutative ring with identity. An ideal $I$ of $R$ is irreducible if it cannot be expressed as the intersection of two ideals of $R$ neither of which is contained in the other. Show the following.

(a) If $P$ is a prime ideal then $P$ is irreducible.

(b) If $x$ is a non-zero element of $R$, then there is an ideal $I_{x}$, maximal with respect to the property that $x \notin I_{x}$, and $I_{x}$ is irreducible.

(c) If every irreducible ideal of $R$ is a prime ideal, then $0$ is the only nilpotent element of $R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
P
$$
be a prime ideal and suppose
$$
P=I\cap J
$$
for ideals
$$
I,J\trianglelefteq R.
$$
If neither $I$ nor $J$ contains the other, choose
$$
a\in I\setminus J,
\qquad
b\in J\setminus I.
$$


::: pf-proof

This is exactly the meaning of incomparability under inclusion.

:::

:::

::: {.pf-step #s1-2}

Under the assumptions of step [](#s1-1){.pf-ref},
$$
a\notin P,
\qquad
b\notin P,
$$
but
$$
ab\in P.
$$


::: pf-proof

Since
$$
P=I\cap J,
$$
the condition
$$
a\notin J
$$
implies
$$
a\notin P.
$$
Similarly,
$$
b\notin I
$$
implies
$$
b\notin P.
$$

Because
$$
a\in I
$$
and $I$ is an ideal,
$$
ab\in I.
$$
Because
$$
b\in J
$$
and $J$ is an ideal,
$$
ab\in J.
$$
Therefore
$$
ab\in I\cap J
=
P.
$$

:::

:::

::: {.pf-step #s1-3}

Every prime ideal is irreducible.


::: pf-proof

If
$$
P=I\cap J
$$
with $I$ and $J$ incomparable, step [](#s1-2){.pf-ref} gives
$$
ab\in P
$$
with
$$
a,b\notin P,
$$
contradicting primality of $P$.
Hence no such decomposition exists, and
$$
\boxed{P\text{ is irreducible}.}
$$

:::

:::

::: {.pf-step #s1-4}

Fix
$$
0\ne x\in R
$$
and let
$$
\mathcal P_x
\coloneqq
\{
I\trianglelefteq R:
x\notin I
\},
$$
ordered by inclusion.
Then $\mathcal P_x$ is nonempty.


::: pf-proof

Since
$$
x\ne0,
$$
one has
$$
x\notin(0).
$$
Thus
$$
(0)\in\mathcal P_x.
$$

:::

:::

::: {.pf-step #s1-5}

Every chain in $\mathcal P_x$ has an upper bound in $\mathcal P_x$.


::: pf-proof

Let
$$
\mathcal C
\subseteq
\mathcal P_x
$$
be a chain and set
$$
U
\coloneqq
\bigcup_{I\in\mathcal C}I.
$$
Because $\mathcal C$ is totally ordered by inclusion, the union $U$ is an ideal.

If
$$
x\in U,
$$
then
$$
x\in I
$$
for some
$$
I\in\mathcal C,
$$
contradicting
$$
I\in\mathcal P_x.
$$
Thus
$$
x\notin U,
$$
so
$$
U\in\mathcal P_x.
$$
Clearly every member of the chain lies in $U$, so $U$ is an upper bound.

:::

:::

::: {.pf-step #s1-6}

There exists an ideal
$$
I_x
$$
maximal with respect to the property
$$
x\notin I_x.
$$


::: pf-proof

By steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}, Zorn's lemma applies to $\mathcal P_x$.
Hence there exists a maximal element
$$
I_x\in\mathcal P_x.
$$

:::

:::

::: {.pf-step #s1-7}

The ideal $I_x$ is irreducible.


::: pf-proof

Suppose
$$
I_x=J\cap K.
$$
If both
$$
J
\quad\text{and}\quad
K
$$
properly contain $I_x$, maximality of $I_x$ among ideals avoiding $x$ forces
$$
x\in J
$$
and
$$
x\in K.
$$
Hence
$$
x\in J\cap K
=
I_x,
$$
contradicting
$$
x\notin I_x.
$$

Therefore at least one of $J,K$ equals $I_x$.
In particular, $I_x$ cannot be written as an intersection of two incomparable ideals, so
$$
\boxed{I_x\text{ is irreducible}.}
$$

:::

:::

::: {.pf-step #s1-8}

Assume every irreducible ideal of $R$ is prime.
Suppose, for contradiction, that
$$
0\ne x\in R
$$
is nilpotent.


::: pf-proof

This sets up the contradiction argument for part (c).

:::

:::

::: {.pf-step #s1-9}

Let $I_x$ be the irreducible ideal from steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}.
Then $I_x$ is prime and
$$
x\notin I_x.
$$


::: pf-proof

By construction,
$$
x\notin I_x.
$$
By step [](#s1-7){.pf-ref}, $I_x$ is irreducible.
Under the hypothesis of part (c), every irreducible ideal is prime.
Therefore
$$
I_x
$$
is prime.

:::

:::

::: {.pf-step #s1-10}

The nilpotence of $x$ forces
$$
x\in I_x,
$$
a contradiction.


::: pf-proof

Choose
$$
n\ge1
$$
such that
$$
x^n=0.
$$
Since
$$
0\in I_x,
$$
one has
$$
x^n\in I_x.
$$
Because $I_x$ is prime, repeated application of primality to
$$
x^n
=
x\cdot x^{n-1}
$$
implies
$$
x\in I_x.
$$
This contradicts step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{
0
\text{ is the only nilpotent element of }R.
}
$$


::: pf-proof

Steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref} show that no nonzero nilpotent element can exist.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), steps [](#s1-4){.pf-ref} through [](#s1-7){.pf-ref} prove part (b), and step [](#s1-11){.pf-ref} proves part (c).

:::

:::

:::
