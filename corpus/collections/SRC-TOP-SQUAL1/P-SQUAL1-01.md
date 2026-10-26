---
schema: qual/card@1
id: P-SQUAL1-01
kind: problem
title: Intersecting a dense set with a subspace, and the open-subspace case
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
A subset $D\subseteq X$ is called dense if $\overline D=X$.

1. Show that if $A\subseteq X$ and $D$ is dense in $X$, then $D\cap A$ need not be dense in $A$.
2. Show that if $A$ is open in $X$ and $D$ is dense in $X$, then $D\cap A$ is dense in $A$.
:::

## Part 1

::: pf

::: pf-step

Take
\[
X=\mathbb R
\]
with its usual topology,
\[
D=\mathbb Q,
\]
and
\[
A=\mathbb R\setminus\mathbb Q.
\]


::: pf-proof

This specifies a concrete example.

:::

:::

::: pf-step

The set \(D=\mathbb Q\) is dense in \(\mathbb R\).


::: pf-proof

Every nonempty open interval in \(\mathbb R\) contains a rational number.
Equivalently,
\[
\overline{\mathbb Q}=\mathbb R.
\]

:::

:::

::: pf-step

One has
\[
\boxed{D\cap A=\varnothing}.
\]


::: pf-proof

The sets of rational and irrational numbers are disjoint.

:::

:::

::: pf-step

Since \(A\ne\varnothing\),
\[
\boxed{
D\cap A
\text{ is not dense in }A}.
\]


::: pf-proof

The closure in \(A\) of the empty set is empty:
\[
\overline{\varnothing}^{\,A}
=
\varnothing
\ne
A.
\]

:::

:::

::: pf-step

Therefore, for an arbitrary subspace \(A\subseteq X\), density of \(D\) in \(X\) does not imply density of \(D\cap A\) in \(A\).


::: pf-proof

Steps <1>1--<1>4 give the required counterexample.

:::

:::

::: pf-step

Let
\[
U\subseteq A
\]
be a nonempty open set in the subspace topology on \(A\).


::: pf-proof

To prove density of \(D\cap A\) in \(A\), it suffices to show that every nonempty open subset of \(A\) meets \(D\cap A\).

:::

:::

::: pf-step

There exists an open set
\[
V\subseteq X
\]
such that
\[
\boxed{U=A\cap V}.
\]


::: pf-proof

This is the definition of the subspace topology.

:::

:::

::: pf-step

Since both \(A\) and \(V\) are open in \(X\),
\[
\boxed{U\text{ is open in }X}.
\]


::: pf-proof

By step <1>7,
\[
U=A\cap V,
\]
an intersection of two open subsets of \(X\).

:::

:::

::: pf-step

Because \(U\ne\varnothing\) and \(D\) is dense in \(X\),
\[
\boxed{U\cap D\ne\varnothing}.
\]


::: pf-proof

A subset is dense exactly when it meets every nonempty open set.
Apply this to the nonempty open set \(U\subseteq X\) from step <1>8.

:::

:::

::: pf-step

Since \(U\subseteq A\),
\[
U\cap D
=
U\cap(D\cap A).
\]


::: pf-proof

Every point of \(U\) already lies in \(A\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
U\cap(D\cap A)\ne\varnothing}.
\]


::: pf-proof

Combine steps <1>9--<1>10.

:::

:::

::: pf-step

Hence every nonempty open subset of \(A\) meets \(D\cap A\).


::: pf-proof

The set \(U\) in step <1>6 was arbitrary.

:::

:::

::: pf-step

Thus
\[
\boxed{
\overline{D\cap A}^{\,A}
=
A}.
\]


::: pf-proof

Step <1>12 is exactly the open-set characterization of density in the subspace \(A\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
D\cap A
\text{ is dense in }A}.
\]


::: pf-proof

This is step <1>13.

:::

:::

::: pf-qed

Step <1>5 answers part 1, and step <1>14 proves part 2.

:::

:::
