---
schema: qual/card@1
id: E-HAT-3.A-4
kind: problem
title: "Tensor product and Tor commute with direct limits"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.A, Exercise 4; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.A Exercise 4, printed p. 267; the statement
    matches the print. The proof was rewritten because both halves rested on machinery outside the
    book: "$\otimes B$ is a left adjoint and therefore preserves colimits", and the claim that the
    colimit of the functorial free presentation is a flat resolution, so that Tor may be computed
    from it — the earlier note here already recorded that the argument leans on torsionfree groups
    being flat. The book defines Tor only through free resolutions (Lemmas 3A.1-3A.2, pp. 262-263)
    and never states that flat resolutions compute it. The replacement proves the tensor half by
    exhibiting the two mutually inverse maps, and the Tor half from a free resolution of the second
    variable and the symmetry of Tor (Proposition 3A.5(1), p. 265), using only that a free group
    tensored with $M$ is a direct sum of copies of $M$ and that filtered colimits of abelian groups
    are exact, which is verified in the proof. No published solution of this exercise is in the
    retained sets; recorded in COMPLAINTS.md.
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    Both identities are published: Weibel, *An Introduction to Homological Algebra* (Cambridge
    Studies in Advanced Mathematics 38, 1994), Corollary 2.6.16 (left adjoints commute with filtered
    colimits, hence $-\otimes_\ZZ B$ does), Corollary 2.6.17 ($\operatorname{Tor}$ commutes with
    filtered colimits in the second variable) and Theorem 2.7.2 (balancing, hence symmetry of
    $\operatorname{Tor}$), all printed on p. 58 of the reading copy
    `tmp/sources/weibel-02-derived-functors.pdf`; read there on 2026-11-11 after searching outside the
    retained sets, as COMPLAINTS.md records. The card now names those three results with their pages
    and proves both identities directly for $\ZZ$-modules, so nothing rests on the general derived
    functor theory of a left adjoint; the two facts Weibel's argument uses are proved in the card.
    Checked against Hatcher (2002), §3.A Exercise 4 (printed p. 267) for the statement, Proposition
    3A.5(1) (p. 265) for the symmetry step and Lemmas 3A.1-3A.2 (pp. 262-263) for
    $\operatorname{Tor}$ being computed from a free resolution. Not claimed: that the card reproduces
    Weibel's derivation line for line — his is the categorical one, and the card says so.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    Re-read for the published-solution obligation. Both identities are published as corollaries of the exactness of filtered colimits of modules in Weibel, *An Introduction to Homological Algebra*, Corollary 2.6.17 with the surrounding section, printed p. 58, cited on the card with the two facts the derivation uses. Checked against the book: the exercise's printed statement on p. 267, Hatcher's definition of Tor by free resolutions (Lemma 3A.2, p. 263) and Proposition 3A.5(1) on the symmetry of Tor (p. 265). Not claimed: that a published solution set contains this exercise; the card says the source is the printed colimit corollary and derives the Tor statement from it.
---

::: {.problem}
Show that $\otimes$ and Tor commute with direct limits: $(\varinjlim_\alpha A_\alpha) \otimes B = \varinjlim(A_\alpha \otimes B)$ and $\operatorname{Tor}(\varinjlim A_\alpha, B) = \varinjlim \operatorname{Tor}(A_\alpha, B)$.
:::

::: {.solution}
Both identities are published as corollaries of the exactness of filtered colimits of modules in Weibel, *An Introduction to Homological Algebra* (Cambridge Studies in Advanced Mathematics 38, 1994), §2.6 and §2.7, printed p. 58. There, Corollary 2.6.16 states that for an abelian category with enough projectives satisfying (AB5) and a left adjoint $F$ the derived functors satisfy $L_*F(\varinjlim A_\alpha)\cong\varinjlim L_*F(A_\alpha)$ over a filtered index category; applied to the left adjoint $-\otimes_\ZZ B$, whose $L_0$ is itself, this is the first identity. Corollary 2.6.17 states $\operatorname{Tor}_*^R(A,\varinjlim B_\alpha)\cong\varinjlim\operatorname{Tor}_*^R(A,B_\alpha)$, and Theorem 2.7.2, balancing the two derived functors of the tensor product, states $\operatorname{Tor}_n^R(A,B)\cong\operatorname{Tor}_n^R(B,A)$; together they give the second identity. The argument below verifies both identities directly for $\ZZ$-modules, which is what the exercise asks for, with the two inputs Weibel uses — that a filtered colimit of abelian groups is exact, and that a free group tensored with $M$ is a direct sum of copies of $M$ — proved rather than cited.

