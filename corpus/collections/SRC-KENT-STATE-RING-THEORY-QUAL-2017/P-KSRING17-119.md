---
schema: qual/card@1
id: P-KSRING17-119
kind: problem
title: The smallest ideal with nilpotent-free quotient
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 119 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
A ring $R$ is nilpotent-free if $a^{n} = 0$ for $a \in R$ and some positive integer $n$ implies $a = 0$.

(a) Suppose there is an ideal $I$ such that $R/I$ is nilpotent-free. Show there is a unique smallest (with respect to inclusion) ideal $A$ such that $R/A$ is nilpotent-free.

(b) Give an example of a ring $R$ such that for every proper ideal $I$, $R/I$ is not nilpotent-free. Verify your example.

(c) Show that if $R$ is a commutative ring with identity, then there is a proper ideal $I$ of $R$ such that $R/I$ is nilpotent-free, and find the ideal $A$ of part (a).
:::

::: {.solution}

For part (a), let
$$
\mathcal F
\coloneqq
\{
J\trianglelefteq R:
R/J\text{ is nilpotent-free}
\}.
$$
By hypothesis,
$$
\mathcal F\ne\varnothing.
$$
Set
$$
A
\coloneqq
\bigcap_{J\in\mathcal F}J.
$$

::: pf

::: pf-step

The set $A$ is an ideal of $R$.


::: pf-proof

An arbitrary intersection of ideals is an ideal.

:::

:::

