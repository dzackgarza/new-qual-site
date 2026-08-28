---
schema: qual/card@1
id: E-VYYH3
kind: exercise
title: Finitely presented groups as fundamental groups of compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem.
If $G$ is a finitely presented group, then there is a compact Hausdorff space $X$ whose fundamental group is isomorphic to $G$.

Proof.
Suppose $G$ has a presentation consisting of $n$ generators and $m$ relations.
Let $A$ be the wedge of $n$ circles; form an adjunction space $X$ from the union of $A$ and $m$ copies $B_1, \ldots, B_m$ of the unit ball by means of a continuous map $f: \bigcup \operatorname{Bd} B_i \to A$.

(a) Show that $X$ is Hausdorff.

(b) Prove the theorem in the case $m = 1$.

(c) Proceed by induction on $m$, using the algebraic result stated in the following exercise.

The construction outlined in this exercise is a standard one in algebraic topology; the space $X$ is called a two-dimensional CW complex.
:::
