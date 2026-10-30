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
A covering transformation is a homeomorphism $h \colon E \to E$ with $p \circ h = p$, and the covering is regular when for every two points $e, e'$ of $p^{-1}(x_0)$ some covering transformation sends $e$ to $e'$.
The figures were read from Munkres, *Topology*, 2nd ed., p. 492–493.

::: pf

::: {.pf-step #covering}
In each figure $p$ is a covering map.

::: pf-proof
In each figure every vertex has exactly one incoming and one outgoing edge of each label, counting a loop as both.
So a small open star of each vertex maps homeomorphically onto a small open star $W$ of $x_0$, and $p^{-1}(W)$ is the disjoint union of these stars.
A point interior to $A$ or $B$ has an open arc as neighbourhood whose preimage is a disjoint union of open arcs, one in each edge with that label, each mapped homeomorphically.
:::

:::

::: {.pf-step #deck}
A covering transformation $h$ permutes the vertices, satisfies $h(a \cdot v) = a \cdot h(v)$ and $h(b \cdot v) = b \cdot h(v)$, and is determined by $h(e_0)$.
Conversely, a bijection $\phi$ of the vertices commuting with $a \cdot$ and $b \cdot$ is induced by a covering transformation.

::: pf-proof
Since $p h = p$, $h$ preserves $p^{-1}(x_0)$.
If $\tilde\gamma$ is the lift of the loop $A$ starting at $v$, then $h \circ \tilde\gamma$ is a lift of $A$ starting at $h(v)$, so by uniqueness of path lifting it ends at $a \cdot h(v)$; likewise for $b$.
Two covering transformations that agree at $e_0$ are lifts of $p$ agreeing at a point of the connected space $E$, hence equal.
For the converse, $\phi$ carries the $A$-edge from $v$ to $a \cdot v$ to the $A$-edge from $\phi(v)$ to $a \cdot \phi(v)$, and similarly for $B$; define $h$ on each closed edge $e$ as $(p\restrict_{e'})^{-1} \circ p\restrict_e$ on its interior, where $e'$ is the image edge, and as $\phi$ on vertices.
Then $h$ is a homeomorphism with $p h = p$.
:::

:::

::: pf-step
(a) $p$ is a regular covering, with group of covering transformations $\ZZ/2$.

::: pf-proof
The vertices are $e_0$ and the other vertex $v$ of the circle $A_1 \cup A_2$; $A_1$ runs from $e_0$ to $v$ and $A_2$ from $v$ to $e_0$, and $B_1$, $B_2$ are loops at $v$, $e_0$.
So $a$ swaps $e_0$ and $v$, and $b$ fixes both.
The swap $e_0 \leftrightarrow v$ commutes with $a$ and $b$, so by step [](#deck){.pf-ref} it is induced by a covering transformation sending $e_0$ to $v$; with the identity, every point of the fibre is sent to every other.
:::

:::

::: pf-step
(b) The group of covering transformations is trivial, and the covering is $\boxed{\text{not regular}}$.

::: pf-proof
Let $u$ be the vertex carrying the loop $B_3$ and $w$ the vertex carrying the loop $A_3$.
From the arrows, $A_1$ runs from $e_0$ to $u$, $A_2$ from $u$ to $e_0$, $B_2$ from $e_0$ to $w$, and $B_1$ from $w$ to $e_0$.
So $a = (e_0\; u)$ with $w$ fixed, and $b = (e_0\; w)$ with $u$ fixed.
A covering transformation commutes with $b$ by step [](#deck){.pf-ref}, so it maps the unique vertex $u$ fixed by $b$ to itself, and similarly fixes the unique vertex $w$ fixed by $a$; then it fixes $e_0$ and is the identity.
In particular no covering transformation sends $e_0$ to $u$.
:::

:::

::: pf-step
(c) The group of covering transformations is $\ZZ/2$, and the covering is $\boxed{\text{not regular}}$.

::: pf-proof
Label the vertices from left to right $u$, $e_0$, $m$, $r$, with loops $B_3$ at $u$ and $B_4$ at $r$.
From the arrows, $A_1 \colon e_0 \to u$, $A_2 \colon u \to e_0$, $B_2 \colon e_0 \to m$, $B_1 \colon m \to e_0$, $A_4 \colon m \to r$, $A_3 \colon r \to m$.
So $a = (e_0\; u)(m\; r)$ and $b = (e_0\; m)$ with $u$, $r$ fixed.
The bijection $\phi = (e_0\; m)(u\; r)$ commutes with $a$ and with $b$, as both are products of disjoint transpositions that $\phi$ permutes among themselves.
A covering transformation commutes with $b$, so it preserves the set $\{u, r\}$ of vertices fixed by $b$ and sends $e_0$ to $e_0$ or $m$; by step [](#deck){.pf-ref} the group is $\{\id, h_\phi\} \cong \ZZ/2$.
No covering transformation sends $e_0$ to $u$, so the covering is not regular.
:::

:::

::: pf-step
(d) The group of covering transformations is $\ZZ$, and the covering is $\boxed{\text{regular}}$.

::: pf-proof
The vertices are $v_n$, $n \in \ZZ$, with $e_0 = v_0$; $A_n$ runs from $v_n$ to $v_{n+1}$ and $B_n$ is a loop at $v_n$.
So $a \cdot v_n = v_{n+1}$ and $b \cdot v_n = v_n$.
For each $k \in \ZZ$ the translation $v_n \mapsto v_{n+k}$ commutes with $a$ and $b$, so by step [](#deck){.pf-ref} it is induced by a covering transformation $t_k$, and $k \mapsto t_k$ is a homomorphism.
Every covering transformation is determined by the image $v_k$ of $v_0$, so it equals $t_k$; hence the group is $\ZZ$, and it sends $v_0$ to every vertex, so the covering is regular.
:::

:::

:::

:::
