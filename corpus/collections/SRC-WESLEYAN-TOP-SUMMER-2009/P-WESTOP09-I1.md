---
schema: qual/card@1
id: P-WESTOP09-I1
kind: problem
title: Metrizable spaces under products, subspaces, and quotients
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Define a metric and a metrizable topological space.
2. Give an example, with justification, of a nonmetrizable space.
3. Determine whether the class of metrizable spaces is closed under each of the following constructions, giving short proofs for positive answers and counterexamples for negative answers:
   - arbitrary products;
   - subspaces;
   - quotient spaces.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A metric on a set $X$ is a function
\[
d:X\times X\to[0,\infty)
\]
such that for all $x,y,z\in X$,
\[
d(x,y)=0\Longleftrightarrow x=y,\qquad
d(x,y)=d(y,x),\qquad
d(x,z)\le d(x,y)+d(y,z).
\]
A topological space $X$ is metrizable if its topology is the topology induced
by some metric on $X$.


::: pf-proof

These are the defining properties of a metric and of metrizability.

:::

:::

::: {.pf-step #s1-2}

If $I$ is uncountable, the product
\[
X=\{0,1\}^I
\]
of two-point discrete spaces, with the product topology, is not metrizable.


::: pf-proof

Let $0\in X$ denote the point all of whose coordinates are $0$. Suppose that
$X$ were first countable at $0$, with countable local base
\[
U_1,U_2,\ldots.
\]
For each $n$, choose a basic product neighborhood $B_n$ of $0$ with
$B_n\subseteq U_n$. Each $B_n$ restricts only finitely many coordinates; let
$F_n\subset I$ be that finite set. Then
\[
F=\bigcup_{n=1}^\infty F_n
\]
is countable, so choose $j\in I\setminus F$. The set
\[
V=\{x\in X:x_j=0\}
\]
is an open neighborhood of $0$. Since the $U_n$ form a local base, some
$U_n\subseteq V$, hence $B_n\subseteq V$. But $j\notin F_n$, so $B_n$ does not
restrict the $j$-th coordinate and therefore contains a point with $x_j=1$,
a contradiction. Thus $X$ is not first countable. Every metric space is first
countable, so $X$ is not metrizable.

:::

:::

::: {.pf-step #s1-3}

The class of metrizable spaces is
\[
\boxed{\text{not closed under arbitrary products}}.
\]


::: pf-proof

Step [](#s1-2){.pf-ref} gives an uncountable product of metrizable spaces whose product
topology is not metrizable.

:::

:::

::: pf-step

The class of metrizable spaces is
\[
\boxed{\text{closed under subspaces}}.
\]


::: pf-proof

Let $(X,d)$ be a metric space and let $A\subseteq X$. The restriction
\[
d|_{A\times A}:A\times A\to[0,\infty)
\]
is a metric on $A$. Its open balls are exactly
\[
B_A(a,r)=A\cap B_X(a,r),
\]
so the induced metric topology is precisely the subspace topology on $A$.

:::

:::

::: {.pf-step #s1-5}

The class of metrizable spaces is
\[
\boxed{\text{not closed under quotient spaces}}.
\]


::: pf-proof

On the metrizable space $\RR$, identify all nonzero points with one
another and leave $0$ in its own equivalence class. The quotient has two
points, say
\[
p=[0],\qquad q=[\RR\setminus\{0\}].
\]
The singleton $\{q\}$ is open because its preimage
$\RR\setminus\{0\}$ is open. The singleton $\{p\}$ is not open because
its preimage $\{0\}$ is not open. Thus the quotient is not Hausdorff: the two
points cannot have disjoint open neighborhoods. Every metric space is
Hausdorff, so this quotient is not metrizable.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definitions, step [](#s1-2){.pf-ref} gives a nonmetrizable
example, and steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref} settle the three closure questions.

:::

:::

:::
