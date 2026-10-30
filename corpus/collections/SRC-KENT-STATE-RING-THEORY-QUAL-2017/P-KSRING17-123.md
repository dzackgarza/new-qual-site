---
schema: qual/card@1
id: P-KSRING17-123
kind: problem
title: Localization of a domain at a prime ideal is local
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 123 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $D$ be an integral domain and $F$ its field of fractions. Let $P$ be a prime ideal in $D$ and $D_{P} = \{ab^{-1} \st a, b \in D,\ b \notin P\} \subseteq F$. Show that $D_{P}$ has a unique maximal ideal.
:::

::: {.solution}

Define
$$
M
\coloneqq
\left\{
\frac ab
\in
D_P:
a\in P
\right\}.
$$

::: pf

::: pf-step

The set $M$ is well-defined.


::: pf-proof

Suppose
$$
\frac ab
=
\frac cd
$$
in the fraction field, with
$$
b,d\notin P.
$$
Then
$$
ad=bc.
$$
Assume
$$
a\in P.
$$
Then
$$
ad\in P,
$$
so
$$
bc\in P.
$$
Since
$$
b\notin P
$$
and $P$ is prime,
$$
c\in P.
$$
Thus membership in $M$ is independent of the chosen representative.

:::

:::

::: {.pf-step #s1-2}

The set $M$ is closed under subtraction.


::: pf-proof

Let
$$
\frac ab,\frac cd
\in
M.
$$
Then
$$
a,c\in P
$$
and
$$
b,d\notin P.
$$
One has
$$
\frac ab-\frac cd
=
\frac{ad-bc}{bd}.
$$
Since
$$
a,c\in P
$$
and $P$ is an ideal,
$$
ad-bc
\in
P.
$$
Also
$$
bd\notin P
$$
because $P$ is prime and neither factor lies in $P$.
Hence
$$
\frac ab-\frac cd
\in
M.
$$

:::

:::

::: {.pf-step #s1-3}

The set $M$ absorbs multiplication by arbitrary elements of $D_P$.


::: pf-proof

Let
$$
\frac rs
\in
D_P
$$
and
$$
\frac ab
\in
M.
$$
Then
$$
a\in P,
\qquad
s,b\notin P.
$$
Their product is
$$
\frac rs\frac ab
=
\frac{ra}{sb}.
$$
Because
$$
a\in P,
$$
one has
$$
ra\in P.
$$
Since
$$
s,b\notin P
$$
and $P$ is prime,
$$
sb\notin P.
$$
Therefore
$$
\frac{ra}{sb}
\in
M.
$$

:::

:::

::: pf-step

Thus
$$
\boxed{
M
\trianglelefteq
D_P.
}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives the additive-subgroup condition, and step [](#s1-3){.pf-ref} gives absorption under multiplication by arbitrary elements of $D_P$.

:::

:::

::: {.pf-step #s1-5}

The ideal $M$ is proper.


::: pf-proof

The identity of $D_P$ is
$$
1=\frac11.
$$
Since $P$ is proper,
$$
1\notin P.
$$
Hence
$$
1\notin M.
$$
Therefore
$$
M\ne D_P.
$$

:::

:::

::: {.pf-step #s1-6}

If
$$
\frac ab
\in
D_P
$$
with
$$
a\notin P,
$$
then
$$
\frac ab
$$
is a unit.


::: pf-proof

Since
$$
a\notin P,
$$
the fraction
$$
\frac ba
$$
belongs to
$$
D_P.
$$
Moreover,
$$
\frac ab\frac ba
=
1.
$$
Thus
$$
\frac ab
\in
D_P^\times.
$$

:::

:::

::: {.pf-step #s1-7}

If
$$
\frac ab
\in
M,
$$
then
$$
\frac ab
$$
is not a unit.


::: pf-proof

Suppose
$$
a\in P
$$
and
$$
\frac ab
$$
were a unit.
Then there would exist
$$
\frac cd
\in
D_P
$$
with
$$
\frac ab\frac cd
=
1.
$$
Hence
$$
ac=bd
$$
in $D$.
Since
$$
a\in P,
$$
one has
$$
ac\in P,
$$
and therefore
$$
bd\in P.
$$
But
$$
b,d\notin P,
$$
contradicting primality of $P$.
Thus
$$
\frac ab
$$
is not invertible.

:::

:::

::: {.pf-step #s1-8}

The nonunits of $D_P$ are exactly the elements of $M$.


::: pf-proof

Step [](#s1-6){.pf-ref} shows that every fraction outside $M$ is a unit.
Step [](#s1-7){.pf-ref} shows that every fraction in $M$ is a nonunit.
Hence
$$
\boxed{
M
=
D_P\setminus D_P^\times.
}
$$

:::

:::

::: pf-step

The ideal $M$ is maximal.


::: pf-proof

The quotient
$$
D_P/M
$$
is nonzero by step [](#s1-5){.pf-ref}.
Let
$$
\frac ab+M
\ne
0+M.
$$
Then
$$
\frac ab
\notin
M.
$$
By step [](#s1-8){.pf-ref},
$$
\frac ab
$$
is a unit of $D_P$.
Its image in the quotient is therefore a unit.
Thus every nonzero element of
$$
D_P/M
$$
is invertible, so the quotient is a field.
Hence $M$ is maximal.

:::

:::

::: {.pf-step #s1-10}

The ideal $M$ is the unique maximal ideal of $D_P$.


::: pf-proof

Let
$$
N
$$
be any maximal ideal of
$$
D_P.
$$
A proper ideal cannot contain a unit, so every element of $N$ is a nonunit.
By step [](#s1-8){.pf-ref},
$$
N\subseteq M.
$$
Since both
$$
N
$$
and
$$
M
$$
are maximal proper ideals, this containment forces
$$
N=M.
$$

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{
D_P
\text{ is a local ring with unique maximal ideal }
P D_P
=
\left\{
\frac ab:
a\in P,\ b\notin P
\right\}.
}
$$


::: pf-proof

Step [](#s1-10){.pf-ref} proves uniqueness, and the displayed description is the definition of $M$.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the required conclusion.

:::

:::

:::
