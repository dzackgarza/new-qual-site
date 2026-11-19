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
This example is apparently due to Kodaira -- see Nagata $[5, II, p. 283]$.
:::

::: {.solution}
Let $X=\operatorname{Bl}_{P_1,\ldots,P_r}\PP^2$ be the blowup, with $h$ the class of the pullback of a line and $e_i$ the exceptional classes, so that $K_X=-3h+\sum_ie_i$. For a class $C=dh-\sum_im_ie_i$ the intersection form gives $C^2=d^2-\sum_im_i^2$, and the virtual genus of the virtual linear system $\mathcal L(d;\sum_im_iP_i)$ is
$$
vg=\frac{d^2-3d+2-\sum_i m_i(m_i-1)}{2},
$$
a quantity of the numerical type alone (Nagata, Section 2(3), printed p. 277, and Lemma 2.8, printed p. 280). An irreducible curve of $X$ that is not one of the $e_i$ has, in Nagata's language, the class $\mathcal L(d;\sum_im_iP_i)$ with $m_i=m(P_i;C)$; Nagata's "grade" $I$ is the self-intersection and his "virtual genus" is the arithmetic genus (Section 1(3), printed p. 276).

The two conditions the exercise's parts (d) and (e) turn on are Nagata's:

- a virtual linear system $L$ is exceptional exactly when it is irreducible with $I(L)=-1$ and $vg(L)=0$, by Proposition 2, printed p. 277; for an irreducible curve $C$ on $X$ its class is exceptional exactly when $C\cong\PP^1$ and $C^2=-1$, which is the definition of an irreducible curve of the first kind;
- a numerical type $(d,m_1,\ldots,m_r)$ is *pre-exceptional* when it is similar to $(1,1,1,0,\ldots,0)$ with $r-2$ zeros, which is the type of $r$ base points with $d=1$, $m_1=m_2=1$ and $m_3=\cdots=m_r=0$, the class of a line through two of the points, so that $I=-1$ and $vg=0$; and by Theorem 3a (printed p. 282) a virtually connected system with $I=-1$ and $vg=0$ is of pre-exceptional type.

