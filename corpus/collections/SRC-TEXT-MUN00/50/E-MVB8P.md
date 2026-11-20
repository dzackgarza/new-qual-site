---
schema: qual/card@1
id: E-MVB8P
kind: problem
title: The dimension of a $\sigma$-compact Hausdorff space is bounded by that of its compact subspaces
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked line by line against Munkres, Topology (2000), §50 Exercise 8, printed p. 316, following the
    exercise's own outline. Points checked in (b): the integer r chosen least with x in the interior of X_r
    exists, x lies outside X_{r-2} because X_{r-2} is contained in the interior of X_{r-1}, and X_{r-2} is closed
    because compact in the Hausdorff space; then a member of B_0 meeting X_n has n at least r-1 and so lies in
    X_{n+1}. In (c) the covering C is built from a refinement of the trace on X_{n+1}, which exists because
    dim X_{n+1} is at most m, together with the pieces B - X_{n+1}; the order bound on X_{n+1} is the case split
    between points of X_n, where members of B_{n+1} lie in distinct members of B_n, and points of X_{n+1} - X_n,
    where no retained member can occur because it would have to lie in X_n. In (d) the cover consists of the sets
    that are eventually retained, and a member through a point of X_n must appear by stage n+1, so the order
    bound passes to the limit. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves Munkres §50 Exercise 8 (printed p. 316).
    Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, and the ten GitHub repositories of
    Munkres solutions listed in COMPLAINTS.md stop before §36. The AoPS post *Topology by Munkres Chapter 8 |
    Day 18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost, and
    the Stack Exchange queries of this pass, listed in the COMPLAINTS.md entry for §43--§50, returned no
    question on it. The exercise is an outline, and the part that carries its content is (d), where the sets
    $D(B)$ must be shown to be open and the family $\mathcal B_{n+1}$ to refine $\mathcal B_n$ and to have
    order at most $m+1$ at points of $X_{n+1}$ while its elements are unchanged off $X_{n-1}$; the card works
    through (a)--(d) in that form. Nothing needed correction.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose in four headed parts with no `pf` structure. It
    is now a `pf` with eight steps, each carrying a `pf-proof`, following the four steps the exercise
    prescribes. Cited by numbered statement only: Munkres, Topology, §50 Exercise 8, §26 Exercise 3 (a
    finite union of compact subspaces is compact) and the definition of topological dimension in §50.
    No retained published set answers the exercise, and the card's preamble says so and names the
    search record. Checked: that the exhaustion can be made increasing with each $X_n$ inside the
    interior of the next, that $B_x$ misses $X_{r-2}$ and therefore forces $n\ge r-1$ when $B_x$ meets
    $X_n$, that the property of $\mathcal B_0$ is inherited by every later family through refinement,
    that $\mathcal C$ covers $X$ by the two kinds of member, that distinct members of
    $\mathcal B_{n+1}$ at $x\in X_n$ have distinct $\mathcal B_n$-preimages, that no retained member
    meets $X_{n+1}-X_n$, and that a member of $\mathcal B$ through $x\in X_n$ already occurs in
    $\mathcal B_{n+1}$.
---

::: {.exercise}

Recall that $X$ is said to be $\sigma$-compact if there is a countable collection of compact subspaces of $X$ whose interiors cover $X$.

Theorem.
Let $X$ be a $\sigma$-compact Hausdorff space.
If every compact subspace of $X$ has topological dimension at most $m$, then so does $X$.

Let $\mathcal{A}$ be an open cover of $X$.
Find an open cover $\mathcal{B}$ of $X$ refining $\mathcal{A}$ that has order at most $m + 1$, as follows:

(a) Show that $X = \bigcup X_n$, where $X_n$ is compact and $X_n \subset \operatorname{Int} X_{n+1}$ for each $n$.
Let $X_0 = \varnothing$.

(b) Find an open covering $\mathcal{B}_0$ of $X$ refining $\mathcal{A}$ such that for each $n$, each element of $\mathcal{B}_0$ that intersects $X_n$ lies in $X_{n+1}$.

(c) Suppose $n \geq 0$ and $\mathcal{B}_n$ is an open covering of $X$ refining $\mathcal{B}_0$ such that $\mathcal{B}_n$ has order at most $m + 1$ at points of $X_n$.
Choose an open covering $\mathcal{C}$ of $X$ refining $\mathcal{B}_n$ that has order at most $m + 1$ at points of $X_{n+1}$.
Choose $f: \mathcal{C} \to \mathcal{B}_n$ so that $C \subset f(C)$.
For $B \in \mathcal{B}_n$, let $D(B)$ be the union of those $C$ for which $f(C) = B$.
Let $\mathcal{B}_{n+1}$ consist of all sets $B \in \mathcal{B}_n$ for which $B \cap X_{n-1} \neq \varnothing$, along with all sets $D(B)$ for which $B \in \mathcal{B}_n$ and $B \cap X_{n-1} = \varnothing$.
Show that $\mathcal{B}_{n+1}$ is an open covering of $X$ that refines $\mathcal{B}_n$ and has order at most $m + 1$ at points of $X_{n+1}$.

