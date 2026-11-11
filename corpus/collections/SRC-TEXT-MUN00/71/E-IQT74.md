---
schema: qual/card@1
id: E-IQT74
kind: problem
title: When a union of circles meeting at a point is Hausdorff
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §71 Exercise 1, printed p. 438. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00, and Murayama's set, the one located set reaching
    §71, skips this exercise. Checked against Exercise 13 of §17 (printed p. 101, the diagonal is closed if and
    only if the space is Hausdorff), Theorem 17.8 and Theorem 17.11 (printed pp. 99--100), Theorem 26.3,
    Theorem 26.5 and Theorem 27.3 (printed pp. 165--173), and the definition of coherence (printed p. 435).
    Part (c) is written as a quotient, so that both the circle topologies and the failure of the Hausdorff
    condition are computed from the definition of the quotient topology rather than asserted.
---

::: {.exercise}

Let $X$ be a space that is the union of subspaces $S_1, \ldots, S_n$, each of which is homeomorphic to the unit circle.
Assume there is a point $p$ of $X$ such that $S_i \cap S_j = \theset{p}$ for $i \neq j$.

(a) Show that $X$ is Hausdorff if and only if each space $S_i$ is closed in $X$.

(b) Show that $X$ is Hausdorff if and only if the topology of $X$ is coherent with the subspaces $S_i$.

(c) Give an example to show that $X$ need not be Hausdorff.
[Hint: See [[E-29WP0]].]
:::

::: {.solution}

::: pf

::: pf-step

(a) If $X$ is Hausdorff, each $S_i$ is closed in $X$.

::: pf-proof

$S_i$ is compact: it is homeomorphic to $S^1$, which is a closed bounded subspace of $\RR^2$, hence compact by Theorem 27.3 (printed p. 173), and the continuous image of a compact space is compact (Theorem 26.5, printed p. 166). A compact subspace of a Hausdorff space is closed (Theorem 26.3, printed p. 165).

:::

:::

::: pf-step

(a) If each $S_i$ is closed in $X$, then $X$ is Hausdorff.

::: pf-proof

By Exercise 13 of §17 (printed p. 101) it suffices to show that the diagonal $\Delta=\theset{x\times x\mid x\in X}$ is closed in $X\times X$. Each $S_i\times S_i$ is closed in $X\times X$, and $\Delta_{S_i}=\Delta\cap(S_i\times S_i)$ is closed in $S_i\times S_i$ because $S_i$ is Hausdorff, being a subspace of the Hausdorff space $\RR^2$ (Theorem 17.11, printed p. 100), hence closed in $X\times X$. Finally $\Delta=\bigcup_i\Delta_{S_i}$: a point of $\Delta$ is $x\times x$, and $x$ lies in some $S_i$, so $x\times x\in\Delta_{S_i}$; the reverse inclusion is clear. A finite union of closed sets is closed.

:::

:::

::: pf-step

(b) If the $S_i$ are closed in $X$, the topology of $X$ is coherent with them.

::: pf-proof

Let $C\subseteq X$ with $C\cap S_i$ closed in $S_i$ for every $i$. Since $S_i$ is closed in $X$, $C\cap S_i$ is closed in $X$; and $C=\bigcup_i(C\cap S_i)$ is a finite union of closed sets, hence closed. So coherence holds, and with step 1 this gives Hausdorff from coherence's failure... see step 4.

:::

:::

::: pf-step

(b) If the topology is coherent with the $S_i$, then $X$ is Hausdorff.

::: pf-proof

Fix $i$ and consider $S_i\subseteq X$. For every $j$, $S_i\cap S_j$ equals $S_i$ if $j=i$ and $\theset{p}$ if $j\ne i$; both are closed in $S_j$, the second because a finite point set in the Hausdorff space $S_j$ is closed (Theorem 17.8, printed p. 99). By coherence $S_i$ is closed in $X$, for every $i$, and step 2 gives that $X$ is Hausdorff. Conversely, if $X$ is Hausdorff then the $S_i$ are closed by step 1 and the topology is coherent by step 3. This proves (b) in both directions.

:::

:::

::: pf-step

(c) A quotient of two circles that is not Hausdorff, with both circles closed copies of $S^1$.

::: pf-proof

Let $S_1,S_2$ be two circles with $S_1\cap S_2=\theset{p}$, choose $q_i\in S_i\setminus\theset{p}$, and choose open arcs $A_i\subseteq S_i\setminus\theset{p}$ about $q_i$ with homeomorphisms $\psi_i:A_i\to(-1,1)$ sending $q_i$ to $0$. Let $X$ be the quotient of the disjoint union $S_1\sqcup S_2$ obtained by identifying $p$ of $S_1$ with $p$ of $S_2$, and by identifying $\psi_1^{-1}(t)$ with $\psi_2^{-1}(t)$ for every $t\in(-1,0)\cup(0,1)$; the points $q_1,q_2$ stay distinct.

Each $S_i$ is a closed copy of $S^1$ in $X$: for $V\subseteq S_1$ open in $S_1$, the set $V\cup\psi_2^{-1}(\psi_1(V\cap A_1))$ has open preimage in each circle, hence is open in $X$, and it meets $S_1$ in $V$; so the subspace topology on $S_1$ is the circle topology, and $S_1\cap S_2=\theset{p}$. Each $S_i$ is closed in $X$: its complement is open by the same computation.

The space is not Hausdorff: let $O$ be any neighbourhood of $q_1$ in $X$. Its preimage in $S_1$ is a neighbourhood of $q_1$, so it contains $\psi_1^{-1}((-\epsilon,\epsilon))$ for some $\epsilon>0$; then by openness of $O$ the preimage in $S_2$ contains $\psi_2^{-1}((-\epsilon,0)\cup(0,\epsilon))$, which is nonempty and lies in $S_2$ near $q_2$. The same computation with the roles of $q_1$ and $q_2$ interchanged shows that every neighbourhood of $q_2$ meets every neighbourhood of $q_1$. So $q_1\ne q_2$ are not separated by disjoint open sets.

:::

:::

::: pf-qed

Parts (a) and (b) are steps 1--4 and part (c) is step 5.

:::

:::
:::
