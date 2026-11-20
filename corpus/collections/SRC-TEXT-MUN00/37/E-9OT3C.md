---
schema: qual/card@1
id: E-9OT3C
kind: problem
title: Quasicomponents equal components in compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof has been checked line by
    line against the book and the search is recorded in the COMPLAINTS.md entry for §37--§42 of
    SRC-TEXT-MUN00. Searched: Aleksey Zinger, "MAT 530" Problem Sets 2-9 (Chapter 5 and 6 items: p235 #1,
    p236 #5, p260 #2, p260 #7 only); "Solutions to exercises in Munkres", file S38.pdf (Exercise 38.4
    onwards, so nothing in §37); "Solutions to exercises for Mathematics 205A" (UC Riverside, Fall 2014),
    section VI.4; Orellana (§37 selection), Doug's World (Chapter 4), Whitman (to §22), "positron0802"
    (Chapters 2 and 3), "shenapse" (§1--§11), "9beach" (§1--§4), "kyp44" (§1--§22); and the dbFin pages,
    which have no chapter-5 or chapter-6 section; Engelking's General Topology, which proves the theorem,
    is not among the retained files. Checked against Munkres, Topology (2000), Section 37 Exercise 4 and
    its printed Theorem, printed p. 236, with Theorem 26.2 (a closed subspace of a compact space is
    compact), the finite intersection property of closed subsets of a compact space (Theorem 26.9), and
    Theorem 32.3 or Theorem 26.3 (compact Hausdorff spaces are normal). The steps that carry the argument
    are: (a) normality separates the two closed pieces of a putative separation of the intersection, and
    compactness makes one chain member miss their union; (c) the smaller closed set inherits the
    quasicomponent relation because a separation of it would combine with the discarded piece to separate
    x from y in D. No correction was needed.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    All twenty-one steps of parts (a)--(c) asserted their claim with no proof body; each now
    carries a `pf-proof` deriving it from the preceding steps, and step 1.1 now says why the
    intersection of the chain is a set. The derivations use Munkres Theorem 26.2 (a closed
    subspace of a compact space is compact), Theorem 26.9 (the finite intersection property),
    Theorem 32.3 (compact Hausdorff spaces are normal), Zorn's lemma of §11 and Theorem 25.1
    (each connected subspace lies in one component). No claim was changed and the statement stands
    as printed. Checked: the three parts at the printed exercise, p. 236, with the cited theorems.
    Not checked: any published solution, none having been located; the search is recorded in the
    COMPLAINTS.md entry for §37--§42.
---

::: {.exercise}

Here is another theorem whose proof uses Zorn's lemma.
Recall that if $A$ is a space and if $x, y \in A$, we say that $x$ and $y$ belong to the same quasicomponent of $A$ if there is no separation $A = C \cup D$ of $A$ into two disjoint sets open in $A$ such that $x \in C$ and $y \in D$.

Theorem.
Let $X$ be a compact Hausdorff space.
Then $x$ and $y$ belong to the same quasicomponent of $X$ if and only if they belong to the same component of $X$.

(a) Let $\mathcal{A}$ be the collection of all closed subspaces $A$ of $X$ such that $x$ and $y$ lie in the same quasicomponent of $A$.
Let $\mathcal{B}$ be a subcollection of $\mathcal{A}$ that is simply ordered by proper inclusion.
Show that the intersection of the elements of $\mathcal{B}$ belongs to $\mathcal{A}$.
[Hint: Compare Exercise 11 of §26.]

(b) Show $\mathcal{A}$ has a minimal element $D$.

(c) Show $D$ is connected.
:::

::: {.solution}

A connected subset lies in a single quasicomponent: a separation that put two of its points on opposite sides would cut it. For the converse, fix $x,y$ in the same quasicomponent of $X$ and let $\mathcal{A}$ be the collection of closed subspaces $A\subseteq X$ in which $x$ and $y$ lie in the same quasicomponent.

::: pf

::: pf-step

Part (a): every chain in $\mathcal{A}$ has a lower bound in $\mathcal{A}$.

::: pf-proof

