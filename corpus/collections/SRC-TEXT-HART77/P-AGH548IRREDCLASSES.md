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
degree $1$ on $X$ is a line, and by Theorem 4.9 of the book, printed pp. 402--403, the irreducible
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
self-intersection $0$. The computation is the one in the proof of Dolgachev's Lemma 8.1.3, printed
p. 248, at $C^2=0$.
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
By Theorem 4.9 of the book, printed pp. 402--403, the $27$ classes $E_i,F_{ij},G_j$ are the classes
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
$D_n^2=n^2D^2+2nD\cdot H+H^2=n^2D^2+2nD\cdot H+3>0$. By Theorem 4.11 of the book, printed
pp. 405--406, whose proof is Lemma 4.12 and the enumeration of the $27$ lines and which uses no
hypothesis on the field, $D_n$ is very ample. Hence for every irreducible curve $E$ on $X$,
$0<D_n\cdot E=n(D\cdot E)+H\cdot E$ for every $n\ge1$, which forces $D\cdot E\ge0$: if $D\cdot E<0$,
the left side is negative for $n>H\cdot E$. So $D$ meets every effective class nonnegatively.

Second, $D$ is effective: by B. Harbourne, *Anticanonical Rational Surfaces* (24 January 1996,
arXiv:alg-geom/9509001v2), Corollary II.3, preprint p. 3, a numerically effective divisor meeting the
anticanonical class nonnegatively lies in $\mathrm{Eff}$, and here $-K_X\cdot D=D\cdot H>0$, while
$D\cdot H\ge2$: the Hodge index inequality, Theorem V.1.9 of the book, printed p. 364, gives
$3D^2\le(D\cdot H)^2$ with $D^2>0$, so $(D\cdot H)^2\ge4$ and $D\cdot H$ is a positive integer.

Third, the system is base point free and $h^1$ vanishes: since $-K_X\cdot D=D\cdot H\ge2$,
Harbourne's Theorem III.1(a), preprint p. 7, gives $h^1(X,\OO_X(D))=0$ and that the sections of $D$
are base point (and hence fixed component) free.

Fourth, a general member is reduced and irreducible: since $D^2>0$ the system is not composed with a
pencil, and Harbourne's Lemma II.6(b), preprint p. 4, then gives $D^2>0$ and that the general section
of $D$ is reduced and irreducible.

Finally, it is nonsingular, in every characteristic. Let $\varphi\colon X\to\PP^N$ be the morphism
defined by the base-point-free system $\linearsystem{D}$; then $N=\dim\linearsystem{D}\ge2$,
because a base-point-free pencil has $D^2=0$, and $\varphi$ is generically finite onto a surface,
because if the image of $\varphi$ were a curve then $D=\varphi^*\OO(1)$ would have $D^2=0$. The
morphism $\varphi$ is separable: if $k(X)/k(\varphi(X))$ were not separable, $\varphi$ would
factor as a purely inseparable morphism $f\colon X\to X'$ of degree $p^m>1$ followed by a morphism
to $\varphi(X)$, and the pullback of a general hyperplane would be $p^m$ times a divisor, hence
non-reduced, whereas the general member is reduced by Harbourne's Lemma II.6(b), preprint p. 4.
Consequently $\varphi$ has generic rank $2$, and $\Omega_{X/\varphi(X)}$ is zero at the generic
point: the extension $k(X)/k(\varphi(X))$ is finite and separable of transcendence degree $0$, so
$\dim_{k(X)}\Omega_{k(X)/k(\varphi(X))}=0$ by Theorem II.8.6A, printed p. 174, and the sheaf is
locally free of rank $0$ on a nonempty open set by Exercise II.5.7(a), printed p. 125.

For $x\in X$ let $r(x)$ be the rank of the differential
$d\varphi_x\colon T_xX\to T_{\varphi(x)}\PP^N$, and let
$$
Z=\{(x,H)\in X\times\PP^{N\vee}:\varphi(x)\in H,\ d(\ell_H\circ\varphi)_x=0\},
$$
where $\ell_H$ is a linear form defining $H$. At $(x,H)$ the local equation of the member
$\varphi^{-1}(H)$ on the nonsingular surface $X$ is $\ell_H\circ\varphi$; if its differential is
nonzero at $x$ it is part of a regular system of parameters, so the quotient local ring is regular
of dimension $1$ and the member is nonsingular at $x$ by Theorem I.5.1, printed p. 32. It is
therefore enough to show that the image of $Z$ in $\PP^{N\vee}$ is a proper closed subset.

