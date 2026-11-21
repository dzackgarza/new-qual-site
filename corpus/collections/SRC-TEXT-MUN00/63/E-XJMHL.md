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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §63 Exercise 3, printed p. 393. Searched outside the checkout for issue #144 on the orchestrator's
    machine, recorded in tmp/sources/mse-searches-144.md; no thread on part (a) was saved because no question on it
    was found. The queries were "topologist's sine curve does not separate", "topologist's sine curve sphere
    complement", "topologist's sine curve complement connected", "does not separate S^2" and the /similar query of
    the exercise's statement. For part (b) the record points to the thread of E-LP6WS,
    tmp/sources/mse-1394696-E-LP6WS.md, whose single answer asserts the two-component conclusion for the Warsaw
    circle through Alexander duality without proving it; that is a source searched, not a proof of part (b), and
    nothing is transcribed. The card's proof is its own, checked on 2026-11-11 against Theorem 63.2, Theorem 63.5,
    Theorem 63.1 and Theorem 26.9 as the note above records; it was not re-read in this pass.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose in two headed parts with no `pf` structure. It is
    now a `pf` with nine steps covering (a) and (b), each carrying a `pf-proof`, and the hints the
    exercise prints are followed. Cited by numbered statement only: Munkres, Topology, §63 Exercise 3,
    Theorem 63.1 (the two-open-sets criterion), Theorem 63.2 (an arc does not separate $S^2$), Theorem
    63.4 (the local disk argument), Theorem 63.5 (two non-separating closed connected sets meeting in
    two points separate $S^2$ into two components), Theorem 25.5, Theorem 26.3, Theorem 26.5 and
    Theorem 26.9, with §59 for the identification $S^2-\{p\}\cong\RR^2$. No retained published set
    reaches §63, and the card's preamble says so and names the search record. Checked: that $h$
    carries the nested compact family to a nested closed family with intersection $C_0$, that the
    finite intersection property applies to $\sigma(I)\cap D_c$, that $D_c\cap A_c$ is the single
    point $p$, that the loop $\alpha*\beta^{-1}$ lies in $X=S^2-\{p\}$ and is null-homotopic there,
    and that $U$ and $V$ are open because components of an open set in a locally connected space are
    open.
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

No retained published solution of Munkres, *Topology*, §63 Exercise 3 was located: the sets searched are listed in the `COMPLAINTS.md` entry for §51--§63 of `SRC-TEXT-MUN00`, and no retained set reaches §63. The proof is the card's own, checked against the numbered statements it cites, and it follows the two hints the exercise prints.

::: pf

