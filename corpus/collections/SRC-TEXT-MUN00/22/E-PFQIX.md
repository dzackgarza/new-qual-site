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
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Supplementary Exercise 7, printed p. 146,
    with the definition of topological group and Exercise TG.5; the four parts and the hints
    are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise TG.7, printed pp.
    270-271. His are the symmetric neighbourhood V with V V contained in U, the Hausdorff
    property by separating e from a = y x^{-1}, the regularity argument separating x from A
    through the closed set A x^{-1}, and the passage to G/H using that the quotient map is
    open and that the sets can be taken saturated. (tmp/sources/munkres-solutions-
    whitman.pdf).
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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.7, printed pp. 270--271** (`tmp/sources/munkres-solutions-whitman.pdf`); the four parts are his, the hint of (a) being used as he uses it.

Let $G$ be a topological group with identity $e$, and for $A,B\subset G$ write $A\cdot B=\{ab\mid a\in A,\ b\in B\}$, $A^{-1}=\{a^{-1}\mid a\in A\}$.

(a) Let $U$ be a neighbourhood of $e$. The multiplication $m:G\times G\to G$ is continuous at $(e,e)$, so there are open $U_{1},U_{2}\ni e$ with $U_{1}\cdot U_{2}\subset U$; put $W=U_{1}\cap U_{2}$, an open neighbourhood of $e$ with $W\cdot W\subset U$. Then $W\cap W^{-1}$ is an open neighbourhood $V$ of $e$ (inversion is a homeomorphism) and it is symmetric: $V=V^{-1}$. Since $V\subset W$, $V\cdot V\subset W\cdot W\subset U$.

(b) *$G$ is Hausdorff.* Let $x\ne y$; since $G$ is $T_{1}$, the set $G-\{y\}$ is a neighbourhood of $x$. Using (a) at the identity: $a=y\,x^{-1}\ne e$, so $G-\{a\}$ is a neighbourhood of $e$; choose a symmetric $V\ni e$ with $V\cdot V\subset G-\{a\}$. Then $V\cdot x$ and $V\cdot y$ are disjoint open sets containing $x$ and $y$: if $v_{1}x=v_{2}y$ with $v_{1},v_{2}\in V$, then $a=yx^{-1}=v_{2}^{-1}v_{1}\in V^{-1}\cdot V=V\cdot V$, contradiction.

(c) *Regularity.* Let $A$ be closed and $x\notin A$. Then $B=A\cdot x^{-1}$ is closed (it is the image of $A$ under the homeomorphism $g_{x^{-1}}$ of Exercise TG.4) and $e\notin B$ (since $x\notin A$). So $G-B$ is a neighbourhood of $e$, and by (a) there is a symmetric $V\ni e$ with $V\cdot V\subset G-B$. Then $V\cdot x$ and $V\cdot A$ are disjoint open sets containing $x$ and $A$: if $v_{1}x=v_{2}a$ with $a\in A$, then $ax^{-1}=v_{2}^{-1}v_{1}\in V\cdot V$, while $ax^{-1}\in A\cdot x^{-1}=B$, a contradiction.

(d) Let $H$ be a closed subgroup and $p:G\to G/H$ the quotient map, which is open by Exercise TG.5(c). Let $F\subset G/H$ be closed and let $xH\notin F$. Put $A=p^{-1}(F)$, closed in $G$ and saturated (a union of cosets), with $x\notin A$; as in (c), $A\cdot x^{-1}$ is closed and does not contain $e$, so there is a symmetric neighbourhood $V$ of $e$ with $V\cdot V\subset G-A\cdot x^{-1}$.

Then $V\cdot x$ and $V\cdot A$ are disjoint open sets containing $x$ and $A$ respectively, by the computation of (c). Both can be saturated: $V\cdot A\cdot H=V\cdot A$ because $A\cdot H=A$; and $U_{1}=V\cdot x\cdot H$ is a union of translates of the open set $V\cdot x$, hence open and saturated, and it contains $x$. They remain disjoint, since a common point would give $v_{1}xh=v_{2}a$ with $v_{1},v_{2}\in V$, $h\in H$, $a\in A$, that is $v_{1}x=v_{2}(ah^{-1})\in V\cdot A\cdot H=V\cdot A$, contradicting the disjointness of $V\cdot x$ and $V\cdot A$.

Since $p$ is open, $p(U_{1})\ni xH$ and $p(U_{2})\supset F$ are disjoint open sets of $G/H$; here $p(U_{2})=F$ because $U_{2}$ is saturated and contains $A$, and $p(U_{1})$ is open. So $G/H$ is regular.
:::
