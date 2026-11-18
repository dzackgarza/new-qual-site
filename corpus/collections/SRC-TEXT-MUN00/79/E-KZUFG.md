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
  date: 2026-11-15
  note: >-
    Munkres §79 Exercise 6(a)-(e), printed pp. 483--484. Searched outside the checkout for issue #146; the
    record is tmp/sources/mse-searches-146.md and the saved threads are tmp/sources/mse-5391-E-KZUFG.md and
    tmp/sources/mse-3967945-E-KZUFG.md, both read whole. Two of the five parts have published proofs and both
    are now named on the card: part (b), the two-sided identity, is Jack Lee's answer 5414 (2010-09-25) to
    question 5391, by comparing the map x -> m(x, e) with the identity as two lifts of p that agree at the
    identity; part (d), associativity, is Jose Carlos Santos' answer 3967971 (2020-12-31) to question 3967945,
    by projecting the two triple products to G and evaluating both at the triple identity. Part (d) is also
    answer 3967979 by Bananach Space in the same thread, phrased through a deck transformation. Parts (a), (c)
    and (e) are in neither thread and stay the card's own. The card's own proofs of (b) and (d) were the same
    arguments; the card now says whose they are and keeps them. Rejected in the search: mse 4879182, a
    different construction of a universal cover that proves only continuity.
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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, one per part, and re-checked each: the image
    computations (p x p)_* = H x H, m_* as the product of classes and (I o p)_* = H^-1, from
    which the lifting criterion of Lemma 79.1 gives the unique based lifts; the identity
    claim by comparing two maps with the same projection; the inverse claim by comparing two
    lifts of the constant map; associativity by comparing the two triple products through p
    and at the base point; and the group axioms, continuity, homomorphism property and
    uniqueness of the multiplication. No repair needed: the card's proof was already
    correct, and the two published arguments it uses are now credited at the steps that use
    them (Jack Lee, MSE 5414; Jose Carlos Santos, MSE 3967971).
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
The proof is the card's own, with two steps drawn from published answers and credited in those steps: the two-sided identity argument is **Jack Lee's, Math Stack Exchange answer 5414**, and the associativity comparison is **José Carlos Santos', answer 3967971**. Nothing else is taken from a retained set; the exercise is the theorem of §79, printed p. 496.

By the Convention of Chapter 13 (printed p. 477), $\overline{G}$ and $G$ are path connected and locally path connected, and a finite product of such spaces is again path connected and locally path connected. The multiplication $m$ and the inversion $I$ are continuous by the definition of a topological group (§22 supplementary exercises, printed p. 145).

::: pf