Let $\mathcal{B}\subseteq\mathcal{A}$ be a chain and $B_\infty=\bigcap_{B\in\mathcal{B}}B$. Steps 1.1--1.9 show $B_\infty\in\mathcal{A}$: a separation of $B_\infty$ would have its two closed pieces separated by disjoint open sets $U,V$ (1.5), compactness would place one member $B_0$ of the chain inside $U\cup V$ (1.6--1.7), and the two open sets would then separate $B_0$, contradicting $B_0\in\mathcal{A}$ (1.8).

::: pf-step

Let $\mathcal{B} \subseteq \mathcal{A}$ be a chain ordered by inclusion, and let $B_\infty = \bigcap_{B \in \mathcal{B}} B$.

::: pf-proof

Since $X\in\mathcal{A}$ (step 2.1) the chain may be taken nonempty, and then $B_\infty\subseteq B\subseteq X$ for any $B\in\mathcal{B}$; so $B_\infty$ is a well-defined subset of $X$.

:::

:::

::: pf-step

As an intersection of closed subsets containing $\{x, y\}$, $B_\infty$ is a closed (hence compact) subspace of $X$ containing $x$ and $y$.

::: pf-proof

Each $B\in\mathcal{B}\subseteq\mathcal{A}$ is closed in $X$ and contains $x$ and $y$. An intersection of closed sets is closed, and $x$ and $y$ lie in every member, hence in $B_\infty$. A closed subspace of the compact space $X$ is compact (Theorem 26.2).

:::

:::

::: pf-step

Suppose for contradiction that $x$ and $y$ do not belong to the same quasicomponent of $B_\infty$.

::: pf-proof

This is the assumption to be refuted: steps 1.4--1.8 derive a contradiction from it, and step 1.9 concludes its negation. By the definition in the statement, the assumption says that $B_\infty$ admits a separation putting $x$ and $y$ on opposite sides; step 1.4 names that separation.

:::

:::

::: pf-step

Then there exists a separation $B_\infty = C \cup D$, where $C, D$ are disjoint closed subsets of $B_\infty$ with $x \in C$ and $y \in D$.

::: pf-proof

By the definition of quasicomponent there are disjoint sets $C$ and $D$, open in $B_\infty$ and covering it, with $x\in C$ and $y\in D$. In a separation each piece is the complement of the other in $B_\infty$, so each is also closed in $B_\infty$ (Munkres, §23).

:::

:::

::: pf-step

Since $B_\infty$ is closed in the normal space $X$, $C$ and $D$ are disjoint closed subsets of $X$. By normality, choose disjoint open sets $U, V \subset X$ with $C \subseteq U$ and $D \subseteq V$.

::: pf-proof

$C$ and $D$ are closed in $B_\infty$ by step 1.4 and $B_\infty$ is closed in $X$ by step 1.2, so both are closed in $X$. A compact Hausdorff space is normal (Theorem 32.3), so the disjoint closed sets $C$ and $D$ have disjoint open neighbourhoods $U\supseteq C$ and $V\supseteq D$.

:::

:::

::: pf-step

Then $B_\infty \subseteq U \cup V$, so $\bigcap_{B \in \mathcal{B}} (B \setminus (U \cup V)) = \varnothing$.

::: pf-proof

$B_\infty=C\cup D\subseteq U\cup V$ by steps 1.4 and 1.5. A point of the intersection lies in $B\setminus(U\cup V)$ for every $B\in\mathcal{B}$, hence lies in $B_\infty$ and outside $U\cup V$, which is impossible; so the intersection is empty.

:::

:::

::: pf-step

By the Finite Intersection Property of compact closed sets in $X$, there exists $B_0 \in \mathcal{B}$ such that $B_0 \subseteq U \cup V$.

::: pf-proof

Each $B\setminus(U\cup V)$ is closed in $X$, because $B$ is closed and $U\cup V$ is open, and $X$ is compact. By step 1.6 the family $\{B\setminus(U\cup V):B\in\mathcal{B}\}$ has empty intersection, so by the finite intersection property (Theorem 26.9) finitely many of its members already have empty intersection: $(B_1\setminus(U\cup V))\cap\cdots\cap(B_n\setminus(U\cup V))=\varnothing$. The members of $\mathcal{B}$ are simply ordered by inclusion, so one of $B_1,\dots,B_n$, say $B_0$, is contained in all the others; then $B_0\setminus(U\cup V)$ is contained in that empty intersection, hence is empty, that is $B_0\subseteq U\cup V$.

