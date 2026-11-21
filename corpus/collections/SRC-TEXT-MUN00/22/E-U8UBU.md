---
schema: qual/card@1
id: E-U8UBU
kind: problem
title: Coset spaces of topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Supplementary Exercise 5, printed p. 146,
    with Theorem 22.2 and Corollary 22.3; the four parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise TG.5, printed pp.
    266-268. All four parts are his: the induced map on cosets is a well-defined bijection
    and a homeomorphism by the quotient criterion, points are closed when H is closed by
    transporting the class of H along the induced homeomorphisms, the quotient map is open
    because the preimage of p(U) is the union of the translates U h, and for closed normal H
    the group structure on G/H is well defined and its operations are continuous by Theorem
    22.2 applied to p x p. (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: one step per part, following the retained solution
    (Whitman, Exercise TG.5, printed pp. 266-268), which was re-read for the left-coset conventions of this
    card. The arguments and conclusions are his.
---

::: {.exercise}

Let $H$ be a subgroup of the topological group $G$.
If $x \in G$, define $xH = \theset{x \cdot h \mid h \in H}$; this set is called a left coset of $H$ in $G$.
Let $G/H$ denote the collection of left cosets of $H$ in $G$; it is a partition of $G$.
Give $G/H$ the quotient topology.

(a) Show that if $\alpha \in G$, the map $f_\alpha(x) = \alpha \cdot x$ induces a homeomorphism of $G/H$ carrying $xH$ to $(\alpha \cdot x)H$.
Conclude that $G/H$ is a homogeneous space.

(b) Show that if $H$ is a closed set in the topology of $G$, then one-point sets are closed in $G/H$.

(c) Show that the quotient map $p: G \to G/H$ is open.

(d) Show that if $H$ is closed in the topology of $G$ and is a normal subgroup of $G$, then $G/H$ is a topological group.
:::

::: {.solution}
The retained solution set is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.5** (`tmp/sources/munkres-solutions-whitman.pdf`), which treats all four parts; the steps below are its arguments, with the left-coset conventions of this card. Write $p:G\to G/H$ for the quotient map.

::: pf

::: {.pf-step #alpha}
(a) For $\alpha\in G$ the map $f_{\alpha}(x)=\alpha x$ induces a homeomorphism of $G/H$ carrying $xH$ to $(\alpha x)H$, so $G/H$ is homogeneous.

::: pf-proof
Left multiplication $L_{\alpha}:G\to G$ is a homeomorphism of $G$, with inverse $L_{\alpha^{-1}}$. It sends the coset $xH$ onto $(\alpha x)H$: indeed $L_{\alpha}(xh)=\alpha xh\in(\alpha x)H$, and conversely $\alpha xh=L_{\alpha}(xh)$. So $L_{\alpha}$ carries cosets to cosets, and it is a bijection of the set of cosets; hence it induces a well-defined bijection $f_{\alpha}$ of $G/H$ with $f_{\alpha}\circ p=p\circ L_{\alpha}$. Since $p$ is a quotient map and $p\circ L_{\alpha}$ is continuous, $f_{\alpha}$ is continuous, and applying the same to $L_{\alpha^{-1}}$ gives the continuous inverse. Thus $f_{\alpha}$ is a homeomorphism. Homogeneity is the assertion that for any two cosets $xH,yH$ some homeomorphism carries one to the other: take $\alpha=yx^{-1}$, so that $f_{\alpha}(xH)=(\alpha x)H=yH$.
:::

:::

::: {.pf-step #closed-points}
(b) If $H$ is closed in $G$ then singletons are closed in $G/H$.

::: pf-proof
The singleton $\{xH\}$ of the quotient equals $p(xH)$, the image of the coset $xH$ under the quotient map. The coset $xH=L_{x}(H)$ is closed, being the image of the closed set $H$ under the homeomorphism $L_{x}$. A set $A\subseteq G$ that is closed and saturated has closed image: $p^{-1}(p(A))=A$ by saturation, and $p(A)$ is closed exactly when its preimage is, by the defining property of the quotient topology. The coset $xH$ is closed and saturated, being a union of cosets, so $p(xH)=\{xH\}$ is closed.
:::

:::

::: {.pf-step #open}
(c) The quotient map $p:G\to G/H$ is open.

::: pf-proof
Let $U\subseteq G$ be open. Then $p^{-1}(p(U))=\bigcup_{h\in H}Uh$, and each $Uh=R_{h}(U)$ is open because right multiplication $R_{h}$ is a homeomorphism of $G$; so $p^{-1}(p(U))$ is open. Since $p$ is a quotient map, a set in $G/H$ is open exactly when its preimage is open, so $p(U)$ is open. Hence $p$ carries open sets to open sets.
:::

:::

::: {.pf-step}
(d) If $H$ is closed and normal, then $G/H$ is a topological group.

::: pf-proof
Normality makes $G/H$ a group with multiplication $(xH)(yH)=(xy)H$ and inverse $(xH)^{-1}=x^{-1}H$, well defined by the normality of $H$; by (b) singletons are closed since $H$ is closed. The multiplication map $G/H\times G/H\to G/H$ is the map induced on quotients by the continuous multiplication $G\times G\to G$, and $p\times p:G\times G\to G/H\times G/H$ is a quotient map because $p$ is an open quotient map by (c) and the product of open quotient maps is a quotient map; the induced multiplication composed with $p\times p$ equals $p$ composed with the multiplication of $G$, which is continuous, so the quotient criterion gives continuity of the induced multiplication. Likewise inversion on $G/H$ is induced by the continuous inversion of $G$. So the group operations are continuous and $G/H$ is a topological group.
:::

:::

:::
:::