::: {.pf-step #image}
Put $H=p_{*}\pi_{1}(\overline{G},\tilde{e})\le\pi_{1}(G,e)$. Under the isomorphism $\pi_{1}(\overline{G},\tilde{e})\times\pi_{1}(\overline{G},\tilde{e})\cong\pi_{1}(\overline{G}\times\overline{G},(\tilde{e},\tilde{e}))$ of Theorem 60.1, the image of $(p\times p)_{*}$ is $H\times H$, the map $m_{*}$ sends $(u,v)$ to the product $u\cdot v$, and the image of $(I\circ p)_{*}$ is $H^{-1}$; since $H$ is a subgroup, $H\cdot H=H$ and $H^{-1}=H$.

::: pf-proof
$\pi_{1}$ of a product is the product of the fundamental groups, the inclusions of the factors inducing the isomorphism (Theorem 60.1, printed p. 371); under it $(p\times p)_{*}$ acts coordinatewise as $p_{*}$, so its image is $H\times H$. For classes $u$, $v$ represented by loops $\alpha$, $\beta$ at $e$, the composite $m\circ(\alpha\times\beta)$ is the loop $t\mapsto\alpha(t)\beta(t)$, which is homotopic to the concatenation $\alpha*\beta$ by the standard reparametrization of a product of loops; so $m_{*}(u,v)=u\cdot v$, the product in $\pi_{1}(G,e)$. Similarly $I\circ\alpha$ represents $u^{-1}$. Since $H$ is a subgroup it contains products and inverses of its elements.
:::

:::

::: {.pf-step #part-a}
(a) There are unique maps $\overline{m}:\overline{G}\times\overline{G}\to\overline{G}$ and $\overline{I}:\overline{G}\to\overline{G}$ with $\overline{m}(\tilde{e},\tilde{e})=\tilde{e}$, $\overline{I}(\tilde{e})=\tilde{e}$, $p\circ\overline{m}=m\circ(p\times p)$ and $p\circ\overline{I}=I\circ p$.

::: pf-proof
The map $m\circ(p\times p)$ carries $(\tilde{e},\tilde{e})$ to $m(e,e)=e$, and $I\circ p$ carries $\tilde{e}$ to $I(e)=e$. By step [](#image){.pf-ref},
$$
\big(m\circ(p\times p)\big)_{*}\pi_{1}\big(\overline{G}\times\overline{G},(\tilde{e},\tilde{e})\big)=H\cdot H=H=p_{*}\pi_{1}(\overline{G},\tilde{e}),
\qquad
(I\circ p)_{*}\pi_{1}(\overline{G},\tilde{e})=H^{-1}=H .
$$
The lifting criterion of Lemma 79.1 (printed p. 478) applies to each, since the domains are path connected and locally path connected, and gives based lifts $\overline{m}$ and $\overline{I}$; the uniqueness assertion of the same lemma, again by path connectedness of the domains, gives uniqueness of each lift.
:::

:::

::: {.pf-step #part-b}
(b) $\overline{m}(\tilde{e},\tilde{g})=\overline{m}(\tilde{g},\tilde{e})=\tilde{g}$ for every $\tilde{g}\in\overline{G}$.

::: pf-proof
Let $L(\tilde{g})=\overline{m}(\tilde{e},\tilde{g})$ and $R(\tilde{g})=\overline{m}(\tilde{g},\tilde{e})$. Then $pL(\tilde{g})=m\big(e,p\tilde{g}\big)=p\tilde{g}$ and $pR(\tilde{g})=m\big(p\tilde{g},e\big)=p\tilde{g}$, and $L(\tilde{e})=R(\tilde{e})=\overline{m}(\tilde{e},\tilde{e})=\tilde{e}$; the identity of $\overline{G}$ is a third map with the same projection and the same value at $\tilde{e}$. Two maps with the same projection to $G$ that agree at one point of the path connected space $\overline{G}$ agree everywhere, by the uniqueness part of Lemma 79.1; so $L=R=\mathsf{l}_{\overline{G}}$, that is, $\tilde{e}$ is a two-sided identity. This is Jack Lee's argument, MSE answer 5414.
:::

:::

::: {.pf-step #part-c}
(c) $\overline{m}\big(\tilde{g},\overline{I}(\tilde{g})\big)=\overline{m}\big(\overline{I}(\tilde{g}),\tilde{g}\big)=\tilde{e}$ for every $\tilde{g}$.

::: pf-proof
Put $A(\tilde{g})=\overline{m}\big(\tilde{g},\overline{I}(\tilde{g})\big)$ and $B(\tilde{g})=\overline{m}\big(\overline{I}(\tilde{g}),\tilde{g}\big)$. Then
$$
pA(\tilde{g})=p\tilde{g}\cdot(p\tilde{g})^{-1}=e,\qquad pB(\tilde{g})=(p\tilde{g})^{-1}\cdot p\tilde{g}=e,
$$
so both lift the constant map $\overline{G}\to\{e\}$, and both send $\tilde{e}$ to $\overline{m}\big(\tilde{e},\overline{I}(\tilde{e})\big)=\overline{m}(\tilde{e},\tilde{e})=\tilde{e}$. The constant map $\tilde{g}\mapsto\tilde{e}$ is a third lift, so by Lemma 79.1 all three agree: $A=B\equiv\tilde{e}$.
:::

:::

::: {.pf-step #part-d}
(d) $\overline{m}\big(\tilde{g},\overline{m}(\tilde{g}',\tilde{g}'')\big)=\overline{m}\big(\overline{m}(\tilde{g},\tilde{g}'),\tilde{g}''\big)$ for all $\tilde{g},\tilde{g}',\tilde{g}''$.

::: pf-proof
Let $F$ and $F'$ be the two maps $\overline{G}^{3}\to\overline{G}$ displayed, which are continuous because $\overline{m}$ is. Their projections agree, by associativity of the multiplication in $G$:
$$
pF=p\tilde{g}\cdot\big(p\tilde{g}'\cdot p\tilde{g}''\big)=\big(p\tilde{g}\cdot p\tilde{g}'\big)\cdot p\tilde{g}''=pF',
$$
and both send $(\tilde{e},\tilde{e},\tilde{e})$ to $\overline{m}\big(\tilde{e},\overline{m}(\tilde{e},\tilde{e})\big)=\tilde{e}$ and to $\overline{m}\big(\overline{m}(\tilde{e},\tilde{e}),\tilde{e}\big)=\tilde{e}$. The domain $\overline{G}^{3}$ is path connected and locally path connected, so the uniqueness part of Lemma 79.1 gives $F=F'$. This comparison is José Carlos Santos', MSE answer 3967971.
:::

:::

::: {.pf-step #part-e}
(e) $(\overline{G},\overline{m},\overline{I},\tilde{e})$ is a topological group, $p$ is a continuous homomorphism, and no other multiplication has both properties.

::: pf-proof
By steps [](#part-b){.pf-ref}, [](#part-c){.pf-ref} and [](#part-d){.pf-ref}, $\overline{m}$ is an associative multiplication on $\overline{G}$ with two-sided identity $\tilde{e}$ and two-sided inverses given by $\overline{I}$, so $\overline{G}$ is a group; $\overline{m}$ and $\overline{I}$ are continuous by construction, so it is a topological group. By construction $p\big(\overline{m}(x,y)\big)=p(x)p(y)$ and $p\big(\overline{I}(x)\big)=p(x)^{-1}$, so $p$ is a continuous homomorphism. If $m'$ is another multiplication making $\tilde{e}$ the identity and $p$ a homomorphism, then $p\circ m'=m\circ(p\times p)$ and $m'(\tilde{e},\tilde{e})=\tilde{e}$, so $m'$ is a based lift of $m\circ(p\times p)$ and equals $\overline{m}$ by the uniqueness part of Lemma 79.1.
:::

:::

::: {.pf-step}
The theorem holds.

::: pf-proof
Step [](#part-a){.pf-ref} secures the multiplication and inversion, step [](#part-e){.pf-ref} verifies the group axioms, continuity and the homomorphism property, and gives uniqueness.
:::

:::

:::
:::
