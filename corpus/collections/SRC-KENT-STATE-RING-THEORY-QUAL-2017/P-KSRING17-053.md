---
schema: qual/card@1
id: P-KSRING17-053
kind: problem
title: A non-nilpotent element avoids some prime ideal
classification:
  areas: [algebra]
  topics:
  - Prime Ideals
  - Nilradical
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 53 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with identity and let $x \in R$ be a non-nilpotent element.
Prove that there exists a prime ideal P of R such that $x \notin P$
:::

::: {.solution}

Define
$$
S
\coloneqq
\{1,x,x^2,x^3,\ldots\}.
$$

::: pf

::: {.pf-step #s1-1}

The set $S$ is multiplicatively closed and does not contain $0$.


::: pf-proof

If
$$
x^m,x^n\in S,
$$
then
$$
x^mx^n=x^{m+n}\in S,
$$
so $S$ is multiplicatively closed.

If
$$
0\in S,
$$
then
$$
x^n=0
$$
for some
$$
n\ge0.
$$
Since
$$
1\ne0,
$$
one must have
$$
n\ge1,
$$
which would make $x$ nilpotent. This contradicts the hypothesis.
Therefore
$$
0\notin S.
$$

:::

:::

::: {.pf-step #s1-2}

Let
$$
\mathcal P
\coloneqq
\{
I\trianglelefteq R:
I\cap S=\varnothing
\},
$$
ordered by inclusion.
Then $\mathcal P$ is nonempty.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
(0)\cap S=\varnothing.
$$
Hence
$$
(0)\in\mathcal P.
$$

:::

:::

::: {.pf-step #s1-3}

Every chain in $\mathcal P$ has an upper bound in $\mathcal P$.


::: pf-proof

Let
$$
\mathcal C
\subseteq
\mathcal P
$$
be a chain and define
$$
U
\coloneqq
\bigcup_{I\in\mathcal C}I.
$$

Because $\mathcal C$ is totally ordered by inclusion, the usual union-of-a-chain argument shows that $U$ is an ideal:
if
$$
a\in I_1,
\qquad
b\in I_2
$$
with
$$
I_1,I_2\in\mathcal C,
$$
then one of $I_1,I_2$ contains the other, so $a$ and $b$ lie in a common ideal of the chain. Thus
$$
a-b\in U,
$$
and closure under multiplication by arbitrary elements of $R$ is immediate.

It remains to show
$$
U\cap S=\varnothing.
$$
If
$$
s\in U\cap S,
$$
then by definition of the union
$$
s\in I
$$
for some
$$
I\in\mathcal C.
$$
This would give
$$
s\in I\cap S,
$$
contrary to
$$
I\in\mathcal P.
$$
Hence
$$
U\in\mathcal P,
$$
and clearly every member of $\mathcal C$ is contained in $U$.

:::

:::

::: {.pf-step #s1-4}

There exists an ideal
$$
P\in\mathcal P
$$
that is maximal with respect to inclusion.


::: pf-proof

By step [](#s1-2){.pf-ref}, the poset $\mathcal P$ is nonempty. By step [](#s1-3){.pf-ref}, every chain has an upper bound in $\mathcal P$. Zorn's lemma therefore yields a maximal element
$$
P\in\mathcal P.
$$

:::

:::

::: {.pf-step #s1-5}

The ideal $P$ is prime.


::: pf-proof

Suppose
$$
ab\in P
$$
and
$$
a\notin P,
\qquad
b\notin P.
$$
Then
$$
P\subsetneq P+(a)
$$
and
$$
P\subsetneq P+(b).
$$
By maximality of $P$ in $\mathcal P$, neither larger ideal can remain disjoint from $S$. Hence choose
$$
s\in(P+(a))\cap S
$$
and
$$
t\in(P+(b))\cap S.
$$
Write
$$
s=p+ra,
\qquad
t=q+ub
$$
with
$$
p,q\in P,
\qquad
r,u\in R.
$$
Then
$$
\begin{aligned}
st
&=
(p+ra)(q+ub)\\
&=
pq+pub+raq+ruab.
\end{aligned}
$$
Every term on the right lies in $P$, because
$$
p,q\in P
$$
and
$$
ab\in P.
$$
Thus
$$
st\in P.
$$
But
$$
s,t\in S
$$
and $S$ is multiplicatively closed, so
$$
st\in S.
$$
This contradicts
$$
P\cap S=\varnothing.
$$

Therefore
$$
ab\in P
\implies
a\in P
\text{ or }
b\in P.
$$
Also $P$ is proper because
$$
1\in S
$$
and
$$
P\cap S=\varnothing.
$$
Hence $P$ is prime.

:::

:::

::: {.pf-step #s1-6}

The prime ideal $P$ does not contain $x$.


::: pf-proof

By definition,
$$
x\in S.
$$
Since
$$
P\cap S=\varnothing,
$$
one has
$$
x\notin P.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore there exists a prime ideal $P$ such that
$$
\boxed{x\notin P.}
$$


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} construct such a prime ideal.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
