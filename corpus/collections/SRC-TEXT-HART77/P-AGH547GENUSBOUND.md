---
schema: qual/card@1
id: P-AGH547GENUSBOUND
kind: problem
title: Maximal arithmetic genus of a divisor of given degree on a cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Adjunction
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.7, the retained Egbert calculation, the cubic-surface
    blowup/anticanonical description, V.1.9 Hodge index, and the ample-line-
    bundle/Bertini inputs. The retained source passes to a standard-form
    coordinate calculation; the sharp bound is more directly obtained from
    H=-K_S, H^2=3, Hodge index D^2<=d^2/3, and the parity
    D^2 congruent d mod 2 forced by adjunction. The maximizing numerical
    classes are mH for d=3m, mH+L for d=3m+1, and mH+Q for d=3m+2,
    where L is a line and Q=H-L is a smooth residual conic. Their required
    linear systems are shown below to contain smooth irreducible members
    without using the later V.4.8 classification.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete Hodge/parity bound and all three sharpness families.
    Tightened the conic construction to use a base-point-free residual
    subpencil rather than claiming completeness, and used the standard
    Bertini irreducibility theorem for the base-point-free birational system
    |H+L|. Verified the low-degree cases d=1,2,3 separately within the same
    line/conic/hyperplane construction.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published-solution pass for issue #121. Read the printed exercise in
    Hartshorne, Algebraic Geometry (1977), V.4.7, printed p. 407 (text
    version tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed
    p. N is PDF p. N+15), with Proposition 4.8, printed pp. 401-402, and
    Corollary 4.13, printed p. 406. Read at the cited place: National Taiwan
    University Algebraic Geometry II (2020 Spring), Chapter V §4 Exercise 7
    by Yi-Tsung Wang, printed pp. 16-17, text version
    tmp/sources/ntu-ag2-chapter5.md, and the same two pages of the PDF,
    where the extracted text loses the signs of two displays. Checked: the
    equivalence the source asserts between its two displayed inequalities
    (substituting 3a = d + sum b_i), which holds with the correct adjunction
    formula 2p_a(D)-2 = a^2-sum b_i^2-d and fails by 2 with the formula as
    printed; its two inequalities, which are (1/2)(sum b_i-2d)^2 >= 0 and
    Cauchy-Schwarz 6 sum b_i^2 >= (sum b_i)^2; and the degree, self-
    intersection and arithmetic genus of every class it lists. Defect found
    in the source: in the d = 2 mod 3 family the multiplicities are
    interchanged, so the printed vector has degree d+2 and not d, while the
    vector with (d+1)/3 on e_1,...,e_4 and (d-2)/3 on e_5,e_6 has degree d
    and the genus the source reports; the card displays the latter and says
    so. Also found: the source asserts attainment by an irreducible
    nonsingular curve without argument, and records d = 4 as unknown. Not
    checked: no source outside this one was read for this card.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the published argument transcribed, each step naming
    its source with its printed page; the card's earlier Hodge-index and
    Bertini construction, which was not a transcription, is replaced by it.
    Steps intersection-data, reduction-to-self-intersection,
    hodge-inequality, genus-bound, extremal-classes and small-degrees are the
    source's pages 16-17; step nonsingular-members supplies the step from a
    class to a curve in it from the book's Corollary 4.13(a),(b), printed
    p. 406, which the source does not supply, and names d = 4 as the case
    where it fails.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the card beside the source. Recomputed, for each family, the
    degree 3a-sum b_i, the self-intersection a^2-sum b_i^2 and
    p_a = (D^2-d)/2+1, and checked the equality with the bound in the
    residue class of each; checked the bound's integrality step in the
    residues 1 and 2 modulo 3; checked the hypotheses of (4.13)(a) for each
    of the classes used, which hold for d > 4 in the second family, d > 2 in
    the third and all d > 0 in the first, and separately at d = 5; checked
    that the d = 4 class of the second family has D.F_56 = 0, so that
    (4.13) does not apply to it. Not reviewed and not supplied: no proof
    that the maximum at d = 4 is achieved, and none was added; the
    2026-11-16 COMPLAINTS record names that case.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass, on the reader's findings for this card. The attainment of the
    maximum at d = 4 was left open on a false premise. The class
    D = 4\ell-(e_1+e_2+e_3+e_4)-2(e_5+e_6) is H+F_56, and D.E_i = b_i > 0,
    D.F_ij = 4-b_i-b_j >= 0 with 0 only at F_56, and D.G_i = b_i > 0, so D
    meets all 27 lines nonnegatively and has D^2 = 4 > 0: it is alternative
    (c) of Exercise V.4.8, whose sufficiency is on P-AGH548IRREDCLASSES from
    Dolgachev's Theorem 8.2.19, Harbourne's Corollary II.3, Theorem III.1(a)
    and Lemma II.6(b), and Bertini's theorem in characteristic 0. So the
    exercise's second request holds for every d > 0, d = 4 included, and the
    card now says so. Also corrected: the sentence that a = d and
    sum b_i = 2d "in each case" of the extremal classes, which fails for the
    d = 5 class (a = 4, sum b_i = 7, kept as its own case); and the citation
    of Proposition 4.8(e), which the book states for effective divisors, now
    with the source's own reduction D = D_1-D_2 and D_1, D_2 effective.
    Checked in this pass: the three line-intersection formulas for H+F_56, its
    self-intersection, the ampleness inequalities for each family, and that
    the d = 5 class satisfies them too. Not checked: no source outside those
    named was read for this card.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The card now closes both requests for every d: the bound from the source's
    Cauchy--Schwarz argument, attainment by Corollary 4.13(b) of the book for
    the ample classes and at d = 4 by condition (c) of Exercise V.4.8. The
    characteristic 0 hypothesis of the Bertini step is carried at the place it
    is used. Process and provenance commentary is removed from the rendered
    card.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read against the source and the book. Recomputed for every family the
    degree, the self-intersection and p_a, and checked equality with the bound
    in its residue class; checked the integrality step in the residues 1 and 2;
    checked the hypotheses of (4.13)(a) family by family and for d = 5; checked
    the line intersections and the self-intersection of H+F_56 and that they
    are the hypotheses of condition (c). Not reviewed: the third family's
    printed multiplicities are recorded as an error of the source and the
    corrected vector is displayed, not derived from anything new; and no
    characteristic p statement is made anywhere on the card.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass, on the second reader's findings for this card. The last event
    of this date ended "no characteristic p statement is made anywhere on the
    card", which is false of the card it describes: the step for the degree 4
    class already said "Bertini's theorem in characteristic 0", and the
    attainment at d = 4 rests on condition (c) of Exercise V.4.8, whose
    sufficiency is proved on P-AGH548IRREDCLASSES from Dolgachev's Theorem
    8.2.19, Harbourne's Corollary II.3, Theorem III.1(a) and Lemma II.6(b) with
    Bertini's theorem in Corollary III.10.9, printed p. 274, a theorem of
    characteristic 0. Read again for this: Corollary 4.13 of Hartshorne,
    printed p. 406, with its proof, which cites Bertini's theorem II.8.18,
    printed p. 179; II.8.18 is stated for a nonsingular closed subvariety of
    projective space over an algebraically closed field with no hypothesis on
    the characteristic, and III.7.9.1, printed p. 273, adds only the
    connectedness of the hyperplane section. So Corollary 4.13(b) gives the
    irreducible nonsingular curve for the ample classes in every
    characteristic, and it is the degree 4 class alone that needs
    characteristic 0. Open, and named here and not on the rendered card: the
    attainment at d = 4 over an algebraically closed field of characteristic
    p > 0. The card now states the field, gives the hypothesis at the two
    places it is used, and claims attainment at every d different from 4 over
    any algebraically closed field and at d = 4 in characteristic 0. Not read
    in this pass: Dolgachev's Theorem 8.2.19 and Harbourne's Lemma II.6 beyond
    the statements the other card records, and no source outside those named
    on the two cards.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution states its field, algebraically closed k, and splits the
    attainment: Corollary 4.13(b) for every degree but 4, in every
    characteristic, from its Bertini II.8.18; and the degree 4 class H+F_56
    from condition (c) of Exercise V.4.8 under the hypothesis that k have
    characteristic 0. The claims of steps nonsingular-members and conclusion no
    longer assert attainment at every d > 0 without a hypothesis. No proof was
    added for d = 4 in characteristic p, and none is claimed.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fourth pass, on the reader's third report: one page in the third pass's
    event of this date is wrong. That event cites "III.7.9.1, printed p. 273"
    for the connectedness of the hyperplane section. Remark 7.9.1 is printed
    on p. 245, in the text version
    tmp/sources/hartshorne-1977-algebraic-geometry.md under the marker for PDF
    page 260, where printed p. N is PDF p. N+15. The other page that event
    cites was rechecked here and stands: Corollary 10.9, printed p. 274, is
    under the marker for PDF page 289. The argument does not move with the
    number: II.8.18, printed p. 179, gives the regular hyperplane section for a
    nonsingular closed subvariety of projective space over an algebraically
    closed field in every characteristic, and Remark 7.9.1 adds that the
    section is connected, hence irreducible and nonsingular, when dim X >= 2.
    The event that carried the wrong page is left as written, and the
    correction is the record of this date in COMPLAINTS.md.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The attainment at d = 4 in characteristic p, recorded as open in the
    third and fourth passes of 2026-11-16 and in COMPLAINTS.md, is now
    proved, and the card claims attainment at every d > 0 over an
    algebraically closed field of any characteristic. The two steps that
    excluded it, nonsingular-members and conclusion, are rewritten, and
    the degree 4 paragraph no longer routes through Corollary III.10.9,
    printed p. 274, whose Bertini hypothesis is characteristic 0: it
    cites condition (c) of Exercise V.4.8, whose sufficiency
    P-AGH548IRREDCLASSES proves in every characteristic in 7d548c5699 by
    Dolgachev's Theorem 8.2.19, printed p. 265, Harbourne's Corollary
    II.3, Theorem III.1(a) and Lemma II.6(b), preprint pp. 3, 4 and 7,
    and the incidence count of Vakil's Bertini theorem, printed p. 375.
    Checked in this pass by recomputation from Proposition 4.8 of the
    book, printed pp. 401-402: H + F_56 is 4l - (e_1+e_2+e_3+e_4) -
    2(e_5+e_6), so a = 4, sum_i b_i = 8, d = 3a - sum_i b_i = 4,
    D^2 = 16 - 12 = 4 and p_a = 1; D.E_i = b_i and D.G_i = 2a -
    (sum_k b_k - b_i) = b_i are positive, and D.F_ij = 4 - b_i - b_j is
    2, 1 or 0, vanishing at F_56 alone, so D meets all 27 lines
    nonnegatively and has D^2 > 0, which is condition (c). Also checked:
    that condition (c) is what P-AGH548IRREDCLASSES assumes, D.L >= 0
    for every line with D^2 > 0, and that D.H = 4 >= 2 is the input its
    Hodge-index step needs. The two events of 2026-11-16 saying that no
    characteristic p attainment is claimed are superseded here and left
    as written, as the corrections of that date are. Not read in this
    pass: Dolgachev's Theorem 8.2.19 and Harbourne's Lemma II.6 beyond
    the statements and pages P-AGH548IRREDCLASSES records, and no source
    outside those named on the two cards. No statement of the exercise
    changed, and no part of it passes from open to proved other than the
    d = 4 case.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The remark of the preceding event of this date, on the rendered card:
    its closing sentence still read that the sufficiency of condition (c) of
    Exercise V.4.8 "is proved on P-AGH548IRREDCLASSES and needs
    characteristic 0 there", which the same repair falsified, that card
    being characteristic-free since 7d548c5699. The sentence now ends "in
    every characteristic". Nothing else on the card changed: the problem
    statement, both step statements, every proof and the rest of the remark
    are as they were, and this event changes no mathematics. Checked after
    the edit: ./.venv/bin/python -m qualc.authoring check
    P-AGH547GENUSBOUND reports "schema and Markdown parsing OK (single
    card)", tmp/lam.sh numbers the steps 1 to 9 with QED labels present,
    tools/check_macros.py reports OK, and a search of the rendered text for
    "characteristic" finds four sentences, each saying either that a cited
    theorem carries no characteristic hypothesis or that the attainment
    holds in every characteristic; no rendered sentence restricts anything
    to characteristic 0.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Independent verification of the intersection numbers the preceding
    events of this date quote, run as a script rather than by hand, since
    they are what places the d = 4 class in condition (c) of Exercise V.4.8.
    With a class a*l - sum_i b_i*e_i stored as (a, -b_1, ..., -b_6) and the
    form u.v = u_0 v_0 - sum_{i>=1} u_i v_i (l^2 = 1, e_i^2 = -1, l.e_i =
    0), the 27 lines were built as E_i = e_i, F_ij = l - e_i - e_j and
    G_j = 2l - sum_{i != j} e_i, and the script reported: every one of the
    27 has self-intersection -1; D = (4,-1,-1,-1,-1,-2,-2) = H + F_56
    pairs nonnegatively with all of them, with a single zero at F_56 and
    values 1, 1, 1, 1, 2, 2 on the E_i, 1, 1, 1, 1, 2, 2 on the G_j and
    0, 1, 2 on the F_ij; D^2 = 4; deg D = 3*4 - 8 = 4; p_a = 1. This
    agrees with the hand computation recorded above, including the identity
    D.G_j = b_j, which follows from 2a = sum_i b_i = 8. No text of the card
    changed, and no claim is weakened or added.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Two repairs to the siting of the attainment for degrees other than 4, and
    no change of statement. Step nonsingular-members said that the proof of
    Corollary 4.13(b) rests on Bertini's theorem II.8.18 alone; it rests on
    II.8.18 and III.7.9.1, as the book's own proof of the corollary says, and
    the step now names both, with what each supplies: II.8.18 the regularity of
    the section, by the count of the bad hyperplanes B_x at each closed point,
    and III.7.9.1 the connectedness, which is Corollary III.7.9 with its
    vanishing III.7.8. Page correction: the event of 2026-11-16 above places
    III.7.9.1 at printed p. 273; it stands on printed p. 245, and Corollary
    III.7.9 on printed p. 244, the retained PDF carrying Corollary 7.9's proof
    on PDF p. 260, whose printed folio is 245, so that printed page = PDF page
    - 15 holds there as it does at the folios 179 and 270 checked for the other
    citations. Read for this pass: Hartshorne, Algebraic Geometry (1977),
    Corollary V.4.13 with its proof, printed p. 406, Theorem II.8.18 with its
    proof, printed pp. 179-180, and Corollary III.7.9 with Remark 7.9.1,
    printed pp. 244-245, in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    with the folio of PDF p. 260 checked in the retained PDF. Not checked: the
    rendered page, and no printing other than the text version beside the
    retained PDF. The degree 4 case is unchanged and still rests on condition
    (c) of Exercise V.4.8 as P-AGH548IRREDCLASSES now proves it.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The degree 4 attainment is replaced by a shorter proof that does not leave
    this card: H + E_6 = pi^*(3L) - E_1 - ... - E_5 is the pullback of the
    class of Corollary 4.7 of the book with r = 5, printed p. 405, which that
    corollary proves very ample on the blowup of the plane at five points;
    H + E_6 meets E_6 in 0, so its sections are the pullbacks of the sections
    of that class, and a general member of |H + E_6| is isomorphic to a general
    member of the very ample system, hence irreducible and nonsingular by
    II.8.18, printed p. 179, with III.7.9.1, printed p. 245. The numbers were
    checked from Proposition 4.8 of the book: (H+E_6)^2 = 9-5 = 4,
    (H+E_6).K = -9+5 = -4, so p_a = 1, which is the bound at d = 4. The class
    H + F_56 of the earlier numbering, its nonnegativity on the 27 lines and
    the route through condition (c) of Exercise V.4.8 are kept as an
    alternative attaining the same bound, so nothing proved is withdrawn. Read
    for this pass: Hartshorne, Corollary V.4.7 with its proof, printed pp.
    405-406, Proposition 4.8, printed pp. 401-402, and II.8.18 with III.7.9.1
    at the pages recorded in the event above. Not checked: the rendered page,
    and no printing other than the text version beside the retained PDF.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Second published proof of the bound, located in a retained set the earlier
    passes did not name. Read Yang Pi-Yeh, Hartshorne Solutions (9 June 2019),
    Solution 5.4.7, printed pp. 109-110, rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page (the folios 109 and 110 stand at the foot of those pages). Checked
    against the book: the exercise of Hartshorne, V.4.7, printed p. 407, read
    again on the PDF page 422, which carries folio 407, asks for the two bounds
    by the residue of d modulo 3 and for achievement by an irreducible
    nonsingular curve for every d > 0, and the source proves the first of these
    in both residues. Recomputed: the identity substituting a = (d + sum b_i)/3
    into p_a = (1/2)(a-1)(a-2) - (1/2)sum b_i^2 + (1/2)sum b_i; the step
    -(1/2)sum b_i^2 <= -(1/12)(sum b_i)^2 from 6 sum b_i^2 >= (sum b_i)^2; the
    two completed-square bounds; the integrality of (1/6)(d-1)(d-2) in the
    residues 1 and 2 modulo 3; and, in each of the three classes the source
    lists, the degree 3a - sum b_i and the genus, which equal d and the bound
    of that residue. At d = 4 the d = 3k + 1 class with k = 1 is
    4l - (e_1+...+e_4) - 2(e_5+e_6) = H + F_56, the class of step
    nonsingular-members. Not checked: Yang's Solutions outside printed pp.
    109-111, and the printed book itself, only the retained copy.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now carries Yang Pi-Yeh's Solution 5.4.7 at printed pp. 109-110
    as a second proof of the bound, with its two completed-square inequalities,
    its three attaining classes and its one gap: the source says of those
    classes only that they achieve the bound, so the exercise's request for an
    irreducible nonsingular member is not proved there, and the remark says the
    card's own step is what supplies it. The statement, the steps and the
    attainment argument are unchanged, and no part of the proof was moved from
    proved to open or the reverse.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Page correction to the degree 4 proof, and no change of mathematics.
    Corollary 4.7 of Hartshorne, V.4, is stated on printed p. 400, with its
    proof running from there to printed p. 401; the source-corrected event of
    2026-11-19 above, in both of its page references, and the rendered degree
    4 paragraph cited printed p. 405, which is where the proof of Theorem 4.11
    and Corollary 4.13 stand, not Corollary 4.7. The event itself is left as
    written, per QUAL-11; this one carries the correction. Checked in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, whose
    markers for PDF pages 415 and 416 give printed pages 400 and 401 by the
    offset printed = PDF - 15 that the folios 179, 245 and 270 also satisfy
    there: the statement of Corollary 4.7, with Theorem 4.6 and its proof,
    lies after the marker of PDF p. 415 and before that of PDF p. 416, and
    the proof of the corollary crosses that second marker. The mathematics
    is unchanged: Corollary 4.7 proves that for each r = 0,...,6 the linear
    system d' = |pi^*3L - E_1 - ... - E_r| embeds the blowup of P^2 at r
    points in P^{9-r}, and r = 5 is the case used. Not checked: any printing
    of the book, only the text version retained in tmp/sources.
