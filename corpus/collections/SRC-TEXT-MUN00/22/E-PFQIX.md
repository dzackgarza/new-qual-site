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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with ten steps, two or three for each of the four parts, each carrying a `pf-proof`; the
    arguments and the attribution are unchanged. Cited by number only: Exercise TG.4 (right
    translations are homeomorphisms) and Exercise TG.5 (the quotient map is open), with the
    definition of a topological group for the $T_1$ property and continuity of multiplication
    and inversion. One sentence is corrected: the prose concluded $p(U_2)=F$; the argument
    gives only $p(U_2)\supseteq F$, and the disjointness of the two images comes from $U_1$ and
    $U_2$ being disjoint and saturated, which is what step 9 now says.
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

::: pf

::: pf-step

(a) If $U$ is a neighbourhood of $e$, there are open sets $U_{1},U_{2}\ni e$ with $U_{1}\cdot U_{2}\subset U$.

::: pf-proof

$U$ is a neighbourhood of $e=e\cdot e$, so it contains an open set $O$ with $e\in O$. Multiplication $m:G\times G\to G$ is continuous and $m(e,e)=e\in O$, so $m^{-1}(O)$ is open and contains $(e,e)$; it therefore contains a basis element $U_1\times U_2$ of the product topology with $U_1,U_2$ open and $e\in U_1\cap U_2$. For such a pair $U_1\cdot U_2=m(U_1\times U_2)\subseteq O\subseteq U$.

:::

:::

::: pf-step

(a) With $W=U_{1}\cap U_{2}$, the set $V=W\cap W^{-1}$ is a symmetric open neighbourhood of $e$ and $V\cdot V\subset U$.

::: pf-proof

$W=U_1\cap U_2$ is open and contains $e$, and $W\cdot W\subseteq U_1\cdot U_2\subseteq U$. Inversion is a homeomorphism, so $W^{-1}$ is open and contains $e^{-1}=e$; hence $V=W\cap W^{-1}$ is open and contains $e$. It is symmetric: $V^{-1}=(W\cap W^{-1})^{-1}=W^{-1}\cap W=V$. Since $V\subseteq W$, $V\cdot V\subseteq W\cdot W\subseteq U$. This is the hint of (a), $W\cdot W^{-1}$ being replaced by $W\cap W^{-1}$, which is symmetric for the same reason.

:::

:::

::: pf-step

(b) If $x\ne y$, then $a=yx^{-1}\ne e$ and $G\setminus\{a\}$ is a neighbourhood of $e$; by (a) there is a symmetric $V\ni e$ with $V\cdot V\subset G\setminus\{a\}$.

::: pf-proof

