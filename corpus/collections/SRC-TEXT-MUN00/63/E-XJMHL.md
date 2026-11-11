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
    asserted the arc-attachment count and is replaced. Part (a) follows the exercise's hint, the path being taken in $S^2-h(\overline S_c)$ for some $c$. Its step bounding the auxiliary
    parameter c is now proved from Theorem 26.9 (the finite intersection property characterisation of
    compactness, printed p. 169) applied to the nested closed sets P(I) cap D_c inside the compact space P(I),
    with D_c closed by Theorem 26.5 and Theorem 26.3, and with the intersection of the whole family computed as
    C_0 from the injectivity of the homeomorphism h; the existence of the path and of its path-component is
    Theorem 63.2 with Theorem 25.5. The closing step is no longer taken from the hint: it is the argument of the second
    proof of Theorem 63.2 (printed pp. 389--390), run with D_1 = D_c and D_2 = A_c, which concludes through
    Theorem 63.1(a) (printed p. 385) that a certain loop class generates an infinite cyclic subgroup of the
    fundamental group of S^2 minus the single point D_c cap A_c. That point is that the book prints Theorem
    63.3 (printed p. 390) in the setwise form, "neither D_i separates S^2", which would require D_c not to
    separate S^2 and so would be circular here; the pointwise form, "a and b joinable in S^2 - D_1 and in
    S^2 - D_2 implies joinable in S^2 - (D_1 cap D_2)", is the statement actually proved on pp. 389--390, and
    the remark on p. 390 states that its argument uses only closedness and the simple connectivity of
    S^2 - D_1 cap D_2. Hypotheses checked on the card: D_c and A_c compact images under h hence closed; D_c cap
    A_c a single point p with S^2 - p homeomorphic to R^2 (stereographic projection, printed p. 377) and
    contractible; a and b joined in S^2 - D_c by the path P; A_c an arc, hence nonseparating by Theorem 63.2. Checked against Theorem 63.2
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
The set $C_0$ is an arc, being $h$ applied to the interval $\{0\}\times[-1,1]$, so by Theorem 63.2 (printed p. 389) it does not separate $S^2$; the set $S^2-C_0$ is open in $S^2$ and hence locally path connected, so by Theorem 25.5 (printed p. 161) its components and path components coincide, and $S^2-C_0$ is path connected. Given $a,b\in S^2-D$, choose a path $\sigma:I\to S^2-C_0$ from $a$ to $b$.

For some $c_0>0$ the path also misses $D_{c_0}$. Each $D_c$ is the image under the continuous map $h$ of the compact set $\overline S\cap\{x\le c\}$, hence compact (Theorem 26.5, printed p. 166) and closed in the Hausdorff space $S^2$ (Theorem 26.3, printed p. 165). The family is nested, $D_c\subseteq D_{c'}$ whenever $c\le c'$, and

$$
\bigcap_{c>0}D_c=h\Bigl(\bigcap_{c>0}\bigl(\overline S\cap\{x\le c\}\bigr)\Bigr)=h(\{0\}\times[-1,1])=C_0,
$$

the middle equality because $h$ is injective. Suppose that $\sigma(I)\cap D_c\ne\emptyset$ for every $c>0$; then the family of closed subsets $\sigma(I)\cap D_c$ of the compact space $\sigma(I)$ has the finite intersection property, since any finite subcollection has intersection $\sigma(I)\cap D_{c_{\min}}$, nonempty by assumption. Theorem 26.9 (printed p. 169) then gives a point of $\bigcap_{c>0}(\sigma(I)\cap D_c)=\sigma(I)\cap C_0$, contradicting $\sigma(I)\subseteq S^2-C_0$. So $\sigma(I)\cap D_{c_0}=\emptyset$ for some $c_0>0$.

The tail
$$
A_c=h\bigl(\{(x,\sin(1/x)):c\le x\le1\}\bigr)
$$
is an arc, being the image under $h$ of the interval $[c,1]$, and $D=D_c\cup A_c$ with $D_c\cap A_c=\theset{p}$ for the single point $p=h(c,\sin(1/c))$.

It remains to pass from the path $\sigma$ in $S^2-D_c$ to a path in $S^2-D$. This is the argument of the second proof of Theorem 63.2 (printed pp. 389--390), whose remark on printed p. 390 identifies the only properties of the two sets that the argument uses: that they are closed subsets of $S^2$, and that $S^2$ minus their intersection is simply connected. Both hold here, with $D_1=D_c$ and $D_2=A_c$. Suppose that $a$ and $b$ cannot be joined by a path in $S^2-D$; put $X=S^2-\theset{p}$, $U=S^2-D_c$, $V=S^2-A_c$. These are open in $S^2$, and $X=U\cup V$ while $U\cap V=S^2-D$. The space $X$ is homeomorphic to $\RR^2$ by a rotation followed by stereographic projection (printed p. 377), and $\RR^2$ is contractible — the straight-line homotopy $H(x,t)=(1-t)x+tx_0$ stays in $\RR^2$ — so $\pi_1(X,a)$ is trivial. The set $U\cap V$ is open in $S^2$, hence locally path connected, so by Theorem 25.4 (printed p. 161) its path components are open in $U\cap V$ and therefore in $X$; let $A$ be the path component of $a$ and $B$ the union of the remaining path components, so that $U\cap V=A\cup B$ is the union of two disjoint open sets with $a\in A$ and $b\in B$. Now $a$ and $b$ are joined by a path in $U$, namely $\sigma$, and by a path in $V$: since $A_c$ is an arc, Theorem 63.2 (printed p. 389) says it does not separate $S^2$, so $S^2-A_c$ is connected, open and locally path connected, hence path connected by Theorem 25.5 (printed p. 161). Theorem 63.1 (printed p. 385) then gives that the path-homotopy class of the loop $\alpha*\beta$ generates an infinite cyclic subgroup of $\pi_1(X,a)$, which is impossible in a trivial group. So $a$ and $b$ are joined by a path in $S^2-D$. As $a$ and $b$ were arbitrary points of $S^2-D$ and that set is open in $S^2$, hence locally path connected, $S^2-D$ is path connected (Theorem 25.5, printed p. 161). Hence $D$ does not separate $S^2$.

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