::: {.pf-step #s1-2}

The canonical map
$$
\Phi:
R/A
\longrightarrow
\prod_{J\in\mathcal F}R/J
$$
defined by
$$
\Phi(r+A)
\coloneqq
(r+J)_{J\in\mathcal F}
$$
is injective.


::: pf-proof

The map is well-defined because
$$
A\subseteq J
$$
for every
$$
J\in\mathcal F.
$$
Its kernel consists of those cosets
$$
r+A
$$
such that
$$
r\in J
$$
for every
$$
J\in\mathcal F.
$$
Thus
$$
r\in
\bigcap_{J\in\mathcal F}J
=
A,
$$
so
$$
r+A=0+A.
$$
Hence
$$
\ker\Phi=0.
$$

:::

:::

::: {.pf-step #s1-3}

A direct product of nilpotent-free rings is nilpotent-free.


::: pf-proof

Let
$$
(x_J)_{J\in\mathcal F}
$$
be an element of
$$
\prod_{J\in\mathcal F}R/J
$$
whose $n$th power is zero.
Then
$$
x_J^n=0
$$
in
$$
R/J
$$
for every
$$
J\in\mathcal F.
$$
Each quotient is nilpotent-free, so
$$
x_J=0
$$
for every $J$.
Therefore the product element is zero.

:::

:::

::: {.pf-step #s1-4}

The quotient
$$
R/A
$$
is nilpotent-free.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
R/A
$$
embeds as a subring of the product in step [](#s1-3){.pf-ref}.
A subring of a nilpotent-free ring is nilpotent-free:
if an element has zero $n$th power in the subring, it has zero $n$th power in the ambient ring and hence is zero.
Thus
$$
R/A
$$
is nilpotent-free.

:::

:::

::: {.pf-step #s1-5}

The ideal $A$ is contained in every ideal
$$
J
$$
for which
$$
R/J
$$
is nilpotent-free.


::: pf-proof

This is immediate from the definition
$$
A
=
\bigcap_{J\in\mathcal F}J.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
A
\text{ is the unique smallest ideal such that }R/A
\text{ is nilpotent-free}.
}
$$


::: pf-proof

Step [](#s1-4){.pf-ref} shows that $A$ itself has the required property.
Step [](#s1-5){.pf-ref} shows that every ideal with the required property contains $A$.
Thus $A$ is the unique smallest such ideal.

:::

:::

::: {.pf-step #s1-7}

For part (b), take
$$
\boxed{
R=M_2(F)
}
$$
for any field $F$.
Then $R$ is simple and not nilpotent-free.


::: pf-proof

The matrix
$$
E_{12}
\ne0
$$
satisfies
$$
E_{12}^2=0,
$$
so $R$ is not nilpotent-free.

To see that $R$ is simple, let
$$
0\ne J\trianglelefteq M_2(F)
$$
and choose
$$
A=(a_{ij})\in J
$$
with
$$
a_{ij}\ne0.
$$
Then for arbitrary
$$
k,\ell,
$$
$$
E_{ki}AE_{j\ell}
=
a_{ij}E_{k\ell}
\in
J.
$$
Since
$$
a_{ij}
$$
is invertible in $F$,
$$
E_{k\ell}\in J.
$$
Thus every matrix unit belongs to $J$, so
$$
J=M_2(F).
$$
Hence the only proper ideal is
$$
(0).
$$

:::

:::

::: {.pf-step #s1-8}

For the ring in step [](#s1-7){.pf-ref}, every proper quotient is not nilpotent-free.


::: pf-proof

The only proper ideal is
$$
I=(0).
$$
Then
$$
R/I
\cong
R,
$$
which contains the nonzero nilpotent
$$
E_{12}.
$$
Thus every proper quotient fails to be nilpotent-free.

:::

:::

::: pf-step

Now assume $R$ is commutative with identity and set
$$
\mathcal N
\coloneqq
\{r\in R:r^n=0\text{ for some }n\ge1\}.
$$
Then $\mathcal N$ is an ideal.


::: pf-proof

The element $0$ is nilpotent.
If
$$
x^m=0
\qquad\text{and}\qquad
y^n=0,
$$
then, because $R$ is commutative,
$$
(x+y)^{m+n-1}
=
\sum_{j=0}^{m+n-1}
\binom{m+n-1}{j}
x^j y^{m+n-1-j}
=
0:
$$
in every summand either
$$
j\ge m
$$
or
$$
m+n-1-j\ge n.
$$
Thus
$$
x+y
$$
is nilpotent.
Also
$$
(-x)^m=0.
$$
Finally, for
$$
r\in R,
$$
$$
(rx)^m
=
r^m x^m
=
0.
$$
Hence $\mathcal N$ is an ideal.

:::

:::

::: {.pf-step #s1-10}

The quotient
$$
R/\mathcal N
$$
is nilpotent-free.


::: pf-proof

Suppose
$$
(r+\mathcal N)^n
=
0+\mathcal N.
$$
Then
$$
r^n\in\mathcal N.
$$
Hence
$$
(r^n)^m
=
r^{nm}
=
0
$$
for some
$$
m\ge1.
$$
Thus
$$
r\in\mathcal N.
$$
Therefore
$$
r+\mathcal N
=
0+\mathcal N.
$$
So the quotient has no nonzero nilpotents.

:::

:::

::: {.pf-step #s1-11}

If
$$
I\trianglelefteq R
$$
and
$$
R/I
$$
is nilpotent-free, then
$$
\mathcal N\subseteq I.
$$


::: pf-proof

Let
$$
n\in\mathcal N.
$$
Choose
$$
k\ge1
$$
with
$$
n^k=0.
$$
Then
$$
(n+I)^k
=
0+I.
$$
Since
$$
R/I
$$
is nilpotent-free,
$$
n+I
=
0+I.
$$
Thus
$$
n\in I.
$$

:::

:::

::: {.pf-step #s1-12}

Therefore, in the commutative case,
$$
\boxed{
A
=
\mathcal N,
}
$$
the nilradical of $R$.


::: pf-proof

Step [](#s1-10){.pf-ref} shows
$$
R/\mathcal N
$$
is nilpotent-free.
Step [](#s1-11){.pf-ref} shows every ideal with nilpotent-free quotient contains
$$
\mathcal N.
$$
By the characterization of the smallest ideal in part (a),
$$
A=\mathcal N.
$$

:::

:::

::: {.pf-step #s1-13}

In particular, if $R$ is nonzero, there is a proper ideal with nilpotent-free quotient.


::: pf-proof

Take
$$
I=\mathcal N.
$$
By step [](#s1-10){.pf-ref} the quotient is nilpotent-free.
Moreover,
$$
1\notin\mathcal N
$$
in a nonzero ring, because
$$
1^n=1\ne0.
$$
Hence
$$
\mathcal N\subsetneq R.
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves part (a), step [](#s1-8){.pf-ref} proves part (b), and steps [](#s1-12){.pf-ref} through [](#s1-13){.pf-ref} prove part (c).

:::

:::

:::