:::

:::

::: pf-step

Then $B_0 \cap U$ and $B_0 \cap V$ form a separation of $B_0$ into disjoint open sets with $x \in B_0 \cap U$ and $y \in B_0 \cap V$, contradicting $B_0 \in \mathcal{A}$.

::: pf-proof

$B_0\subseteq U\cup V$ by step 1.7 and $U\cap V=\varnothing$ by step 1.5, so $B_0\cap U$ and $B_0\cap V$ are disjoint, open in $B_0$ and cover $B_0$. Both are nonempty: $x\in B_0$ because $B_0\in\mathcal{B}\subseteq\mathcal{A}$, and $x\in C\subseteq U$ by steps 1.4 and 1.5; likewise $y\in B_0\cap V$. So $B_0=(B_0\cap U)\cup(B_0\cap V)$ is a separation of $B_0$ with $x$ and $y$ on opposite sides, which is exactly what $B_0\in\mathcal{A}$ forbids.

:::

:::

::: pf-step

Hence $x$ and $y$ lie in the same quasicomponent of $B_\infty$, so $B_\infty \in \mathcal{A}$.

::: pf-proof

The assumption of step 1.3 led to the contradiction of step 1.8, so no separation of $B_\infty$ puts $x$ and $y$ on opposite sides; that is, they lie in the same quasicomponent of $B_\infty$. And $B_\infty$ is closed in $X$ by step 1.2, so $B_\infty\in\mathcal{A}$.

:::

:::

:::

:::

::: pf-step

Part (b): the existence of a minimal element $D \in \mathcal{A}$.

::: pf-proof

Steps 2.1--2.4 apply Zorn's lemma to $\mathcal{A}$ ordered by reverse inclusion: the collection is nonempty (2.1), that order is a partial order (2.2), every chain has an upper bound (2.3), and a maximal element for reverse inclusion is a minimal element for inclusion (2.4).

::: pf-step

The collection $\mathcal{A}$ is non-empty because $X$ is closed and $x, y$ are in the same quasicomponent of $X$.

::: pf-proof

$X$ is closed in $X$, and by hypothesis $x$ and $y$ lie in the same quasicomponent of $X$; so $X\in\mathcal{A}$.

:::

:::

::: pf-step

Order $\mathcal{A}$ by reverse inclusion ($A_1 \le A_2 \iff A_1 \supseteq A_2$).

::: pf-proof

Inclusion is a partial order on the subsets of $X$, and reversing it preserves the three axioms: $A\supseteq A$; $A\supseteq A'$ and $A'\supseteq A$ give $A=A'$; $A\supseteq A'$ and $A'\supseteq A''$ give $A\supseteq A''$.

:::

:::

::: pf-step

By Part (a), every chain in $\mathcal{A}$ has an upper bound under this ordering (its intersection).

::: pf-proof

Let $\mathcal{B}\subseteq\mathcal{A}$ be a chain for the reverse order; the same pairs are comparable for inclusion, so by step 1.9 its intersection $B_\infty$ lies in $\mathcal{A}$. And $B_\infty\subseteq B$ for every $B\in\mathcal{B}$, that is $B\le B_\infty$ in the reverse order, so $B_\infty$ is an upper bound.

:::

:::

::: pf-step

By Zorn's Lemma, $\mathcal{A}$ contains a maximal element with respect to reverse inclusion, which is a minimal element $D \in \mathcal{A}$ with respect to inclusion.

::: pf-proof

$\mathcal{A}$ is nonempty by step 2.1 and every chain in it has an upper bound by step 2.3, so Zorn's lemma (Munkres, §11) gives an element $D\in\mathcal{A}$ maximal for reverse inclusion. If $A\in\mathcal{A}$ and $A\subseteq D$, then $D\le A$ in that order, hence $A=D$; so $D$ is minimal for inclusion.

:::

:::

:::

:::

::: pf-step

Part (c): $D$ is connected, and the two notions agree.

::: pf-proof

