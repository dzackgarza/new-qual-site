---
schema: qual/card@1
id: P-KSRING17-093
kind: problem
title: Nonzero prime ideals of a Euclidean domain are maximal
classification:
  areas: [algebra]
  topics:
  - Euclidean Domains
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 93 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be a Euclidean domain.
Prove that every non-zero prime ideal is a maximal ideal.
:::

::: {.solution}

Let
$$
P
$$
be a nonzero prime ideal of the Euclidean domain $D$.

::: pf

::: {.pf-step #s1-1}

Every ideal of $D$ is principal.


::: pf-proof

Let
$$
I\trianglelefteq D
$$
be nonzero, and let
$$
\delta:D\setminus\{0\}\to\NN
$$
be a Euclidean function.
Choose
$$
0\ne d\in I
$$
with
$$
\delta(d)
$$
minimal among the Euclidean values of nonzero elements of $I$.

For any
$$
a\in I,
$$
Euclidean division gives
$$
a=qd+r
$$
with either
$$
r=0
$$
or
$$
\delta(r)<\delta(d).
$$
But
$$
r=a-qd\in I.
$$
Minimality of $\delta(d)$ therefore forces
$$
r=0.
$$
Thus
$$
d\mid a
$$
for every $a\in I$, so
$$
I\subseteq(d).
$$
The reverse inclusion holds because
$$
d\in I.
$$
Hence
$$
I=(d).
$$
The zero ideal is
$$
(0).
$$
Thus every ideal is principal.

:::

:::

::: {.pf-step #s1-2}

Write
$$
P=(p)
$$
with
$$
p\ne0.
$$
Then $p$ is irreducible.


::: pf-proof

Suppose
$$
p=ab.
$$
Then
$$
ab\in(p).
$$
Since
$$
(p)
$$
is prime,
$$
a\in(p)
\quad\text{or}\quad
b\in(p).
$$

If
$$
a=pc,
$$
then
$$
p=pcb.
$$
Because $D$ is a domain and
$$
p\ne0,
$$
cancellation gives
$$
1=cb,
$$
so $b$ is a unit.
The other case similarly makes $a$ a unit.
Therefore $p$ is irreducible.

:::

:::

::: {.pf-step #s1-3}

Let
$$
I
$$
be an ideal satisfying
$$
P\subseteq I\subseteq D.
$$
Then
$$
I=P
\quad\text{or}\quad
I=D.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
I=(a)
$$
for some
$$
a\in D.
$$
The containment
$$
(p)\subseteq(a)
$$
gives
$$
p=ar
$$
for some
$$
r\in D.
$$
Since $p$ is irreducible by step [](#s1-2){.pf-ref}, either
$$
a
$$
is a unit or
$$
r
$$
is a unit.

If $a$ is a unit,
$$
I=(a)=D.
$$
If $r$ is a unit, $a$ is associate to $p$, hence
$$
I=(a)=(p)=P.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{P\text{ is maximal}.}
$$


::: pf-proof

The ideal $P$ is proper because it is prime.
Step [](#s1-3){.pf-ref} shows that no proper ideal lies strictly between $P$ and $D$.
Thus $P$ is maximal.

:::

:::

::: pf-qed

Since $P$ was an arbitrary nonzero prime ideal, step [](#s1-4){.pf-ref} proves the assertion.

:::

:::

:::
