---
schema: qual/card@1
id: P-KSRING17-122
kind: problem
title: A ring whose non-units are closed under addition is local
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 122 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with $1 \neq 0$ in which the set of nonunits is closed under addition.
Prove that R is local, i.e., has a unique maximal ideal.
:::

Let
$$
N
\coloneqq
\{a\in R:a\text{ is not a unit}\}.
$$

::: pf

::: pf-step

The element
$$
0
$$
belongs to $N$.


::: pf-proof

Since
$$
1\ne0,
$$
the zero element cannot have a multiplicative inverse.
Thus
$$
0\in N.
$$

:::

:::

::: pf-step

If
$$
a\in N,
$$
then
$$
-a\in N.
$$


::: pf-proof

Suppose
$$
-a
$$
were a unit.
Since
$$
-1
$$
is a unit,
$$
a
=
(-1)(-a)
$$
would be a product of units and hence a unit.
This contradicts
$$
a\in N.
$$
Therefore
$$
-a\in N.
$$

:::

:::

::: pf-step

The set $N$ is an additive subgroup of $R$.


::: pf-proof

By hypothesis, $N$ is closed under addition.
Step <1>1 gives
$$
0\in N,
$$
and step <1>2 gives closure under additive inverses.
Thus $N$ is an additive subgroup.

:::

:::

::: pf-step

If
$$
a\in N
$$
and
$$
r\in R,
$$
then
$$
ra\in N.
$$


::: pf-proof

Suppose
$$
ra
$$
were a unit.
Then there would exist
$$
s\in R
$$
such that
$$
(ra)s=1.
$$
Because $R$ is commutative,
$$
a(rs)=1.
$$
Thus $a$ would be a unit, contradicting
$$
a\in N.
$$
Therefore
$$
ra\in N.
$$

:::

:::

::: pf-step

Hence
$$
\boxed{
N
\text{ is an ideal of }R.
}
$$


::: pf-proof

Step <1>3 gives the additive-subgroup condition, and step <1>4 gives absorption under multiplication by arbitrary elements of $R$.

:::

:::

::: pf-step

The ideal $N$ is proper.


::: pf-proof

The identity
$$
1
$$
is a unit.
Therefore
$$
1\notin N,
$$
so
$$
N\ne R.
$$

:::

:::

::: pf-step

Every nonzero element of
$$
R/N
$$
is invertible.


::: pf-proof

Let
$$
a+N
\ne
0+N.
$$
Then
$$
a\notin N.
$$
By definition of $N$, the element $a$ is a unit in $R$.
Choose
$$
b\in R
$$
with
$$
ab=1.
$$
Then
$$
(a+N)(b+N)
=
1+N.
$$
Thus
$$
a+N
$$
is invertible.

:::

:::

::: pf-step

The quotient
$$
R/N
$$
is a field, so $N$ is maximal.


::: pf-proof

By step <1>6, the quotient is nonzero.
Step <1>7 shows every nonzero element is invertible.
Thus
$$
R/N
$$
is a field.
The maximal-ideal quotient criterion gives that
$$
N
$$
is maximal.

:::

:::

::: pf-step

Every proper ideal of $R$ is contained in $N$.


::: pf-proof

Let
$$
I\trianglelefteq R
$$
be proper.
If
$$
u\in I
$$
were a unit, then
$$
1
=
u^{-1}u
\in
I,
$$
forcing
$$
I=R.
$$
Thus every element of a proper ideal is a nonunit.
Hence
$$
I\subseteq N.
$$

:::

:::

::: pf-step

The ideal $N$ is the unique maximal ideal.


::: pf-proof

Let
$$
M
$$
be any maximal ideal.
It is proper, so step <1>9 gives
$$
M\subseteq N.
$$
Since $N$ is proper by step <1>6, maximality of $M$ forces
$$
M=N.
$$
Thus every maximal ideal is equal to $N$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
R
\text{ is local}.
}
$$


::: pf-proof

Step <1>10 shows that $R$ has exactly one maximal ideal.

:::

:::

::: pf-qed

Step <1>11 is the required conclusion.

:::

:::
