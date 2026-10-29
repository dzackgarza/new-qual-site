---
schema: qual/card@1
id: P-WESRA12-1
kind: problem
title: 'Sigma-algebras, rings of sets, and finite sigma-algebras'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $X$ be nonempty and let $\mathcal A$ be a collection of subsets of $X$.

(a) Define a $\sigma$-algebra.

(b) Prove that if $A,B\in\mathcal A$, then $A\cap B\in\mathcal A$.

(c) Give a nonempty $X$, a ring $\mathcal R$ on $X$, and sets $A_n\in\mathcal R$ such that $\bigcap_{n=1}^\infty A_n\notin\mathcal R$.

(d) If $X$ has exactly four points, determine the possible cardinalities of $\sigma$-algebras on $X$, and for each cardinality determine how many such $\sigma$-algebras exist.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A collection
\[
\mathcal A\subseteq\mathcal P(X)
\]
is a **$\sigma$-algebra** if:

1. \[
   X\in\mathcal A;
   \]
2. whenever
   \[
   E\in\mathcal A,
   \]
   then
   \[
   X\setminus E\in\mathcal A;
   \]
3. whenever
   \[
   E_1,E_2,\dots\in\mathcal A,
   \]
   then
   \[
   \bigcup_{n=1}^\infty E_n
   \in
   \mathcal A.
   \]


::: pf-proof

This is the standard definition.
The empty set also belongs to $\mathcal A$ because
\[
\varnothing
=
X\setminus X.
\]

:::

:::