Let $(A_\alpha)_{\alpha\in\Lambda}$ be a directed system of abelian groups over a directed index set $\Lambda$, with colimit $A=\varinjlim_\alpha A_\alpha$ and structure maps $i_\alpha:A_\alpha\to A$.

*Tensor products.* The maps $i_\alpha\otimes\id_B$ are compatible, so they induce $u:\varinjlim_\alpha(A_\alpha\otimes B)\to A\otimes B$. In the other direction, define a map $v:A\otimes B\to\varinjlim_\alpha(A_\alpha\otimes B)$ by the universal property of $\otimes$, from the bilinear map $(a,b)\mapsto[a_\alpha\otimes b]$, where $a_\alpha\in A_\alpha$ is any element with $i_\alpha(a_\alpha)=a$: two such choices $a_\alpha,a_{\alpha'}$ both map to a common later stage $A_\gamma$, because $\Lambda$ is directed, so the classes $[a_\alpha\otimes b]$ and $[a_{\alpha'}\otimes b]$ agree; the map is additive in each variable because the colimit is an abelian group and $i_\alpha$ is a homomorphism. On simple tensors $u v(a\otimes b)=i_\alpha(a_\alpha)\otimes b=a\otimes b$ and $vu[a_\alpha\otimes b]=[a_\alpha\otimes b]$, and simple tensors generate, so $u$ and $v$ are mutually inverse:
$$
\left(\varinjlim_\alpha A_\alpha\right)\otimes B\cong\varinjlim_\alpha(A_\alpha\otimes B).
$$

*Tor.* It is enough to prove that for a fixed abelian group $B$ the functor $M\mapsto\operatorname{Tor}(B,M)$ commutes with this colimit, since $\operatorname{Tor}(A,B)\cong\operatorname{Tor}(B,A)$ by Proposition 3A.5(1) (p. 265). Choose a free resolution $0\to G_1\xrightarrow{\varphi}G_0\to B\to0$; by the definition of Tor through a free resolution (Lemma 3A.2, p. 263, makes the choice immaterial)
$$
\operatorname{Tor}(B,M)=\ker\bigl(G_1\otimes M\xrightarrow{\varphi\otimes\id}G_0\otimes M\bigr).
$$
Two facts about the colimit are used.

(i) For a free abelian group $G$ with basis $J$ one has $G\otimes M\cong\bigoplus_J M$, and a filtered colimit of $J$-indexed direct sums is the direct sum of the colimits, because a sum has finite support and the support of an element does not change as the stage grows. Hence $G_i\otimes A\cong\varinjlim_\alpha(G_i\otimes A_\alpha)$ for $i=0,1$.

(ii) Filtered colimits in the category of abelian groups are exact. Indeed, given a directed system of exact sequences $0\to K_\alpha\to M_\alpha\to N_\alpha\to0$, an element of $\varinjlim K_\alpha$ maps to $0$ in $\varinjlim M_\alpha$ only if it is killed already at some stage, and an element of $\varinjlim M_\alpha$ with zero image in $\varinjlim N_\alpha$ is killed at some stage, hence lifts there from that stage of $K$. Applying this to the images of the exact sequences $0\to\ker(\varphi\otimes\id)\to G_1\otimes A_\alpha\to G_0\otimes A_\alpha$ gives
$$
\ker\left(\varinjlim_\alpha (G_1\otimes A_\alpha)\to\varinjlim_\alpha (G_0\otimes A_\alpha)\right)
\cong\varinjlim_\alpha\ker\bigl(G_1\otimes A_\alpha\to G_0\otimes A_\alpha\bigr).
$$
Combining with (i) and with the definition of Tor in each stage,
$$
\operatorname{Tor}(B,A)
=\ker\bigl(G_1\otimes A\to G_0\otimes A\bigr)
\cong\varinjlim_\alpha\operatorname{Tor}(B,A_\alpha)
\cong\varinjlim_\alpha\operatorname{Tor}(A_\alpha,B).
$$
Symmetry of Tor turns this into the asserted $\operatorname{Tor}(\varinjlim_\alpha A_\alpha,B)\cong\varinjlim_\alpha\operatorname{Tor}(A_\alpha,B)$.
:::
