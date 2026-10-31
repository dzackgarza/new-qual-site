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
By part (a), $D$ is closed and connected and $S^2-D$ has one component. The arc-attachment result proved earlier in this section says that adjoining an arc whose intersection with a closed connected set consists exactly of the two endpoints increases the number of complementary components by one. Hence
$$
S^2-C=S^2-(D\cup Q)
$$
has exactly two components; call them $U$ and $V$.

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