$yx^{-1}=e$ would give $y=x$, so $a\ne e$. A topological group is $T_1$ (Munkres' definition), so $\{a\}$ is closed and $G\setminus\{a\}$ is open and contains $e$, hence is a neighbourhood of $e$; apply step 2 with $U=G\setminus\{a\}$.

:::

:::

::: pf-step

(b) $V\cdot x$ and $V\cdot y$ are disjoint open sets containing $x$ and $y$; hence $G$ is Hausdorff.

::: pf-proof

Left translations are homeomorphisms, so $V\cdot x$ and $V\cdot y$ are open, and they contain $x$ and $y$ because $e\in V$. If a point lay in both, $v_1x=v_2y$ with $v_1,v_2\in V$, so $a=yx^{-1}=v_2^{-1}v_1\in V^{-1}\cdot V=V\cdot V$ by symmetry of $V$, contradicting $V\cdot V\subseteq G\setminus\{a\}$. Distinct points therefore have disjoint open neighbourhoods.

:::

:::

::: pf-step

(c) Let $A$ be closed and $x\notin A$. Then $B=A\cdot x^{-1}$ is closed and $e\notin B$, so by (a) there is a symmetric $V\ni e$ with $V\cdot V\subset G\setminus B$.

::: pf-proof

$B$ is the image of the closed set $A$ under the homeomorphism $g\mapsto gx^{-1}$ (right translations are homeomorphisms, Exercise TG.4), so $B$ is closed. If $e=ax^{-1}$ with $a\in A$ then $x=a\in A$, contrary to hypothesis, so $e\notin B$. Then $G\setminus B$ is open and contains $e$, and step 2 applies to it.

:::

:::

::: pf-step

(c) $V\cdot x$ and $V\cdot A$ are disjoint open sets containing $x$ and $A$; hence $G$ is regular.

::: pf-proof

$V\cdot x$ is open and contains $x$; $V\cdot A=\bigcup_{a\in A}V\cdot a$ is a union of open sets, hence open, and contains $A$ because $e\in V$. If $v_1x=v_2a$ with $a\in A$, then $ax^{-1}=v_2^{-1}v_1\in V^{-1}\cdot V=V\cdot V$, while $ax^{-1}\in A\cdot x^{-1}=B$; that contradicts $V\cdot V\subseteq G\setminus B$. So a closed set and a point outside it are separated by disjoint open sets, which is regularity.

:::

:::

::: pf-step

(d) Let $H$ be a closed subgroup, $p:G\to G/H$ the quotient map, $F\subset G/H$ closed and $xH\notin F$. Then $A=p^{-1}(F)$ is closed, saturated, and $x\notin A$; as in (c), $A\cdot x^{-1}$ is closed and misses $e$, so there is a symmetric $V\ni e$ with $V\cdot V\subset G\setminus A\cdot x^{-1}$.

::: pf-proof

$p$ is continuous, so $A=p^{-1}(F)$ is closed, and it is saturated: it is a union of cosets because $F$ is a set of cosets. If $x\in A$ then $xH=p(x)\in F$, contrary to hypothesis. The set $A\cdot x^{-1}$ is closed as in step 5 and does not contain $e$, since $x\notin A$; step 2 applied to its complement gives the symmetric $V$.

:::

:::

::: pf-step

(d) $V\cdot x$ and $V\cdot A$ are disjoint open sets containing $x$ and $A$; and $U_{1}=V\cdot x\cdot H$ and $U_{2}=V\cdot A\cdot H=V\cdot A$ are saturated open sets, still disjoint, containing $x$ and $A$.

::: pf-proof

Step 6, applied to this $A$ and $V$, gives the disjointness and openness of $V\cdot x$ and $V\cdot A$. $A\cdot H=A$ because $A$ is saturated, so $U_2=V\cdot A$ is saturated; and $U_1=\bigcup_{h\in H}V\cdot x\cdot h$ is a union of translates of the open set $V\cdot x$, hence open, and it is saturated because $H$ is a subgroup. If a point lay in both, $v_1xh=v_2a$ with $v_1,v_2\in V$, $h\in H$, $a\in A$; then $v_1x=v_2(ah^{-1})$, and $ah^{-1}\in A\cdot H=A$, so $v_1x\in V\cdot A$, contradicting the disjointness of $V\cdot x$ and $V\cdot A$.

:::

:::

::: pf-step

(d) Since $p$ is open, $p(U_{1})\ni xH$ and $p(U_{2})\supset F$ are disjoint open sets of $G/H$; hence $G/H$ is regular.

::: pf-proof

$p$ is an open map (Exercise TG.5), so both images are open; $x\in U_1$ gives $xH\in p(U_1)$, and $A\subseteq U_2$ gives $p(U_2)\supseteq p(A)=F$. They are disjoint because $U_1$ and $U_2$ are disjoint and saturated: if $p(u_1)=p(u_2)$ with $u_i\in U_i$, then $u_1\in u_2H\subseteq U_2$, since $U_2$ is saturated, contrary to disjointness. (The prose's $p(U_2)=F$ is not asserted: what the argument needs is $p(U_2)\supseteq F$.) Thus a closed subset of $G/H$ and a point outside it are separated by disjoint open sets.

:::

:::

::: pf-step

The four parts are proved: symmetric halves in $G$, the Hausdorff property, regularity, and regularity of $G/H$ for closed $H$.

::: pf-proof

Part (a) is steps 1--2, part (b) steps 3--4, part (c) steps 5--6 and part (d) steps 7--9.

:::

:::

:::
:::
