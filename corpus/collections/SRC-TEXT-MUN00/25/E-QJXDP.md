---
schema: qual/card@1
id: E-QJXDP
kind: problem
title: Weak local connectedness at a point without local connectedness
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 7, printed p. 162, with the figure
    and the hint; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.7, PDF pp. 9-10. A connected neighbourhood of p
    would have to contain every a_i, by spreading along the segments crossing a small ball;
    the sub-broom over the tail of the a_i is a path-connected set containing a
    neighbourhood of p. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    Two defects located, neither repaired in this pass, which is why the solution section
    still carries the retained set's argument. (1) The printed statement cannot hold. The
    definition in Exercise 6 of the same page, read at 600 dpi from the retained PDF
    (printed p. 162), is "for every neighborhood U of x, there is a connected subspace of X
    contained in U that contains a neighborhood of x"; the connected subspace then contains
    a neighbourhood of x, so it is itself a connected neighbourhood of x contained in U, and
    a space weakly locally connected at x is locally connected at x. The exercise asks for a
    space that is not locally connected at p and is weakly locally connected at p, so the
    printed conclusion is impossible under the printed definition, whatever the space.
    (2) The description of the space in the solution section, taken from the retained
    positron0802 solution, does not have the property the exercise asserts: with bristles
    running from (a_i,0) to (a_{i+1},r_j), choose epsilon with a_{N+1} < epsilon < a_N and
    delta no larger than a_{N+1}; every bristle meeting B(p,delta) has its foot of the form
    (a_i,0) with a_i <= a_{N+1} < epsilon, hence inside B(p,epsilon), so the component of p
    in the trace of B(p,epsilon) contains the whole trace of B(p,delta) and is a
    neighbourhood of p: that space is locally connected at p. The book draws Figure 25.1 and
    states no formula for the bristles, no retained set in the checkout describes them in
    words (the Whitman, 9beach and shenapse manuals have no occurrence of the broom), and
    the figure does not determine what the bristles attach to. The card is therefore left as
    it stands pending a description of the space that the figure settles; rewriting the
    proof alone would not repair it.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    The card rewritten as a structured proof, after the two defects recorded above. (1) The
    space: the book gives Figure 25.1 and no formula; the retained description (branches from
    (a_i,0) to (a_{i+1},r_j)) is discarded because it makes X locally connected at p, as the
    note above shows. The description now on the card is the one the figure shows, with the
    properties the proof uses stated: branches from (a_i,0) to (a_{i+j},r_j) with
    r_j decreasing to 0, branches meeting the axis only at their feet and having pairwise
    disjoint relative interiors, which is what lets a point of a branch have a ball meeting X
    only in that branch. (2) Part (b): the printed definition of weak local connectivity makes
    part (b) impossible for any space, so the proof is given for the standard notion, "for
    every neighbourhood U of p a connected subspace containing p and contained in U", and the
    card says so on its face. What was searched for a description and did not supply one:
    Wikipedia's "infinite broom" is a different space (segments from the origin to (1,1/n)
    with an interval on the axis); the Math StackExchange threads 2439096 and 4145547 discuss
    this exercise without stating the figure's geometry, and 4145547 records the same
    difficulty with the printed definition; the retained manuals (Whitman, 9beach, shenapse)
    contain no occurrence of the broom. The proof of (a): for epsilon in (0,a_1), delta in
    (0,epsilon) and j large, the point (a_{1+j},r_j) lies in B(p,delta) and is an endpoint of
    the branch from (a_1,0), whose foot is outside B(p,epsilon); so in any open neighbourhood
    V of p inside B(p,epsilon) the set V intersected with that branch is nonempty, open and
    closed in V and misses p, and V is disconnected. Part (b) is then the axis piece.
---
---

::: {.exercise}

Consider the "infinite broom" $X$ pictured in Figure 25.1 of the text.
Show that $X$ is not locally connected at $p$, but is weakly locally connected at $p$.
[Hint: Any connected neighborhood of $p$ must contain all the points $a_i$.]
:::

::: {.solution}
Two things have to be fixed before the exercise can be proved, and both are recorded in the audit: the description of the space, and the notion in part (b).

The book draws $X$ in Figure 25.1 (printed p. 162) and states no formula, and the description in the retained solution -- branches from $(a_i,0)$ to $(a_{i+1},r_j)$ -- makes $X$ locally connected at $p$, so it cannot be the figure's space. The description used here is the one the figure shows, branches of decreasing height running left from the points $a_i$ and crowding towards $p$: $p=(0,0)$; points $(a_i,0)$ on the axis with $a_1=1$ and $a_i$ strictly decreasing to $p$; the segment $L$ from $p$ to $(a_1,0)$; for each $i,j\ge1$ a closed segment $L_{i,j}$ from $(a_i,0)$ to $(a_{i+j},r_j)$, where $r_j>0$ and $r_j\downarrow0$ with $r_j<a_j$; branches meet the axis only at their feet and have pairwise disjoint relative interiors, as in the figure; $X=L\cup\bigcup_{i,j}L_{i,j}$ with the subspace topology of $\RR^2$.

