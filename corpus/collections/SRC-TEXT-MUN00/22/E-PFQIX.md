---
schema: qual/card@1
id: E-PFQIX
kind: problem
title: Separation properties of topological groups and coset spaces
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Hausdorff Spaces
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
---

::: {.exercise}

If $A$ and $B$ are subsets of the topological group $G$, let $A \cdot B$ denote the set of all points $a \cdot b$ for $a \in A$ and $b \in B$.
Let $A^{-1}$ denote the set of all points $a^{-1}$, for $a \in A$.

(a) A neighborhood $V$ of the identity element $e$ is said to be symmetric if $V = V^{-1}$.
If $U$ is a neighborhood of $e$, show there is a symmetric neighborhood $V$ of $e$ such that $V \cdot V \subset U$.
[Hint: If $W$ is a neighborhood of $e$, then $W \cdot W^{-1}$ is symmetric.]

(b) Show that $G$ is Hausdorff.
In fact, show that if $x \neq y$, there is a neighborhood $V$ of $e$ such that $V \cdot x$ and $V \cdot y$ are disjoint.

(c) Show that $G$ satisfies the following separation axiom, which is called the regularity axiom: given a closed set $A$ and a point $x$ not in $A$, there exist disjoint open sets containing $A$ and $x$, respectively.
[Hint: There is a neighborhood $V$ of $e$ such that $V \cdot x$ and $V \cdot A$ are disjoint.]

(d) Let $H$ be a subgroup of $G$ that is closed in the topology of $G$; let $p: G \to G/H$ be the quotient map.
Show that $G/H$ satisfies the regularity axiom.
[Hint: Examine the proof of (c) when $A$ is saturated.]
:::

::: {.solution}
(a) Continuity of multiplication at $(e,e)$ gives a neighborhood $W$ of $e$ such that
\[
W\cdot W\subseteq U.
\]
Set
\[
V=W\cap W^{-1}.
\]
Since inversion is a homeomorphism, $V$ is an open neighborhood of $e$; it is symmetric and
\[
V\cdot V\subseteq W\cdot W\subseteq U.
\]

(b) Let $x\ne y$. Since one-point sets are closed in a topological group in Munkres's convention,
\[
U=G-\{xy^{-1}\}
\]
is a neighborhood of $e$. Choose symmetric $V$ with $VV\subseteq U$. If
\[
v_1x=v_2y
\]
with $v_1,v_2\in V$, then
\[
xy^{-1}=v_1^{-1}v_2\in VV\subseteq U,
\]
a contradiction. Hence $Vx$ and $Vy$ are disjoint open neighborhoods, so $G$ is Hausdorff.

(c) Let $A$ be closed and $x\notin A$. The right translate $Ax^{-1}$ is closed and does not contain $e$. Choose a symmetric neighborhood $V$ of $e$ with
\[
VV\subseteq G-Ax^{-1}.
\]
The sets
\[
Vx,\qquad VA=\bigcup_{a\in A}Va
\]
are open and contain $x$ and $A$. If $v_1x=v_2a$, then
\[
ax^{-1}=v_2^{-1}v_1\in VV,
\]
contradicting the choice of $V$. Thus they are disjoint, proving regularity.

(d) Let $C\subseteq G/H$ be closed and let $xH\notin C$. Put
\[
A=p^{-1}(C).
\]
Then $A$ is closed, saturated, and $x\notin A$; saturation means $AH=A$. Apply (c) to choose symmetric $V$ with
\[
VA\cap Vx=\varnothing.
\]
The quotient map $p:G\to G/H$ is open, so $p(VA)$ and $p(Vx)$ are open neighborhoods of $C$ and $xH$. They are disjoint: if a coset lay in both, there would be $v_1,v_2\in V$, $a\in A$, and $h\in H$ with
\[
v_1a=v_2xh.
\]
Then
\[
v_1ah^{-1}=v_2x,
\]
and $ah^{-1}\in AH=A$, contradicting $VA\cap Vx=\varnothing$. Hence $G/H$ satisfies the regularity axiom.
:::
