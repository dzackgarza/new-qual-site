---
schema: qual/card@1
id: E-KZUFG
kind: problem
title: Covering maps of topological groups lift the group structure
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 79 Exercise 6, printed pp. 483--484. The lifted multiplication, identity and inverse by uniqueness of based lifts, then associativity, then uniqueness of the group structure. Checked part by part against the printed parts (a) to (e), with the lifting criterion of Theorem 79.1. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Every step now cites Munkres by number and page: Lemma 79.1 (printed p. 478) for existence and uniqueness of based lifts, Theorem 60.1 (printed p. 371) for pi_1 of a product, the definition of a topological group in the supplementary exercises of §22 (printed p. 145), and the Convention of Chapter 13 (printed p. 477). Corrected: part (a) justified the lifting criterion by the assertion that pi_1(G,e) is abelian and that m_* is "addition", which is neither a numbered result of the book nor needed; the computation is now the group-theoretic one, p_*(pi_1 of the product) = H x H and m_* of an ordered pair of classes is their product, so the image of pi_1(G x G) is H*H = H because H is a subgroup, and the image of pi_1(G) under I o p is H^{-1} = H. Nothing in the proof now uses commutativity. What the certificate does not cover: the continuity of m and I is the definition of a topological group, not re-proved on the card.
---

::: {.exercise}

Prove the following.

Theorem.
Let $G$ be a topological group with multiplication operation $m: G \times G \to G$ and identity element $e$.
Assume $p: \overline{G} \to G$ is a covering map.
Given $\tilde{e}$ with $p(\tilde{e}) = e$, there is a unique multiplication operation on $\overline{G}$ that makes it into a topological group such that $\tilde{e}$ is the identity element and $p$ is a homomorphism.

(a) Let $I: G \to G$ be the map $I(g) = g^{-1}$.
Show there exist unique maps $\overline{m}: \overline{G} \times \overline{G} \to \overline{G}$ and $\overline{I}: \overline{G} \to \overline{G}$ with $\overline{m}(\tilde{e} \times \tilde{e}) = \tilde{e}$ and $\overline{I}(\tilde{e}) = \tilde{e}$ such that $p \circ \overline{m} = m \circ (p \times p)$ and $p \circ \overline{I} = I \circ p$.

(b) Show the maps $\overline{G} \to \overline{G}$ given by $\tilde{g} \to \overline{m}(\tilde{e} \times \tilde{g})$ and $\tilde{g} \to \overline{m}(\tilde{g} \times \tilde{e})$ equal the identity map of $\overline{G}$.
[Hint: Use the uniqueness part of Lemma 79.1.]

(c) Show the maps $\overline{G} \to \overline{G}$ given by $\tilde{g} \to \overline{m}(\tilde{g} \times \overline{I}(\tilde{g}))$ and $\tilde{g} \to \overline{m}(\overline{I}(\tilde{g}) \times \tilde{g})$ map $\overline{G}$ to $\tilde{e}$.

(d) Show the maps $\overline{G} \times \overline{G} \times \overline{G} \to \overline{G}$ given by

$$
\tilde{g} \times \tilde{g}' \times \tilde{g}'' \to \overline{m}(\tilde{g} \times \overline{m}(\tilde{g}' \times \tilde{g}''))
$$

$$
\tilde{g} \times \tilde{g}' \times \tilde{g}'' \to \overline{m}(\overline{m}(\tilde{g} \times \tilde{g}') \times \tilde{g}'')
$$

are equal.

(e) Complete the proof.
:::

::: {.solution}
By the Convention of Chapter 13 (printed p. 477), $\overline{G}$ and $G$ are path connected and locally path connected; a product of finitely many such spaces is again path connected and locally path connected, a path being given coordinatewise. The multiplication $m$ and the inversion $I$ are continuous by the definition of a topological group (supplementary exercises of §22, printed p. 145).

Put
$$
H=p_*\pi_1(\overline G,\tilde e)\le\pi_1(G,e).
$$
By Theorem 60.1 (printed p. 371) the inclusions of the two factors induce an isomorphism $\pi_1(\overline G,\tilde e)\times\pi_1(\overline G,\tilde e)\cong\pi_1(\overline G\times\overline G,(\tilde e,\tilde e))$, and under it $(p\times p)_*$ has image $H\times H$, while $m_*$ carries the pair $(u,v)$ to the product $u\cdot v$. Since $H$ is a subgroup, $H\cdot H=H$, and since $H$ is closed under inverses, $I_*(H)=H^{-1}=H$.

