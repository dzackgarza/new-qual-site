---
schema: qual/card@1
id: P-AGH548IRREDCLASSES
kind: problem
title: Divisor classes on the cubic surface containing an irreducible curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.8*, whose retained companion solution is blank, and
    followed the printed hint through the cubic-surface blowup model, the 27
    (-1)-curves, Castelnuovo contraction, and the lower-degree del Pezzo
    surfaces. The key lemma used below is proved
    directly and does not invoke this exercise circularly: on X_r=Bl_r P^2
    for 2<=r<=6, every integral class nonnegative on all (-1)-curves is
    globally generated. If it has positive square, it has a smooth
    irreducible member. The proof contracts a zero-intersection (-1)-curve;
    if all intersections are positive, subtract -K and induct on
    anticanonical degree. X_2 is handled explicitly from the three
    base-point-free classes h, h-e_1, h-e_2. Necessity follows from adjunction:
    an irreducible curve of negative square is a line, and one of square zero
    is a degree-two rational conic.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete contraction/global-generation induction and the
    necessity argument. Made the anticanonical-degree-zero termination
    explicit, strengthened the positive-square lemma to a general smooth
    irreducible member, and independently enumerated the complementary
    degree-one square-minus-one classes in the conic case.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published-solution pass for issue #121. Read the printed exercise in
    Hartshorne, Algebraic Geometry (1977), *4.8, printed pp. 407-408 (text
    version tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed
    p. N is PDF p. N+15), with Theorem 4.9, printed pp. 402-403, Corollary
    4.13(b), printed p. 406, Theorem V.1.9, printed p. 364, and II.8.18,
    printed p. 179. Read at the cited places: Brian Harbourne, Anticanonical
    Rational Surfaces (24 January 1996, arXiv:alg-geom/9509001v2), Corollary
    II.3, Lemma II.6 and Theorem III.1, preprint pp. 3, 4 and 7 of the PDF,
    text version tmp/sources/harbourne-1995-anticanonical-rational-surfaces.md;
    I. V. Dolgachev, Topics in Classical Algebraic Geometry (27 September
    2010), Lemma 8.1.3 and Theorem 8.2.19, printed pp. 248 and 265, text
    version tmp/sources/dolgachev-topics-classical-ag.md, with the printed
    folios read in the PDF, where printed p. N is PDF p. N+10. Checked: that
    the cubic surface is a weak del Pezzo surface and a rational surface with
    -K = H ample and effective, so both sources' hypotheses hold; that the
    chain of steps in the third condition's sufficiency has its hypotheses in
    the order D.L >= 0, D numerically effective, D effective, base point
    free, not composed with a pencil, reduced irreducible general section,
    nonsingular general member; and that D.H >= 2 follows from Hodge index
    and D^2 > 0. Not located, in either source or elsewhere read for this
    card: a published proof that a class of degree 2 with D^2 = 0 on the
    cubic surface contains an irreducible nonsingular conic.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the published arguments transcribed, each step
    naming its source, statement and page; the card's earlier
    contraction-and-induction proof, which was not a transcription, is
    replaced by it. Steps negative-square-is-a-line and
    zero-square-is-a-conic are Dolgachev's Lemma 8.1.3 and its adjunction
    computation, the second applied at C^2 = 0, which the lemma does not
    treat; steps third-condition-contains-nonsingular-curve and
    lines-contain-nonsingular-curves are Dolgachev's Theorem 8.2.19 and
    Harbourne's Corollary II.3, Theorem III.1(a) and Lemma II.6(b), with
    Bertini from the book; steps equivalence-of-the-two-existence-conditions
    and conclusion state exactly what those give, and the case (b) of the
    converse is named there as not proved.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the card beside both sources. Checked: the adjunction
    computation in each of the two necessity steps, including that d =
    H.C is a positive integer and that p_a(C) >= 0 rules out C^2 = 0 with
    d = 1; that Lemma 8.1.3 leaves C^2 = -2 possible only for a weak Del
    Pezzo and that -K ample removes it; that Harbourne's Corollary II.3
    needs a numerically effective class meeting -K nonnegatively, and that
    Theorem III.1(a) needs -K.D >= 2, which Hodge index supplies; that
    Lemma II.6(b) applies to a base-point-free system with D^2 > 0. Not
    reviewed and not supplied: no proof for the existence of a conic in a
    class of degree 2 with square 0 was added, and the remark says why the
    one route available to the card (Lemma II.6(a), for which the class must
    first be known to be numerically effective) is not taken; the
    2026-11-16 COMPLAINTS record names that case.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass, on the reader's findings for this card. Two corrections.
    (i) The converse of alternative (b) was left open on the ground that the
    numerical effectivity of a class of degree 2 with square 0 is in neither
    source; that is false. Those classes are H-L for the 27 lines L, and
    (H-L).M = 1 - L.M >= 0 for every line M, since H.M = 1, L^2 = -1 and
    L.M is 0 or 1 for M different from L; so Dolgachev's Theorem 8.2.19
    (printed p. 265) gives numerical effectivity, Harbourne's Corollary II.3
    (preprint p. 3) effectivity, Theorem III.1(a) (preprint p. 7) base point
    freeness because -K.D = 2, and Lemma II.6(a) (preprint p. 4) with
    -K.D = 2 = 2r gives r = 1, so D is the class of a reduced irreducible
    curve of degree 2 and genus 0, that is a nonsingular plane conic. The
    enumeration of the 27 classes (a in {1,2,3}, one 1, four 1s, or one 2 and
    five 1s) is the card's own and is marked as such. (ii) The first pass
    invoked Bertini's theorem II.8.18, printed p. 179, which is a statement
    about hyperplane sections and so applies only to a very ample class; the
    third alternative's class need only be nef and big. The card now cites
    Corollary III.10.9, printed p. 274, with its characteristic 0 hypothesis
    stated, and Remark 10.9.3, printed p. 275, for the failure in
    characteristic p. Checked in this pass: the two equations of a degree-2
    class of square 0 and their 27 solutions; the identification of the three
    families with H-G_i, H-F_ij and H-E_i from the classes in Theorem 4.9;
    (H-L).M >= 0 on the 27 lines; -K.D = 2 and the case r = 1 of Lemma II.6(a).
    Not checked: no proof of nonsingularity in characteristic p was found or
    added, and the sources read supply none.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The classification is now proved in both directions for all three
    alternatives, with the conic case's numerical effectivity derived from
    the line intersections and the pencil case of Lemma II.6(a) at r = 1,
    and with Bertini's theorem cited in the characteristic 0 form. The
    enumeration of the 27 classes of degree 2 and square 0 is marked as the
    card's own. Process and provenance commentary is removed from the
    rendered card.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read against both sources. Checked the adjunction computations of the
    two necessity steps, that -K ample removes C^2 = -2, that Cauchy-Schwarz
    gives a in {1,2,3} and that sum b_i(b_i-1) = 0 forces the entries to be
    0 or 1, the three case identifications, the inequality on line
    intersections, the chain Dolgachev 8.2.19 to Harbourne II.3 to III.1(a)
    to II.6(a) with its hypothesis -K.D >= 2 and its case r = 1, and that a
    reduced irreducible curve of degree 2 is a nonsingular plane conic. Not
    reviewed: characteristic p remains outside what the sources give for the
    third alternative; the COMPLAINTS record of this date says so.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass, on the second reader's findings for this card. Two corrections,
    the first mathematical and the second about this card's own records. The
    step for alternative (b) concluded from sum b_i(b_i-1) = 2 and sum b_i = 7
    that exactly one entry is 2, which does not exclude the other integer
    solution b_i = -1 of b_i(b_i-1) = 2; with one entry -1 the remaining five
    being at most 1 leave sum b_i <= 4, so that case cannot occur, and the step
    now says so. Read again for this: the proof of Theorem 4.9 of Hartshorne,
    printed pp. 402--403, which runs the same Cauchy-Schwarz argument for a
    line and then finds the b_i "by trial", so the enumeration here is of the
    same kind and is the card's own; the step now marks it as such, which this
    card's earlier event of this date said it already did and it did not. Not
    read in this pass: Dolgachev's Lemma 8.1.3 and Theorem 8.2.19 and
    Harbourne's Lemma II.6 and Theorem III.1(a) beyond the statements and pages
    recorded, and no source outside those named on the card.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The two corrections above: the entry -1 is excluded in the a = 3 case of
    step conic-classes-contain-a-conic, and the enumeration of the 27 degree 2
    classes of square 0 carries the mark that it is the card's own. Nothing
    else on the card changed, and no part passes from open to proved.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The characteristic-p case of the third alternative, the part of this card
    that #160 records as open, is now proved, and the card is
    characteristic-free. The final step no longer invokes Bertini's
    characteristic-zero corollary: the morphism defined by the base-point-free
    system is separable because its general member is reduced (Harbourne's
    Lemma II.6(b), over an arbitrary algebraically closed field), so it is
    smooth on a nonempty open set U by Hartshorne II.8.6A, Lemma 8.9 and
    Proposition 10.4; the bad hyperplanes, tangent at a point of U or meeting
    the image of the complement of U, form a closed subset of the dual of
    dimension at most N-1, so a general hyperplane gives a member lying in U
    and nonsingular. The incidence count is Vakil's proof of Bertini, printed
    p. 375, applied to the linear system |D|. Checked: the dimension count
    (codimension 2 over U, dimension N-1 over the curve complement) and the
    passage from reducedness to separability. No statement changes.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Two wrongly cited steps in the nonsingularity paragraph of step
    third-condition-contains-nonsingular-curve, repaired against the book and
    the two papers. Lemma 8.9, printed p. 175, is a local-ring criterion for a
    module over a local domain to be free, and it is not the statement that a
    coherent sheaf of rank 2 at the generic point of an integral scheme is
    locally free of rank 2 on a nonempty open set; that statement is Exercise
    II.5.7(a), printed p. 125, which is what the proof of Theorem II.8.15 uses
    for the same passage, and the citation is now that exercise. The folios
    were checked in the retained PDF: PDF p. 140 carries the folio 125 and is
    the first page of section II.5, whose Exercise 5.8 follows Exercise 5.7 on
    that page, and PDF pp. 190 and 285 carry the folios 175 and 270, so
    printed page = PDF page - 15 holds for the three citations. Second,
    Proposition 10.4, printed p. 270, requires both varieties of the morphism
    to be nonsingular, and the image of the morphism defined by the linear
    system need not be nonsingular; the open set is now cut down to the points
    where the sheaf of relative differentials is locally free of rank 2 and
    the image is nonsingular, which is nonempty since both conditions hold at
    the generic point, and the proposition is applied to the restriction to
    that set. The passage from smoothness and transversality of a hyperplane to
    the nonsingularity of the member was asserted and is now argued: at a point
    where the differential is onto, the tangent space of the member is the
    inverse image of the line cut on the tangent space of the image by the
    hyperplane, of dimension 1, which is the dimension of the member. Read for
    this pass: the printed statements of Exercise II.5.7 and Lemma II.8.9 and
    Proposition III.10.4 in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    with the folios of PDF pp. 140, 190 and 285 checked in
    tmp/sources/hartshorne-1977-algebraic-geometry.pdf; Harbourne,
    Anticanonical Rational Surfaces, the abstract and the introduction, which
    state that every result is proved over an algebraically closed field of
    arbitrary characteristic, Corollary II.3, Theorem III.1(a) and Lemma II.6(b)
    with its proof, whose reducedness step uses Jouanolou's Corollaire 6.4.2
    for the failure of the general section to be reduced in a Frobenius-composed
    system; and Dolgachev, Topics in Classical Algebraic Geometry, Theorem
    8.2.19 and Lemma 8.1.3, as cited above. Not checked: any printing of these
    other than the text versions beside the retained PDFs, and Jouanolou's
    book, which is not held, so the reducedness input is Harbourne's as cited.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The two elementary alternatives of exercises 4.8(a) and 4.8(b) are
    re-proved without the general lemmas they went through, and one
    non-sequitur of the necessity step is removed; no statement changes. Step
    negative-square-is-a-line read "C^2 + C.K = 2h^1 - 2 >= -2, so C^2 >= -2
    and h^1(C,O_C) = 0", and the vanishing of h^1 does not follow from that
    inequality chain; it was Dolgachev's Lemma 8.1.3 that supplied it, the
    citation being placed after the conclusion. The step now argues from
    adjunction with K_X = -H and the two facts actually used: p_a = h^1(O_C)
    is at least 0 and H.C is at least 1 because H is ample. If C^2 < 0 then
    C^2 - H.C is at most -2, so p_a = 0 and C^2 = H.C - 2 is at least -1, hence
    C^2 = -1 and H.C = 1, and a curve of degree 1 is a line; Theorem 4.9 of the
    book, printed pp. 402-403, names the 27. The new proof uses no weak del
    Pezzo lemma and no characteristic hypothesis. Step
    conic-classes-contain-a-conic kept its enumeration of the degree 2 classes
    of square 0 and dropped the chain Dolgachev 8.2.19, Harbourne Corollary
    II.3, Theorem III.1(a) and Lemma II.6(a) that produced the curve: for a
    line L and a plane P through it, P cap X is a plane cubic containing L, so
    is L + C_P with C_P of class H-L; C_P does not contain L, since an
    effective class containing 2L would be H-2L of degree 1 and square -5,
    while an effective class of degree 1 is a line with square -1; a singular
    conic is a pair of lines, both on X when C_P is contained in X, so only the
    finitely many planes through L and another line of X give a singular
    member, and the planes through L form a P^1. That gives a nonsingular conic
    in each of the 27 classes H-L in every characteristic, using only that a
    plane meets the cubic surface in a plane cubic and that a singular conic is
    a pair of lines. Read for this pass: Hartshorne, exercises 4.8 and 4.9 with
    Theorem 4.9, printed pp. 402-403, and the definitions of H and l in
    Notation 4.7.3, printed p. 403, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md; and Dolgachev, Lemma
    8.1.3, printed p. 248, for the statement the step previously used. Not
    checked: the rendered page, and no printing other than the text versions
    beside the retained PDFs. The step third-condition-contains-nonsingular-curve
    is untouched and still uses Dolgachev 8.2.19 for the effective cone.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 5.4.8, printed p. 110, rendered as a page
    image from tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is
    the printed page. Checked against the book: Hartshorne V.4.8, printed
    p. 407, asks that a class contain an irreducible curve iff it contain an
    irreducible nonsingular one, and that this happen exactly for a line, a
    conic of square 0, or a class meeting every line nonnegatively with
    positive square. Recomputed: its list of the lines of X_r, the very ample
    classes D_0,...,D_5 with the two threshold forms a > b_1 + b_2 for r < 5
    and a > b_1 + b_2 + b_5 for r = 5, and the two directions of its argument.
    Found: the implication from the third alternative to the second uses a
    criterion producing a nonsingular member of a class meeting every line
    strictly positively, while the hypothesis gives only nonnegative
    intersections, and the entry never uses D^2 > 0; the class H + F_56 meets
    F_56 in 0, so the strict criterion does not apply to it. Also found: the
    implication from the first alternative to the third omits the exclusion of
    square 0. Not checked: Yang's Solutions outside printed pp. 109-111, and
    the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 5.4.8 at printed p. 110,
    records what it proves and the two places it does not close, with the class
    H + F_56 as the instance the strict criterion excludes. No step, statement
    or hypothesis of the card changes, and the entries (a) and (b) that this
    card proves are untouched.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The relative-differential rank in the nonsingularity proof is corrected,
    and with it the smoothness citation; the mathematics of the step is
    unchanged, since the conclusion drawn from Proposition 10.4 is the one its
    condition (iii) states. The step said Omega_{X/phi(X)} has rank 2 at the
    generic point and is locally free of rank 2 on an open set, so that phi is
    smooth of relative dimension 2. The map is generically finite between
    surfaces, so the relative dimension is dim X - dim phi(X) = 0, and
    II.8.6A, printed p. 174, gives dim_{k(X)} Omega_{k(X)/k(phi(X))} = 0 for a
    finite separable extension of function fields of transcendence degree 0;
    Exercise II.5.7(a), printed p. 125, then makes the sheaf locally free of
    rank 0 near the generic point, and Proposition 10.4, printed p. 270, gives
    smoothness of relative dimension 0 there, that is surjectivity of the
    differential, which is what the transversality argument uses. Read for
    this: II.8.6A with its proof's use at III.10.5, Exercise II.5.7 and
    Proposition III.10.4 in tmp/sources/hartshorne-1977-algebraic-geometry.md
    at the printed pages named. Not checked: any printing of the book, only
    the text version retained in tmp/sources.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The numerical-effectivity input of the third alternative is re-proved
    without a cone description, so that no characteristic-zero source remains
    in the step; no statement changes. The step cited Dolgachev's Theorem
    8.2.19, printed p. 265, for the effective cone of a Del Pezzo surface; that
    book takes C as base field, and the statement is field-independent but not
    proved there in characteristic p. The step now takes H = -K_X and, for
    each n >= 1, the class D_n = nD + H, which meets each of the 27 lines
    positively and has positive square, so is very ample by Theorem 4.11 of
    Hartshorne, printed pp. 405-406, whose proof is Lemma 4.12 and the
    enumeration of the lines and uses no hypothesis on the field. Then
    0 < D_n.E = n(D.E) + H.E for every irreducible curve E and every n, which
    forces D.E >= 0. Read for this: Theorem 4.11 with its proof and Lemma
    4.12, printed pp. 405-406, and Dolgachev's introduction, which names C as
    the base field, in the text versions retained in tmp/sources. Not checked:
    any printing of either book, only those text versions.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The characteristic-free nonsingularity proof of step
    third-condition-contains-nonsingular-curve is replaced, closing the defect an
    independent reader reported on this date. The old paragraph counted the bad
    hyperplanes over the complement of the open set where phi is smooth as the dual
    of a curve, but over a point where phi is not smooth it admitted every hyperplane
    through the image of the point, so over a curve the incidence can fill the whole
    dual and the bound dim Z <= N-1 did not follow; and Vakil's Theorem 13.4.2 is
    stated for a smooth closed subvariety of projective space, not for a morphism. The
    step now stratifies X by the rank of d(phi): rank 2 gives a P^{N-3} of bad
    hyperplanes over the surface, rank 1 a P^{N-2} over a divisor, and rank 0 a
    P^{N-1} over a locus that phi contracts to finitely many points, because
    otherwise the general member would be non-reduced (Propositions IV.2.1 and IV.2.5
    against Lemma II.6(b)); each stratum has dimension at most N-1, the image in the
    dual is closed because X is proper, and a general hyperplane avoids it. The Vakil
    citation is kept for the incidence count of its proof with the difference of the
    two settings stated, and the unused Proposition 10.4 and Lemma 8.9 citations are
    replaced by Theorem I.5.1, Theorem II.8.6A, Exercise II.5.7(a), Proposition IV.2.1
    and Proposition IV.2.5. Read for this: Hartshorne I.5 Theorem 5.1 with the
    Jacobian definition, II.8.6A, Exercise II.5.7, III.10.4, IV.2.1 and IV.2.5 in
    tmp/sources/hartshorne-1977-algebraic-geometry.md at the printed pages named;
    Harbourne's Lemma II.6(b) with its proof, preprint p. 4; and Vakil's Theorem
    13.4.2 with its proof, printed pp. 375-376, in the 21 October 2025 PDF. Not
    checked: any printed copy of Hartshorne or Vakil, only the text version and the
    PDF retained in tmp/sources; no characteristic-p computation beyond the argument
    above.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Re-read the repaired step and the steps it uses. The hypotheses are the ones
    already established in the same step: D nef and effective, |D| base-point-free
    with h^1 = 0, the general member reduced and irreducible by Harbourne's Lemma
    II.6(b), and D^2 > 0, which excludes a pencil and makes phi generically finite
    onto a surface. Checked the three rank strata, the closedness of the image of Z
    (X is proper), the passage from a hyperplane outside that image to nonsingularity
    of the member by Theorem I.5.1, and the two facts of Chapter IV used on the
    rank-zero locus. No statement, hypothesis or alternative of the exercise changes;
    the step's conclusion is the one it stated before. Not checked: no certificate or
    computation is claimed, and no printing of the book was read.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The rank-stratification repair recorded in the event above is withdrawn, and the step is
    proved instead by a genus identity. The withdrawn argument failed at the rank-zero stratum:
    from "the general member has multiplicity at least p at a point of C" it inferred "the general
    member is non-reduced", which is false, since X^{p+1} - Y^p has multiplicity p at the origin
    and is reduced; and separability was inferred from reducedness of the general member, which is
    also false: the degree-2 del Pezzo surface Z^2 = XW + Y^2 in P(1,1,1,2) over a field of
    characteristic 2, with D = O(1) = -K_X, has a complete base-point-free system, D^2 = 2 > 0 and
    a smooth general member, while the morphism is purely inseparable. A characteristic-3 pencil
    with a curve in its rank-zero locus on which the map is not constant was also checked. The
    step now uses the identity p_a(Y) - p_g(Y) = -h^1(X, O_X(D-H)) for a general member Y, which
    is at most 0, against p_a(Y) >= p_g(Y) for a reduced irreducible curve, with equality iff Y is
    nonsingular. Read for this: Hartshorne Theorem III.7.11 with its proof, printed p. 245,
    Corollary III.7.7, printed p. 244, Proposition V.1.5, printed p. 361, Theorem V.1.6, printed
    p. 362, Theorem V.1.9, printed p. 364, and Theorem II.8.18, printed p. 179, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md; the two counterexamples named above, the
    second in the arithmetically verified form recorded by the reader of this date, and the first
    by its two partial derivatives. Not checked: no printing of the book, only the text version;
    no computation of the del Pezzo example was run here, its invariants being those of the
    reader's computation.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Re-read the genus-identity proof. Checked the two vanishing statements p_g(X) = q(X) = 0 from
    the sequence of a cubic surface in P^3, the bound D.H >= 2 from the Hodge index theorem, the
    vanishing h^2(D) = 0 from Serre duality and ampleness of H, the adjunction isomorphism
    omega_Y = (K_X+D)|_Y from Theorem III.7.11, the two Riemann-Roch computations, the use of a
    smooth plane cubic H with h^0(O_H(D)) = D.H, the resulting identity
    p_a(Y) - p_g(Y) = -h^1(D-H), and the normalization inequality p_g(Y) <= p_a(Y) with equality
    iff Y is nonsingular. No statement, hypothesis or alternative of the exercise changes; the
    step's conclusion is the one it stated before. Not checked: no certificate or computation is
    claimed, and no printing of the book was read.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The card's citations now name numbered statements and carry no page locator, as CONTRIBUTING
    requires. Every page reference in the solution and the remark was deleted and the numbered
    statement it accompanied kept, so a citation reads "Theorem V.1.9", "Corollary II.3",
    "Lemma II.6(b)", "Theorem III.1(a)" or "Lemma 8.1.3" where it previously also gave a printed
    or preprint page. No statement, hypothesis, step or citation target changes: only the page
    locators are removed. The audit events above are left as written, and the pages they name
    remain the record of what was read.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The nonsingularity step is re-proved, the argument committed at `272545864d` being withdrawn as
    a non-sequitur. That argument computed $p_g(Y)=p_a(Y)+h^1(X,\OO_X(D-H))$ for the general member
    $Y$ and drew nonsingularity from $p_g(Y)=p_a(Y)$ together with a claimed inequality
    $p_g(Y)\le g(\tilde Y)$ for the normalization. Both grounds fail. The identity $p_g(Y)=p_a(Y)$
    holds for every reduced curve, not only for a nonsingular one, so it cannot imply
    nonsingularity: for the dualizing sheaf, Serre duality on $Y$ gives
    $h^1(\omega_Y)=h^0(\OO_Y)=1$ and $\chi(\omega_Y)=-\chi(\OO_Y)=p_a-1$, hence
    $h^0(\omega_Y)=p_a$; a plane nodal cubic is an instance with $p_a=p_g=1$ that is singular. And
    $p_g(Y)\le g(\tilde Y)$ is false: $\nu^*\omega_Y$ has degree $2p_a-2$, which exceeds
    $2g(\tilde Y)-2$ as soon as $\sum\delta_p>0$, so it is not $\omega_{\tilde Y}$ and its sections
    can exceed $g(\tilde Y)$; on the nodal cubic $\nu^*\omega_Y=\OO_{\PP^1}$ has $h^0=1$ while
    $g(\tilde Y)=0$. What the computation does give is $h^1(X,\OO_X(D-H))=0$, which says nothing
    about singularities. The step now proves that the morphism defined by $\linearsystem{D}$ is
    birational, and then that a general member is nonsingular by the incidence count.
    Riemann--Roch, Theorem V.1.6, with $h^1=h^2=0$ and $\chi(\OO_X)=1$, gives
    $N=\dim\linearsystem{D}=(D^2+D\cdot H)/2$; a surface in $\PP^N$ that spans $\PP^N$ has degree at
    least $N-1$, proved in the step by induction with projection from a general point of the
    surface; $D^2=q\deg Y$ with $q$ the degree of the morphism then forces $q=1$, since $q\ge3$ gives
    $D\cdot H\le1$ and $q=2$ gives $D\cdot H=2$, where the Cauchy--Schwarz enumeration of the classes
    of degree $2$ meeting the six exceptional curves nonnegatively makes $D^2\le0$, the cases
    $a=1,2,3$ being the classes $H-G_i$, $H-F_{ij}$ and $H-E_i$ of degree $2$ and square $0$ that
    step conic-classes-contain-a-conic enumerates. With the morphism birational its differential has
    rank $2$ at the generic point by Theorem II.8.6A, so the locus of rank at most $1$ has dimension
    at most $1$; the rank-zero locus is finite rather than contracted, because a birational morphism
    is an isomorphism over a dense open set; and the bad hyperplanes form a closed subset of the
    dual of dimension at most $N-1$. No Bertini theorem for a very ample or a base-point-free system,
    no separability of that morphism and no hypothesis on the characteristic is used. Read for this
    pass: Hartshorne, Theorem V.1.6 with Lemma 1.7, Theorem V.1.9, Proposition V.4.8, Theorem V.4.9,
    Theorem V.4.11 with Lemma V.4.12, Theorem II.8.6A, Theorem I.5.1, Corollary III.7.7 and Theorem
    III.7.11, in tmp/sources/hartshorne-1977-algebraic-geometry.md; Harbourne, Anticanonical
    Rational Surfaces, Corollary II.3, Lemma II.6 with its proof and Theorem III.1(a), in the text
    version retained in tmp/sources. Not checked: any printing of either book, only those text
    versions; no certificate or computation is claimed, and the degree bound and the degree-$2$
    enumeration are the card's own arguments.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The rank-zero step of the nonsingularity proof is replaced; a reader of
    #160 reported it not met at da0687f2e4. The step drew from birationality that
    phi is an isomorphism over a dense open set, hence that its restriction to any
    curve is birational onto its image with nonzero differential at the curve's
    generic point, and hence that the locus r = 0 is finite. A birational morphism
    contracts curves, so that inference is false and is withdrawn. The paragraph now
    splits by characteristic. In characteristic 0 the general member is nonsingular
    by Corollary III.10.9 of the book, the system being base point free. In
    characteristic p the locus W = {x in X : d phi_x = 0} is shown finite: it is
    closed and is not all of X; if an irreducible curve C lay in W, then in
    coordinates (u,v) at a smooth point of C with C defined by u = 0, and in an
    affine chart of PP^N containing the image of that point, the vanishing of d phi
    along C would put the two partial derivatives of each coordinate function f_i in
    the ideal (u), which forces f_i = c_i(v) + u^2 k_i with c_i' = 0, hence c_i in
    k[v^p]; then k(f_1,...,f_N) lies in k(u,v^p), over which k(u,v) has degree p,
    contradicting q = 1. Checked in this pass: the two integrations in u, the
    inference from c_i' = 0 to c_i in k[v^p], the degree [k(u,v) : k(u,v^p)] = p, and
    the closedness of the image of Z in the dual from properness of X. Not checked:
    any printing of the book, only the text version retained in tmp/sources; the
    characteristic-0 case is now a citation of Corollary III.10.9 and is no longer
    re-proved on the card.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The coordinate argument recorded in the event above is withdrawn, and the rank-zero step is
    proved instead by a global argument; the body of the card is also checked for page locators. The
    withdrawal: that event infers from f_i in k[v^p] + u^2k[u,v] that f_i lies in k(u,v^p),
    and the inclusion is false, because v is not in k(u,v^p); the shape alone yields no contradiction,
    since u^2, u^2v, u^3 and v^p all have differentials vanishing along u = 0 and generate k(u,v). What
    replaces it: if d(phi)_x = 0 at a point x, then a plane through x exists whose section X_0 is a
    smooth plane cubic, because the tangent planes through x are the images of the curve Q_x cap X
    under the Gauss map, Q_x being the polar quadric of x; the 1-jet image of the restricted system W_0
    in the two-dimensional space L(x) tensor O/m_x^2 is one-dimensional, so ker(ev_x) lies in
    H^0(L(-2x)), which has dimension D.H - 2 on the elliptic curve; hence dim W_0 <= D.H - 1, so
    h^0(D-H) >= p_a + 1, while Riemann-Roch gives chi(D-H) = p_a and h^2(D-H) = 0, so h^1(D-H) >= 1,
    which Serre duality turns into h^1(O_X(-D)) >= 1, against the vanishing that a reduced connected
    member of the linear system gives. So no point of X has rank 0, and a curve contracted by the
    morphism, such as E_1 when D = H + E_1, is a curve of rank 1, already bounded by the r = 1
    paragraph. The body carries no printed or PDF page locator; the page locators inside the earlier
    dated events are left as written under QUAL-11 and remain the record of what was read. Checked:
    Euler's relation for the polar quadric, D.H >= 3 from the Hodge index theorem and the integrality
    of N, h^0(L(-2x)) = D.H - 2 on the elliptic section, the two Riemann-Roch computations, the duality
    h^1(D-H) = h^1(-D), the vanishing of h^1(O_X(-D)), and the failure of the inclusion, by the four
    generating functions named. Not checked: no printing of the book was read, only the text version
    retained in tmp/sources; no certificate or computation is claimed for this step.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Two corrections to the written step; the rank-zero argument itself is unchanged.
    (i) The case split by characteristic is removed. It cited Bertini's Corollary
    III.10.9 in characteristic 0 and then proved that no point has rank 0 in
    characteristic p, but that proof uses only Euler's relation for the polar
    quadric, the Hodge index theorem, two Riemann-Roch computations, Serre duality
    and the vanishing of h^1(O_X(-D)) for a reduced connected member of the system,
    and none of these has a hypothesis on the characteristic; the step now runs in
    every characteristic and the citation is dropped. (ii) The example of a curve
    contracted by the morphism was E_1 with D = H + E_1, and that class is not in
    alternative (c): (H + E_1).E_1 = -1, so E_1 is a fixed component of the system
    and not a contracted curve. The example is now F_56 with D = H + F_56, which
    has square 4, meets every one of the 27 lines nonnegatively and meets F_56 in 0.
    Checked in this pass: each of the six steps of the rank-zero argument, the value
    chi(D-H) = p_a, the inequality D.H >= 3 from the Hodge index theorem and the
    integrality of N, and both intersection numbers (H + E_1).E_1 = -1 and
    (H + F_56).F_56 = 0. Not checked: any printing of the book, only the text
    version retained in tmp/sources.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    One arithmetic claim of the event above is corrected, and that event is left as written. For a
    line E on the cubic surface H.E = 1, a line having degree 1, and E^2 = -1 by adjunction with
    K = -H and genus 0; hence (H + E_1).E_1 = 0, not -1. The class D = H + E_1 therefore has
    D.E_1 = 0, D.L at least 1 on each of the other 26 lines, and D^2 = 4, so it lies in alternative
    (c) and E_1 is contracted by the morphism of the system; E_1 is not a fixed component, and a
    base-point-free system has none, E_1 being disjoint from every member because D.E_1 = 0. So
    E_1 and F_56 are both valid instances of a contracted curve, and the body keeps F_56, which is
    equally valid. Nothing else changes: the rank-zero step does not depend on which class is
    named, a curve contracted by the morphism having rank 1 in either case. Checked: H.E = 1 and
    E^2 = -1, the value (H + E_1)^2 = 4, the intersections of H + E_1 with the other 26 lines, and
    the corresponding values (H + F_56)^2 = 4 and (H + F_56).F_56 = 0. Not checked: no source was
    read for this event, and neither intersection table was recomputed from a printed copy.
- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Citation repairs on the third condition's argument, and one sentence of
    justification added, with no change of mathematics. (i) The Hodge index
    inequality was cited as Theorem V.1.9 itself, which the book states only
    for a divisor meeting the ample class in 0. The three places that use
    (D.H)^2 >= 3D^2 now name the divisor (H^2)D - (D.H)H, which does meet H in
    0, so the inequality is the theorem at its own number. (ii) The image of
    the morphism defined by the complete system was called a surface without
    argument; the sentence now adds that D^2 > 0 excludes an image of
    dimension at most 1, whose pullback of an ample class has square 0. Read
    for (i): Theorem V.1.9 and its proof in
    tmp/sources/hartshorne-1977-algebraic-geometry.md. Not read: Remark
    1.9.1, which is about the signature and states no inequality, and no
    printing of the book. The card's own parts and the characteristic-free
    claim are unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    The open item recorded for this card is closed, and its being open is
    recorded here first. As the card stood at 081eb8789f, line 774 read
    "writing D ~ a l - sum_ib_ie_i as in Proposition 4.8", and that notation is
    used from step negative-square-is-a-line on: the proof presupposed that X,
    a smooth cubic surface over an algebraically closed field of
    characteristic p, is the blowup of P^2 at six points, which is what
    Notation V.4.7.3 and Proposition V.4.8 assume and what their numbers do
    not supply for an arbitrary smooth cubic surface. The characteristic claim
    of the card therefore rested on an unproved identification, and that is now
    a step of the proof, geometric-marking, placed first. It cites Dolgachev
    and Duncan, Automorphisms of cubic surfaces in positive characteristic
    (2017), §2, over an algebraically closed field of arbitrary characteristic:
    27 lines, each an exceptional curve of the first kind; a smooth cubic
    surface obtained by blowing up six points of P^2 in general position;
    conversely six mutually skew lines blown down to six points, a geometric
    marking; the remaining 21 lines as the strict transforms of the 15 lines
    and 6 conics. Each blowdown is the contraction of a curve isomorphic to P^1
    of self-intersection -1, which exists by Castelnuovo's criterion, Theorem
    V.5.7. Read for this: Dolgachev--Duncan §2 in
    tmp/sources/dolgachev-duncan-2017-automorphisms-cubic-surfaces-char-p.md,
    and Theorem V.5.7 with its preamble in
    tmp/sources/hartshorne-1977-algebraic-geometry.md. No other step changed
    and no claim was weakened: the proof now applies to a smooth cubic surface
    in every characteristic, which before this step it did only under an
    assumption. Not read: any printing of either work, only the text versions
    in tmp/sources; and Dolgachev--Duncan's own proof of the 27-line count,
    which §2 states without proof.
- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    The attribution in the preceding event of this date is withdrawn: it
    described step geometric-marking as citing Dolgachev and Duncan,
    Automorphisms of cubic surfaces in positive characteristic (2017), §2. That
    section carries no numbered statement — its numbered results are Theorem
    2.1, Theorem 2.4 and Remark 2.5, none of them about lines or blowups — and
    its prose sentence that a smooth cubic surface "can be obtained by blowing
    up six points in general position" states neither a field range as a
    hypothesis nor the two general-position conditions as conclusions, so it
    could not discharge the step. The step now cites numbered statements of R.
    Vakil, The Rising Sea (21 October 2025): Theorem 27.0.2, "Every smooth
    cubic surface over k is isomorphic to P^2 blown up at six points", whose
    field convention §27.0.3 fixes as "X will be a smooth cubic surface over an
    algebraically closed field k", with no hypothesis on the characteristic in
    the statement; Exercise 27.1.B, that a curve on a smooth cubic surface is a
    line if and only if it is an exceptional curve of the first kind; and
    Exercise 27.3.E, whose conclusion is that blowing up six points gives a
    smooth cubic surface only when the points are distinct, no three on a line
    and not all on a conic. The card derives the second and the third itself as
    well, from the adjunction formula (II, 8.20), H = -K_X, Proposition V.3.3
    and the ampleness of H. What Vakil's own proof of Theorem 27.0.2 uses is
    disclosed here: §27.3 reduces it to Exercise 27.2.J, two disjoint lines with
    exactly five lines meeting both, and §27.2 proves 27.2.J under the
    assumption char k = 0, "which carries through without change if char k != 3",
    the one required check being Exercise 27.1.C, the 27 lines of the Fermat
    cubic, which is smooth in every characteristic but 3; the case p = 3 is
    Vakil's starred Exercise 27.2.K, stated and not worked out. So in
    characteristic 3 the card rests on Theorem 27.0.2 as stated rather than on
    its printed proof, and Dolgachev and Duncan's prose remains the only
    assertion for that characteristic among the retained sources. Read in this
    pass: Vakil's Theorem 27.0.1 and Theorem 27.0.2, §27.0.3, §27.1 Exercises
    27.1.A to 27.1.C, §27.2 to Exercise 27.2.K, and §27.3 through the proof of
    Theorem 27.0.2, in tmp/sources/vakil-rising-sea-2025-10-21.md;
    Dolgachev--Duncan §2 and its numbering; and the adjunction formula (II,
    8.20) with Proposition V.3.3 in
    tmp/sources/hartshorne-1977-algebraic-geometry.md. No other step changed.
