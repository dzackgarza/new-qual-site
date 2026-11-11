---
schema: qual/card@1
id: E-79XXG
kind: problem
title: Covering transformations of four coverings of the figure eight
classification:
  areas:
  - topology
  topics:
  - Covering Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 81 Exercise 2, printed p. 493. The covering-transformation groups of the four coverings of the figure eight, with regularity decided by normality of p_* pi_1(E). Checked against Theorem 81.2 and the printed figures. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages and against Figures 81.4 to 81.7 read from the page image of printed p. 493, and the repair. Corrected: part (c) described the graph of Figure 81.6 wrongly. It labelled the vertices "from left to right u, e0, m, r", which puts e0 second, whereas the printed figure marks e0 on the third vertex, and it read the A-labelled edges as joining u to m and m to r and the B-labelled edge as joining e0 to m. The printed figure is a chain u - m - e0 - r with the A-edges between u and m and between e0 and r, the B-edges between m and e0, and the loops B3 at u and B4 at r; with that data the permutations are a = (u m)(e0 r) and b = (m e0), and the commuting vertex bijection is (u r)(m e0). The answer (group of order 2, not regular) is unchanged, but the old derivation applied its own wrong graph and its transposition phi = (e0 m)(u r) is not the one the figure gives. Every step now cites Munkres by number and page: Definition of a covering map (printed p. 336), Lemma 54.1 (printed p. 342) for uniqueness of path liftings, Lemma 79.1 (printed p. 478) for a covering transformation agreeing at one point being the identity, and Corollary 81.3 (printed p. 489) for regularity of a covering. What the certificate does not cover: the four figures are pictures in the book; their incidence and orientations are read from the page image and are the hypothesis of the computation.
---

::: {.exercise}

Let $X = A \vee B$ be the wedge of two circles.

(a) Let $E$ be the space pictured in Figure 81.4; let $p: E \to X$ wrap each arc $A_1$ and $A_2$ around $A$ and map $B_1$ and $B_2$ homeomorphically onto $B$.
Show that $p$ is a regular covering map.

(b) Determine the group of covering transformations of the covering of $X$ indicated in Figure 81.5. Is this covering regular?

(c) Repeat (b) for the covering pictured in Figure 81.6.

(d) Repeat (b) for the covering pictured in Figure 81.7.

:::

::: {.solution}

Let $x_0$ be the wedge point of $X$, with $A$ and $B$ oriented by the arrows of the figures.
In each figure $E$ is a graph whose vertices form $p^{-1}(x_0)$ and whose edges are labelled $A_i$ or $B_i$; $p$ maps each edge onto $A$ or $B$ according to its label, in the direction of its arrow.
For a vertex $v$, let $a \cdot v$ be the head of the $A$-labelled edge leaving $v$, and $b \cdot v$ the head of the $B$-labelled edge leaving $v$.
A covering transformation is a homeomorphism $h \colon E \to E$ with $p \circ h = p$ (Definition of a covering map, printed p. 336, and §81 printed p. 487), and the covering is regular when for every two points $e, e'$ of $p^{-1}(x_0)$ some covering transformation sends $e$ to $e'$ (Corollary 81.3, printed p. 489).
The four figures are Figures 81.4 to 81.7 of Munkres, *Topology*, 2nd ed., printed pp. 492--493.

::: pf

