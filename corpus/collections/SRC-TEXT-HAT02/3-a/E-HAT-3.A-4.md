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

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two colimit identities, which is what Queue D asks for on this card. The four printed results the argument applies are listed with their statements in the lead, and the proof is then three steps: the adjunction and the identification of the zeroth derived functor, the tensor identity in degree zero, and the Tor identity in every degree with the balancing isomorphism. The long prose passage on why the symmetry of Tor is not passed through the colimit is kept, but moved out of the proof into a remark after it, since it is not a step of the argument. Weibel's four locators were re-read against the retained text version and the PDF folios: Theorem 2.6.15 on printed p. 57, Corollaries 2.6.16 and 2.6.17 and Theorem 2.7.2 on printed p. 58, all as the card had them. No statement repair: the exercise is Hatcher §3.A Exercise 4, printed p. 267, and no retained solution set reaches §3.A.
---

::: {.problem}
Show that $\otimes$ and Tor commute with direct limits: $(\varinjlim_\alpha A_\alpha) \otimes B = \varinjlim(A_\alpha \otimes B)$ and $\operatorname{Tor}(\varinjlim A_\alpha, B) = \varinjlim \operatorname{Tor}(A_\alpha, B)$.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout hold nothing from §3.A. The argument below is the card's own, and it is an application, not a re-proof, of four printed results of Weibel, *An Introduction to Homological Algebra* (Cambridge Studies in Advanced Mathematics 38, 1994), read in `tmp/sources/weibel-02-derived-functors.md`:

(i) Theorem 2.6.15, printed p. 57: filtered colimits of $R$-modules are exact, considered as functors from $(\mathbf{mod}\text{-}R)^I$ to $\mathbf{mod}\text{-}R$. That is axiom (AB5) of Exercise 2.6.5, printed p. 57; $\ZZ$-mod also has enough projectives, free abelian groups being projective.

(ii) Corollary 2.6.16, printed p. 58: if $\mathcal A=\mathbf{mod}\text{-}R$, or $\mathcal A$ is any abelian category with enough projectives satisfying (AB5), and $F:\mathcal A\to\mathcal B$ is a left adjoint, then for every $A:I\to\mathcal A$ with $I$ filtered,
$$
L_*F\bigl(\varinjlim A_i\bigr)\cong\varinjlim L_*F(A_i).
$$

(iii) Theorem 2.7.2, printed p. 58: $L_n(A\otimes_R-)(B)\cong L_n(-\otimes_RB)(A)=\operatorname{Tor}_n^R(A,B)$, the balancing of the two left derived functors of the tensor product.

(iv) Corollary 2.6.17, printed p. 58, gives the same colimit theorem for $\operatorname{Tor}$ in the second variable. It is not the step the exercise needs, and the remark after the proof says why.

Throughout, $\Lambda$ is a directed index set, $(A_\alpha)_{\alpha\in\Lambda}$ a directed system of abelian groups with colimit $A=\varinjlim_\alpha A_\alpha$. A directed set is a filtered index category, so (i) and (ii) apply.

::: pf

::: {.pf-step #left-adjoint}
The functor $F=-\otimes_\ZZ B:\ZZ\text{-}\mathbf{mod}\to\ZZ\text{-}\mathbf{mod}$ is a left adjoint, and $L_0F=F$.

::: pf-proof
$-\otimes_\ZZ B$ is left adjoint to $\operatorname{Hom}_\ZZ(B,-)$, by the tensor-hom adjunction. A left adjoint is right exact, and the zeroth left derived functor of a right exact functor is the functor itself: the augmentation $P_0\to A$ of a projective resolution gives $L_0F(A)=\operatorname{coker}(F(P_1)\to F(P_0))$, which is $F(A)$ precisely because $F$ is right exact.
:::

:::

::: {.pf-step #tensor}
$\bigl(\varinjlim_\alpha A_\alpha\bigr)\otimes_\ZZ B\cong\varinjlim_\alpha(A_\alpha\otimes_\ZZ B)$.

::: pf-proof
Corollary 2.6.16 applies to the left adjoint $F$ of step [](#left-adjoint){.pf-ref}, whose hypotheses hold by (i) and the projectivity of free abelian groups; in degree zero it reads $L_0F(\varinjlim A_\alpha)\cong\varinjlim L_0F(A_\alpha)$, which is $F(\varinjlim A_\alpha)\cong\varinjlim F(A_\alpha)$ by $L_0F=F$. Unwinding $F$ gives the identity.
:::

:::

::: {.pf-step #tor}
$\operatorname{Tor}_n^{\ZZ}\bigl(\varinjlim_\alpha A_\alpha,B\bigr)\cong\varinjlim_\alpha\operatorname{Tor}_n^{\ZZ}(A_\alpha,B)$ for every $n$, and in particular for $n=1$.

::: pf-proof
Apply Corollary 2.6.16 to the same left adjoint in degree $n$ and identify both sides by the balancing isomorphism of Theorem 2.7.2:
$$
\operatorname{Tor}_n^{\ZZ}\Bigl(\varinjlim_\alpha A_\alpha,B\Bigr)
=L_n(-\otimes_\ZZ B)\Bigl(\varinjlim_\alpha A_\alpha\Bigr)
\cong\varinjlim_\alpha L_n(-\otimes_\ZZ B)(A_\alpha)
\cong\varinjlim_\alpha\operatorname{Tor}_n^{\ZZ}(A_\alpha,B).
$$
The first and last equalities are (iii), the middle is (ii). The exercise's $\operatorname{Tor}$ is $\operatorname{Tor}_1^{\ZZ}$, Hatcher's convention on printed p. 263, so the case $n=1$ is the second identity; $\operatorname{Tor}_n^{\ZZ}=0$ for $n>1$ because every abelian group has a free resolution of length one, so nothing is lost in restricting to $n=1$.
:::

:::

:::

:::

::: {.remark}
Both identities are stated with the colimit in the *first* variable, and the derivation keeps that variable fixed: Corollary 2.6.16 concerns the single functor $F=-\otimes_\ZZ B$, and Theorem 2.7.2 is a natural isomorphism in the module variable, so it applies at the colimit and at every stage at once. Nothing of the form $\operatorname{Tor}(B,A_\alpha)\cong\operatorname{Tor}(A_\alpha,B)$ is used, and no compatibility of such a stagewise isomorphism with the structure maps has to be checked. For a colimit in the second variable the argument runs with the other adjunction $A\otimes_R-\dashv\operatorname{Hom}_R(A,-)$, which is how Weibel obtains Corollary 2.6.17; the two variables agree for $\ZZ$-mod by Theorem 2.7.2, and that theorem is where the symmetry of $\operatorname{Tor}$ enters, once, as a natural isomorphism.
:::
