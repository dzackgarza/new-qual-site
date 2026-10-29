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

::: {.solution}

## Part 1

::: pf

::: {.pf-step #s1-1}

Take
\[
X=\RR
\]
with its usual topology,
\[
D=\QQ,
\]
and
\[
A=\RR\setminus\QQ.
\]


::: pf-proof

This specifies a concrete example.

:::

:::

::: {.pf-step #s1-2}

The set \(D=\QQ\) is dense in \(\RR\).


::: pf-proof

Every nonempty open interval in \(\RR\) contains a rational number.
Equivalently,
\[
\overline{\QQ}=\RR.
\]

:::

:::

::: {.pf-step #s1-3}

One has
\[
\boxed{D\cap A=\varnothing}.
\]


::: pf-proof

The sets of rational and irrational numbers are disjoint.

:::

:::

::: {.pf-step #s1-4}

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

::: {.pf-step #s1-5}

Therefore, for an arbitrary subspace \(A\subseteq X\), density of \(D\) in \(X\) does not imply density of \(D\cap A\) in \(A\).


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} give the required counterexample.

:::

:::

::: {.pf-step #s1-6}

Let
\[
U\subseteq A
\]
be a nonempty open set in the subspace topology on \(A\).


::: pf-proof

To prove density of \(D\cap A\) in \(A\), it suffices to show that every nonempty open subset of \(A\) meets \(D\cap A\).

:::

:::

::: {.pf-step #s1-7}

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

::: {.pf-step #s1-8}

Since both \(A\) and \(V\) are open in \(X\),
\[
\boxed{U\text{ is open in }X}.
\]


::: pf-proof

By step [](#s1-7){.pf-ref},
\[
U=A\cap V,
\]
an intersection of two open subsets of \(X\).

:::

:::

::: {.pf-step #s1-9}

Because \(U\ne\varnothing\) and \(D\) is dense in \(X\),
\[
\boxed{U\cap D\ne\varnothing}.
\]


::: pf-proof

A subset is dense exactly when it meets every nonempty open set.
Apply this to the nonempty open set \(U\subseteq X\) from step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

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

Combine steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Hence every nonempty open subset of \(A\) meets \(D\cap A\).


::: pf-proof

The set \(U\) in step [](#s1-6){.pf-ref} was arbitrary.

:::

:::

::: {.pf-step #s1-13}

Thus
\[
\boxed{
\overline{D\cap A}^{\,A}
=
A}.
\]


::: pf-proof

Step [](#s1-12){.pf-ref} is exactly the open-set characterization of density in the subspace \(A\).

:::

:::

::: {.pf-step #s1-14}

Therefore
\[
\boxed{
D\cap A
\text{ is dense in }A}.
\]


::: pf-proof

This is step [](#s1-13){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} answers part 1, and step [](#s1-14){.pf-ref} proves part 2.

:::

:::

:::