- event: source-checked
  by: claude
  date: 2026-11-22
  note: >-
    Published-solution pass for issue #160, on the transcription rule. The
    exercise's second request, attainment of the bound by an irreducible
    nonsingular curve, is proved by no retained solution set, and the
    "Published solution" remark now says so and names the sets searched.
    Read for that, each at its own numbering: Egbert, entry 5.4.8, which
    states the bound and then the existence of a smooth connected curve of
    each degree and genus as a claim whose numerical conditions it verifies,
    taking the curves from Harris--Eisenbud, Curves in Projective Space,
    Theorem 3.13, for the cubic surfaces not on a quadric, and whose genus
    range at d=4, g > 8/sqrt(3) - 3 and g <= 5/3, contains no integer; Yang
    Pi-Yeh, Solution 5.4.7, and the National Taiwan University
    Algebraic Geometry II (2020 Spring), Chapter V §4 Exercise 7, by Yi-Tsung
    Wang, which prove the bound and say only that the listed classes achieve
    it; and, for absence, the retained sets that carry no Chapter V §4
    exercise, Borcherds (through IV.1), Cais (through Chapter 4),
    Cutrone--Marshburn (Chapters 1 and 2), Ionita--Kumar (Chapter I), Kim
    (§2.4), Lomont, Okamoto (§II.9), Park (Chapter 4 and §V.5), Saglam--Chris (Chapter III),
    Sam (through IV.6), Stein (III.7), Troiani (Chapter II), Reiser (IV.2.5)
    and the Chapter 1 notes of btg. Also read: Corollary V.4.13 with its
    proof, that part (b) is a consequence of II.8.18 and III.7.9.1; Theorem
    II.8.18, stated for a nonsingular closed subvariety of PP^n_k with no
    hypothesis on the characteristic; and Remark III.7.9.1, that the section
    is connected, hence irreducible, and regular, hence nonsingular, when
    dim X >= 2. Two citations are corrected in the same pass, on the proof of
    step intersection-data: its p_a line now cites the virtual arithmetic
    genus of Chapter V §1 Exercise 3(c), 2p_a(D)-2 = D.(D+K_X), for a class
    that need not be effective, with items (e) and (g) of Proposition 4.8
    kept as the effective case, and its degree line cites (c) with the
    pairing of (b) rather than (e), whose hypothesis is effectiveness. Read
    for that: Exercise V.1.3(a), (b) and (c) in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, and the proof of
    Proposition 4.8, which reads (g) off the adjunction formula of Ex. 1.3.
    Third, the degree 4 paragraph now proves what it asserts about sections:
    pi is the monoidal transformation of Chapter V §3 at the sixth point, so
    pi_*O_X = O_{X'} by Proposition V.3.4, and the projection formula gives
    H^0(X, H+E_6) = H^0(X', d'). Read for that: Proposition V.3.4, pi_*O = O
    and R^i pi_* O = 0 for a monoidal transformation, and the intersection
    (H+E_6).E_6 = 1 - 1 = 0. No statement changed and no proof step's
    mathematics changed. Not read: any printing of the book, only the text
    version in tmp/sources.
- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    The coordinates of step intersection-data are now sited. As the card stood,
    D ~ a l - sum_ib_ie_i was written with no statement that a smooth cubic
    surface over an algebraically closed field of characteristic p is the
    blowup of P^2 at six points, which is what Proposition 4.8 and Notation
    4.7.3 assume and what Theorem V.4.9 does not supply for an arbitrary cubic
    surface. The solution's opening sentence now names a geometric marking,
    cites Dolgachev and Duncan, Automorphisms of cubic surfaces in positive
    characteristic (2017), §2, over an algebraically closed field of arbitrary
    characteristic, and Castelnuovo's criterion, Theorem V.5.7, and points at
    step geometric-marking of P-AGH548IRREDCLASSES, which gives the argument in
    full. Read for this: the same two sources, at the places that card's event
    of this date records. No step changed and no claim was weakened.
- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    The event above of this date names Dolgachev and Duncan, §2, and
    Castelnuovo's criterion, Theorem V.5.7, as what the opening sentence cites
    for the geometric marking. That attribution is withdrawn on this card too:
    P-AGH548IRREDCLASSES now proves its step geometric-marking from R. Vakil,
    The Rising Sea (21 October 2025), Theorem 27.0.2, and this card's opening
    sentence cites the same numbered statement and points at that step. Nothing
    in the argument of this card changes and no claim is added or weakened.
---

::: {.problem}
If $D$ is any divisor of degree $d$ on the cubic surface (4.7.3), show that
$$
p_a(D) \leqslant \begin{cases}\frac{1}{6}(d-1)(d-2) & \text{if } d \equiv 1,2\, (\bmod 3) \\ \frac{1}{6}(d-1)(d-2)+\frac{2}{3} & \text{if } d \equiv 0\, (\bmod 3)\end{cases}
$$
Show furthermore that for every $d>0$, this maximum is achieved by some irreducible nonsingular curve.
:::

::: {.solution}

Write $X$ for the cubic surface over an algebraically closed field $k$, with $-K_X=H$ its hyperplane
class and $H^2=3$, and let $D$ be a divisor of degree $d=D\cdot H$. The expression $D\sim a\ell-\sum_ib_ie_i$
below is taken in a geometric marking of $X$: a set of six mutually skew lines, whose existence and
whose blowdown to $\PP^2$ hold over an algebraically closed field of any characteristic, so that $X$ is
the blowup of $\PP^2$ at six points with $\Pic X$ free on $\ell,e_1,\ldots,e_6$ (R. Vakil, *The Rising Sea* (21 October 2025),
Theorem 27.0.2, over an algebraically closed field with no hypothesis on the characteristic; step
geometric-marking of [[P-AGH548IRREDCLASSES]] gives the argument, with the general position of the six
points).
The class $H$ of a hyperplane section is then $3\ell-\sum_ie_i$.

::: pf

::: {.pf-step #intersection-data}
For a class
$$
D\sim a\ell-\sum_{i=1}^6b_ie_i
$$
one has
$$
d=\deg D=3a-\sum_ib_i,
\qquad
D^2=a^2-\sum_ib_i^2,
\qquad
D\cdot K_X=-d,
\qquad
p_a(D)=\tfrac12(D^2-d)+1 .
$$

::: pf-proof
The line bundle computations are items (b), (c), (d) and (f) of Proposition 4.8 of the book: the degree is $D\cdot h=3a-\sum_ib_i$ by (c) and the pairing of (b), the self-intersection is $a^2-\sum_ib_i^2$ because
$\ell^2=1$ and $e_i^2=-1$ with all other pairings zero, and $D\cdot K_X=-D\cdot h=-d$ by (d). A class
need not be effective, so the genus is the virtual arithmetic genus of Chapter V §1 Exercise 3(c),
$2p_a(D)-2=D\cdot(D+K_X)$, which is the ordinary arithmetic genus when $D$ is effective; items (e) and
(g) of Proposition 4.8 are that case, and the book's proof of (g) reads it off the same adjunction
formula of Exercise 1.3. Chapter V §4 Exercise 7 of the National Taiwan University *Algebraic
Geometry II* homework (2020 Spring), by Yi-Tsung Wang writes $D=D_1-D_2$ with
$D_1,D_2$ effective and reads $\deg D=3a-\sum_ib_i$ and $D^2=a^2-\sum_ib_i^2$ off (4.8)(b) and (e),
which the book states for effective divisors; it then writes "$2p_a(D)=D^2+D\cdot K=a^2-\sum
b_i^2-\deg D$", whose left side omits the $-2$ of the adjunction formula.
:::

:::

::: {.pf-step #reduction-to-self-intersection}
The genus bound of the exercise is equivalent to
$$
a^2-\sum_i b_i^2\le\frac{d^2}{3}.
$$

::: pf-proof
By step [](#intersection-data){.pf-ref},
$$
p_a(D)\le\tfrac16(d-1)(d-2)+\tfrac23
\iff
2p_a(D)-2\le\tfrac{d^2-3d}{3}
\iff
a^2-\sum_ib_i^2\le\tfrac{d^2}{3},
$$
using $a^2-\sum b_i^2-d=2p_a(D)-2$ and $(d-1)(d-2)=d^2-3d+2$. This is the reduction of the source,
which says that it suffices to prove $(d+\sum b_i)^2-9\sum b_i^2-9d\le 3d^2-9d$, the same inequality
after $3a=d+\sum b_i$.
:::

:::

::: {.pf-step #hodge-inequality}
$$
2d\sum_ib_i+\Bigl(\sum_ib_i\Bigr)^2-9\sum_ib_i^2\le 2d^2 .
$$

::: pf-proof
The two inequalities of the source, for arbitrary reals:
$$
2d^2\ge 2d\sum_ib_i-\tfrac12\Bigl(\sum_ib_i\Bigr)^2,
$$
which is $\frac12\bigl(\sum b_i-2d\bigr)^2\ge0$, and
$$
2d\sum_ib_i-\tfrac12\Bigl(\sum_ib_i\Bigr)^2
\ge
2d\sum_ib_i+\Bigl(\sum_ib_i\Bigr)^2-9\sum_ib_i^2,
$$
which is $6\sum_ib_i^2\ge(\sum_ib_i)^2$, Cauchy--Schwarz for six numbers, the inequality the source
cites. Together they give the displayed inequality.
:::

:::

::: {.pf-step #genus-bound}
For every divisor $D$ of degree $d$ on the cubic surface,
$$
p_a(D)\le
\begin{cases}
\tfrac16(d-1)(d-2)+\tfrac23, & d\equiv0\pmod3,\\
\tfrac16(d-1)(d-2), & d\equiv1,2\pmod3 .
\end{cases}
$$

::: pf-proof
Steps [](#reduction-to-self-intersection){.pf-ref} and [](#hodge-inequality){.pf-ref} give
$a^2-\sum b_i^2\le d^2/3$, hence $p_a(D)\le\frac16(d^2-3d+6)=\frac16(d-1)(d-2)+\frac23$. If
$d\equiv1$ or $2$ modulo $3$ then $(d-1)(d-2)$ is divisible by $3$ and by $2$, so
$\frac16(d-1)(d-2)$ is an integer, and since $p_a(D)$ is an integer the bound sharpens to it. This
is the source's argument in the two residues, and it is the first display of the exercise.
:::

:::

::: {.pf-step #extremal-classes}
For each of the following classes the degree is $d$ and $p_a$ equals the bound of step
[](#genus-bound){.pf-ref}:
$$
d\equiv0:\quad D=d\ell-\tfrac d3\sum_{i=1}^6e_i ,
$$
$$
d\equiv1,\ d>4:\quad
D=d\ell-\tfrac{d-1}{3}(e_1+e_2+e_3+e_4)-\tfrac{d+2}{3}(e_5+e_6),
$$
$$
d\equiv2,\ d>5:\quad
D=d\ell-\tfrac{d+1}{3}(e_1+e_2+e_3+e_4)-\tfrac{d-2}{3}(e_5+e_6),
$$
$$
d=5:\quad D=4\ell-2e_1-e_2-e_3-e_4-e_5-e_6 .
$$

::: pf-proof
In the first three families $a=d$ and $\sum_ib_i=2d$, so $d=\deg D$ by step
[](#intersection-data){.pf-ref}. For the first, $\sum_ib_i^2=6(d/3)^2=2d^2/3$, so
$D^2=d^2-2d^2/3=d^2/3$ and $p_a(D)=\frac12(d^2/3-d)+1=\frac16(d-1)(d-2)+\frac23$, which is equality in
step [](#genus-bound){.pf-ref}. For the second, with $k=\frac{d-1}{3}$ one has
$\sum_ib_i^2=4k^2+2(k+1)^2=6k^2+4k+2$ and $d=3k+1$, so $D^2=d^2-6k^2-4k-2=\frac{d^2-4}{3}$ and
$p_a(D)=\frac12\left(\frac{d^2-4}{3}-d\right)+1=\frac16(d-1)(d-2)$. For the third the same
computation with $k=\frac{d-2}{3}$ and $d=3k+2$ gives $D^2=\frac{d^2-4}{3}$ and
$p_a(D)=\frac16(d-1)(d-2)$. For $d=5$ the class has $a=4$, $\sum_ib_i=7$,
$\sum_ib_i^2=4+5=9$, so $D^2=16-9=7$ and $p_a(D)=\frac12(7-5)+1=2=\frac16\cdot4\cdot3$.

The source prints the third family with the multiplicities interchanged, $\frac{d-2}{3}$ on
$e_1,\ldots,e_4$ and $\frac{d+1}{3}$ on $e_5,e_6$; for that vector $\sum_ib_i=2d-2$ and the degree is
$3d-(2d-2)=d+2$, with $d=3m+2$, so the degree it states fails there. The vector displayed above is the
one for which the degree and the value of $p_a$ that the source reports both hold.
:::

:::

::: {.pf-step #small-degrees}
For $d=1$ and $d=2$ the bound is attained by a line and by a conic, and for $d=4$ by the class
$$
D=4\ell-(e_1+e_2+e_3+e_4)-2(e_5+e_6),
$$
which is $H+F_{56}$ and has degree $4$ and $p_a=1$.

::: pf-proof
A line has $d=1$, $D^2=-1$ and $p_a=0=\frac16\cdot0\cdot(-1)$; a conic has $d=2$, $D^2=0$ and
$p_a=0=\frac16\cdot1\cdot0$; both are nonsingular irreducible curves, and these are the source's "for
$d=1$ and $2$, a line and a conic achieve the maximum, respectively". At $d=4$ the second family of
step [](#extremal-classes){.pf-ref} reads
$D=4\ell-(e_1+e_2+e_3+e_4)-2(e_5+e_6)$, which is $H+F_{56}$ and has degree $4$, self-intersection
$16-(4+8)=4$ and $p_a=\frac12(4-4)+1=1$, the maximum of step [](#genus-bound){.pf-ref} for
$d\equiv1\pmod3$. The source excludes $d=4$ from that family and writes "For $d=4$, I don't know".
:::

:::

::: {.pf-step #nonsingular-members}
For every $d$ the class of step [](#extremal-classes){.pf-ref} or [](#small-degrees){.pf-ref} of
degree $d$ contains an irreducible nonsingular curve over every algebraically closed field $k$.

::: pf-proof
For the classes of the first three families of step [](#extremal-classes){.pf-ref} and for the class of
degree $5$, Corollary 4.13 of the book, applies. Its part (a) says that $D$ is ample
exactly when $b_i>0$ for each $i$, $a>b_i+b_j$ for each $i,j$, and $2a>\sum_{i\ne j}b_i$ for each $j$;
for those classes $a=d$ and $\sum_ib_i=2d$, so the last condition reads $2d>2d-b_j$, the middle one
$d>b_i+b_j$, which for the largest pair is $d>\frac{2(d+2)}{3}$, that is $d>4$, in the second family,
$d>\frac{2(d+1)}{3}$, that is $d>2$, in the third, and $d>\frac{2d}{3}$ in the first, and $b_i>0$
because $d>0$ in the first family, $d>1$ in the second and $d>2$ in the third. The class of degree $5$
has $a=4$, $b_1=2$ and the remaining $b_i$ equal to $1$, so $a=4>b_i+b_j$ and
$2a=8>6=\sum_ib_i-1\ge\sum_{i\ne j}b_i$. By Corollary 4.13(b) each of these classes contains an
irreducible nonsingular curve; the corollary's proof uses Bertini's theorem for hyperplane sections, II.8.18 of the book, together with III.7.9.1, and neither carries a hypothesis on
the characteristic: II.8.18 is stated for a nonsingular closed subvariety of $\PP^n_k$ over an
algebraically closed field $k$ and proves regularity by counting the dimension of the bad hyperplanes
$B_x$, and the connectedness III.7.9.1 adds is Corollary III.7.9, for an integral
normal projective variety of dimension at least $2$ over an algebraically closed field, proved from
the vanishing of III.7.8 and the exact sequence of $qD$ with $q$ large. So these
degrees are attained over every algebraically closed field $k$.

The classes of degrees $1$ and $2$ are the line and the conic of step
[](#small-degrees){.pf-ref}. The class of degree $4$ is $H+E_6=\pi^*(3L)-E_1-\cdots-E_5$, the pullback of
the class $\mathfrak d'$ of Corollary 4.7 of the book, with $r=5$, which that corollary
proves very ample and which embeds the blowup of $\PP^2$ at five points in $\PP^4$. The morphism
$\pi$ is the monoidal transformation of Chapter V §3 at the sixth point, so
$\pi_*\OO_X=\OO_{X'}$ with $X'$ that blowup, by Proposition V.3.4, and the projection formula gives
$H^0(X,H+E_6)=H^0(X',\mathfrak d')$; since $H+E_6$ meets $E_6$ in $0$, a general member of
$\linearsystem{H+E_6}$ is the pullback of a general member of $\linearsystem{\mathfrak d'}$ and is isomorphic to
it. And
$$
(H+E_6)^2=9-5=4,\qquad (H+E_6)\cdot K_X=-9+5=-4,\qquad p_a(H+E_6)=\tfrac12(4-4)+1=1,
$$
which is the bound at $d=4$. Bertini's theorem II.8.18 of the book, and the
connectedness of III.7.9.1 give that a general member of $\linearsystem{\mathfrak d'}$, hence of
$\linearsystem{H+E_6}$, is an irreducible nonsingular curve, in every characteristic.
The class $H+F_{56}$ of the
earlier numbering also has degree $4$, square $4$ and $p_a=1$, and meets every one of the $27$ lines
nonnegatively; it attains the same bound, and the sufficiency of condition (c) of
[[P-AGH548IRREDCLASSES|Exercise V.4.8]] gives an irreducible nonsingular member in it too.
:::

:::

::: {.pf-step #conclusion}
The bound of the exercise holds for every divisor of degree $d$, and its maximum is achieved by an
irreducible nonsingular curve for every $d$, over an algebraically closed field $k$ of any
characteristic.

::: pf-proof
The bound is step [](#genus-bound){.pf-ref} and the attainment is step
[](#nonsingular-members){.pf-ref}, in the two residue classes and at $d=4$.
:::

:::

::: pf-qed
Steps [](#intersection-data){.pf-ref}, [](#reduction-to-self-intersection){.pf-ref},
[](#hodge-inequality){.pf-ref} and [](#genus-bound){.pf-ref} are the bound; steps
[](#extremal-classes){.pf-ref}, [](#small-degrees){.pf-ref} and
[](#nonsingular-members){.pf-ref} are the classes that attain it and the curves in them.
:::

:::
:::

::: {.remark title="Published solution"}
National Taiwan University, *Algebraic Geometry II* (2020 Spring, Chin-Lung Wang), Chapter V §4,
Exercise 7, by Yi-Tsung Wang: the reduction of $2p_a(D)-2$ to
$a^2-\sum b_i^2-d$, the bound $a^2-\sum b_i^2\le d^2/3$ by Cauchy--Schwarz and one square, its
sharpening in the residues $1,2$ modulo $3$ by integrality, and the classes attaining it. The source
writes $2p_a(D)=D^2+D\cdot K$ for $2p_a(D)-2=D\cdot(D+K)$; it interchanges the two multiplicities in
its $d\equiv2$ family, so that family as printed has degree $d+2$; and it leaves $d=4$ open, stating
its conclusion for every $d>0$ "possibly except $d=4$".

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 5.4.7, proves the
same bound in a second arrangement of the same two inputs, for arbitrary real $b_i$. With
$a=\frac{1}{3}(d+\sum b_i)$ it writes
$$
p_a(D)=\frac{1}{2}(a-1)(a-2)-\frac{1}{2}\sum b_i^2+\frac{1}{2}\sum b_i
=\frac{1}{18}(d-3+\sum b_i)(d-6+\sum b_i)-\frac{1}{2}\sum b_i^2+\frac{1}{2}\sum b_i,
$$
then $-\frac{1}{2}\sum b_i^2\le-\frac{1}{12}\bigl(\sum b_i\bigr)^2$, which is Cauchy--Schwarz
$6\sum b_i^2\ge\bigl(\sum b_i\bigr)^2$, and
$$
p_a(D)\le\frac{1}{6}d^2-\frac{1}{2}d+1-\Bigl(\frac{1}{6}\sum b_i-\frac{1}{3}d\Bigr)^2
\le\frac{1}{6}(d-1)(d-2)+\frac{2}{3},
$$
sharpened to $\frac{1}{6}(d-1)(d-2)$ in the residues $1,2$ modulo $3$, where $\frac{1}{6}(d-1)(d-2)$
is an integer and so is $p_a(D)$. Its attaining classes are $d\ell-\frac{d}{3}(e_1+\cdots+e_6)$ for
$d\equiv0$, $d\ell-k(e_1+\cdots+e_4)-(k+1)(e_5+e_6)$ for $d=3k+1$ and
$d\ell-k(e_1+e_2)-(k+1)(e_3+\cdots+e_6)$ for $d=3k+2$; at $d=4$ the second is $H+F_{56}$, the class
of step [](#nonsingular-members){.pf-ref}, and its $d\equiv2$ class has degree $d$ where the NTU
solution's printed one has degree $d+2$, so the correction recorded above is confirmed by a second
source. Of those classes the source says only that they "achieve the bound", computing $p_a$; it says
nothing of an irreducible nonsingular member of one, so the exercise's second request is not proved
there and remains the card's own step.

The retained solution sets were searched for this exercise, and none proves the second request. Three
of them contain an exercise of Chapter V §4: Egbert's entry 5.4.8, which states the bound, states the
existence of a smooth connected curve of each degree and genus as a claim whose numerical conditions
it then verifies, and takes the curves themselves from Harris--Eisenbud, *Curves in Projective
Space*, Theorem 3.13, for the cubic surfaces not lying on a quadric; its genus range at $d=4$, which
is $g>\frac{8}{\sqrt3}-3$ and $g\le\frac53$, contains no integer, so it establishes nothing at that
degree; and Yang Pi-Yeh's Solution 5.4.7 and the National Taiwan University Chapter V §4 Exercise 7,
which prove the bound alone. The other retained sets carry no Chapter V §4 exercise: Borcherds, Cais,
Cutrone--Marshburn, Ionita--Kumar, Kim, Lomont, Okamoto, Park, Saglam--Chris, Sam, Stein, Troiani, Reiser and
the Chapter 1 notes of btg. The argument of step
[](#nonsingular-members){.pf-ref} is therefore the card's own: Corollary 4.13(b) of the book for the
ample classes, Corollary 4.7 with Theorem II.8.18 and Remark III.7.9.1 at $d=4$, and, for the second
route at that degree, condition (c) of Exercise V.4.8 as [[P-AGH548IRREDCLASSES]] proves it.

For the curves in those classes: Corollary 4.13(a),(b) of Hartshorne for the ample
ones, and, at $d=4$, condition (c) of Exercise V.4.8, whose sufficiency is proved on
[[P-AGH548IRREDCLASSES]] in every characteristic.
:::