::: {.pf-step #setup}
Write $\bar S=\{(x,\sin(1/x)):0<x\le1\}\cup(\{0\}\times[-1,1])$, let $h:\bar S\to D$ be a homeomorphism onto $D\subseteq S^2$, and put $C_0=h(\{0\}\times[-1,1])$ and, for $0<c<1$, $D_c=h(\bar S\cap\{x\le c\})$ and $A_c=h(\{(x,\sin(1/x)):c\le x\le1\})$.

::: pf-proof
These are definitions. $\{0\}\times[-1,1]$ and $\{(x,\sin(1/x)):c\le x\le1\}$ are intervals, hence arcs, and $\bar S$ is the union of the interval and the graph, as in Example 7 of §24.
:::

:::

::: {.pf-step #arcs-do-not-separate}
$C_0$ and each $A_c$ are arcs in $S^2$, so neither separates $S^2$; $S^2-C_0$ is path connected.

::: pf-proof
An arc in $S^2$ does not separate it: Munkres, Theorem 63.2. The complement of an arc is open in $S^2$, and $S^2$ is locally path connected, so that complement is locally path connected and its components are path components (Munkres, Theorem 25.5); it is connected, so it is path connected.
:::

:::

::: {.pf-step #path-to-sigma}
Given $a,b\in S^2-D$ there is a path $\sigma:I\to S^2-C_0$ from $a$ to $b$.

::: pf-proof
$a$ and $b$ lie in $S^2-D\subseteq S^2-C_0$, and $S^2-C_0$ is path connected by step [#arcs-do-not-separate]{.pf-ref}.
:::

:::

::: {.pf-step #misses-small}
The path $\sigma$ misses $D_{c_0}$ for some $c_0>0$.

::: pf-proof
Each $D_c$ is the image under the continuous injection $h$ of the compact set $\bar S\cap\{x\le c\}$, hence compact (Munkres, Theorem 26.5) and closed in the Hausdorff space $S^2$ (Theorem 26.3). The family is nested, and $\bigcap_{c>0}D_c=h\bigl(\bigcap_{c>0}(\bar S\cap\{x\le c\})\bigr)=h(\{0\}\times[-1,1])=C_0$ because $h$ is injective. If $\sigma(I)\cap D_c\ne\varnothing$ for every $c$, the closed subsets $\sigma(I)\cap D_c$ of the compact space $\sigma(I)$ meet in every finite subfamily, since the family is nested, so by the finite intersection property (Munkres, Theorem 26.9) some point of $\sigma(I)$ lies in $\bigcap_cD_c=C_0$, contradicting $\sigma(I)\subseteq S^2-C_0$. So some $c_0>0$ has $\sigma(I)\cap D_{c_0}=\varnothing$.
:::

:::

::: {.pf-step #decomposition}
$D=D_c\cup A_c$ and $D_c\cap A_c$ is the single point $p=h(c,\sin(1/c))$.

::: pf-proof
$\bar S$ is the union of $\bar S\cap\{x\le c\}$ and the graph over $[c,1]$, and these meet exactly in $(c,\sin(1/c))$; applying the injective $h$ gives the claim.
:::

:::

::: {.pf-step #two-closed-sets}
Let $D_1,D_2$ be closed subsets of $S^2$ with $D_1\cap D_2=\{p\}$ and $S^2-\{p\}$ simply connected. If $a,b\notin D_1\cup D_2$ are joined by paths in $S^2-D_1$ and in $S^2-D_2$, then they are joined by a path in $S^2-(D_1\cup D_2)$.

::: pf-proof
Suppose not. Put $X=S^2-\{p\}$, $U=S^2-D_1$, $V=S^2-D_2$; these are open in $S^2$, $X=U\cup V$ and $U\cap V=S^2-(D_1\cup D_2)$. Choose paths $\alpha$ in $U$ and $\beta$ in $V$ from $a$ to $b$ and let $\beta^{-1}$ be $\beta$ reversed; the loop $\alpha*\beta^{-1}$ lies in $X$ and is not null-homotopic, since a null-homotopy would produce a path in $U\cap V$ (Munkres, Theorem 63.1), contradicting the assumption. $X$ is homeomorphic to $\RR^2$ by a rotation followed by stereographic projection (Munkres, §59), and $\RR^2$ is contractible through straight-line homotopies, so $\pi_1(X,a)$ is trivial and every loop in $X$ is null-homotopic. Contradiction.
:::

:::

::: {.pf-step #part-a}
(a) $D$ does not separate $S^2$.

::: pf-proof
By step [#misses-small]{.pf-ref} and step [#decomposition]{.pf-ref}, $a$ and $b$ are joined by $\sigma$ in $S^2-D_{c_0}$ and by a path in $S^2-A_{c_0}$, which is path connected by step [#arcs-do-not-separate]{.pf-ref}. With $D_1=D_{c_0}$ and $D_2=A_{c_0}$, both closed subsets of $S^2$ meeting in the single point $p$, and $S^2-\{p\}\cong\RR^2$ simply connected, step [#two-closed-sets]{.pf-ref} joins $a$ to $b$ in $S^2-D$. As $a,b$ were arbitrary and $S^2-D$ is open and locally path connected, $S^2-D$ is path connected (Munkres, Theorem 25.5), so $D$ does not separate $S^2$.
:::

:::

::: {.pf-step #part-b-separates}
(b) $C$ separates $S^2$ into precisely two components.

::: pf-proof
The closed topologist's sine curve is $\bar S$ together with a broken-line arc $P$ from $(0,-1)$ to $(1,\sin1)$ meeting $\bar S$ exactly in its two endpoints. Let $h$ be the homeomorphism onto $C$ and put $D=h(\bar S)$, $Q=h(P)$. Then $D$ is closed and connected and does not separate $S^2$ by part (a); $Q$ is an arc, closed and connected, and does not separate $S^2$ by Munkres, Theorem 63.2; and $D\cap Q=h(\bar S\cap P)$ consists of two points. Munkres, Theorem 63.5 then says that $D\cup Q=C$ separates $S^2$ into precisely two components, $U$ and $V$.
:::

:::

::: {.pf-step #part-b-boundary}
(b) $\partial U=\partial V=C$.

::: pf-proof
Each point of $C-C_0=h(\bar S)\setminus h(\{0\}\times[-1,1])$ is locally an ordinary point of an embedded arc, and the local argument of the proof of Munkres, Theorem 63.4 applies: a small disk meets $C$ in a single crosscut whose two sides lie in the two distinct components, so $C-C_0\subseteq\partial U\cap\partial V$. Each point of $C_0$ is a limit of points of the oscillating graph and hence of $C-C_0$, and boundaries are closed, so $C_0\subseteq\partial U\cap\partial V$; hence $C\subseteq\partial U\cap\partial V$. Conversely $U$ and $V$ are components of the open set $S^2-C$, which is open and locally connected, so both are open in $S^2$; a point of the open set $S^2-C$ therefore lies in neither boundary, giving $\partial U\cup\partial V\subseteq C$. Hence $\partial U=\partial V=C$.
:::

:::

:::

:::
