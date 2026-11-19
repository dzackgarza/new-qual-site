---
schema: qual/card@1
id: E-ETKNU
kind: problem
title: The imbedding theorem for $m=1$ and linear graphs in $\RR^3$
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The source says g maps X onto a linear graph. The proof gives only containment in one: a Cantor-set domain can have an infinite totally disconnected image inside an edge.'
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), §50 Exercise 5, printed p. 315, and the proof of the imbedding
    theorem (Theorem 50.5) on printed pp. 309-312, in particular the step where the approximating map
    g(x) = sum of phi_i(x) z_i is built from a cover of order m+1 = 2 and points z_i in general position. What
    was corrected: the card had stored the exercise with the word "into" in place of the printed "onto", and
    proved only that the image lies in the graph; it now states the exercise as printed and says where "onto"
    is realized, namely after the injectivity step at the end of the theorem, the single approximation step
    giving containment in the graph G that has the z_i as vertices. The argument itself, that at most two
    partition functions are nonzero at a point so the image lies in the union of the segments [z_i,z_j], and that
    those segments meet only at common vertices because four of the z_i are never coplanar and three never
    collinear, is unchanged.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located treats Munkres §50 Exercise 5 (printed p. 315).
    Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the ten GitHub repositories of Munkres
    solutions listed in COMPLAINTS.md stop before §36, and the AoPS post *Topology by Munkres Chapter 8 | Day
    18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost. The
    exercise is a check on the proof of Theorem 50.5 rather than a statement with an answer of its own, and the
    card's two points are the ones the case $m=1$ needs: at most two of the partition-of-unity functions are
    nonzero at a point, so $g(X)$ lies in the union of the segments $[z_i,z_j]$, and general position keeps two
    such segments from meeting except in a shared endpoint, which the card verifies from the affine
    independence of every four of the $z_i$. Nothing needed correction.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the data of the theorem at $m=1$, the at-most-two-nonzero
    step, the containment in the union of segments, the two general-position checks, and the closing step on
    the word "onto". The mathematics is the card's own, unchanged, including its recorded repair that the
    single approximation step gives containment only. No complete published solution was located on the
    earlier pass, whose searches are listed in the audit events above; nothing was re-searched here.
---

::: {.exercise}

Examine the proof of the imbedding theorem in the case $m = 1$ and show that the map $g$ of part (2) actually maps $X$ onto a linear graph in $\RR^3$.
:::

::: {.solution}
No retained solution set covers this exercise: it is a check on the proof of Theorem 50.5 rather than a statement with an answer of its own, and the searches recorded in the audit events above located nothing that treats §50 Exercise 5 (printed p. 315). The argument is therefore the card's own.

The data are those of the theorem's proof with $m=1$, so $N=2m+1=3$: a finite open cover $\{U_{1},\dots,U_{r}\}$ of order at most $2$, a partition of unity $\{\phi_{1},\dots,\phi_{r}\}$ dominated by it, points $z_{1},\dots,z_{r}\in\RR^{3}$ in general position, and $g(x)=\sum_{i}\phi_{i}(x)z_{i}$.

::: pf

::: {.pf-step #order}
At most two of the numbers $\phi_{1}(x),\dots,\phi_{r}(x)$ are nonzero at any $x\in X$, and those present are nonnegative and sum to $1$.

::: pf-proof
The cover has order at most $2$: no point of $X$ lies in three of its members. The partition of unity is dominated by the cover, so the support of $\phi_{i}$ lies in $U_{i}$, and hence $\phi_{i}(x)\ne0$ forces $x\in U_{i}$; if three of the $\phi_{i}(x)$ were nonzero, $x$ would lie in three members of the cover. Nonnegativity and the sum being $1$ are the defining properties of a partition of unity.
:::

:::

::: {.pf-step #image}
$g(x)$ is either one of the $z_{i}$ or a point of a segment $[z_{i},z_{j}]$ with $i\ne j$; consequently $g(X)\subseteq G:=\bigcup_{i<j}[z_{i},z_{j}]$.

::: pf-proof
By step [](#order){.pf-ref} either exactly one $\phi_{i}(x)=1$ and all others vanish, giving $g(x)=z_{i}$, or exactly two are nonzero, $\phi_{i}(x)=t$ and $\phi_{j}(x)=1-t$ with $0<t<1$, giving $g(x)=tz_{i}+(1-t)z_{j}\in[z_{i},z_{j}]$. In either case $g(x)$ lies in $G$, so the image is contained in it.
:::

:::

::: {.pf-step #general-position}
Every four of the $z_{i}$ are affinely independent, hence no four are coplanar and no three are collinear.

::: pf-proof
General position in $\RR^{3}$ for $r$ points means, by the definition used in the proof, that any $4=3+1$ of them are affinely independent; four affinely independent points of $\RR^{3}$ do not lie in a plane. If three of them were collinear, those three together with any fourth would lie in a plane, contradicting the preceding sentence.
:::

:::

::: {.pf-step #disjoint}
If $\{i,j\}\cap\{k,l\}=\varnothing$ then $[z_{i},z_{j}]\cap[z_{k},z_{l}]=\varnothing$.

::: pf-proof
A common point of the two segments would lie on both, so the four endpoints would all lie in the plane spanned by that point and the two lines: concretely, the two segments with a common point determine two lines meeting there, those lines span a plane, and the four $z$'s lie in it. That contradicts the affine independence of every four points from step [](#general-position){.pf-ref}.
:::

:::

::: {.pf-step #shared}
If the two segments share exactly one endpoint $z_{i}$ then they meet in that point only.

::: pf-proof
Suppose $[z_{i},z_{j}]$ and $[z_{i},z_{l}]$ meet at a point other than $z_{i}$. Then the two segments have two distinct common points, so the two lines they span coincide, and $z_{i},z_{j},z_{l}$ are collinear, contrary to step [](#general-position){.pf-ref}. So the intersection is $\{z_{i}\}$.
:::

:::

::: {.pf-step #graph}
$G=\bigcup_{i<j}[z_{i},z_{j}]$ with vertices $z_{1},\dots,z_{r}$ is a linear graph in $\RR^{3}$, and $g$ carries $X$ into it.

::: pf-proof
$G$ is a finite union of straight line segments; by steps [](#disjoint){.pf-ref} and [](#shared){.pf-ref}, any two of its segments meet at most in a common endpoint, which is exactly the condition that makes such a union a linear graph with the $z_{i}$ as its vertices. Step [](#image){.pf-ref} gives $g(X)\subseteq G$.
:::

:::

::: {.pf-step}
The word "onto" in the exercise is realized at the end of the theorem's proof, after injectivity.

::: pf-proof
What the approximation step above establishes is containment, $g(X)\subseteq G$, and that is all it can give: a single choice of the partition of unity need not produce an injective map, and a Cantor set inside an edge of the graph can occur in the image of a non-injective $g$. The theorem's proof then shows that $g$ may be taken injective, and a continuous injection from the compact space $X$ into the metric space $\RR^{3}$ is an imbedding onto its image; the image, being a subspace of the linear graph $G$, is then the linear graph the exercise speaks of, with vertices the points $g(x)$ at which exactly one partition function is nonzero. So "onto a linear graph" holds in the sense that $g$ maps $X$ onto a linear graph — its image, once $g$ is injective — and the containment in $G$ proved above is the part of the statement that the approximation step alone supplies.
:::

:::

:::
:::