::: {.pf-step #covering}

In each figure $p$ is a covering map.

::: pf-proof

In each figure every vertex has exactly one incoming and one outgoing edge of each label, counting a loop as both.
So a small open star of each vertex maps homeomorphically onto a small open star $W$ of $x_0$, and $p^{-1}(W)$ is the disjoint union of these stars.
A point interior to $A$ or $B$ has an open arc as neighbourhood whose preimage is a disjoint union of open arcs, one in each edge with that label, each mapped homeomorphically.
This is the condition of the Definition of a covering map (printed p. 336).

:::

:::

::: {.pf-step #deck}

A covering transformation $h$ permutes the vertices, satisfies $h(a \cdot v) = a \cdot h(v)$ and $h(b \cdot v) = b \cdot h(v)$, and is determined by $h(e_0)$.
Conversely, a bijection $\phi$ of the vertices commuting with $a \cdot$ and $b \cdot$ is induced by a covering transformation.

::: pf-proof

Since $p h = p$, $h$ preserves $p^{-1}(x_0)$, the set of vertices.
If $\tilde\gamma$ is the lift of the loop $A$ starting at $v$, then $h \circ \tilde\gamma$ is a lift of $A$ starting at $h(v)$, so by uniqueness of path lifting (Lemma 54.1, printed p. 342) it ends at $a \cdot h(v)$; likewise for $b$, and $h$ of a loop at $v$ is a loop at $h(v)$.
Two covering transformations that agree at $e_0$ are lifts of $p$ agreeing at a point of the path connected space $E$, hence equal by the uniqueness part of Lemma 79.1 (printed p. 478).
For the converse, $\phi$ carries the $A$-edge from $v$ to $a \cdot v$ to the $A$-edge from $\phi(v)$ to $a \cdot \phi(v)$, and similarly for $B$; define $h$ on each closed edge $e$ as $(p|_{e'})^{-1} \circ p|_{e}$ on its interior, where $e'$ is the image edge, and as $\phi$ on vertices.
Then $h$ is a homeomorphism with $p h = p$.

:::

:::

::: pf-step

(a) $p$ is a regular covering, with group of covering transformations $\ZZ/2$.

::: pf-proof

In Figure 81.4 the vertices are $e_0$ and the other vertex $v$ of the circle $A_1 \cup A_2$; $A_1$ runs from $e_0$ to $v$ and $A_2$ from $v$ to $e_0$, and $B_1$, $B_2$ are loops at $v$ and at $e_0$ respectively.
So $a$ swaps $e_0$ and $v$, and $b$ fixes both.
The swap $e_0 \leftrightarrow v$ commutes with $a$ and $b$, so by step [](#deck){.pf-ref} it is induced by a covering transformation sending $e_0$ to $v$; with the identity, every point of the fibre is sent to every other, which is regularity by Corollary 81.3 (printed p. 489).

:::

:::

::: pf-step

(b) The group of covering transformations is trivial, and the covering is $\boxed{\text{not regular}}$.

::: pf-proof

In Figure 81.5 the vertices are $u$ (carrying the loop $B_3$), $e_0$ and $w$ (carrying the loop $A_3$).
From the arrows, $A_1$ runs from $e_0$ to $u$, $A_2$ from $u$ to $e_0$, $B_2$ from $e_0$ to $w$, and $B_1$ from $w$ to $e_0$.
So $a = (e_0\; u)$ with $w$ fixed, and $b = (e_0\; w)$ with $u$ fixed.
A covering transformation commutes with $b$ by step [](#deck){.pf-ref}, so it maps the unique vertex $u$ fixed by $b$ to itself, and similarly fixes the unique vertex $w$ fixed by $a$; then it fixes $e_0$ and is the identity.
In particular no covering transformation sends $e_0$ to $u$, so the covering is not regular.

:::

:::

::: pf-step

(c) The group of covering transformations is $\ZZ/2$, and the covering is $\boxed{\text{not regular}}$.

::: pf-proof

In Figure 81.6 the four vertices, from left to right, are $u$ (carrying the loop $B_3$), $m$, $e_0$ and $r$ (carrying the loop $B_4$); the $A$-labelled edges join $u$ to $m$ and $e_0$ to $r$, and the $B$-labelled edges join $m$ to $e_0$.
From the arrows, $A_1 \colon m \to u$, $A_2 \colon u \to m$, $B_1 \colon e_0 \to m$, $B_2 \colon m \to e_0$, $A_3 \colon r \to e_0$, $A_4 \colon e_0 \to r$, with $B_3$ a loop at $u$ and $B_4$ a loop at $r$.
So $a = (u\; m)(e_0\; r)$, and $b = (m\; e_0)$ with $u$ and $r$ fixed.
The bijection $\phi = (u\; r)(m\; e_0)$ commutes with $a$ and with $b$: it carries $u \mapsto r$, $m \mapsto e_0$, $e_0 \mapsto m$, $r \mapsto u$, and one checks on the four vertices that $\phi a \phi^{-1} = a$ and $\phi b \phi^{-1} = b$.
A covering transformation commutes with $b$, so it preserves the set $\{u, r\}$ of vertices fixed by $b$; it sends $e_0$ to $e_0$ or to $m = b \cdot e_0$. If $h(e_0) = e_0$, commutation with $b$ gives $h(m) = m$, then $h(r) = h(a \cdot e_0) = a \cdot e_0 = r$ and $h(u) = u$, so $h$ is the identity; if $h(e_0) = m$, then $h(m) = b \cdot m = e_0$, $h(r) = a \cdot m = u$ and $h(u) = a \cdot e_0 = r$, so $h = \phi$. Hence the group is $\{\id, h_\phi\} \cong \ZZ/2$ by step [](#deck){.pf-ref}.
No covering transformation sends $e_0$ to $u$, so the covering is not regular.

:::

:::

::: pf-step

(d) The group of covering transformations is $\ZZ$, and the covering is $\boxed{\text{regular}}$.

::: pf-proof

In Figure 81.7 the vertices are $v_n$, $n \in \ZZ$, with $e_0 = v_0$; the arc $A_n$ runs from $v_n$ to $v_{n+1}$ and $B_n$ is a loop at $v_n$.
So $a \cdot v_n = v_{n+1}$ and $b \cdot v_n = v_n$.
For each $k \in \ZZ$ the translation $v_n \mapsto v_{n+k}$ commutes with $a$ and $b$, so by step [](#deck){.pf-ref} it is induced by a covering transformation $t_k$, and $k \mapsto t_k$ is a homomorphism.
Every covering transformation is determined by the image $v_k$ of $v_0$, so it equals $t_k$; hence the group is $\ZZ$, and it sends $v_0$ to every vertex, so the covering is regular by Corollary 81.3 (printed p. 489).

:::

:::

:::

:::
