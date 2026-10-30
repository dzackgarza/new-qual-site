---
schema: qual/card@1
id: P-KSRING17-054
kind: problem
title: A prime ideal consisting of zero divisors
classification:
  areas: [algebra]
  topics:
  - Prime Ideals
  - Zero Divisors
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 54 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with identity and let S be the set of all elements of R that are not zero-divisors.
Show that there is a prime ideal P such that $P \cap S$ is empty.
(Hint: Use Zorn’s Lemma.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
0\notin S
\qquad\text{and}\qquad
1\in S.
$$


::: pf-proof

Because $R$ has identity and is nonzero, there exists a nonzero element of $R$, namely $1$. Hence
$$
0\cdot1=0,
$$
so $0$ is a zero divisor under the repository's convention and therefore
$$
0\notin S.
$$

The identity $1$ is not a zero divisor: if
$$
1\cdot r=0,
$$
then
$$
r=0.
$$
Thus
$$
1\in S.
$$

:::

:::

::: {.pf-step #s1-2}

The set $S$ is multiplicatively closed.


::: pf-proof

Let
$$
a,b\in S.
$$
Suppose
$$
ab
$$
were a zero divisor. Then there would exist
$$
0\ne c\in R
$$
such that
$$
(ab)c=0.
$$
By associativity,
$$
a(bc)=0.
$$
Since $a$ is not a zero divisor,
$$
bc=0.
$$
Since $b$ is not a zero divisor,
$$
c=0,
$$
contradicting the choice of $c$.

Therefore
$$
ab\in S.
$$

:::

:::

::: {.pf-step #s1-3}

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

::: {.pf-step #s1-4}

Every chain in $\mathcal P$ has an upper bound in $\mathcal P$.


::: pf-proof

Let
$$
\mathcal C\subseteq\mathcal P
$$
be a chain and set
$$
U
\coloneqq
\bigcup_{I\in\mathcal C}I.
$$
Because the members of $\mathcal C$ are totally ordered by inclusion, the union $U$ is an ideal:
if
$$
x\in I,
\qquad
y\in J
$$
with
$$
I,J\in\mathcal C,
$$
then one of $I,J$ contains the other, so $x$ and $y$ lie in a common member of the chain; closure under subtraction and multiplication by elements of $R$ follows there.

If
$$
U\cap S\ne\varnothing,
$$
choose
$$
s\in U\cap S.
$$
Then
$$
s\in I
$$
for some
$$
I\in\mathcal C,
$$
contradicting
$$
I\cap S=\varnothing.
$$
Thus
$$
U\in\mathcal P,
$$
and it is an upper bound for $\mathcal C$.

:::

:::

::: pf-step

There exists an ideal
$$
P\in\mathcal P
$$
maximal with respect to inclusion.


::: pf-proof

By step [](#s1-3){.pf-ref}, $\mathcal P$ is nonempty, and by step [](#s1-4){.pf-ref} every chain has an upper bound in $\mathcal P$. Zorn's lemma therefore yields a maximal element
$$
P\in\mathcal P.
$$

:::

:::

::: {.pf-step #s1-6}

The ideal $P$ is proper.


::: pf-proof

Since
$$
1\in S
$$
by step [](#s1-1){.pf-ref} and
$$
P\cap S=\varnothing,
$$
one has
$$
1\notin P.
$$
Thus
$$
P\ne R.
$$

:::

:::

::: {.pf-step #s1-7}

Suppose
$$
ab\in P
$$
with
$$
a\notin P,
\qquad
b\notin P.
$$
Then
$$
P+(a)
$$
and
$$
P+(b)
$$
each meet $S$.


::: pf-proof

Because
$$
a\notin P,
$$
the ideal
$$
P+(a)
$$
properly contains $P$. By maximality of $P$ among ideals disjoint from $S$, the larger ideal cannot remain disjoint from $S$. Hence
$$
(P+(a))\cap S\ne\varnothing.
$$
The same argument with $b$ gives
$$
(P+(b))\cap S\ne\varnothing.
$$

:::

:::

::: {.pf-step #s1-8}

Under the assumptions of step [](#s1-7){.pf-ref}, choose
$$
s=p+ra\in S
$$
and
$$
t=q+ub\in S
$$
with
$$
p,q\in P,
\qquad
r,u\in R.
$$
Then
$$
st\in P.
$$


::: pf-proof

Expand:
$$
\begin{aligned}
st
&=
(p+ra)(q+ub)\\
&=
pq+pub+raq+ruab.
\end{aligned}
$$
The first three terms lie in $P$ because
$$
p,q\in P,
$$
and the last term lies in $P$ because
$$
ab\in P.
$$
Thus
$$
st\in P.
$$

:::

:::

::: {.pf-step #s1-9}

The assumptions of step [](#s1-7){.pf-ref} are impossible.


::: pf-proof

By step [](#s1-8){.pf-ref},
$$
st\in P.
$$
But
$$
s,t\in S
$$
and $S$ is multiplicatively closed by step [](#s1-2){.pf-ref}, so
$$
st\in S.
$$
Hence
$$
st\in P\cap S,
$$
contradicting
$$
P\cap S=\varnothing.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
P\text{ is prime and }P\cap S=\varnothing.
}
$$


::: pf-proof

Step [](#s1-6){.pf-ref} shows that $P$ is proper. Step [](#s1-9){.pf-ref} shows that whenever
$$
ab\in P,
$$
one must have
$$
a\in P
\quad\text{or}\quad
b\in P.
$$
Thus $P$ is prime. By construction,
$$
P\cap S=\varnothing.
$$

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} gives the required prime ideal.

:::

:::

:::
