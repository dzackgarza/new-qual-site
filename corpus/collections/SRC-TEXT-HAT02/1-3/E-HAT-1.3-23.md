---
schema: qual/card@1
id: E-HAT-1.3-23
kind: problem
title: "Free properly discontinuous actions are covering space actions"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 23; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Shrunk a properly discontinuous neighborhood against the finitely many nontrivial intersecting translates, using Hausdorffness and freeness.
---

Show that if a group $G$ acts freely and properly discontinuously on a Hausdorff space $X$, then the action is a covering space action.
(Here "properly discontinuously" means that each $x \in X$ has a neighborhood $U$ such that $\{g \in G \mid U \cap g(U) \neq \emptyset\}$ is finite.)
In particular, a free action of a finite group on a Hausdorff space is a covering space action.


::: {.solution}
Let
\[
q:X\to X/G
\]
be the orbit map.

<1>1. Fix $x\in X$.
By proper discontinuity there is an open neighborhood $U$ of $x$ such that
\[
F=\{g\in G:U\cap gU\ne\varnothing\}
\]
is finite.
::: {.proof}
This is exactly the stated proper-discontinuity hypothesis.
:::

<1>2. There is an open neighborhood $V\subseteq U$ of $x$ such that
\[
V\cap gV=\varnothing
\qquad\text{for every }g\ne e.
\]
::: {.proof}
For each nonidentity $g\in F$, freeness gives
\[
gx\ne x.
\]
Since $X$ is Hausdorff, choose disjoint open neighborhoods
\[
A_g\ni x,
\qquad
B_g\ni gx.
\]
Replace $A_g$ by
\[
A_g\cap g^{-1}(B_g),
\]
so that
\[
gA_g\subseteq B_g
\]
and therefore
\[
A_g\cap gA_g=\varnothing.
\]
Because $F\setminus\{e\}$ is finite, the intersection
\[
V=U\cap\bigcap_{g\in F\setminus\{e\}}A_g
\]
is an open neighborhood of $x$.

If $g\in F\setminus\{e\}$, then
\[
V\subseteq A_g,
\qquad
gV\subseteq gA_g,
\]
so $V\cap gV=\varnothing$.
If $g\notin F$, then already $U\cap gU=\varnothing$, and since $V\subseteq U$ we again have
\[
V\cap gV=\varnothing.
\]
Thus the asserted disjointness holds for every nonidentity $g$.
:::

<1>3. The translates $gV$ are pairwise disjoint.
::: {.proof}
If
\[
gV\cap hV\ne\varnothing,
\]
then applying $g^{-1}$ gives
\[
V\cap g^{-1}hV\ne\varnothing.
\]
By <1>2 this forces $g^{-1}h=e$, hence $g=h$.
:::

<1>4. The orbit map restricts to a homeomorphism
\[
q|_V:V\longrightarrow q(V).
\]
Moreover,
\[
q^{-1}(q(V))=\coprod_{g\in G}gV.
\]
::: {.proof}
The second equality follows from the definition of an orbit.
By <1>3 the union is disjoint.
The map $q|_V$ is injective because two points of $V$ in the same orbit would lie in $V\cap gV$ for some $g$, forcing $g=e$.
It is surjective onto $q(V)$ by definition.
The quotient map $q$ is open because
\[
q^{-1}(q(W))=\bigcup_{g\in G}gW
\]
is open for every open $W\subseteq X$.
Hence $q|_V$ is an open continuous bijection, thus a homeomorphism.
:::

<1>5. Therefore $q:X\to X/G$ is a covering map, so the action is a covering space action.
::: {.proof}
The neighborhood $q(V)$ of $q(x)$ is evenly covered by the pairwise disjoint sheets $gV$, each mapped homeomorphically onto $q(V)$ by $q$.
Since $x$ was arbitrary, this holds at every orbit.
:::

<1>6. If $G$ is finite and acts freely on a Hausdorff space $X$, then the action is a covering space action.
::: {.proof}
For every neighborhood $U$ of any point,
\[
\{g\in G:U\cap gU\ne\varnothing\}\subseteq G
\]
is finite because $G$ itself is finite.
Thus the action is properly discontinuous in the stated sense, and <1>5 applies.
:::
:::
