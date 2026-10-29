---
schema: qual/card@1
id: P-WESTOP09-I2
kind: problem
title: The slotted plane is Hausdorff, separable, nonregular, and not first countable
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Define the *slotted plane* to be $\RR^2$ with the following topology: a set $U$ is open if for every $x\in U$ there are an ordinary open disk $D$ about $x$, an integer $k\ge0$, and straight lines $L_1,\dots,L_k$ through $x$ such that
\[
\{x\}\cup\bigl(D\setminus(L_1\cup\cdots\cup L_k)\bigr)\subseteq U.
\]

1. Prove that these sets form a topology finer than the usual topology on $\RR^2$.
2. Prove that the slotted plane is Hausdorff but not regular.
3. Prove that it is separable but not first countable.
:::

::: {.solution}

For a point $x$, an ordinary open disk $D$ about $x$, and finitely many lines
$L_1,\dots,L_k$ through $x$, write
\[
B(x;D;L_1,\dots,L_k)
=\{x\}\cup\bigl(D\setminus(L_1\cup\cdots\cup L_k)\bigr).
\]

::: pf

::: {.pf-step #s1-1}

The declared open sets form a topology on $\RR^2$.


::: pf-proof

The empty set satisfies the defining condition vacuously, and $\RR^2$
satisfies it by taking $k=0$ at every point.

An arbitrary union of declared open sets is open: if a point lies in the
union, it lies in one member, and a basic slotted neighborhood witnessing
openness of that member also lies in the union.

Now let $U$ and $V$ be declared open and let $x\in U\cap V$. Choose
\[
B(x;D_1;L_1,\dots,L_k)\subseteq U
\]
and
\[
B(x;D_2;M_1,\dots,M_\ell)\subseteq V.
\]
Choose an ordinary disk $D$ about $x$ with $D\subseteq D_1\cap D_2$. Then
\[
B(x;D;L_1,\dots,L_k,M_1,\dots,M_\ell)
\subseteq U\cap V.
\]
Hence finite intersections are open, proving the topology axioms.

:::

:::

::: {.pf-step #s1-2}

The slotted-plane topology is strictly finer than the usual topology.


::: pf-proof

Every ordinary open set $U$ is slotted-open: for $x\in U$, choose an ordinary
disk $D$ with $x\in D\subseteq U$ and take $k=0$.

To see that the inclusion is strict, let $o=(0,0)$, let $L$ be the $x$-axis,
and let $D$ be the ordinary unit disk. Then
\[
W=\{o\}\cup(D\setminus L)
\]
is slotted-open. At $o$ this is a basic slotted neighborhood; at every other
point of $W$, a sufficiently small ordinary disk lies in $D\setminus L$.
However, $W$ is not open in the usual topology because no ordinary disk about
$o$ is contained in $W$.

:::

:::

::: {.pf-step #s1-3}

The slotted plane is Hausdorff.


::: pf-proof

By step [](#s1-2){.pf-ref}, the slotted topology is finer than the usual Euclidean topology.
Distinct points have disjoint Euclidean open neighborhoods, and those
neighborhoods remain open in the finer topology.

:::

:::

::: {.pf-step #s1-4}

Let
\[
F=\{(1/n,0):n\ge1\}.
\]
Then $F$ is closed in the slotted plane and $o=(0,0)\notin F$.


::: pf-proof

It suffices to show that every point outside $F$ has a slotted-open
neighborhood disjoint from $F$.

At $o$, remove the $x$-axis from a small ordinary disk:
\[
\{o\}\cup(D\setminus L)
\]
is a slotted neighborhood disjoint from $F$. If $x$ lies on the $x$-axis but
$x\notin F\cup\{o\}$, the same construction centered at $x$, again slotting
out the $x$-axis, misses $F$. If $x$ lies off the $x$-axis, an ordinary disk
about $x$ can be chosen disjoint from the $x$-axis and hence from $F$.
Therefore $\RR^2\setminus F$ is slotted-open.

:::

:::

::: {.pf-step #s1-5}

If $U$ is any slotted-open neighborhood of $o$, then
\[
\overline U\cap F\ne\varnothing.
\]


::: pf-proof

Choose a basic slotted neighborhood
\[
B=B(o;D;L_1,\dots,L_k)\subseteq U.
\]
Since $D$ is an ordinary disk about $o$, choose $n$ large enough that
\[
p_n=(1/n,0)\in D.
\]
We claim that $p_n\in\overline B$. Let $N$ be any slotted-open neighborhood
of $p_n$, and choose
\[
C=B(p_n;E;M_1,\dots,M_\ell)\subseteq N.
\]
The ordinary open set $D\cap E$ contains $p_n$. A finite union of straight
lines has empty Euclidean interior, so there is a point
\[
q\in(D\cap E)\setminus
\bigl(L_1\cup\cdots\cup L_k\cup M_1\cup\cdots\cup M_\ell\bigr).
\]
Then $q\in B\cap C\subseteq B\cap N$. Thus every neighborhood of $p_n$
meets $B$, proving $p_n\in\overline B\subseteq\overline U$. Since
$p_n\in F$, the claim follows.

:::

:::

::: {.pf-step #s1-6}

The slotted plane is not regular.


::: pf-proof

By step [](#s1-3){.pf-ref} the space is Hausdorff, hence $T_1$. In a regular $T_1$ space,
given a closed set $F$ and a point $o\notin F$, there is an open neighborhood
$U$ of $o$ such that
\[
\overline U\cap F=\varnothing:
\]
indeed, separate $o$ and $F$ by disjoint open sets $U$ and $V$; then
$\overline U\subseteq X\setminus V$.

For the closed set $F$ in step [](#s1-4){.pf-ref}, step [](#s1-5){.pf-ref} shows that no neighborhood of
$o$ has closure disjoint from $F$. Hence the slotted plane is not regular.

:::

:::

::: {.pf-step #s1-7}

The slotted plane is separable.


::: pf-proof

The countable set $\QQ^2$ is dense. Let $U$ be a nonempty slotted-open
set and choose $x\in U$ together with
\[
B(x;D;L_1,\dots,L_k)\subseteq U.
\]
The Euclidean open set
\[
D\setminus(L_1\cup\cdots\cup L_k)
\]
is nonempty, because finitely many lines cannot contain an open disk. Since
$\QQ^2$ is dense in the Euclidean plane, this set contains a point of
$\QQ^2$. Hence every nonempty slotted-open set meets $\QQ^2$.

:::

:::

::: {.pf-step #s1-8}

The slotted plane is not first countable.


::: pf-proof

Fix a point $x$ and suppose
\[
U_1,U_2,\dots
\]
were a countable local base at $x$. For each $n$, choose a basic slotted
neighborhood
\[
B_n=B(x;D_n;L_{n,1},\dots,L_{n,k_n})\subseteq U_n.
\]
Only countably many lines through $x$ occur among all the finite lists
$L_{n,j}$. There are uncountably many lines through $x$, so choose a line
$L$ through $x$ that occurs in none of those lists.

The set
\[
V=\{x\}\cup(\RR^2\setminus L)
\]
is slotted-open: at $x$ one slots out $L$, while at any point off $L$ an
ordinary disk disjoint from $L$ suffices. Thus $V$ is a neighborhood of $x$.
If the $U_n$ formed a local base, some $U_n$ would satisfy $U_n\subseteq V$.
But $L$ is not among the lines removed from $B_n$, so $B_n$ contains points of
$L$ other than $x$. Hence
\[
B_n\not\subseteq V.
\]
Since $B_n\subseteq U_n$, this contradicts $U_n\subseteq V$. Therefore no
countable local base exists at $x$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} prove part 1, steps [](#s1-3){.pf-ref} through [](#s1-6){.pf-ref} prove part 2, and
steps [](#s1-7){.pf-ref} and [](#s1-8){.pf-ref} prove part 3.

:::

:::

:::