- event: source-checked
  by: claude
  date: 2026-11-22
  note: >-
    Corroboration of the numbered statement, and the unheld references it does
    not use. Hartshorne asserts the same identification, in prose and without a
    number, in Remark V.4.7.1: that every Del Pezzo surface is either one given
    by (4.7) for a suitable choice of points or the 2-uple embedding of a
    quadric, that "in particular, every nonsingular cubic surface in P^3 can be
    obtained by blowing up 6 points in the plane", that for a cubic surface the
    condition omega_X = O_X(-1) is automatic by Chapter II Exercise 8.4, and
    that proofs are in Manin, Cubic Forms, §24, or Nagata, I, Theorem 8. Read
    for this: Remark V.4.7.1 in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, and Chapter II Exercise
    8.4, which is not read here. Neither Manin nor Nagata is held in
    tmp/sources, so neither was read and neither is cited by number on the
    card; the numbered statement the step uses remains Vakil's Theorem 27.0.2.
    This event adds no claim to the mathematics.
- event: source-checked
  by: claude
  date: 2026-11-22
  note: >-
    What the characteristic-3 caveat leaves open, and what closes part of it.
    The 27 lines themselves are available in every characteristic by a proof
    that uses no separability, no discriminant and no vanishing theorem: the
    Fano scheme of lines of X is the zero scheme in the Grassmannian G(1,3) of
    the section of Sym^3 S^* given by the cubic form; by adjunction N_{L/X} is
    a line bundle of degree 2 - 3 = -1, hence O(-1), so h^0 = h^1 = 0 and every
    point of the zero scheme is isolated and reduced; and c_4(Sym^3 S^*) = 27.
    That last number, checked by hand in this pass: the Chern roots of
    Sym^3 S^* are -3x, -2x-y, -x-2y, -3y, so
    c_4 = 9xy(2x^2+5xy+2y^2) = 9(2c_1^2c_2+c_2^2), and on G(2,4) the Pieri
    products give c_1^2 c_2 and c_2^2 both equal to the class of a point. The
    zero scheme therefore has length 27 and consists of 27 reduced points,
    which is the 27-lines theorem in every characteristic. This is not the
    route the step uses and it is not written out on the card; it is recorded
    because it is the characteristic-free substitute for the one part of
    Theorem 27.0.2 that Vakil's printed proof leaves to characteristic != 3. It
    does not by itself give the six mutually skew lines nor the identification
    of the surface as a blowup, which remain where the step says they are.
