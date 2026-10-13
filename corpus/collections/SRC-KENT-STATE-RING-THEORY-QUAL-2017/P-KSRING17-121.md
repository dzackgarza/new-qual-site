---
schema: qual/card@1
id: P-KSRING17-121
kind: problem
title: Local rings are those whose non-units form an ideal
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 121 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
A local ring is a commutative ring with 1 that has a unique maximal ideal.
Show that a ring R is local if and only if the set of non-units in R is an ideal.
:::

::: {.solution}
Let
$$
N
\coloneqq
\{r\in R:r\text{ is not a unit}\}.
$$

<1>1. Assume first that $R$ is local, with unique maximal ideal
$$
\mathfrak m.
$$
Then every element of
$$
\mathfrak m
$$
is a nonunit.

::: {.proof}
If
$$
u\in\mathfrak m
$$
were a unit, then
$$
1
=
u^{-1}u
\in
\mathfrak m,
$$
contradicting properness of the maximal ideal.
Hence
$$
\mathfrak m
\subseteq
N.
$$
:::

<1>2. Every nonunit belongs to some maximal ideal.

::: {.proof}
Let
$$
a\in R
$$
be a nonunit.
Then the principal ideal
$$
(a)
$$
is proper:
if
$$
(a)=R,
$$
then
$$
1=ra
$$
for some
$$
r\in R,
$$
making $a$ a unit.

Every proper ideal of a commutative ring with identity is contained in a maximal ideal.
Hence
$$
(a)
\subseteq
M
$$
for some maximal ideal
$$
M,
$$
and therefore
$$
a\in M.
$$
:::

<1>3. If $R$ is local with maximal ideal $\mathfrak m$, then
$$
N=\mathfrak m.
$$

::: {.proof}
Step <1>1 gives
$$
\mathfrak m\subseteq N.
$$
Let
$$
a\in N.
$$
By step <1>2, $a$ lies in some maximal ideal.
Since $R$ is local, that maximal ideal must be
$$
\mathfrak m.
$$
Thus
$$
a\in\mathfrak m.
$$
Hence
$$
N\subseteq\mathfrak m.
$$
Combining the two inclusions,
$$
N=\mathfrak m.
$$
:::

<1>4. Therefore, if $R$ is local, then the set of nonunits is an ideal.

::: {.proof}
By step <1>3, the set of nonunits is exactly the maximal ideal
$$
\mathfrak m,
$$
which is an ideal.
:::

<1>5. Conversely, assume the set $N$ of nonunits is an ideal.
Then $N$ is proper.

::: {.proof}
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

<1>6. Every nonzero element of
$$
R/N
$$
is invertible.

::: {.proof}
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
Then in the quotient,
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

<1>7. The quotient
$$
R/N
$$
is a field.

::: {.proof}
By step <1>5, the quotient is nonzero.
It is commutative with identity because $R$ is.
Step <1>6 shows every nonzero element is invertible.
Hence
$$
R/N
$$
is a field.
:::

<1>8. The ideal $N$ is maximal.

::: {.proof}
By step <1>7,
$$
R/N
$$
is a field.
The maximal-ideal quotient criterion therefore gives that
$$
N
$$
is maximal.
:::

<1>9. Every proper ideal of $R$ is contained in $N$.

::: {.proof}
Let
$$
I\trianglelefteq R
$$
be proper.
No element of $I$ can be a unit, because if
$$
u\in I
$$
were a unit, then
$$
1=u^{-1}u
\in
I,
$$
forcing
$$
I=R.
$$
Thus every element of $I$ is a nonunit:
$$
I\subseteq N.
$$
:::

<1>10. The ideal $N$ is the unique maximal ideal of $R$.

::: {.proof}
Let
$$
M
$$
be any maximal ideal.
It is proper, so step <1>9 gives
$$
M\subseteq N.
$$
But $N$ is proper by step <1>5.
Maximality of $M$ therefore forces
$$
M=N.
$$
Thus every maximal ideal equals $N$.
:::

<1>11. Therefore
$$
\boxed{
R\text{ is local}
\iff
\{\text{nonunits of }R\}
\text{ is an ideal}.
}
$$

::: {.proof}
Step <1>4 proves the forward implication, and step <1>10 proves the converse.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>11 is the required equivalence.
:::
:::
