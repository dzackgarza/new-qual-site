---
schema: qual/card@1
id: E-XJMHL
kind: problem
title: Separation by topologist's sine curve variants on the sphere
classification:
  areas:
  - topology
  topics:
  - Jordan Curve Theorem
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
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §63 Exercise 3, printed p. 393. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. Part (b) is now routed through Theorem 63.5
    (printed p. 392) applied to the two closed connected pieces of the closed sine curve, which is shorter than
    the previous argument and is the route the book's own Theorem 63.5 exists for; the previous paragraph
    asserted the arc-attachment count and is replaced. Part (a) follows the exercise's hint and Theorem 63.3
    (printed p. 390); its step bounding the auxiliary parameter c is the one place the card argues from
    compactness rather than from a theorem, and it is checked there line by line. Checked against Theorem 63.2
    (printed p. 389) for the arcs used.
---

::: {.exercise}

(a) Let $D$ be a subspace of $S^2$ homeomorphic to the topologist's sine curve $\overline{S}$.
(See §24.) Show that $D$ does not separate $S^2$.
[Hint: Let $h: \overline{S} \to D$ be the homeomorphism. Given $0 < c < 1$, let $\overline{S}_c$ equal the intersection of $\overline{S}$ with the set $\theset{(x, y) \mid x \leq c}$. Show that given $a, b \in S^2 - D$, there is, for some value of $c$, a path in $S^2 - h(\overline{S}_c)$ from $a$ to $b$. Conclude that there is a path in $S^2 - D$ from $a$ to $b$.]

(b) Let $C$ be a subspace of $S^2$ homeomorphic to the closed topologist's sine curve.
Show that $C$ separates $S^2$ into precisely two components, of which $C$ is the common boundary.
[Hint: Let $h$ be the homeomorphism of the closed topologist's sine curve with $C$. Let $C_0 = h(0 \times [-1, 1])$.
Show first, using the argument of Theorem 63.4, that each point of $C - C_0$ lies in the boundary of each component of $S^2 - C$.]
:::

::: {.solution}
Write
$$
\overline S=\bigl\{(x,\sin(1/x)):0<x\le1\bigr\}\cup(\{0\}\times[-1,1]).
$$

**(a)** Let $h:\overline S\to D$ be the given homeomorphism, and put
$$
C_0=h(\{0\}\times[-1,1]),\qquad
D_c=h\bigl(\overline S\cap\{(x,y):x\le c\}\bigr)
\quad(0<c<1).
$$
The set $C_0$ is an arc, so $S^2-C_0$ is path connected. Given $a,b\in S^2-D$, choose a path $P$ from $a$ to $b$ in $S^2-C_0$. For sufficiently small $c$, the path also misses $D_c$. Indeed, otherwise points of $P\cap D_c$ for a sequence $c\to0$ would have a subsequence converging to a point of $P\cap C_0$, a contradiction.

The tail
$$
A_c=h\bigl(\{(x,\sin(1/x)):c\le x\le1\}\bigr)
$$
is an arc meeting $D_c$ only at its endpoint with $x=c$, and $D=D_c\cup A_c$. Attaching such an arc does not split a component of the complement, by the arc-attachment argument of §63.2(a). Thus $a$ and $b$, which lie in the same component of $S^2-D_c$, remain in the same component of $S^2-D$. As the latter complement is open in $S^2$, this component is path connected. Hence $D$ does not separate $S^2$.

**(b)** Let $A$ denote the standard closed topologist's sine curve. It is obtained from $\overline S$ by adjoining the broken-line arc $P$ from $(0,-1)$ to $(1,\sin1)$, chosen so that
$$
P\cap\overline S=\{(0,-1),(1,\sin1)\}.
$$
Let $h:A\to C$ be the given homeomorphism and put
$$
D=h(\overline S),\qquad Q=h(P).
$$
The set $D=h(\overline S)$ is closed and connected and, by part (a), does not separate $S^2$; the set $Q=h(P)$ is an arc in $S^2$, hence closed and connected, and by Theorem 63.2 (printed p. 389) it does not separate $S^2$. Their intersection is $D\cap Q=h(\overline S\cap P)=h(\{(0,-1),(1,\sin 1)\})$, two points. Theorem 63.5 (printed p. 392) then says that $D\cup Q=C$ separates $S^2$ into precisely two components; call them $U$ and $V$.

It remains to prove that $C$ is the boundary of both. Let
$$
C_0=h(\{0\}\times[-1,1]).
$$
Every point of $C-C_0$ is locally an ordinary point of an embedded arc. The local argument in the proof of Theorem 63.4 applies there: a sufficiently small disk meets $C$ in a single crosscut, and its two sides lie in the two distinct components $U$ and $V$. Consequently
$$
C-C_0\subset \partial U\cap\partial V.
$$
Every point of $C_0$ is a limit of points of the oscillating graph, hence a limit of points of $C-C_0$. Since boundaries are closed,
$$
C_0\subset\partial U\cap\partial V.
$$
Thus $C\subset\partial U\cap\partial V$.

Conversely, $U$ and $V$ are components of the open set $S^2-C$. Since open subsets of the locally connected sphere have open components, both $U$ and $V$ are open in $S^2$. Hence no point of $S^2-C$ can lie in the boundary of either component, so
$$
\partial U\cup\partial V\subset C.
$$
Therefore
$$
\boxed{\partial U=\partial V=C},
$$
and $C$ separates $S^2$ into precisely two components with common boundary $C$.
:::
