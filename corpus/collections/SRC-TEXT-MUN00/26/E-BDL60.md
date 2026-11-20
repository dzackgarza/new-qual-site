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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked (a) the finite subcover extracted from one open
    set and the finitely many points outside it, through Lemma 26.1; (b) the increasing open
    cover A_n = [0,1] - {1/k : k >= n} of the cocountable subspace and the failure of every
    finite subcollection at the point 1/N. Label repaired: part (b) concerns the cocountable
    topology, which the earlier prose called the finite complement topology. positron0802,
    Chapter 3 Exercise 26.2, PDF p. 12.
---

::: {.exercise}

(a) Show that in the finite complement topology on $\RR$, every subspace is compact.

(b) If $\RR$ has the topology consisting of all sets $A$ such that $\RR - A$ is either countable or all of $\RR$, is $[0, 1]$ a compact subspace?
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both parts are theirs, and the label of part (b) is corrected below: the topology with countable complements is the cocountable topology, not the finite complement topology.

::: pf

::: {.pf-step #part-a}
(a) In the finite complement topology on $\RR$, every subspace is compact.

::: pf-proof
Let $B$ be a subspace and $\mathcal{A}$ a cover of $B$ by open sets of $\RR$; it suffices by Lemma 26.1 to extract a finite subcollection covering $B$. Fix $A_{0}\in\mathcal{A}$, nonempty because it covers some point. Its complement $\RR-A_{0}$ is finite, say $\{c_{1},\dots,c_{n}\}$. For each $c_{i}$ that lies in $B$ choose $A_{i}\in\mathcal{A}$ with $c_{i}\in A_{i}$, and let $I$ be the set of such $i$. Then every point of $B$ lies in $A_{0}$ or is one of the $c_{i}$ with $i\in I$, so $\{A_{0}\}\cup\{A_{i}\mid i\in I\}$ is a finite subcollection of $\mathcal{A}$ covering $B$.
:::

:::

::: {.pf-step #part-b}
(b) If $\RR$ carries the cocountable topology, whose open sets are $\varnothing$ and the sets with countable complement, then $[0,1]$ is not compact.

:::: pf-proof

::: {.pf-step #b-cover}
With $B_{n}=\{1/k\mid k\ge n\}$ and $A_{n}=[0,1]-B_{n}$, the sets $A_{n}$ are open in the subspace $[0,1]$, increase with $n$, and cover $[0,1]$.

::: pf-proof
$B_{n}$ is countable, so $\RR-B_{n}$ is cocountable, hence open in $\RR$, and $A_{n}=[0,1]\cap(\RR-B_{n})$ is open in the subspace. Clearly $B_{n+1}\subset B_{n}$, so $A_{n}\subset A_{n+1}$. If $x\in[0,1]$ then either $x=0$, which lies in every $A_{n}$, or $x=1/k$ for exactly one $k$, which lies in $A_{n}$ for $n>k$, or $x$ is of neither form, in which case $x\notin B_{n}$ for every $n$ and $x$ lies in every $A_{n}$.
:::

:::

::: {.pf-step #b-no-subcover}
No finite subcollection of $\{A_{n}\}$ covers $[0,1]$.

::: pf-proof
A finite subcollection has a largest index $N$. Since $1/N\in B_{N}$, the point $1/N$ is not in $A_{N}$, and by monotonicity it is in no $A_{n}$ with $n\le N$; so $1/N\in[0,1]$ is in no member of the subcollection.
:::

:::

::: {.pf-step}
(b) holds.

::: pf-proof
Steps [](#b-cover){.pf-ref} and [](#b-no-subcover){.pf-ref} exhibit an open cover of $[0,1]$ with no finite subcover, so $[0,1]$ is not compact in the cocountable topology.
:::

:::

:::

:::

::: {.pf-step}
Both parts hold.

::: pf-proof
Steps [](#part-a){.pf-ref} and [](#part-b){.pf-ref} are the two assertions.
:::

:::

:::
:::
