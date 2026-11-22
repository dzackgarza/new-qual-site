---
schema: qual/card@1
id: P-AGH543ORDINARYSING
kind: problem
title: Reduction of a plane curve to ordinary singularities by quadratic transformations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Geometry
  - Blowups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.3 and the retained Egbert pointer to Hirschfeld,
    together with the exercise's prescribed V.3.8 resolution input and the
    quadratic-transform formulas of V.4.2. When projection from a chosen bad
    point is separable, a point blowup can be realized inside a quadratic
    transformation by taking the other two base points generally off the
    curve; the three fundamental lines may then be chosen transverse away
    from the chosen centre, so their contractions create only ordinary
    multiple points. In positive characteristic this pencil argument can fail
    at a strange/inseparable centre. The retained source explicitly sends
    that characteristic-free case to Hirschfeld, Algebraic Curves over
    Finite Fields, Theorem 3.27, so the proof below does not silently extend
    the separable argument across that obstruction.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof after separating the separable-pencil argument
    from the positive-characteristic inseparable case. Verified the common
    blowup geometry and ordinary-singularity calculation against V.4.2; the
    inseparable case is attributed only to the Hirschfeld theorem explicitly
    cited by the retained source, rather than extrapolated from Bertini.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.4,
    exercise 4.3, printed page 407. Checked the multiplicity accounting of steps
    s1 to s6 against V.4.2, printed page 406: for a quadratic transformation
    centred at P, A, B with multiplicities m, 0, 0 the strict transform has
    degree 2d-m and the multiplicities at the three points corresponding to the
    fundamental lines PA, PB, AB are d-m, d-m and d, so the three contraction
    points are ordinary d-fold and (d-m)-fold points formed from the d and d-m
    transverse intersection points of those lines with C. Checked that the
    auxiliary choice in step choose-auxiliary-points is made with lines outside
    the tangent cone at P, which is what makes i_P(C,PA) = mu_P(C), and that
    separability of the projection is carried as a hypothesis on that step.
    Searched outside the twelve retained sets: Egbert, PDF p. 286, is the single
    line "See Algebraic Curves over Finite Fields by Hirschfeld, Theorem 3.27",
    and Hirschfeld's book is not in tmp/sources; Algebraic Geometry II,
    National Taiwan University, 2020 Spring, Chapter V homework, Exercise 3 of
    section 4, PDF p. 15 (tmp/sources/ntu-ag2-chapter5.pdf), replaces the
    resolution blowups by quadratic transformations with two auxiliary centres
    and then analyses the multiplicity at P in a single chart, ending "so
    induction on this then we are done" without the case where every tangent
    direction must be separated; Yang Pi-Yeh, Hartshorne Solutions, exercise
    5.4.3, printed p. 109 (tmp/sources/lfwin-hartshorne-solutions.pdf), chooses
    the two points so that P1Pi meets C transversally at P1, notes
    mu(R_i) < mu(P_1), and concludes that the process stops with only ordinary
    singularities, but does not show that the contracted points are ordinary.
    Not checked: Hirschfeld's Theorem 3.27, which the card takes as its source
    for the inseparable case and which is not available here.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Step inseparable-case gave a false reason for the separability of the
    projection in characteristic 0: it said that a bad point carries at least
    two tangent directions, whereas an ordinary cusp is a bad point with one
    tangent direction. The step now argues that the projection from a bad point
    is nonconstant on the normalization, an irreducible plane curve with a
    singular point being no line, and that a nonconstant morphism of
    nonsingular curves is separable in characteristic 0. Re-read the printed
    exercise, Hartshorne, Algebraic Geometry (1977), V.4, exercise 4.3, printed
    p. 407, and the quadratic-transformation multiplicities of (4.2), printed
    p. 406, in the text version
    tmp/sources/hartshorne-1977-algebraic-geometry.md; the count d, d-m, d-m of
    step contraction-points-ordinary was rechecked and is unchanged. The
    positive-characteristic status is unchanged: the inseparable-projection
    case is still the unread citation of Hirschfeld, Algebraic Curves over
    Finite Fields, Theorem 3.27, not in tmp/sources, so the exercise as printed
    is still unproved there. The two treatments cited in the remarks were
    re-read in their text versions and are described correctly as they stand:
    NTU, Exercise 3 of section 4, PDF pp. 15-16
    (tmp/sources/ntu-ag2-chapter5.md), which asserts that the singularities
    from the blown-down lines are ordinary without showing it, and Egbert,
    entry 5.4.3, PDF p. 286
    (tmp/sources/hartshorne-solutions-egbert.md), the bare Hirschfeld citation.
    Not checked: Hirschfeld's Theorem 3.27, Yang Pi-Yeh printed p. 109, and any
    printing of these sets other than their text versions. The event of
    2026-11-11 above had been rewritten in place; it is restored to the text it
    was dated with, and this note is its correction.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcribed for issue #121 from a published proof that covers the exercise
    in every characteristic: William Fulton, Algebraic Curves (2008), §7.4
    Quadratic Transformations, the standard quadratic transformation and the
    formulas (1)-(3) on printed pp. 87-89, good and excellent position with
    (4)-(7) on printed pp. 88-90, the invariant g* with (8) on printed p. 90,
    Lemma 1 on printed p. 90 with Problem 5.26 and Theorem 2 of §5.4 behind it
    on printed p. 60, Theorem 2 of §7.4 on printed p. 91, and Appendix A
    Nonzero Characteristic on printed p. 113. Read in the text version
    tmp/sources/fulton-2008-algebraic-curves-pp55-62-86-92-110-115.md, whose
    markers name PDF pages 63-70, 94-100 and 118-123 against printed 55-62,
    86-92 and 110-115, so printed page = marker - 8; the pages were checked
    against the PDF page by page. The same theorem is proved by the same route
    in Thomas Rüd, Resolution of singularities on projective curves (2015),
    Proposition 19 printed p. 25, Propositions 20-21 printed pp. 26-27,
    Proposition 22 printed p. 28, Theorem 13 printed p. 28 and §7.3 printed
    p. 40, read in tmp/sources/rud-2015-resolution-singularities-curves.md
    with printed page = PDF page - 1. Supplied on the card, and named as such
    there: the calculation of (8), which Fulton gives only as "a calculation,
    using (2) and (7)", verified by the identity binom(2n-r-1,2) - binom(n,2)
    - 2*binom(n-r,2) = binom(n-1,2) - binom(r,2), both sides
    (n^2-r^2-3n+r+2)/2; the passage from (6) to the ordinariness of the three
    fundamental images, following Rüd's Propositions 20-21; the observation
    that the two centres of the preparatory transformation of Appendix A are
    taken off C, which is what makes deg F' = 2n - m there; and the accounting
    that the preliminary steps of the positive-characteristic case do not
    increase g*, so that they interleave harmlessly with the terminating
    sequence. Checked against Hartshorne V.4.3, printed p. 407, and against
    the multiplicity formulas of (V, 4.2), printed p. 406, which give the same
    three target multiplicities d, d-r, d-r. The card's earlier proof, which
    covered characteristic 0 alone and took the inseparable case from
    Hirschfeld's Theorem 3.27, is replaced, and the remark that called the
    published treatments of the exercise incomplete is withdrawn, the two
    proofs above being complete. Not checked: Fulton's Problem 4.16, to which
    his proof of Lemma 1 defers the change of coordinates carrying three lines
    to X, Y, Z, was not read; the printed copies of either book were not
    consulted, only the text versions beside the retained PDFs; and Rüd's
    Remark 23, printed p. 28, which says that an ordinary multiple point
    contributes nothing to g*, is false as printed, an ordinary double point
    contributing 1, and is used nowhere on the card.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Page correction to the event above, which is left as written. The formulas
    (1), (2) and (3) of Fulton's §7.4 all stand on printed p. 88, not across
    pp. 88-89: PDF p. 96 of the retained PDF, whose head reads 88, carries all
    three, and printed p. 89 carries (5) and (6). The solution's first step and
    the remark now say p. 88 for all three; (4) on p. 88, (5) and (6) on p. 89,
    excellent position, g*, (8) and Lemma 1 on p. 90 and Theorem 2 on p. 91 are
    as the event above records, and no mathematical claim changes.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's findings on this batch, repaired here; the two events of 2026-11-16
    above are left as written. The termination measure was wrong: step
    termination ordered the pair (number of bad points, g*) lexicographically,
    which a step can violate by adding bad points among the P_i while g* drops,
    and the bound N + g* then did not follow. The step now proves that
    N + g* itself drops by at least 1 at each step: a bad P_i has r_i >= 2, so
    the number of bad P_i is at most the sum of binom(r_i,2) that (8) subtracts
    from g*. That accounting is the card's, Fulton stating at printed p. 91 the
    two alternatives and the bound without it. Step excellent-position's part
    (b) was muddled and misattributed: it spoke of branches of C' at P meeting L,
    where P is not on L, and it credited Rud's Propositions 20-21 with an
    argument they do not give, those propositions proving sum I = n. In its
    place a new step tangent-directions states the fact the passage needs --- that
    the strict transform of a plane germ under the blowup meets the exceptional
    curve in one point per tangent direction, with multiplicity the exponent of
    that factor in the tangent cone --- and proves it from the local model (5) of
    printed p. 89; part (b) then applies it with D = C' and its transform C, the
    n points of C ∩ L being smooth and transverse. That argument is the card's:
    Fulton's own line is only "applying (6) to the curves C' and (C')' = C". So
    is the paragraph of step positive-characteristic that keeps the preliminary
    transformations of Appendix A from breaking the termination, the appendix
    saying only "we can proceed as before"; Fulton's printed "insure that p
    doesn't divide n-r" is named there as a slip for n'-r. Page corrections:
    Rud's Proposition 22 and Remark 23 stand on printed p. 27, not p. 28, as do
    his Proposition 23 and the whole of §6.3 after Proposition 21; only Theorem
    13 is on p. 28. Two claims about Rud are withdrawn: that Proposition 22
    proves the nonnegativity of g*, which its first case does not, arriving only
    at sum r(r-1) <= n(n-1); and that its route is the same throughout, since
    Proposition 19's proof infers the irreducibility of the section G_lambda
    from that of F and Theorem 13 uses the false Remark 23. Those three defects
    are now stated on the card's remark instead of being passed over. The
    rendered remarks are also reduced to mathematics and citation: the sentences
    about which book was read, and which steps were supplied where, leave them
    (QUAL-08), and the remark opener takes the attribute form of STYLE-01.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's findings on the second round of this batch, repaired here; every
    event above is left as written. The step tangent-directions, which the
    earlier pass on this date added, is withdrawn. No source states it: (5) of
    Fulton, printed p. 89, is the isomorphism of neighbourhoods under
    (x,z) -> (x,xz) and the factorisation of F(X,XZ,1), not a statement about
    tangent directions at all. Its proof was also false in one case: it said
    that the direction X = 0 occurs in the tangent cone exactly when F_m(1,Y')
    vanishes identically, which never happens for F_m nonzero, the condition
    being that X divides F_m, that is deg F_m(1,Y') < m. No new proof of that
    fact is written here. Part (b) of step excellent-position returns to the
    card's own argument, marked in the step as the card's: the count
    mu_P(C') = n is (6) applied to C' and to C as Fulton directs, legitimate
    by (4) on printed p. 88, and the passage from the count to ordinariness is
    read off the model (5) with C' in the role of the curve, so the n
    multiplicities I(P_i, C cap L) = 1 become the n exponents of the tangent
    cone of C' at P. Rud's Propositions 20 and 21 are no longer credited with
    that passage, which they do not carry; they prove the sum instead.
    Two further arguments are corrected and marked in their steps as the
    card's own. In step termination, the accounting that turns Fulton's two
    alternatives into the single quantity N + g* is the card's own and now
    says so, and its closing sentence was off by one, now at most
    N + g*(C) + 1 terms, that is at most N + g*(C) steps. In step
    positive-characteristic, the paragraph that keeps Appendix A's preliminary
    transformations from breaking the termination is the card's own, the
    appendix saying only "we can proceed as before", and it was false. It said
    that N' + g* still drops at a preliminary step. There the centre
    has multiplicity m = 0 or 1, so it is not a bad point, and (7) gives
    sum I(P_i, C' cap L) = m <= 1, so no P_i is a multiple point; hence
    N' = N, g*(C') = g*(C) by (8) with r = m and binom(m,2) = 0, and N' + g*
    is unchanged. The paragraph now says that, and takes the termination from
    it. The remark's sentence calling Rud's route the same as this one is
    corrected, since three of his arguments do not hold as printed and the
    proof uses none of the three. Read for this pass: Fulton, Algebraic
    Curves (2008), §7.4 (1) to (8), Lemma 1 and Theorem 2, printed pp. 88 to
    91, and Appendix A, printed p. 113, in the text version
    tmp/sources/fulton-2008-algebraic-curves-pp55-62-86-92-110-115.md, whose
    markers name PDF page ranges only, so the printed pages were located in
    the retained PDF: PDF p. 96 is printed 88, PDF p. 97 carries (5) and (6)
    and is printed 89, PDF p. 98 carries (7), (8) and Lemma 1 and is printed
    90, and PDF p. 99 carries Theorem 2 and is printed 91, so printed page =
    PDF page - 8; and Rud, Resolution of singularities on projective curves
    (2015), Propositions 19 to 23, Remark 23, Theorem 13 and §7.3, in
    tmp/sources/rud-2015-resolution-singularities-curves.md, whose printed
    page is its PDF page minus one: PDF p. 26 carries Proposition 19 and is
    printed 25, PDF p. 27 carries Propositions 20 and 21 and is printed 26,
    PDF p. 28 carries Proposition 22, Proposition 23 and Remark 23 and is
    printed 27, and PDF p. 29 carries Theorem 13 and is printed 28. Not read
    here: Rud's sections 6.1 to 6.3 and 7, and his Propositions 24 to 26,
    beyond the statements named above; Fulton's
    Problem 4.16 and Problem 5.26, which the Lemma 1 step cites; and the
    printed copies of either book, only the text versions beside the retained
    PDFs.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Correction to the event above, which is left as written. It says of Rud's
    Propositions 20 and 21 that they prove the sum and not the ordinariness.
    The second part of Proposition 21 does state that P, P' and P'' are
    ordinary multiple points of C' with multiplicities n, n-r and n-r, and
    that statement stands on printed p. 26. What its proof carries is the
    count: with C' in good position, (6) applied to C' and (C')' = C gives
    sum I(P_i, C cap L) = sum 1 = n = mu_P(C'), and the same for P' and P''.
    That the n tangent directions of C' at P are then simple is not derived
    there, since the equality of the sum with the multiplicity says nothing
    about how it is distributed among them, and that is the passage the card
    supplies as its own. The remark now says what the propositions prove and
    what they state, and the record of this date in COMPLAINTS.md, which says
    they prove the sum and not the ordinariness, is corrected by a record of
    the same date there.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's findings on the third round of this batch, repaired here; every
    event above is left as written. Two arguments written on this date are
    withdrawn, each being a proof of a part that no source proves. Step
    termination's accounting through N + g* was written in 188bff5ee6 and
    restated in e904d316b6 with the mark that it is the card's own; marking it
    does not make it a source's, and it is not kept. The step now states
    Fulton's Theorem 2 as printed on p. 91, quoting his two alternatives and
    his bound N + g*(C), and says that the estimate is his and is not derived
    on the card; the nonnegativity of g* his argument draws on is his Theorem 2
    of §5.4, printed p. 60, which step genus-invariant-nonnegative transcribes.
    Step positive-characteristic's interleaving paragraph is withdrawn for the
    same reason: it was written in 47d792392b and rewritten in 188bff5ee6 and
    in e904d316b6, and its mathematics is right at a preliminary step, where
    N' = N and g* is unchanged since (7) gives sum I(P_i, C' cap L) = m <= 1,
    but it is a proof written on this date of a part no source proves, Appendix
    A saying only "we can proceed as before". The step keeps Appendix A's own
    reduction, transcribed, and says that the iteration is not carried out
    there, the case being that appendix's assertion together with the citation
    Hirschfeld, Algebraic Curves over Finite Fields, Theorem 3.27, which is what
    the card carried before this round. The preamble and the qed say the same:
    characteristic 0 is proved, characteristic p is cited. Page claim
    corrected: g* is defined in the paragraph before Rüd's Remark 23, printed
    p. 27, and his Proposition 22, printed p. 27, states that it is a
    nonnegative integer, so the remark no longer says that Proposition 22
    introduces g*. Read for this pass, in the text versions: Fulton, Algebraic
    Curves (2008), Theorem 2 and its proof at lines 456 to 460 of
    tmp/sources/fulton-2008-algebraic-curves-pp55-62-86-92-110-115.md, whose
    marker "PDF pages 94-100" carries printed pp. 86 to 92, printed page =
    PDF page - 8, so Theorem 2 is on printed p. 91; and Appendix A at line 575
    of the same file, under the marker "PDF pages 118-123", printed p. 113.
    Rüd, Resolution of singularities on projective curves (2015), the definition
    of g*, Remark 23 and Proposition 22 at lines 873 to 877 of
    tmp/sources/rud-2015-resolution-singularities-curves.md, printed p. 27, the
    PDF page being the printed page plus one. The remark's claims about Rüd's
    Propositions 19 to 23 and Theorem 13 are unchanged. Not read here:
    Hirschfeld's Theorem 3.27, still not held; Fulton's Problem 4.16 and
    Problem 5.26; and any printing of either book other than the text versions
    beside the retained PDFs. The COMPLAINTS records of this date that call the
    two withdrawn arguments the card's own, and the record added to that file by
    f32e7f5159 whose lead carries no day, are corrected by records of this date
    there.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's finding of QUAL-08 on the rendered text of this card, repaired
    here; every event above is left as written, and no mathematical claim
    changes. Three passages of the public text stated what the card does or
    does not prove and how much of a source's entry the citation is, which
    belongs in COMPLAINTS.md and not on the card. The preamble no longer says
    that the bound N + g*(C) is his, that Appendix A ends by asserting the
    theorem rather than deriving it, or that Hirschfeld's theorem is the whole
    of Egbert's entry; it gives the terminating count as Fulton's Theorem 2,
    printed p. 91, the reduction in characteristic p as his Appendix A, printed
    p. 113, and the case as Hirschfeld's Theorem 3.27. Step termination's proof
    no longer says that the estimate stands as he prints it and that the card
    does not derive it: the transcription of Theorem 2 is the proof of the
    step, and the citation of Theorem 2 of §5.4, printed p. 60, for the
    nonnegativity of g* stays a citation. Step positive-characteristic no
    longer says what the appendix does not carry out, that no argument for the
    interleaved sequence is given on the card, or that Egbert's entry cites
    Hirschfeld in place of a solution: its claim states the reduction of
    Appendix A, its proof transcribes that reduction, and one sentence gives
    the case as Hirschfeld's Theorem 3.27. The qed no longer says that the step
    states what the case rests on, and step excellent-position-attained no
    longer says what the appendix does about the failure of separability in
    characteristic p. The status those passages carried is recorded in
    COMPLAINTS.md, in the record of this date for the two withdrawn arguments
    and in the record this pass adds beside it. Read for this pass: the same
    passages of
    tmp/sources/fulton-2008-algebraic-curves-pp55-62-86-92-110-115.md, lines
    456 to 460 for Theorem 2 and line 575 for Appendix A, and of
    tmp/sources/rud-2015-resolution-singularities-curves.md, lines 873 to 877;
    nothing further. Not checked here: the rendered page, and any printing of
    either book other than the text versions beside the retained PDFs.
- event: source-corrected
  by: claude
  date: 2026-11-17
  note: >-
    Markup only, no change of statement or proof. The remark on other published
    treatments quoted the National Taiwan University solution's closing
    sentence with a raw `\ldots' where the quotation elides words, and Pandoc's
    HTML writer drops raw TeX it cannot typeset, so the reader saw no ellipsis
    at all: `qualc check` reported the span as raw TeX the page cannot show.
    STYLE-04's rule that ellipses are `\ldots' governs mathematics, where an
    ellipsis is a list separator between two math atoms, and sets `\cdots'
    between binary operators; this one is punctuation inside quoted prose, and
    is now the character `…', which is how the corpus writes a prose ellipsis
    elsewhere (for example in the solution of `E-SS7.EX-8'). The quotation is
    otherwise unchanged. Not checked: the rendered page in a browser, and no
    source was re-read for this repair.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The characteristic-p case is now proved on the card, and the citation of
    Hirschfeld, Algebraic Curves over Finite Fields, Theorem 3.27 is no longer
    used anywhere in the proof. What the card had was Fulton's Appendix A,
    printed p. 113, transcribed as far as "one of the choices m = 0, 1 will
    insure that p doesn't divide n - r" together with the remark that the
    printed sentence needs n' - r where it writes n - r, and then the sentence
    "the case is Hirschfeld, Theorem 3.27". What was missing is that the
    preliminary transformation of the appendix is neutral and that it restores
    the hypothesis of Fulton's Lemma 1, so that his Theorem 2 runs in
    characteristic p unchanged. Three steps and two sentences changed: (1)
    excellent-position-attained now assumes that the projection from P is
    separable rather than that char k = 0, char 0 being the case in which every
    projection is separable, and its last paragraph says that the coprimality
    of G_lambda and G'_lambda is reducedness of the fibre of pi_P, which holds
    for all but finitely many slopes exactly under that hypothesis; (2)
    positive-characteristic now states and proves the characteristic-p case: if
    pi_P is not separable then p divides n - r, the inseparable degree being a
    power of p dividing the degree; the preliminary transformation centred at Q
    of multiplicity m in {0,1} and two points off C, with P on no fundamental
    line and the fundamental lines transverse at smooth points, sends P to a
    point of the same multiplicity r and leaves N and g* unchanged (the points
    over the centres are smooth, the three new points are ordinary, and the
    cancellation of step genus-invariant-drops applies with an empty sum over
    the centres), and deg pi_{P_1} = 2n - m - r is congruent to n - m modulo p,
    so m = 0 when p does not divide r and m = 1 when it does gives p not
    dividing that degree, hence separability; the descent then applies at P_1
    and drops N + g*, so at most 2(N + g*(C)) transformations suffice; (3) the
    termination bound is quoted in that doubled form in the step and in the
    qed, which no longer says the case is Hirschfeld's. The introductory
    paragraph of the solution and the "Published solution" remark were brought
    into line, the latter saying that Appendix A settles characteristic p once
    the neutrality of its preliminary transformation is observed. The remark
    that quotes Egbert's one-sentence pointer to Hirschfeld is unchanged: it is
    a true statement about his entry, and the card no longer depends on it.
    Checked in this pass: the congruence and the choice of m (m = 0 if
    p does not divide r, since n = r modulo p; m = 1 if p does divide r, since
    then n is 0 modulo p and n - 1 is not); that an inseparable morphism of
    curves has degree divisible by p; that the preliminary transformation
    preserves N and g*, by the same cancellation the card already carries for
    the descent step, with the sum over the points over the three centres, each
    of multiplicity at most 1; and that the descent step at P_1 then applies,
    its inputs being exactly separability at P_1 and the identity for g*.
    Gates: ./.venv/bin/python -m qualc.authoring check P-AGH543ORDINARYSING,
    "schema and Markdown parsing OK (single card)"; tmp/lam.sh, numbering the
    steps 1 to 8 with QED labels present and no unknown step label;
    tools/check_macros.py, OK. Not checked: the rendered page in a browser, and
    no source was re-read for this pass beyond Fulton's Appendix A as the card
    already transcribed it. The argument was found and checked in this session
    in a swarm of eight agents working the exercise independently, whose three
    surviving proofs (conic-pencil repair, branch-height measure, and the
    degree adjustment used here) were each checked step by step before
    transcription; the card carries the third, it being the shortest, and
    states it in the card's own words.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Independent check of step positive-characteristic, the step that makes the
    exercise proved in characteristic p, and three repairs to its citations;
    the event above is left as written and no statement or bound changes.
    Checked again from Fulton's (8) and (7), printed p. 90: the preliminary
    transformation has three new ordinary points of multiplicities n, n-m and
    n-m, so with deg C_1 = 2n-m its invariant is
    binom(2n-m-1,2) - sum binom(r_Q,2) - binom(n,2) - 2 binom(n-m,2), which
    equals g*(C) = binom(n-1,2) - sum binom(r_Q,2) exactly when
    binom(2n-m-1,2) - binom(n,2) - 2 binom(n-m,2) = binom(n-1,2) - binom(m,2),
    the identity of step genus-invariant-drops at r = m; since m is 0 or 1 the
    right-hand side is binom(n-1,2), and both sides are (n^2-m^2-3n+m+2)/2,
    which was checked at n = 3, 4, 5 for m = 0 and m = 1. The points over the
    three centres have multiplicity at most 1, so the subtracted sum is empty
    and g* is preserved; the three new points are ordinary and the old
    non-ordinary points are preserved with their multiplicities, so N is
    preserved too, which is what the doubling of Fulton's bound needs. The
    congruence n'-r congruent to n-m mod p and the choice of m (m = 0 when p
    does not divide r, m = 1 when it does, since n is then congruent to r and
    n-1 is not) are as the step states. Repairs: the claim that the projection
    from P has degree n-r was cited to step excellent-position, which does not
    state it, and is now derived from the intersection of C with a general
    line through P; the degree and multiplicity of C_1 at P_1, cited as loc.
    cit., now name step algebraic-transform-multiplicities; and the
    ordinariness of the three fundamental points, likewise cited as loc. cit.
    to a step that does not prove it, now names step excellent-position, whose
    part (b) proves exactly that passage. Read for this pass: Fulton, Algebraic
    Curves (2008), (7) and (8) and Lemma 1 on printed pp. 89-90 and Theorem 2
    on printed p. 91, and Appendix A on printed p. 113, in
    tmp/sources/fulton-2008-algebraic-curves-pp55-62-86-92-110-115.md. Not
    checked: any printing other than that text version, and no source outside
    Fulton was re-read, Hirschfeld's Theorem 3.27 no longer being used anywhere
    in the proof.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The characteristic-p step is read against Fulton's own numbered
    statements, and two of its sentences are rewritten to carry their proofs;
    no statement changes. (i) The step asserted of a terrible point that
    "then p divides n-r". Fulton states this at the head of Appendix A,
    printed p. 113, from Problem 5.26, printed p. 60, and the card gave no
    argument. The argument is now supplied: the projection from P has degree
    n-r; a separable projection has reduced general fibre, that is n-r
    distinct points; a terrible point gives a non-reduced general fibre, so
    the projection is inseparable, and the inseparable degree is a power of p
    dividing the degree. (ii) The sentence on g^* said that the cancellation
    of step genus-invariant-drops "applies verbatim with the sum taken over
    the points over the three centres". The right invocation is (8) of
    Fulton, printed p. 90: with the centre of multiplicity m = 0 or 1, the
    non-fundamental points of C_1 on the exceptional line L through the two
    centres of multiplicity 0 are the points of C on that line, smooth and
    transverse by the choice of the fundamental lines, so all r_i = 1 and the
    sum in (8) vanishes. Read for this pass, in
    tmp/sources/fulton-2008-algebraic-curves-pp55-62-86-92-110-115.md, printed
    pp. 87-91 and 113: (1) to (3), printed pp. 88-89, against step
    algebraic-transform-multiplicities; (4) and (6), printed pp. 89-90,
    against step excellent-position; (7), printed p. 90, against the
    ordinariness of P, P', P'' and the absence of non-fundamental points on
    C' cap L' and C' cap L''; (8), printed p. 90, against step
    genus-invariant-drops; Lemma 1, printed p. 90, with Problem 5.26, printed
    p. 60, against step excellent-position-attained; Theorem 2, printed p. 91,
    against step termination; and Appendix A, printed p. 113, against this
    step, including its misprint "p doesn't divide n-r" where the congruence
    needs n'-r, and the two further centres of the preparatory transformation
    being off C, which the card states and Fulton leaves implicit. Not
    checked: any printing other than that text version, and Problem 4.16, to
    which Lemma 1 defers the change of coordinates.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Page correction to the event immediately above, and no change of
    mathematics. That event gave (1) to (3) as printed pp. 88-89 and (4) and
    (6) as printed pp. 89-90. Checked page by page in the retained PDF, whose
    folios stand at the foot of each page: PDF p. 96 carries folio 88 and the
    statements (1), (2), (3) and (4); PDF p. 97 is the next page, printed
    p. 89, and carries (5) and (6); PDF p. 98 carries folio 90 and the
    definition of excellent position, (7), (8) and Lemma 1; PDF p. 99 is
    printed p. 91 and carries Theorem 2. The correct attributions are (1) to
    (4) on printed p. 88, (5) and (6) on p. 89, (7), (8) and Lemma 1 on
    p. 90, and Theorem 2 on p. 91, which is what the card's steps already
    cite. Read for this: the folios of
    tmp/sources/fulton-2008-algebraic-curves.pdf at PDF pp. 96-100. Not
    checked: any printing other than that PDF.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Page locators are removed from the rendered text, the citation rule of
    CONTRIBUTING requiring numbered statements. Deleted, with the numbered statement
    kept in each case: "printed p. 113" at Fulton's Appendix A, twice, in step
    positive-characteristic and in the remark; "printed p. 88" for (1), (2) and (3),
    for (4), and for the formulas of section 7.4; "printed p. 89" for (5) and for
    (6); "printed p. 90" for (7), for (8) twice, and for Lemma 1; "printed
    pp. 88--90" for (4) to (7); "printed p. 60" for Problem 5.26 and for Theorem 2
    of section 5.4; "printed p. 91" for Theorem 2 of section 7.4; and "printed
    p. 87" for the standard quadratic transformation. The audit events above are not
    edited, and the pages they name remain the record of what was read. Not checked:
    the rendered page, and no printing of Fulton other than the text version
    retained in tmp/sources.
- event: source-checked
  by: claude
  date: 2026-11-22
  note: >-
    Published-solution pass for issue #160, on the transcription rule. The
    exercise's characteristic-p case is proved by Fulton's Appendix A together
    with the neutrality of its preliminary transformation, and by no retained
    Hartshorne solution set; the "Other published treatments" remark now says
    so and names the sets searched. Read in this pass, at their own numbering:
    the printed exercise in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    where the number is garbled to "4.." and the wording is the card's
    statement; Yang Pi-Yeh, Solution 5.4.3, which chooses the two auxiliary
    points, shows the image point is on neither fundamental line and has
    smaller multiplicity, and stops, separating no characteristic; Egbert,
    Exercise V.4.3, which is the sentence citing Hirschfeld's Theorem 3.27;
    the National Taiwan University Chapter V §4 Exercise 3, by Shuang-Yen Lee,
    whose local computation through the chart x = (t+mu)y ends "induction on
    this then we are done" and asserts that the blown-down singularities are
    ordinary without proving it; and, for absence, the retained sets carrying
    no Chapter V §4 exercise, Borcherds (through IV.1), Cais (through Chapter
    4), Cutrone--Marshburn (Chapters 1 and 2), Ionita--Kumar (Chapter I), Kim
    (§2.4), Lomont, Okamoto (§II.9), Park (Chapter 4 and §V.5), Saglam--Chris (Chapter III),
    Sam (through IV.6), Stein (III.7), Troiani (Chapter II) and Reiser
    (IV.2.5). The remark now states that only those three retained sets contain
    the exercise, that each is incomplete, and that the two passages the card
    supplies itself are the ordinariness at step excellent-position and the
    neutrality for N and g*. No statement and no proof step changed in this
    pass. Not read: Hirschfeld's tract, still not held; any printing of Fulton
    or Hartshorne, only the text versions in tmp/sources.
- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    One sentence of step positive-characteristic, part (iii), repaired, with no
    change of mathematics and no change to any other step. It said that the
    non-fundamental points of C_1 cap L, L the exceptional line through the two
    centres of multiplicity 0, "are the points of C cap L", hence of
    multiplicity 1. That identifies the wrong points: L is contracted by the
    transformation, and by (7)(c) of Fulton §7.4 the sum of the intersection
    multiplicities at the non-fundamental points of C_1 cap L is mu_Q(C_1) = m,
    the multiplicity of the centre Q, so there is at most one such point and
    its multiplicity is at most 1; the sum (8) subtracts vanishes either way,
    which is what the step needs. The sentence now says that. Read for it:
    (6), (7) and (8) of Fulton §7.4 in
    tmp/sources/fulton-2008-algebraic-curves-pp55-62-86-92-110-115.md, and the
    clause of step excellent-position that transcribes (7)(c). Not read: any
    printing of Fulton, only the text version.
---

::: {.problem}
Let $C$ be an irreducible curve in $\PP^2$.
Then there exists a finite sequence of quadratic transformations, centered at suitable triples of points, so that the strict transform $C^{\prime}$ of $C$ has only ordinary singularities, i.e., multiple points with all distinct tangent directions (I, Ex.
5.14). Use (3.8).
:::

::: {.solution}
Let $C\subseteq\PP^2$ be an irreducible curve of degree $n$, and for a point $Q$ of the plane write $r_Q=\mu_Q(C)$ for the multiplicity of $C$ at $Q$. A point is *bad* if it is not an ordinary multiple point, that is, if its tangent cone is not a product of distinct lines, each with multiplicity one; the exercise asks for a finite sequence of quadratic transformations after which the strict transform has no bad point.

The argument is that of Fulton, *Algebraic Curves* (2008), §7.4, with Appendix A of that book, for a field of positive characteristic. It takes successive quadratic transformations, each centred at a bad point of the current curve, and follows the invariant
$$
g^*(C)=\binom{n-1}{2}-\sum_{Q}\binom{r_Q}{2},
$$
the sum being taken over the multiple points of $C$. The terminating count is Fulton's Theorem 2: a curve with $N$ non-ordinary multiple points reaches one whose singularities are all ordinary after at most $N+g^*(C)$ steps. In characteristic $p>0$ the reduction is that of his Appendix A, and it is not a reduction to another theorem: the preliminary transformation it prescribes is neutral for $N$ and for $g^*$, and it restores the separability that the count needs, so the same count runs in every characteristic with the bound doubled.

::: pf

::: {.pf-step #algebraic-transform-multiplicities}
Set
$$
Q([x:y:z])=[yz:xz:xy],
$$
the standard quadratic transformation, with fundamental points
$$
P=[0:0:1],
\qquad
P'=[0:1:0],
\qquad
P''=[1:0:0]
$$
and exceptional lines
$$
L=V(Z),
\qquad
L'=V(Y),
\qquad
L''=V(X).
$$
A quadratic transformation is $Q\circ T$ for a projective change of coordinates $T$, and it is centred at the three points $T^{-1}(P)$, $T^{-1}(P')$, $T^{-1}(P'')$. For an irreducible $C$ with equation $F$ of degree $n$, and
$$
r=\mu_P(C),
\qquad
r'=\mu_{P'}(C),
\qquad
r''=\mu_{P''}(C),
$$
put
$$
F^Q=F(yz,xz,xy),
\qquad
F^Q=Z^{r}Y^{r'}X^{r''}F'.
$$
Then
$$
\deg F'=2n-r-r'-r'',
\qquad
\mu_P(C')=n-r'-r'',
$$
with the symmetric formulas $\mu_{P'}(C')=n-r-r''$ and $\mu_{P''}(C')=n-r-r'$; $F'$ is irreducible, $(F')'=F$, and $C'=V(F')$ is the strict transform of $C$.

::: pf-proof
This is the opening of Fulton, §7.4, with (1), (2) and (3) of that section. On $U=\PP^2-V(XYZ)$ the map $Q$ is its own inverse, so $Q$ is a birational map of $\PP^2$ with itself, and $C'=\overline{Q^{-1}(C\cap U)}$.

For (1), write $F=F_r(X,Y)Z^{n-r}+\cdots+F_n(X,Y)$ with $F_i$ a form of degree $i$; substituting $YZ$, $XZ$, $XY$ for $X$, $Y$, $Z$ gives
$$
F^Q=Z^{r}\bigl(F_r(Y,X)(XY)^{n-r}+ZF_{r+1}(Y,X)(XY)^{n-r-1}+\cdots\bigr),
$$
so $Z^{r}$ is the largest power of $Z$ dividing $F^Q$, and the same computation at $P'$ and $P''$ gives the factors $Y^{r'}$ and $X^{r''}$. These are coprime, because $F$ is irreducible and is not one of the exceptional lines, so $F^Q=Z^{r}Y^{r'}X^{r''}F'$ with $\deg F'=2n-r-r'-r''$.

For (2), $(F^Q)^Q=(XYZ)^nF$, whence $F'$ is irreducible and $(F')'=F$; and $V(F')$ contains $Q^{-1}(C\cap U)$, so by irreducibility it is $C'$.

For (3), Fulton rewrites
$$
F'=\sum_{i=0}^{n-r}F_{r+i}(Y,X)\,X^{n-r-r''-i}\,Y^{n-r-r'-i}\,Z^{i},
$$
all of whose terms have degree at least $n-r'-r''$ at $P=[0:0:1]$, the term $i=n-r$ attaining it; the leading form of $F'$ at $P$ is therefore $F_n(Y,X)X^{-r''}Y^{-r'}$, of degree $n-r'-r''$. The two other formulas follow by symmetry.
:::

:::

::: {.pf-step #excellent-position}
Call $C$ in *good position* if no exceptional line is tangent to $C$ at a fundamental point, and in *excellent position* if in addition $L$ meets $C$ transversally in $n$ distinct non-fundamental points and $L'$ and $L''$ each meet $C$ transversally in $n-r$ distinct non-fundamental points. If $C$ is in excellent position, then $r'=r''=0$, so $\deg C'=2n-r$ and
$$
\mu_P(C')=n,
\qquad
\mu_{P'}(C')=\mu_{P''}(C')=n-r,
$$
these three points being ordinary multiple points of $C'$; every multiple point of $C$ away from the three exceptional lines is a multiple point of $C'$ of the same multiplicity, ordinary or not as before; there is no non-fundamental point on $C'\cap L'$ or on $C'\cap L''$; and the non-fundamental points $P_1,\ldots,P_s$ of $C'\cap L$ satisfy
$$
\mu_{P_i}(C')\le I(P_i,C'\cap L),
\qquad
\sum_{i=1}^{s}I(P_i,C'\cap L)=r.
$$

::: pf-proof
This is (7) of Fulton. In excellent position the points of $C\cap L'$ and of $C\cap L''$ are non-fundamental, so $P'\notin C$ and $P''\notin C$, that is $r'=r''=0$; step [](#algebraic-transform-multiplicities){.pf-ref} then gives the degree $2n-r$ and the three multiplicities.

Part (a) of (7) follows because $C'\cap U$ and $C\cap U$ are isomorphic. Part (c) is (6) of the same section, whose computation is
$$
\sum_{i=1}^{s}I(P_i,F'\cap Z)=\sum_{i=1}^{s}I(P_i,F_r(Y,X)\cap Z)=r
$$
and which gives $\mu_{P_i}(C')\le I(P_i,C'\cap L)$; applied with $P'$ and with $P''$ in the role of the centre, (6) says that the analogous sum equals $r'=0$ and $r''=0$, so there is no non-fundamental point on $C'\cap L'$ or on $C'\cap L''$.

Part (b) is the case in which the reading is not immediate. Fulton obtains it by "applying (6) to the curves $C'$ and $(C')'=C$", which is legitimate because $C'$ is in good position by (4); what that application gives is the count $\mu_P(C')=n$, the left-hand side of (6) being $\sum_i I(P_i,C\cap L)$ over the $n$ points $P_i$ of $C\cap L$, at each of which $L$ meets $C$ transversally and the intersection multiplicity is therefore $1$. The step from that count to the ordinariness of the three fundamental images is the card's own, and reads the local model (5) with $C'$ in the role of the curve there: the points of $C\cap L$ are the points in which the strict transform of $C'$ under the blowup of $P$ meets the exceptional curve $L$, and they correspond one to one to the tangent directions of $C'$ at $P$, the exponent of a direction in the tangent cone of $C'$ at $P$ being the intersection multiplicity of $C$ with $L$ at the corresponding point. Those $n$ exponents are $n$ positive integers with sum $\mu_P(C')=n$, so all are $1$; the tangent cone of $C'$ at $P$ is therefore a product of $n$ distinct lines, and $P$ is an ordinary $n$-fold point. The same reading with $P'$ and with $P''$ in the role of the centre gives $\mu_{P'}(C')=\mu_{P''}(C')=n-r$, ordinary there too.
:::

:::

::: {.pf-step #excellent-position-attained}
Let $F$ be irreducible and let $P\in F$ be a point whose projection $\pi_P$ is separable. Then there is a projective change of coordinates $T$ such that $F^T$ is in excellent position and $T([0:0:1])=P$. In characteristic $0$ the hypothesis is automatic, every projection from a point being separable.

::: pf-proof
This is Lemma 1 of Fulton, §7.4, and its input is Problem 5.26 of the same book: for an irreducible curve of degree $n$ over a field of characteristic $0$ and a point $P$, all but finitely many lines through $P$ meet $C$ in $n-r$ distinct points other than $P$. Fulton's proof of the lemma chooses lines
$$
L'\cdot C=rP+P'_{r+1}+\cdots+P'_n,
\qquad
L''\cdot C=rP+P''_{r+1}+\cdots+P''_n,
\qquad
L\cdot C=P_1+\cdots+P_n,
$$
with all the named points distinct, and then a change of coordinates carrying $L$, $L'$, $L''$ to $Z$, $Y$, $X$; the last step he defers to Problem 4.16 of the book.

Problem 5.26 is outlined there in three parts: take $P=[0:1:0]$, as one may after a projective change of coordinates, and the lines $L_\lambda=\{[\lambda:t:1]\}\cup\{P\}$, and write
$$
F=A_r(X,Z)Y^{n-r}+\cdots+A_n(X,Z),
\qquad
A_r\neq0;
$$
then $G_\lambda(t)=F(\lambda,t,1)$ has degree $n-r$ whenever $A_r(\lambda,1)\neq0$, which fails for only finitely many $\lambda$; and $G_\lambda$ has $n-r$ distinct roots whenever in addition $F\cap F_Y\cap L_\lambda=\{P\}$, that is, whenever $G_\lambda$ and its derivative have no common root on $L_\lambda$, which again fails for only finitely many $\lambda$ because $F$ and $F_Y$ have no common component. In characteristic $0$ that is the whole condition, the coprimality of $G_\lambda$ and $G'_\lambda$ being reducedness of the fibre of $\pi_P$ over the slope $\lambda$; in characteristic $p$ it is not, and the hypothesis of this step is exactly that the coprimality holds for all but finitely many $\lambda$, that is, that the generic fibre of $\pi_P$ is reduced. Step [](#positive-characteristic){.pf-ref} arranges that hypothesis at a point where it fails, by a preliminary transformation.
:::

:::

::: {.pf-step #genus-invariant-nonnegative}
$g^*(C)$ is a nonnegative integer.

::: pf-proof
The sum is an integer. Fulton, Theorem 2 of §5.4, proves
$$
\sum_{Q}\binom{r_Q}{2}\le\binom{n-1}{2}
$$
for an irreducible plane curve of degree $n$, by counting the conditions that a form $G$ of degree $n-1$ is made to satisfy at the multiple points of $C$ and at further simple points of $C$, applying Corollary 1 of Bézout to $C$ and $G$, and reading the resulting inequality backwards. Rüd's Proposition 22, states the same nonnegativity, but its first case, $\partial F/\partial z\ne0$, applies Bézout to $F$ and $\partial F/\partial z$ and gets only $\sum_Q r_Q(r_Q-1)\le n(n-1)$, which gives $g^*(C)\ge-(n-1)$ and not $g^*(C)\ge0$; the nonnegativity used here is Fulton's.
:::

:::

::: {.pf-step #genus-invariant-drops}
If $C$ is in excellent position then
$$
g^*(C')=g^*(C)-\sum_{i=1}^{s}\binom{r_i}{2},
\qquad
r_i=\mu_{P_i}(C'),
$$
where $P_1,\dots,P_s$ are the non-fundamental points of $C'\cap L$. In particular $g^*(C')\le g^*(C)$, with equality exactly when no $P_i$ has multiplicity at least $2$.

::: pf-proof
This is (8) of Fulton, whose proof is given there as "a calculation, using (2) and (7)"; the calculation is the following. By step [](#excellent-position){.pf-ref} the multiple points of $C'$ are the multiple points $Q\neq P$ of $C$ with their multiplicities, the three ordinary points $P$, $P'$, $P''$ of multiplicities $n$, $n-r$, $n-r$, and the points $P_i$ of multiplicities $r_i$. With $\deg C'=2n-r$ this gives
$$
g^*(C')=\binom{2n-r-1}{2}-\sum_{Q}\binom{r_Q}{2}-\binom{n}{2}-2\binom{n-r}{2}-\sum_{i=1}^{s}\binom{r_i}{2},
$$
while
$$
g^*(C)=\binom{n-1}{2}-\sum_{Q}\binom{r_Q}{2}-\binom{r}{2},
$$
the sum over $Q$ running over the multiple points of $C$ other than $P$ in both displays. The two differ by the last sum alone, because
$$
\binom{2n-r-1}{2}-\binom{n}{2}-2\binom{n-r}{2}=\binom{n-1}{2}-\binom{r}{2},
$$
both sides of which are $\tfrac12(n^2-r^2-3n+r+2)$, as $2\binom{k}{2}=k(k-1)$ shows. Since $\binom{r_i}{2}\ge0$, with equality exactly when $r_i\le1$, the statement follows.
:::

:::

::: {.pf-step #termination}
Let $N$ be the number of non-ordinary multiple points of $C$. Then a finite sequence of quadratic transformations, of length at most $N+g^*(C)$, carries $C$ to a curve whose only singularities are ordinary multiple points.

::: pf-proof
This is Fulton, Theorem 2 of §7.4. He takes successive quadratic transformations, centring each one at a non-ordinary multiple point, and observes from (7) and (8) of the same section that "at each step, either $C'$ has one less non-ordinary multiple point than $C$, or $g^*(C')=g^*(C)-\sum_i\frac{r_i(r_i-1)}{2}<g^*(C)$", the second alternative being (8) in the form step [](#genus-invariant-drops){.pf-ref} states it, with $r_i=\mu_{P_i}(C')$, and concluding that "if the original curve $C$ has $N$ non-ordinary multiple points, we reach the desired curve after at most $N+g^*(C)$ steps". The nonnegativity of $g^*$ that his argument uses is his Theorem 2 of §5.4, which step [](#genus-invariant-nonnegative){.pf-ref} transcribes.
:::

:::

::: {.pf-step #positive-characteristic}
Assume $\operatorname{char}k=p>0$. Then the transformation sequence of step [](#termination){.pf-ref} exists in this characteristic, at most $2(N+g^*(C))$ transformations sufficing: where the projection from the chosen point is inseparable, one preliminary quadratic transformation, centred at a point of multiplicity $0$ or $1$ and two points off $C$, changes neither $N$ nor $g^*$, creates only ordinary points, and makes the projection from the image of that point separable.

::: pf-proof
This is Appendix A of Fulton. Call $P$ *terrible* for $F$ if infinitely many lines through $P$ meet $C$ in fewer than $n-r$ distinct points other than $P$. A terrible $P$ forces $p\mid(n-r)$: the projection $\pi_P\colon C\to\PP^1$ has degree $n-r$, a general line through $P$ meeting $C$ in $P$ with multiplicity $r$ and in $n-r$ further points counted with multiplicity; if $\pi_P$ were separable its general fibre would consist of $n-r$ distinct reduced points, whereas a terrible $P$ has non-reduced fibres over infinitely many lines, so the general fibre is not reduced and $\pi_P$ is not separable, and the inseparable degree of a finite morphism of curves is then a power $p^e>1$ dividing its degree $n-r$. Fulton states this at the head of Appendix A, "P can only be terrible if $p$ divides $n-r$", from Problem 5.26. The lines through $P$ form a line of the dual plane, so for a terrible $P$ the dual curve of $C$ contains infinitely many points of a line and, being irreducible, is that line; hence $F$ has at most one terrible point, and lines meeting $C$ in $n$ distinct points always exist.

If the chosen bad point $P$ is terrible for $F$, Fulton takes a quadratic transformation centred at a point $Q$ of multiplicity $m=0$ or $m=1$, so that $P$ lies on no fundamental line, and writes $F'$ for the transform; the two remaining centres are taken off $C$, so that $n'=\deg F'=2n-m$. Since $p$ divides $n-r$,
$$
n'-r\equiv 2n-m-r\equiv n-m \pmod p,
$$
and one of the choices $m=0$, $m=1$ makes $p$ not divide $n-m$, hence not divide $n'-r$. The transformation is an isomorphism near $P$, so the multiplicity of $P$ on $F'$ is still $r$, and the point of $F'$ corresponding to $P$ is therefore not terrible for $F'$.

By step [](#excellent-position-attained){.pf-ref} excellent position at $P$ is available exactly when the projection $\pi_P$ from $P$ is separable; what the appendix above supplies is the transformation that produces that hypothesis when it fails. If $\pi_P$ is not separable then $p\mid(n-r)$: a general line through $P$ meets $C$ in $P$ with multiplicity $r$ and in $n-r$ further points counted with multiplicity, so $\pi_P$ has degree $n-r$, and the inseparable degree of $\pi_P$ is a power $p^e>1$ dividing that degree. Choose the preliminary transformation $T$ of the paragraph above, centred at $Q$ of multiplicity $m\in\{0,1\}$ and two points off $C$, with $P$ on no fundamental line, no fundamental line containing a singular point of $C$ other than $Q$, and every fundamental line meeting $C$ transversally at smooth points; write $C_1=T(C)$ and $P_1=T(P)$. Then:

(i) $P$ is not a fundamental point and lies on no fundamental line, so $T$ is an isomorphism near $P$, and $P_1$ has multiplicity $r$ and the singularity of $P$ (step [](#algebraic-transform-multiplicities){.pf-ref}).

(ii) $\deg C_1=2n-m$ and $\mu_{P_1}(C_1)=r$ (step [](#algebraic-transform-multiplicities){.pf-ref}), so $\deg\pi_{P_1}=2n-m-r\equiv n-m\pmod p$. Since $p\mid(n-r)$, the choice $m=0$ when $p\nmid r$ and $m=1$ when $p\mid r$ gives $p\nmid(n-m)$, hence $p\nmid\deg\pi_{P_1}$; and an inseparable morphism of curves has degree divisible by $p$. So $\pi_{P_1}$ is separable.

(iii) The points of $C_1$ over $Q$ are smooth, $m$ being $0$ or $1$; the three fundamental points of $C_1$ are ordinary multiple points of multiplicities $n$, $n-m$ and $n-m$, the fundamental lines meeting $C$ transversally at smooth points (step [](#excellent-position){.pf-ref}); and $T$ is an isomorphism near every other point of $C$, all singular points other than $P$ being off the fundamental lines by construction. Hence the non-ordinary points of $C_1$ are exactly those of $C$ other than $P$, together with $P_1$: $N(C_1)=N(C)$. For $g^*$, apply (8) of Fulton in the form step [](#genus-invariant-drops){.pf-ref} states it, to the curve $C_1$ in excellent position: by (7)(c) of the same section the sum $\sum_iI(P_i,C_1\cap L)$ over the non-fundamental points of $C_1\cap L$ is the multiplicity $\mu_Q(C_1)=m$ of the centre, which is $0$ or $1$, so at most one such point occurs, its intersection multiplicity is $1$, and hence its multiplicity $r_i$ is at most $1$; the sum $\sum_i\binom{r_i}{2}$ of (8) therefore vanishes, and $g^*(C_1)=g^*(C)$.

So $(C_1,P_1)$ has the numbers $N$ and $g^*$ of $(C,P)$, the singularity of $P$, and a separable projection at $P_1$; the descent step of steps [](#excellent-position-attained){.pf-ref} and [](#genus-invariant-drops){.pf-ref} then applies at $P_1$ and drops $N+g^*$ by at least $1$, as step [](#termination){.pf-ref} records. Each descent step is preceded by at most one preliminary transformation, so at most $2(N+g^*(C))$ quadratic transformations suffice, $N+g^*$ being a non-negative integer by step [](#genus-invariant-nonnegative){.pf-ref}. No theorem for characteristic $p$ beyond this count is used: the preliminary transformation is the one Fulton prescribes in Appendix A, and the only thing added here is that it is neutral for $N$ and $g^*$ and that it restores the hypothesis of step [](#excellent-position-attained){.pf-ref}.

The appendix's sentence on the choice of $m$ reads "one of the choices $m=0,1$ will insure that $p$ doesn't divide $n-r$", with $n-r$ where the congruence requires $n'-r$; the divisibility it needs is that of $n'-r$, and $n-r$ is divisible by $p$ by the first paragraph.
:::

:::

::: pf-qed
Steps [](#algebraic-transform-multiplicities){.pf-ref} and [](#excellent-position){.pf-ref} compute the multiplicities of a quadratic transform and of the multiple points it creates or preserves. Step [](#excellent-position-attained){.pf-ref} puts the current curve in excellent position at the chosen centre in characteristic $0$, and step [](#positive-characteristic){.pf-ref} treats the failure of that in characteristic $p>0$. Step [](#termination){.pf-ref} iterates the transformation finitely many times, with Fulton's bound, and the strict transform that results has no bad point, that is, only ordinary multiple points. This proves the exercise over an algebraically closed field of characteristic $0$; in characteristic $p>0$ the same descent applies, the preliminary transformation of step [](#positive-characteristic){.pf-ref} restoring the separability that step [](#excellent-position-attained){.pf-ref} needs, at the cost of doubling the bound. The hint (3.8) is not used: the proof resolves no curve by point blowups, terminating instead on the count of bad points against $g^*$.
:::

:::
:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.4, exercise 4.3, and its notion of ordinary singularity is that of (I, Ex. 5.14).

The proof is William Fulton, *Algebraic Curves: An Introduction to Algebraic Geometry* (2008), §7.4 "Quadratic Transformations": the standard quadratic transformation, the formulas (1), (2) and (3), good and excellent position with (4) to (7), the invariant $g^*$ and (8), Lemma 1, resting on Problem 5.26 and on Theorem 2 of §5.4, Theorem 2 of §7.4, and Appendix A "Nonzero Characteristic". Appendix A is where the characteristic-$p$ case is settled, once it is observed that the preliminary transformation Fulton prescribes there is neutral for $N$ and for $g^*$ and restores the hypothesis of his Lemma 1: that observation is step [](#positive-characteristic){.pf-ref}, and with it his Theorem 2 runs unchanged in every characteristic.

Thomas Rüd, *Resolution of singularities on projective curves* (2015), treats the same theorem: Proposition 19, states excellent position; Propositions 20 and 21, prove the sum $\sum_i I(P_i,C'\cap L)=n$ and the multiplicities $n$, $n-r$, $n-r$, and Proposition 21 states the ordinariness of $P$, $P'$ and $P''$ in its second part while its proof reaches only those multiplicities, so that passage stays the card's own; the invariant $g^*$ is defined in the paragraph before his Remark 23, and Proposition 22, states that it is a nonnegative integer; Theorem 13, gives the finite sequence; and §7.3, treats a field of positive characteristic. Three of its arguments do not hold as printed, and the proof above uses none of the three: Proposition 19 infers from the irreducibility of $F$ that the section $G_\lambda$ is irreducible and therefore has no multiple root, which does not follow --- an irreducible polynomial over an algebraically closed field is linear. Theorem 13 uses Remark 23, which says that an ordinary multiple point contributes nothing to $g^*$, whereas an ordinary double point contributes $1$. And Proposition 22's first case, $\partial F/\partial z\ne0$, reaches only $\sum_Q r_Q(r_Q-1)\le n(n-1)$.
:::

::: {.remark title="Other published treatments"}
Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 3 of §4, chooses the two auxiliary points through the bad point and analyses the multiplicity at the image point in the chart $x=(t+\mu)y$; its case analysis ends "if there's a $k$ such that $e'_k+k=e$ since we can factor into linear equations such that every direction has multiplicity less than $e$ … induction on this then we are done", and it does not show that the three contracted points are ordinary.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.4.3, states the termination criterion: with $P_2,P_3$ chosen so that $P_1P_i$ meets $C$ transversally at $P_1$, the image point $R_i$ lies on neither fundamental line and $\mu(R_i)<\mu(P_1)$, so the process stops. It does not show that the images at the three contraction points are ordinary, and it separates no characteristic.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.4.3, is the single sentence "See Algebraic Curves over Finite Fields by Hirschfeld, Theorem 3.27".

No retained solution set proves the exercise, in any characteristic, so the proof above is the
card's own wherever it goes beyond Fulton and Rüd. Of the retained sets only the three named in this
remark contain Exercise V.4.3 at all, and each of them is incomplete: the National Taiwan University
set does not show that the three contracted points are ordinary, Yang Pi-Yeh's entry proves the
termination criterion alone and separates no characteristic, and Egbert's entry is a citation of a
book that is not held and was not read. The other retained sets carry no Chapter V §4 exercise:
Borcherds, Cais, Cutrone--Marshburn, Ionita--Kumar, Kim, Lomont, Okamoto, Park, Saglam--Chris, Sam, Stein,
Troiani and Reiser. The two passages the card supplies itself are the ordinariness of the three
fundamental images in step [](#excellent-position){.pf-ref}, where Rüd's Proposition 21 states it and
its proof reaches only the multiplicities, and the neutrality for $N$ and $g^*$ of the preliminary
transformation of Fulton's Appendix A in step [](#positive-characteristic){.pf-ref}, where the
appendix says only that one may then proceed as before.
:::
