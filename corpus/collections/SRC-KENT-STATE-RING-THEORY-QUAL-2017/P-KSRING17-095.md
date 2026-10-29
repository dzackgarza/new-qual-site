---
schema: qual/card@1
id: P-KSRING17-095
kind: problem
title: Euclidean domains with ultrametric norm are fields or polynomial rings
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 95 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D with $\varphi : D - \{ 0 \} \to \NN$ be a Euclidean domain.
Suppose $\varphi ( a + b ) \leqslant$ max $\{ \varphi ( a ) , \varphi ( b ) \}$ for all $a , b \in D$ . Prove that D is either a field or isomorphic to a polynomial ring over a field.
:::

::: {.remark}
This problem uses the classical Euclidean-function convention in which, in addition to division with remainder, one has
$$
\varphi(a)\le \varphi(ab)
$$
for all nonzero $a,b\in D$.
The proof below uses this monotonicity axiom.
:::

::: {.solution}

Assume throughout that
$$
\varphi(a)\le\varphi(ab)
$$
for all nonzero
$$
a,b\in D,
$$
and that
$$
\varphi(a+b)
\le
\max\{\varphi(a),\varphi(b)\}
$$
whenever the displayed values are defined.

::: pf

::: {.pf-step #s1-1}

The value
$$
\varphi(1)
$$
is the minimum value of $\varphi$ on
$$
D\setminus\{0\}.
$$


::: pf-proof

Let
$$
0\ne a\in D.
$$
Applying monotonicity to
$$
1
\qquad\text{and}\qquad
a
$$
gives
$$
\varphi(1)
\le
\varphi(1\cdot a)
=
\varphi(a).
$$
Thus
$$
\varphi(1)
$$
is minimal.

:::

:::

::: {.pf-step #s1-2}

If
$$
u\in D^\times,
$$
then
$$
\varphi(u)=\varphi(1).
$$


::: pf-proof

Monotonicity gives
$$
\varphi(1)
\le
\varphi(u).
$$
Since
$$
u^{-1}
$$
is nonzero,
$$
\varphi(u)
\le
\varphi(uu^{-1})
=
\varphi(1).
$$
Therefore
$$
\varphi(u)=\varphi(1).
$$

:::

:::

::: {.pf-step #s1-3}

Conversely, if
$$
0\ne a\in D
$$
and
$$
\varphi(a)=\varphi(1),
$$
then $a$ is a unit.


::: pf-proof

Apply Euclidean division to
$$
1
$$
by
$$
a.
$$
There exist
$$
q,r\in D
$$
such that
$$
1=qa+r
$$
and either
$$
r=0
$$
or
$$
\varphi(r)<\varphi(a)=\varphi(1).
$$
The latter alternative is impossible by step [](#s1-1){.pf-ref}.
Hence
$$
r=0
$$
and
$$
1=qa.
$$
Thus $a$ is a unit.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
D^\times
=
\{
a\ne0:
\varphi(a)=\varphi(1)
\}.
}
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Define
$$
F
\coloneqq
D^\times\cup\{0\}.
$$
Then $F$ is closed under addition.


::: pf-proof

Let
$$
a,b\in F.
$$
If
$$
a=0
$$
or
$$
a+b=0,
$$
there is nothing to prove.
Assume
$$
a\ne0
\qquad\text{and}\qquad
a+b\ne0.
$$
Then
$$
a
$$
is a unit.

If
$$
b=0,
$$
then
$$
a+b=a\in F.
$$
Assume
$$
b\ne0.
$$
Then $b$ is also a unit.
By step [](#s1-4){.pf-ref},
$$
\varphi(a)
=
\varphi(b)
=
\varphi(1).
$$
The ultrametric inequality gives
$$
\varphi(a+b)
\le
\varphi(1).
$$
Step [](#s1-1){.pf-ref} gives the reverse inequality, so
$$
\varphi(a+b)=\varphi(1).
$$
By step [](#s1-4){.pf-ref},
$$
a+b
$$
is a unit.
Hence
$$
a+b\in F.
$$

:::

:::

::: {.pf-step #s1-6}

The set $F$ is a subfield of $D$.


::: pf-proof

It contains
$$
0
$$
and
$$
1.
$$
Step [](#s1-5){.pf-ref} gives closure under addition.
If
$$
u\in D^\times,
$$
then
$$
-u
=
(-1)u
$$
is again a unit, so $F$ is closed under additive inverses.
The product of two nonzero elements of $F$ is a product of units and hence a unit.
The inverse of a nonzero element of $F$ is again a unit.
Thus
$$
F
$$
is a field.

:::

:::

::: {.pf-step #s1-7}

If
$$
D=F,
$$
then $D$ is a field.


::: pf-proof

This is immediate from step [](#s1-6){.pf-ref}.

:::

:::

::: pf-step

Assume now that
$$
D\ne F.
$$
Choose
$$
x\in D\setminus F
$$
such that
$$
\varphi(x)
$$
is minimal among the values
$$
\{
\varphi(a):
a\in D\setminus F
\}.
$$


::: pf-proof

The set
$$
D\setminus F
$$
is nonempty by assumption.
Its $\varphi$-values form a nonempty subset of $\NN$, so they have a least element.
Choose $x$ realizing it.

:::

:::

::: {.pf-step #s1-9}

The element $x$ is transcendental over $F$.


::: pf-proof

Suppose
$$
x
$$
were algebraic over the field $F$.
Then
$$
F[x]
$$
would be a finite-dimensional integral domain over $F$, hence a field.
In particular,
$$
x^{-1}
\in
F[x]
\subseteq
D.
$$
Thus $x$ would be a unit of $D$, so
$$
x\in F,
$$
contradicting the choice
$$
x\in D\setminus F.
$$
Therefore $x$ is transcendental over $F$.

:::

:::

::: {.pf-step #s1-10}

If
$$
0\ne a\in D
$$
and
$$
c\in F
$$
with
$$
a+c\ne0,
$$
then
$$
\varphi(a+c)=\varphi(a).
$$


::: pf-proof

If
$$
c=0,
$$
the statement is immediate.
Assume
$$
c\ne0.
$$
Then
$$
c
$$
is a unit, so by step [](#s1-4){.pf-ref},
$$
\varphi(c)=\varphi(1).
$$
The ultrametric inequality gives
$$
\varphi(a+c)
\le
\max\{
\varphi(a),\varphi(c)
\}
=
\varphi(a),
$$
because step [](#s1-1){.pf-ref} gives
$$
\varphi(1)\le\varphi(a).
$$

Also
$$
a
=
(a+c)+(-c).
$$
Since
$$
-c
$$
is a unit,
$$
\varphi(-c)=\varphi(1).
$$
Applying the ultrametric inequality again,
$$
\varphi(a)
\le
\max\{
\varphi(a+c),\varphi(1)
\}
=
\varphi(a+c),
$$
where the last equality uses step [](#s1-1){.pf-ref}.
Thus equality holds.

:::

:::

::: {.pf-step #s1-11}

If
$$
0\ne a,b\in D
$$
and
$$
\varphi(a)=\varphi(ab),
$$
then $b$ is a unit.


::: pf-proof

Suppose
$$
b
$$
is not a unit.
Then
$$
(ab)
\subsetneq
(a).
$$
Choose
$$
c
\in
(a)\setminus(ab).
$$
Divide $c$ by $ab$:
$$
c=q(ab)+r
$$
with either
$$
r=0
$$
or
$$
\varphi(r)<\varphi(ab).
$$
Because
$$
c\notin(ab),
$$
one cannot have
$$
r=0.
$$
Thus
$$
\varphi(r)<\varphi(ab)=\varphi(a).
$$

On the other hand,
$$
c\in(a)
$$
and
$$
q(ab)\in(a),
$$
so
$$
r
=
c-q(ab)
\in
(a).
$$
Write
$$
r=da.
$$
Then monotonicity gives
$$
\varphi(a)
\le
\varphi(da)
=
\varphi(r),
$$
contradiction.
Therefore
$$
b
$$
is a unit.

:::

:::

::: {.pf-step #s1-12}

If
$$
b
$$
is a nonunit, then for every nonzero
$$
a\in D,
$$
one has
$$
\varphi(a)<\varphi(ab).
$$


::: pf-proof

Monotonicity gives
$$
\varphi(a)\le\varphi(ab).
$$
Equality would imply, by step [](#s1-11){.pf-ref}, that $b$ is a unit.
Hence equality is impossible and the inequality is strict.

:::

:::

::: {.pf-step #s1-13}

Every element of $D$ belongs to
$$
F[x].
$$


::: pf-proof

We use strong induction on
$$
\varphi(a)
$$
for nonzero
$$
a\in D.
$$
The zero element is already in
$$
F[x].
$$

If
$$
a\in F,
$$
then
$$
a\in F[x].
$$
Assume
$$
a\notin F.
$$
Divide $a$ by $x$:
$$
a=sx+r
$$
with either
$$
r=0
$$
or
$$
\varphi(r)<\varphi(x).
$$
By minimality of
$$
\varphi(x)
$$
among nonunits, every nonzero such $r$ lies in $F$.
Thus in all cases
$$
r\in F.
$$

If
$$
s=0,
$$
then
$$
a=r\in F,
$$
contrary to
$$
a\notin F.
$$
Hence
$$
s\ne0.
$$

If
$$
s\in F,
$$
then
$$
a=sx+r\in F[x].
$$
Assume instead
$$
s\notin F.
$$
Then
$$
x
$$
is a nonunit, so step [](#s1-12){.pf-ref} gives
$$
\varphi(s)
<
\varphi(sx).
$$
Because
$$
a=sx+r
$$
with
$$
r\in F,
$$
step [](#s1-10){.pf-ref} gives
$$
\varphi(a)
=
\varphi(sx).
$$
Therefore
$$
\varphi(s)
<
\varphi(a).
$$
By the strong induction hypothesis,
$$
s\in F[x].
$$
Hence
$$
a=sx+r
\in
F[x].
$$
This completes the induction.

:::

:::

::: {.pf-step #s1-14}

Therefore
$$
D=F[x].
$$


::: pf-proof

Step [](#s1-13){.pf-ref} gives
$$
D\subseteq F[x].
$$
The reverse inclusion is automatic because
$$
F\subseteq D
$$
and
$$
x\in D.
$$
Thus equality holds.

:::

:::

::: {.pf-step #s1-15}

Since $x$ is transcendental over $F$, the evaluation homomorphism
$$
F[T]\to D,
\qquad
T\longmapsto x
$$
is an isomorphism.


::: pf-proof

The map is surjective by step [](#s1-14){.pf-ref}.
Its kernel consists of polynomials in
$$
F[T]
$$
vanishing at
$$
x.
$$
Step [](#s1-9){.pf-ref} says $x$ is transcendental over $F$, so the kernel is zero.
Therefore the map is injective as well.
Hence
$$
D
\cong
F[T].
$$

:::

:::

::: {.pf-step #s1-16}

Consequently,
$$
\boxed{
D
\text{ is either a field or isomorphic to a polynomial ring over a field}.
}
$$


::: pf-proof

If
$$
D=F,
$$
step [](#s1-7){.pf-ref} gives the field case.
If
$$
D\ne F,
$$
step [](#s1-15){.pf-ref} gives
$$
D\cong F[T]
$$
for the field $F$ from step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-16){.pf-ref} is the required classification under the intended Euclidean-function convention.

:::

:::

:::