The locus $r=2$ is nonempty and open, because $\varphi$ has generic rank $2$; hence the locus
$r\le1$ is a proper closed subset of the surface, of dimension at most $1$. Where $r(x)=2$ the
image $d\varphi_x(T_xX)$ is a $2$-plane in $T_{\varphi(x)}\PP^N$, and the hyperplanes $H$ with
$(x,H)\in Z$ are those containing it, a linear subspace of $\PP^{N\vee}$ of dimension $N-3$; this
part of $Z$ has dimension at most $2+(N-3)=N-1$. Where $r(x)=1$ the hyperplanes $H$ with
$(x,H)\in Z$ contain the line $d\varphi_x(T_xX)$, a linear subspace of dimension $N-2$; over the
at most one-dimensional locus $r=1$ this part of $Z$ has dimension at most $1+(N-2)=N-1$. Where
$r(x)=0$ every hyperplane through $\varphi(x)$ satisfies $(x,H)\in Z$. Each component $C$ of the
closed locus $r=0$ is contracted by $\varphi$: if $\restrictionof{\varphi}{C}$ were non-constant, then on the
normalization of $C$ it would be a finite morphism of smooth curves with identically zero
differential, hence not separable by Theorem II.8.6A, printed p. 174. In the factorization of a
finite morphism of curves as a purely inseparable morphism followed by a separable one, the purely
inseparable part has degree $p^m>1$ here, and the pullback of a local parameter of $\varphi(C)$
along it is a $p^m$-th power by Proposition IV.2.5, printed p. 302; so
for a general hyperplane $H$ meeting $\varphi(C)$ the equation $\ell_H\circ\varphi$ would have
multiplicity at least $p$ at the corresponding point of $C$, and $\varphi^{-1}(H)$ would be
non-reduced, contradicting the reducedness of the general member. Hence $\varphi$ maps the locus
$r=0$ to a finite set, and this part of $Z$ lies in the union of the $\PP^{N-1}$ of hyperplanes
through the finitely many points of that set, so it has dimension at most $N-1$.

Thus $Z$ has dimension at most $N-1$, and so does its image in $\PP^{N\vee}$, which is closed
because $X$ is proper. A general hyperplane $H$ therefore lies outside that image, and for such
$H$ no point of the member $\varphi^{-1}(H)$ lies in $Z$, so the member is nonsingular. This is
the incidence count of the proof of Vakil's Bertini theorem, *The Rising Sea* (21 October 2025),
Theorem 13.4.2, printed pp. 375--376, carried out for the morphism $\varphi$ rather than for a
smooth closed subvariety of $\PP^N$: where $\varphi$ is a closed immersion the fibre of $Z$ is the
$\PP^{N-1-\dim X}$ of Vakil's proof, and the cases $r=1$ and $r=0$ above are the additional
$\PP^{N-2}$ and $\PP^{N-1}$ fibres created by the drop in rank. The characteristic-zero Corollary
III.10.9, printed p. 274, is not used.
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
$H-G_i$, $H-F_{ij}$ and $H-E_i$, by the classes of those lines in Theorem 4.9, printed pp. 402--403.
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
Corollary II.3, preprint p. 3, that a numerically effective divisor meeting $-K$ nonnegatively is
effective; Lemma II.6, preprint p. 4, that a fixed-component-free class whose system is not composed
with a pencil has $D^2>0$ and reduced irreducible general section, and that a class whose system is
composed with a pencil is a multiple of a class with reduced irreducible general section; and Theorem
III.1(a), preprint p. 7, that $-K_X\cdot D\ge2$ makes the system base point free with $h^1=0$. The
paper works over an algebraically closed field of arbitrary characteristic, so its Lemma II.6 gives
reduced irreducible members in every characteristic. The nonsingularity of the member of a class of
the third alternative is then the incidence count of Vakil's proof of Theorem 13.4.2, printed
pp. 375--376, carried out for the morphism defined by $\linearsystem{D}$ and stratified by the rank of
its differential: the bad hyperplanes form a closed subset of the dual of dimension at most $N-1$,
the rank-zero stratum being contracted because otherwise the general member would be non-reduced.

I. V. Dolgachev, *Topics in Classical Algebraic Geometry* (September 27, 2010): Lemma 8.1.3 and its
proof, printed p. 248, on irreducible curves of negative self-intersection on a weak Del Pezzo
surface, whose computation step positive-square-satisfies-the-third-condition repeats. The book
takes $\CC$ as its base field, so its Theorem 8.2.19, printed p. 265, on the effective cone is not
used: the numerical effectivity of step third-condition-contains-nonsingular-curve is proved from
Hartshorne's Theorem 4.11, printed pp. 405--406, which has no hypothesis on the characteristic.

Theorem 4.9 of Hartshorne, printed pp. 402--403, for the $27$ lines and for the curves of negative
self-intersection; J. Vakil, *The Rising Sea* (21 October 2025), Theorem 13.4.2 and its proof,
printed pp. 375--376, for the incidence count; Hartshorne, Theorem I.5.1, printed p. 32, Theorem
II.8.6A, printed p. 174, Exercise II.5.7(a), printed p. 125, and Propositions IV.2.1 and IV.2.5,
printed pp. 300 and 302, for the nonsingularity of the general member and for the rank-zero stratum.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 5.4.8, printed p. 110, argues both
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
:::
