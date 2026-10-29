---
schema: qual/card@1
id: P-WESTOP03-03
kind: problem
title: Characterize several classes of spaces as subspaces of familiar spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: A second copy of the 2003 exam later in the same retained extraction recovers the previously garbled fourth item as “Open subspaces of compact Hausdorff spaces.”
---

::: {.problem}
Characterize each of the following classes in terms of familiar intrinsic properties, with some justification:

1. subspaces of Hausdorff spaces;
2. subspaces of compact spaces, where compact means only that every open cover has a finite subcover;
3. subspaces of compact Hausdorff spaces;
4. open subspaces of compact Hausdorff spaces;
5. subspaces of path-connected spaces.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A space is homeomorphic to a subspace of a Hausdorff space if and only if it is Hausdorff.


::: pf-proof

Every subspace of a Hausdorff space is Hausdorff: distinct points can be separated by intersecting disjoint ambient neighborhoods with the subspace. Conversely, every Hausdorff space $X$ is itself a subspace of the Hausdorff space $X$.

:::

:::

::: {.pf-step #s1-2}

Every topological space is homeomorphic to a subspace of a compact space, when no separation axiom is imposed on the compact ambient space.


::: pf-proof

Given any space $X$, adjoin one point $\infty$ and let
$$
X^*=X\sqcup\{\infty\}.
$$
Declare the open sets of $X^*$ to be all open subsets of $X$, together with $X^*$ itself. Then the subspace topology on $X$ is its original topology. Moreover, every open cover of $X^*$ contains the only open set containing $\infty$, namely $X^*$ itself, so it has a one-element finite subcover. Thus $X^*$ is compact and contains $X$ as a subspace.

:::

:::

::: {.pf-step #s1-3}

A space is homeomorphic to a subspace of a compact Hausdorff space if and only if it is Tychonoff, i.e. completely regular and Hausdorff.


::: pf-proof

Every subspace of a compact Hausdorff space is completely regular and Hausdorff, because compact Hausdorff spaces are Tychonoff and the Tychonoff property is hereditary to subspaces. Conversely, the Tychonoff embedding theorem embeds every Tychonoff space $X$ into a cube
$$
[0,1]^I
$$
for a suitable index set $I$ (for example using its continuous $[0,1]$-valued functions). By Tychonoff's theorem this cube is compact, and it is Hausdorff as a product of Hausdorff spaces.

:::

:::

::: {.pf-step #s1-4}

A space is homeomorphic to an open subspace of a compact Hausdorff space if and only if it is locally compact Hausdorff.


::: pf-proof

If $X$ is open in a compact Hausdorff space $K$, then $X$ is Hausdorff. For $x\in X$, regularity of $K$ gives an open neighborhood $V$ of $x$ whose closure in $K$ is contained in $X$; this closure is compact, so $X$ is locally compact. Conversely, if $X$ is locally compact Hausdorff and noncompact, its one-point compactification
$$
X^+=X\sqcup\{\infty\}
$$
is compact Hausdorff and $X=X^+\setminus\{\infty\}$ is open. If $X$ is already compact Hausdorff, take $X$ itself as the compact Hausdorff ambient space.

:::

:::

::: {.pf-step #s1-5}

Every topological space is homeomorphic to a subspace of a path-connected space.


::: pf-proof

For any space $X$, form its cone
$$
CX=(X\times[0,1])/(X\times\{1\}),
$$
and let $v$ denote the cone point. The map
$$
i:X\to CX,
\qquad
i(x)=[x,0],
$$
is an embedding: the quotient map restricts to a homeomorphism from $X\times\{0\}$ onto its image because the only identifications occur in $X\times\{1\}$. For any point $[x,t]\in CX$, the path
$$
s\longmapsto[x,(1-s)t+s]
$$
joins it to $v$. Thus every point can be joined to $v$, so $CX$ is path connected.

:::

:::

::: {.pf-step #s1-6}

Consequently the requested characterizations are
$$
\boxed{
\begin{array}{c|c}
\text{ambient class} & \text{intrinsic class of subspaces}\\ \hline
\text{Hausdorff} & \text{Hausdorff}\\
\text{compact, no separation axiom} & \text{all spaces}\\
\text{compact Hausdorff} & \text{Tychonoff spaces}\\
\text{open in compact Hausdorff} & \text{locally compact Hausdorff}\\
\text{path connected} & \text{all spaces}
\end{array}}
$$


::: pf-proof

The five rows are exactly steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} collects the five required characterizations with the constructions and necessity arguments established above.

:::

:::

:::
