---
schema: qual/card@1
id: P-KSRING17-141
kind: problem
title: Ideals maximal for non-Artinian or non-Noetherian module quotients $N/NI$ are prime
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 141 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the script set name I, which the extraction split into I and T, against problem 141 on Ring_Theory_Qual_Problems.pdf PDF page 16.
---

::: {.problem}
Let $R$ be a commutative ring with $1$ and let $M$ be an $R$-module that is not Artinian (Noetherian, of finite composition length).
Let $\mathcal{I}$ be the set of ideals $I$ of $R$ such that there exists an $R$-submodule $N$ of $M$ with the property that $N/NI$ is not Artinian (Noetherian, of finite composition length, respectively).
Show that if $A \in \mathcal{I}$ is a maximal element of $\mathcal{I}$, then $A$ is a prime ideal of $R$.
:::

Fix one of the three properties
$$
\mathsf P
\in
\{
\text{Artinian},
\text{Noetherian},
\text{finite composition length}
\}.
$$
The same argument applies in each case.

::: pf

::: pf-step

The class of modules satisfying $\mathsf P$ is closed under quotients.


::: pf-proof

If
$$
L
$$
is Artinian, every descending chain of submodules in a quotient
$$
L/K
$$
lifts to a descending chain of submodules of $L$ containing $K$, so it stabilizes.

If
$$
L
$$
is Noetherian, every ascending chain in
$$
L/K
$$
lifts to an ascending chain in $L$, so it stabilizes.

If
$$
L
$$
has finite composition length, every quotient has length at most
$$
\ell(L),
$$
and in particular finite length.

:::

:::

::: pf-step

The class of modules satisfying $\mathsf P$ is closed under extensions.


::: pf-proof

Suppose
$$
0
\longrightarrow
L'
\longrightarrow
L
\longrightarrow
L''
\longrightarrow
0
$$
is exact.

For the Artinian case, let
$$
L_1
\supseteq
L_2
\supseteq
\cdots
$$
be a descending chain in $L$.
Its images in $L''$ stabilize because $L''$ is Artinian, and its intersections with $L'$ stabilize because $L'$ is Artinian.
Once both stabilize, the original chain stabilizes.

For the Noetherian case, the same argument with ascending chains shows that if $L'$ and $L''$ are Noetherian, then so is $L$.