Steps 3.1--3.7 refute the assumption that $D$ is disconnected: a separation $D=C_1\cup D_1$ with $x$ and $y$ both in $C_1$ (3.2) makes $C_1$ a strictly smaller member of $\mathcal{A}$ (3.3--3.5), contradicting minimality (3.6). Step 3.8 then places $x$ and $y$ in one component, which is contained in every quasicomponent holding them.

::: pf-step

Suppose for contradiction that $D$ is disconnected, so $D = C_1 \cup D_1$ is a separation of $D$ into disjoint, non-empty closed sets.

::: pf-proof

A disconnected space admits a separation: disjoint nonempty sets $C_1$, $D_1$, open in $D$, whose union is $D$. Each piece is the complement of the other, hence is also closed in $D$.

:::

:::

::: pf-step

Since $x$ and $y$ are in the same quasicomponent of $D$, they cannot be separated by this clopen partition; hence both $x, y \in C_1$ (without loss of generality).

::: pf-proof

$x$ and $y$ lie in $D$ because $D\in\mathcal{A}$. Were they in different pieces, $D=C_1\cup D_1$ would be a separation of $D$ with $x$ and $y$ on opposite sides, which $D\in\mathcal{A}$ forbids. So both lie in one piece, and that piece may be named $C_1$.

:::

:::

::: pf-step

$C_1$ is a closed subset of $D$ (hence of $X$). Because $D_1 \neq \varnothing$, $C_1 \subsetneq D$ is a strictly smaller closed subset.

::: pf-proof

$C_1$ is closed in $D$ by step 3.1, and $D$ is closed in $X$ because $D\in\mathcal{A}$, so $C_1$ is closed in $X$. Since $D_1$ is nonempty and $C_1\cap D_1=\varnothing$, $C_1\ne D$.

:::

:::

::: pf-step

If $x$ and $y$ were separated in $C_1$ by $C_1 = E \cup F$, then $D = E \cup (F \cup D_1)$ would be a separation of $D$ separating $x$ and $y$, contradicting $D \in \mathcal{A}$.

::: pf-proof

$E$ and $F$ are open in $C_1$, and $C_1$ is open in $D$ because it is the complement in $D$ of the open set $D_1$; so $E$ and $F$, and hence also $F\cup D_1$, are open in $D$. $E$ is disjoint from $F$ and from $D_1$, so $E\cap(F\cup D_1)=\varnothing$, and both parts are nonempty, $E$ and $F$ because they are the pieces of a separation of $C_1$, and $D_1$ by step 3.1. Thus $D=E\cup(F\cup D_1)$ is a separation of $D$ with $x\in E$ and $y\in F\cup D_1$, contrary to $D\in\mathcal{A}$.

:::

:::

::: pf-step

Thus $x, y$ lie in the same quasicomponent of $C_1$, which implies $C_1 \in \mathcal{A}$.

::: pf-proof

A separation of $C_1$ putting $x$ and $y$ on opposite sides would, by step 3.4, give a separation of $D$ doing the same, which $D\in\mathcal{A}$ forbids. So $x$ and $y$ lie in the same quasicomponent of $C_1$. And $C_1$ is closed in $X$ by step 3.3, so $C_1\in\mathcal{A}$.

:::

:::

::: pf-step

This contradicts the minimality of $D$ in $\mathcal{A}$.

::: pf-proof

$C_1\in\mathcal{A}$ by step 3.5 and $C_1\subsetneq D$ by step 3.3, whereas $D$ is minimal for inclusion among the members of $\mathcal{A}$ by step 2.4.

:::

:::

::: pf-step

Therefore $D$ is connected.

::: pf-proof

The assumption of step 3.1 is refuted: $D$ admits no separation, so $D$ is connected (Munkres, §23).

:::

:::

::: pf-step

Since $D$ is a connected subspace containing both $x$ and $y$, $x$ and $y$ belong to the same connected component of $X$.

::: pf-proof

$D$ is connected by step 3.7 and contains $x$ and $y$ because $D\in\mathcal{A}$. The components of a space are its maximal connected subspaces, and each connected subspace lies in one component (Theorem 25.1); so $D$, and with it both points, lies in one component of $X$. A component is connected and so lies in a single quasicomponent, namely the one holding $x$ and $y$; hence the two notions select the same pair.

:::

:::

:::

:::

:::
:::