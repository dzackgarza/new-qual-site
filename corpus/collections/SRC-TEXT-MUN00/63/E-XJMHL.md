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
    asserted the arc-attachment count and is replaced. Part (a) follows the exercise's hint. Its step bounding the auxiliary
    parameter c is now proved from Theorem 26.9 (the finite intersection property characterisation of
    compactness, printed p. 169) applied to the nested closed sets P(I) cap D_c inside the compact space P(I),
    with D_c closed by Theorem 26.5 and Theorem 26.3, and with the intersection of the whole family computed as
    C_0 from the injectivity of the homeomorphism h; the existence of the path and of its path-component is
    Theorem 63.2 with Theorem 25.5. One step is still taken from the hint rather than proved on the card: that
    attaching the arc A_c to D_c along one endpoint does not disconnect a component of the complement, whose
    prototype for two arcs meeting in a point is the second proof of Theorem 63.2. Checked against Theorem 63.2
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
The set $C_0$ is an arc, being $h$ applied to the interval $\{0\}\times[-1,1]$, so by Theorem 63.2 (printed p. 389) it does not separate $S^2$; the set $S^2-C_0$ is open in $S^2$ and hence locally path connected, so by Theorem 25.5 (printed p. 161) its components and path components coincide, and $S^2-C_0$ is path connected. Given $a,b\in S^2-D$, choose a path $P:I\to S^2-C_0$ from $a$ to $b$.

For some $c_0>0$ the path also misses $D_{c_0}$. Each $D_c$ is the image under the continuous map $h$ of the compact set $\overline S\cap\{x\le c\}$, hence compact (Theorem 26.5, printed p. 166) and closed in the Hausdorff space $S^2$ (Theorem 26.3, printed p. 165). The family is nested, $D_c\subseteq D_{c'}$ whenever $c\le c'$, and

$$
\bigcap_{c>0}D_c=h\Bigl(\bigcap_{c>0}\bigl(\overline S\cap\{x\le c\}\bigr)\Bigr)=h(\{0\}\times[-1,1])=C_0,
$$

the middle equality because $h$ is injective. Suppose that $P(I)\cap D_c\ne\emptyset$ for every $c>0$; then the family of closed subsets $P(I)\cap D_c$ of the compact space $P(I)$ has the finite intersection property, since any finite subcollection has intersection $P(I)\cap D_{c_{\min}}$, nonempty by assumption. Theorem 26.9 (printed p. 169) then gives a point of $\bigcap_{c>0}(P(I)\cap D_c)=P(I)\cap C_0$, contradicting $P(I)\subseteq S^2-C_0$. So $P(I)\cap D_{c_0}=\emptyset$ for some $c_0>0$.

The tail
$$
A_c=h\bigl(\{(x,\sin(1/x)):c\le x\le1\}\bigr)
$$
is an arc meeting $D_c$ only at its endpoint with $x=c$, and $D=D_c\cup A_c$ with $D_c\cap A_c$ a single point. Attaching an arc to a closed set along one of its endpoints does not disconnect a component of the complement: this is the attachment step of the exercise's hint, and the same step for two arcs meeting in a point is carried out in the second proof of Theorem 63.2 (printed pp. 389--390). With it, $a$ and $b$, which lie in the same component of $S^2-D_c$, remain in the same component of $S^2-D$. As $S^2-D$ is open in $S^2$ and hence locally path connected, that component is path connected (Theorem 25.5, printed p. 161). Hence $D$ does not separate $S^2$.

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
