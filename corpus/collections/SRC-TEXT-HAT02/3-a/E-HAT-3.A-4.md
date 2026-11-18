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
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Citations only; nothing in the statement or the derivation changes. No citation on this card named
    its text version. Weibel's §2.6--2.7 is read in `tmp/sources/weibel-02-derived-functors.md`, which
    was opened this pass and does contain Theorem 2.6.15, axiom (AB5), Corollaries 2.6.16 and 2.6.17
    and Theorem 2.7.2 on its printed pp. 57--58, and Hatcher is read in
    `tmp/sources/hatcher-2002-algebraic-topology.md`. Both are now named where they are cited. Checked
    against Hatcher (2002), §3.A Exercise 4 on printed p. 267 and the remark on printed p. 263 that
    $\operatorname{Tor}_n=0$ for $n>1$. Not claimed: a text version for any other source, this card
    citing none; nothing was read from a rendered page.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule applied at paragraph level: the solution opens with the provenance
    convention for a prose proof. The two paragraphs the probe found without a citation --- the
    tensor-product adjunction and the remark that the symmetry of Tor is not passed through the
    colimit --- are the card's own, the second stating what the exercise does not ask and Weibel's
    Corollary 2.6.17, printed p. 58, does not supply. Checked: the Weibel pages 57 and 58.

---

::: {.problem}
Show that $\otimes$ and Tor commute with direct limits: $(\varinjlim_\alpha A_\alpha) \otimes B = \varinjlim(A_\alpha \otimes B)$ and $\operatorname{Tor}(\varinjlim A_\alpha, B) = \varinjlim \operatorname{Tor}(A_\alpha, B)$.
:::

::: {.solution}
Provenance, paragraph by paragraph: a paragraph that names a printed source records that source's argument at the page given, and a paragraph that names none is the card's own, possibly applying a result cited in another paragraph.

Both identities are instances of the filtered-colimit theorems of Weibel, *An Introduction to Homological Algebra* (Cambridge Studies in Advanced Mathematics 38, 1994), §2.6--2.7, printed p. 58, read in `tmp/sources/weibel-02-derived-functors.md`, applied to the left adjoint $-\otimes_\ZZ B$ of $\ZZ$-mod. Let $\Lambda$ be a directed index set, $(A_\alpha)_{\alpha\in\Lambda}$ a directed system of abelian groups with colimit $A=\varinjlim_\alpha A_\alpha$ and structure maps $i_\alpha:A_\alpha\to A$. A directed set is a filtered index category, so the theorems of §2.6 apply.

*The results used, with their printed statements.*

(i) Theorem 2.6.15, printed p. 57: filtered colimits of $R$-modules are exact, considered as functors from $(\text{mod-}R)^I$ to $\text{mod-}R$. Weibel calls a cocomplete abelian category in which filtered colimits are exact a category satisfying (AB5) (Exercise 2.6.5, printed p. 57), and the theorem says $\text{mod-}R$ and $R\text{-mod}$ do; $\ZZ$-mod has enough projectives as well, free abelian groups being projective.

(ii) Corollary 2.6.16, printed p. 58: if $\mathcal A=\text{mod-}R$, or $\mathcal A$ is any abelian category with enough projectives satisfying (AB5), and $F:\mathcal A\to\mathcal B$ is a left adjoint, then for every $A:I\to\mathcal A$ with $I$ filtered,
$$
L_*F\bigl(\varinjlim A_i\bigr)\cong\varinjlim L_*F(A_i).
$$

(iii) Theorem 2.7.2, printed p. 58: $L_n(A\otimes_R-)(B)\cong L_n(-\otimes_RB)(A)=\operatorname{Tor}_n^R(A,B)$, the balancing of the two left derived functors of the tensor product.

Weibel prints the same colimit theorem for $\operatorname{Tor}$ in the second variable as Corollary 2.6.17, printed p. 58: $\operatorname{Tor}_*^R(A,\varinjlim B_i)\cong\varinjlim\operatorname{Tor}_*^R(A,B_i)$. It is not the step the exercise needs, and the text below says why.

*Tensor products.* Take $F=-\otimes_\ZZ B:\ZZ\text{-}\mathbf{mod}\to\ZZ\text{-}\mathbf{mod}$, a left adjoint with right adjoint $\operatorname{Hom}_\ZZ(B,-)$. Its zeroth left derived functor is $F$ itself, because the tensor product is right exact. Corollary 2.6.16 in degree zero then reads
$$
\Bigl(\varinjlim_\alpha A_\alpha\Bigr)\otimes_\ZZ B\cong\varinjlim_\alpha(A_\alpha\otimes_\ZZ B),
$$
which is the exercise's first identity.

*Tor.* Apply the same corollary to the same functor in degree $n$ and use (iii) at each argument:
$$
\operatorname{Tor}_n^{\ZZ}\Bigl(\varinjlim_\alpha A_\alpha,B\Bigr)
=L_n(-\otimes_\ZZ B)\Bigl(\varinjlim_\alpha A_\alpha\Bigr)
\cong\varinjlim_\alpha L_n(-\otimes_\ZZ B)(A_\alpha)
\cong\varinjlim_\alpha\operatorname{Tor}_n^{\ZZ}(A_\alpha,B).
$$
The outer equalities are the balancing isomorphism of Theorem 2.7.2, the middle one is Corollary 2.6.16. The exercise's second identity is the case $n=1$, which is $\operatorname{Tor}$ for abelian groups; $\operatorname{Tor}_n^{\ZZ}=0$ for $n>1$ because every abelian group has a free resolution of length one (Hatcher, printed p. 263).

*The symmetry of $\operatorname{Tor}$ is not passed through the colimit.* Both identities of the exercise are stated with the colimit in the first variable, and the derivation above keeps that variable fixed: Corollary 2.6.16 is a statement about the one functor $F=-\otimes_\ZZ B$, and Theorem 2.7.2 is a natural isomorphism of functors in the module variable, so it applies at the colimit and at every stage simultaneously. Nothing of the form $\operatorname{Tor}(B,A_\alpha)\cong\operatorname{Tor}(A_\alpha,B)$ occurs, and no compatibility of such a stagewise isomorphism with the structure maps $A_\alpha\to A_\beta$ has to be checked. For a colimit in the second variable the same argument runs with the other adjunction $A\otimes_R-\dashv\operatorname{Hom}_R(A,-)$, which is how the book obtains Corollary 2.6.17; the two variables agree for $\ZZ$-mod by Theorem 2.7.2, and that theorem is where the symmetry of $\operatorname{Tor}$ enters, once, as a natural isomorphism.

Checked against Hatcher, *Algebraic Topology* (2002), §3.A Exercise 4, printed p. 267, read in `tmp/sources/hatcher-2002-algebraic-topology.md`: "Show that $\otimes$ and $\operatorname{Tor}$ commute with direct limits: $(\varinjlim_\alpha A_\alpha)\otimes B=\varinjlim(A_\alpha\otimes B)$ and $\operatorname{Tor}(\varinjlim A_\alpha,B)=\varinjlim\operatorname{Tor}(A_\alpha,B)$", with Hatcher's $\operatorname{Tor}=\operatorname{Tor}_1^{\ZZ}$ as on printed p. 263. Weibel's derivation gives both identities in every degree and asks nothing of the directed system beyond filteredness.
:::