For finite composition length,
$$
\ell(L)
=
\ell(L')
+
\ell(L''),
$$
so finiteness of the two end lengths implies finiteness of the middle one.

:::

:::

::: pf-step

The maximal element $A\in\mathcal I$ is proper.


::: pf-proof

If
$$
A=R,
$$
then for every submodule
$$
N\subseteq M,
$$
one has
$$
NA=NR=N.
$$
Thus
$$
N/NA=0,
$$
and the zero module satisfies all three properties $\mathsf P$.
Hence
$$
R\notin\mathcal I.
$$
Therefore
$$
A\ne R.
$$

:::

:::

::: pf-step

Since
$$
A\in\mathcal I,
$$
there exists a submodule
$$
N\subseteq M
$$
such that
$$
N/NA
$$
does not satisfy $\mathsf P$.


::: pf-proof

This is the definition of membership
$$
A\in\mathcal I.
$$
Fix such a witness $N$ for the rest of the proof.

:::

:::

::: pf-step

Suppose, for contradiction, that
$$
ab\in A
$$
with
$$
a\notin A,
\qquad
b\notin A.
$$
Then
$$
A
\subsetneq
A+(a)
$$
and
$$
A
\subsetneq
A+(b).
$$


::: pf-proof

Because
$$
a\notin A,
$$
adjoining $a$ strictly enlarges $A$.
Likewise for $b$.

:::

:::

::: pf-step

The ideals
$$
A+(a)
\qquad\text{and}\qquad
A+(b)
$$
do not belong to $\mathcal I$.


::: pf-proof

The ideal $A$ is maximal in
$$
\mathcal I.
$$
By step <1>5, each displayed ideal strictly contains $A$.
Hence neither can belong to $\mathcal I$.

:::

:::

::: pf-step

Therefore
$$
N/N(A+(a))
$$
and
$$
N/N(A+(b))
$$
both satisfy $\mathsf P$.


::: pf-proof

If, for example,
$$
N/N(A+(a))
$$
failed $\mathsf P$, then the same witness submodule $N$ would show
$$
A+(a)
\in
\mathcal I,
$$
contradicting step <1>6.
The argument for
$$
A+(b)
$$
is identical.

:::

:::

::: pf-step

Set
$$
L
\coloneqq
N(A+(a))
=
NA+Na.
$$
Then there is a short exact sequence
$$
0
\longrightarrow
L/NA
\longrightarrow
N/NA
\longrightarrow
N/L
\longrightarrow
0.
$$


::: pf-proof

Because
$$
NA\subseteq L\subseteq N,
$$
the standard quotient sequence gives
$$
0
\to
L/NA
\to
N/NA
\to
N/L
\to
0.
$$

:::

:::

::: pf-step

The quotient
$$
N/L
$$
satisfies $\mathsf P$.


::: pf-proof

By definition,
$$
L=N(A+(a)).
$$
Thus
$$
N/L
=
N/N(A+(a)),
$$
which satisfies $\mathsf P$ by step <1>7.

:::

:::

::: pf-step

Multiplication by $a$ induces a surjective homomorphism
$$
\theta:
N
\longrightarrow
L/NA,
\qquad
\theta(n)
\coloneqq
na+NA.
$$


::: pf-proof

The map is $R$-linear because $R$ is commutative.
Its image is
$$
(Na+NA)/NA
=
L/NA.
$$
Hence it is surjective.

:::

:::

::: pf-step

The kernel of $\theta$ contains
$$
N(A+(b))
=
NA+Nb.
$$


::: pf-proof

First let
$$
n\in NA.
$$
Then
$$
na\in NA
$$
because $NA$ is a submodule.
Hence
$$
n\in\ker\theta.
$$

Now let
$$
n\in Nb.
$$
Write
$$
n=n'b
$$
for some
$$
n'\in N.
$$
Then
$$
na
=
n'ba
=
n'(ab).
$$
Since
$$
ab\in A,
$$
one has
$$
n'(ab)\in NA.
$$
Thus
$$
n\in\ker\theta.
$$

Therefore
$$
NA+Nb
\subseteq
\ker\theta.
$$

:::

:::

::: pf-step

The module
$$
L/NA
$$
is a quotient of
$$
N/N(A+(b)).
$$


::: pf-proof

By step <1>11,
$$
N(A+(b))
\subseteq
\ker\theta.
$$
Therefore the surjection $\theta$ factors through the quotient:
$$
N/N(A+(b))
\twoheadrightarrow
L/NA.
$$

:::

:::

::: pf-step

The module
$$
L/NA
$$
satisfies $\mathsf P$.


::: pf-proof

By step <1>7,
$$
N/N(A+(b))
$$
satisfies $\mathsf P$.
By step <1>12,
$$
L/NA
$$
is its quotient.
Apply quotient-closure from step <1>1.

:::

:::

::: pf-step

The module
$$
N/NA
$$
satisfies $\mathsf P$.


::: pf-proof

In the exact sequence from step <1>8, the submodule
$$
L/NA
$$
satisfies $\mathsf P$ by step <1>13, and the quotient
$$
N/L
$$
satisfies $\mathsf P$ by step <1>9.
By extension-closure from step <1>2,
$$
N/NA
$$
satisfies $\mathsf P$.

:::

:::

::: pf-step

This contradicts the choice of $N$ in step <1>4.


::: pf-proof

Step <1>4 says
$$
N/NA
$$
does not satisfy $\mathsf P$, while step <1>14 says that it does.

:::

:::

::: pf-step

Therefore
$$
ab\in A
\implies
a\in A
\text{ or }
b\in A.
$$


::: pf-proof

If both factors lay outside $A$, steps <1>5--<1>15 would produce a contradiction.

:::

:::

::: pf-step

Hence
$$
\boxed{
A
\text{ is a prime ideal of }R.
}
$$


::: pf-proof

Step <1>3 shows $A$ is proper, and step <1>16 gives the prime-product condition.

:::

:::

::: pf-qed

The argument applies verbatim when $\mathsf P$ is Artinian, Noetherian, or finite composition length.
Thus step <1>17 proves all three versions of the problem.

:::

:::
