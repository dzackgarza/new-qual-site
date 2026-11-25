---
schema: qual/card@1
id: P-AGH5415GENPOSITION
kind: problem
title: Points in general position and exceptional curves on blowups of the plane
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Birational Geometry
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.15 as transcribed here, the retained Andrew Egbert
    companion notes, and the quadratic-transformation formulas in V.4.2.
    The companion gives only a partial r=7,8 count and an abbreviated
    openness argument, and it does not prove the starred r=9 assertion. The
    solution below instead works on the marked blowup: admissible
    transformations give explicit Picard-basis changes, negative curves for
    r<=8 are reduced to exceptional divisors by decreasing plane degree, and
    for r=9 repeated transformations make the degree of a (-1)-class
    unbounded.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof against the V.4.2 quadratic-transform formulas.
    Checked the six-point pullbacks in part (a), the countable bad-locus
    argument in part (c), the degree-decreasing standard-form argument for all
    negative curves when r=7,8, every multiplicity partition and count in the
    56/240 tables, and the r=9 recurrence
    d'=2d-(m_1+m_2+m_3)>=d+1. The final orbit argument uses actual terminal
    exceptional divisors pulled back to the original blowup, so distinct
    lattice classes give distinct (-1)-curves on the fixed surface.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Checked for issue #121 against the printed exercise, Hartshorne V.4.15,
    printed pp. 423-424 (its parts (a)-(e), the starred (e) last). Rechecked
    the decisive computations of the card's own proof. degree-bound-nonneg-square:
    with c = b_3, at most six of the b_i are at least 3 in index, so
    sum b_i^2 <= (a-2c)^2 + 7c^2 = a^2 - 4ac + 11c^2, and 3c <= a gives
    11c < 4a; verified. r7-classes-fifty-six: (3a-1)^2 <= 7(a^2+1) gives
    a^2-3a-3 <= 0, so a <= 3, and the three rows give 7 + 21 + 21 + 7 = 56.
    r8-classes-two-forty: a <= 6 with the Cauchy-Schwarz equality case excluded
    because 5/2 is not an integer, and the seven rows give
    8+28+56+56+56+28+8 = 240; both sums and each row's multinomial count were
    recomputed. negative-curve-is-minus-one-curve: the descent
    a' = 2a-b_1-b_2-b_3 < a with b_i+b_j <= a is the standard quadratic
    transformation of an irreducible plane curve, and the process stops at
    plane degree 0, an exceptional divisor. r7-classes-realized-unique: two
    distinct irreducible curves in one class would have intersection -1, which
    is impossible on a smooth surface. Parts (a) and (c) were read but not
    re-derived: their steps are six-points-general-position-iff,
    six-point-condition-preserved, uncountable-field-lemma,
    bad-locus-proper-closed and dense-general-position-extension. Published
    sources read for this card and what each has: Egbert, printed p. 294,
    parts (a)-(d) with (d) as a list of eight families and no proof that no
    other negative curves exist, and (e) as a citation of Nagata; Dolgachev,
    Proposition 8.2.15, printed pp. 261-262, the count of (-1)-classes only;
    Yang Pi-Yeh, printed p. 112, (a)-(c) sketched, (d) the same two sums
    without the negative-curve assertion, (e) argued. No source has all five.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Checked for issue #121 against the printed exercise, Hartshorne V.4.15,
    printed p. 409, all five parts including the starred (e) on that one page
    (PDF p. 424). The line case is correct: the class h-e_1-e_2 has square
    1-1-1 = -1, and the pair bound b_i+b_j <= a is dropped only for it, which is
    what negative-curve-is-minus-one-curve says. The remark on published
    solutions gave Egbert's (d) as "seven and seven" families and Yang's (d) as
    seven rows for r=7; both counts are wrong. Egbert, printed p. 295, finds 7
    exceptional curves, 21 lines, 21 conics through 5 points and 7 cubics
    through 7 points with one doubled, and writes "Thus we have 14+42=56"; for
    r=8 he lists eight exceptional curves, 28 lines, 56 conics, 8 cubics, 56
    quartics, 28 quintics and the sextics as "the rest", which is 56 to make
    240. That is four families for r=7 and seven for r=8. Yang, printed p. 112,
    lists the same four rows for r=7 --- the tuples (0,1,0,0,0,0,0,0),
    (2,1,1,0,0,0,0,0), (2,1,1,1,1,1,0,0) and (3,2,1,1,1,1,1,1) at 7, 21, 21 and
    7, totalling 7+21+21+7=56 --- and seven rows for r=8, totalling
    8+28+56+56+56+28+8=240. Both sentences of the remark now say so. An
    undated sentence recording what an earlier version of
    negative-curve-is-minus-one-curve asserted is removed; the mathematics of
    the sentence it qualified, that the pair bound fails precisely in the line
    case, is kept. Part (c) is unchanged and stays unproved here: the
    properness in bad-locus-proper-closed is asserted and not derived, and that
    step and the qed remark say so. Not checked: the card's own 56 and 240
    tables were not re-enumerated, Dolgachev's Proposition 8.2.15 was not
    re-read, and nothing was searched for a published proof of the properness
    in (c). The event of 2026-11-16 above had been rewritten in place; it is
    restored to the text it was dated with, and the pages it gives there, 423
    and 424, are PDF pages. This note is its correction.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Under issue #121 the solution is now a transcription, one step per printed
    statement, of what the listed sources prove about the five parts. Read at
    the printed places: M. Nagata, On rational surfaces II, Section 2(c)
    (non-special points), printed p. 279, Lemma 2.2 (corresponding base points),
    p. 278, Lemma 2.5 (independent generic points are non-special), p. 279,
    Proposition 3 (the criterion for special points), p. 279, Theorem 2a
    (bijection between pre-exceptional types and irreducible exceptional curves
    of the first kind), pp. 280--281, Theorem 4a (finitely many for r at most 8,
    infinitely many for r = 9), pp. 283--284, Theorem 3a, p. 282, and
    Proposition 12 (no irreducible negative curve that is not of the first kind
    unless the points are special), p. 293; I. Dolgachev, Topics in Classical
    Algebraic Geometry, Proposition 8.2.15 with its proof and its table,
    printed pp. 261--262, and Section 8.2.6, printed p. 263. The paper's text
    version marks pages only in ten-page blocks; every printed page above was
    read off the paper's own folios in the PDF, which give PDF 1 = printed 271
    and so PDF 7 = 277 for Lemma 2.1, PDF 8 = 278 for Lemma 2.2, PDF 9 = 279 for
    Lemma 2.5 and Proposition 3, PDF 12 = 282 for Theorem 3a, PDF 14 = 284 for
    Theorem 4a, and PDF 21--23 = 291--293 for Propositions 9 to 12. What the
    transcription proves: (b) from the definition and Lemma 2.2, (d) from
    Proposition 12 with Theorem 2a and Dolgachev's count, and (e) from the
    second half of Theorem 4a with Theorem 2a. What it does not prove, and does
    not supply, is named on the card and recorded in COMPLAINTS.md this day:
    part (a) beyond its printed criterion, and part (c) in full. This card's own
    proofs of the parts the sources do not cover --- the six-point class
    computation, the countable-union lemma, the closedness and properness of
    the bad locus, the density argument, and the 56 and 240 tables --- are
    removed from the solution rather than kept beside the transcription, and the
    arithmetic they carried was rechecked against Dolgachev's table and against
    Nagata's r = 8 list before it was dropped.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Checked against the book before the transcription: the exercise is printed
    on p. 409 (PDF p. 424) with parts (a)--(e) and the starred (e) last, the
    hint for (c) being the countable-union lemma and the hint for (e) being the
    line P_1P_2 whose strict transform is made to rise in degree, with the
    attribution to Kodaira and "Nagata [5, II, p. 283]"; Nagata's Theorem 4a,
    the reference the book's own note points at, is the theorem printed at
    pp. 283--284 of the paper. Also checked: Nagata's "Cremona transformation
    with centers within P_i" is by his Section 2(2) a product of
    F-admissible quadratic transformations, which is the class of sequences
    Hartshorne's definition quantifies over, so "general position" and
    "non-special with respect to Cremona transformations" are the same
    condition on ordinary configurations with no three collinear. Not checked:
    the printed pages of Nagata's Lemma 2.1, cited on the card for the formula
    relating the degree, the multiplicities and the invariants, since the text
    version fixes only the ten-page block.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report of this day on the transcription, repaired on the card.
    (i) Part (a) is not open: both directions are printed. The "only if"
    direction is Yang Pi-Yeh's 5.4.15(a), printed p. 112, a conic
    axy + byz + czx = 0 through the six points going to the line
    bx + cy + az = 0 through the images of P_4, P_5, P_6 under the quadratic
    transformation; the "if" direction is Hartshorne's own verification in the
    proof of Proposition 4.10, Case 2, printed pp. 403--404, that no three of
    Q_1, Q_2, Q_3, P_4', P_5', P_6' are collinear and no six lie on a conic,
    which is general position by induction over the sequence of admissible
    transformations. The step on (a) is now that proof, and the event above
    that named (a) open is corrected in place.
    (ii) Part (b): the argument transcribed was not Nagata's Section 2(2). It
    is Yang's 5.4.15(b), printed p. 112, and the step now names him; Section
    2(2) supplies only the identification of admissible sequences with products
    of F-admissible quadratic transformations, which is the second half of the
    same step.
    (iii) The virtual genus was missing its factor 1/2: Nagata Section 2(3),
    printed p. 277, prints (d^2 - 3d + 2 - sum m_i(m_i - 1))/2. Lemma 2.1(iii),
    also p. 277, is the identity 3d - sum m_i = I - 2vg + 2 and does not
    characterise curves of the first kind, which is what the card cited it for;
    that characterisation is Proposition 2, printed p. 277, and each is now
    cited for its own statement.
    (iv) Nagata's Proposition 3, printed p. 279, prints the criterion for a
    special configuration with a type similar to (1,1,1,1,0,...,0) "with r - 3
    zeros", the class of a line through three of the points, and a nonempty
    L^oplus; the card had written (1,1,1,0,...,0), a class of the wrong size.
    Since (a) is now proved from the two sources in (i), the criterion is named
    in the remark and is no longer offered as the route to (a).
    (v) Nagata's Lemma 2.5, printed p. 279, does not say that the bad locus is
    a proper closed subset. Its proof takes a quadratic transformation with
    centres at three generic points and observes that its corresponding base
    points and the remaining points are again independent generic over the prime
    field; that is a statement about a fully generic configuration, and the
    special locus is a countable union of closed conditions, not one of them.
    The step on part (c) now says exactly that and stops there.
    (vi) Dolgachev's Proposition 8.2.15: statement, list, table and proof are
    all on printed p. 261, not pp. 261--262. The printed list for N = 8 is short
    by the eight vectors -2 k_8 - e_i, each of square -1 with k_8 . v = -1,
    which are Nagata's row (6;3,2,...,2) on printed p. 284, so Nagata's table
    and Dolgachev's list are not the same list. The conic family is printed
    summed to e_7 in the N = 7 row and again in the N = 8 row, and the card's
    sum to e_N made it a class of square -2 there. The converse of the count now
    cites Lemma 2.4, printed p. 279, with the descent by the operator q in
    Nagata's proof of Theorem 2a, printed pp. 280--281. The counts 56 and 240
    stand, from Dolgachev's table on p. 261 and Nagata's table on p. 284, whose
    seven rows count 8 + 28 + 56 + 56 + 56 + 28 + 8.
    (vii) The remark's provenance --- the tmp/sources paths, the twenty- and
    ten-page block markers, and the sentence on the PDF folios --- is removed
    from the rendered page and recorded here. Nagata's printed pages were read
    at the PDF's folios on this pass, PDF 1 being printed 271: Proposition 2 and
    Lemma 2.1 at p. 277, Lemma 2.2 at p. 278, Lemma 2.4, Lemma 2.5 and
    Proposition 3 at p. 279, Lemma 2.8 and the statement of Theorem 2a at p. 280,
    the proof of Theorem 2a on p. 281, Theorem 3a at p. 282, and the table of
    Theorem 4a at p. 284, whose last row reads (6;3,2,2,2,2,2,2,2).
    Dolgachev's Proposition 8.2.15 was read in
    tmp/sources/dolgachev-topics-classical-ag.md from line 9857, and its printed
    page 261 is taken from the folio of the PDF and was not re-checked on this
    pass. Read for this pass: Hartshorne printed pp. 403--406, Yang pp. 111--112,
    Nagata pp. 276--284 and 291--293, Dolgachev pp. 261--264. Not read: Nagata's
    Part I, cited inside his proof of Theorem 2a for the inequality
    m_1 + m_2 + m_3 > d, and no search outside the brief's sources was made for
    part (c), which stays open.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report of this day, repaired here. (i) Three events of this day
    --- the source-corrected, the solution-written and the source-checked ones
    above --- had been rewritten in place by 38d4d33bee, which a dated record
    does not allow; they are restored to the text they were introduced with, and
    what that commit changed is recorded in the event it appended, which stands.
    (ii) The first of the orchestrator's decisions for this repair was not
    applied to part (c): the card's own proof of it, in the steps
    uncountable-field-lemma, bad-locus-proper-closed and
    dense-general-position-extension of 83d33296ae, had been dropped when the
    solution was turned into a transcription. It is restored, and the steps say
    that it is the card's own; the second of them asserts the properness of the
    bad locus and does not derive it, and (c) is open on that assertion. No
    source listed for the card proves (c), so nothing is transcribed for it.
    (iii) Nagata's table for r = 8, printed p. 284, has first row
    (0;-1,0,...,0), the class L(0;-P_1) of an exceptional curve, as the proof of
    Theorem 2a uses; the card had written (0;1,0,...,0), which is not
    pre-exceptional. The row is now printed with its negative multiplicity and
    named.
    (iv) The converse, that every solution of the two equations is
    pre-exceptional, is not in Nagata's printed proof of Theorem 2a, which treats
    only the class of an irreducible exceptional curve with non-negative
    multiplicities and positive degree. It is Dolgachev's Proposition 8.2.15,
    printed p. 261, whose statement is that an exceptional vector is exactly one
    with k_N . v = -1 and v^2 = -1, with his Noether-inequality sketch, and the
    card now cites that; joining his W(E_N)-orbit to Nagata's similarity classes
    through Lemma 2.4 also needs W(E_N) to be generated by the permutations and
    the reflection r_{alpha_123}, which no source read here prints, and the card
    does not carry that passage.
    (v) The description of Dolgachev's printed list for N = 8 contradicted
    itself: the conic family is printed summed to e_7, read literally the last
    family is not a family of exceptional vectors, and "short by the eight
    classes -2k_8-e_i" is not what reading the list literally gives. The card now
    prints the list as printed, says that it is not a list of exceptional vectors
    read literally, and takes the count from the two tables, the only claim it
    needs.
    (vi) The rendered remark said what Nagata's paper "contributes to this
    exercise" and that the card "uses its table and not its list"; both are
    bookkeeping and are removed, the mathematical statements kept. Read for this
    pass: Nagata, On rational surfaces II, printed pp. 276--284 and 291--293, and
    Dolgachev, Topics in Classical Algebraic Geometry, printed pp. 261--264, in
    tmp/sources/nagata-1960-rational-surfaces-ii.md (markers in ten-page blocks)
    and tmp/sources/dolgachev-topics-classical-ag.md (markers in twenty-page
    blocks, Proposition 8.2.15 from line 9857). Not read: Nagata's Part I, and no
    search was made outside these sources for part (c).
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report of this day on the count step, repaired here. (i) The step
    said that no source read for this card prints that W(E_N) is generated by the
    permutations together with r_{alpha_123}, and that the passage from
    Dolgachev's W(E_N)-orbit to Nagata's similarity classes is therefore not
    carried out. That is false of Dolgachev's Topics, a source of this card:
    Theorem 8.2.11, printed p. 258 (PDF 268), defines W(E_N) as the subgroup of
    O(E_N) generated by the reflections in a canonical root basis, the canonical
    basis (8.5), printed p. 257 (PDF 267), is beta_1 = alpha_123 and
    beta_i = alpha_{i-1,i}, and the sentence after Definition 7.5, printed p. 235
    (PDF 245), says that the reflections r_{alpha_i}, i not 0, act as S_N on
    e_1, ..., e_N. With Nagata's Lemma 2.4, printed p. 279, that gives that the
    similarity classes are the W(E_N)-orbits, and the step now carries the
    passage, in which r_{alpha_123} applied to d e_0 - sum m_i e_i is Nagata's
    operator q. Corollary 8.2.12, printed p. 259, and Proposition 8.2.14, printed
    p. 259, were read but are not cited on the card, which needs only the
    definition of W(E_N) with the basis (8.5) and the action of the simple
    reflections. (ii) The definition of pre-exceptional type is printed on p. 280
    of Nagata as "Elements of E(1, 1, 1, 0, ..., 0) (with r - 2 zeros)", an
    r-tuple with r + 1 entries, read as an image rendered at 200 dpi from
    tmp/sources/nagata-1960-rational-surfaces-ii.pdf, PDF 10, whose folio is 280,
    and Proposition 3 on printed p. 279, read the same way, carries the same extra
    1 in "(1, 1, 1, 1, 0, ..., 0) (with r - 3 zeros)". The class the notion needs,
    and the one the proof of Theorem 2a carries by q to L(0; -P_1), is the class
    of a line through two of the points, (1, 1, 0, ..., 0) with r - 2 zeros; the
    solution's bullet now states that class and names what the paper prints, and
    the two equations d^2 - sum m_i^2 = -1 and 3d - sum m_i = 1 of the step hold
    for it, which the printed representative does not satisfy. Read for this
    pass: Dolgachev's Definition 8.6, Theorem 8.2.11, Corollary 8.2.12,
    Proposition 8.2.14, the sentence after Definition 7.5 and Proposition 8.2.15
    with its proof and its table, at those printed pages in
    tmp/sources/dolgachev-topics-classical-ag.md, whose markers are twenty-page
    blocks so that the printed page is the folio, taken here from PDF 245, 257,
    258, 259 and 271; and Nagata's Section 2 with Lemmas 2.1, 2.4, 2.5 and 2.8,
    Theorem 2a with its proof, and the table of Theorem 4a, printed pp. 279--284,
    in tmp/sources/nagata-1960-rational-surfaces-ii.md, whose markers are ten-page
    blocks and whose printed page is the folio less 270. Not read here: Nagata's
    Part I, cited inside his own proof of Theorem 2a; Dolgachev's Chapter 7
    outside the sentence after Definition 7.5, and his Chapter 9; and the pages
    of Dolgachev and Duncan. Nothing was searched for part (c), which stays open
    on the assertion that step bad-locus-proper-closed makes and does not derive.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report of this day on the event above, repaired here. Item (ii) of
    that event said that Nagata's printed pre-exceptional type, (1, 1, 1, 0, ...,
    0) "with r - 2 zeros" on printed p. 280, is an r-tuple with r + 1 entries and
    that the solution's bullet must therefore be the class of a line through two
    of the points, (1, 1, 0, ..., 0) with r - 2 zeros; the bullet and the step
    were changed so, and the printed form was named a misprint. That is wrong
    twice over. A numerical type is (d, m_1, ..., m_r), which has r + 1 entries,
    so three 1s followed by r - 2 zeros are exactly d = 1, m_1 = m_2 = 1 and
    m_3 = ... = m_r = 0, the class of a line through two of the points, and it
    satisfies d^2 - sum m_i^2 = -1 and 3d - sum m_i = 1; and the replacement
    (1, 1, 0, ..., 0) with r - 2 zeros has r entries and is not a type with r base
    points at all. The same count disposes of Proposition 3's (1, 1, 1, 1, ...,
    0) "with r - 3 zeros" on printed p. 279, which is d = 1 with three points and
    also r + 1 entries: neither place misprints anything, and there is no defect
    of the source to name here. The bullet again prints the representative as the
    paper does and unpacks it as d = 1, m_1 = m_2 = 1, m_3 = ... = m_r = 0, and
    the step's sentence on the degree-1 family says the same. What stands from the
    event above is the passage through Theorem 8.2.11, the basis (8.5), the
    sentence after Definition 7.5 and Lemma 2.4, and the computation of
    r_{alpha_123} as Nagata's operator q. The 200 dpi render of printed pp. 279 and
    280 that event records is a reading of the page and was not at fault; the
    conclusion drawn from it was. Nothing further was read for this event, the
    pages it rests on being those of the event above.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Issue #157, acceptance item 2: the rendered solution no longer claims a
    proof it does not give. The head of the solution said part (c) "is proved
    on the card" and then that "the proof rests on an assertion it does not
    derive", and the qed remark said the three steps "prove (c), which is as
    strong as the properness" that the step on the bad locus asserts and does
    not derive. Both now say part (c) is not proved on this card and that its
    steps carry it only on that properness; the head also states what the bad
    locus is. No step, reference, statement or source claim changes, and no
    earlier event is touched. Not done: the proof of that properness, which is
    acceptance item 1 and stays open, and the check of any step of the card.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Issue #157, acceptance item 1, partial: a new step properness-reduction
    writes out what the card previously only named. It records that the last
    quadratic transformation contributes a finite union of branches, the
    branches other than the conic being collinearities at the previous stage;
    that the conic branch is contained in the effectivity locus of the class
    Gamma = s_{w'}(2e_0-e_a-e_b-e_c-e_X-e_Y-e_Z), which has square -2 and
    K-degree 0; that the case m_N = 0 is empty, by Nagata's Proposition 3,
    printed p. 279; and that for m_N = 1 the locus is the whole plane exactly
    when the fixed system L(d;sum m_iP_i) is superabundant, by Riemann-Roch
    plus the fact that a positive-dimensional linear system covers the plane.
    Step part-c-open now names the two cases that remain, m_N >= 2 and m_N = 1
    with superabundance, and the printed range in which the second is settled
    (Proposition 8 of Nagata, printed p. 293, for r = 8, d >= m_1+m_2+m_3,
    m_i >= 0), with the reduction to that range not carried out. The qed now
    says which step derives what. Part (c) is still not proved on this card
    and no step claims otherwise. Read for this event: the printed pages cited,
    already read for the earlier events; nothing was re-read and no other step
    changed.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #157: the solution sets retained for Hartshorne were read for part (c)
    of V.4.15, printed p. 409, under the owner's rule that such a proof is a
    transcription of a published solution set, cited by set and page, not a
    re-derivation. Read in tmp/sources, with their coverage: Borcherds (Chapter
    I), Troiani (Chapter I), Cais (Chapter IV), Sam (Chapters III--IV), Lomont
    (Chapter IV), Park (Chapter IV and V.5, but his "5.4" is III.5 Exercise 4),
    Stein (Chapter III.7), Saglam--Chris (Chapter III), Kim (Chapters I--III),
    Cutrone--Marshburn (Chapter IV) and Okamoto (II.9). None of these reaches
    V.4.15. Two sets print it. Egbert, printed p. 295, keeps only what is
    printed: general position as the complement of the vanishing of
    determinants on (P^2)^r, with no proof that the complement is nonempty and
    no statement about the fibre over a fixed tuple, so it does not prove (c)
    as the book asks it. Yang Pi-Yeh, Solution 5.4.15(c), printed p. 112, takes
    V to be the complement of the lines P_iP_j and the conics through five of
    the points and concludes "by (a)", but (a) is the six-point criterion and
    does not give general position for r+1 > 6, so it does not prove (c)
    either. No set therefore proves part (c). Following the same rule, the step
    properness-reduction added in 7334bcf5fe on this date is removed from the
    solution: no set's proof uses it, and its content is recorded here so that
    it is not lost -- the last transformation contributes a finite union of
    branches, the conic branch being contained in the effectivity locus of
    s_{w'}(2e_0-e_a-e_b-e_c-e_X-e_Y-e_Z), of square -2 and K-degree 0, which is
    empty when the multiplicity m_N at the moving point is 0 (Nagata
    Proposition 3, printed p. 279) and, for m_N = 1, is the whole plane exactly
    when the fixed system L(d;sum m_i P_i) is superabundant; m_N >= 2 was left
    open there. Part (c) is not proved on this card and no step claims it is.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165: one rendered sentence contradicted the rest of the card. The
    last sentence of step dense-general-position-extension read "This is
    exactly the definition of general position, proving (c)", while the head of
    the solution, step bad-locus-proper-closed and the qed all say that (c) is
    not proved on this card, its three steps carrying it only on the properness
    of the bad locus, which step bad-locus-proper-closed asserts and does not
    derive. The sentence now says what the step proves: every point of V
    satisfies (c) given that properness, and without it V can be empty and (c)
    is not proved. No step, reference, statement or source claim changes, and
    the events of 2026-11-19 that made the head, the qed and step part-c-open
    say (c) is open stand. Checked in this pass: the printed exercise,
    Hartshorne V.4.15 on printed p. 409 (PDF p. 424), and the three part-(c)
    steps against it; and Nagata, Proposition 12 on printed p. 293 with
    Theorem 4a on printed pp. 283--284, read at those folios of
    tmp/sources/nagata-1960-rational-surfaces-ii.pdf, which the parts (d) and
    (e) steps cite. Not done: the proof of that properness, which is the open
    item of issue #157 and is not claimed here.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165, reader's report on the card: the two part-(c) step statements
    are corrected to what their proofs give, the remark at five places, and the
    earlier notes this supersedes are named. (1) Step
    dense-general-position-extension stated part (c) itself while its proof was
    complete only given the properness of the bad locus; its statement now
    carries that hypothesis. (2) Step bad-locus-proper-closed said the bad set
    "is contained in a proper closed subset of PP^2", while its proof carries
    out the closedness only and says properness is asserted and not derived;
    its statement now says that the set is closed and that it is proper
    whenever the determinant is not identically zero, which is the asserted and
    unproved point. With those two, the density proof's sentence that the
    preceding step "produces only countably many proper closed bad subsets"
    now reads that it produces countably many closed bad subsets, proper by the
    hypothesis; the head, step part-c-open and the qed are unchanged. (3) The
    remark said that Nagata's Section 2(c) is "the identification of general
    position with non-speciality"; the paper defines non-speciality only, and
    the identification is step general-position-is-non-special. It called
    Nagata's Corollary to Proposition 9 "the eight-point criterion" (it is a
    criterion for special points with no number of points), described Lemma
    2.5 as "the generic-point statement that (c) is a spreading-out of but is
    not" (an ungrammatical clause; Lemma 2.5 is the generic-point statement,
    not a statement about the fibre over a fixed tuple), gave Egbert's r=8
    list as "seven ... whose counts make 240" where his seventh row is "the
    rest" and the 56 is the card's, and gave Yang's (a) as "in both
    directions" where his "if" direction treats only a line through the images
    of P_4, P_5, P_6. Each of the five now says what the source prints. (4)
    The event of this date above whose note reads "No step, reference,
    statement or source claim changes" is corrected here: it was true of the
    commit it records and not of this one. (5) Earlier notes the card no
    longer holds, named with their text: the 2026-11-16 event saying "What it
    does not prove ... part (a) beyond its printed criterion, and part (c) in
    full" is superseded for part (a) by step general-position-six-points,
    whose two directions are Yang's and Hartshorne's and which the head counts
    as proved; the event saying "Step part-c-open now names the two cases that
    remain ... Proposition 8 of Nagata, printed p. 293" describes a step
    removed the same day and gives the wrong page, Proposition 8 being printed
    on p. 289; the event saying "Park (Chapter IV and V.5 ...)" is wrong about
    V.5, Park's 5.x being Appendix C, and the rendered card says Park stops at
    Chapter IV; the event saying Egbert has "(d) as a list of eight families"
    and "(e) as a citation of Nagata" is wrong on both counts, as the remark
    now says; the event saying the pages "423 and 424 are PDF pages" gives
    V.4.10's page with V.4.15's, which is printed p. 409 = PDF p. 424 alone;
    and the event reviewing the steps six-points-general-position-iff,
    six-point-condition-preserved, degree-bound-nonneg-square,
    r7-classes-fifty-six, r8-classes-two-forty,
    negative-curve-is-minus-one-curve and r7-classes-realized-unique names
    labels the card does not have. Checked in this pass: the printed exercise
    on p. 409 (PDF 424); Nagata's Section 2(c) and Lemma 2.2 at printed
    pp. 278--279, Proposition 3 and Lemma 2.5 at p. 279, Theorem 2a at
    pp. 280--281, Theorem 4a at pp. 283--284 and Proposition 12 at p. 293, at
    those folios of the PDF; Egbert's V.4.15 entry at PDF pp. 294--296; and
    Yang's 5.4.15 in the text version at lines 2818--2834. Not checked: the
    proof of the properness of the bad locus, which stays open under issue
    #157, and no source outside those already on the card was searched for
    part (c).
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165, the item the last report left open: a search outside the
    retained sets for a published proof of part (c) of V.4.15, printed p. 409.
    Searched were Ceramic for the exercise's own wording and for "general
    position" with Cremona and quadratic transformations, and Linkup for the
    exercise by number and parts; the hits were the Egbert set already held in
    tmp/sources (its V.4.15 entry is the one read at PDF pp. 294--296, which
    proves (a) by the m(m+3)/2 count and lists (d) without proving (c)),
    a dokumen.pub page titled "Algebraic Geometry by Robin Hartshorne Full
    Solutions" which returns HTTP 502 and so was not read, two Scribd
    compilations whose text is not served to a reader, and the published book.
    No complete published proof of (c) was located, so part (c) stays open on
    the properness of the bad locus exactly as the head, step
    bad-locus-proper-closed, step part-c-open and the qed say, and nothing on
    the card changes. Not done: the Scribd compilations and the dokumen.pub
    page were not read, and no library or print source was consulted.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165, the item the last report left open: the proof of step
    bad-locus-proper-closed now proves the properness in the case where no
    centre triple of the word contains the label of P. There the word acts on
    the fixed configuration by part (b), so the terminal positions of
    P_1,...,P_r have no three collinear, and the terminal position of P is
    T(P) for the composite T of the word's quadratic transformations, a
    birational map of the plane; a terminal triple not containing P gives a
    condition independent of P, which is empty, and one containing P gives
    T(P) in L for the line through the other two terminal points, whose
    preimage is a proper closed subset because T is dominant and L is proper.
    The case where some centre triple contains P stays open and the proof says
    so; no claim of the step changes, and the head, step part-c-open and the
    qed still say (c) is not proved on this card. Read for this event: the
    exercise on printed p. 409, and part (b) as step
    general-position-preserved-under-sequence proves it. Not checked: the case
    with P among the centres, for which no published proof was located; the
    search is recorded in the event above.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165, the remaining case, taken as authorised by the instruction to
    write the mathematics: the proof of step bad-locus-proper-closed now also
    proves the properness when P occurs as a centre only in the last step. The
    last step is centred at Q, X, Y with Q the image of P and X, Y images of
    fixed labels; part (b) makes the configuration before it (C_0, Q) with C_0
    in general position, and Q is a birational function of P. In adapted
    coordinates the images of the three centres are the three coordinate
    points and the image of a point a is (y_a z_a : z_a x_a : x_a y_a), so a
    terminal triple gives one of: a line in Q (Q with two points of C_0); the
    condition x_a y_a = 0, that is a in XY, which is false because a, X, Y are
    three points of the general-position configuration C_0, or a in QY, a line
    in Q; the condition y_a z_a = 0, the same two alternatives with QX; or the
    conic through five points of C_0, which is a conic in Q. Each is a proper
    closed condition in Q, hence in P. What stays open, and the proof says so,
    is a word that uses P as a centre and then continues past that step, whose
    later centres are functions of P. No claim of the step changes and (c) is
    still not claimed as proved on this card.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Part (c) proved for r <= 7, so the sentence above is superseded for those
    r. Read for this event: Dolgachev, Topics in Classical Algebraic Geometry,
    §8.1, the definition of points in general position (i)-(iv) and
    Proposition 8.1.9, both printed p. 251 (PDF p. 261, folio read on the
    page), that the blowup of N <= 8 points is a Del Pezzo surface exactly when
    the points are in general position; and Hartshorne V.4.15, printed p. 409.
    Recomputed: the bookkeeping of a quadratic transformation on classes,
    h -> 2h - c_1 - c_2 - c_3 and c_j -> h - c_k - c_l, an integral isometry
    fixing K = -3h + sum c_i, so that for a word w and a terminal triple
    {a,b,c} the class D = h_w - c_a - c_b - c_c has square -2, K-degree 0 and
    D.h_w = 1, independently of P; that the terminal triple is collinear
    exactly when the linear system of D is nonempty, a member of it meeting
    each of c_a, c_b, c_c in 1 and so having none as a component; and that on a
    Del Pezzo surface every nonzero effective class has negative K-degree,
    which kills D. The closed sets to exclude are the lines through pairs of
    the fixed points, the conics through its fives, and the locus where a cubic
    through the r+1 points is singular at a fixed one of them, a square system
    whose determinant is not identically zero; the Del Pezzo locus is their
    nonempty complement. Not checked: Nagata's paper beyond the statements the
    card quotes; r >= 8, where -K is not ample and the question stays open; and
    the printed books themselves, only the retained copies.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    New step properness-r-at-most-seven, with the head, the bad-locus step, the
    density step, the qed and the part-c-open step qualified to say (c) is
    proved for r <= 7 and open for r >= 8. No other step changes: (a), (b),
    (d) and (e) and the numbers 56 and 240 are untouched.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A reading in the step above corrected. Dolgachev's general-position
    definition on printed p. 251 lists four conditions, and the step first cited
    all four for every N <= 8; but at N <= 7 the fourth is automatic: a cubic
    singular at one of the N points and through the other N-1 meets 3 + (N-1)
    conditions on the 10 coefficients of a cubic, so one exists for every
    position of the points, and a condition that always holds cannot be part of
    a criterion that fails. The criterion at N <= 7 is therefore (i)-(iii), no
    three collinear and no six on a conic, which is the standard statement; the
    printed (iv) bites only at N = 8, where the count is square (8 + 2 = 10),
    and that is the case the step now excludes. Read for this event: Dolgachev
    printed p. 251 (PDF p. 261) again, both the definition and the sufficiency
    argument of Proposition 8.1.9, which removes the last point and checks that
    it lies on no (-2)-curve, the lines through three and the conics through
    five of the remaining ones being what conditions (ii) and (iii) exclude
    there. Not checked: whether the book states the N <= 7 reading in so many
    words elsewhere, and the printed volume itself.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Issue #180 (kernel of #157). Part (c) is now proved on this card for
    r <= 8 in every characteristic and for r = 9 when k has characteristic 0
    or the nine points lie on a cubic that is not cuspidal; it stays open for
    r >= 10 and for r = 9 with a unique, cuspidal cubic in characteristic p.
    New steps: subset-general-position, bad-locus-root-class,
    bad-locus-closed, no-minus-two-curve, no-effective-root, smooth-cubic,
    properness-r-at-most-eight, properness-r-nine and
    effective-root-for-every-point. The seven steps from bad-locus-root-class
    to properness-r-at-most-eight are the proof of commit c0ac5252ae, which
    was written for this issue on 2026-11-19 and never reached main; they are
    carried over with their citations given by numbered statement, and the
    statements of Demazure, Lang, Bombieri--Mumford and Milne that they cite
    were read by that commit's author and not again for this event. Step
    properness-r-nine is new: for P on the cubic through the nine points the
    strict transform of the cubic is an anticanonical curve of square -1 on
    the blow-up, an effective root must then contain a (-2)-curve disjoint
    from it, and such a curve either lies on the nine-point blow-up, which
    step no-minus-two-curve excludes, or gives a relation nP ~ M on the cubic
    with n >= 1, which finitely many P satisfy. Step
    effective-root-for-every-point is new: for fifteen independent points of a
    nonsingular cubic, which are in general position, the root
    9h - 5e_1 - 3e_2 - e_3 - ... - e_15 - 6e is the cubic plus four times the
    line P P_1 plus twice the line P P_2 and is effective for every P; so the
    statement "no root is effective for some P", which carries r <= 9, is
    false from r = 15 on, and step part-c-open now states the remaining
    statement for the bad set itself. The head, the statement and last
    sentences of step bad-locus-proper-closed, step
    dense-general-position-extension, step part-c-open and the qed are
    reworded to these ranges; the density step now assumes that each bad set
    lies in a proper closed subset, which is what the properness steps prove.
    Read for this event in Hartshorne, by numbered statement: Exercise V.4.15,
    Example V.4.2.3, Exercise V.4.2, Propositions V.1.4, V.3.2, V.3.3 and
    V.3.6, Theorem V.1.9, Exercise V.1.3, Theorem III.12.8, Example IV.1.3.7,
    Exercises II.6.7 and II.6.9 and Example II.6.11.4, each located by its
    number in tmp/sources/hartshorne-1977-algebraic-geometry.md; the statements
    of Propositions V.1.4, V.3.3 and V.3.6, Exercises V.4.2 and II.6.7 and
    Examples IV.1.3.7 and II.6.11.4 were read there, the others identified by
    their headings. Recomputed: the two intersection numbers of the fifteen-point
    root, and the inequality -2 - a^2 >= -2 sum c_j^2 - a^2 of step
    properness-r-nine. Not checked: the cuspidal case in characteristic p,
    and r >= 10, for which no proof and no published statement was found.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Issue #180, a second round on this date, after a reader's report on the
    event above. (1) Step no-minus-two-curve is stated for n points and its
    descent used a third centre without showing that one exists; its proof now
    shows m_i <= d from the pencil of lines through R_i, hence n >= 3 and
    m_3 >= 1, and writes out the repetition on the new configuration. (2) Step
    bad-locus-proper-closed claimed a closed subset of P^2 while its proof
    worked on the open set where the word is defined; the statement now names
    that set W_w, the proof shows by induction on the word that W_w is open in
    U and that the terminal configuration is locally a morphism on it, and the
    bad set B(w,T) is closed in W_w, so locally closed in P^2. (3) New step
    effective-line-class-is-not-general: for P in U the r+1 points are in
    general position exactly when no class alpha_{w,T}, the class
    h' - e'_a - e'_b - e'_c of a terminal basis written in the original one, is
    effective on Y_P; the converse direction is new, and it makes part (c) for
    P_1,...,P_r equivalent to Z_alpha != U for these classes. (4) New step
    properness-on-a-cubic: part (c) for every r >= 9 when the points lie on a
    cubic that is not cuspidal, or in characteristic 0. It uses the irreducible
    terminal line L: L is not the anticanonical curve E' through P, so
    0 <= L.E' = 3 - |S|, the line carries exactly three points, is disjoint
    from E', and gives the relation nP ~ M on the cubic with n >= 1. (5) New
    step cuspidal-cubic-every-point-fails: in characteristic 5, the points
    P(t_i) of y^2 z = x^3 with t_1,...,t_8 independent over F_5 and
    t_9 = t_1 - t_2 - ... - t_8 are in general position, and for every tenth
    point P of the cubic the class 8h - 3e_1 - 2(e_2+...+e_9) - 5e restricts
    trivially to the cubic, is effective, and gives a (-2)-curve; so the
    cuspidal case cannot be decided with P on the cubic. (6) Step
    effective-root-for-every-point: by (4), part (c) holds for its points and
    its root is none of the classes alpha_{w,T}. Step part-c-open had drawn
    from that root that the remaining statement does not concern the
    effectivity of a root; that sentence is replaced by the equivalence of (3).
    The head, the density step, step part-c-open and the qed are reworded to
    the new ranges. Read for this event: Hartshorne, Example II.6.11.4 with its
    proof, and Theorem V.1.6, Corollary III.7.7, Proposition V.1.4 and Exercise
    V.1.3 at their statements, in the text version of the book; Cantat and
    Dolgachev, Rational surfaces with a large group of automorphisms,
    arXiv:1106.0930, Sections 1.3 to 1.5, Section 3.3 with its lemma on
    effective divisors, Proposition 4.5 and Section 6.1 with its two lemmas on
    effective roots; Totaro, Hilbert's fourteenth problem over finite fields,
    arXiv:0808.0695, Section 2 and Corollary 3.2; Dolgachev, Topics in
    Classical Algebraic Geometry, Sections 8.2.7 and 8.2.8, on effective roots
    and Cremona isometries of weak Del Pezzo surfaces, with a search of the
    text version of the whole book for "unnodal", "nodal root" and "Cremona
    general". None of them states part (c) for a fixed configuration. Recomputed: the two intersection numbers of the
    class in (5) and its restriction to the cubic, and the sums
    sum nu_i = 3 d_0 and sum nu_i^2 = d_0^2 + 2 of that step. Not proved, and
    no published statement found: part (c) for r >= 10 points on no cubic, and
    for points whose one cubic is cuspidal in characteristic p. Not read:
    Harbourne, Blowings-up of P^2 and their blowings-down, of which no copy
    was found, and Dolgachev and Ortland, Point sets in projective spaces and
    theta functions, beyond its introduction.

- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Issue #165, on this card: the head called the whole solution a transcription and
    said that it proves (c) for r <= 7, while step bad-locus-proper-closed and step
    part-c-open say that the proof of (c) is the card's own, and step
    properness-r-at-most-seven reached r = 7 only through the general-position
    criterion for eight points, where the printed condition on cubics is a square
    system whose determinant the step called nonzero because the system is square.
    Squareness does not give a nonzero determinant. The second proof is therefore
    restricted to r <= 6, where the criterion is the one printed in Dolgachev,
    Section 6.3.3: condition (*), no three collinear and no six on a conic, which the
    fixed tuple satisfies and whose two excluded loci are proper. At N <= 7 the
    printed fourth condition, that no cubic pass through the points with one of them
    singular, holds for no configuration at all, since a cubic singular at one of N
    points and through the other N - 1 meets 3 + (N - 1) <= 9 conditions on the ten
    coefficients and so exists for every position; the step now says that instead of
    calling the condition automatic. Part (c) for r <= 8, r = 7 included, is step
    properness-r-at-most-eight. The head now names the transcribed parts, (a), (b),
    (d) and (e), with their sources, and says that the proof of (c) is the card's
    own. The marker in step uncountable-field-lemma read "this step and the two after
    it are the card's own" and said that no source prints the statement of (c); the
    card's step part-c-open names two sets that print an argument for (c) and proves
    neither, so the marker now scopes the card's own work to the steps that carry
    (c) and states that no source proves it. This supersedes the 2026-11-19 event whose note reads "Part (c) proved for
    r <= 7, so the sentence above is superseded for those r": the second proof
    covers r <= 6, and (c) for r <= 8 rests on properness-r-at-most-eight. Read in
    this pass: Dolgachev, Topics in Classical Algebraic Geometry, the definition of
    points in general position preceding Proposition 8.1.9, Proposition 8.1.9, and
    Section 6.3.3 with condition (*); Hartshorne, Exercise V.4.15. Recomputed: the
    count 3 + (N - 1) at N <= 7, and the square case 10 = 10 at N = 8. Not done: no
    proof that the determinant is nonzero was found or written, and the step no
    longer uses one.

- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Issue #165, the same day, closing what the event above left restricted: the head
    and step properness-r-at-most-seven are restored to r <= 7, because the
    properness of the fourth general-position condition at eight points is now
    proved on the card instead of inferred from the squareness of a system. Fix
    $P_1,\ldots,P_7$ in general position and a nonsingular cubic $E_0$ through them,
    which step smooth-cubic supplies. The bad locus $B$, of points $P$ for which a
    cubic through $P_1,\ldots,P_7,P$ is singular at one of the eight, is closed,
    being a projection from $\PP^2\times\PP^9$. A cubic $C\ne E_0$ of that kind
    meets $E_0$ in a divisor of degree $9$ containing the singular point twice and
    the other seven points once, hence in exactly $2Q+\sum_{R\ne Q}R$; for $Q=P$
    the class of $2P$ is fixed and has at most four square roots, by Example
    IV.1.3.7 with Milne, *Abelian Varieties*, Theorem I.7.2, and for $Q=P_j$ the
    point $P$ is the single point of a fixed class of degree one; a cubic singular
    at two of the eight points would meet $E_0$ in degree at least $10$. So $B$ is
    a proper closed subset of $\PP^2$. Read in this pass: Dolgachev, the definition
    preceding Proposition 8.1.9, Proposition 8.1.9, and Section 6.3.3; Hartshorne,
    Example IV.1.3.7; Milne, Theorem I.7.2 as the card cites it. Recomputed: the two
    intersection divisors, $2P+\sum_{i\le7}P_i$ and $2P_j+\sum_{i\ne j,\,i\le7}P_i+P$,
    both of degree $9$, and the count $3+(N-1)$ at $N\le7$. Not done: no determinant
    was computed and none is used, and no case of step part-c-open is touched.

- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Issue #165, third item on this card, found by reading the step claims against
    their proofs: four claims said that part (c) holds for their range without the
    hypothesis of part (c), that the ground field is uncountable. What those proofs
    give in every characteristic is that the bad loci are contained in proper closed
    subsets; the passage from that to (c) is step dense-general-position-extension,
    whose statement assumes $k$ uncountable, and over a countable field its
    countable-union lemma is false. The claims of steps properness-r-at-most-seven,
    properness-r-at-most-eight, properness-r-nine and effective-root-for-every-point
    now carry "when $k$ is uncountable", and the head says the same of the range it
    lists. Read in this pass: the four claims, and the statements of steps
    dense-general-position-extension and part-c-open; Hartshorne, Exercise V.4.15(c),
    whose first sentence is that hypothesis. No proof changed.

- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Issue #165, the condition count withdrawn. On inspection the sentence "a cubic singular at
    one of $N$ points and through the other $N-1$ meets $3+(N-1)\le9$ conditions on the ten
    coefficients", and the two conclusions drawn from it — that the printed condition on cubics
    holds for no configuration below eight points, and that the printed list is read for the
    maximal case — are removed from step properness-r-at-most-seven. What replaces them is a
    numbered statement for each range: for $r+1\le6$ points Hartshorne, Theorem V.4.6 with
    Corollary V.4.7, that with no three of them collinear and no six on a conic the linear system
    of cubics through them is very ample and the blowup embeds with $\omega\cong\mathcal O(-1)$;
    for $r+1=7$ points Dolgachev, §6.3.3, the sentence after Proposition 6.3.5, condition (*);
    and for $r+1=8$ points Proposition 8.1.9, whose fourth condition the residuation argument on
    $E_0$ makes available. The residuation and $E_0$-intersection argument is kept only at
    $r+1=8$, where its proof applies, and the step's range $r\le7$ is unchanged. This withdraws,
    in the rendered text, the count-based clause of the 2026-11-19 event whose note reads "A
    reading in the step above corrected ... at N <= 7 the fourth is automatic", and the same
    clause of the 2026-11-22 event whose note reads "Issue #165, on this card: the head called
    the whole solution a transcription"; both dated events keep their text as QUAL-11 requires.
    Read in this pass: Hartshorne, Theorem V.4.6 and Corollary V.4.7; Dolgachev, the definition
    preceding Proposition 8.1.9, Proposition 8.1.9, and §6.3.3 with Proposition 6.3.5. Not done:
    no hypothesis on the characteristic of the field was added, and the two ranges step
    part-c-open names stay open.

- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Issue #165, two corrections to step properness-r-at-most-seven after reading its Dolgachev
    references again. (1) The Del Pezzo statement for seven points is the unnumbered sentence
    after Proposition 6.3.5 in §6.3.3, not Proposition 6.3.5 itself, which states the degree-2
    map and asserts no Del Pezzo property; the step now cites that sentence in both places. (2)
    Dolgachev fixes $\CC$ as the base field in Chapter 1, so the criteria in Proposition 8.1.9
    and in §6.3.3 give the Del Pezzo property over $\CC$ only, while Hartshorne's Theorem V.4.6
    with Corollary V.4.7 is stated over an algebraically closed field of any characteristic and
    the residuation argument on $E_0$ uses no field hypothesis. The step's claim is therefore
    stated for $k=\CC$, its proof says so before using the two Dolgachev criteria, and the head
    and step bad-locus-proper-closed name the second proof as one over $\CC$; the range $r\le7$
    is unchanged, and part (c) in every characteristic remains step
    properness-r-at-most-eight. Read in this pass: Dolgachev, Chapter 1 for the base field,
    §6.3.3 with Proposition 6.3.5 and the sentence after it, and Proposition 8.1.9; Hartshorne,
    Theorem V.4.6 with Corollary V.4.7 and Remark 4.7.1, where a Del Pezzo surface is a surface
    of degree $d$ in $\PP^d$ with $\omega=\mathcal O(-1)$. Not done: no characteristic-free
    statement for seven points was located, and none is claimed.

- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Issue #165, two items on this card. (1) The residuation sentence states why the intersection
    divisor is exactly $2Q+\sum_{R\ne Q}R$: for $P\in E_0$ the singular point $Q$ is one of the
    eight and lies on $E_0$, the divisor has degree $9$ and contains $Q$ at least twice and the
    other seven at least once, so both multiplicities are exactly what is written; a cubic
    singular at two of the eight, or with multiplicity three at one of them, would need degree at
    least $10$. (2) The 2026-11-19 event whose note reads "Part (c) proved for r <= 7, so the
    sentence above is superseded for those r" still records the closed sets as including "a
    square system whose determinant is not identically zero". That clause is withdrawn here: no
    determinant was computed, the step no longer uses one, and the properness of the cubic locus
    is the residuation argument. Both dated events keep their text as QUAL-11 requires. Read in
    this pass: the residuation paragraph and Hartshorne, Example IV.1.3.7. Not done: nothing on
    the two ranges step part-c-open names.

- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Issue #165, the last record of the condition count: the 2026-11-22 event whose note reads
    "Issue #165, the same day, closing what the event above left restricted" ends "Recomputed: ...
    and the count 3+(N-1) at N<=7". That recomputation is withdrawn with the sentence it
    supported: the rendered step contains no condition count and uses none, and the ranges it
    covers rest on Hartshorne, Theorem V.4.6 with Corollary V.4.7, on the sentence after
    Dolgachev, Proposition 6.3.5, and on Dolgachev, Proposition 8.1.9 with the fourth condition
    supplied by the residuation argument. The dated event keeps its text as QUAL-11 requires, and
    nothing on the card changes.

---

::: {.problem}
Let $P_1, \ldots, P_r$ be a finite set of (ordinary) points of $\PP^2$, no 3 collinear.
We define an **admissible transformation** to be a quadratic transformation (4.2.3) centered at some three of the $P_i$ (call them $P_1, P_2, P_3$).

This gives a new $\PP^2$, and a new set of $r$ points, namely $Q_1, Q_2, Q_3$, and the images of $P_4, \ldots, P_r$.

We say that $P_1, \ldots, P_r$ are **in general position** if no three are collinear, and furthermore after any finite sequence of admissible transformations, the new set of $r$ points also has no three collinear.

(a) A set of 6 points is in general position if and only if no three are collinear and not all six lie on a conic.

(b) If $P_1, \ldots, P_r$ are in general position, then the $r$ points obtained by any finite sequence of admissible transformations are also in general position.

(c) Assume the ground field $k$ is uncountable.
Then given $P_1, \ldots, P_r$ in general position, there is a dense subset $V \subseteq \PP^2$ such that for any $P_{r+1} \in V$, $P_1, \ldots, P_{r+1}$ will be in general position.

Hint: Prove a lemma that when $k$ is uncountable, a variety cannot be equal to the union of a countable family of proper closed subsets.

(d) Now take $P_1, \ldots, P_r \in \PP^2$ in general position, and let $X$ be the surface obtained by blowing up $P_1, \ldots, P_r$.
If $r=7$, show that $X$ has exactly 56 irreducible nonsingular curves $C$ with $g=0$, $C^2=-1$, and that these are the only irreducible curves with negative self-intersection.
Ditto for $r=8$, the number being 240.

(e) For $r=9$, show that the surface $X$ defined in (d) has infinitely many irreducible nonsingular curves $C$ with $g=0$ and $C^2=-1$.

Hint: Let $L$ be the line joining $P_1$ and $P_2$.
Show that there exist finite sequences of admissible transformations such that the strict transform of $L$ becomes a plane curve of arbitrarily high degree.
This example is apparently due to Kodaira -- see Nagata, *On rational surfaces, II*, Theorem 4a.
:::

::: {.solution}
Let $X=\operatorname{Bl}_{P_1,\ldots,P_r}\PP^2$ be the blowup, with $h$ the class of the pullback of a line and $e_i$ the exceptional classes, so that $K_X=-3h+\sum_ie_i$. For a class $C=dh-\sum_im_ie_i$ the intersection form gives $C^2=d^2-\sum_im_i^2$, and the virtual genus of the virtual linear system $\mathcal L(d;\sum_im_iP_i)$ is
$$
vg=\frac{d^2-3d+2-\sum_i m_i(m_i-1)}{2},
$$
a quantity of the numerical type alone (Nagata, Section 2(3) and Lemma 2.8). An irreducible curve of $X$ that is not one of the $e_i$ has, in Nagata's language, the class $\mathcal L(d;\sum_im_iP_i)$ with $m_i=m(P_i;C)$; Nagata's "grade" $I$ is the self-intersection and his "virtual genus" is the arithmetic genus (Section 1(3)).

The two conditions the exercise's parts (d) and (e) turn on are Nagata's:

- a virtual linear system $L$ is exceptional exactly when it is irreducible with $I(L)=-1$ and $vg(L)=0$, by Proposition 2; for an irreducible curve $C$ on $X$ its class is exceptional exactly when $C\cong\PP^1$ and $C^2=-1$, which is the definition of an irreducible curve of the first kind;
- a numerical type $(d,m_1,\ldots,m_r)$ is *pre-exceptional* when it is similar to $(1,1,1,0,\ldots,0)$ with $r-2$ zeros, which is the type of $r$ base points with $d=1$, $m_1=m_2=1$ and $m_3=\cdots=m_r=0$, the class of a line through two of the points, so that $I=-1$ and $vg=0$; and by Theorem 3a  a virtually connected system with $I=-1$ and $vg=0$ is of pre-exceptional type.

The steps below transcribe (a) from Yang Pi-Yeh, Solution 5.4.15(a), for the "only if" direction, and from the proof of Proposition V.4.10, Case 2, for the "if" direction; (b) from Yang, Solution 5.4.15; and (d) and (e) from Nagata, Theorems 2a and 4a, with the count from Dolgachev, Proposition 8.2.15. The proof of (c) is the card's own, and no source listed for the card proves part (c) for any $r$: it establishes part (c) for $r\le8$ in every characteristic, under the hypothesis of (c) that $k$ is uncountable, in step [](#properness-r-at-most-eight){.pf-ref}, with a second proof for $r\le7$ over $\CC$ in step [](#properness-r-at-most-seven){.pf-ref}, and for every $r\ge9$ in step [](#properness-on-a-cubic){.pf-ref} when the points lie on a cubic and either $k$ has characteristic $0$ or that cubic is not cuspidal. At $r=9$ the cubic hypothesis costs nothing, since nine points always lie on a cubic, and step [](#properness-r-nine){.pf-ref} is a second proof for that case. Part (c) is not proved here in two cases: $r\ge10$ points that lie on no cubic, and, in characteristic $p>0$, $r\ge9$ points that lie on exactly one cubic when that cubic is cuspidal. Step [](#effective-line-class-is-not-general){.pf-ref} turns part (c) into a statement about countably many divisor classes, and step [](#part-c-open){.pf-ref} states it for these two cases.

For part (c), fix $P_1,\ldots,P_r$ in general position, let $X_r$ be their blow-up, and let $U\subseteq\PP^2$ be the complement of the points $P_i$ and of the lines $P_iP_j$; $U$ is open and dense, and it is also an open subset of $X_r$. For $P\in U$ let $Y_P=\Bl_PX_r$, with $\Pic Y_P$ free on $h,e_1,\ldots,e_r,e$, where $e$ is the class of the exceptional curve over $P$, so that $K_{Y_P}=-3h+\sum_ie_i+e$ (Hartshorne, Propositions V.3.2 and V.3.3). A root is a class $\alpha$ with $\alpha^2=-2$ and $K\cdot\alpha=0$, and for a root $\alpha$ we put $Z_\alpha=\{P\in U:\alpha\text{ is the class of an effective divisor on }Y_P\}$.

::: pf