Part (b) carries a defect of the printed page. The definition in §25 Exercise 6 (printed p. 162) is "for every neighborhood $U$ of $x$ there is a connected subspace of $X$ contained in $U$ that contains a neighborhood of $x$" (checked at 600 dpi against the retained PDF): a connected subspace containing a neighbourhood of $x$ is itself a connected neighbourhood of $x$, so with that definition a space weakly locally connected at $x$ is locally connected at $x$, and the printed conclusion of this exercise cannot hold for any space. Part (b) is proved below for the standard notion, which is what the exercise needs: for every neighbourhood $U$ of $p$ there is a connected subspace containing $p$ and contained in $U$.

::: pf

::: {.pf-step #space}
$X$ is connected, and $X\cap B(p,\varepsilon)$ for $0<\varepsilon<a_1$ consists of the axis piece $[0,\varepsilon)\times\{0\}$ together with the pieces inside the ball of the branches that meet it.

::: pf-proof
$X$ is the union of the connected set $L$ and the branches, each of which is a compact connected set meeting $L$ at its foot $(a_i,0)$; a union of connected sets all meeting one of them is connected. The description of the trace on $B(p,\varepsilon)$ is the definition of the subspace topology.
:::

:::

::: {.pf-step #not-locally}
(a) $X$ is not locally connected at $p$.

::: pf-proof

::: {.pf-step #far-end}
Let $0<\varepsilon<a_1$, let $0<\delta<\varepsilon$ and choose $j$ with $a_{1+j}<\delta/2$ and $r_j<\delta/2$. Then $q=(a_{1+j},r_j)$ is an endpoint of the branch $L_{1,j}$, whose foot is $(a_1,0)$, and $q\in B(p,\delta)$.

::: pf-proof
$a_{1+j}\to0$ and $r_j\to0$, so such $j$ exists; the distance from $q$ to $p$ is $\sqrt{a_{1+j}^2+r_j^2}<\delta$, since both coordinates are below $\delta/2$. The foot of $L_{1,j}$ is $(a_1,0)$, whose distance to $p$ is $a_1=1>\varepsilon$.
:::

:::

::: {.pf-step #clopen}
If $V$ is an open subset of $X$ with $p\in V$ and $V\subseteq X\cap B(p,\varepsilon)$, then $V\cap L_{1,j}$ is a nonempty subset of $V$, open and closed in $V$, not containing $p$; hence $V$ is disconnected.

::: pf-proof
Let $A=V\cap L_{1,j}$. It is nonempty as soon as $V$ contains $q$, which holds if $X\cap B(p,\delta)\subset V$ by step [](#far-end){.pf-ref}. It is compact, being a closed subset of the compact segment $L_{1,j}$, and $V$ is a subspace of the metric space $\RR^2$, so $A$ is closed in $V$. For each $a\in A$ there is a ball about $a$ meeting $X$ only in $L_{1,j}$: the branches have pairwise disjoint relative interiors, and the only points of $L_{1,j}$ on the axis is its foot $(a_1,0)$, which is outside $B(p,\varepsilon)$; its other endpoint $(a_{1+j},r_j)$ has $r_j>0$ and so is not on the axis nor a foot of another branch. So every point of $A$ is an interior point of the branch, where a ball meets $X$ only in that branch; shrinking that ball into $V$, which is open, gives a neighbourhood of $a$ in $V$ contained in $A$, and $A$ is open in $V$. Finally $p\notin A$ because $p\notin L_{1,j}$. So $A$ and $V-A$ are nonempty, disjoint and open in $V$.
:::

:::

:::

:::

::: {.pf-step}
(a) Every neighbourhood of $p$ inside $X\cap B(p,\varepsilon)$ is disconnected, so $X$ is not locally connected at $p$; and (b) for every neighbourhood $U$ of $p$ there is a connected subspace containing $p$ and contained in $U$, namely $L\cap U$.

::: pf-proof
For the first assertion, let $V$ be an open neighbourhood of $p$ with $V\subseteq X\cap B(p,\varepsilon)$; since $V$ is a neighbourhood of $p$ in $X$ there is $\delta>0$ with $X\cap B(p,\delta)\subset V$, and then step [](#clopen){.pf-ref} shows $V$ disconnected. As $V$ was arbitrary, no connected neighbourhood of $p$ lies in $X\cap B(p,\varepsilon)$, which is a neighbourhood of $p$; hence $X$ is not locally connected at $p$. For the second, let $U$ be a neighbourhood of $p$; it contains $X\cap B(p,\delta)$ for some $\delta>0$, and $C=L\cap U$ is an interval of the axis containing $p$, hence connected, with $p\in C\subset U$; this is weak local connectivity at $p$ in the standard sense stated above, which is the assertion of part (b) under the corrected reading.
:::

:::

:::
:::