(d) Define $\mathcal{B}$ as follows.
Given a set $B$, it belongs to $\mathcal{B}$ if there is an $N$ such that $B \in \mathcal{B}_n$ for all $n \geq N$.
:::

::: {.solution}

No retained published solution of Munkres, *Topology*, §50 Exercise 8 was located: the sets searched are listed in the `COMPLAINTS.md` entry for §43--§50 of `SRC-TEXT-MUN00`, and the self-study notes that reach Chapter 7 state the exercise without answering it. The proof is the card's own, checked against the numbered statements it cites, and it follows the four steps the exercise prescribes.

::: pf

::: {.pf-step #exhaustion}
(a) There are compact $X_1\subseteq X_2\subseteq\cdots$ with $X_n\subseteq\operatorname{Int}X_{n+1}$ for every $n$ and $\bigcup_nX_n=X$; put $X_0=\varnothing$.

::: pf-proof
$\sigma$-compactness gives compact subspaces $K_1,K_2,\dots$ whose interiors cover $X$. Choose integers $1\le r_1<r_2<\cdots$ and put $X_n=K_1\cup\cdots\cup K_{r_n}$, a finite union of compact subspaces and hence compact (Munkres, §26 Exercise 3). Given $r_n$, the compact set $X_n$ is covered by the open family $\{\operatorname{Int}K_j\}_j$, so finitely many members cover it; taking $r_{n+1}$ above all their indices gives $X_n\subseteq\operatorname{Int}X_{n+1}$. Since $r_n\ge n$ one has $X_n\supseteq K_n$, so the $X_n$ cover $X$.
:::

:::

::: {.pf-step #base-cover}
(b) There is an open cover $\mathcal B_0$ refining $\mathcal A$ such that $B\cap X_n\ne\varnothing$ implies $B\subseteq X_{n+1}$ for every $B\in\mathcal B_0$ and every $n$, and every member of every later $\mathcal B_k$ inherits that property.

::: pf-proof
For $x\in X$ let $r\ge1$ be least with $x\in\operatorname{Int}X_r$; choose $A_x\in\mathcal A$ with $x\in A_x$ and an open $B_x$ with $x\in B_x\subseteq A_x\cap\operatorname{Int}X_r$, disjoint from $X_{r-2}$ (here $X_{-1}=X_0=\varnothing$). Put $\mathcal B_0=\{B_x:x\in X\}$; it is an open cover refining $\mathcal A$. If $B_x\cap X_n\ne\varnothing$ then $n\ge r-1$, since $B_x$ misses $X_{r-2}$ and the $X_k$ increase; hence $B_x\subseteq X_r\subseteq X_{n+1}$. Inheritance: a member of $\mathcal B_k$ lies in some member of $\mathcal B_0$ because $\mathcal B_k$ refines $\mathcal B_0$, and if it meets $X_n$ so does that member, which therefore lies in $X_{n+1}$.
:::

:::

::: {.pf-step #refine-next}
(c) If $\mathcal B_n$ is an open cover refining $\mathcal B_0$ with order at most $m+1$ at points of $X_n$, there is an open cover $\mathcal C$ of $X$ refining $\mathcal B_n$ with order at most $m+1$ at points of $X_{n+1}$.

::: pf-proof
$X_{n+1}$ is compact and $\dim X_{n+1}\le m$ by hypothesis, and the traces $\{B\cap X_{n+1}:B\in\mathcal B_n\}$ form an open cover of $X_{n+1}$; by the definition of dimension in Munkres §50 it has an open refinement $\mathcal V$ of order at most $m+1$. For $V\in\mathcal V$ choose $B_V\in\mathcal B_n$ with $V\subseteq B_V\cap X_{n+1}$ and an open $O_V\subseteq X$ with $O_V\cap X_{n+1}=V$. Let $\mathcal C$ consist of the sets $O_V\cap B_V$ for $V\in\mathcal V$ together with the sets $B-X_{n+1}$ for $B\in\mathcal B_n$. Each is open, each is contained in the member of $\mathcal B_n$ named in its definition, and $\mathcal C$ covers $X$: a point of $X_{n+1}$ lies in some $V$, hence in $O_V\cap B_V$, and a point outside $X_{n+1}$ lies in some $B-X_{n+1}$. The sets $B-X_{n+1}$ miss $X_{n+1}$, and the trace of $O_V\cap B_V$ on $X_{n+1}$ is $V$, so the order of $\mathcal C$ at a point of $X_{n+1}$ is that of $\mathcal V$, at most $m+1$.
:::

:::

::: {.pf-step #next-cover}
(c) With $f:\mathcal C\to\mathcal B_n$ chosen so that $C\subseteq f(C)$ and $D(B)=\bigcup\{C\in\mathcal C:f(C)=B\}$, the family
$$
\mathcal B_{n+1}=\{B\in\mathcal B_n:B\cap X_{n-1}\ne\varnothing\}\cup\{D(B):B\in\mathcal B_n,\ B\cap X_{n-1}=\varnothing\}
$$
is an open cover of $X$ refining $\mathcal B_n$.

::: pf-proof
Such an $f$ exists because $\mathcal C$ refines $\mathcal B_n$. Each $D(B)$ is a union of open sets and is contained in $B$, so it is open and lies in $B$; the retained members are themselves members of $\mathcal B_n$. So $\mathcal B_{n+1}$ is an open refinement of $\mathcal B_n$. It covers $X$: a point lying in a retained member is covered, and otherwise it lies in some $C\in\mathcal C$, hence in $D(f(C))$, which is a member of $\mathcal B_{n+1}$ unless $f(C)$ was retained, in which case the point is covered by that retained member.
:::

:::

::: {.pf-step #next-order}
(c) $\mathcal B_{n+1}$ has order at most $m+1$ at every point of $X_{n+1}$.

::: pf-proof
Let $x\in X_{n+1}$ and let $\mathcal M$ be the members of $\mathcal B_{n+1}$ containing $x$. If $x\in X_n$, map each member of $\mathcal M$ to a member of $\mathcal B_n$ containing $x$: a retained member to itself, and $D(B)$ to $B$. Distinct members have distinct images, because $D(B)\subseteq B$ and the retained members are distinct members of $\mathcal B_n$; since $\mathcal B_n$ has order at most $m+1$ at $x\in X_n$, $\abs{\mathcal M}\le m+1$. If $x\in X_{n+1}-X_n$, no retained member contains $x$: a retained member meets $X_{n-1}$ and therefore lies in $X_n$ by the inherited property of step [#base-cover]{.pf-ref}, and $x\notin X_n$. So every member of $\mathcal M$ is some $D(B)$; distinct such sets give distinct $C\in\mathcal C$ containing $x$ (choose $C$ with $f(C)=D(B)$'s indexing member and $x\in C$), and $\mathcal C$ has order at most $m+1$ at $x\in X_{n+1}$ by step [#refine-next]{.pf-ref}. Hence $\abs{\mathcal M}\le m+1$ in either case.
:::

:::

::: {.pf-step #family-covers}
(d) The family $\mathcal B$ of sets that belong to $\mathcal B_n$ for all sufficiently large $n$ is an open cover of $X$ refining $\mathcal A$.

::: pf-proof
Every member of $\mathcal B$ belongs to some $\mathcal B_n$, which refines $\mathcal B_0$, which refines $\mathcal A$; so $\mathcal B$ refines $\mathcal A$. For the cover let $x\in X$ and take $n$ with $x\in X_n$; step [#next-cover]{.pf-ref} gives $B\in\mathcal B_{n+1}$ with $x\in B$. For every $k\ge n+2$ the set $B$ meets $X_{k-1}$, because $x\in B\cap X_n$ and $X_n\subseteq X_{k-1}$, so $B$ is retained at stage $k$ and therefore belongs to $\mathcal B_k$. Hence $B\in\mathcal B_k$ for all $k\ge n+1$ and $B\in\mathcal B$.
:::

:::

::: {.pf-step #order-everywhere}
(d) $\mathcal B$ has order at most $m+1$.

::: pf-proof
Let $x\in X$ and take $n$ with $x\in X_n$. Every member of $\mathcal B$ containing $x$ already belongs to $\mathcal B_{n+1}$: such a set cannot be newly created as a $D(B)$ at any stage $k>n+1$, because its predecessor $B$ contains $x$, hence meets $X_n$, hence lies in $X_{n+1}$ by the inherited property of step [#base-cover]{.pf-ref} and is retained at stage $k=n+2$, and all later stages retain it in turn. So the members of $\mathcal B$ through $x$ are members of $\mathcal B_{n+1}$ through $x$, of which there are at most $m+1$ by step [#next-order]{.pf-ref} since $x\in X_n\subseteq X_{n+1}$.
:::

:::

::: {.pf-step #conclusion}
$\dim X\le m$.

::: pf-proof
Given the arbitrary open cover $\mathcal A$ of $X$, steps [#family-covers]{.pf-ref} and [#order-everywhere]{.pf-ref} produce an open refinement of order at most $m+1$. That is the definition of $\dim X\le m$ in Munkres §50, so the theorem holds.
:::

:::

:::

:::
