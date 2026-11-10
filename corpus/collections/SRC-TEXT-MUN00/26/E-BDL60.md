---
schema: qual/card@1
id: E-BDL60
kind: problem
title: Compact subspaces in the finite complement and countable complement topologies
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 2, printed p. 171, with Lemma 26.1
    and the finite complement topology of §12; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.2, PDF p. 12. In the finite complement topology
    one member of a cover misses finitely many points, each of which needs one more member;
    and the increasing cover by [0,1] minus the tails of 1/n has no finite subcover.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

(a) Show that in the finite complement topology on $\RR$, every subspace is compact.

(b) If $\RR$ has the topology consisting of all sets $A$ such that $\RR - A$ is either countable or all of $\RR$, is $[0, 1]$ a compact subspace?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.2, PDF p. 12** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both parts are theirs.

(a) Let $B$ be a subspace of $\RR$ in the finite complement topology and let $\mathcal{A}$ be a cover of $B$ by open sets of $\RR$. Fix $A_{0}\in\mathcal{A}$; its complement is finite, say $\{c_{1},\dots,c_{n}\}$. For each $c_{i}\in B$ choose $A_{i}\in\mathcal{A}$ containing $c_{i}$. Then $A_{0},A_{1},\dots,A_{n}$ is a finite subcollection covering $B$. By Lemma 26.1, $B$ is compact. As $B$ was arbitrary, every subspace is compact.

(b) $[0,1]$ is **not** compact in the finite complement topology inherited from $\RR$. Put $B_{n}=\{1/k\mid k\ge n\}$ and $A_{n}=[0,1]-B_{n}$, which is open in the subspace since $B_{n}$ is finite; the $A_{n}$ increase and cover $[0,1]$, because a point $1/k$ lies in $A_{n}$ once $n>k$ and $0$ lies in every $A_{n}$. A finite subcollection has a largest index $N$, and $1/N\notin A_{N}$, so $1/N$ is in no member of the subcollection: no finite subcover exists.
:::