- event: source-checked
  by: claude
  date: 2026-11-22
  note: >-
    Published-solution pass for issue #160, on the transcription rule: the
    nonsingularity of the member of alternative (c) is proved by no retained
    solution set, in any characteristic, and the "Published solution" remark
    now says so and names the sets searched. Read for that, each at its own
    numbering: Egbert's entry 5.4.8, which quotes the statement and gives no
    solution; Yang Pi-Yeh's Solution 5.4.8, whose (*) supplies an irreducible
    nonsingular member only for a class meeting every line strictly
    positively, its (i) implies (iii) direction contracts to X_r without
    excluding D^2 = 0 from the third alternative, and the hypothesis
    D^2 > 0 of the exercise is never used; the National Taiwan University
    Algebraic Geometry II (2020 Spring) Chapter V §4 homework, whose
    exercises are 1, 2, 3, 4, 5, 7, 10, 11, 12, 14 and 16 and which therefore
    does not treat this one; and, for absence, the sets that carry no
    Chapter V §4 exercise, Borcherds (through IV.1), Cais (through Chapter 4),
    Cutrone--Marshburn (Chapters 1 and 2), Ionita--Kumar (Chapter I), Kim
    (§2.4), Lomont, Okamoto (§II.9), Park (Chapter 4 and §V.5), Saglam--Chris (Chapter III),
    Sam (through IV.6), Stein (III.7), Troiani (Chapter II) and Reiser
    (IV.2.5). Read in this pass: the printed text of Exercise V.4.8 in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, which asks for the two
    equivalences and the three alternatives; Yang's Solution 5.4.8 in
    tmp/sources/lfwin-hartshorne-solutions.md; Egbert's entry 5.4.8; and the
    exercise list of the NTU file. Not read in this pass: Hartshorne's
    Theorem 4.9, Theorem 4.11, Theorem V.1.6, Theorem V.1.9, Corollary
    III.7.7 and Theorem II.8.6A, whose statements the steps cite and whose
    numbered statements earlier events record; Harbourne's and Vakil's
    statements only as the card records them; and any printing of the book,
    only the text version in tmp/sources. No proof step and no statement
    changed on the card in this pass.
---

::: {.problem}
Show that a divisor class $D$ on the cubic surface contains an irreducible curve $\iff$ it contains an irreducible nonsingular curve $\iff$ it is either

(a) one of the 27 lines, or

(b) a conic (meaning a curve of degree 2) with $D^2=0$, or

(c) $D . L \geqslant 0$ for every line $L$, and $D^2>0$.

Hint: Generalize (4.11) to the surfaces obtained by blowing up $2,3,4$, or 5 points of $\PP^2$, and combine with our earlier results about curves on $\PP^1 \times \PP^1$ and the rational ruled surface $X_1$, (2.18).
:::

::: {.solution}

Write $X$ for the cubic surface, so that $-K_X=H$ is the hyperplane class, and let $k$ be
algebraically closed.

::: pf

