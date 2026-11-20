---
schema: qual/card@1
id: E-S4J3T
kind: problem
title: Unions of closed paracompact subspaces
classification:
  areas:
  - topology
  topics:
  - Paracompactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Aleksey Zinger, "MAT 530: Topology & Geometry, I",
    Fall 2005, Problem Set 6, "Solution to Problem p260, #7", PDF pp. 2-3
    (tmp/sources/munkres-solutions-zinger-mat530-ps6.pdf; the sheet has no printed page numbers, so the
    PDF page is the locator). Checked against Munkres, Topology (2000), Section 41 Exercise 7, printed
    p. 260, with Lemma 41.3 (the equivalence of its conditions (1), (2), (3) and (4) for a regular space)
    and Theorem 41.2 (a closed subspace of a paracompact space is paracompact). What was corrected: the
    *published* posts on this exercise ("Praying For Stockholm", "Unions of Paracompact Spaces (6.41.7)",
    30 December 2014) refine inside the closed subspaces and then call the union a locally finite open
    refinement of X, although a set open in K_i need not be open in X; the card follows Zinger, who
    derives local finiteness in X explicitly (for x outside B the set X - B, for x in B the same open set
    W that witnesses local finiteness in B, since every member lies in B) and applies Lemma 41.3. In part
    (b) the card keeps Zinger's C_n = A_n - union of the earlier interiors in place of the post's
    intersection with int K_n, and states the passage from local finiteness in each C_n to local
    finiteness in X that both sources leave implicit.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf` with
    nine steps covering both parts, each carrying a `pf-proof`. Cited by number only: Munkres,
    Topology, §41 Exercise 7, Lemma 41.3 (condition (3), a locally finite closed covering refinement)
    and Theorem 41.2 (a closed subspace of a paracompact space is paracompact). The transcription is
    from Aleksey Zinger, MAT 530: Topology & Geometry I, Problem Set 6, Solution to Problem 7, and the
    two passages it leaves to the reader are written out: local finiteness in a closed subspace passes
    to the ambient space, and local finiteness in each C_n passes to the union. Checked: that the
    traces of an open cover on a closed subspace are an open cover of it, that C_n is closed in X, that
    the least m with x in the interior of A_m puts x in C_m, and that a neighbourhood meeting only
    finitely many C_n meets only finitely many members of the corresponding families.
---

::: {.exercise}

Let $X$ be a regular space.

(a) If $X$ is a finite union of closed paracompact subspaces of $X$, then $X$ is paracompact.

(b) If $X$ is a countable union of closed paracompact subspaces whose interiors cover $X$, show $X$ is paracompact.
:::

::: {.solution}

The argument is Aleksey Zinger's, *MAT 530: Topology & Geometry, I*, Problem Set 6, Solution to Problem 7, read in the retained text `tmp/sources/munkres-solutions-zinger-mat530-ps6.pdf`. Two passages Zinger leaves to the reader are written out here: that local finiteness in a closed subspace passes to the ambient space (steps [](#part-a-closed){.pf-ref} and [](#part-b-refinements){.pf-ref}), and that local finiteness in each $C_n$ passes to their union (step [](#part-b-union){.pf-ref}).

::: pf

::: {.pf-step #criterion}
A regular space is paracompact if and only if every open cover of it has a refinement that is a locally finite closed covering.

::: pf-proof
This is condition (3) of Munkres, Lemma 41.3, which states the equivalence of conditions (1)--(4) for a regular space.
:::

:::

::: {.pf-step #part-a-refinement}
(a) Let $X=A_1\cup\cdots\cup A_m$ with each $A_i$ closed and paracompact, and let $\mathcal U$ be an open cover of $X$. For each $i$ the family $\{U\cap A_i:U\in\mathcal U\}$ is an open cover of $A_i$ and has a refinement $\mathcal F_i$ that is a locally finite closed covering of $A_i$.

::: pf-proof
$\mathcal U$ covers $X$, so its traces on $A_i$ cover $A_i$, and they are open in the subspace $A_i$. Since $A_i$ is paracompact and regular, condition (3) of Lemma 41.3 applied in the space $A_i$ supplies $\mathcal F_i$.
:::

:::

::: {.pf-step #part-a-closed}
Each $\mathcal F_i$ is a locally finite family of closed subsets of $X$.

::: pf-proof
A member of $\mathcal F_i$ is closed in $A_i$, and $A_i$ is closed in $X$, so it is closed in $X$. For local finiteness let $x\in X$. If $x\in A_i$, local finiteness of $\mathcal F_i$ in $A_i$ gives an open set $W$ of $A_i$ containing $x$ and meeting only finitely many members of $\mathcal F_i$; write $W=O\cap A_i$ with $O$ open in $X$. Every member of $\mathcal F_i$ lies in $A_i$, so $O$ meets exactly the members that $W$ meets, finitely many. If $x\notin A_i$, then $X-A_i$ is an open neighbourhood of $x$ meeting none of them.
:::

:::

::: {.pf-step #part-a-union}
$\mathcal F=\mathcal F_1\cup\cdots\cup\mathcal F_m$ is a refinement of $\mathcal U$ that is a locally finite closed covering of $X$.

::: pf-proof
A finite union of families that are locally finite at a point is locally finite at that point, by intersecting the finitely many neighbourhoods the families provide. Each member of $\mathcal F_i$ is closed in $X$ by step [](#part-a-closed){.pf-ref}, and it lies in some member of $\mathcal U$ because $\mathcal F_i$ refines $\mathcal U$ in $A_i$. The union covers $X$ because $\bigcup_iA_i=X$ and $\mathcal F_i$ covers $A_i$.
:::

:::

::: {.pf-step #part-a-done}
(a) $X$ is paracompact.

::: pf-proof
Given an open cover $\mathcal U$, step [](#part-a-union){.pf-ref} produces a refinement that is a locally finite closed covering, so condition (3) of Lemma 41.3 holds; $X$ is regular by hypothesis, hence paracompact.
:::

:::

::: {.pf-step #part-b-sets}
(b) Let $X=\bigcup_{n\ge1}A_n$ with each $A_n$ closed and paracompact and the interiors $A_n^\circ$ covering $X$, and put $C_n=A_n-\bigcup_{i<n}A_i^\circ$. Then each $C_n$ is a closed paracompact subspace of $X$, the family $\{C_n\}$ covers $X$, and it is locally finite.

::: pf-proof
The set $C_n$ is $A_n$ minus an open set, hence closed in $X$, and as a closed subspace of the paracompact space $A_n$ it is paracompact by Munkres, Theorem 41.2. For the cover let $x\in X$ and let $m$ be the least index with $x\in A_m^\circ$; then $x\notin A_i^\circ$ for every $i<m$, so $x\notin\bigcup_{i<m}A_i^\circ$, while $x\in A_m$, so $x\in C_m$. For local finiteness, $A_m^\circ$ is a neighbourhood of $x$, and for $n>m$ the set $A_m^\circ$ is among the sets subtracted in $C_n=A_n-\bigcup_{i<n}A_i^\circ$, so $C_n\cap A_m^\circ=\varnothing$.
:::

:::

::: {.pf-step #part-b-refinements}
For each $n$ the traces $\{U\cap C_n:U\in\mathcal U\}$ form an open cover of $C_n$ having a refinement $\mathcal F_n$ that is a locally finite closed covering of $C_n$, and $\mathcal F_n$ is a locally finite family of closed subsets of $X$.

::: pf-proof
The traces cover $C_n$ and are open in the subspace $C_n$, which is paracompact by step [](#part-b-sets){.pf-ref}; condition (3) of Lemma 41.3 applied in $C_n$ supplies $\mathcal F_n$. A member of $\mathcal F_n$ is closed in $C_n$ and $C_n$ is closed in $X$, so it is closed in $X$, and local finiteness passes from $C_n$ to $X$ by the argument of step [](#part-a-closed){.pf-ref} with $C_n$ in place of $A_i$.
:::

:::

::: {.pf-step #part-b-union}
$\mathcal F=\bigcup_{n\ge1}\mathcal F_n$ is a refinement of $\mathcal U$ that is a locally finite closed covering of $X$.

::: pf-proof
Let $x\in X$ and choose $m$ with $x\in A_m^\circ$, as step [](#part-b-sets){.pf-ref} allows. The open set $A_m^\circ$ meets $C_n$ only for $n\le m$, so it meets a member of $\mathcal F_n$ only for $n\le m$. For each of the finitely many $n\le m$, local finiteness of $\mathcal F_n$ at $x$ gives an open neighbourhood $O_n$ of $x$ meeting only finitely many members of $\mathcal F_n$; then $A_m^\circ\cap\bigcap_{n\le m}O_n$ is an open neighbourhood of $x$ meeting only finitely many members of $\mathcal F$. Each member of $\mathcal F$ is closed in $X$ by step [](#part-b-refinements){.pf-ref}, and it lies in some member of $\mathcal U$ because its own family refines $\mathcal U$ on $C_n$. The union covers $X$ because $\bigcup_nC_n=X$ and $\mathcal F_n$ covers $C_n$.
:::

:::

::: {.pf-step #part-b-done}
(b) $X$ is paracompact.

::: pf-proof
Given an open cover $\mathcal U$, step [](#part-b-union){.pf-ref} produces a refinement that is a locally finite closed covering, so condition (3) of Lemma 41.3 holds; $X$ is regular by hypothesis, hence paracompact.
:::

:::

:::

:::
