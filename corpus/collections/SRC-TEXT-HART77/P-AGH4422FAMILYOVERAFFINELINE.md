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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Step abelian-scheme now carries a published proof of the relative statement,
    which is what issue #155 asks for, and the card no longer says that the step
    is unproved. Read for it: Katz and Mazur, *Arithmetic Moduli of Elliptic
    Curves* (1985), (2.1.1) and Theorem 2.1.2 (Abel) with its proof, printed
    pp. 63--66, in the text version
    tmp/sources/katz-mazur-arithmetic-moduli-of-elliptic-curves.md and on the
    rendered pages of
    tmp/sources/katz-mazur-arithmetic-moduli-of-elliptic-curves.pdf, where
    printed p. N is PDF p. N+12, so that printed p. 63 is PDF p. 75 and the
    proof's last page, printed p. 66, is PDF p. 78. Their (2.1.1) defines an
    elliptic curve over an arbitrary scheme as a proper smooth curve with
    geometrically connected fibres of genus one and a section, which is the
    exercise's data, and Theorem 2.1.2 supplies the commutative group-scheme
    structure by transporting that of the relative Picard functor along Abel's
    map, so the step's statement is a published theorem and not the card's own.
    Two of that proof's citations were read in the same text: Mumford,
    *Abelian Varieties* (1970), p. 53, for the invertibility and base-change
    compatibility of the pushforward of a fibrewise-degree-one sheaf, and their
    (1.2.7), that an effective Cartier divisor of degree one in E/S is a
    section, which the proof quotes on printed p. 66. Checked against the book
    for the comparison with Hartshorne's language: the definition of a group
    scheme before Remark 4.10.5, printed p. 324, Theorem 4.11 with its last
    clause identifying the group structure of Remark 4.10.6, printed p. 325,
    and the printed exercise, IV Ex. 4.22 on printed p. 340, whose statement is
    unchanged. The conclusion of the solution and the remark on the published
    solution now read the step as proved. Not checked: Mumford's p. 53 itself,
    which is in no retained set and is cited as Katz and Mazur cite it;
    Deligne, *Theorie de Hodge II*, 4.4.3, and the results of Peters and
    Steenbrink and of Strauch that Youcis cites, as before; and the card's other
    steps were not re-derived in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The fibre input of step abelian-scheme is now cited, and the first of the
    two citations the step rests on is a source on this machine. Altman and
    Kleiman, *Introduction to Grothendieck Duality Theory*, Lecture Notes in
    Mathematics 146 (1970), read in
    tmp/sources/altman-kleiman-introduction-to-grothendieck-duality.md and on
    the rendered pages of
    tmp/sources/altman-kleiman-introduction-to-grothendieck-duality.pdf, where
    printed p. N is PDF p. N+2 (printed p. 164 is PDF p. 166, printed p. 167 is
    PDF p. 169): Theorem (1.4) (Riemann), printed p. 164, gives
    chi(D) = deg(D) + chi(O_X) for X proper over an artinian ring, and Theorem
    (1.15) (Roch), printed p. 167, gives H^0(X, Hom(F, omega_X)) isomorphic to
    H^1(X, F)^* for X a reduced proper curve over a field and F a coherent
    subsheaf of K_X. Applied to an invertible sheaf of degree one on a curve of
    genus one they give h^1 = 0 and h^0 = 1, which is the rank the pushforward
    is asserted to have fibrewise. The base-change half is left as Katz and
    Mazur give it, cited to Mumford, Abelian Varieties (1970), p. 53, and the
    step now also names the book's own form of that theorem, III.12.11
    (Cohomology and Base Change) at printed p. 290 with Corollary 12.9
    (Grauert) at printed p. 288, read in
    tmp/sources/hartshorne-1977-algebraic-geometry.md between the page markers
    of PDF pages 305 and 306, and before that of 304. No step of this card
    needs Mumford, Fogarty and Kirwan, Geometric Invariant Theory: the earlier
    records named its Theorem 6.14 as a candidate relative source, the step is
    now carried by Katz and Mazur's Theorem 2.1.2, and that book is not
    available in full on this machine. Not checked: Mumford's Abelian Varieties,
    p. 53, which is cited as Katz and Mazur cite it; and Altman and Kleiman's
    Chapter VIII beyond the theorems named, in particular the residue theory of
    its sections 2 to 4, which this step does not use.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Mumford's page was obtained and read, so the base-change citation of step
    abelian-scheme is now verified rather than transcribed. Source: D. Mumford,
    *Abelian Varieties*, Tata Institute of Fundamental Research Studies in
    Mathematics 5, Oxford University Press, 1970, Chapter II section 5,
    "Cohomology and base change", read on a scan fetched for this check from
    wstein.org and kept for the reading only; that scan puts two book pages on a
    PDF page, printed pp. 46--47 being PDF p. 28, printed pp. 50--51 PDF p. 30
    and printed pp. 52--53 PDF p. 31, each folio read off the page. What stands
    there: the section's main theorem, printed p. 46, "Let f: X to Y be a proper
    morphism of noetherian schemes with Y = Spec A affine, and F a coherent
    sheaf on X, flat over Y", gives a finite complex of finitely generated
    projective A-modules computing H^p(X x_Y Spec B, F x_A B); Corollary 2,
    printed pp. 50--51, states that for Y reduced and connected and F as in the
    theorem, the constancy of y to dim H^p(X_y, F_y) is equivalent to R^pf_*(F)
    being locally free with the natural map R^pf_*(F) x k(y) to H^p(X_y, F_y) an
    isomorphism for all y; Corollary 3, printed p. 53, states that if
    H^p(X_y, F_y) vanishes for all y, then R^{p-1}f_*(F) x k(y) to
    H^p-1(X_y, F_y) is an isomorphism for all y. Corollary 3 at p = 1 and
    Corollary 2 at p = 0 are exactly the two facts the step attributes to
    Mumford's p. 53, and the step now names both with their pages. The previous
    event's caveat that Hartshorne III.12.11 asks for a projective morphism is
    discharged: Mumford's theorem is stated for a proper morphism, so nothing in
    the step needs projectivity, and the rendered step no longer points to
    Hartshorne for this statement, the page numbers standing in the event above.
    Not checked: Mumford's printed pp. 48--49, 52 and 54 onwards, that is the
    proof of the section's theorem and the rest of Chapter II; the scan is not in
    a retained set and was removed after the reading, so a later session must
    fetch it again before re-reading these pages.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The first of the two analytic inputs of Youcis's proof is now read, so the
    step that transcribes him cites it by page and by its statement. Source:
    P. Deligne, "Théorie de Hodge : II", Publications mathématiques de
    l'I.H.É.S. 40 (1971), pp. 5--57, read in the numdam copy, where the first
    PDF page is numdam's notice, PDF p. 2 is printed p. 5 and PDF p. 3 carries
    the folio 6, so printed p. N is PDF p. N-3; the pages cited were read in the
    text layer at those positions and their folios checked. Rappel (4.4.3),
    printed p. 51, reads: "Soit S un schéma lisse de type fini sur C. La
    construction (4.4.2) établit une équivalence de catégorie entre: a) la
    catégorie des schémas abéliens sur S; b) la catégorie des familles continues
    polarisables de structures de Hodge H de type (-1,0)+(0,-1) sur S, telles
    que H_Z soit sans torsion et que la filtration de Hodge varie
    holomorphiquement sur S." The construction is (4.4.2), printed p. 50, under
    section 4.4, "Homomorphismes de schémas abéliens": for an abelian scheme
    f: X to S the exponential gives the exact sequence 0 to R^1f_*Z to Lie(X) to
    X to 0 and the Hodge filtration is 0 to Ker(a) to R^1f_*Z (x) O_S to Lie(X)
    to 0, with (4.4.1) on the same page giving R^1f_*Z for a proper smooth f as
    the local system of homology of the fibres, of weight -1. So Youcis's
    sentence is Deligne's (4.4.3) and his map is Deligne's construction. Two
    qualifications now on the card: Deligne states it as a rappel, not as a
    theorem proved there, and he gives its essential surjectivity to Borel [13],
    full faithfulness resting on the Hom-scheme of two abelian schemes being
    unramified over the base. Not checked: Deligne's section 4.4 beyond printed
    pp. 50--51, Borel's paper as he cites it, and the manuscript's other
    sections; the second analytic input, the constancy of the Q-variation over a
    compactification, still rests on the cited Peters and Steenbrink and on
    Strauch's rigidity result, neither of which is on this machine, and the
    numdam copy was removed after the reading.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Correction of the pagination and of the rendered derivation of Katz and
    Mazur's proof of Theorem 2.1.2, in the event of this date above that gives
    them as printed pp. 63--66, and in the rendered solution and remark. (i) The statement of Theorem 2.1.2 ends on
    printed p. 63, which is PDF p. 75; the proof begins on printed p. 64, PDF
    p. 76; and its last line, "are inverse isomorphisms. Q.E.D.", and the
    invocation of (1.2.7) stand on printed p. 67, PDF p. 79, where (2.2) begins
    below them. Printed p. 66, PDF p. 78, stops in the middle of the
    effective-Cartier-divisor argument. (ii) The rendered derivation is now
    Katz and Mazur's argument in their order: the bijection
    E(T) -> Pic^(1)(E_T/T) (printed p. 64); the reduction to T = S and the
    Zariski-local patching using f_*O_E = O_S (printed p. 65); the reduction to
    S affine noetherian (printed p. 66); R^1f_*L = 0 because R^1f_* is of
    formation compatible with arbitrary base change for f proper and flat of
    relative dimension one (the case p = 2 of Mumford's Corollary 3), and over
    an algebraically closed field H^1 of an invertible sheaf of degree one on a
    genus-one curve vanishes, so the coherent sheaf R^1f_*L has zero fibres and
    is zero by Nakayama; f_*L
    locally free of rank one from Mumford, *Abelian Varieties*, printed p. 53,
    Corollary 3 at p = 1, the fibres H^0 being one-dimensional by Altman and
    Kleiman (1.4) at printed p. 164 and (1.15) at printed p. 167; and a local
    basis of f_*L giving an effective Cartier divisor of degree one, hence a
    section by (1.2.7) on printed p. 67. The earlier rendering, which used
    Mumford's Corollary 3 at p = 1 for "constancy of h^0" and Corollary 2 at
    p = 0 for the invertibility, with S = A^1_C reduced and connected, is
    withdrawn: Corollary 3 at p = 1 is the base-change isomorphism for
    R^0f_*, the constancy of h^0 is the fibre computation, the vanishing of
    R^1f_* is the relative-dimension-one and Nakayama argument, and no
    reducedness or connectedness of S or of T is used. Checked in this pass:
    the pages of the scan named in (i), at 160 dpi; Mumford's printed
    pp. 50--53 on the wstein.org scan, whose folios were read; and Altman and
    Kleiman's printed pp. 164 and 167, whose folios were read. Not checked:
    Mumford's printed pp. 54 onwards, and the card's other steps were not
    re-derived.
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
The proof is A. Youcis, *Abelian schemes over the integers* (2016), section "The case over the complex line", once the family is one of abelian varieties over $S$, which is step [](#abelian-scheme){.pf-ref} and is Katz and Mazur's Theorem 2.1.2.
His Theorem 8 is stronger than the exercise and is applied to $V=S$ in step [](#conclusion){.pf-ref}.

::: pf

::: {.pf-step #abelian-scheme}

$E\to S$ is a smooth proper group scheme over $S$ with geometrically connected fibres, with identity $O$: a family of abelian varieties over $S$ in the sense of Youcis.

::: pf-proof

The data are an elliptic curve over $S$ in the sense of Katz and Mazur, *Arithmetic Moduli of Elliptic Curves* (1985), (2.1.1), printed p. 63: "Let $S$ be an arbitrary scheme. An elliptic curve $E/S$ is a proper smooth curve" --- their display carries the morphisms $E\to S$ and the section "$0$" --- "with geometrically connected fibers all of genus one, given with a section '$0$'." The exercise gives exactly that: $\pi\colon E\to S$ proper and smooth with fibres of genus $1$, and the section $O$.

Katz and Mazur, Theorem 2.1.2 (Abel), printed p. 63, proved on printed pp. 64--67: "There exists a unique structure of commutative group-scheme on $E/S$ such that for any $S$-scheme $T$, and any three points $P,Q,R$ in $E(T)=E_T(T)$, we have
$$
P+Q=R
$$
if and only if there exists an invertible sheaf $\mathcal L_0$ on $T$ and an isomorphism of invertible sheaves on $E_T$
$$
I^{-1}(P)\otimes I^{-1}(Q)\otimes I(0)\cong I^{-1}(R)\otimes f_T^*(\mathcal L_0)."
$$
There $I(P)$ is the ideal sheaf of a section $P$ viewed as an effective Cartier divisor of degree one in $E$, and $f_T\colon E_T\to T$ is the projection.

Their proof is Abel's theorem in the relative setting, and it runs on printed pp. 64--67. The map $E(T)\to\Pic^{(1)}(E_T/T)$, $P\mapsto$ the class of $I^{-1}(P)$, where $\Pic^{(1)}(E_T/T)$ is the set of isomorphism classes of invertible sheaves on $E_T$ that are fibrewise of degree one modulo those of the form $f_T^*(\mathcal L_0)$ with $\mathcal L_0$ on $T$, is what they prove bijective (printed pp. 64--67). Given the bijection, $I^{-1}(P)\otimes I^{-1}(Q)\otimes I(0)$ is fibrewise of degree one, hence is isomorphic to $I^{-1}(R)\otimes f_T^*(\mathcal L_0)$ for a unique $R\in E(T)$; composing with $\Pic^{(1)}(E_T/T)\to\Pic^{(0)}(E_T/T)$, $\mathcal L\mapsto\mathcal L\otimes I(0)$, transports the group law of the abelian group $\Pic^{(0)}(E_T/T)$ to $E(T)$, functorially in $T$, and the bijection is what makes that law unique.

For the bijection they reduce to $T=S$ (printed p. 65) and then show that the question is Zariski local on $S$: if $\{U_i\}$ is an affine open cover and $\phi_i\colon\mathcal L\cong\mathcal L'\otimes f^*(\mathcal L_{0,i})$ on $f^{-1}(U_i)$, then $f_*\OO_E=\OO_S$ and $f_*f^*(\mathcal L_{0,i})=\mathcal L_{0,i}$ show that $f_*(\mathcal L^{-1}\otimes\mathcal L')$ and $f_*(\mathcal L\otimes(\mathcal L')^{-1})$ are inverse invertible sheaves, so there are $\mathcal L_0$ on $S$, namely $f_*(\mathcal L\otimes(\mathcal L')^{-1})$, and an isomorphism $\mathcal L\cong\mathcal L'\otimes f^*(\mathcal L_0)$ (printed p. 65). Since $E/S$ is of finite presentation, this leaves $S$ affine noetherian (printed p. 66).

Let $\mathcal L$ be invertible on $E$, fibrewise of degree one. Their claim (printed p. 66) is that $f_*\mathcal L$ is invertible of formation compatible with arbitrary base change and that $R^1f_*\mathcal L=0$, and they prove the vanishing first: $R^1f_*\mathcal L$ is of formation compatible with arbitrary base change --- "being an $R^1f_*$ for $f$ proper and flat of relative dimension one", which is the case $p=2$ of Mumford's Corollary 3 at printed p. 53, $H^2$ of a curve vanishing --- and over an algebraically closed field $H^1(E,\mathcal L)=0$ because $\deg\mathcal L=1>2g-2=0$, so the coherent sheaf $R^1f_*\mathcal L$ has all fibres zero and vanishes by Nakayama's lemma. Then Mumford, *Abelian Varieties* (1970), p. 53, cited by Katz and Mazur as [Mum 4], gives that $f_*\mathcal L$ is locally free and of formation compatible with arbitrary base change: Corollary 3 there, at $p=1$, is the isomorphism $f_*\mathcal L\otimes k(y)\cong H^0(E_y,\mathcal L_y)$ for every $y$, and the right side is one-dimensional for every $y$, being so over an algebraic closure of $k(y)$, so $f_*\mathcal L$ is locally free of rank one by Nakayama, and a base-change map between locally free sheaves that is an isomorphism on every fibre is an isomorphism. Over an algebraically closed field $h^0(\mathcal L)=\chi(\mathcal L)=\deg\mathcal L+\chi(\OO)=1+0=1$ by Altman and Kleiman, *Introduction to Grothendieck Duality Theory* (1970), Theorem (1.4) (Riemann), printed p. 164, and $H^1(\mathcal L)\cong H^0(\omega\otimes\mathcal L^{-1})^*=0$ by their Theorem (1.15) (Roch), printed p. 167, the sheaf $\omega\otimes\mathcal L^{-1}$ having degree $2g-2-1=-1$.

With $f_*\mathcal L$ invertible they choose a local $\OO_S$-basis $\ell$ and show that $\OO_E\to\mathcal L$, $1\mapsto\ell$, is injective and remains so after any base change, reducing to $S$ the spectrum of a field, where $\ell$ is a nonzero $k$-basis (printed p. 67); hence $(\mathcal L,\ell)$ is an effective Cartier divisor in $E/S$, of degree one fibrewise, and by (1.2.7), printed pp. 10--11 and invoked on printed p. 67, an effective Cartier divisor of degree one is a section $P\in E(S)$. The two constructions are inverse to each other, so the map $E(S)\to\Pic^{(1)}(E/S)$ is bijective (printed p. 67).

That is a group scheme over $S$ with identity $O$ in the sense of the definition before Remark 4.10.5, printed p. 324: the identity is the section $O$, the inverse and the operation are morphisms over $S$, and the two axioms asserted there are the group-scheme axioms of Katz and Mazur. Since $\pi$ is smooth and proper with geometrically connected fibres, $E$ is an abelian scheme over $S$ in the sense of Youcis, "a smooth proper group scheme with connected fibers", from his section "Two statements of the main result".

On a fibre the law is the classical one. At $T=\Spec\CC$ over a closed point $t\in S$ the condition reads $I^{-1}(P)\otimes I^{-1}(Q)\otimes I(O)\cong I^{-1}(R)$ in $\Pic E_t$ for $P+Q=R$, which is the identification of the genus-one curve $E_t$ with its own Picard group of degree zero, Hartshorne Theorem 4.11, printed p. 325, whose last clause identifies the group structure of Remark 4.10.6, printed p. 324, with the classical one.

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

First, "By 4.4.3 of Deligne's *Théorie de Hodge II* there is an equivalence of categories between abelian schemes and polarizable $\ZZ$-variations of Hodge structure. The map is given by $\mathscr A\mapsto(R^1f^{\text{an}}_*\underline{\ZZ})^\vee$." The cited statement is Deligne, *Théorie de Hodge II*, (4.4.3), printed p. 51: "Soit $S$ un schéma lisse de type fini sur $\CC$. La construction (4.4.2) établit une équivalence de catégorie entre: a) la catégorie des schémas abéliens sur $S$; b) la catégorie des familles continues polarisables de structures de Hodge $H$ de type $(-1,0)+(0,-1)$ sur $S$, telles que $H_\ZZ$ soit sans torsion et que la filtration de Hodge varie holomorphiquement sur $S$." The construction it names is (4.4.2), printed p. 50: for an abelian scheme $f\colon X\to S$ the exponential gives the exact sequence $0\to R^1f_*\ZZ\to\operatorname{Lie}(X)\to X\to 0$, and the Hodge filtration is the exact sequence $0\to\ker(a)\to R^1f_*\ZZ\otimes\OO_S\to\operatorname{Lie}(X)\to 0$. Deligne states the equivalence as a *rappel* and gives its essential surjectivity to Borel [13], the full faithfulness resting on the scheme of homomorphisms of two abelian schemes over $S$ being unramified over $S$.

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
Step [](#abelian-scheme){.pf-ref} makes $E\to S$ a family of abelian varieties over $V=S$.
With it, Theorem 8 applies through its proof in step [](#deligne-argument){.pf-ref} and $E\to S$ is isotrivial, that is, by step [](#constant-family){.pf-ref}, a product $E_0\times_\CC\AA^1_\CC$ over $\AA^1_\CC$.
That is the triviality the exercise asks for.

:::

:::

:::

:::

::: {.remark title="Published solution"}

Youcis's Theorem 8, section "The case over the complex line", proves the exercise once the family is one of abelian varieties in his sense, and more: the base may be any smooth connected complex algebraic variety with simply connected analytification, and the fibres may be abelian varieties of any dimension.
The passage from the exercise's family, which carries a section, to a family of abelian varieties is step [](#abelian-scheme){.pf-ref}: Katz and Mazur's Theorem 2.1.2, printed p. 63, with its proof on printed pp. 64--67. The printed hint's first clause, "Use the section to fix the group structure on the fibres", asks for exactly that theorem.
Its two analytic inputs are cited rather than proved there: the equivalence of Deligne, *Théorie de Hodge II*, (4.4.3), printed p. 51, stated there as a *rappel* with its essential surjectivity given to Borel, and the constancy of the $\QQ$-variation of Hodge structure over a compactification, for which his remark after the proof invokes the cited result of Peters and Steenbrink together with the rigidity result of Strauch that he takes from a MathOverflow post.
The section closes with his remark that the theorem "becomes wildly false" outside the algebraic category, the family of elliptic curves over the upper half-plane $\halfplane$ with $g_4$ and $g_6$ the level-one modular forms being non-isotrivial although $\halfplane$ is simply connected, and that $\halfplane$ is not algebraic is what saves the theorem.

The printed hint follows a different route: the points of order $2$ form an étale cover of $\AA^1_\CC$, hence are four disjoint sections, and the Legendre parameter $\lambda$ they define is a morphism $\AA^1_\CC\to\AA^1_\CC\setminus\{0,1\}$, hence constant.
Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.4.22, printed p. 95, carries that hint out: the four $2$-torsion sections, four copies of $\AA^1_\CC$ because $\AA^1_\CC$ is simply connected, the coordinates $\infty,0,1,\lambda$ on each fibre, and $\lambda$ constant.
That route ends at the constancy of $\lambda$, which is equality of the fibres, and does not by itself give the triviality of the family.

:::