::: {.pf-step #geometric-marking}
$X$ admits a geometric marking: six mutually skew lines whose blowdown is a morphism $\pi\colon X\to\PP^2$ making $X$ the blowup of $\PP^2$ at six distinct points, no three collinear and not all six on a conic. With it, every divisor class is written $D\sim a\ell-\sum_ib_ie_i$, and the intersection numbers used below are those of Proposition 4.8.

::: pf-proof
R. Vakil, *The Rising Sea* (21 October 2025), Theorem 27.0.2, states over an algebraically closed field $k$, with no hypothesis on the characteristic, that every smooth cubic surface over $k$ is isomorphic to $\PP^2$ blown up at six points; §27.0.3 of the same book fixes that convention for the chapter, and the surface is the smooth cubic surface of that chapter. Let $\pi\colon X\to\PP^2$ be the resulting morphism and $E_1,\ldots,E_6$ its exceptional curves, and let $H$ be the class of a hyperplane section. By the adjunction formula (II, 8.20), $K_X=(K_{\PP^3}\tensor\OO_{\PP^3}(X))\restriction_X=(-4H+3H)\restriction_X=-H$, so $H=-K_X$. Each $E_i$ is isomorphic to $\PP^1$ with $E_i^2=-1$ and $E_i\cdot K_X=-1$, so $E_i\cdot H=-E_i\cdot K_X=1$, and $E_i$ is a line of the cubic surface by Vakil's Exercise 27.1.B, a curve on a smooth cubic surface being a line exactly when it is an exceptional curve of the first kind. Distinct exceptional curves of a blowup are disjoint, so the six are mutually skew.

The six points $\pi(E_1),\ldots,\pi(E_6)$ are in general position. By Proposition V.3.3 applied to the six blowups, $K_X=\pi^*K_{\PP^2}+\sum_iE_i=-3\ell+\sum_ie_i$, so $H=3\ell-\sum_ie_i$. If three of the points lay on a line $M$, the strict transform of $M$ would be an effective curve of class $\ell-e_1-e_2-e_3$ and of $H$-degree $3-3=0$; if all six lay on a conic $C$, the strict transform of $C$ would be an effective curve of class $2\ell-\sum_ie_i$ and of $H$-degree $6-6=0$. An effective curve on the surface $X$ has positive degree in the class $H$ of a hyperplane section, so neither curve exists: no three of the points are collinear, and not all six lie on a conic. This is the conclusion of Vakil's Exercise 27.3.E, drawn there from the existence of a curve of nonnegative degree.

After the marking $\Pic X$ is free on $\ell,e_1,\ldots,e_6$ with the intersection numbers of Proposition V.4.8(a) and (b): that proposition and Notation V.4.7.3 phrase these for the surface obtained by blowing up the six points, and the marking is an isomorphism from $X$ to that surface, so the classes and their pairings carry over.
:::

:::

::: {.pf-step #negative-square-is-a-line}
If $D$ contains an irreducible curve $C$ with $C^2<0$, then $C$ is one of the $27$ lines, so $D$ is
alternative (a).

::: pf-proof
Adjunction on the surface, with $K_X=-H$, gives
$$
2p_a(C)-2=C^2+C\cdot K_X=C^2-H\cdot C,
\qquad
p_a(C)=h^1(C,\OO_C)\ge0,
$$
and $H\cdot C\ge1$ because $H$ is ample and $C$ is a curve. If $C^2<0$ then $C^2-H\cdot C\le-2$, so
$p_a(C)=0$ and $C^2=H\cdot C-2\ge-1$, since $H\cdot C\ge1$; hence $C^2=-1$ and $H\cdot C=1$. A curve of
degree $1$ on $X$ is a line, and by Theorem 4.9 of the book, the irreducible
curves on $X$ of negative self-intersection are the $27$ lines $E_i,F_{ij},G_j$. Only the ampleness of
$H$ and the nonnegativity of $p_a$ are used, in every characteristic; the first paragraph of the
proof of Theorem 4.9 draws the same conclusion in the same way.
:::

:::

::: {.pf-step #zero-square-is-a-conic}
If $D$ contains an irreducible curve $C$ with $C^2=0$, then
$$
H\cdot C=2,
\qquad
p_a(C)=0,
$$
so $D$ is alternative (b).

::: pf-proof
Adjunction and $K_X=-H$ give
$$
0-H\cdot C=C^2+C\cdot K_X=2p_a(C)-2,
$$
so $2p_a(C)=2-H\cdot C$. Since $H$ is ample, $d=H\cdot C\ge1$, and since $p_a(C)=h^1(C,\OO_C)\ge0$
this gives $d\le2$; $d=1$ would give $2p_a(C)=1$. Hence $d=2$ and $p_a(C)=0$, so $C$ is a conic of
self-intersection $0$. The computation is the one in the proof of Dolgachev's Lemma 8.1.3, at $C^2=0$.
:::

:::

::: {.pf-step #positive-square-satisfies-the-third-condition}
If $D$ contains an irreducible curve $C$ with $C^2>0$, then
$$
C\cdot L\ge0\quad\text{for every line }L,
\qquad
C^2>0,
$$
so $D$ is alternative (c).

::: pf-proof
Two distinct irreducible curves on a surface have nonnegative intersection number, $C\cdot L$ being a
sum of local intersection multiplicities, and if $C=L$ then $C^2=-1<0$. Since $C$ is not a line,
$C\ne L$ for each of the $27$ lines $L$, so $C\cdot L\ge0$.
:::

:::

::: {.pf-step #lines-contain-nonsingular-curves}
Every class in alternative (a) contains an irreducible nonsingular curve.

::: pf-proof
By Theorem 4.9 of the book, the $27$ classes $E_i,F_{ij},G_j$ are the classes
of the $27$ lines of $X$, each isomorphic to $\PP^1$.
:::

:::

::: {.pf-step #third-condition-contains-nonsingular-curve}
Let $D$ satisfy
$$
D\cdot L\ge0\quad\text{for every one of the }27\text{ lines }L,
\qquad
D^2>0 .
$$
Then the complete linear system $\linearsystem{D}$ has an irreducible nonsingular member.

::: pf-proof
First, $D$ is numerically effective, and this needs no hypothesis on the characteristic: let
$H=-K_X$ be the hyperplane class and put $D_n=nD+H$ for an integer $n\ge1$. Each of the $27$ lines
$L$ has $D_n\cdot L=n(D\cdot L)+1>0$ because $H\cdot L=1$, and
$D_n^2=n^2D^2+2nD\cdot H+H^2=n^2D^2+2nD\cdot H+3>0$. By Theorem 4.11 of the book, whose proof is Lemma 4.12 and the enumeration of the $27$ lines and which uses no
hypothesis on the field, $D_n$ is very ample. Hence for every irreducible curve $E$ on $X$,
$0<D_n\cdot E=n(D\cdot E)+H\cdot E$ for every $n\ge1$, which forces $D\cdot E\ge0$: if $D\cdot E<0$,
the left side is negative for $n>H\cdot E$. So $D$ meets every effective class nonnegatively.

Second, $D$ is effective: by B. Harbourne, *Anticanonical Rational Surfaces* (24 January 1996,
arXiv:alg-geom/9509001v2), Corollary II.3, a numerically effective divisor meeting the
anticanonical class nonnegatively lies in $\mathrm{Eff}$, and here $-K_X\cdot D=D\cdot H>0$, while
$D\cdot H\ge2$: Theorem V.1.9, the Hodge index theorem, applied to the divisor
$(H^2)D-(D\cdot H)H$, which meets the ample class $H$ in $0$, gives
$3D^2\le(D\cdot H)^2$, and $D^2>0$ makes $(D\cdot H)^2\ge3$, so $D\cdot H$ is a positive integer of
absolute value at least $2$.

Third, the system is base point free and $h^1$ vanishes: since $-K_X\cdot D=D\cdot H\ge2$,
Harbourne's Theorem III.1(a) gives $h^1(X,\OO_X(D))=0$ and that the sections of $D$
are base point (and hence fixed component) free.

Fourth, a general member is reduced and irreducible: since $D^2>0$ the system is not composed with a
pencil, and Harbourne's Lemma II.6(b) then gives $D^2>0$ and that the general section
of $D$ is reduced and irreducible.

Finally, it is nonsingular, in every characteristic. Put
$H=\OO_X(1)=-K_X$, so $H^2=3$. Since $X$ is a cubic surface in $\PP^3$, the sequence
$0\to\OO_{\PP^3}(-3)\to\OO_{\PP^3}\to\OO_X\to0$ gives $q(X)=h^1(\OO_X)=0$, and
$p_g(X)=h^0(K_X)=h^0(\OO_X(-1))=0$. Also $D\cdot H\ge2$: Theorem V.1.9, applied to
$(H^2)D-(D\cdot H)H$, which meets $H$ in $0$, gives $3D^2\le(D\cdot H)^2$ with $H^2=3$, and $D^2>0$
makes $(D\cdot H)^2\ge3$, so
the integer $D\cdot H$ has absolute value at least $2$ and is positive because $D$ is nef and $H$
is ample. And $h^2(X,\OO_X(D))=0$: Serre duality, Corollary III.7.7, gives
$h^2(D)=h^0(K_X-D)=h^0(-H-D)$, and $(-H-D)\cdot H=-3-D\cdot H<0$ with $H$ ample, so $-H-D$ is not
effective.

It remains to show that a general member is nonsingular, and this is done without a Bertini theorem
for a base-point-free system and without a hypothesis on the characteristic. Let
$N=\dim\linearsystem{D}$, let $\varphi\colon X\to\PP^N$ be the morphism defined by
$\linearsystem{D}$, whose general member is the preimage of a general hyperplane, and note that
$N\ge2$, because a base-point-free pencil has $D^2=0$. Riemann--Roch, Theorem V.1.6, applied with
$h^1(D)=h^2(D)=0$ and $\chi(\OO_X)=1-p_g(X)+q(X)=1$, gives
$$
h^0(\OO_X(D))=\chi(\OO_X(D))=\frac{1}{2}D\cdot(D-K_X)+1=\frac{1}{2}(D^2+D\cdot H)+1,
\qquad\text{so}\qquad
N=\frac{1}{2}(D^2+D\cdot H).
$$
Let $Y=\varphi(X)$ be the image, a surface spanning $\PP^N$ because the system is complete and
$D^2>0$, an image of dimension at most $1$ giving $D^2=0$; and let
$q=[k(X):k(Y)]$ be the degree of $\varphi$; then $D^2=q\deg Y$ by the projection formula. A surface
in $\PP^N$ that spans $\PP^N$ has degree at least $N-1$: a surface spanning $\PP^2$ is $\PP^2$
itself, of degree $1$; a surface spanning $\PP^3$ is not a plane,
and for $N\ge4$ the projection of $Y$ from a general point of $Y$ is a birational map onto a surface
of degree $\deg Y-1$ in $\PP^{N-1}$ which still spans, a general $\PP^{N-2}$ through that point
meeting $Y$ in $\deg Y$ points one of which is that point with multiplicity one, while a hyperplane
of $\PP^{N-1}$ containing the image would lift to a hyperplane of $\PP^N$ containing $Y$. Hence
$D^2=q\deg Y\ge q(N-1)$, and
$$
D\cdot H=2N-D^2\le 2N-q(N-1)=N(2-q)+q .
$$
If $q\ge3$ the right-hand side is at most $1$, contradicting $D\cdot H\ge2$. If $q=2$ then
$D\cdot H=2$, and no class of degree $2$ meeting the six exceptional curves nonnegatively has
positive square: writing $D\sim a\ell-\sum_ib_ie_i$ as in Proposition 4.8, the inequalities
$D\cdot E_i=b_i\ge0$ and $3a-\sum_ib_i=D\cdot H=2$ give $a\ge1$, while $D^2=a^2-\sum_ib_i^2>0$ needs
$a^2>(3a-2)^2/6$ by Cauchy--Schwarz, that is $3a^2-12a+4<0$ and $a\in\{1,2,3\}$, and six nonnegative
integers $b_i$ with $\sum_ib_i$ equal to $1$, $4$ or $7$ have $\sum_ib_i^2$ at least $1$, $4$ or $9$,
which is $a^2$; so $D^2\le0$ in each case, a contradiction. Therefore $q=1$ and $\varphi$ is
birational; its differential has rank $2$ at the generic point of $X$, since $k(X)=k(Y)$ makes
$\dim_{k(X)}\Omega_{k(X)/k(Y)}=0$ by Theorem II.8.6A, and the locus where the rank of $d\varphi$ is
at most $1$ is a proper closed subset of the surface.

For $x\in X$ let $r(x)$ be the rank of $d\varphi_x\colon T_xX\to T_{\varphi(x)}\PP^N$, and let
$$
Z=\{(x,H)\in X\times\PP^{N\vee}:\varphi(x)\in H,\ d(\ell_H\circ\varphi)_x=0\},
$$
where $\ell_H$ is a linear form defining $H$. The local equation of the member $\varphi^{-1}(H)$ at a
point $x$ of it is $\ell_H\circ\varphi$; if its differential is nonzero at $x$ it is part of a
regular system of parameters of the local ring of the nonsingular surface $X$, so the quotient local
ring is regular of dimension $1$ and the member is nonsingular at $x$ by Theorem I.5.1. It is
therefore enough to show that the image of $Z$ in $\PP^{N\vee}$ is a proper closed subset, and no
hypothesis on the characteristic is used below.

Where $r(x)=2$ the image $d\varphi_x(T_xX)$ is a $2$-plane in $T_{\varphi(x)}\PP^N$ when $N\ge3$, and
the hyperplanes $H$ with $(x,H)\in Z$ are those containing it, a linear subspace of $\PP^{N\vee}$ of
dimension $N-3$, so this part of $Z$ has dimension at most $2+(N-3)=N-1$; for $N=2$ no hyperplane
contains that image and the part is empty. Where $r(x)=1$ the hyperplanes $H$ with $(x,H)\in Z$
contain the line $d\varphi_x(T_xX)$, a linear subspace of dimension $N-2$, and over the at most
one-dimensional locus $r=1$ this part of $Z$ has dimension at most $1+(N-2)=N-1$. Where $r(x)=0$ the two conditions on $H$ reduce to $\varphi(x)\in H$, since
$d(\ell_H\circ\varphi)_x=\ell_H\circ d\varphi_x$ vanishes; and there is no such point. Suppose that
$d\varphi_x=0$. The planes through $x$ that are tangent to $X$ are the planes $T_pX$ with
$x\in T_pX$, and $x\in T_pX$ is equivalent to $p\in Q_x\cap X$, where
$Q_x=\{y:\sum_ix_i\partial_iF(y)=0\}$ is the polar quadric of $x$: the relation is Euler's,
$\sum_ip_i\partial_iF(p)=3F(p)=0$ for $p\in X$. That intersection is a curve, so its image under
$p\mapsto T_pX$ is at most one-dimensional in the plane of planes through $x$, and a general plane
$\Pi$ through $x$ is not tangent to $X$; for such a $\Pi$ the section $X_0=X\cap\Pi$ is a smooth
plane cubic.

Let $L=\OO_{X_0}(D)$, of degree $\delta=D\cdot H$, and let $W_0\subseteq H^0(L)$ be the image of
$H^0(\OO_X(D))$; $W_0$ defines the morphism $\psi=\restrictionof{\varphi}{X_0}$ and is base point free. Since
$d\psi_x=0$, every quotient $s/t$ of members of $W_0$ with $t(x)\ne0$ has zero derivative at $x$, so
the image of $W_0$ in the two-dimensional space $L(x)\otimes\OO_{X_0}/\mathfrak m_x^2$ is
one-dimensional; hence every $s\in W_0$ with $s(x)=0$ has $ds_x=0$, that is,
$\ker(\operatorname{ev}_x)\subseteq H^0(L(-2x))$. Now $\delta\ge3$: Theorem V.1.9, applied to
$(H^2)D-(D\cdot H)H$, gives $(D\cdot H)^2\ge3D^2$, so $D\cdot H\ge2$, and $D\cdot H=2$ would give $D^2=1$
and $2N=D^2+D\cdot H=3$, which is impossible. The curve $X_0$ is elliptic, so $h^0(L(-2x))=\delta-2$; with
$\dim\ker(\operatorname{ev}_x)=\dim W_0-1$ this gives $\dim W_0\le\delta-1$.

The sequence $0\to\OO_X(D-H)\to\OO_X(D)\to L\to0$ identifies $H^0(D-H)$ with the kernel of
$H^0(\OO_X(D))\to H^0(L)$, so $h^0(D-H)=(N+1)-\dim W_0\ge N+2-\delta$, and $\delta=D\cdot H=2N-D^2$
makes this $D^2-N+2=p_a+1$, where $p_a=D^2-N+1=1+\frac12(D^2-D\cdot H)$ is the arithmetic genus of
a member of $\linearsystem{D}$ by adjunction. On the other hand Riemann--Roch gives
$\chi(\OO_X(D-H))=\frac12\bigl((D-H)^2-(D-H)\cdot K\bigr)+1=\frac12(D^2-D\cdot H)+1=p_a$, and
$h^2(D-H)=h^0(K-D+H)=h^0(-D)=0$ because $(-D)\cdot H<0$ with $H$ ample, so
$h^0(D-H)=p_a+h^1(D-H)$ and $h^1(D-H)\ge1$. Serre duality, Corollary III.7.7, gives
$h^1(D-H)=h^1(-D)$, hence $h^1(\OO_X(-D))\ge1$. But that group vanishes: for a reduced connected
member $A$ of $\linearsystem{D}$ the sequence $0\to\OO_X(-D)\to\OO_X\to\OO_A\to0$ gives
$0\to H^0(\OO_X)\to H^0(\OO_A)\to H^1(\OO_X(-D))\to H^1(\OO_X)=0$, and $h^0(\OO_X)=h^0(\OO_A)=1$
because $X$ is rational and $A$ is a reduced connected curve. So $r(x)\ge1$ at every point of $X$,
and a curve contracted by $\varphi$, such as $F_{56}$ when $D=H+F_{56}$, is a curve of rank $1$ and
is covered by the preceding paragraph.

Thus the image of $Z$ has dimension at most $N-1$, and it is closed because
$X$ is proper. A general hyperplane $H$ therefore lies outside that image, and for such $H$ no point
of the member $\varphi^{-1}(H)$ lies in $Z$, so the member, reduced and irreducible by the fourth
paragraph, is nonsingular. This is the incidence
count of the proof of Vakil's Bertini theorem, *The Rising Sea* (21 October 2025), Theorem 13.4.2,
carried out for the morphism $\varphi$ rather than for a smooth closed subvariety of $\PP^N$: where
$\varphi$ is an isomorphism the fibre of $Z$ is the $\PP^{N-1-\dim X}$ of that proof, and the case
$r=1$ above is the additional $\PP^{N-2}$ fibre created by the drop in rank.
:::

:::

::: {.pf-step #conic-classes-contain-a-conic}
Every class in alternative (b) contains an irreducible nonsingular conic.

::: pf-proof
Let $D$ satisfy $D\cdot H=2$ and $D^2=0$. The classes with these two invariants are the classes
$H-L$ for the $27$ lines $L$: writing $D\sim a\ell-\sum_ib_ie_i$, the conditions
$$
3a-\sum_ib_i=2,
\qquad
a^2-\sum_ib_i^2=0
$$
give $\sum_ib_i=3a-2$ and $\sum_ib_i^2=a^2$, hence
$$
\sum_ib_i(b_i-1)=a^2-3a+2 .
$$
Cauchy--Schwarz applied to the sequences $1$ and $b_i$ gives $(3a-2)^2\le6a^2$, that is
$3a^2-12a+4\le0$, so $a\in\{1,2,3\}$. For $a=1$ and $a=2$ the sum of $b_i(b_i-1)$ vanishes, and
since each $b_i(b_i-1)\ge0$ for an integer $b_i$, every entry is $0$ or $1$: with $\sum_ib_i=1$ that
is one entry $1$, and with $\sum_ib_i=4$ it is four entries $1$. For $a=3$ the sum is $2$ and
$\sum_ib_i=7$; since $b_i(b_i-1)=2$ only for $b_i=2$ and for $b_i=-1$, and an entry $-1$ would leave
$\sum_ib_i\le4$, exactly one entry is $2$ and the other five are $1$. These are the classes
$H-G_i$, $H-F_{ij}$ and $H-E_i$, by the classes of those lines in Theorem 4.9.
This enumeration of the degree $2$ classes of square $0$ from the two equations is the card's own, in
the manner of the proof of Theorem 4.9, which finds the $b_i$ of a line by trial.

Each of these classes contains an irreducible nonsingular conic. For a line $L$ on $X$ and a plane
$\Pi$ through $L$, the intersection $\Pi\cap X$ is a plane cubic curve containing $L$, so as a divisor
it is $L+C_\Pi$ with $C_\Pi$ a conic of class $H-L$. The conic $C_\Pi$ does not contain $L$: a class
containing $2L$ would be $H-2L$, of degree $3-2=1$ and of square $3-4-4=-5$, whereas an effective class
of degree $1$ is a line and has square $-1$. A singular plane conic is a union of two lines, equal or
not, and both lie on $X$ because $C_\Pi\subseteq X$; a plane through $L$ and another line of $X$ is
determined by that pair, so at most $26$ planes through $L$ give a singular $C_\Pi$, and every other
one gives an irreducible nonsingular conic of the class $H-L$. The planes through a line form a
$\PP^1$, so such a plane exists. Only two facts are used, that a plane meets the cubic surface in a
plane cubic and that a singular conic is a pair of lines, so the argument holds in every
characteristic.
:::

:::

::: {.pf-step #classification-and-equivalence}
A class contains an irreducible curve if and only if it contains an irreducible nonsingular curve,
and this happens exactly in alternatives (a), (b) and (c).

::: pf-proof
If $D$ contains an irreducible curve $C$, then $C^2<0$, $C^2=0$ or $C^2>0$, and steps
[](#negative-square-is-a-line){.pf-ref}, [](#zero-square-is-a-conic){.pf-ref} and
[](#positive-square-satisfies-the-third-condition){.pf-ref} place $D$ in alternatives (a), (b) and
(c) respectively. Conversely steps [](#lines-contain-nonsingular-curves){.pf-ref},
[](#conic-classes-contain-a-conic){.pf-ref} and
[](#third-condition-contains-nonsingular-curve){.pf-ref} give an irreducible nonsingular member of
every class in alternatives (a), (b) and (c). An irreducible nonsingular curve is an irreducible
curve, so the two existence conditions agree, and both are equivalent to the classification.
:::

:::

::: {.pf-step #conclusion}
A divisor class on the cubic surface contains an irreducible curve if and only if it is one of the
$27$ lines, or a conic of degree $2$ with $D^2=0$, or satisfies $D\cdot L\ge0$ for every line $L$
with $D^2>0$; and then it contains an irreducible nonsingular curve.

::: pf-proof
Step [](#classification-and-equivalence){.pf-ref} gives both directions and the equivalence of the two
existence conditions.
:::

:::

::: pf-qed
Steps [](#negative-square-is-a-line){.pf-ref}, [](#zero-square-is-a-conic){.pf-ref} and
[](#positive-square-satisfies-the-third-condition){.pf-ref} are the necessity of the three
alternatives; steps [](#lines-contain-nonsingular-curves){.pf-ref},
[](#conic-classes-contain-a-conic){.pf-ref} and
[](#third-condition-contains-nonsingular-curve){.pf-ref} are their sufficiency, with irreducible
nonsingular members; step [](#classification-and-equivalence){.pf-ref} is the equivalence of the two
existence conditions.
:::

:::
:::

::: {.remark title="Published solution"}
Brian Harbourne, *Anticanonical Rational Surfaces* (24 January 1996, arXiv:alg-geom/9509001v2):
Corollary II.3, that a numerically effective divisor meeting $-K$ nonnegatively is
effective; Lemma II.6, that a fixed-component-free class whose system is not composed
with a pencil has $D^2>0$ and reduced irreducible general section, and that a class whose system is
composed with a pencil is a multiple of a class with reduced irreducible general section; and Theorem
III.1(a), that $-K_X\cdot D\ge2$ makes the system base point free with $h^1=0$. The
paper works over an algebraically closed field of arbitrary characteristic, so its Lemma II.6 gives
reduced irreducible members in every characteristic. The nonsingularity of the member of a class of
the third alternative is then the incidence count of Vakil's proof of Theorem 13.4.2, carried out
for the morphism defined by $\linearsystem{D}$: Riemann--Roch and the degree of a surface spanning
$\PP^N$ make that morphism birational, no point of $X$ has rank $0$ --- the argument is
characteristic-free --- and the bad hyperplanes form a closed subset of the dual of dimension at most
$N-1$.

I. V. Dolgachev, *Topics in Classical Algebraic Geometry* (September 27, 2010): Lemma 8.1.3 and its
proof, on irreducible curves of negative self-intersection on a weak Del Pezzo
surface, whose computation step positive-square-satisfies-the-third-condition repeats. The book
takes $\CC$ as its base field, so its Theorem 8.2.19, on the effective cone is not
used: the numerical effectivity of step third-condition-contains-nonsingular-curve is proved from
Hartshorne's Theorem 4.11, which has no hypothesis on the characteristic.

Theorem 4.9 of Hartshorne, for the $27$ lines and for the curves of negative
self-intersection; Hartshorne, Corollary III.7.7, Theorem V.1.6, Proposition V.1.5 and Theorem
V.1.9 for the cohomology of $D$, the adjunction numbers and the degree of the morphism, and
Theorem I.5.1 and Theorem II.8.6A for the nonsingularity of the general member.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 5.4.8, argues both
implications through the blowups $X_r$, $2\le r\le5$: it lists the lines of $X_r$, the $E_i$ and
$F_{ij}$ with $G$ added at $r=5$, takes the classes $D_0,\ldots,D_5$ of Lemma 4.12 and Corollaries
4.1 and 4.3, and reads off that $a>b_1+b_2$ for $r<5$ and $a>b_1+b_2+b_5$ for $r=5$ make a class very
ample on $X_r$, equivalently $D\cdot L>0$ for every line. For (i) implies (iii) it contracts to $X_r$
and concludes $D\cdot L\ge0$, without excluding $D^2=0$ from the third alternative, which is where the
conic sits. For (iii) implies (ii) it takes a member of the system of $D'=\pi_r(D)$; and there the
entry does not close: the step it cites as its (*) produces an irreducible nonsingular member of a
class meeting every line strictly positively, while (iii) gives only $D\cdot L\ge0$, and the
hypothesis $D^2>0$ that the exercise adds for that case is never used. The class $H+F_{56}$ of
[[P-AGH547GENUSBOUND|V.4.7]] is the case in point: it meets $F_{56}$ in $0$, meets every one of the
$27$ lines nonnegatively
and has square $4$, so (c) gives it an irreducible nonsingular member while the strict criterion the
entry invokes does not apply. The card's own proof, Harbourne's Lemma II.6 and Theorem III.1(a) with
Hartshorne's Theorem 4.11 in place of any cone description, does not depend on the entry.

The retained solution sets were searched for this exercise and none proves what the third
alternative needs in characteristic $p$. Two of them contain it: Egbert's entry 5.4.8, which quotes
the statement and gives no solution, and Yang Pi-Yeh's Solution 5.4.8, the entry whose gap the
preceding paragraph records. The National Taiwan University Chapter V §4 homework treats exercises
1, 2, 3, 4, 5, 7, 10, 11, 12, 14 and 16 and not this one, and Borcherds, Cais, Cutrone--Marshburn,
Ionita--Kumar, Kim, Lomont, Okamoto, Park, Saglam--Chris, Sam, Stein, Troiani and Reiser carry no Chapter V §4
exercise. The argument on this card is therefore the card's own. Its inputs, each cited by numbered
statement, are: Harbourne's Lemma II.6(b) for a reduced irreducible general section and Theorem
III.1(a) for base point freeness and the vanishing of $h^1$; Hartshorne's Theorem 4.9 for the $27$
lines, Theorem 4.11 for the very ampleness of $D_n$, Theorem V.1.9 for the Hodge index inequality,
Theorem V.1.6 and Corollary III.7.7 for the cohomology of $D$, Theorem I.5.1 and Theorem II.8.6A for
the nonsingularity of a general member; Dolgachev's Lemma 8.1.3 for the computation at $C^2=0$; and
the incidence count of Vakil's Theorem 13.4.2, carried out for the morphism $\varphi$ rather than for
a closed subvariety of $\PP^N$.
:::
