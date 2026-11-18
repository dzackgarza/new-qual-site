---
schema: qual/card@1
id: P-AGH4422FAMILYOVERAFFINELINE
kind: problem
title: A family of elliptic curves over $\AA^1_\CC$ with a section is trivial
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.22 together with the preceding torsion and etale-cover
    exercises. Cross-checked that multiplication by 2 is finite etale in
    characteristic zero and that full 2-torsion gives Legendre form. The
    proof also closes the residual quadratic-twist issue after lambda is
    shown constant.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published solution located for this exercise (issue #121). Printed
    exercise read: Hartshorne, Algebraic Geometry (1977), IV.4.22, printed
    p. 340, with the four hint clauses the proof follows. Source: Yang
    Pi-Yeh, Hartshorne Solutions (9 June 2019), Solution 4.4.22, printed
    p. 95 of tmp/sources/lfwin-hartshorne-solutions.pdf, read in its text
    version tmp/sources/lfwin-hartshorne-solutions.md and settled on the
    PDF page where the OCR breaks his formula for S. His argument is steps
    s1--s5 here: the section as origin, the four 2-torsion points as a
    finite etale cover via (II, 9.9) and unramifiedness, four copies of
    A^1 by simple connectivity of A^1_C, the sections T_0, T_1, T_lambda
    giving coordinates, and t -> lambda a constant morphism to
    A^1 - {0,1}. His last sentence, that equal lambda makes the family
    trivial, is a gap: equal fibres do not give a trivial family and
    nothing in his argument excludes a twist over A^1_C; steps s6 and s7
    supply it. Book checks: IV.4.4 and IV.4.5, printed pp. 333--334
    (Legendre form, and the six substitutions that make the parameter well
    defined), IV.4.1, printed pp. 332--333 (isomorphic curves have equal
    j), II.9.9 as he cites it. Not checked: simple connectivity of A^1_C
    in the etale topology is taken from the printed hint, as he does; both
    texts assert the four 2-torsion points of a fibre without computing
    them, and the card's s1 proves it instead.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on the reader's report of this batch. The remark no longer says
    that the source's cover is unramified because its four points are
    distinct: that is the card's reason, and the source writes only
    "obviously unramified". It also no longer presents the source's
    flatness step as complete: (II, 9.9) needs the fibre of psi to have
    length four, and the source shows only that it has four closed points.
    The claim that this card is closed on a published solution is withdrawn
    here and in COMPLAINTS.md; what is located is an outline that follows
    the printed hint to the Legendre parameter, with those two steps
    asserted and with the last step, equal lambda giving a trivial family,
    missing. Checked against the book: IV.4.22 on printed p. 340, IV.4.4 and
    IV.4.5 on printed p. 318, IV.4.1 on printed pp. 317-318, II.9.9. Not
    checked: nothing new; the card's own steps were not re-derived.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass on the reader's report of this batch. The sentence of the
    remark that the previous pass broke is repaired: that pass left "the
    invertibility of 2. since A^1_C is simply connected", and the text now
    reads as one sentence again. The remark's "s1 supplies both" was too
    strong, and step s1 no longer asserts that [2] on an elliptic scheme is
    finite locally free of degree 4: it counts the four 2-torsion points of
    a complex elliptic curve, uses the differential of [2] for etaleness,
    and gets finiteness from Exercise III.11.2, so the step now proves what
    it claims. The event of 2026-11-16 above, whose note begins "Published
    solution located for this exercise", is restored as it was written and
    is named here. Checked against the book in this pass: IV.4.22 on printed
    p. 340, Exercise III.11.2 on printed p. 280, IV.4.1 and IV.4.4, IV.4.5
    on printed pp. 317-318. Not checked: simple connectivity of A^1_C in the
    etale topology is taken from the printed hint, as the card says.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass on the reader's report of this batch, on the audit trail only.
    The event of 2026-11-16 whose note begins "Repairs on the reader's report
    of this batch" is restored as it was written, and this event is appended
    after it rather than put in its place. The sentence and step-s1 repairs of
    the event above stand; the remark on the card records the published
    outline and the two steps it leaves asserted, so the obligation to cite a
    complete published solution stays open, as the remark says. Checked in
    this pass: nothing new; the card's own steps were not re-derived.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fourth pass, on the audit trail and the rule that a dated event is never
    edited. Two events of 2026-11-16 had been edited in place and are restored
    to their text at their date. (i) The event above whose note begins
    "Published solution located for this exercise" was changed by commit
    2145766034, which replaced "IV.4.4 and IV.4.5, printed pp. 333--334" by
    "printed p. 318" and "IV.4.1, printed pp. 332--333" by "IV.4.1, statement
    on printed pp. 317--318". It is restored as it was written in 114814f0e6,
    and the correction is here: those numbers were the PDF folios of the text
    version, and printed p. N is PDF p. N+15 in it. Verified in this pass in
    tmp/sources/hartshorne-1977-algebraic-geometry.md: Lemma 4.4 and Lemma
    4.5 stand between the markers of PDF pages 332 and 333, so on printed
    pp. 317--318, and the definition of the invariant of IV.4.1 is on the same
    two pages. (ii) The event above whose note begins "Second pass on the
    reader's report of this batch" was extended in place by commit 15a20526df
    with the sentence naming the text version and the offset; it is restored
    as it was written in 1abd969bbb, and that sentence is here: the pages it
    cites were read in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    where printed p. N is PDF p. N+15. Checked in this pass: this card's audit
    trail in git, commit by commit, and the pages of the text version named in
    (i). Not checked: no other page was re-read, and no step was re-derived.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Correction to the event above, whose note begins "Fourth pass, on the audit
    trail": its last two sentences place the two citations it verifies one page
    too early. In tmp/sources/hartshorne-1977-algebraic-geometry.md, Lemma 4.4
    and Lemma 4.5 of Hartshorne IV §4 stand between the markers of PDF pages
    333 and 334, that is on printed p. 318, and Theorem 4.1, which is the
    definition of the invariant that the citation of IV.4.1 rests on, stands
    between the markers of PDF pages 332 and 333, on printed p. 317. What the
    event concludes is unchanged: the numbers the earlier text carried,
    printed pp. 333--334 for IV.4.4 and IV.4.5, are PDF folios, and the printed
    pages are 318 and 317. Checked in this pass: both placements, re-read from
    the page markers of that text version. Not checked: no other page was
    re-read, and no step was re-derived.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    A complete published proof of this exercise was located for this batch:
    A. Youcis, *Abelian schemes over the integers* (2016), Theorem 8, section
    "The case over the complex line", read at that section in the text version
    tmp/sources/youcis-2016-abelian-schemes-over-integers.md, with his
    definition of an abelian scheme in the section "Two statements of the main
    result" and his definition of isotrivial in the section "Analogies and
    intuitions". The post carries no printed folios, so its statements are
    cited on the card by number and section heading. Checked against the book:
    the printed exercise, IV Ex. 4.22, printed p. 340 and starred, with its
    four hint clauses; the exercise's "family of elliptic curves having a
    section" is a family of abelian varieties in Youcis's sense once the
    section fixes the origin on each fibre, which is the first clause of the
    printed hint, and his base V = A^1_C satisfies his hypothesis with
    V^an = C simply connected. Not checked: Deligne, *Theorie de Hodge II*,
    4.4.3, and the rigidity result of Peters and Steenbrink, both of which
    Youcis cites and neither of which is in tmp/sources; his proof is
    complete only modulo them.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the transcription of that proof, one step per move,
    each naming its numbered statement or quoted sentence with the section
    heading of the post: step abelian-scheme from the printed hint's first
    clause and Youcis's definition of an abelian scheme, step
    constant-family from his definition of isotrivial, step theorem-eight
    quoting Theorem 8, step deligne-argument carrying his four moves, and
    step conclusion applying the theorem at V = A^1_C. Two things leave the
    card: its former seven steps, which counted the four 2-torsion points,
    built the four sections, the double cover q and the Legendre coordinate,
    and closed the twist through the trace decomposition of the double cover
    and Pic(A^1_C) = 0, remain readable at commit 574af010f7; and the
    conclusion of the events of 2026-11-16 above, that the card is not closed
    on a published solution, is superseded: what those events established is
    that Yang's Solution 4.4.22 stops at the constancy of lambda, and Youcis's
    Theorem 8 does not follow the printed hint at all. Nothing in the problem
    statement changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's report, and the record of what
    the events of this date above left out. (i) Step abelian-scheme is the
    card's own and unproved, which commit 64d0d101ab made it: the step now
    says that the passage from a pointed family of elliptic curves over S to a
    smooth proper group scheme over S, hence to a family of abelian varieties
    in Youcis's sense, needs the fibrewise group laws to be restrictions of
    morphisms E x_S E -> E and E -> E over S, equivalently the
    representability of the relative Picard functor together with the
    identification of E with it, and that neither Youcis nor the book at this
    exercise supplies them. No event recorded that repair until this one.
    (ii) Corrected here, the events above not being rewritable: the
    solution-written event's "step abelian-scheme from the printed hint's
    first clause and Youcis's definition of an abelian scheme", and the
    source-checked event's "is a family of abelian varieties in Youcis's sense
    once the section fixes the origin on each fibre, which is the first clause
    of the printed hint". The printed hint's first clause asks for exactly
    what step abelian-scheme states and does not prove. (iii) The remark and
    the conclusion of the solution are now relative to that step: the remark
    says that Theorem 8 proves the exercise once the family is one of abelian
    varieties in Youcis's sense and names step abelian-scheme as the card's
    own and unproved passage, and the conclusion's proof says so before
    applying the theorem. (iv) The paragraph in step deligne-argument that
    reads Youcis's cyclic kernel as a finite constant group scheme, through
    the triviality of a finite étale cover of a base with simply connected
    analytification, now says that it is the card's own; the post asserts the
    cyclic kernel with no argument. Not read in this pass: Deligne, Théorie de
    Hodge II, 4.4.3, and the rigidity result of Peters and Steenbrink, as
    before; the card's own steps were not re-derived. Checked against the book
    in this pass: Hartshorne IV Ex. 4.22 on printed p. 340, unchanged.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's second report. (i) The provenance
    sentences that stood in the rendered solution are out of it: step
    abelian-scheme's statement no longer says "and is not proved from the
    sources read", and its proof no longer closes "Neither is in Youcis, and
    neither is in the book at this exercise, which asserts the first of them in
    its hint and no more". The step keeps the sanctioned mark "This step is the
    card's own", and says what the passage needs, which is mathematics; the
    search status it used to carry is in the events above and in the record of
    this date in COMPLAINTS.md. The sentence that remains on the printed hint,
    "The printed hint asserts the first of the two", states what the hint asks
    for. (ii) Step deligne-argument's statement said "a finite kernel with
    constant quotient makes it constant", which misstates the fourth move: the
    constant family is the source of the isogeny and the family is its quotient
    by a finite constant group scheme, as his own sentence quoted in the proof
    has it. The statement is corrected; the quoted moves were already right.
    Not read in this pass: nothing new; Deligne's Théorie de Hodge II, 4.4.3,
    and the rigidity result of Peters and Steenbrink remain unread here, and no
    step of the proof was re-derived.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's whole-batch report, and the
    correction of two misattributions in one remark of the source. Youcis's
    remark after the proof of Theorem 8, in the text version
    tmp/sources/youcis-2016-abelian-schemes-over-integers.md at line 264,
    reads: "Using the results mentioned in this mathoverflow post, namely the
    cited rigidity result of Strauch, one can use the above cited result of
    Peters and Steenbrink to show that not only must a Q-VHS on a
    compactifiable complex manifold be constant (as a VHS) but also that the
    same is true for integral Hodge structures." The rigidity result there is
    Strauch's, cited from a MathOverflow post; Peters and Steenbrink's is "the
    above cited result" used with it, and his later remark on algebraicity, at
    line 274, places it at the compactifiability of V, which is the same
    reading. Step deligne-argument's third move gave the rigidity result to
    Peters and Steenbrink and, in a bracketed change of his words, made them
    the subject of "show[s]"; the remark on the published solution repeated
    the attribution in its clause on the two analytic inputs. Both are
    corrected: the step now quotes the remark as written and says which
    result is whose, and the remark now gives Peters and Steenbrink's result
    as the constancy of the Q-VHS with Strauch's rigidity result named beside
    it. The event of 2026-11-16 above whose note begins "A complete published
    proof of this exercise was located" carries the same attribution, in its
    clause "the rigidity result of Peters and Steenbrink, both of which
    Youcis cites"; it stands as written, and this event is the correction.
    Checked in this pass: that remark and the algebraicity remark in the text
    version at the lines named, and the two places on the card. Not read in
    this pass: Deligne, Théorie de Hodge II, 4.4.3, and Strauch's rigidity
    result, neither of which is in tmp/sources, as before; no step was
    re-derived, and the printed exercise on printed p. 340 was not reopened.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The step now cites what the book proves for it and says why that is not the
    relative form it needs. Read for this: Hartshorne IV.4 in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, Theorem 4.11 at printed
    p. 325 (its hypothesis "Let X be an elliptic curve, and fix a point P0 in
    X", its last clause identifying the group structure of 4.10.6 with that of
    4.7), Remarks 4.10.5 and 4.10.6 at printed pp. 323--324 (the definition of a
    group scheme over a base, and "the Jacobian variety J of a curve X is
    automatically a group scheme over k"), and the definition "an abelian
    variety is a complete group variety over k" at printed p. 140. Those give
    the fibre-level statement and not the relative one: the theorem fixes the
    curve over k and varies the test scheme T, so it does not say that a family
    E to S with a section is a group scheme over S, which is what the step
    states and what the printed hint asserts. The step therefore stays the
    card's own, and the conclusion stays relative to it. Not checked: no other
    source was searched for this step in this pass, and no step of the exercise
    was re-derived.
---

::: {.problem}
\* If $X \to \AA_{\CC}^1$ is a family of elliptic curves having a section, show that the family is trivial.

Hints: Use the section to fix the group structure on the fibres.
Show that the points of order 2 on the fibres form an étale cover of $\AA_{\CC}^1$, which must be trivial, since $\AA_{\CC}^1$ is simply connected.
This implies that $\lambda$ can be defined on the family, so it gives a map $\AA_{\CC}^1 \to \AA_{\CC}^1-\theset{0,1}$.
Any such map is constant, so $\lambda$ is constant, so the family is trivial.
:::



::: {.solution}

Write
$$
S=\AA^1_{\CC}=\Spec\CC[t],
$$
let $\pi:E\to S$ be the family, and let $O:S\to E$ be the given section.
The proof is A. Youcis, *Abelian schemes over the integers* (2016), section "The case over the complex line".
His Theorem 8 is stronger than the exercise and is applied to $V=S$ in step [](#conclusion){.pf-ref}.

::: pf

::: {.pf-step #abelian-scheme}

The section $O$ makes each fibre $E_t$ an elliptic curve with origin $O(t)$, so $E\to S$ is a family of elliptic curves pointed by $O$; that it is consequently a family of abelian varieties over $S$ in the sense of Youcis, a smooth proper group scheme with connected fibres, is the card's own step.

::: pf-proof

This step is the card's own.

The printed hint of the exercise begins "Use the section to fix the group structure on the fibres", and each fibre $E_t$ is a smooth curve of genus $1$ with the point $O(t)$: a genus-one curve with a chosen point is an elliptic curve, and its group law has that point as identity.
What the book proves about that point is Hartshorne IV.4: an elliptic curve is its own Jacobian, Theorem 4.11, printed p. 325, whose last clause identifies the group structure of Remark 4.10.6, printed p. 324, with the one of (4.7); the book's definition of an abelian variety is "a complete group variety over $k$", printed p. 140. That is the fibre-level statement over $k=\CC$, and it makes each $E_t$ an abelian variety. It is not the relative statement this step needs: the theorem quantifies over an elliptic curve over $k$ and over $k$-schemes $T$, so it fixes the curve and varies only the test scheme, and it says nothing about a family $E\to S$.
Youcis's definition, in his section "Two statements of the main result", is "an abelian scheme $\mathscr A/S$ is a smooth proper group scheme with connected fibers", and the passage from the pointed family to a smooth proper group scheme over $S$ needs two things that are not proved here: that the fibrewise group laws are the restrictions of morphisms $E\times_SE\to E$ and $E\to E$ over $S$, and the representability of the relative Picard functor $\Pic^0_{E/S}$ together with the identification $E\cong\Pic^0_{E/S}$ that would supply them. The printed hint asserts the first of the two.

:::

:::

::: {.pf-step #constant-family}

In Youcis's sense, a family over $S$ is isotrivial exactly when it is the product of $S$ with a single object, which is the conclusion of the exercise.

::: pf-proof

His section "Analogies and intuitions" fixes the term: "a family $\mathscr X/\AA^1_F$ of curves/abelian schemes is isotrivial if there exists an object $X/F$ such that $\mathscr X=X\times_F\AA^1_F$ --- it's a constant family with fiber $X$."
For a family of elliptic curves over $S$ it is the assertion that $E\cong E_0\times_\CC S$ for some elliptic curve $E_0$ over $\CC$, the structure morphism of the product being the projection to $S$; that is what the exercise asks.

:::

:::

::: {.pf-step #theorem-eight}

Youcis, Theorem 8, section "The case over the complex line", quoted: "Let $V/\CC$ be a smooth connected algebraic variety such that $V^\text{an}$ is simply connected. Then, every family of abelian varieties $f:\mathscr A\to V$ is isotrivial."

::: pf-proof

This is the statement of Theorem 8 of the post at the cited section, with the proof that step [](#deligne-argument){.pf-ref} transcribes.
Its hypotheses are on $V$ and on the family being one of abelian varieties; step [](#abelian-scheme){.pf-ref} supplies the second for $E\to S$.

:::

:::

::: {.pf-step #deligne-argument}

Proof of Theorem 8, as published: the local system of the family is constant because $V^\text{an}$ is simply connected, the family is therefore isogenous to a constant family $\underline A$, and $\mathscr A$ is the quotient of $\underline A$ by a finite constant group scheme, hence itself constant.

::: pf-proof

Youcis's proof has four moves, each quoted or cited as he gives it.

First, "By 4.4.3 of Deligne's *Théorie de Hodge II* there is an equivalence of categories between abelian schemes and polarizable $\ZZ$-variations of Hodge structure. The map is given by $\mathscr A\mapsto(R^1f^{\text{an}}_*\underline{\ZZ})^\vee$." The cited statement is Deligne, *Théorie de Hodge II*, 4.4.3.

Second, "since $V^\text{an}$ is simply connected then the $\ZZ$-local system $(R^1f^{\text{an}}_*\underline{\ZZ})^\vee$ is a constant local system but, a priori, one might be worried that the Hodge filtration is not constant."

Third, "Since $V^\text{an}$ is compactifiable by Hironaka's theorem and by the discussion following Theorem 11 of this article we may conclude that $(R^1f^{\text{an}}_*\underline{\QQ})^\vee$ is constant and thus, by Deligne's theorem, that $\mathscr A$ is isogenous to a constant family $\underline A$." What that constancy rests on, his remark after the proof states in these words: "Using the results mentioned in this mathoverflow post, namely the cited rigidity result of Strauch, one can use the above cited result of Peters and Steenbrink to show that not only must a $\QQ$-VHS on a compactifiable complex manifold be constant (as a VHS) but also that the same is true for integral Hodge structures." The rigidity result in that sentence is Strauch's, taken from a MathOverflow post, and it enters together with the cited result of Peters and Steenbrink: the constancy of the $\QQ$-variation of Hodge structure on a compactifiable manifold is Peters and Steenbrink's, and the integral statement is what the two give together.

Fourth, "the kernel of some isogeny $\underline A\to\mathscr A$ must be a finite group constant group scheme $\underline{\ZZ/n\ZZ}$. Thus, $\mathscr A\cong\underline{A/(\ZZ/n\ZZ)}$ as desired."

The group $\ZZ/n\ZZ$ in that sentence is the source's, and it is more special than the argument yields: what the third move produces is a finite étale subgroup scheme of the constant family $\underline A$, and a finite étale cover of a variety with simply connected analytification is trivial, so the kernel is a finite constant group scheme, which need not be cyclic. The conclusion uses constancy alone, so the argument stands with $\ZZ/n\ZZ$ read as a finite constant group scheme. This paragraph is the card's own: the source writes $\ZZ/n\ZZ$ with no argument for it, and the triviality of a finite étale cover of a simply connected base is not in the post.

The third move is where the hypothesis that $V$ is algebraic enters, as his remark after the proof says: Deligne's classification needs algebraicity of $V$, and the compactifiability is that of an algebraic variety.

:::

:::

::: {.pf-step #conclusion}

$$
\boxed{E\cong E_0\times_\CC\AA^1_{\CC}\ \text{over}\ \AA^1_{\CC}\ \text{for some elliptic curve } E_0/\CC}
$$

::: pf-proof

Take $V=S=\AA^1_\CC$ in step [](#theorem-eight){.pf-ref}.
$S$ is a smooth connected algebraic variety over $\CC$, and $S^\text{an}=\CC$ is simply connected, being contractible: the homotopy $x\mapsto(1-s)x$, $0\le s\le1$, contracts $\CC$ to the origin.
Step [](#abelian-scheme){.pf-ref} is what makes $E\to S$ a family of abelian varieties over $V=S$; that step is the card's own and unproved, so what follows is relative to it.
With it, Theorem 8 applies through its proof in step [](#deligne-argument){.pf-ref} and $E\to S$ is isotrivial, that is, by step [](#constant-family){.pf-ref}, a product $E_0\times_\CC\AA^1_\CC$ over $\AA^1_\CC$.
That is the triviality the exercise asks for.

:::

:::

:::

:::

::: {.remark title="Published solution"}

Youcis's Theorem 8, section "The case over the complex line", proves the exercise once the family is one of abelian varieties in his sense, and more: the base may be any smooth connected complex algebraic variety with simply connected analytification, and the fibres may be abelian varieties of any dimension.
The passage from the exercise's family, which carries a section, to a family of abelian varieties is step [](#abelian-scheme){.pf-ref}, which is the card's own and unproved.
Its two analytic inputs are cited rather than proved there: the equivalence of Deligne, *Théorie de Hodge II*, 4.4.3, and the constancy of the $\QQ$-variation of Hodge structure over a compactification, for which his remark after the proof invokes the cited result of Peters and Steenbrink together with the rigidity result of Strauch that he takes from a MathOverflow post.
The section closes with his remark that the theorem "becomes wildly false" outside the algebraic category, the family of elliptic curves over the upper half-plane $\halfplane$ with $g_4$ and $g_6$ the level-one modular forms being non-isotrivial although $\halfplane$ is simply connected, and that $\halfplane$ is not algebraic is what saves the theorem.

The printed hint follows a different route: the points of order $2$ form an étale cover of $\AA^1_\CC$, hence are four disjoint sections, and the Legendre parameter $\lambda$ they define is a morphism $\AA^1_\CC\to\AA^1_\CC\setminus\{0,1\}$, hence constant.
Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.4.22, printed p. 95, carries that hint out: the four $2$-torsion sections, four copies of $\AA^1_\CC$ because $\AA^1_\CC$ is simply connected, the coordinates $\infty,0,1,\lambda$ on each fibre, and $\lambda$ constant.
That route ends at the constancy of $\lambda$, which is equality of the fibres, and does not by itself give the triviality of the family.

:::
