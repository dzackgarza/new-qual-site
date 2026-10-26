---
schema: qual/card@1
id: P-WESTOP10-I3
kind: problem
title: Urysohn metrization and metrizable compact images
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. State the Urysohn Metrization Theorem.
2. Prove that the continuous image of a compact metric space in a Hausdorff space is metrizable.
:::

::: pf

::: pf-step

**Urysohn Metrization Theorem.**

Every
\[
T_1
\]
regular second-countable space is metrizable.


::: pf-proof

Equivalently, under the common convention that “regular” already includes
the $T_1$ condition, every regular second-countable space is metrizable.
This is the theorem statement.

:::

:::

::: pf-step

Let
\[
X
\]
be a compact metric space,
\[
Y
\]
a Hausdorff space, and
\[
f:X\to Y
\]
continuous.
Set
\[
K
\coloneqq
f(X)
\subseteq
Y.
\]
Then $K$ is compact and Hausdorff.


::: pf-proof

The continuous image of a compact space is compact, so
\[
K
\]
is compact.

Since $Y$ is Hausdorff, every subspace of $Y$ is Hausdorff.
Therefore $K$ is Hausdorff.

:::

:::

::: pf-step

The map
\[
f:X\to K
\]
is a closed surjection.


::: pf-proof

It is surjective by definition of
\[
K=f(X).
\]

Let
\[
C\subseteq X
\]
be closed.
Because $X$ is compact, $C$ is compact.
Then
\[
f(C)
\]
is compact in $K$.
Since $K$ is Hausdorff, compact subsets are closed.
Hence $f$ is closed.

:::

:::

::: pf-step

The compact metric space $X$ has a countable basis
\[
\mathcal B
=
\{B_1,B_2,\dots\}.
\]


::: pf-proof

Every compact metric space is separable.
Choose a countable dense set
\[
\{x_1,x_2,\dots\}
\]
and take all open balls with centers among the $x_j$ and rational radii.
These form a countable basis.

:::

:::

::: pf-step

Let
\[
\mathcal U
\]
be the family of all finite unions of elements of
\[
\mathcal B.
\]
Then
\[
\mathcal U
\]
is countable.


::: pf-proof

The set of finite subsets of a countable set is countable.
Each finite subset of
\[
\mathcal B
\]
determines one finite union.
Thus
\[
\mathcal U
\]
is countable.

:::

:::

::: pf-step

For
\[
U\in\mathcal U,
\]
define
\[
V_U
\coloneqq
K\setminus f(X\setminus U).
\]
Then
\[
V_U
\]
is open in $K$.


::: pf-proof

The set
\[
X\setminus U
\]
is closed in $X$.
By step <1>3,
\[
f(X\setminus U)
\]
is closed in $K$.
Therefore its complement
\[
V_U
\]
is open.

:::

:::

::: pf-step

A point
\[
y\in K
\]
lies in $V_U$ exactly when
\[
f^{-1}(y)
\subseteq
U.
\]


::: pf-proof

By definition,
\[
y\in V_U
\]
if and only if
\[
y\notin f(X\setminus U).
\]
This means there is no point
\[
x\in X\setminus U
\]
with
\[
f(x)=y.
\]
Equivalently, every point of the fiber
\[
f^{-1}(y)
\]
lies in $U$.

:::

:::

::: pf-step

The family
\[
\{V_U:U\in\mathcal U\}
\]
is a basis for the topology of $K$.


::: pf-proof

Let
\[
O\subseteq K
\]
be open and let
\[
y\in O.
\]
Then
\[
f^{-1}(O)
\]
is open in $X$ and contains the compact fiber
\[
F
\coloneqq
f^{-1}(y).
\]

For each
\[
x\in F,
\]
choose a basis element
\[
B_x\in\mathcal B
\]
such that
\[
x\in B_x
\subseteq
f^{-1}(O).
\]
The family
\[
\{B_x:x\in F\}
\]
covers the compact set $F$.
Choose finitely many
\[
B_{x_1},\dots,B_{x_m}
\]
covering $F$, and set
\[
U
\coloneqq
B_{x_1}\cup\cdots\cup B_{x_m}.
\]
Then
\[
U\in\mathcal U,
\qquad
F\subseteq U
\subseteq
f^{-1}(O).
\]

By step <1>7,
\[
y\in V_U.
\]

If
\[
y'\in V_U,
\]
then
\[
f^{-1}(y')
\subseteq
U
\subseteq
f^{-1}(O).
\]
Since the fiber is nonempty,
\[
y'\in O.
\]
Thus
\[
y\in V_U\subseteq O.
\]
Hence the family is a basis.

:::

:::

::: pf-step

The space $K$ is second countable.


::: pf-proof

By step <1>5,
\[
\mathcal U
\]
is countable.
Therefore the basis
\[
\{V_U:U\in\mathcal U\}
\]
from step <1>8 is countable.

:::

:::

::: pf-step

The space $K$ is regular.


::: pf-proof

Every compact Hausdorff space is normal.
In particular it is regular.
By step <1>2, $K$ is compact Hausdorff.

:::

:::

::: pf-step

Therefore
\[
\boxed{
K=f(X)
\text{ is metrizable}.
}
\]


::: pf-proof

By step <1>2, $K$ is Hausdorff, hence $T_1$.
By step <1>10, it is regular.
By step <1>9, it is second countable.
Apply the Urysohn Metrization Theorem from step <1>1.

:::

:::

::: pf-qed

Step <1>1 states the requested theorem, and steps <1>2--<1>11 prove that
the continuous image of a compact metric space in a Hausdorff space is
metrizable.

:::

:::