The transcription below proves (a), (b), (d) and (e), and it proves (c) for $r\le7$ in step [](#properness-r-at-most-seven){.pf-ref}. For $r\ge8$ its three steps prove (c) only given the properness of the bad locus --- the set of points $P$ for which some fixed finite word of admissible transformations makes a specified terminal triple collinear --- and the step on that locus asserts that properness without deriving it. No source listed for the card proves part (c) for any $r$.

::: pf

::: {.pf-step #general-position-is-non-special}
For ordinary points $P_1,\ldots,P_r$ of $\PP^2$ with no three collinear, being in general position is the same condition as being non-special with respect to Cremona transformations.

::: pf-proof
Nagata, Section 2(c), printed p. 279, calls the points non-special when for every Cremona transformation $T$ with centres within the $P_i$ the corresponding base points to the $P_i$ under $T$ are ordinary points of $T(S)$ no three of which are collinear; the corresponding base points are the $r$ points of Lemma 2.2, printed p. 278, which are exactly $r$ in number and satisfy $F=\operatorname{dil}_{(P_1',\ldots,P_r')}(T(S))$. By Section 2(2) of the paper a Cremona transformation with centres within the $P_i$ is by definition a product of $F$-admissible quadratic Cremona transformations, and $F$-admissible here means exactly that the centres are points of the configuration, so these are the finite sequences of admissible transformations of the exercise. The two definitions therefore quantify over the same sequences and require the same thing of the resulting configuration.
:::

:::

::: {.pf-step #general-position-preserved-under-sequence}
General position is preserved by every finite sequence of admissible transformations, which is part (b).

::: pf-proof
Part (b) is the argument of Yang Pi-Yeh, Solution 5.4.15, printed p. 112: if the $r$ points obtained from a configuration in general position by a finite sequence $w$ of admissible transformations were not in general position, then some three of them would become collinear after a further finite sequence $v$ of admissible transformations, and the composite $v\circ w$ is a finite sequence of admissible transformations from the original configuration under which those three points are collinear, which contradicts general position. The same conclusion follows from step [](#general-position-is-non-special){.pf-ref}: a configuration in general position is non-special in Nagata's sense, so the corresponding base points to its points under a Cremona transformation with centres within them are ordinary with no three collinear, and Section 2(2) of the paper makes a product of $F$-admissible quadratic transformations such a transformation.
:::

:::

::: {.pf-step #general-position-six-points}
Part (a) holds: a set of six points is in general position if and only if no three are collinear and not all six lie on a conic.

::: pf-proof
For the "only if" direction, suppose that six points in general position lie on a conic, take $P_1,P_2,P_3$ to be the coordinate points after a change of coordinates, and write the conic through them as $axy+byz+czx=0$. The quadratic transformation with centres $P_1,P_2,P_3$ is $(x:y:z)\mapsto(yz:zx:xy)$, so it sends $P_i=(x_i:y_i:z_i)$ to $(y_iz_i:z_ix_i:x_iy_i)$ for $i=4,5,6$, and those three points satisfy $bx+cy+az=0$ because $by_iz_i+cz_ix_i+ax_iy_i$ is the value of the conic at $P_i$. Three of the images are then collinear, which general position forbids. This is Yang Pi-Yeh, Solution 5.4.15(a), printed p. 112.

For the "if" direction, suppose that no three of the six points are collinear and that not all six lie on a conic, and let $Q_1,Q_2,Q_3,P_4',P_5',P_6'$ be their images under the quadratic transformation with centres $P_1,P_2,P_3$. Hartshorne's proof of Proposition 4.10, Case 2, printed pp. 403--404, verifies that no three of the six images are collinear and that no six lie on a conic: $Q_1,Q_2,Q_3$ are noncollinear by construction; $Q_1,Q_2,P_4'$ collinear would put $P_4$ infinitely near $P_3$; $Q_1,P_4',P_5'$ collinear would make the strict transform of their line a line through $P_1,P_4,P_5$; $P_4',P_5',P_6'$ collinear would make the strict transform of their line a conic through $P_1,\ldots,P_6$; and six of the images on a conic would pull back to a line through $P_4,P_5,P_6$. Each admissible transformation therefore carries a configuration with these two properties to another, and the configuration reached after any finite sequence is again one to which the same verification applies, so no three of the six points are collinear after any finite sequence. That is general position.
:::

:::

::: {.pf-step #uncountable-field-lemma}
Let $k$ be uncountable. A nonempty open subset of $\PP_k^2$ cannot be covered by countably many proper closed subsets.

::: pf-proof
This step and the two after it are the card's own: no source listed for this card prints the statement of (c).

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
Fix $P_1,\ldots,P_r$ in general position. For every fixed finite word $w$ of admissible transformations and every fixed triple of labels, the set of points
$$
P\in\PP^2
$$
for which the word is defined on
$$
(P_1,\ldots,P_r,P)
$$
and the specified terminal triple is collinear is a closed subset of $\PP^2$. It is a proper subset whenever the determinant written below is not identically zero, which this step asserts and does not prove; that nonvanishing is the one point of part (c) that this card leaves open.

::: pf-proof
Work on the open subset on which the successive centers occurring in $w$ are noncollinear and all quadratic transformations are defined at the remaining labeled points. The standard quadratic formula [[P-AGH46CREMONA]] shows inductively that every terminal point has homogeneous coordinates which are rational functions of the coordinates of $P$. Collinearity of a specified terminal triple is therefore the vanishing of a rational determinant. Clearing denominators gives a closed condition on the initial point $P$.

The determinant is not identically zero, and the proof of that is the one point of this step that the card does not carry out.

What the argument gives is the closedness, which is all the rest of (c) uses: the terminal coordinates are rational functions of $P$, so after clearing denominators a specified terminal collinearity is the vanishing of a polynomial in $P$. Properness is a separate assertion, and one case of it is proved here. If no centre triple of $w$ contains the label of $P$, then $w$ acts on the fixed configuration by part (b), so the terminal positions of $P_1,\ldots,P_r$ have no three collinear, and the terminal position of $P$ is $T(P)$ for the composite $T$ of the quadratic transformations of $w$, a birational map of $\PP^2$. A terminal triple not containing $P$ therefore imposes a condition independent of $P$, which is empty; one containing $P$ imposes $T(P)\in L$ for the line $L$ through the other two terminal points, and $T^{-1}(L)$ is a proper closed subset because $T$ is dominant and $L$ is proper. The same conclusion holds if $P$ occurs as a centre only in the last step. Let that step be centred at $Q,X,Y$ with $Q$ the image of $P$ and $X,Y$ the images of fixed labels; by part (b) the configuration before it is $(C_0,Q)$ with $C_0$ in general position and $Q$ a birational function of $P$. In adapted coordinates $Q=(1:0:0)$, $X=(0:1:0)$, $Y=(0:0:1)$, the images of the three centres are $(1:0:0),(0:1:0),(0:0:1)$, and the image of a point $a$ is $(y_az_a:z_ax_a:x_ay_a)$. A terminal triple containing $Q$ and two points $a,b$ of $C_0$ imposes that $a,b,Q$ be collinear, a line in $Q$; one containing $Q,X$ and $a$ imposes $x_a y_a=0$, that is $a\in XY$ or $a\in QY$ --- the first false because $a,X,Y$ are three points of the general-position configuration $C_0$, the second a line in $Q$ --- and one containing $X,Y,a$ imposes $y_a z_a=0$, the same two alternatives with $QX$ in place of $QY$; one containing only points of $C_0$ imposes that $Q$ lie on the conic through those points and $X,Y$, five points of a general-position configuration, which is a conic. Each is a proper closed condition in $Q$, hence in $P$. A word that uses $P$ as a centre and then continues past that step is not treated here. The natural route for it is induction on the length of $w$, pulling a terminal collinearity back through the last quadratic transformation --- a target line meets the inverse images of the three target base points as a conic, so the condition becomes one of a triple of configuration points lying on a conic through three others, of which collinearity is the degenerate case --- and that forces a stronger induction hypothesis, on incidences with curves of every degree, which is not written out here. So this card asserts properness and does not prove it in general: step [](#dense-general-position-extension){.pf-ref} is complete *given* it, and for $r\ge8$ part (c) is therefore not proved on this card. The case $r\le7$ is proved in step [](#properness-r-at-most-seven){.pf-ref}, where the Del Pezzo criterion turns every one of these sets proper. What is proved without it is (a), (b), and everything in (d) and (e).
:::

:::

::: {.pf-step #properness-r-at-most-seven}
If $r\le7$, every set of step [](#bad-locus-proper-closed){.pf-ref} is contained in a proper closed subset of $\PP^2$, and part (c) holds for those $r$.

::: pf-proof
Fix a word $w$ and a terminal triple $T=\{a,b,c\}$. The classes on $\operatorname{Bl}_{r+1}\PP^2$ can be followed through the moves of $w$: a quadratic transformation centred at three of the current points replaces $h$ by $2h-c_1-c_2-c_3$ and the three exceptional classes by $h-c_j-c_k$, an integral orthogonal transformation of $\operatorname{Pic}$ which fixes $K=-3h+\sum_ic_i$. So the classes $h_w$ and $c_1,\ldots,c_{r+1}$ attached to the terminal plane depend on $w$ alone and not on $P$, and
$$
D=h_w-c_a-c_b-c_c,\qquad D^2=1-3=-2,\qquad K\cdot D=0,\qquad D\cdot h_w=1 .
$$
The three terminal points are collinear exactly when $\linearsystem{D}\ne\emptyset$: a member of $\linearsystem{D}$ meets each of $c_a,c_b,c_c$ in $1$, so none of them is a component of it, and its image in the terminal plane is a line through the three; conversely the strict transform of that line lies in $\linearsystem{D}$.

Now let $U$ be the complement in $\PP^2$ of the finitely many closed subsets on which the $r+1$ points fail Dolgachev's general-position conditions of the definition preceding Proposition 8.1.9, printed p. 251: no three collinear, no six on a conic, and, at $r+1=8$ only, no cubic through the eight singular at one of them. Each is proper: the first two because the fixed tuple is in general position and the lines through its pairs and the conics through its fives are proper closed subsets, the third because eight points impose eight conditions on the ten coefficients of a cubic and the singularity two more, a square system whose determinant is not identically zero. At $r+1\le7$ the printed condition (iv) is automatic --- a cubic singular at one of the points and through the other $N-1$ meets $3+(N-1)\le9$ conditions on $10$ coefficients --- so the criterion at those $N$ is (i)--(iii), which is how the proposition is used here; the printed list is stated for the maximal case and is read that way. $U$ is then nonempty. For $P\in U$ the blowup of $\PP^2$ at the $r+1\le8$ points is a Del Pezzo surface by Proposition 8.1.9 on that page, so $-K$ is ample and every nonzero effective class has negative $K$-degree; since $K\cdot D=0$ and $D\ne0$, $\linearsystem{D}=\emptyset$.

Hence no point of $U$ lies in a set of step [](#bad-locus-proper-closed){.pf-ref}: were $w$ defined at $P\in U$ with the terminal triple collinear, $\linearsystem{D}$ would be nonempty there. Each of those sets is therefore contained in the complement of $U$, a proper closed subset of $\PP^2$, and step [](#dense-general-position-extension){.pf-ref} applied to their closures gives (c) for $r\le7$, with $V$ the complement of the countable union of those closures and of the finitely many points and lines. The sets themselves need not be closed, since definedness of a word is an open condition; it is their closures that the density argument uses.
:::

:::

::: {.pf-step #dense-general-position-extension}
Assume that for every finite word $w$ of admissible transformations and every terminal triple the set of step [](#bad-locus-proper-closed){.pf-ref} is a proper subset of $\PP^2$.
If $k$ is uncountable and $P_1,\ldots,P_r$ are in general position, there is then a dense subset
$$
\boxed{V\subseteq\PP^2}
$$
such that every $P_{r+1}\in V$ makes $P_1,\ldots,P_r,P_{r+1}$ a general-position configuration.

::: pf-proof
There are only finitely many choices of a triple of labels at each stage, so there are only countably many finite words of admissible transformations. For each word there are finitely many terminal triples. Step [](#bad-locus-proper-closed){.pf-ref} therefore produces only countably many bad subsets of $\PP^2$, each closed and, by the hypothesis of this step, proper.

Also exclude the finitely many original lines through pairs of the fixed points and the finitely many points $P_i$ themselves. Let $B$ be the union of all these bad subsets and put
$$
V=\PP^2\setminus B.
$$
Step [](#uncountable-field-lemma){.pf-ref}, applied inside every nonempty open subset of $\PP^2$, shows that $V$ is dense. For $P_{r+1}\in V$, no collinear triple occurs initially or after any finite admissible word, which is the definition of general position. Every point of $V$ therefore satisfies (c) --- given that each of the countably many bad sets is proper, which for $r\le7$ is step [](#properness-r-at-most-seven){.pf-ref} and for $r\ge8$ is what step [](#bad-locus-proper-closed){.pf-ref} asserts and does not derive; without that properness the intersection $V$ can be empty. Part (c) is therefore proved on this card for $r\le7$ and not for $r\ge8$.
:::

:::

::: {.pf-step #part-c-open}
No source listed for this card proves part (c).

::: pf-proof
What the sources print is the generic-point statement, Lemma 2.5 of Nagata, printed p. 279, that independent generic points over the prime field are non-special with respect to Cremona transformations; its proof keeps the transformed points generic over the prime field and says nothing about the position of one further point with the first $r$ fixed. Hartshorne's hint for (c), printed p. 409, is the countable-union lemma for an uncountable field, which neither source prints. The proof above is therefore the card's own, and it is complete for $r\le7$ by step [](#properness-r-at-most-seven){.pf-ref} and, for $r\ge8$, given the properness that step [](#bad-locus-proper-closed){.pf-ref} asserts and does not derive. Of the solution sets retained for the book, two print part (c), and neither proves it: Egbert at printed p. 295, which treats the tuple $(P_1,\ldots,P_r)$ as a point of $(\PP^2)^r$ and does not address the fibre over a fixed tuple, and Yang Pi-Yeh at printed p. 112, whose argument uses part (a), the criterion for six points, for general $r$. The other sets retained for the book stop before Chapter V: Borcherds and Troiani at Chapter I, Cais, Sam, Lomont and Park at Chapter IV, and Stein, Saglam--Chris and Kim in Chapter III.
:::

:::

::: {.pf-step #every-negative-curve-is-exceptional}
Assume $r\le9$ and let the $P_i$ be in general position. Then every irreducible curve $C\subseteq X$ with $C^2<0$ is an irreducible exceptional curve of the first kind: $C\cong\PP^1$ and $C^2=-1$.

::: pf-proof
By step [](#general-position-is-non-special){.pf-ref} the points are non-special, so Proposition 12 of Nagata, printed p. 293, applies: for $r\le9$ the surface $\operatorname{dil}_{(P_1,\ldots,P_r)}(S)$ carries only finitely many irreducible curves that are not exceptional curves of the first kind and have negative grade, and the existence of such a curve is equivalent to the points being special. The points are not special, so no such curve exists; every irreducible curve of negative self-intersection is therefore an exceptional curve of the first kind, hence isomorphic to $\PP^1$ with self-intersection $-1$.
:::

:::

::: {.pf-step #classes-are-pre-exceptional}
For $r\le9$ and $P_1,\ldots,P_r$ in general position, the map sending an irreducible exceptional curve of the first kind to its numerical type is a bijection onto the set of pre-exceptional types with $r$ base points.

::: pf-proof
This is Theorem 2a of Nagata, printed pp. 280--281: if $P_1,\ldots,P_r$ are non-special with respect to Cremona transformations, there is a one-one correspondence between all pre-exceptional types $(d,m_1,\ldots,m_r)$ with $r$ base points and all irreducible exceptional curves of the first kind on $\operatorname{dil}_{(P_1,\ldots,P_r)}(S)$, in such a way that the curve corresponds to the type of $\operatorname{dil}(\mathcal L(d;\sum_im_iP_i))$. The proof runs by Lemma 2.6, which turns a pre-exceptional type into $\mathcal L(0;-P_1')$ over a Cremona transform with centres within the $P_i$ and so produces the curve, and by induction on the degree for the converse, using that $m_1+m_2+m_3>d$ for a curve of grade $-1$ and virtual genus $0$. Step [](#general-position-is-non-special){.pf-ref} supplies the hypothesis.
:::

:::

::: {.pf-step #count-fifty-six-and-two-forty}
The number of pre-exceptional types with $r$ base points is $56$ for $r=7$ and $240$ for $r=8$.

::: pf-proof
A pre-exceptional type has $I=-1$ and $vg=0$, and by Lemma 2.1(iii) of Nagata, printed p. 277, the invariants of a type satisfy $3d-\sum_im_i=I-2vg+2$, so a pre-exceptional type is a solution of
$$
d^2-\sum_{i=1}^r m_i^2=-1,\qquad 3d-\sum_{i=1}^rm_i=1
$$
up to permutation. Conversely, every solution of these two equations is pre-exceptional, and the passage between the two formulations is printed in Dolgachev. By Definition 8.6, printed p. 261, a vector of $I^{1,N}$ is exceptional when it lies in the $W(\mathbf E_N)$-orbit of $\omega_N$, and by Proposition 8.2.15, printed p. 261, it is exceptional exactly when $\mathbf k_N\cdot v=-1$ and $v^2=-1$; for $v=d\mathbf e_0-\sum_im_i\mathbf e_i$ these are the same two equations, since $\mathbf k_N=-3\mathbf e_0+\mathbf e_1+\cdots+\mathbf e_N$ gives $\mathbf k_N\cdot v=\sum_im_i-3d$ and $v^2=d^2-\sum_im_i^2$. By Theorem 8.2.11, printed p. 258, $W(\mathbf E_N)$ is the subgroup of $\mathbf O(\mathbf E_N)$ generated by the reflections in a canonical root basis, and in the canonical basis (8.5), printed p. 257, that basis is $\beta_1=\alpha_{123}$ and $\beta_i=\alpha_{i-1,i}$ for $i\ge2$; the reflections $r_{\alpha_{i-1,i}}$, $i\ge2$, act as the permutation group $\mathfrak S_N$ of $\mathbf e_1,\ldots,\mathbf e_N$, as the sentence after Definition 7.5, printed p. 235, says, so these together with $r_{\alpha_{123}}$ generate $W(\mathbf E_N)$. On $v$ one has $(v,\alpha_{123})=d-m_1-m_2-m_3=a$ and $\alpha_{123}^2=-2$, so
$$
r_{\alpha_{123}}(v)=v+a\alpha_{123}=(d+a)\mathbf e_0-(m_1+a)\mathbf e_1-(m_2+a)\mathbf e_2-(m_3+a)\mathbf e_3-\sum_{i\ge4}m_i\mathbf e_i
$$
is Nagata's operator $\mathfrak q$ on the type $(d,m_1,\ldots,m_r)$ of Section 2, printed p. 279. Lemma 2.4, printed p. 279, says that two numerical types are similar exactly when one is obtained from the other by a word in $\mathfrak q$ and in the permutations of the multiplicities, which is exactly the condition that the two vectors lie in one $W(\mathbf E_N)$-orbit, so the similarity classes are the $W(\mathbf E_N)$-orbits. The vectors satisfying the two equations are the $W(\mathbf E_N)$-orbit of $\omega_N$, and that orbit contains $\mathbf e_0-\mathbf e_1-\mathbf e_2$, the degree-$1$ family the same proposition lists, whose type is $(1,1,1,0,\ldots,0)$ with $r-2$ zeros, that is $d=1$ and $m_1=m_2=1$: the solutions of the two equations are therefore one similarity class, the pre-exceptional one, and Dolgachev's proof of completeness is the same descent, Noether's inequality after the permutations of $\mathfrak S_N$ and then $r_{\alpha_{123}}$ to lower the degree. What remains from the sources is the enumeration. Nagata's table for $r=8$, printed p. 284, lists all pre-exceptional types up to permutation, in seven rows $(0;-1,0,\ldots,0)$, $(1;1,1,0,\ldots,0)$, $(2;1,1,1,1,1,0,0,0)$, $(3;2,1,1,1,1,1,1,0)$, $(4;2,2,2,1,1,1,1,1)$, $(5;2,2,2,2,2,2,1,1)$ and $(6;3,2,\ldots,2)$, which account for $8+28+56+56+56+28+8=240$ classes; its first row is the class $\mathcal L(0;-P_1)$ of an exceptional curve, the only row with a negative multiplicity, and its last is the degree-$6$ class $6l-3e_{i_1}-2e_{i_2}-\cdots-2e_{i_8}$, of square $-1$ and $\mathbf k_8\cdot v=-1$. Dolgachev's table, printed p. 261, gives $240$ at $N=8$ and $56$ at $N=7$, and his printed list for $N=7$ runs $\mathbf e_i$, $\mathbf e_0-\mathbf e_i-\mathbf e_j$, $2\mathbf e_0-\mathbf e_1-\cdots-\mathbf e_7+\mathbf e_i+\mathbf e_j$ and $-\mathbf k_7-\mathbf e_i$, which count $7+21+21+7=56$. His printed list for $N=8$ is not to be read as a list of exceptional vectors: its last family, $-\mathbf k_8+2\mathbf e_{i_1}-\mathbf e_{i_2}-\cdots-\mathbf e_{i_6}$, has square $-14$ and $\mathbf k_8\cdot v=2$.
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
This is the second half of Theorem 4a of Nagata, printed pp. 283--284: if $r\ge9$ and the $P_i$ are non-special, then $\operatorname{dil}_{(P_1,\ldots,P_r)}(S)$ carries infinitely many exceptional curves of the first kind. The proof given there is that $3d-\sum_im_i$ is an invariant of the similarity class by Lemma 2.8, so a pre-exceptional type satisfies $3d-\sum_im_i=1$; ordering $m_1\le\cdots\le m_r$ then gives $m_1+m_2+m_3\le(\sum_im_i)/3=(3d-1)/3<d$, so the operator $\mathfrak q$ of Section 2, which sends $(d,m_1,\ldots,m_r)$ to $(d+a,m_1+a,m_2+a,m_3+a,m_4,\ldots,m_r)$ with $a=d-m_1-m_2-m_3>0$, produces a pre-exceptional type of strictly larger degree. Iterating gives infinitely many pre-exceptional types with $r$ base points, and Theorem 2a of step [](#classes-are-pre-exceptional){.pf-ref} turns them into that many distinct irreducible exceptional curves of the first kind on $X$.
:::

:::

::: pf-qed
Steps [](#general-position-six-points){.pf-ref} and [](#general-position-preserved-under-sequence){.pf-ref} prove (a) and (b). Steps [](#uncountable-field-lemma){.pf-ref}, [](#bad-locus-proper-closed){.pf-ref} and [](#dense-general-position-extension){.pf-ref} carry (c): for $r\le7$ the properness they rest on is step [](#properness-r-at-most-seven){.pf-ref}, and for $r\ge8$ it is asserted there and not derived, step [](#part-c-open){.pf-ref} records that no source listed proves it, and part (c) is not proved on this card for $r\ge8$. Steps [](#every-negative-curve-is-exceptional){.pf-ref}, [](#classes-are-pre-exceptional){.pf-ref}, [](#count-fifty-six-and-two-forty){.pf-ref} and [](#part-d){.pf-ref} prove (d), and step [](#part-e){.pf-ref} proves the starred (e).
:::

:::
:::

::: {.remark title="Published solutions"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.4, exercise 4.15, printed p. 409, all five parts on that one page. Part (a) is decided in the book and in Yang: the "only if" direction is Yang's (a), the argument of step [](#general-position-six-points){.pf-ref}, and the "if" direction is the verification in the proof of Proposition 4.10, Case 2, printed pp. 403--404, that a quadratic transformation centred at three of six points with no three collinear and not all six on a conic produces six points with those same two properties, which is general position by induction over finite sequences.

M. Nagata, *On rational surfaces, II*, Mem. Coll. Sci. Univ. Kyoto Ser. A 32 (1960), is the source the book's own note cites ("see Nagata [5, II, p. 283]"), and its Theorem 4a is the printed theorem at those pages. The paper contains: Section 2(c) with Lemma 2.2, printed pp. 278--279, the definition of non-speciality, which step [](#general-position-is-non-special){.pf-ref} identifies with general position and which is the hypothesis of Theorem 2a and of Proposition 12; Proposition 3, printed p. 279, the criterion for special points, that some type similar to $(1,1,1,1,0,\ldots,0)$, with $r-3$ zeros, the class of a line through three of the points, has a nonempty effective system; Lemma 2.4, printed p. 279, the descent by the operator $\mathfrak q$ that exhausts a similarity class; Lemma 2.5, printed p. 279, the statement that independent generic points over the prime field are non-special, which is a statement about one generic configuration and not about the fibre over a fixed one; Theorem 2a, printed pp. 280--281, the bijection between pre-exceptional types and irreducible exceptional curves of the first kind; Theorem 4a, printed pp. 283--284, finiteness at $r\le8$ with its table of pre-exceptional types for $r=8$ on p. 284, and the infinite family at $r=9$, which is the starred part (e); and Proposition 12, printed p. 293, the statement that an irreducible curve of negative self-intersection that is not of the first kind exists only when the points are special.

Igor V. Dolgachev, *Topics in Classical Algebraic Geometry*, Proposition 8.2.15 with its proof and its table, printed p. 261, and Section 8.2.6 with Lemma 8.2.18, printed pp. 263--264, classifies and counts the vectors with $\mathbf k_N\cdot v=-1$ and $v^2=-1$, which are the classes with $C\cdot K_X=-1$ and $C^2=-1$, at $56$ for $N=7$ and $240$ for $N=8$; Section 8.2.6 explains why on a Del Pezzo surface the image of each exceptional vector is a $(-1)$-curve, which is Dolgachev's route to the same realization that Theorem 2a gives here. Three defects of that printed passage are worth naming. The degree bound the proof draws from $(3d-1)^2\le N(d^2+1)$ is not what that inequality gives, which is $d\le3$ at $N=7$ and, the equality case $d=7$ forcing every multiplicity to equal $5/2$, $d\le6$ at $N=8$. The list for $N=8$ reads, after the classes $\mathbf e_i$, $\mathbf e_0-\mathbf e_i-\mathbf e_j$ and $2\mathbf e_0-\mathbf e_1-\cdots-\mathbf e_7+\mathbf e_i+\mathbf e_j$, the families $-\mathbf k_8+\mathbf e_i-\mathbf e_j$, $-\mathbf k_8+\mathbf e_0-\mathbf e_i-\mathbf e_j-\mathbf e_k$ and $-\mathbf k_8+2\mathbf e_{i_1}-\mathbf e_{i_2}-\cdots-\mathbf e_{i_6}$, and the last of these, read as it stands, is not a family of exceptional vectors; so the printed list is not to be read as a list of them. And even read so as to make it one, it does not reach the degree $6$ of Nagata's row $(6;3,2,\ldots,2)$ on p. 284, which is an exceptional class: $-2\mathbf k_8-\mathbf e_i$ has square $-1$ and $\mathbf k_8\cdot v=-1$. The counts $56$ and $240$ stand, in his table and in Nagata's.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.4.15, printed p. 294 for part (a) --- the statement that one curve of order $m$ passes through $m(m+3)/2$ points, by induction on $m$ --- and p. 295 for the rest: (b) is the single line "This is Nagata, Rational Surfaces II, corollary to proposition 9, and use (a) of this problem", (c) is the general-position set as the complement of the vanishing of finitely many determinants, (d) is a list of four families for $r=7$ summing to $56$ and, for $r=8$, six counted rows whose last entry is "the rest", which must be $56$ to make $240$, and there is no entry for the starred (e). His (b) cites the corollary at p. 291, which is the criterion for special points and not the invariance of the definition.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.4.15, printed p. 112, argues all five parts: its (a) in the "only if" direction, a conic through the six points becoming a line through the images of $P_4,P_5,P_6$, and in the "if" direction only the case of a line through those three images, which pulls back to a conic through all six; (b) the composability argument; (c) the union of the lines $P_iP_j$ and the conics through five of the points, whose complement is dense because $k$ is uncountable, the printed hint's lemma used and not proved; (d) the four rows for $r=7$ and the seven for $r=8$, without saying which classes are represented by irreducible curves nor whether negative curves other than $(-1)$-curves exist; and (e) the degree-increasing argument, labelled by him "the case $r>9$".
:::