(a) The maps $m\circ(p\times p):\overline G\times\overline G\to G$ and $I\circ p:\overline G\to G$ carry the respective base points to $e$. By the computation above,
$$
(m\circ(p\times p))_*\pi_1(\overline G\times\overline G,(\tilde e,\tilde e))=H\cdot H=H=p_*\pi_1(\overline G,\tilde e),
$$
and $(I\circ p)_*\pi_1(\overline G,\tilde e)=H^{-1}=H$. The lifting criterion of Lemma 79.1 (printed p. 478) and its uniqueness assertion therefore give unique maps $\overline m:\overline G\times\overline G\to\overline G$ and $\overline I:\overline G\to\overline G$ with
$$
p\circ\overline m=m\circ(p\times p),\qquad \overline I(\tilde e)=\tilde e,\qquad p\circ\overline I=I\circ p,\qquad \overline m(\tilde e,\tilde e)=\tilde e .
$$

(b) Define $L(\tilde g)=\overline m(\tilde e,\tilde g)$ and $R(\tilde g)=\overline m(\tilde g,\tilde e)$. Then
$$
pL(\tilde g)=m(e,p\tilde g)=p\tilde g,\qquad pR(\tilde g)=m(p\tilde g,e)=p\tilde g,
$$
so $L$ and $R$ both lift $p$ and both send $\tilde e$ to $\overline m(\tilde e,\tilde e)=\tilde e$; the identity map of $\overline G$ is a third such lift. By the uniqueness part of Lemma 79.1 (printed p. 478), $L=R=1_{\overline G}$. So $\tilde e$ is a two-sided identity for $\overline m$.

(c) For $A(\tilde g)=\overline m(\tilde g,\overline I(\tilde g))$ and $B(\tilde g)=\overline m(\overline I(\tilde g),\tilde g)$,
$$
pA(\tilde g)=p\tilde g\cdot(p\tilde g)^{-1}=e,\qquad pB(\tilde g)=(p\tilde g)^{-1}\cdot p\tilde g=e,
$$
so $A$ and $B$ both lift the constant map $\overline G\to\{e\}$, and $A(\tilde e)=B(\tilde e)=\overline m(\tilde e,\tilde e)=\tilde e$. The constant map $\tilde g\mapsto\tilde e$ is such a lift, so by Lemma 79.1 (printed p. 478), $A=B\equiv\tilde e$. Thus $\overline I$ gives two-sided inverses.

(d) Let
$$
F(\tilde g,\tilde g',\tilde g'')=\overline m(\tilde g,\overline m(\tilde g',\tilde g'')),\qquad
F'(\tilde g,\tilde g',\tilde g'')=\overline m(\overline m(\tilde g,\tilde g'),\tilde g'').
$$
Their projections to $G$ agree, by associativity of the multiplication in $G$:
$$
pF=p\tilde g\cdot(p\tilde g'\cdot p\tilde g'')=(p\tilde g\cdot p\tilde g')\cdot p\tilde g''=pF',
$$
and both send $(\tilde e,\tilde e,\tilde e)$ to $\tilde e$. So $F$ and $F'$ are two based lifts of the same map out of the path connected and locally path connected space $\overline G\times\overline G\times\overline G$, and Lemma 79.1 (printed p. 478) gives $F=F'$, that is, $\overline m$ is associative.

(e) Parts (b), (c) and (d) show that $\overline m$ is an associative multiplication on $\overline G$ with two-sided identity $\tilde e$ and two-sided inverses $\overline I$, that is, a group structure; $\overline m$ and $\overline I$ are continuous by construction, so $(\overline G,\overline m,\overline I,\tilde e)$ is a topological group. By construction,
$$
p(\overline m(x,y))=p(x)p(y),\qquad p(\overline I(x))=p(x)^{-1},
$$
so $p$ is a continuous group homomorphism.

For uniqueness, let $m'$ be any multiplication on $\overline G$ making $\tilde e$ the identity and $p$ a homomorphism. Then $p\circ m'=m\circ(p\times p)$ and $m'(\tilde e,\tilde e)=\tilde e$, so $m'$ is a based lift of $m\circ(p\times p)$, hence $m'=\overline m$ by Lemma 79.1.
:::
