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
---

::: {.exercise}

Let $X$ be a regular space.

(a) If $X$ is a finite union of closed paracompact subspaces of $X$, then $X$ is paracompact.

(b) If $X$ is a countable union of closed paracompact subspaces whose interiors cover $X$, show $X$ is paracompact.
:::

::: {.solution}
We use the closed-refinement characterization: a regular space is paracompact iff every open cover has a locally finite closed refinement covering the space.

(a) Suppose
$$
X=A_1\cup\cdots\cup A_m
$$
with each $A_i$ closed and paracompact. Let $\mathcal U$ be an open cover of $X$. Its restriction to $A_i$ has a locally finite closed refinement $\mathcal F_i$ covering $A_i$. Because $A_i$ is closed in $X$, every member of $\mathcal F_i$ is closed in $X$, and a family that is locally finite in $A_i$ is locally finite in $X$: for $x\in A_i$ the open set $W$ that local finiteness provides inside $A_i$ contains $x$ and meets the same members, since every member of $\mathcal F_i$ lies in $A_i$, and for $x\notin A_i$ the set $X-A_i$ is an open neighbourhood of $x$ meeting none of them. A finite union of locally finite families is locally finite, so
$$
\mathcal F_1\cup\cdots\cup\mathcal F_m
$$
is a locally finite closed refinement of $\mathcal U$ covering $X$. Thus $X$ is paracompact.

(b) Suppose
$$
X=\bigcup_{n\ge1}A_n
$$
where each $A_n$ is closed and paracompact and the interiors $A_n^\circ$ cover $X$. Define
$$
C_n=A_n-\bigcup_{i<n}A_i^\circ.
$$
Each $C_n$ is closed in $X$, is a closed subspace of the paracompact space $A_n$, hence is paracompact, and the $C_n$'s cover $X$. They are locally finite: if $x\in A_m^\circ$, then the neighborhood $A_m^\circ$ misses $C_n$ for every $n>m$.

Let $\mathcal U$ be an open cover of $X$. For each $n$, choose a locally finite closed refinement $\mathcal F_n$ of the restricted cover on $C_n$, covering $C_n$. Since $C_n$ is closed in $X$, all members of $\mathcal F_n$ are closed in $X$, and each $\mathcal F_n$ is locally finite in $X$ by the argument of part (a) applied to the closed subspace $C_n$. The union
$$
\mathcal F=\bigcup_{n\ge1}\mathcal F_n
$$
is locally finite: near a fixed point only finitely many $C_n$'s occur, and within each of those finitely many $C_n$'s the corresponding family $\mathcal F_n$ is locally finite. Thus $\mathcal F$ is a locally finite closed refinement of $\mathcal U$ covering $X$. Hence $X$ is paracompact.
:::