::: {.pf-step #s1-2}

If
\[
A,B\in\mathcal A,
\]
then
\[
A\cap B\in\mathcal A.
\]


::: pf-proof

By closure under complements,
\[
A^c,B^c\in\mathcal A.
\]
By closure under countable unions, in particular finite unions,
\[
A^c\cup B^c\in\mathcal A.
\]
Taking complements again,
\[
(A^c\cup B^c)^c
\in
\mathcal A.
\]
By De Morgan's law,
\[
(A^c\cup B^c)^c
=
A\cap B.
\]

:::

:::

::: {.pf-step #s1-3}

Let
\[
X=\NN
\]
and let
\[
\mathcal R
\coloneqq
\{E\subseteq\NN:
E\text{ is finite or cofinite}\}.
\]
Then $\mathcal R$ is a ring of sets.


::: pf-proof

The empty set is finite, so
\[
\varnothing\in\mathcal R.
\]

If $E,F$ are finite or cofinite, then
\[
E\cup F
\]
is again finite or cofinite:

- finite union finite is finite;
- if either set is cofinite, the union is cofinite.

Likewise,
\[
E\setminus F
\]
is finite or cofinite:

- finite minus anything is finite;
- cofinite minus finite is cofinite;
- cofinite minus cofinite is contained in the finite complement of the
  second set, hence finite.

Thus $\mathcal R$ is closed under finite unions and differences, so it is
a ring of sets.

:::

:::

::: {.pf-step #s1-4}

For
\[
n\ge1,
\]
define
\[
A_n
\coloneqq
\NN\setminus\{2n\}.
\]
Then
\[
A_n\in\mathcal R
\]
for every $n$, but
\[
\bigcap_{n=1}^\infty A_n
\notin
\mathcal R.
\]


::: pf-proof

Each $A_n$ is cofinite, so
\[
A_n\in\mathcal R.
\]

Their intersection is
\[
\bigcap_{n=1}^\infty
(\NN\setminus\{2n\})
=
\NN\setminus\{2,4,6,\dots\},
\]
the set of odd positive integers.
This set is infinite, and its complement is also infinite.
Hence it is neither finite nor cofinite, so it does not belong to
\[
\mathcal R.
\]

:::

:::

::: {.pf-step #s1-5}

Let $X$ be finite and let
\[
\mathcal A
\]
be a $\sigma$-algebra on $X$.
For
\[
x\in X,
\]
define the atom containing $x$ by
\[
P_x
\coloneqq
\bigcap
\{E\in\mathcal A:x\in E\}.
\]
Then
\[
P_x\in\mathcal A.
\]


::: pf-proof

Because $X$ is finite, its power set is finite, so
\[
\mathcal A
\]
is finite.
Therefore the displayed intersection is a finite intersection of members of
$\mathcal A$.
By repeated use of step [](#s1-2){.pf-ref},
\[
P_x\in\mathcal A.
\]
Also
\[
x\in P_x.
\]

:::

:::

::: {.pf-step #s1-6}

The distinct sets among the $P_x$ form a partition of $X$.


::: pf-proof

Every point lies in its own atom, so the atoms cover $X$.

Suppose
\[
P_x\cap P_y\ne\varnothing.
\]
If
\[
y\notin P_x,
\]
then by definition of $P_x$ there is some
\[
E\in\mathcal A
\]
with
\[
x\in E
\quad\text{and}\quad
y\notin E.
\]
Then
\[
P_x\subseteq E.
\]
Since
\[
y\in E^c,
\]
one has
\[
P_y\subseteq E^c.
\]
Thus
\[
P_x\cap P_y
=
\varnothing,
\]
contradiction.

Therefore
\[
y\in P_x.
\]
By symmetry
\[
x\in P_y.
\]
This implies
\[
P_x=P_y.
\]
Hence distinct atoms are disjoint.

:::

:::

::: {.pf-step #s1-7}

Every set
\[
E\in\mathcal A
\]
is a union of atoms.


::: pf-proof

Let
\[
x\in E.
\]
Since $E$ is one of the measurable sets containing $x$, the definition of
$P_x$ gives
\[
P_x\subseteq E.
\]
Thus
\[
E
=
\bigcup_{x\in E}P_x.
\]
After removing duplicates, this is a union of distinct atoms.

:::

:::

::: {.pf-step #s1-8}

Conversely, every union of atoms belongs to
\[
\mathcal A.
\]


::: pf-proof

Each atom belongs to $\mathcal A$ by step [](#s1-5){.pf-ref}.
There are only finitely many atoms.
Finite unions of members of a $\sigma$-algebra belong to the
$\sigma$-algebra.

:::

:::

::: {.pf-step #s1-9}

If a finite $\sigma$-algebra has exactly
\[
k
\]
atoms, then
\[
|\mathcal A|
=
2^k.
\]


::: pf-proof

By steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref}, measurable sets are exactly unions of atoms.
Choosing a measurable set is therefore equivalent to choosing an arbitrary
subset of the set of $k$ atoms.
There are
\[
2^k
\]
such choices.

:::

:::

::: {.pf-step #s1-10}

If
\[
|X|=4,
\]
the possible numbers of atoms are
\[
k=1,2,3,4.
\]
Hence the possible cardinalities of $\sigma$-algebras are
\[
\boxed{
2,4,8,16.
}
\]


::: pf-proof

A partition of a four-point set has between one and four nonempty blocks.
Apply step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

There is exactly one $\sigma$-algebra of cardinality
\[
2.
\]


::: pf-proof

This corresponds to the one-block partition
\[
\{X\}.
\]
The resulting $\sigma$-algebra is
\[
\{\varnothing,X\}.
\]

:::

:::

::: {.pf-step #s1-12}

There are exactly
\[
7
\]
$\sigma$-algebras of cardinality
\[
4.
\]


::: pf-proof

A four-element $\sigma$-algebra has exactly two atoms, so it has the form
\[
\{\varnothing,A,A^c,X\}
\]
for some nonempty proper subset
\[
A\subsetneq X.
\]
There are
\[
2^4-2
=
14
\]
nonempty proper subsets.
The subsets $A$ and $A^c$ define the same $\sigma$-algebra, and no other
duplication occurs.
Therefore the number is
\[
\frac{14}{2}
=
7.
\]

:::

:::

::: {.pf-step #s1-13}

There are exactly
\[
6
\]
$\sigma$-algebras of cardinality
\[
8.
\]


::: pf-proof

An eight-element $\sigma$-algebra has three atoms.
A partition of a four-point set into three nonempty blocks must have block
sizes
\[
2,1,1.
\]
Such a partition is uniquely determined by the two-element block.
There are
\[
\binom42
=
6
\]
choices.

:::

:::

::: {.pf-step #s1-14}

There is exactly one $\sigma$-algebra of cardinality
\[
16.
\]


::: pf-proof

This corresponds to the four singleton atoms.
Every subset is then a union of atoms, so the $\sigma$-algebra is the full
power set
\[
\mathcal P(X),
\]
which is unique.

:::

:::

::: {.pf-step #s1-15}

The complete table is
\[
\boxed{
\begin{array}{c|cccc}
|\mathcal A|
&2&4&8&16\\
\hline
\text{number of }\sigma\text{-algebras}
&1&7&6&1
\end{array}
}
\]


::: pf-proof

Collect steps [](#s1-11){.pf-ref} through [](#s1-14){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), step [](#s1-2){.pf-ref} answers part (b),
steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} answer part (c), and steps [](#s1-5){.pf-ref} through [](#s1-15){.pf-ref} answer part (d).

:::

:::

:::
