---
schema: qual/card@1
id: P-WESRA14-7
kind: problem
title: 'A Borel set that is measure-theoretically thick in every interval'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Construct a Borel set $E\subset\RR$ such that
\[
0<m(E\cap I)<m(I)
\]
for every finite nonempty nondegenerate interval $I$.
:::

::: {.solution}

Let
\[
\{J_1,J_2,\dots\}
\]
be an enumeration of all bounded open intervals with rational endpoints.

::: pf

::: {.pf-step #s1-1}

Every nonempty nondegenerate interval
\[
I\subset\RR
\]
contains some
\[
J_n.
\]


::: pf-proof

Choose two rational numbers
\[
a<b
\]
strictly inside $I$.
Then
\[
(a,b)
\subseteq
I,
\]
and this interval occurs somewhere in the enumeration.

:::

:::

::: {.pf-step #s1-2}

Every nonempty open interval
\[
U
\]
contains a compact nowhere-dense set of strictly positive Lebesgue measure.


::: pf-proof

Take the Smith--Volterra--Cantor set
\[
S\subset[0,1],
\]
which is compact, nowhere dense, and has
\[
m(S)=\frac12.
\]

Choose a closed subinterval
\[
[a,b]\subset U.
\]
The affine image
\[
a+(b-a)S
\]
is compact and nowhere dense and has measure
\[
(b-a)m(S)
>
0.
\]

:::

:::

::: {.pf-step #s1-3}

We construct recursively pairs of compact nowhere-dense sets
\[
K_n,L_n
\subseteq
J_n
\]
such that
\[
m(K_n)>0,
\qquad
m(L_n)>0,
\]
and all sets in the family
\[
K_1,L_1,K_2,L_2,dots
\]
are pairwise disjoint.


::: pf-proof

Assume
\[
K_1,L_1,dots,K_{n-1},L_{n-1}
\]
have been chosen.
Their finite union
\[
F_{n-1}
\]
is compact and nowhere dense.

Therefore
\[
J_n\setminus F_{n-1}
\]
is a nonempty open subset of $J_n$.
Choose two disjoint nonempty open intervals
\[
U_n,V_n
\subseteq
J_n\setminus F_{n-1}.
\]

By step [](#s1-2){.pf-ref}, choose a compact nowhere-dense positive-measure set
\[
K_n\subseteq U_n
\]
and another
\[
L_n\subseteq V_n.
\]
They are disjoint from each other and from every earlier set.
This completes the induction.

:::

:::

::: {.pf-step #s1-4}

Define
\[
\boxed{
E
\coloneqq
\bigcup_{n=1}^{\infty}K_n.
}
\]
Then $E$ is Borel.


::: pf-proof

Each
\[
K_n
\]
is compact, hence closed.
Therefore $E$ is an
\[
F_\sigma
\]
set, hence Borel.

:::

:::

::: {.pf-step #s1-5}

For every
\[
n,
\]
one has
\[
K_n\subseteq E
\]
and
\[
L_n\subseteq\RR\setminus E.
\]


::: pf-proof

The first inclusion is immediate from the definition of $E$.

By step [](#s1-3){.pf-ref}, every $L_n$ is disjoint from every $K_m$, including those
chosen later because each later stage avoids all previously chosen $L_n$.
Hence
\[
L_n
\cap
E
=
\varnothing.
\]

:::

:::

::: {.pf-step #s1-6}

Let
\[
I
\]
be any finite nonempty nondegenerate interval.
Choose
\[
J_n\subseteq I
\]
as in step [](#s1-1){.pf-ref}.
Then
\[
m(E\cap I)>0.
\]


::: pf-proof

Since
\[
K_n
\subseteq
J_n
\subseteq
I
\]
and
\[
K_n\subseteq E,
\]
one has
\[
K_n
\subseteq
E\cap I.
\]
Therefore
\[
m(E\cap I)
\ge
m(K_n)
>
0.
\]

:::

:::

::: {.pf-step #s1-7}

For the same interval $I$,
\[
m(I\setminus E)>0.
\]


::: pf-proof

By step [](#s1-5){.pf-ref},
\[
L_n
\subseteq
\RR\setminus E.
\]
Also
\[
L_n
\subseteq
J_n
\subseteq
I.
\]
Thus
\[
L_n
\subseteq
I\setminus E,
\]
so
\[
m(I\setminus E)
\ge
m(L_n)
>
0.
\]

:::

:::

::: {.pf-step #s1-8}

Hence
\[
m(E\cap I)
<
m(I).
\]


::: pf-proof

The disjoint decomposition
\[
I
=
(E\cap I)
\sqcup
(I\setminus E)
\]
gives
\[
m(I)
=
m(E\cap I)
+
m(I\setminus E).
\]
Step [](#s1-7){.pf-ref} shows the second summand is strictly positive.
Therefore
\[
m(E\cap I)
<
m(I).
\]

:::

:::

::: {.pf-step #s1-9}

Consequently
\[
\boxed{
0
<
m(E\cap I)
<
m(I)
}
\]
for every finite nonempty nondegenerate interval $I$.


::: pf-proof

The left inequality is step [](#s1-6){.pf-ref} and the right inequality is step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} constructs a Borel set $E$, and step [](#s1-9){.pf-ref} proves it has the
required measure-theoretic thickness in every interval.

:::

:::

:::
