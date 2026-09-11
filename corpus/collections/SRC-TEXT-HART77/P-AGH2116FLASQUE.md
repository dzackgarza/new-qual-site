---
schema: qual/card@1
id: P-AGH2116FLASQUE
kind: problem
title: Flasque sheaves and the exactness of sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Flasque Sheaves
  - Exact Sequences
relations: []
review: draft
---

::: problem
A sheaf $\mcf$ on a topological space $X$ is **flasque** if for every inclusion $V \subseteq U$ of open sets the restriction map $\mcf(U) \to \mcf(V)$ is surjective.

a. Show that a constant sheaf on an irreducible topological space is flasque.

b. If
\[
0 \to \mcf' \to \mcf \to \mcf'' \to 0
\]
is an exact sequence of sheaves and $\mcf'$ is flasque, then for any open set $U$ the sequence
\[
0 \to \mcf'(U) \to \mcf(U) \to \mcf''(U) \to 0
\]
of abelian groups is also exact.

c. If
\[
0 \to \mcf' \to \mcf \to \mcf'' \to 0
\]
is an exact sequence of sheaves and $\mcf'$ and $\mcf$ are flasque, then $\mcf''$ is flasque.

d. If $f: X \to Y$ is a continuous map and $\mcf$ is a flasque sheaf on $X$, then $f_* \mcf$ is a flasque sheaf on $Y$.

e. Let $\mcf$ be any sheaf on $X$.
Define a new sheaf $\mcg$, called the sheaf of **discontinuous sections** of $\mcf$, as follows: for each open set $U \subseteq X$, let $\mcg(U)$ be the set of maps $s: U \to \Union_{P \in U} \mcf_P$ such that $s(P) \in \mcf_P$ for each $P \in U$.
Show that $\mcg$ is a flasque sheaf and that there is a natural injective morphism $\mcf \to \mcg$.
:::