::: {.pf-step #general-position-is-non-special}
For ordinary points $P_1,\ldots,P_r$ of $\PP^2$ with no three collinear, being in general position is the same condition as being non-special with respect to Cremona transformations.

::: pf-proof
Nagata, Section 2(c), calls the points non-special when for every Cremona transformation $T$ with centres within the $P_i$ the corresponding base points to the $P_i$ under $T$ are ordinary points of $T(S)$ no three of which are collinear; the corresponding base points are the $r$ points of Lemma 2.2, which are exactly $r$ in number and satisfy $F=\operatorname{dil}_{(P_1',\ldots,P_r')}(T(S))$. By Section 2(2) of the paper a Cremona transformation with centres within the $P_i$ is by definition a product of $F$-admissible quadratic Cremona transformations, and $F$-admissible here means exactly that the centres are points of the configuration, so these are the finite sequences of admissible transformations of the exercise. The two definitions therefore quantify over the same sequences and require the same thing of the resulting configuration.
:::

:::

::: {.pf-step #general-position-preserved-under-sequence}
General position is preserved by every finite sequence of admissible transformations, which is part (b).

::: pf-proof
Part (b) is the argument of Yang Pi-Yeh, Solution 5.4.15: if the $r$ points obtained from a configuration in general position by a finite sequence $w$ of admissible transformations were not in general position, then some three of them would become collinear after a further finite sequence $v$ of admissible transformations, and the composite $v\circ w$ is a finite sequence of admissible transformations from the original configuration under which those three points are collinear, which contradicts general position. The same conclusion follows from step [](#general-position-is-non-special){.pf-ref}: a configuration in general position is non-special in Nagata's sense, so the corresponding base points to its points under a Cremona transformation with centres within them are ordinary with no three collinear, and Section 2(2) of the paper makes a product of $F$-admissible quadratic transformations such a transformation.
:::

:::

::: {.pf-step #general-position-six-points}
Part (a) holds: a set of six points is in general position if and only if no three are collinear and not all six lie on a conic.

::: pf-proof
For the "only if" direction, suppose that six points in general position lie on a conic, take $P_1,P_2,P_3$ to be the coordinate points after a change of coordinates, and write the conic through them as $axy+byz+czx=0$. The quadratic transformation with centres $P_1,P_2,P_3$ is $(x:y:z)\mapsto(yz:zx:xy)$, so it sends $P_i=(x_i:y_i:z_i)$ to $(y_iz_i:z_ix_i:x_iy_i)$ for $i=4,5,6$, and those three points satisfy $bx+cy+az=0$ because $by_iz_i+cz_ix_i+ax_iy_i$ is the value of the conic at $P_i$. Three of the images are then collinear, which general position forbids. This is Yang Pi-Yeh, Solution 5.4.15(a).

For the "if" direction, suppose that no three of the six points are collinear and that not all six lie on a conic, and let $Q_1,Q_2,Q_3,P_4',P_5',P_6'$ be their images under the quadratic transformation with centres $P_1,P_2,P_3$. Hartshorne's proof of Proposition 4.10, Case 2, verifies that no three of the six images are collinear and that no six lie on a conic: $Q_1,Q_2,Q_3$ are noncollinear by construction; $Q_1,Q_2,P_4'$ collinear would put $P_4$ infinitely near $P_3$; $Q_1,P_4',P_5'$ collinear would make the strict transform of their line a line through $P_1,P_4,P_5$; $P_4',P_5',P_6'$ collinear would make the strict transform of their line a conic through $P_1,\ldots,P_6$; and six of the images on a conic would pull back to a line through $P_4,P_5,P_6$. Each admissible transformation therefore carries a configuration with these two properties to another, and the configuration reached after any finite sequence is again one to which the same verification applies, so no three of the six points are collinear after any finite sequence. That is general position.
:::

:::

::: {.pf-step #uncountable-field-lemma}
Let $k$ be uncountable. A nonempty open subset of $\PP_k^2$ cannot be covered by countably many proper closed subsets.

::: pf-proof
This step and the steps after it that carry (c) are the card's own: no source listed for this card proves (c) for any $r$, and the two that print an argument for it are named in step [](#part-c-open){.pf-ref}.

Let $U\subseteq\PP^2$ be nonempty open and let
$$
Z_1,Z_2,\ldots
$$
be proper closed subsets. Each $Z_n$ has only finitely many one-dimensional irreducible components. Since $k$ is uncountable, there are uncountably many lines in $\PP^2$, so one can choose a line $\ell$ which is not a component of any $Z_n$ and which meets $U$.

For every $n$, the intersection
$$
\ell\cap Z_n
$$
is finite. Hence
$$
\ell(k)\cap\bigcup_nZ_n
$$
is countable. But $\ell(k)\cong\PP^1(k)$ is uncountable, and $U\cap\ell$ is the complement of finitely many points in $\ell$. Therefore $U\cap\ell$ contains a point outside every $Z_n$.
:::

:::

::: {.pf-step #bad-locus-proper-closed}
Fix $P_1,\ldots,P_r$ in general position. For a finite word $w$ of triples of labels let $W_w\subseteq U$ be the set of points $P$ at which $w$ is admissible on
$$
(P_1,\ldots,P_r,P),
$$
which means that before each step of $w$ no three of the current $r+1$ points are collinear. Then $W_w$ is open in $U$, and for every triple $T$ of labels the set $B(w,T)$ of points $P\in W_w$ for which the terminal triple $T$ is collinear is closed in $W_w$. So $B(w,T)$ is a locally closed subset of $\PP^2$, and it lies in a proper closed subset of $\PP^2$ exactly when $W_w=\emptyset$ or $B(w,T)\ne W_w$. This step does not prove that in general; steps [](#properness-r-at-most-eight){.pf-ref}, [](#properness-r-nine){.pf-ref} and [](#properness-on-a-cubic){.pf-ref} prove under their hypotheses that $B(w,T)$ lies in a proper closed subset, and in the cases of step [](#part-c-open){.pf-ref} that is the one point of part (c) that this card leaves open.

::: pf-proof
The proof is by induction on the length of $w$, together with the statement that the terminal configuration of $w$ is given on $W_w$, locally, by a morphism to $(\PP^2)^{r+1}$. For the empty word $W_w=U$ and the configuration is $(P_1,\ldots,P_r,P)$. Let $A,B,C$ be the centres of a step. On an open set where coordinate vectors of $A,B,C$ are chosen regularly, let $M$ be the matrix with those columns; it is invertible because $A,B,C$ are not collinear. In the coordinates $M^{-1}x$ the centres are the coordinate points and the quadratic transformation is $(x:y:z)\mapsto(yz:zx:xy)$ [[P-AGH46CREMONA]]. The three new points $Q_A,Q_B,Q_C$ are the coordinate points of the target, and a point on none of the lines $AB$, $BC$, $CA$ has an image whose coordinates are polynomials in the coordinates of $A,B,C$ and of the point. Another choice of coordinate vectors changes the target by a projective transformation, which preserves collinearity. So on $W_w$ the configuration after each step is locally a morphism to $(\PP^2)^{r+1}$. Collinearity of the triple $T$ is the vanishing of a $3\times3$ determinant in the coordinates of the terminal points, so $B(w,T)$ is closed in $W_w$. For a further step $\tau$ the set $W_{w\tau}$ is the complement in $W_w$ of the finite union of the sets $B(w,T)$ over all triples $T$, so it is open in $W_w$, hence in $U$.

$U$ is irreducible, so a nonempty $W_w$ is dense in $\PP^2$, and a closed subset of $W_w$ is dense in $\PP^2$ exactly when it is $W_w$. This gives the criterion for $B(w,T)$ to lie in a proper closed subset of $\PP^2$.

Whether $B(w,T)\ne W_w$ is a separate question, and one case of it is proved here. If no centre triple of $w$ contains the label of $P$, then $w$ acts on the fixed configuration by part (b), so the terminal positions of $P_1,\ldots,P_r$ have no three collinear, and the terminal position of $P$ is $T(P)$ for the composite $T$ of the quadratic transformations of $w$, a birational map of $\PP^2$. A terminal triple not containing $P$ therefore imposes a condition independent of $P$, which is empty; one containing $P$ imposes $T(P)\in L$ for the line $L$ through the other two terminal points, and $T^{-1}(L)$ is a proper closed subset because $T$ is dominant and $L$ is proper. The same conclusion holds if $P$ occurs as a centre only in the last step. Let that step be centred at $Q,X,Y$ with $Q$ the image of $P$ and $X,Y$ the images of fixed labels; by part (b) the configuration before it is $(C_0,Q)$ with $C_0$ in general position and $Q$ a birational function of $P$. In adapted coordinates $Q=(1:0:0)$, $X=(0:1:0)$, $Y=(0:0:1)$, the images of the three centres are $(1:0:0),(0:1:0),(0:0:1)$, and the image of a point $a$ is $(y_az_a:z_ax_a:x_ay_a)$. A terminal triple containing $Q$ and two points $a,b$ of $C_0$ imposes that $a,b,Q$ be collinear, a line in $Q$; one containing $Q,X$ and $a$ imposes $x_a y_a=0$, that is $a\in XY$ or $a\in QY$ --- the first false because $a,X,Y$ are three points of the general-position configuration $C_0$, the second a line in $Q$ --- and one containing $X,Y,a$ imposes $y_a z_a=0$, the same two alternatives with $QX$ in place of $QY$; one containing only points of $C_0$ imposes that $Q$ lie on the conic through those points and $X,Y$, five points of a general-position configuration, which is a conic. Each is a proper closed condition in $Q$, hence in $P$. A word that uses $P$ as a centre and then continues past that step is not treated here. The natural route for it is induction on the length of $w$, pulling a terminal collinearity back through the last quadratic transformation --- a target line meets the inverse images of the three target base points as a conic, so the condition becomes one of a triple of configuration points lying on a conic through three others, of which collinearity is the degenerate case --- and that forces a stronger induction hypothesis, on incidences with curves of every degree, which is not written out here. So this step does not prove in general that $B(w,T)$ lies in a proper closed subset: step [](#dense-general-position-extension){.pf-ref} is complete *given* it, and in the cases of step [](#part-c-open){.pf-ref} part (c) is therefore not proved on this card. The case $r\le7$ over $\CC$ is proved in step [](#properness-r-at-most-seven){.pf-ref}, where the Del Pezzo criterion puts every one of these sets in a proper closed subset, the case $r\le8$ in step [](#properness-r-at-most-eight){.pf-ref}, the case $r=9$ in step [](#properness-r-nine){.pf-ref}, and the case of points on a cubic in step [](#properness-on-a-cubic){.pf-ref}. What is proved without it is (a), (b), and everything in (d) and (e).
:::

:::

::: {.pf-step #properness-r-at-most-seven}
If $k=\CC$ and $r\le7$, every set of step [](#bad-locus-proper-closed){.pf-ref} is contained in a proper closed subset of $\PP^2$, and part (c) holds for those $r$.

::: pf-proof
Fix a word $w$ and a terminal triple $T=\{a,b,c\}$. The classes on $\operatorname{Bl}_{r+1}\PP^2$ can be followed through the moves of $w$: a quadratic transformation centred at three of the current points replaces $h$ by $2h-c_1-c_2-c_3$ and the three exceptional classes by $h-c_j-c_k$, an integral orthogonal transformation of $\operatorname{Pic}$ which fixes $K=-3h+\sum_ic_i$. So the classes $h_w$ and $c_1,\ldots,c_{r+1}$ attached to the terminal plane depend on $w$ alone and not on $P$, and
$$
D=h_w-c_a-c_b-c_c,\qquad D^2=1-3=-2,\qquad K\cdot D=0,\qquad D\cdot h_w=1 .
$$
The three terminal points are collinear exactly when $\linearsystem{D}\ne\emptyset$: a member of $\linearsystem{D}$ meets each of $c_a,c_b,c_c$ in $1$, so none of them is a component of it, and its image in the terminal plane is a line through the three; conversely the strict transform of that line lies in $\linearsystem{D}$.

The two criteria of Dolgachev used below are stated over $\CC$, the base field the book fixes in Chapter 1, so this proof gives part (c) over $\CC$; the proof in every characteristic is step [](#properness-r-at-most-eight){.pf-ref}.

Now let $U$ be the complement in $\PP^2$ of the finitely many closed subsets on which the $r+1$ points violate the conditions that the criterion for their number requires: some three collinear, some six on a conic, and, at $r+1=8$, a cubic through the eight singular at one of them. Each is proper. For the first two, the fixed tuple is in general position, so the lines through its pairs and the conics through its fives are proper closed subsets. For the third, at $r+1=8$, let $E_0\subseteq\PP^2$ be a nonsingular cubic through $P_1,\ldots,P_7$, which step [](#smooth-cubic){.pf-ref} supplies. The set $B$ of points $P$ for which some cubic through $P_1,\ldots,P_7,P$ is singular at one of the eight points is closed in $\PP^2$, being the projection of a closed subset of $\PP^2\times\PP^9$. Let $P\in E_0$ and let $C\ne E_0$ be a cubic through the eight points singular at one of them, say at $Q$. The point $Q$ lies on $E_0$, since it is one of the eight, and $E_0$ is irreducible of degree $3$, so a cubic $C\ne E_0$ has no component in common with it; the divisor $C\cdot E_0$ has degree $9$ and contains $Q$ with multiplicity at least $2$ and the other seven points with multiplicity at least $1$. Its degree is at least $2+7=9$, so the multiplicities are exactly $2$ and $1$ and $C\cdot E_0=2Q+\sum_{R\ne Q}R$. In particular no cubic through the eight points is singular at two of them, and $C=E_0$ is nonsingular. If $Q=P$, then $\mathcal O_{E_0}(2P)\cong\mathcal O_{E_0}(3)(-\sum_{i\le7}P_i)$ is a fixed class of degree $2$, and at most four points $P$ satisfy it, because $P\mapsto\mathcal O_{E_0}(P-P_0)$ is a bijection onto $\Pic^\circ E_0$ (Example IV.1.3.7) and multiplication by $2$ there has finite kernel (Milne, *Abelian Varieties*, Theorem I.7.2); if $Q=P_j$, then $P$ is the single point of the effective divisor of the fixed class $\mathcal O_{E_0}(3)(-2P_j-\sum_{i\ne j,\,i\le7}P_i)$, of degree one. So $B\cap E_0$ is finite and $B\ne\PP^2$. At $r+1\le6$ the criterion is Hartshorne's Theorem V.4.6 with Corollary V.4.7: for ordinary points, at most six of them, with no three collinear and no six on a conic, the linear system of cubics through them is very ample, and the blowup embeds in $\PP^{9-(r+1)}$ with $\omega\cong\mathcal O(-1)$, so it is a Del Pezzo surface. At $r+1=7$ the criterion is the one printed in Dolgachev, §6.3.3, in the unnumbered sentence after Proposition 6.3.5: with condition (*), no three of the points collinear and no six on a conic, the blowup is a Del Pezzo surface of degree 2. $U$ is then nonempty. For $P\in U$ the blowup of $\PP^2$ at the $r+1\le8$ points is a Del Pezzo surface: at $r+1=8$ by Proposition 8.1.9, at $r+1=7$ by the sentence after Proposition 6.3.5, and at $r+1\le6$ by Theorem V.4.6 with Corollary V.4.7. Hence $-K$ is ample and every nonzero effective class has negative $K$-degree; since $K\cdot D=0$ and $D\ne0$, $\linearsystem{D}=\emptyset$.

Hence no point of $U$ lies in a set of step [](#bad-locus-proper-closed){.pf-ref}: were $w$ defined at $P\in U$ with the terminal triple collinear, $\linearsystem{D}$ would be nonempty there. Each of those sets is therefore contained in the complement of $U$, a proper closed subset of $\PP^2$, and step [](#dense-general-position-extension){.pf-ref} applied to their closures gives (c) for $r\le7$, with $V$ the complement of the countable union of those closures and of the finitely many points and lines. The sets themselves need not be closed, since definedness of a word is an open condition; it is their closures that the density argument uses.
:::

:::

::: {.pf-step #subset-general-position}
Every subset of a set of points in general position is in general position.

::: pf-proof
Let $S'\subseteq S$ with $S$ in general position. A quadratic transformation centred at three points of $S'$ is one centred at three points of $S$, and the points it produces from $S'$ are among the points it produces from $S$. So a finite sequence of admissible transformations for $S'$ is one for $S$, and three collinear points among the images of $S'$ are three collinear points among the images of $S$.
:::

:::

::: {.pf-step #bad-locus-root-class}
If $P\in U$ and $P_1,\ldots,P_r,P$ are not in general position, then $P\in Z_\alpha$ for one of countably many roots $\alpha\in\ZZ^{r+2}$, each fixed independently of $P$.

::: pf-proof
No three of $P_1,\ldots,P_r,P$ are collinear because $P\in U$. Take a word $w$ of admissible transformations of minimal length after which some three terminal points $T$ are collinear. At every earlier stage the three centres are noncollinear and no other point lies on a side of their triangle, so each step is defined and produces $r+1$ distinct ordinary points. By Example V.4.2.3 each step identifies $Y_P$ with the blow-up of the new configuration, and the new basis is $h'=2h-e_1-e_2-e_3$, $e'_{Q_i}=h-e_j-e_k$ and $e'_l=e_l$ for $l\ge4$, integer formulas that do not involve $P$. The strict transform of the terminal line through $T$ is an irreducible curve on $Y_P$ of class $h'-\sum_{s\in S}e'_s$, where $S\supseteq T$ is the set of terminal points on that line; adding the effective classes $e'_s$ for $s\in S\setminus T$ shows that $\alpha_{w,T}=h'-\sum_{s\in T}e'_s$, written in the original basis, is effective on $Y_P$. It has square $-2$ and $K$-degree $0$, because the transformations preserve the intersection form and $K$. There are countably many pairs $(w,T)$.
:::

:::

::: {.pf-step #bad-locus-closed}
Each $Z_\alpha$ is closed in $U$.

::: pf-proof
Let $\Gamma\subseteq X_r\times U$ be the graph of the inclusion $U\hookrightarrow X_r$ and $\mathcal Y=\Bl_\Gamma(X_r\times U)\to U$; it is a smooth projective family whose fibre over $P$ is $Y_P$. For $\alpha=dh-\sum_im_ie_i-me$, the line bundle $\operatorname{pr}^*\mathcal O(dh-\sum_im_ie_i)\otimes\mathcal O(-m\mathcal E)$ on $\mathcal Y$, with $\mathcal E$ the exceptional divisor, restricts to $\alpha$ on each fibre. By the semicontinuity theorem III.12.8, $\{P:h^0(Y_P,\alpha)\ge1\}=Z_\alpha$ is closed.
:::

:::

::: {.pf-step #effective-line-class-is-not-general}
For a finite word $w$ of triples of labels and a triple $T$ of labels, let $\alpha_{w,T}\in\ZZ^{r+2}$ be the class $h'-\sum_{s\in T}e'_s$, where $h',e'_1,\ldots,e'_{r+1}$ is obtained from the basis $h,e_1,\ldots,e_r,e$ of $\Pic Y_P$ by applying the integer formulas of step [](#bad-locus-root-class){.pf-ref} along $w$. Let $P\in U$. Then $P_1,\ldots,P_r,P$ are in general position if and only if no class $\alpha_{w,T}$ is the class of an effective divisor on $Y_P$. If $k$ is uncountable, part (c) holds for $P_1,\ldots,P_r$ if and only if $Z_{\alpha_{w,T}}\ne U$ for every $w$ and $T$.

::: pf-proof
If the points are not in general position, the proof of step [](#bad-locus-root-class){.pf-ref} gives a pair $(w,T)$ for which $\alpha_{w,T}$ is effective on $Y_P$.

Conversely, let $P_1,\ldots,P_r,P$ be in general position and fix $(w,T)$. By the definition of general position every step of $w$ is an admissible transformation, so by Example V.4.2.3 the terminal basis $h',e'_1,\ldots,e'_{r+1}$ consists of the class of the pullback of a line and the classes of the exceptional curves $E'_j$ for a blowing-down of $Y_P$ to a plane with centres $R_1,\ldots,R_{r+1}$, distinct ordinary points no three of which are collinear. Suppose that $D$ is an effective divisor of class $\alpha_{w,T}$. Write $D=D_0+\sum_ja_jE'_j$ with $a_j\ge0$ and no $E'_j$ a component of $D_0$. The image of $D_0$ in the plane is an effective divisor of degree $D\cdot h'=1$, so it is a line $\Lambda$, and $D_0$ is the strict transform of $\Lambda$, of class $h'-\sum_{R_j\in\Lambda}e'_j$ (Proposition V.3.6). For $s\in T$, comparing the coefficients of $e'_s$ in the two expressions for the class of $D$ gives $a_s=0$ and $R_s\in\Lambda$. So the three points $R_s$ with $s\in T$ are collinear, a contradiction.

Let $k$ be uncountable. If $Z_{\alpha_{w,T}}\ne U$ for every $(w,T)$, then each of these sets is a proper closed subset of the irreducible set $U$ by step [](#bad-locus-closed){.pf-ref}, each set $B(w,T)$ of step [](#bad-locus-proper-closed){.pf-ref} lies in $Z_{\alpha_{w,T}}$ by the proof of step [](#bad-locus-root-class){.pf-ref}, and step [](#dense-general-position-extension){.pf-ref} gives part (c). If $Z_{\alpha_{w,T}}=U$ for some $(w,T)$, then no point of $U$ makes $P_1,\ldots,P_r,P$ a set in general position, and no point outside $U$ does, because such a point is one of the $P_i$ or lies on a line $P_iP_j$. So no dense set $V$ exists.
:::

:::

::: {.pf-step #no-minus-two-curve}
Let $R_1,\ldots,R_n$ be ordinary points of $\PP^2$, no three collinear, and $X$ their blow-up. If $X$ carries an irreducible curve $C$ with $C^2=-2$ and $K\cdot C=0$, then $R_1,\ldots,R_n$ are not in general position.

::: pf-proof
$C$ is not exceptional, so $C=dh-\sum m_ie_i$ with $d\ge1$ and $m_i\ge0$ the multiplicities of its image (Proposition V.3.6), and $\sum m_i=3d$, $\sum m_i^2=d^2+2$. Each $m_i$ is at most $d$: the strict transforms of the lines through $R_i$ have class $h-e_i$ and cover $X$, so one of them is not $C$, and $C\cdot(h-e_i)=d-m_i\ge0$. Order the points so that $m_1\ge m_2\ge\cdots\ge m_n$. Then $n\ge3$ and $m_3\ge1$: otherwise $3d=m_1+m_2\le2d$, which contradicts $d\ge1$. Put $a=m_1$, $b=m_2$, $c=m_3$. If $a+b+c\le d$ then $\sum m_i^2\le a^2+b^2+c(3d-a-b)$, because $m_i\le c$ for $i\ge3$ and $\sum_{i\ge3}m_i=3d-a-b$; the function $d^2-3cd-(a^2+b^2-ac-bc)$ of $d$ increases for $d\ge 3c/2$, and at $d=a+b+c\ge3c$ it equals $2ab-2c^2\ge0$, so $\sum m_i^2\le d^2$, a contradiction. Hence $a+b+c>d$.

If three of the points $R_1,\ldots,R_n$ are collinear, they are not in general position. Otherwise the transformation centred at $R_1,R_2,R_3$ is admissible. It produces $n$ ordinary points of a plane whose blow-up is $X$ (Example V.4.2.3). On this blow-up $C$ is again an irreducible curve with $C^2=-2$ and $K\cdot C=0$. Its degree in the new plane is $2d-a-b-c<d$ (Exercise V.4.2), and this degree is at least $1$ because $C$, of square $-2$, is none of the exceptional curves of the new blow-up. So the argument applies to the new points and $C$. The degree is a positive integer that decreases at each repetition, so after finitely many admissible transformations three of the points are collinear, and $R_1,\ldots,R_n$ are not in general position.
:::

:::

::: {.pf-step #no-effective-root}
Let $Z$ be the blow-up of points in general position with $K_Z^2>0$ and $-K_Z$ the class of an irreducible curve. Then no root is effective on $Z$.

::: pf-proof
$-K_Z$ is nef, since its curve has square $K_Z^2>0$. If $D=\sum c_j\Gamma_j$ is an effective root, then $0=-K\cdot D=\sum c_j(-K\cdot\Gamma_j)$ with every term $\ge0$, so $K\cdot\Gamma_j=0$. By the Hodge index theorem V.1.9, $\Gamma_j^2<0$, and by adjunction (Exercise V.1.3) $\Gamma_j^2=2p_a-2\ge-2$, so $\Gamma_j^2=-2$, which step [](#no-minus-two-curve){.pf-ref} excludes.
:::

:::

::: {.pf-step #smooth-cubic}
If $r\le8$, there is a nonsingular plane cubic $E_0$ through $P_1,\ldots,P_r$.

::: pf-proof
No three of the points are collinear and no six lie on a conic, by step [](#subset-general-position){.pf-ref} and the "only if" argument of step [](#general-position-six-points){.pf-ref}; and no eight lie on a cubic singular at one of them, since such a cubic is irreducible (a line through at most two of the points and a conic through at most five cover at most seven) and its strict transform is excluded by step [](#no-minus-two-curve){.pf-ref}. A nonsingular member $C$ of $\abs{-K_{X_r}}$ meets each $E_i$ once ($C\cdot e_i=1$), so its image is a nonsingular cubic through the points; it remains to find $C$.

For $r\le6$, Corollary V.4.7 embeds $X_r$ in $\PP^{9-r}$ with hyperplane class $-K$; Bertini's theorem II.8.18, valid over any algebraically closed field, gives a nonsingular hyperplane section, which is connected by Corollary III.7.9 and hence irreducible.

For $r=7$, by Demazure, *Surfaces de Del Pezzo* III, No 9 (a), the surface is of strictly negative type, so $-K$ is ample, and by V, No 3, the anticanonical map $\varphi:X_7\to\PP^2$ is a double cover given locally by $\sigma^2-a\sigma-b=0$ with $\deg a=2$, $\deg b=4$, whose fibres over lines are the members of $\abs{-K}$. In characteristic $2$, $a\ne0$: if $a=0$ the singular points correspond to the zeros of $db$ (V, No 3), and $db$, which satisfies $\sum x_i\partial_ib=4b=0$, is a section of $\Omega_{\PP^2}(4)$, whose second Chern class $3-12+16=7$ is nonzero, so $db$ has a zero and $X_7$ would be singular. In every characteristic the kernel of $d\varphi_z$ is $T_zX_7\cap\langle\partial_\sigma\rangle$, of dimension at most $1$, and it is $1$ only on the curve $\{2\sigma=a\}$, which is a proper subset because the cover is separable. The member $\varphi^*\ell$ is singular at $z$ only when $d(\ell\circ\varphi)_z=0$, that is, when $z$ lies on that curve and $\ell$ is the line through $\varphi(z)$ in the direction of the image of $d\varphi_z$; these lines form a family of dimension at most $1$, and the reducible members $\varphi^*\ell$ are the finitely many sums of two exceptional curves (V, after Proposition 3). A general line therefore gives a nonsingular irreducible $C$.

For $r=8$, $\abs{-K_{X_8}}$ is a pencil whose members meet at one point $x$, transversally (Demazure III, Proposition 2); finitely many members are reducible (III, Lemma 1). Blowing up $x$ gives $X_9$ and a morphism $f:X_9\to\PP^1$ with connected fibres of arithmetic genus $1$, the exceptional curve $e_9$ being a section. If its general fibre were singular, $f$ would be quasi-elliptic, which happens only in characteristic $2$ and $3$ (Lang, *Quasi-elliptic surfaces in characteristic three*, Ann. Sci. ENS 12 (1979), Proposition 1.2). Then by Lang's formula (9), $e(X_9)=e(F_g)e(\PP^1)+\sum_b(e(F_b)-e(F_g))$ with $e(F_g)=2$ for the étale Euler numbers; since $e(X_9)=3+9=12$, $\sum_b(e(F_b)-2)=8$. Every irreducible fibre of a quasi-elliptic fibration is a rational curve with a cusp (Bombieri--Mumford, *Enriques' classification of surfaces in char. p, II*, proof of Proposition 5), of Euler number $2$, so some fibre $F=\sum n_jC_j$ is reducible. The section meets exactly one component, so another component $C$ has $C\cdot e_9=0$; since $F$ is connected, $n_CC^2=-\sum_{j}n_jC_j\cdot C<0$ over the other components, and $K\cdot C=-F\cdot C=0$ with adjunction gives $C^2=-2$. Being disjoint from $e_9$, $C$ is the pullback of an irreducible curve on $X_8$ with square $-2$ and $K$-degree $0$, which step [](#no-minus-two-curve){.pf-ref} excludes. So the general member of the pencil is nonsingular.
:::

:::

::: {.pf-step #properness-r-at-most-eight}
If $r\le8$, then $Z_\alpha\ne U$ for every root $\alpha$ in every characteristic, and, when $k$ is uncountable, part (c) holds for those $r$.

::: pf-proof
Take $E_0$ from step [](#smooth-cubic){.pf-ref}. Its strict transform on $X_r$ is irreducible of class $-K_{X_r}$ and square $9-r>0$, so step [](#no-effective-root){.pf-ref} applies to $X_r$. Let $P\in E_0\cap U$; all but finitely many points of $E_0$ qualify. On $Y_P$ the strict transform $E$ of $E_0$ is irreducible, $E\cong E_0$, of class $-K_{Y_P}$ with $E^2=8-r\ge0$. Suppose $D$ is effective of class $\alpha=dh-\sum_im_ie_i-me$ and write $D=aE+D'$ with $D'$ effective and not containing $E$; $0\le a\le d/3$ because $h$ is nef. Then $D'\cdot E=-K\cdot\alpha-aE^2=-a(8-r)$ is $\ge0$, so $D'\cdot E=0$ (and $a=0$ when $r<8$). By Proposition V.1.4, $D'\cap E=\emptyset$, so $\mathcal O_E(D')\cong\mathcal O_E$; restricting $h$, $e_i$, $e$ to $E\cong E_0$ gives $\mathcal O_{E_0}(1)$, $\mathcal O_{E_0}(P_i)$, $\mathcal O_{E_0}(P)$, hence
$$
\mathcal O_{E_0}(d-3a)\cong\mathcal O_{E_0}\Big(\textstyle\sum_i(m_i-a)P_i+(m-a)P\Big).
$$
For each of the finitely many $a$ put $n=m-a$. If $n\ne0$ and two points $P,P'$ satisfy the relation, then $n(P-P')\sim0$; by Example IV.1.3.7, $P\mapsto\mathcal O(P-P_0)$ identifies $E_0$ with $\Pic^\circ E_0$, and multiplication by $n$ on the elliptic curve $E_0$ is an isogeny (Milne, *Abelian Varieties* v2.00, Theorem I.7.2), so its kernel is finite and only finitely many $P$ satisfy the relation. If $n=0$, then $D'$ has class $\alpha+mK_{Y_P}$ and $D'\cdot e=m-m=0$, so its image on $X_r$ is effective of class $(d-3m)h-\sum_i(m_i-m)e_i$, a root, which step [](#no-effective-root){.pf-ref} excludes. So $Z_\alpha\cap E_0$ is finite and $Z_\alpha\ne U$.

By step [](#bad-locus-root-class){.pf-ref} every set of step [](#bad-locus-proper-closed){.pf-ref} meets $U$ inside some $Z_\alpha$, which is closed in $U$ by step [](#bad-locus-closed){.pf-ref} and is not $U$; so the set lies in a proper closed subset of $\PP^2$, the union of the closure of $Z_\alpha$ with the points $P_i$ and the lines $P_iP_j$, and step [](#dense-general-position-extension){.pf-ref} applies to these closed subsets.
:::

:::

::: {.pf-step #properness-r-nine}
Let $r=9$, and suppose that $k$ has characteristic $0$ or that some cubic through $P_1,\ldots,P_9$ is not cuspidal. Then $Z_\alpha\ne U$ for every root $\alpha$, and, when $k$ is uncountable, part (c) holds.

::: pf-proof
The plane cubics form a $\PP^9$, so some cubic $E_0$ passes through the nine points; in positive characteristic choose it not cuspidal. No three of the points are collinear, and no six lie on a conic: on an irreducible conic by step [](#subset-general-position){.pf-ref} and the "only if" argument of step [](#general-position-six-points){.pf-ref}, on a pair of lines because each line carries at most two. A cubic with a line as a component therefore carries at most $2+5$ of the points, so $E_0$ is irreducible and reduced. $E_0$ is nonsingular at each $P_i$: otherwise its strict transform on the blow-up of eight of the points, $P_i$ among them, is an irreducible curve of class $3h-2e_i-\sum_{j\ne i}e_j$, of square $-2$ and $K$-degree $0$, and the eight points are in general position by step [](#subset-general-position){.pf-ref}, against step [](#no-minus-two-curve){.pf-ref}. So the strict transform $E\subseteq X_9$ of $E_0$ has class $-K_{X_9}$ and $E\cong E_0$.

Let $P\in U$ be a nonsingular point of $E_0$ and $E'\subseteq Y_P$ the strict transform of $E$. Then $E'$ is irreducible of class $-K_{Y_P}$ (Proposition V.3.6), $E'^2=K_{Y_P}^2=-1$, and the blowing-down maps $E'$ isomorphically onto $E$. Suppose $D$ is effective of class a root $\alpha=dh-\sum_im_ie_i-me$, and write $D=aE'+\sum_jc_j\Gamma_j$ with $a\ge0$, $c_j>0$ and the $\Gamma_j$ distinct irreducible curves other than $E'$. Put $k_j=\Gamma_j\cdot E'=-K\cdot\Gamma_j\ge0$. Since $\alpha\cdot E'=-K\cdot\alpha=0$,
$$
\sum_jc_jk_j=(D-aE')\cdot E'=a,\qquad (D-aE')^2=\alpha^2+a^2E'^2=-2-a^2 .
$$
By adjunction (Exercise V.1.3), $\Gamma_j^2=2p_a(\Gamma_j)-2+k_j\ge k_j-2$. So $\Gamma_j^2\ge0$ when $k_j\ge2$, $\Gamma_j^2\ge-1$ when $k_j=1$, and when $k_j=0$ the even number $\Gamma_j^2$ is $-2$ or is $\ge0$. Let $J$ be the set of $j$ with $k_j=0$ and $\Gamma_j^2=-2$. Distinct irreducible curves meet nonnegatively, so
$$
-2-a^2=\Big(\sum_jc_j\Gamma_j\Big)^2\ge\sum_jc_j^2\Gamma_j^2\ge-2\sum_{j\in J}c_j^2-\sum_{k_j=1}c_j^2\ge-2\sum_{j\in J}c_j^2-a^2 ,
$$
the last inequality because $\sum_{k_j=1}c_j^2\le\big(\sum_{k_j=1}c_j\big)^2\le\big(\sum_jc_jk_j\big)^2=a^2$. Hence $J\ne\emptyset$: some component $\Gamma$ of $D$ is an irreducible curve other than $E'$ with $\Gamma^2=-2$ and $\Gamma\cdot E'=0$. By Proposition V.1.4, $\Gamma\cap E'=\emptyset$, so $\mathcal O_{Y_P}(\Gamma)$ is trivial on $E'$.

$\Gamma$ is not the exceptional curve over $P$, whose square is $-1$, so it is the strict transform of an irreducible curve $C_0\subseteq X_9$; let $c\in\Pic X_9$ be the class of $C_0$ and $n\ge0$ its multiplicity at $P$, so that $\Gamma$ has class $c-ne$ (Proposition V.3.6) and $0=\Gamma\cdot E'=c\cdot E-n$. If $n=0$, then $C_0\cong\Gamma$ is an irreducible curve on $X_9$ with $C_0^2=-2$ and $K\cdot C_0=-C_0\cdot E=0$, which step [](#no-minus-two-curve){.pf-ref} excludes. So $n=c\cdot E\ge1$, and restricting $\mathcal O_{Y_P}(\Gamma)$ to $E'\cong E$, where $e$ restricts to the point $P$, gives
$$
\mathcal O_{X_9}(c)\otimes\mathcal O_E\cong\mathcal O_E(nP).
$$
The class $c$ is one of finitely many that depend on $\alpha$ alone: $\Gamma$ is a component of $D$ and $h$ is nef, so $h\cdot c\le d$, and $C_0$ is one of the $e_i$ or has multiplicities between $0$ and its degree at the $P_i$. Fix $c$ with $n=c\cdot E\ge1$. If $P$ and $P'$ both satisfy the displayed relation, then $\mathcal O_E(n(P-P'))\cong\mathcal O_E$. The map $P\mapsto\mathcal O_E(P-P_0)$ is a bijection from the nonsingular points of $E$ to $\Pic^\circ E$, which is an elliptic curve when $E$ is nonsingular (Example IV.1.3.7), the group $\mathbf G_m$ when $E$ is nodal (Exercises II.6.7 and II.6.9) and the group $\mathbf G_a$ when $E$ is cuspidal (Example II.6.11.4). The elements killed by $n$ are finite in number on an elliptic curve (Milne, *Abelian Varieties* v2.00, Theorem I.7.2), are the $n$-th roots of unity in $\mathbf G_m$, and in $\mathbf G_a$ are $0$ alone in characteristic $0$. So only finitely many $P$ satisfy the relation for a given $c$. Hence $Z_\alpha\cap E_0$ is finite and $Z_\alpha\ne U$, and part (c) follows as in the last paragraph of the proof of step [](#properness-r-at-most-eight){.pf-ref}.

When the characteristic is $p>0$ and $E_0$ is cuspidal, every nonsingular point of $E_0$ is killed by $p$, the relation for a class $c$ with $p\mid c\cdot E$ holds for all $P$ or for none, and this argument does not decide that case.
:::

:::

::: {.pf-step #properness-on-a-cubic}
Let $r\ge9$ and let $k$ be uncountable. Suppose that $P_1,\ldots,P_r$ lie on a cubic $E_0$, and that $k$ has characteristic $0$ or $E_0$ is not cuspidal. Then $Z_{\alpha_{w,T}}\ne U$ for every class $\alpha_{w,T}$ of step [](#effective-line-class-is-not-general){.pf-ref}, and part (c) holds.

::: pf-proof
The first paragraph of the proof of step [](#properness-r-nine){.pf-ref} uses only nine of the points, so $E_0$ is irreducible and reduced and is nonsingular at each $P_i$. The strict transform $E\subseteq X_r$ of $E_0$ therefore has class $-K_{X_r}$, and $E\cong E_0$. All but finitely many points of $E_0$ lie in $U$, because $E_0$ meets each line $P_iP_j$ in at most three points.

Let $P\in U$ be a nonsingular point of $E_0$ and $E'\subseteq Y_P$ the strict transform of $E$. Then $E'$ is irreducible of class $-K_{Y_P}$ (Proposition V.3.6), its arithmetic genus is $1$ by adjunction (Exercise V.1.3), and the blowing-down maps $E'$ isomorphically onto $E$. Suppose that $P_1,\ldots,P_r,P$ are not in general position. As in the proof of step [](#bad-locus-root-class){.pf-ref}, there are a word $w$, a set $S$ of at least three terminal labels and a triple $T\subseteq S$ such that the strict transform $L\subseteq Y_P$ of a terminal line is an irreducible curve, isomorphic to $\PP^1$, of class $h'-\sum_{s\in S}e'_s$. The curve $L$ is not $E'$, because its arithmetic genus is $0$. In the terminal basis $K_{Y_P}=-3h'+\sum_je'_j$, so
$$
0\le L\cdot E'=-K_{Y_P}\cdot L=3-\abs{S}.
$$
Hence $S=T$ and $L\cdot E'=0$. By Proposition V.1.4, $L\cap E'=\emptyset$, so $\mathcal O_{Y_P}(L)$ is trivial on $E'$. The class of $L$ is $\alpha_{w,T}$. Write it as $c-ne$ with $c\in\Pic X_r$; then $n=L\cdot e\ge0$, because $L$, of square $-2$, is not the exceptional curve over $P$.

If $n=0$, then $L$ does not meet the exceptional curve over $P$, so it is the pullback of an irreducible curve on $X_r$ with square $-2$ and $K$-degree $0$, which step [](#no-minus-two-curve){.pf-ref} excludes. So $n\ge1$, and restricting $\mathcal O_{Y_P}(L)$ to $E'\cong E$, where $e$ restricts to the point $P$, gives
$$
\mathcal O_{X_r}(c)\otimes\mathcal O_E\cong\mathcal O_E(nP).
$$
The class $c$ and the integer $n\ge1$ depend on $(w,T)$ alone. For a fixed pair $(w,T)$, two points $P$ and $P'$ that satisfy this relation have $\mathcal O_E(n(P-P'))\cong\mathcal O_E$, and the proof of step [](#properness-r-nine){.pf-ref} shows that only finitely many points $P$ satisfy it for a given class $c$ and integer $n\ge1$: under the hypothesis on $E_0$ the elements of $\Pic^\circ E$ killed by $n$ are finite in number. There are countably many pairs $(w,T)$. So the nonsingular points $P\in E_0\cap U$ for which $P_1,\ldots,P_r,P$ are not in general position form a countable set $N$.

Now fix $(w,T)$. By step [](#effective-line-class-is-not-general){.pf-ref} every nonsingular point of $E_0$ in $Z_{\alpha_{w,T}}$ lies in $N$. The curve $E_0$ has uncountably many nonsingular points in $U$, because $k$ is uncountable. So $Z_{\alpha_{w,T}}\ne U$, and the last assertion of step [](#effective-line-class-is-not-general){.pf-ref} gives part (c).
:::

:::

::: {.pf-step #cuspidal-cubic-every-point-fails}
Let $k$ have characteristic $5$, let $E_0$ be the cuspidal cubic $y^2z=x^3$ with nonsingular points $P(t)=(t:1:t^3)$, let $t_1,\ldots,t_8\in k$ be linearly independent over $\FF_5$, and put $t_9=t_1-t_2-\cdots-t_8$ and $P_i=P(t_i)$. Then $P_1,\ldots,P_9$ are in general position, and for every nonsingular point $P$ of $E_0$ in $U$ the points $P_1,\ldots,P_9,P$ are not in general position. So the hypothesis on $E_0$ in step [](#properness-on-a-cubic){.pf-ref} is needed for an argument that takes $P$ on $E_0$.

::: pf-proof
By Example II.6.11.4, $t\mapsto\mathcal O_{E_0}(P(t)-P(0))$ is an isomorphism from the additive group of $k$ to $\Pic^\circ E_0$. The line $z=0$ meets $E_0$ only at $P(0)$, so $\mathcal O_{E_0}(1)\cong\mathcal O_{E_0}(3P(0))$. Hence, for integers $d$ and $\nu_j$ with $\sum_j\nu_j=3d$ and parameters $s_j\in k$,
$$
\mathcal O_{E_0}(d)\otimes\mathcal O_{E_0}\Big(-\sum_j\nu_jP(s_j)\Big)\cong\mathcal O_{E_0}\quad\Longleftrightarrow\quad\sum_j\nu_js_j=0 .
$$

The points $P_1,\ldots,P_9$ are distinct, because $t_9$ is none of $t_1,\ldots,t_8$. Let $X_9$ be their blow-up and $E\subseteq X_9$ the strict transform of $E_0$; it is irreducible of class $-K_{X_9}$, of arithmetic genus $1$, and $E\cong E_0$. Suppose that $P_1,\ldots,P_9$ are not in general position. A word of minimal length after which three points are collinear gives, as in the proof of step [](#bad-locus-root-class){.pf-ref}, an irreducible curve $L\subseteq X_9$, isomorphic to $\PP^1$, of class $h'-\sum_{s\in S}e'_s$ with $\abs{S}\ge3$. As in the proof of step [](#properness-on-a-cubic){.pf-ref}, $0\le L\cdot E=3-\abs{S}$, so $L^2=-2$, $K\cdot L=0$, and $\mathcal O_{X_9}(L)$ is trivial on $E$. Write $L=dh-\sum_i\mu_ie_i$. Then $\sum_i\mu_i=3d$, $\sum_i\mu_i^2=d^2+2$ and $\sum_i\mu_it_i=0$. Substituting $t_9$ gives $(\mu_1+\mu_9)t_1+\sum_{i=2}^8(\mu_i-\mu_9)t_i=0$, so $5$ divides $\mu_i-\mu_9$ for $2\le i\le8$, because $t_1,\ldots,t_8$ are linearly independent over $\FF_5$. Put $\nu_i=\mu_i-\mu_9$ for $i\le8$ and $d_0=d-3\mu_9$. Then $\sum_{i\le8}\nu_i=3d_0$ and $\sum_{i\le8}\nu_i^2=d_0^2+2$. The Cauchy--Schwarz inequality gives $9d_0^2\le8(d_0^2+2)$, so $d_0^2\le16$ and $\sum_{i\le8}\nu_i^2\le18$. So $\abs{\nu_i}\le4$, and $\nu_i=0$ for $2\le i\le8$. Then $\nu_1=3d_0$ and $9d_0^2=d_0^2+2$, which no integer satisfies. So $P_1,\ldots,P_9$ are in general position.

Let $P=P(t)\in U$ be a nonsingular point of $E_0$, and let $E'\subseteq Y_P$ be the strict transform of $E$, an irreducible curve of class $-K_{Y_P}$ with $E'^2=-1$ and $E'\cong E_0$. Put
$$
\gamma=8h-3e_1-2(e_2+\cdots+e_9)-5e,\qquad\gamma^2=64-9-32-25=-2,\qquad K_{Y_P}\cdot\gamma=-24+3+16+5=0 .
$$
The restriction of $\mathcal O_{Y_P}(\gamma)$ to $E'\cong E_0$ is $\mathcal O_{E_0}(8)\otimes\mathcal O_{E_0}(-3P_1-2(P_2+\cdots+P_9)-5P)$, and
$$
3t_1+2(t_2+\cdots+t_8)+2t_9+5t=5t_1+5t=0 ,
$$
so the restriction is trivial. The class $\gamma$ is effective. Otherwise the sequence $0\to\mathcal O_{Y_P}(\gamma+K_{Y_P})\to\mathcal O_{Y_P}(\gamma)\to\mathcal O_{E'}\to0$ gives $h^1(\gamma+K_{Y_P})\ge1$, so $h^1(-\gamma)\ge1$ by Serre duality (Corollary III.7.7). The Riemann--Roch theorem V.1.6 gives $\chi(-\gamma)=\tfrac12\gamma\cdot(\gamma+K_{Y_P})+1=0$, so $h^0(-\gamma)+h^2(-\gamma)\ge1$. But $h^0(-\gamma)=0$, because $-\gamma\cdot h=-8$ and the strict transforms of lines cover $Y_P$, and $h^2(-\gamma)=h^0(\gamma+K_{Y_P})\le h^0(\gamma)=0$, because $\gamma$ is the sum of $\gamma+K_{Y_P}$ and the class of $E'$.

Let $D$ be an effective divisor of class $\gamma$. The proof of step [](#properness-r-nine){.pf-ref} shows that an effective divisor $D$ of the class of a root has a component $\Gamma$ that is an irreducible curve with $\Gamma^2=-2$ and $K_{Y_P}\cdot\Gamma=-\Gamma\cdot E'=0$; that part of the proof uses only that $E'$ is irreducible of class $-K_{Y_P}$ with $E'^2=-1$. By step [](#no-minus-two-curve){.pf-ref} the points $P_1,\ldots,P_9,P$ are not in general position.
:::

:::

::: {.pf-step #effective-root-for-every-point}
For every $r\ge15$ there are points $P_1,\ldots,P_r$ in general position and a root $\alpha$ with $Z_\alpha=U$. For such $r$ the statement "$Z_\alpha\ne U$ for every root $\alpha$", which step [](#properness-r-at-most-eight){.pf-ref} proves for $r\le8$ and step [](#properness-r-nine){.pf-ref} for $r=9$ under its hypothesis, is false. The root $\alpha$ is none of the classes $\alpha_{w,T}$ of step [](#effective-line-class-is-not-general){.pf-ref}, and, when $k$ is uncountable, part (c) holds for these points.

::: pf-proof
Let $E_0$ be a nonsingular plane cubic. Call points $P_1,\ldots,P_r$ of $E_0$ *independent* when $\mathcal O_{E_0}(d)\otimes\mathcal O_{E_0}(-\sum_im_iP_i)$ is not trivial for any nonzero $(d;m_1,\ldots,m_r)\in\ZZ^{r+1}$ with $3d=\sum_im_i$. Since $k$ is uncountable, independent points exist for every $r$: choose them one at a time. If $P_1,\ldots,P_{j-1}$ are independent, a relation with $m_j\ne0$ fixes the class of $\mathcal O(m_jP_j)$, which leaves finitely many $P_j$ (Example IV.1.3.7 and Milne, *Abelian Varieties* v2.00, Theorem I.7.2); there are countably many relations, and one with $m_j=0$ is a relation among the earlier points.

Independent points are in general position. Three of them on a line $L$ give $\mathcal O_{E_0}(1)\cong\mathcal O_{E_0}(P_a+P_b+P_c)$, a relation, so no three are collinear. Let $X$ be the blow-up of the points and $E\subseteq X$ the strict transform of $E_0$, of class $3h-\sum_ie_i$; independence says that $\mathcal O_X(c)\otimes\mathcal O_E$ is not trivial for any nonzero $c\in\Pic X$ with $c\cdot E=0$, a condition on the pair $(X,E)$ that does not involve the basis of $\Pic X$. The admissible transformation centred at three of the points is, by Example V.4.2.3, a second blowing-down of $X$ to a plane; it maps $E$ isomorphically onto a cubic through the $r$ new points, because $E$ meets each contracted curve $h-e_j-e_k$ and each $e_l$ once (Exercise V.4.2). So the new points are independent points of a nonsingular cubic, no three of them are collinear, and by induction the same holds after every word.

Now let $r\ge15$ and $P\in U\setminus E_0$. On $Y_P$ the class $3h-\sum_{i\le15}e_i$ is effective, being the sum of the strict transform of $E_0$ and the $e_i$ with $i>15$, and $h-e_i-e$ is the class of the strict transform of the line $PP_i$. So
$$
\alpha=\Big(3h-\sum_{i\le15}e_i\Big)+4(h-e_1-e)+2(h-e_2-e)=9h-5e_1-3e_2-\sum_{i=3}^{15}e_i-6e
$$
is effective on $Y_P$. It is a root: $\alpha^2=81-25-9-13-36=-2$ and $K\cdot\alpha=-27+5+3+13+6=0$. So $Z_\alpha\supseteq U\setminus E_0$, and $Z_\alpha=U$ by step [](#bad-locus-closed){.pf-ref}.

The points $P_1,\ldots,P_r$ lie on the nonsingular cubic $E_0$. By step [](#properness-on-a-cubic){.pf-ref}, part (c) holds for them and $Z_{\alpha_{w,T}}\ne U$ for every $w$ and $T$. So $\alpha$ is none of the classes $\alpha_{w,T}$.
:::

:::

::: {.pf-step #dense-general-position-extension}
Assume that for every finite word $w$ of admissible transformations and every terminal triple the set of step [](#bad-locus-proper-closed){.pf-ref} lies in a proper closed subset of $\PP^2$.
If $k$ is uncountable and $P_1,\ldots,P_r$ are in general position, there is then a dense subset
$$
\boxed{V\subseteq\PP^2}
$$
such that every $P_{r+1}\in V$ makes $P_1,\ldots,P_r,P_{r+1}$ a general-position configuration.

::: pf-proof
There are only finitely many choices of a triple of labels at each stage, so there are only countably many finite words of admissible transformations. For each word there are finitely many terminal triples. Step [](#bad-locus-proper-closed){.pf-ref} therefore produces only countably many bad subsets of $\PP^2$, each contained, by the hypothesis of this step, in a proper closed subset.

Also exclude the finitely many original lines through pairs of the fixed points and the finitely many points $P_i$ themselves. Let $B$ be the union of all these closed subsets and put
$$
V=\PP^2\setminus B.
$$
Step [](#uncountable-field-lemma){.pf-ref}, applied inside every nonempty open subset of $\PP^2$, shows that $V$ is dense. For $P_{r+1}\in V$, no collinear triple occurs initially or after any finite admissible word, which is the definition of general position. Every point of $V$ therefore satisfies (c) --- given that each of the countably many bad sets lies in a proper closed subset, which for $r\le8$ is step [](#properness-r-at-most-eight){.pf-ref}, for $r\ge9$ points on a cubic is step [](#properness-on-a-cubic){.pf-ref} under its hypothesis, and in the cases of step [](#part-c-open){.pf-ref} is not derived on this card. When one of the bad sets is dense in $\PP^2$, the closed set $Z_{\alpha_{w,T}}$ that contains it is all of $U$, and by step [](#effective-line-class-is-not-general){.pf-ref} no point $P_{r+1}$ gives a set in general position. Part (c) is therefore proved on this card for $r\le8$ and for $r\ge9$ under the hypothesis of step [](#properness-on-a-cubic){.pf-ref}, and not in the cases of step [](#part-c-open){.pf-ref}.
:::

:::

::: {.pf-step #part-c-open}
Part (c) is not proved on this card in two cases: $r\ge10$ points that lie on no cubic, and, in characteristic $p>0$, $r\ge9$ points that lie on exactly one cubic when that cubic is cuspidal. In both cases part (c) for $P_1,\ldots,P_r$ is equivalent to the following statement: for every word $w$ and every triple $T$ there is a point $P\in U$ such that the class $\alpha_{w,T}$ is not the class of an effective divisor on $Y_P$. No source listed for this card proves part (c).

::: pf-proof
The equivalence is the last assertion of step [](#effective-line-class-is-not-general){.pf-ref}, which holds for every $r$. Steps [](#properness-r-at-most-eight){.pf-ref} and [](#properness-r-nine){.pf-ref} prove, under their hypotheses, more than part (c) needs: $Z_\alpha\ne U$ for every root $\alpha$. By step [](#effective-root-for-every-point){.pf-ref} that stronger statement is false for $r\ge15$, for a root that is none of the classes $\alpha_{w,T}$; so a proof for large $r$ has to use that the class has the form $\alpha_{w,T}$. Step [](#properness-on-a-cubic){.pf-ref} uses it through the irreducible curve of class $\alpha_{w,T}$, and it needs a cubic through $P_1,\ldots,P_r$ and $P$, which exists for some $P$ only when $P_1,\ldots,P_r$ lie on a cubic. When that cubic is cuspidal and the characteristic is positive, step [](#cuspidal-cubic-every-point-fails){.pf-ref} shows that the points of the cubic can all fail, so the point $P$ has to be taken off the cubic. If two cubics pass through all of $P_1,\ldots,P_r$, then $r=9$ and they span the pencil of cubics through eight of the points, whose general member is nonsingular by the proof of step [](#smooth-cubic){.pf-ref}; so the second case is that of a single cubic through the points, which is cuspidal.

What the sources print is the generic-point statement, Lemma 2.5 of Nagata, that independent generic points over the prime field are non-special with respect to Cremona transformations; its proof keeps the transformed points generic over the prime field and says nothing about the position of one further point with the first $r$ fixed. Hartshorne's hint for (c) is the countable-union lemma for an uncountable field, which neither source prints. The proof of part (c) on this card is therefore the card's own, and it is complete for $r\le8$ and for $r\ge9$ under the hypothesis of step [](#properness-on-a-cubic){.pf-ref}. Of the solution sets retained for the book, two print part (c), and neither proves it: Egbert, V.4.15, which treats the tuple $(P_1,\ldots,P_r)$ as a point of $(\PP^2)^r$ and does not address the fibre over a fixed tuple, and Yang Pi-Yeh, solution 5.4.15, whose argument uses part (a), the criterion for six points, for general $r$. The other sets retained for the book stop before Chapter V: Borcherds and Troiani at Chapter I, Cais, Sam, Lomont and Park at Chapter IV, and Stein, Saglam--Chris and Kim in Chapter III.
:::

:::

::: {.pf-step #every-negative-curve-is-exceptional}
Assume $r\le9$ and let the $P_i$ be in general position. Then every irreducible curve $C\subseteq X$ with $C^2<0$ is an irreducible exceptional curve of the first kind: $C\cong\PP^1$ and $C^2=-1$.

::: pf-proof
By step [](#general-position-is-non-special){.pf-ref} the points are non-special, so Proposition 12 of Nagata applies: for $r\le9$ the surface $\operatorname{dil}_{(P_1,\ldots,P_r)}(S)$ carries only finitely many irreducible curves that are not exceptional curves of the first kind and have negative grade, and the existence of such a curve is equivalent to the points being special. The points are not special, so no such curve exists; every irreducible curve of negative self-intersection is therefore an exceptional curve of the first kind, hence isomorphic to $\PP^1$ with self-intersection $-1$.
:::

:::

::: {.pf-step #classes-are-pre-exceptional}
For $r\le9$ and $P_1,\ldots,P_r$ in general position, the map sending an irreducible exceptional curve of the first kind to its numerical type is a bijection onto the set of pre-exceptional types with $r$ base points.

::: pf-proof
This is Theorem 2a of Nagata: if $P_1,\ldots,P_r$ are non-special with respect to Cremona transformations, there is a one-one correspondence between all pre-exceptional types $(d,m_1,\ldots,m_r)$ with $r$ base points and all irreducible exceptional curves of the first kind on $\operatorname{dil}_{(P_1,\ldots,P_r)}(S)$, in such a way that the curve corresponds to the type of $\operatorname{dil}(\mathcal L(d;\sum_im_iP_i))$. The proof runs by Lemma 2.6, which turns a pre-exceptional type into $\mathcal L(0;-P_1')$ over a Cremona transform with centres within the $P_i$ and so produces the curve, and by induction on the degree for the converse, using that $m_1+m_2+m_3>d$ for a curve of grade $-1$ and virtual genus $0$. Step [](#general-position-is-non-special){.pf-ref} supplies the hypothesis.
:::

:::

::: {.pf-step #count-fifty-six-and-two-forty}
The number of pre-exceptional types with $r$ base points is $56$ for $r=7$ and $240$ for $r=8$.

::: pf-proof
A pre-exceptional type has $I=-1$ and $vg=0$, and by Lemma 2.1(iii) of Nagata, the invariants of a type satisfy $3d-\sum_im_i=I-2vg+2$, so a pre-exceptional type is a solution of
$$
d^2-\sum_{i=1}^r m_i^2=-1,\qquad 3d-\sum_{i=1}^rm_i=1
$$
up to permutation. Conversely, every solution of these two equations is pre-exceptional, and the passage between the two formulations is printed in Dolgachev. By Definition 8.6, a vector of $I^{1,N}$ is exceptional when it lies in the $W(\mathbf E_N)$-orbit of $\omega_N$, and by Proposition 8.2.15, it is exceptional exactly when $\mathbf k_N\cdot v=-1$ and $v^2=-1$; for $v=d\mathbf e_0-\sum_im_i\mathbf e_i$ these are the same two equations, since $\mathbf k_N=-3\mathbf e_0+\mathbf e_1+\cdots+\mathbf e_N$ gives $\mathbf k_N\cdot v=\sum_im_i-3d$ and $v^2=d^2-\sum_im_i^2$. By Theorem 8.2.11, $W(\mathbf E_N)$ is the subgroup of $\mathbf O(\mathbf E_N)$ generated by the reflections in a canonical root basis, and in the canonical basis (8.5) that basis is $\beta_1=\alpha_{123}$ and $\beta_i=\alpha_{i-1,i}$ for $i\ge2$; the reflections $r_{\alpha_{i-1,i}}$, $i\ge2$, act as the permutation group $\mathfrak S_N$ of $\mathbf e_1,\ldots,\mathbf e_N$, as the sentence after Definition 7.5, says, so these together with $r_{\alpha_{123}}$ generate $W(\mathbf E_N)$. On $v$ one has $(v,\alpha_{123})=d-m_1-m_2-m_3=a$ and $\alpha_{123}^2=-2$, so
$$
r_{\alpha_{123}}(v)=v+a\alpha_{123}=(d+a)\mathbf e_0-(m_1+a)\mathbf e_1-(m_2+a)\mathbf e_2-(m_3+a)\mathbf e_3-\sum_{i\ge4}m_i\mathbf e_i
$$
is Nagata's operator $\mathfrak q$ on the type $(d,m_1,\ldots,m_r)$ of Section 2. Lemma 2.4, says that two numerical types are similar exactly when one is obtained from the other by a word in $\mathfrak q$ and in the permutations of the multiplicities, which is exactly the condition that the two vectors lie in one $W(\mathbf E_N)$-orbit, so the similarity classes are the $W(\mathbf E_N)$-orbits. The vectors satisfying the two equations are the $W(\mathbf E_N)$-orbit of $\omega_N$, and that orbit contains $\mathbf e_0-\mathbf e_1-\mathbf e_2$, the degree-$1$ family the same proposition lists, whose type is $(1,1,1,0,\ldots,0)$ with $r-2$ zeros, that is $d=1$ and $m_1=m_2=1$: the solutions of the two equations are therefore one similarity class, the pre-exceptional one, and Dolgachev's proof of completeness is the same descent, Noether's inequality after the permutations of $\mathfrak S_N$ and then $r_{\alpha_{123}}$ to lower the degree. What remains from the sources is the enumeration. Nagata's table for $r=8$, in Theorem 4a, lists all pre-exceptional types up to permutation, in seven rows $(0;-1,0,\ldots,0)$, $(1;1,1,0,\ldots,0)$, $(2;1,1,1,1,1,0,0,0)$, $(3;2,1,1,1,1,1,1,0)$, $(4;2,2,2,1,1,1,1,1)$, $(5;2,2,2,2,2,2,1,1)$ and $(6;3,2,\ldots,2)$, which account for $8+28+56+56+56+28+8=240$ classes; its first row is the class $\mathcal L(0;-P_1)$ of an exceptional curve, the only row with a negative multiplicity, and its last is the degree-$6$ class $6l-3e_{i_1}-2e_{i_2}-\cdots-2e_{i_8}$, of square $-1$ and $\mathbf k_8\cdot v=-1$. Dolgachev's table in Proposition 8.2.15 gives $240$ at $N=8$ and $56$ at $N=7$, and his printed list for $N=7$ runs $\mathbf e_i$, $\mathbf e_0-\mathbf e_i-\mathbf e_j$, $2\mathbf e_0-\mathbf e_1-\cdots-\mathbf e_7+\mathbf e_i+\mathbf e_j$ and $-\mathbf k_7-\mathbf e_i$, which count $7+21+21+7=56$. His printed list for $N=8$ is not to be read as a list of exceptional vectors: its last family, $-\mathbf k_8+2\mathbf e_{i_1}-\mathbf e_{i_2}-\cdots-\mathbf e_{i_6}$, has square $-14$ and $\mathbf k_8\cdot v=2$.
:::

:::

::: {.pf-step #part-d}
Part (d) holds: for $r=7$ the surface $X$ carries exactly $56$ irreducible nonsingular curves $C$ with $g=0$ and $C^2=-1$, and these are the only irreducible curves of negative self-intersection; for $r=8$ the numbers are $240$ and the same conclusion.

::: pf-proof
By step [](#every-negative-curve-is-exceptional){.pf-ref} every irreducible curve of negative self-intersection is an exceptional curve of the first kind, and by step [](#classes-are-pre-exceptional){.pf-ref} the exceptional curves of the first kind correspond one to one to the pre-exceptional types. Step [](#count-fifty-six-and-two-forty){.pf-ref} counts those types: $56$ for $r=7$ and $240$ for $r=8$. An exceptional curve of the first kind is by definition a nonsingular rational curve of self-intersection $-1$, so the count is the count of the curves the exercise asks for, and the same two steps say that there are no others of negative self-intersection.
:::

:::

::: {.pf-step #part-e}
Part (e) holds: for $r=9$ the surface $X$ carries infinitely many irreducible nonsingular curves $C$ with $g=0$ and $C^2=-1$.

::: pf-proof
This is the second half of Theorem 4a of Nagata: if $r\ge9$ and the $P_i$ are non-special, then $\operatorname{dil}_{(P_1,\ldots,P_r)}(S)$ carries infinitely many exceptional curves of the first kind. The proof given there is that $3d-\sum_im_i$ is an invariant of the similarity class by Lemma 2.8, so a pre-exceptional type satisfies $3d-\sum_im_i=1$; ordering $m_1\le\cdots\le m_r$ then gives $m_1+m_2+m_3\le(\sum_im_i)/3=(3d-1)/3<d$, so the operator $\mathfrak q$ of Section 2, which sends $(d,m_1,\ldots,m_r)$ to $(d+a,m_1+a,m_2+a,m_3+a,m_4,\ldots,m_r)$ with $a=d-m_1-m_2-m_3>0$, produces a pre-exceptional type of strictly larger degree. Iterating gives infinitely many pre-exceptional types with $r$ base points, and Theorem 2a of step [](#classes-are-pre-exceptional){.pf-ref} turns them into that many distinct irreducible exceptional curves of the first kind on $X$.
:::

:::

::: pf-qed
Steps [](#general-position-six-points){.pf-ref} and [](#general-position-preserved-under-sequence){.pf-ref} prove (a) and (b). Steps [](#uncountable-field-lemma){.pf-ref}, [](#bad-locus-proper-closed){.pf-ref} and [](#dense-general-position-extension){.pf-ref} carry (c): the properness they rest on is step [](#properness-r-at-most-eight){.pf-ref} for $r\le8$ and step [](#properness-on-a-cubic){.pf-ref} for $r\ge9$ under its hypothesis; in the two cases of step [](#part-c-open){.pf-ref} it is not derived, and part (c) is not proved on this card in those cases. Steps [](#every-negative-curve-is-exceptional){.pf-ref}, [](#classes-are-pre-exceptional){.pf-ref}, [](#count-fifty-six-and-two-forty){.pf-ref} and [](#part-d){.pf-ref} prove (d), and step [](#part-e){.pf-ref} proves the starred (e).
:::

:::
:::

::: {.remark title="Published solutions"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.4, exercise 4.15, read in `tmp/sources/hartshorne-1977-algebraic-geometry.md`. Part (a) is decided in the book and in Yang: the "only if" direction is Yang's (a), the argument of step [](#general-position-six-points){.pf-ref}, and the "if" direction is the verification in the proof of Proposition 4.10, Case 2, that a quadratic transformation centred at three of six points with no three collinear and not all six on a conic produces six points with those same two properties, which is general position by induction over finite sequences.

M. Nagata, *On rational surfaces, II*, Mem. Coll. Sci. Univ. Kyoto Ser. A 32 (1960), is the source the book's own note cites (Nagata [5, II]), and its Theorem 4a is the theorem in question. The paper contains: Section 2(c) with Lemma 2.2, the definition of non-speciality, which step [](#general-position-is-non-special){.pf-ref} identifies with general position and which is the hypothesis of Theorem 2a and of Proposition 12; Proposition 3, the criterion for special points, that some type similar to $(1,1,1,1,0,\ldots,0)$, with $r-3$ zeros, the class of a line through three of the points, has a nonempty effective system; Lemma 2.4, the descent by the operator $\mathfrak q$ that exhausts a similarity class; Lemma 2.5, the statement that independent generic points over the prime field are non-special, which is a statement about one generic configuration and not about the fibre over a fixed one; Theorem 2a, the bijection between pre-exceptional types and irreducible exceptional curves of the first kind; Theorem 4a, finiteness at $r\le8$ with its table of pre-exceptional types for $r=8$, and the infinite family at $r=9$, which is the starred part (e); and Proposition 12, the statement that an irreducible curve of negative self-intersection that is not of the first kind exists only when the points are special.

Igor V. Dolgachev, *Topics in Classical Algebraic Geometry*, Proposition 8.2.15 with its proof and its table, and Section 8.2.6 with Lemma 8.2.18, classifies and counts the vectors with $\mathbf k_N\cdot v=-1$ and $v^2=-1$, which are the classes with $C\cdot K_X=-1$ and $C^2=-1$, at $56$ for $N=7$ and $240$ for $N=8$; Section 8.2.6 explains why on a Del Pezzo surface the image of each exceptional vector is a $(-1)$-curve, which is Dolgachev's route to the same realization that Theorem 2a gives here. Three defects of that passage in the book are worth naming. The degree bound the proof draws from $(3d-1)^2\le N(d^2+1)$ is not what that inequality gives, which is $d\le3$ at $N=7$ and, the equality case $d=7$ forcing every multiplicity to equal $5/2$, $d\le6$ at $N=8$. The list for $N=8$ reads, after the classes $\mathbf e_i$, $\mathbf e_0-\mathbf e_i-\mathbf e_j$ and $2\mathbf e_0-\mathbf e_1-\cdots-\mathbf e_7+\mathbf e_i+\mathbf e_j$, the families $-\mathbf k_8+\mathbf e_i-\mathbf e_j$, $-\mathbf k_8+\mathbf e_0-\mathbf e_i-\mathbf e_j-\mathbf e_k$ and $-\mathbf k_8+2\mathbf e_{i_1}-\mathbf e_{i_2}-\cdots-\mathbf e_{i_6}$, and the last of these, read as it stands, is not a family of exceptional vectors; so the printed list is not to be read as a list of them. And even read so as to make it one, it does not reach the degree $6$ of Nagata's row $(6;3,2,\ldots,2)$, which is an exceptional class: $-2\mathbf k_8-\mathbf e_i$ has square $-1$ and $\mathbf k_8\cdot v=-1$. The counts $56$ and $240$ stand, in his table and in Nagata's.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.4.15: for part (a) the statement that one curve of order $m$ passes through $m(m+3)/2$ points, by induction on $m$; for the rest, (b) is the single line "This is Nagata, Rational Surfaces II, corollary to proposition 9, and use (a) of this problem", (c) is the general-position set as the complement of the vanishing of finitely many determinants, (d) is a list of four families for $r=7$ summing to $56$ and, for $r=8$, six counted rows whose last entry is "the rest", which must be $56$ to make $240$, and there is no entry for the starred (e). His (b) cites Nagata's corollary to Proposition 9, which is the criterion for special points and not the invariance of the definition.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.4.15 argues all five parts: its (a) in the "only if" direction, a conic through the six points becoming a line through the images of $P_4,P_5,P_6$, and in the "if" direction only the case of a line through those three images, which pulls back to a conic through all six; (b) the composability argument; (c) the union of the lines $P_iP_j$ and the conics through five of the points, whose complement is dense because $k$ is uncountable, the printed hint's lemma used and not proved; (d) the four rows for $r=7$ and the seven for $r=8$, without saying which classes are represented by irreducible curves nor whether negative curves other than $(-1)$-curves exist; and (e) the degree-increasing argument, labelled by him "the case $r>9$".
:::
