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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.5, printed pp. 266--268** (`tmp/sources/munkres-solutions-whitman.pdf`); all four parts are his. In (d) the continuity of the induced multiplication and inversion is stated below in the form that Theorem 22.2 gives it, which is the step his bookkeeping sets up.

Let $H$ be a subgroup of the topological group $G$ with identity $e$, let $G/H=\{xH\mid x\in G\}$ be the set of left cosets, and let $p:G\to G/H$ be the quotient map. Recall $e\in H$ and $x\in xH$.

(a) For $\alpha\in G$ let $f_{\alpha}(x)=\alpha x$ (a homeomorphism, Exercise TG.4) and define $h_{\alpha}:G/H\to G/H$ by $h_{\alpha}(xH)=f_{\alpha}(x)H$.

It is well defined: if $xH=yH$ then $y=xh$ with $h\in H$, so $f_{\alpha}(y)=\alpha xh=f_{\alpha}(x)h\in f_{\alpha}(x)H$ and hence $f_{\alpha}(y)H=f_{\alpha}(x)H$.

It is a bijection: $h_{\alpha}(xH)=h_{\alpha}(yH)$ gives $f_{\alpha}(x)\in f_{\alpha}(y)H$, say $f_{\alpha}(x)=f_{\alpha}(y)h$, and injectivity of $f_{\alpha}$ gives $x=yh\in yH$, so $xH=yH$; and for $yH\in G/H$ pick $x$ with $f_{\alpha}(x)=y$, then $h_{\alpha}(xH)=yH$.

It is a homeomorphism: for a collection $\mathcal{U}$ of cosets one has $h_{\alpha}\big(\bigcup\mathcal{U}\big)=f_{\alpha}\big(\bigcup\mathcal{U}\big)$, and a union of cosets is open in $G/H$ exactly when its preimage in $G$ is open, so $h_{\alpha}(\mathcal{U})$ is open in $G/H$ exactly when $\bigcup\mathcal{U}$ is open in $G$, exactly when $f_{\alpha}(\bigcup\mathcal{U})$ is open in $G$; this is the criterion for a bijection of quotient spaces to be a homeomorphism.

$G/H$ is homogeneous: given $xH,yH$, take $\alpha=yx^{-1}$; then $h_{\alpha}(xH)=yx^{-1}xH=yH$.

(b) If $H$ is closed in $G$ then $p^{-1}(\{H\})=H$ is closed, so the point $H$ is closed in $G/H$; and every other point $xH$ is the image of $H$ under the homeomorphism $h_{x}$ of (a), hence closed. So one-point sets are closed.

(c) For $U$ open in $G$,
$$
p^{-1}\big(p(U)\big)=\bigcup_{h\in H}g_{h}(U),
$$
where $g_{h}(x)=xh$ is a homeomorphism (Exercise TG.4): $x\in p^{-1}(p(U))$ means $xH=yH$ for some $y\in U$, i.e. $x=yh$ with $h\in H$, i.e. $x\in g_{h}(U)$. Each $g_{h}(U)$ is open, so $p^{-1}(p(U))$ is open, and $p(U)$ is open in $G/H$ because $p$ is a quotient map. So $p$ is an open map.

(d) Let $H$ be closed and normal. The set $G/H$ is a group under $(xH)(yH)=(xy)H$: this is well defined because $H$ is normal — if $x'=xh$, $y'=yk$ then $x'y'=xy\,(y^{-1}hy)k\in xyH$ — and the axioms follow from those of $G$, with identity $H$ and inverse $x^{-1}H$. By (b) one-point sets are closed, so $G/H$ is $T_{1}$.

*Continuity of the operations.* Let $m:G\times G\to G$ be multiplication. The composite $m\circ(p\times p):G\times G\to G/H$ is constant on the fibres of the quotient map $p\times p$ (which is a quotient map because $p$ is open, §22), so by Theorem 22.2 it induces a map $G/H\times G/H\to G/H$, namely $m'(xH,yH)=m(x,y)H=(xy)H$; and $m'$ is continuous by that theorem. The inversion $\iota:G\to G$ is continuous, and $\iota\circ p=p\circ\iota'$ for the map $\iota'(xH)=x^{-1}H$ of $G/H$, so by Theorem 22.2 again $\iota'$ is continuous. Hence $G/H$ is a topological group.
:::
