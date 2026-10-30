---
schema: qual/card@1
id: P-KSRING17-055
kind: problem
title: Unions and intersections of chains of prime ideals are prime
classification:
  areas: [algebra]
  topics:
  - Prime Ideals
  - Chains of Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 55 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a commutative ring with identity and let $\mathcal{C}$ be a chain of prime ideals of $R$. Show that $\bigcup_{P \in \mathcal{C}} P$ and $\bigcap_{P \in \mathcal{C}} P$ are prime ideals of $R$.
:::

::: {.solution}

Set
$$
U
\coloneqq
\bigcup_{P\in\mathcal C}P
$$
and
$$
I
\coloneqq
\bigcap_{P\in\mathcal C}P.
$$

::: pf

::: pf-step

The set $U$ is an ideal of $R$.


::: pf-proof

Let
$$
x,y\in U.
$$
Then
$$
x\in P,
\qquad
y\in Q
$$
for some
$$
P,Q\in\mathcal C.
$$
Because $\mathcal C$ is a chain, either
$$
P\subseteq Q
$$
or
$$
Q\subseteq P.
$$
Thus $x$ and $y$ lie in a common member of the chain, and therefore
$$
x-y\in U.
$$

If
$$
r\in R
$$
and
$$
x\in U,
$$
choose
$$
P\in\mathcal C
$$
with
$$
x\in P.
$$
Then
$$
rx\in P\subseteq U.
$$
Hence $U$ is an ideal.

:::

:::

::: {.pf-step #s1-2}

The ideal $U$ is proper.


::: pf-proof

If
$$
1\in U,
$$
then
$$
1\in P
$$
for some
$$
P\in\mathcal C.
$$
This would imply
$$
P=R,
$$
contradicting the fact that $P$ is prime and therefore proper.
Thus
$$
1\notin U.
$$

:::

:::

::: {.pf-step #s1-3}

The ideal $U$ is prime.


::: pf-proof

Suppose
$$
ab\in U.
$$
Then
$$
ab\in P
$$
for some
$$
P\in\mathcal C.
$$
Since $P$ is prime,
$$
a\in P
\quad\text{or}\quad
b\in P.
$$
Hence
$$
a\in U
\quad\text{or}\quad
b\in U.
$$
Together with step [](#s1-2){.pf-ref}, this proves that
$$
\boxed{U\text{ is prime}.}
$$

:::

:::

::: pf-step

The set $I$ is an ideal of $R$.


::: pf-proof

An arbitrary intersection of ideals is an ideal. Explicitly, if
$$
x,y\in I,
$$
then
$$
x,y\in P
$$
for every
$$
P\in\mathcal C.
$$
Thus
$$
x-y\in P
$$
for every $P$, so
$$
x-y\in I.
$$
Likewise, for
$$
r\in R,
$$
one has
$$
rx\in P
$$
for every $P$, hence
$$
rx\in I.
$$

:::

:::

::: {.pf-step #s1-5}

The ideal $I$ is proper.


::: pf-proof

Every
$$
P\in\mathcal C
$$
is proper, so
$$
1\notin P.
$$
Hence
$$
1\notin
\bigcap_{P\in\mathcal C}P
=
I.
$$
Thus
$$
I\ne R.
$$

:::

:::

::: {.pf-step #s1-6}

Suppose
$$
ab\in I
$$
and
$$
a\notin I,
\qquad
b\notin I.
$$
Then there exist
$$
P,Q\in\mathcal C
$$
such that
$$
a\notin P
$$
and
$$
b\notin Q.
$$


::: pf-proof

The condition
$$
a\notin I
=
\bigcap_{T\in\mathcal C}T
$$
means that $a$ fails to lie in at least one member of the chain. Choose such a member and call it $P$.
Similarly, choose
$$
Q\in\mathcal C
$$
with
$$
b\notin Q.
$$

:::

:::

::: {.pf-step #s1-7}

The assumptions in step [](#s1-6){.pf-ref} lead to a contradiction.


::: pf-proof

Because $\mathcal C$ is a chain, either
$$
P\subseteq Q
$$
or
$$
Q\subseteq P.
$$

Suppose first that
$$
P\subseteq Q.
$$
Since
$$
b\notin Q,
$$
one also has
$$
b\notin P.
$$
By construction,
$$
a\notin P.
$$
But
$$
ab\in I\subseteq P,
$$
contradicting primality of $P$.

The case
$$
Q\subseteq P
$$
is symmetric: then
$$
a\notin P
$$
implies
$$
a\notin Q,
$$
while
$$
b\notin Q
$$
by construction, yet
$$
ab\in I\subseteq Q,
$$
contradicting primality of $Q$.

:::

:::

::: {.pf-step #s1-8}

Therefore $I$ is prime.


::: pf-proof

By step [](#s1-7){.pf-ref}, if
$$
ab\in I,
$$
it is impossible for both $a$ and $b$ to lie outside $I$. Hence
$$
a\in I
\quad\text{or}\quad
b\in I.
$$
Together with step [](#s1-5){.pf-ref}, this gives
$$
\boxed{I\text{ is prime}.}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves that the union of the chain is prime, and step [](#s1-8){.pf-ref} proves that the intersection is prime.

:::

:::

:::
