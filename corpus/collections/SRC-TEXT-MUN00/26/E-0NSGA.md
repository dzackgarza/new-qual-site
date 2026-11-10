---
schema: qual/card@1
id: E-0NSGA
kind: problem
title: Products of compact sets in topological groups
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 13, printed p. 172, with Lemma 26.4,
    Exercise 26.5, Exercise 26.9, TG.5 and TG.7(b); the three parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.13, PDF p. 15, for the plan. Its printed proofs
    are not usable — the neighbourhood in (a) is a translate of B rather than one of the
    fixed point, and (b) and (c) answer compactness questions instead of the Hausdorff one —
    so the three arguments are written out: A . B closed for A closed and B compact via the
    compact set c B^{-1} separated from A and the tube lemma, compact times compact compact
    as an image, and p perfect with G Hausdorff exactly when G/H is. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $G$ be a topological group.

(a) Let $A$ and $B$ be subspaces of $G$.
If $A$ is closed and $B$ is compact, show $A \cdot B$ is closed.
[Hint: If $c$ is not in $A \cdot B$, find a neighborhood $W$ of $c$ such that $W \cdot B^{-1}$ is disjoint from $A$.]

(b) Let $H$ be a subgroup of $G$; let $p: G \to G/H$ be the quotient map.
If $H$ is compact, show that $p$ is a closed map.

(c) Let $H$ be a compact subgroup of $G$.
Show that if $G/H$ is compact, then $G$ is compact.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.13, PDF p. 15** (`tmp/sources/munkres-solutions-positron-ch3.pdf`) for the plan of the three parts. Its printed proofs are not usable as they stand — the neighbourhood $U\cdot B$ in (a) is a translate of the whole of $B$ rather than a neighbourhood of the fixed point, and its (b) and (c) answer questions about compactness of $G$ instead of the Hausdorff question asked — so the arguments below are written out, using the two facts they cite: that a topological group is Hausdorff (Supplementary Exercise TG.7(b)) and that the quotient map to the coset space is open (TG.5(c)).

Let $G$ be a topological group with identity $e$, $H$ a compact subgroup, $p:G\to G/H$ the quotient map.

(a) *If $A$ is closed and $B$ compact then $A\cdot B$ is closed.* Let $c\notin A\cdot B$. The set $c\cdot B^{-1}=\{cb^{-1}\mid b\in B\}$ is compact (a homeomorphic image of $B$) and disjoint from $A$: $cb^{-1}=a$ would give $c=ab\in A\cdot B$. As $G$ is Hausdorff, Exercise 26.5 gives disjoint open sets $U\supset A$, $V\supset c\cdot B^{-1}$. The set $\{(g,b)\mid gb^{-1}\in V\}$ is open in $G\times G$ and contains $\{c\}\times B$, so by the tube lemma (Exercise 26.9) there is a neighbourhood $W$ of $c$ with $W\cdot B^{-1}\subset V$. Then $W\cap A\cdot B=\varnothing$: a point $w=ab$ would satisfy $wb^{-1}=a\in A$ and $wb^{-1}\in V$. So $A\cdot B$ is closed.

(b) *If $A$ and $B$ are compact then $A\cdot B$ is compact*, being the image of the compact space $A\times B$ under the continuous multiplication.

(c) *$p$ is perfect.* It is continuous and surjective; each fibre $p^{-1}(\{xH\})=xH$ is compact, being homeomorphic to $H$; and it is closed: for closed $A\subset G$, $p^{-1}(p(A))=A\cdot H$ is closed by (a), with $H$ compact, so $p(A)$ is closed in $G/H$ because $p$ is a quotient map.

*$G$ is Hausdorff if and only if $G/H$ is.* If $G$ is Hausdorff, let $xH\ne yH$; the cosets $xH$ and $yH$ are disjoint compact subsets of $G$, so by Exercise 26.5 there are disjoint open $U\supset xH$, $V\supset yH$. Their images $p(U)\ni xH$ and $p(V)\ni yH$ are open because $p$ is open, and disjoint because $U\cap V$ contains no coset. Conversely a topological group is $T_{1}$ by definition — one-point sets are closed, singletons being the fibres of translations — and a $T_{1}$ topological group is Hausdorff by Supplementary Exercise TG.7(b). So the assertion reduces to the direction just proved, $G$ Hausdorff implying $G/H$ Hausdorff, which needs the closedness and openness of $p$ together with the compactness of $H$.
:::
