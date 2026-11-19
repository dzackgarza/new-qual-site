---
schema: qual/card@1
id: P-AGH67PUNCTUREDLINE
kind: problem
title: The number of punctures of $\AA^1 \sm \theset{P_1, \ldots, P_r}$ is an isomorphism invariant
classification:
  areas:
  - algebraic-geometry
  topics:
  - Automorphisms
  - Affine Varieties
  - Nonsingular Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.6.7 and the preceding automorphism exercise I.6.6 in the Hartshorne source. The proof computes the unit group of a punctured affine line and also extends any isomorphism to P^1, giving the sharper projective-equivalence criterion and the cross-ratio obstruction to the converse.
- event: solution-written
  by: chatgpt
  date: 2026-09-18

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.6.7, printed
    p. 47. Published treatment located outside the twelve retained sets:
    A. Shichijo, Solutions to Hartshorne's Algebraic Geometry, Chapter 1
    section 6, Exercise 6.7, printed pp. 5--6 of
    tmp/sources/shitijyou-ch1-section6.pdf. For the r = s direction the source
    embeds A^1 in P^1, extends the isomorphism to a birational map P^1 to P^1,
    which is an automorphism by Exercise I.6.8, and concludes
    phi-bar({P_i}) = P^1 - phi-bar(P^1 - {P_i}) = {Q_j}, so r = s; that is the
    card's step r-equals-s by a different route, the card using the unit group
    of the coordinate ring, which is also what the same file's Exercise 6.6(c)
    computation of Aut k(x) = PGL(1) supplies. On the converse the source is not
    a proof: it observes that an element of PGL(1) is determined by the images of
    three points and then says that since A^1 is infinite one can choose
    {P_i}, {Q_j} not carried to each other by any element, which is the claim at
    issue and needs an invariant of four points; its footnote replaces the
    argument by a configuration in A^3. The card's counterexample, the four-point
    sets {inf,0,1,lambda} and {inf,0,1,mu} with mu outside the six cross-ratio
    transforms of lambda, is therefore still the only complete argument the
    search produced, and the converse half stays without a published proof.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Step r-equals-s now carries the source's route as a paragraph after the
    card's unit-group proof, in Shichijo's own words as far as the two set
    identities go and with the missing infinity written in; the card's proof is
    unchanged, no step is transcribed from the source, and the converse keeps the
    card's cross-ratio obstruction because the source's version is an assertion.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    The closing paragraph of the published-solution remark was wrong about the
    extension automorphism and is corrected. It said that the automorphism of P^1
    produced in the step carries infinity to infinity, and inferred that the
    finite set it moves has r+1 elements. What the step proves is that the
    automorphism carries the (r+1)-point set {infinity} union P bijectively onto
    {infinity} union Q; it need not fix infinity, and the statement of the step
    (printed as the two (r+1)-point subsets) already says so. The conclusion is
    unchanged and now rests on the right statement: an isomorphism of the
    punctured lines requires those two (r+1)-point subsets to be in one
    PGL(2)-orbit, and for r = 3 they are four-point sets, where step
    converse-fails' cross ratio separates them. Checked against Borcherds p. 8,
    Egbert p. 55 and Cutrone--Marshburn p. 25: all three state the threshold
    r <= 3, which is what makes the count matter.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121. Step converse-fails now proves what it
    used to assert: that an element of PGL(1) fixing infinity, 0 and 1 is the
    identity, hence that an element is determined by three values, hence
    invariance of the cross ratio, and then the six values of the orderings
    from the three transposition computations (ab), (ac) and (cd), which
    generate the orderings and give the substitutions 1/lambda and 1-lambda.
    The threshold for the converse is r <= 2, not r <= 3: the retained sets'
    r <= 3 is one too high because the four-point sets of step converse-fails
    are already separated by the cross ratio. Vakil, The Rising Sea
    (21 October 2025), text version
    tmp/sources/vakil-rising-sea-2025-10-21.md, prints the uniqueness of the
    normalizing automorphism in 19.9.7 (line 13770) and the six values in
    (19.9.7.1) (line 13797); his Exercise 19.9.B (line 13774) leaves the
    classification of four ordered points, and Exercise 19.9.C the S_4 action
    on the cross ratio, to the reader. Not checked in this pass: the card's
    own proof of r = s, which the reader accepted, and the Math Stack Exchange
    search for a thread on the converse, which the reader ran and which agrees
    with the record kept in COMPLAINTS.md.
- event: source-corrected
  by: claude
  date: 2026-11-17
  note: >-
    Reader's report on issue #121, third pass, one mislabel and no change of
    mathematics. The 2026-11-16 note above names the three transpositions
    (ab), (ac) and (cd); the second of the three computations is not (ac). The
    orderings computed are [b,a,c,d], which is (ab), then [a,c,b,d], which is
    (bc), then [a,b,d,c], which is (cd), and the three adjacent transpositions
    (ab), (bc), (cd) generate the orderings. The 2026-11-16 note is left as
    written, since a dated event is a record of its date; the solution now
    names (bc), and the three values 1/lambda, 1-lambda and 1/lambda, with the
    normalizing maps that produce them, are unchanged and were re-read. The
    invariance of the cross ratio, the six-value orbit and the threshold r <= 2
    are as the reader accepted them.
- event: source-corrected
  by: claude
  date: 2026-11-17
  note: >-
    Four further repairs on the same pass, none of them on the reader's list.
    First, and the only mathematical one: the invariance of the cross ratio was
    proved with the wrong composite. The normalizing transformation of the
    definition of [phi a, phi b, phi c, phi d] is the unique element carrying
    phi a, phi b, phi c to infinity, 0, 1, and that is rho o phi^{-1}, not
    rho o phi: rho o phi carries phi^{-1}a, phi^{-1}b, phi^{-1}c there and
    equals rho only when phi is the identity. Step converse-fails now says so
    and concludes [phi a, phi b, phi c, phi d] = rho(d) = [a,b,c,d] directly.
    The invariance itself, the six values and r <= 2 are unchanged, and the
    reader accepted all three.
    Second, the paragraph of the published-solution remark that begins "All
    three retained sets" follows five named sources, the last three of which
    are Egbert, Cutrone--Marshburn and Shichijo, and Shichijo states no
    threshold; the three meant are Borcherds, Egbert and Cutrone--Marshburn
    and they are now named.
    Third, the quotation from Cutrone--Marshburn on PDF p. 25 was punctuated
    as the card needed it: its text version
    tmp/sources/hartshorne-solutions-cutrone-marshburn.md, line 425, reads
    "under Aut P^1 . Any isomorphism between P^1 and P^1 fixes at most 2
    points", and the card had turned the full stop into a semicolon and the
    capital into a lower-case letter inside quotation marks. Restored.
    Fourth, the line of COMPLAINTS.md that records this card's converse said
    that all located sets state a threshold; Shichijo asserts the converse
    without one, and the three that do state it state it as r <= 3, which the
    card refutes at r = 3. The line now names them.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Record of a date, on the reader's report of issue #121's fourth pass. The
    two events above are dated 2026-11-17 and were written and committed on
    2026-11-16: the (bc) mislabel in a9d902a1a9 (committer date 2026-11-16
    07:15:38), and the four repairs of the (ab), (bc), (cd) computation, the
    normalizing composite rho o phi^{-1}, the three retained sets and the
    Cutrone--Marshburn punctuation in 27598ae933 (2026-11-16 07:30:29). A
    record carries the day of the commit that lands it, so 2026-11-16 is
    their date. They are left unedited, as dated events must be, and their
    content stands: the three transpositions are (ab), (bc), (cd), the
    normalizing map of [phi a, phi b, phi c, phi d] is rho o phi^{-1}, and the
    threshold line and the quotation are as they state. This event is the
    record of the dates, and nothing else on the card changed.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, fifth pass: two dates, no mathematics. The
    two source-corrected events above are dated 2026-11-17, a day that had not
    happened when they were written and committed: the (bc) mislabel in
    a9d902a1a9 (committer date 2026-11-16 07:15:38) and the four further
    repairs in 27598ae933 (committer date 2026-11-16 07:30:29). A record
    carries the day of the commit that lands it, so both are dated 2026-11-16
    now, and their text is untouched. The "Record of a date" event below left
    the dates as written; the reader of this pass requires the field itself to
    carry the commit's day. Nothing else on the card changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, sixth pass: the fifth-pass note above says
    the two source-corrected events "are dated 2026-11-17" in the present
    tense, and neither field of this card reads so. The note's sentence is
    true in the past tense, and this event is its correction: the two events
    it speaks of were dated 2026-11-17, a day that had not happened when
    a9d902a1a9 (2026-11-16 07:15:38) and 27598ae933 (2026-11-16 07:30:29)
    wrote and committed them, and their fields read 2026-11-16 now, changed
    in 2e7631a711, the commit that added the fifth-pass note. Their text
    stands, and the fifth-pass note stands as written, a dated event being a
    record of its date. Nothing else on the card changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121 on in-place edits to dated events; four
    records are restored and nothing else changes. (1) Commit 2e7631a711
    (committer date 2026-11-16 09:00:21) changed two date fields from 2026-11-17
    to 2026-11-16: the (bc)-mislabel event's and the four-further-repairs
    event's. Both fields are restored to 2026-11-17, the day their authors
    wrote, in a9d902a1a9 (committer date 2026-11-16 07:15:38) and 27598ae933
    (2026-11-16 07:30:29) respectively; each record carries a day one later
    than the commit that landed it, and its correction is this event rather
    than an edit of the record. (2) That commit also added the "Record of a
    date" and fifth-pass events, whose text c7b68fc6fd and 5675cba726 then
    rewrote in place. Both are restored to the text they were committed with in
    2e7631a711, the fifth-pass note's closing sentence about the record event
    and the record's statement that the dates are left unedited included.
    (3) The fifth-pass note and the sixth-pass event after it say the two dates
    read 2026-11-16; that is the state the first restoration undoes, and both
    stand as written, a dated event being a record of its date. Nothing in the
    problem, the solution or the pages changes, and no page was re-read.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A wording defect in the restored fifth-pass note above, recorded rather
    than edited: it calls the "Record of a date" event "below" although
    that event stands above it. The note is a dated record and is not
    touched; the order is the one 2e7631a711 gave the two events, which added
    both. Nothing else on the card changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121 on in-place edits to dated events: two of
    this card's records stand rewritten and the gate refuses their
    restoration, so neither is touched here and this event is the record of
    it. (1) Commit 96b162602a (committer date 2026-11-15 14:38:11) replaced
    the first 2026-11-15 source-checked note, the one 9bb4dbad80 committed,
    by a longer note naming the PDF page of the checked-in extraction, the
    MinerU extraction of Shichijo and three defects of his solution; that
    commit and that record carry the same day. (2) Commit f67ed2b29e
    (committer date 2026-11-16 02:30:41) added the text-version paths of
    Borcherds, Egbert and Cutrone--Marshburn to the second 2026-11-15
    source-checked note. Those two records share one identity in the gate's
    sense, source-checked by claude on 2026-11-15, so the one-to-one
    comparison of tools/qualc/authoring.py cannot tell which is which: a
    commit that restores either of them, or both, is refused with "multiple
    dated audit events share one identity (source-checked, claude,
    2026-11-15); their earlier texts cannot be distinguished, so the
    comparison is refused (QUAL-11)", together with the line naming the event
    it restores as changed. A restoration is the repair QUAL-11 asks for and
    it waits on a comparison that separates two records of one identity; this
    card is left as committed until that comparison exists, and no record
    here is edited to make the pair distinguishable. The three defects the
    replaced note named are stated in the body meanwhile: the paragraph on
    Shichijo after step r-equals-s and the Shichijo paragraph of the
    published-solution remark give his own Exercise 6.3 block and Corollary
    I.6.12 in place of Exercise I.6.8, the omitted infinity in his displayed
    identity, and the converse left as an assertion. Nothing in the problem,
    the solution or the pages changes, and no page was re-read.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121 on in-place edits to dated events: the two
    2026-11-15 source-checked records above are restored to the text of the
    commit that wrote each, and this is the correction of the event above,
    which recorded their restoration as blocked. The gate refused both until
    41131d3ea5 (issue #147) compared two records of one identity as a multiset
    of the texts introduced under it. (1) The first is 9bb4dbad80's note,
    which 96b162602a replaced. (2) The second is its text before f67ed2b29e
    appended the text-version paths of Borcherds, Egbert and
    Cutrone--Marshburn.
    What the two rewrites added is stated here, so that nothing is lost with
    them. The first rewrite read the checked-in file as the MinerU extraction
    tmp/sources/shitijyou-ch1-section6.md, named PDF p. 62 of it, and placed
    Exercise 6.7 on printed pp. 5--6 with Proposition 6.7 the different
    statement on printed p. 42; the restored note names
    tmp/sources/shitijyou-ch1-section6.pdf and printed pp. 5--6, so the MinerU
    path and both pages are recorded here and nowhere else on this card. It
    also listed three defects of Shichijo's solution, which stand in the body,
    in the paragraph on Shichijo after step r-equals-s and in the Shichijo
    paragraph of the published-solution remark. The second rewrite added the
    text versions of Borcherds, Egbert and Cutrone--Marshburn, which that
    remark names.
    The restored first note states the extension as Exercise I.6.8, which is
    not what the source does; that is the first of the three defects the body
    corrects. The event above stands as written, a dated event being a record
    of its date. Nothing in the problem, the solution or the pages changes,
    and no page was re-read.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.6.7, printed
    p. 47, which asks r = s and then "Is the converse true?". Read each source
    at its cited place in its text version: A. Shichijo, Chapter 1 section 6,
    Exercise 6.7, printed pp. 5-6 (the extension of the birational map P^1 -->
    P^1 to an automorphism, and the converse left as an assertion with the
    author's own footnote 4 giving a configuration in A^3); A. Kock, Abstract
    Projective Lines (2009), Theorem 1 on printed p. 6, the paragraph after (8)
    on printed p. 5, the permutation laws (4)-(7) on printed p. 4, and Section 4
    on printed pp. 8-11 with the determinant formula for the cross ratio and the
    fractional linear form of a projectivity; and the accepted answer 834758,
    the six values from the transpositions (12), (13), (14). Folios verified in
    the copies: Kock's Theorem 1 is on the page whose folio reads 6, the
    permutation laws on the page whose folio reads 4, Section 4 begins on the
    page whose folio reads 8, and Shichijo's Exercise 6.7 begins on his printed
    p. 5 and ends with footnote 4 on p. 6. Checked against the book:
    Proposition I.6.7 is on printed p. 42, Proposition I.6.8 on p. 43 and
    Corollary I.6.12 on p. 45, read in tmp/sources/hartshorne-1977-algebraic-
    geometry.pdf and located by the section headings of those pages; the
    exercise is over the algebraically closed k of Chapter I, which is infinite,
    so the choice of mu outside six values is available. Not checked in this
    pass: the card's unit-group route to r = s, which was read and accepted
    earlier, and Shichijo's Exercise 6.3 block, which the card cites through his
    own reference rather than reads.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The converse's step now names its sources at each paragraph, and the pages
    of the book it cites: Kock's Theorem 1 on printed p. 6 for the uniqueness
    of the projectivity through three points, with Section 4 on printed
    pp. 8-11 for the identification with P(k^2) and the determinant cross
    ratio; Kock's printed p. 5 for the invariance of the cross ratio under
    projectivities; and the permutation laws (4)-(7) on printed p. 4 quoted in
    full, with answer 834758 beside them for the same six values from the
    transpositions (12), (13), (14). The published-solution remark now names
    Kock's paper and answer 834758 and says that no located source states the
    counterexample itself. No mathematics changes: the values 1/lambda,
    1 - lambda and 1/lambda, the six-value orbit, the invariance and the
    threshold r <= 2 are as before, and the pages of Propositions I.6.7 and
    I.6.8 are added to the step that uses them.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on a local reader's report against the sources, five items, and the
    provenance commentary removed from the rendered card. (1) Step r-equals-s is
    now Shichijo's proof transcribed, on printed pp. 5-6, with his displayed
    identity reproduced and named as wrong as printed because it omits
    infinity; the unit-group argument that was the step's only proof is now the
    card's own route, marked as such, and the two steps it uses are marked as
    the card's own at their proofs. (2) Step
    isomorphism-iff-fractional-linear-equivalent names the three solution sets
    that argue the extension (Borcherds PDF p. 8, Egbert PDF p. 55, Shichijo
    printed pp. 5-6) and the two propositions of the book it applies. (3) The
    counterexample now meets the printed hypothesis that all P_i and Q_j be
    distinct: it takes P = {0,1,lambda} and Q_mu = {2,3,mu} with the six points
    distinct, and reaches the cross-ratio condition through tau(x) = (x-2)/2
    carrying infinity, 2, 3 to infinity, 0, 1; the earlier form took
    {0,1,lambda} and {0,1,mu}, which share 0 and 1. (4) Kock's sentence that
    projectivities preserve cross ratios is placed in the paragraph before
    display (8), printed p. 5, as it stands there; the earlier text, and the
    audit event of this date that repeated it, said "after (8)". (5) The claim
    that a fractional linear transformation fixing infinity, 0 and 1 is the
    identity is marked as the card's own, with Kock's Theorem 1 on printed p. 6
    as the general statement beside it rather than after it. The remark is now
    the printed statements with the two corrections of the sets, without the
    text-version paths and the notes on which source has no solution. Not
    checked in this pass: the rank computation in the card's own route, which
    the reader did not dispute.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121 against the sources: one record restored and
    five repairs in the rendered card, with no change to the result. (1) The
    solution-written event above, the one opening "Repairs on a local reader's
    report against the sources, five items", is restored to the text 04cb777d99
    committed with it: f327292c75 rewrote its item (3) in place four minutes
    later, and QUAL-11 makes a dated record the evidence of its day and a
    correction a new record, not an edit of the old one. The restored text is
    left exactly as written, and the corrections it needs are here. Its item (3)
    says that tau(x) = (x-2)/2 carries infinity, 2, 3 to infinity, 0, 1, which
    no map does: the projectivity carrying 2 to 0 and 3 to 1 is x - 2 =
    (x-2)/(3-2). It also gives the two auxiliary points without excluding lambda
    from their range, so that the six points need not be distinct, and without
    saying that they differ from each other. (2) The counterexample now requires
    a and b distinct and outside {0,1,lambda}, not merely outside {0,1}. Under
    the weaker condition a = lambda is allowed, and then P and Q_mu both contain
    lambda, so the two sets are not disjoint and the exercise's hypothesis that
    all the points be distinct fails; lambda, a and b are fixed before mu is
    chosen, and mu is outside {0,1,lambda,a,b} as before. (3) The letters a and
    b named two different things in one step: the two auxiliary points of Q_mu,
    and the generic arguments of the cross ratio [a,b,c,d], of rho and of the
    transpositions. The generic four points are now A, B, C, D and the
    transpositions (AB), (BC), (CD); Kock's Theorem 1 is paraphrased without the
    letters A, B, C, A', B', C' it was stated with, so that the card's A, B, C,
    D do not collide with them, and the vectors of Kock's determinant
    expression, which he writes a, b, c, d for homogeneous coordinate vectors of
    A, B, C, D, are written as bold capitals here for the same reason. The
    computed values, the six-value orbit, the invariance of the cross ratio and
    the threshold r <= 2 are unchanged. (4)
    The quotation in the published-solution remark was credited to Borcherds and
    Egbert together; it is Borcherds's sentence only. Borcherds, Exercise 6.7,
    PDF p. 8, text version tmp/sources/hartshorne-solutions-borcherds.md, line
    260, reads "The converse is true if and only if r <= 3, because any set of
    at most 3 distinct points in P^1 can be mapped to any other set of the same
    size under Aut(P^1), but this is not true for sets of 4 or more points".
    Egbert, Exercise I.6.7, PDF p. 55, text version
    tmp/sources/hartshorne-solutions-egbert.md, lines 2407-2408, gives another
    reason: "The converse is only true for r <= 3 by virtue of the fact that
    mobius transformations can take at most 3 distinct points in P^1 to any
    other 3 distinct points." Each is now quoted in his own words. (5) Step
    isomorphism-iff-fractional-linear-equivalent said Egbert gives "the same
    sentence" as Borcherds, which is false; his sentence is at lines 2405-2406
    of the same text version, "We can extend any map between the two curves to a
    map P^1 -> P^1. Since P_i must map to Q_j thus r = s.", and the step now
    quotes it. (6) The rendered step said Shichijo's extension is not on
    "Exercise I.6.8, which says that a nonsingular projective curve is
    determined by its function field". Chapter I has no Exercise 6.8: the
    exercises of section 6 end at 6.7 on printed p. 47, which is the exercise
    this card answers, and section 7 begins on that page (retained copy
    tmp/sources/hartshorne-1977-algebraic-geometry.pdf, PDF p. 62). The
    statement that a nonsingular projective curve is determined by its function
    field is Corollary I.6.12, printed p. 45 (PDF p. 60), which is the corollary
    Shichijo cites; a clause about an exercise that does not exist is removed
    rather than replaced, and the step says what he writes instead. Shichijo,
    tmp/sources/shitijyou-ch1-section6.md, states the extension in a paragraph
    under his Exercise 6.3 heading (line 137, heading at line 135) because, as he
    says, it is used in the question of Proposition 6.8 and in Exercise 6.7, and
    rests on Cor 6.12; Exercise 6.7 begins at line 242 and refers to "Ex 6.3" at
    line 247. The mention of Exercise I.6.8 in the restored 2026-11-15
    source-checked note above is where the error came from; that note is a dated
    record and stands as written.
    Not checked in this pass: the unit-group route to r = s, the invariance of
    the cross ratio, the six values and the threshold r <= 2, none of which this
    pass changes; Shichijo's footnote 4 and the counterexample he gives for
    Proposition 6.8; and the rank computation in the card's own route, which the
    event above records as unread and which is still unread.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121 against the sources: one display corrected and
    no change of mathematics. The event above, of this date, says that the
    vectors of Kock's determinant expression are written as bold capitals here;
    the display committed with it still carried the letters alpha, beta, gamma
    and delta, which that event does not declare and which the card already uses
    as the coefficients of its fractional linear transformation two sentences
    earlier, so the card carried them in two senses (NOT-3). The display now
    takes the determinants of the bold-capital vectors its gloss names -- the
    determinant of the pair A, C times that of B, D, over the determinant of
    A, D times that of B, C -- which makes the event's statement true of the
    display rather than changing what the event says: that event is a dated
    record and stands as written. Kock's own letters are a, b, c, d, spanning
    A, B, C, D (text version tmp/sources/kock-2009-abstract-projective-lines.md,
    section 4, the display after the definition of the action on E and the
    sentence "we describe the points A in L by homogeneous coordinates
    [a_1 : a_2], where a is any vector spanning A"), and the formula is his with
    the letters changed, which the event above records. The cross ratio, the six
    values, the invariance and the threshold r <= 2 are untouched, and nothing
    else on the card changes.
    Not checked in this pass: Kock's section 4 was not re-read beyond the display
    and the sentence naming the vectors, and no page was re-read.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Two repairs of the printed source and one page, from a read of the card in
    this pass. (1) The problem block dropped the exercise's last clause: the
    printed I.6.7, on printed p. 47 (PDF p. 62, folio read), ends "Is the
    converse true? Cf. (Ex. 3.1)", and the card ended at the question. The
    clause is restored, since the statement keeps the source's wording and tails
    (QUAL-01). (2) The step's citation of Anders Kock, Abstract Projective
    Lines (4 December 2009), gave the permutation laws as "(4)--(7) on printed
    p. 4". Read on the PDF's folios, (4), (5) and (6) are on printed p. 4 and
    (7) is on printed p. 5, where it stands alone above the page break; the
    sentence now gives each its page. The mathematics of the step was read in
    this pass and is unchanged: the invariance of the cross ratio under a
    fractional linear transformation, the three normalisations [B,A,C,D] =
    1/rho(D), [A,C,B,D] = 1-rho(D), [A,B,D,C] = rho(C)/lambda, the six values
    as the orbit under nu -> 1/nu and nu -> 1-nu, and the choice of mu outside
    that orbit with k infinite. Checked in this pass: the printed exercise at
    printed p. 47 and Kock's printed pp. 4--5 on the PDF's folios. Not checked
    in this pass: Kock's printed pp. 6 and 8--11, which the card also cites,
    were not re-read, and the printed pages of Borcherds's, Egbert's and
    Cutrone--Marshburn's sets were not opened.
---
::: {.problem}
Let $P_1, \ldots, P_r, Q_1, \ldots, Q_s$ be distinct points of $\AA^1$.
If
$$
\AA^1 \sm \theset{P_1, \ldots, P_r} \cong \AA^1 \sm \theset{Q_1, \ldots, Q_s},
$$
show that $r = s$.
Is the converse true? Cf. (I, Ex. 3.1).
:::

::: {.solution}
Write $P_i=p_i\in k$ and $Q_j=q_j\in k$ in the affine coordinate $x$.

::: pf

::: pf-step
The coordinate ring of
$$
U=\AA^1\setminus\{P_1,\ldots,P_r\}
$$
is
$$
A_U=k[x,(x-p_1)^{-1},\ldots,(x-p_r)^{-1}].
$$

::: pf-proof
This step is the card's own; none of the sources named below computes this ring.
Put
$$
g(x)=\prod_{i=1}^r(x-p_i).
$$
Then $U=D(g)\subseteq\Spec k[x]$, so
$$
\Gamma(U,\OO_U)=k[x,g^{-1}].
$$
Because the linear factors $x-p_i$ are pairwise coprime, inverting their product is equivalent to inverting each factor separately.
This gives the displayed description.
:::

:::

::: {.pf-step #unit-group-structure}
The unit group of $A_U$ is
$$
A_U^\times
=k^\times\,(x-p_1)^{\ZZ}\cdots(x-p_r)^{\ZZ},
$$
and therefore
$$
A_U^\times/k^\times\cong\ZZ^r.
$$

::: pf-proof
This step is the card's own as well, and it is the input of the card's own route in step [](#r-equals-s){.pf-ref}.
The polynomial ring $k[x]$ is a unique factorization domain.
An element of its localization at the multiplicative system generated by the $x-p_i$ is a unit exactly when every irreducible factor of its numerator and denominator belongs to that multiplicative system.
Thus every unit has a unique expression
$$
c\prod_{i=1}^r(x-p_i)^{n_i},
\qquad c\in k^\times, n_i\in\ZZ.
$$
Modulo the constant units, the exponent vector $(n_1,\ldots,n_r)$ identifies the quotient with the free abelian group $\ZZ^r$.
:::

:::

::: {.pf-step #r-equals-s}
If
$$
\AA^1\setminus\{P_1,\ldots,P_r\}
\cong
\AA^1\setminus\{Q_1,\ldots,Q_s\},
$$
then $r=s$.

::: pf-proof
A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), Chapter 1 section 6, Exercise 6.7, printed pp. 5--6, proves this by the published route. He writes
$$
\AA^1\sm\theset{P_1,\ldots,P_r}=\PP^1\sm(\theset{P_1,\ldots,P_r}\union\theset{\infty}),
$$
so the isomorphism gives a birational map $\PP^1\dashrightarrow\PP^1$, and that map extends to an automorphism $\bar\phi'$ of $\PP^1$, which then carries the omitted sets to one another. His extension is stated in a paragraph he places under his Exercise 6.3 heading, because, as he says there, it is used in the question of Proposition 6.8 and in Exercise 6.7: by Corollary I.6.12 (printed p. 45), nonsingular projective curves birational to one another are isomorphic.

His displayed identity
$$
\bar\phi'(\theset{P_n})=\PP^1-\bar\phi'(\PP^1-\theset{P_n})=\PP^1-(\PP^1-\theset{Q_n})=\theset{Q_n}
$$
is wrong as printed: it omits $\infty$. The sets exchanged are the $(r+1)$-point set $\theset{P_n}_{n=1}^r\union\theset{\infty}$ and the $(s+1)$-point set $\theset{Q_n}_{n=1}^s\union\theset{\infty}$ of step [](#isomorphism-iff-fractional-linear-equivalent){.pf-ref}, and $\bar\phi'$ restricts to a bijection between them, so $r+1=s+1$ and
$$
\boxed{r=s}.
$$

The card's own route does not use the extension theorem. An isomorphism of the two $k$-varieties induces an isomorphism of their coordinate rings and hence of their unit groups, and it fixes the subgroup $k^\times$ of constant units, so step [](#unit-group-structure){.pf-ref} gives an isomorphism
$$
\ZZ^r\cong A_U^\times/k^\times
\cong A_V^\times/k^\times\cong\ZZ^s,
$$
and free abelian groups of finite rank are isomorphic only when their ranks agree.
:::

:::

::: {.pf-step #isomorphism-iff-fractional-linear-equivalent}
More precisely, the two punctured lines are isomorphic if and only if the two $(r+1)$-point subsets
$$
\{\infty,P_1,\ldots,P_r\},
\qquad
\{\infty,Q_1,\ldots,Q_s\}
$$
of $\PP^1$ are carried to one another by a fractional linear transformation.

::: pf-proof
This is the extension of a morphism between curves to the projective closures, argued in three of the solution sets: Borcherds, Exercise 6.7, PDF p. 8, "any map from one curve to the other can be extended to a map from $\PP^1$ to $\PP^1$, so the points $P_i$ must be mapped to the points $Q_j$"; Egbert, Exercise I.6.7, PDF p. 55, "We can extend any map between the two curves to a map $\PP^1\to\PP^1$. Since $P_i$ must map to $Q_j$ thus $r=s$."; and Shichijo, printed pp. 5--6, whose route is step [](#r-equals-s){.pf-ref}.

The theorem applied is Hartshorne's. Both $U$ and $V$ are nonsingular quasi-projective curves, hence abstract nonsingular curves by Proposition I.6.7 (printed p. 42), and $\PP^1$ is projective, so Proposition I.6.8 (printed p. 43), which is stated for abstract nonsingular curves, applies to them.
Apply Proposition I.6.8 successively at the finitely many omitted points to extend the composite
$$
U\xrightarrow{\phi}V\hookrightarrow\PP^1
$$
to a morphism $\bar\phi:\PP^1\to\PP^1$.
Doing the same for $\phi^{-1}$ gives a morphism $\bar\psi:\PP^1\to\PP^1$.
The composites $\bar\psi\bar\phi$ and $\bar\phi\bar\psi$ agree with the identity on dense open subsets, hence everywhere.
Thus $\bar\phi$ is an automorphism of $\PP^1$.
By [[P-AGH66AUTP1|Exercise I.6.6]], it is fractional linear.

Since $\bar\phi$ restricts to a bijection $U\to V$, it carries the complement of $U$ in $\PP^1$ bijectively to the complement of $V$.
This proves necessity.
Conversely, any fractional linear transformation carrying one displayed finite subset to the other restricts to an isomorphism of their complements.
:::

:::

::: {.pf-step #converse-fails}
The converse to $r=s$ is false in general.

::: pf-proof
Take $r=s=3$. Fix $\lambda,a,b\in k$ with $\lambda\notin\{0,1\}$ and $a,b$ distinct and outside $\{0,1,\lambda\}$, which is possible because $k$ is infinite. Put
$$
P=\theset{0,1,\lambda},
\qquad
Q_\mu=\theset{a,b,\mu}
$$
for $\mu\in k$ with $\mu\notin\{0,1,\lambda,a,b\}$, so that the six points are distinct and $P\cap Q_\mu=\varnothing$, as the exercise requires.

Write $[A,B,C,D]$ for the image of $D$ under the unique fractional linear transformation carrying $A,B,C$ to $\infty,0,1$. Kock, *Abstract Projective Lines* (4 December 2009), Theorem 1, printed p. 6, is that existence and uniqueness in general form, for the projective line over any field: for three distinct points of one projective line and three distinct points of another there is a unique projectivity carrying them to one another in order.
The case needed here, which is the card's own: a fractional linear transformation $x\mapsto(\alpha x+\beta)/(\gamma x+\delta)$ fixing $\infty$ forces $\gamma=0$, then fixing $0$ forces $\beta=0$, and then fixing $1$ forces $\alpha=\delta$; so the transformation fixing $\infty$, $0$ and $1$ is the identity, and an element of $\PGL(1)$ is determined by its values at three distinct points.

That cross ratios are preserved is Kock's, printed p. 5: "projectivities, in the sense defined here, commute with composition, since they are functors. Hence it is clear that projectivities preserve cross ratios."
Here is the computation for four points $A,B,C,D$ of $\PP^1$. Let $\rho$ carry $A,B,C$ to $\infty,0,1$, and let $\phi$ be fractional linear; then $\rho\circ\phi^{-1}$ carries $\phi A,\phi B,\phi C$ to $\infty,0,1$, so it is the normalizing transformation of $[\phi A,\phi B,\phi C,\phi D]$ and sends $\phi D$ to $\rho(D)$. Hence
$$
[\phi A,\phi B,\phi C,\phi D]=[A,B,C,D].
$$
Kock gives the cross ratio in $\PP^1=\PP(k^2)$ as the determinant expression
$$
(A,B;C,D)=\frac{\abs{\mathbf{A},\mathbf{C}}\cdot\abs{\mathbf{B},\mathbf{D}}}{\abs{\mathbf{A},\mathbf{D}}\cdot\abs{\mathbf{B},\mathbf{C}}},
$$
with $\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}$ homogeneous coordinate vectors of $A,B,C,D$, and records in Section 4, printed pp. 8--11, that every projectivity of $\PP^1$ is tracked by a linear automorphism, the fractional linear transformation $x\mapsto(\alpha_{21}+\alpha_{22}x)/(\alpha_{11}+\alpha_{12}x)$.

The cross ratios of the other orderings are computed with $\rho$ normalizing $(A,B,C)$, so that $\rho(D)=[A,B,C,D]=\lambda$:
$$
[B,A,C,D]=\frac{1}{\rho(D)}=\frac1\lambda,
\qquad
[A,C,B,D]=1-\rho(D)=1-\lambda,
\qquad
[A,B,D,C]=\frac{\rho(C)}{\lambda}=\frac1\lambda
$$
where the three right-hand sides use that $x\mapsto1/\rho(x)$ carries $B,A,C$ to $\infty,0,1$, that $x\mapsto1-\rho(x)$ carries $A,C,B$ to $\infty,0,1$, and that $x\mapsto\rho(x)/\lambda$ carries $A,B,D$ to $\infty,0,1$. These are Kock's permutation laws (4)--(6) on printed p. 4 and (7) on printed p. 5, stated there for $\mu=(A,B;C,D)$:
$$
(A,B;C,D)=(B,A;D,C)=(C,D;A,B)=(D,C;B,A),
$$
$$
(A,B;D,C)=\mu^{-1},
\qquad
(A,C;B,D)=1-\mu,
\qquad
(A,C;D,B)=(1-\mu)^{-1},
$$
$$
(A,D;B,C)=\frac{\mu-1}{\mu},
\qquad
(A,D;C,B)=\frac{\mu}{\mu-1},
$$
and the accepted answer 834758 to Mathematics Stack Exchange question 834693 computes the same six values from the transpositions $(12)$, $(13)$ and $(14)$, which generate $S_4$, getting $1/\lambda$, $\lambda/(\lambda-1)$ and $1-\lambda$. The transpositions $(AB)$, $(BC)$ and $(CD)$ generate the group of all orderings of four points, so every ordering of a four-point subset is reached by a composite of them, and the substitutions $\lambda\mapsto1/\lambda$ and $\lambda\mapsto1-\lambda$ generate the six-element set
$$
\lambda,\quad1-\lambda,\quad\lambda^{-1},\quad
(1-\lambda)^{-1},\quad
\frac{\lambda}{\lambda-1},\quad
\frac{\lambda-1}{\lambda}.
$$

Now let $\tau\in\PGL(1)$ carry $\infty,a,b$ to $\infty,0,1$, that is $\tau(x)=(x-a)/(b-a)$.
By step [](#isomorphism-iff-fractional-linear-equivalent){.pf-ref} the two punctured lines are isomorphic exactly when some fractional linear transformation carries $\{\infty\}\union P=\{\infty,0,1,\lambda\}$ onto $\{\infty\}\union Q_\mu=\{\infty,a,b,\mu\}$, and by the invariance above that happens exactly when $\lambda$ is the cross ratio of some ordering of $\{\infty,a,b,\mu\}$; applying $\tau$ to the four entries, exactly when $\lambda$ is the cross ratio of some ordering of $\{\infty,0,1,\tau(\mu)\}$, that is exactly when $\tau(\mu)$ is one of the six values attached to $\lambda$; the six values attached to a point are its orbit under the substitutions $\nu\mapsto1/\nu$ and $\nu\mapsto1-\nu$, which generate a group, so $\lambda$ lies among the six values attached to $\nu$ exactly when $\nu$ lies among the six values attached to $\lambda$.

Because the algebraically closed field $k$ is infinite, choose $\mu\notin\{0,1,\lambda,a,b\}$ with $\tau(\mu)$ outside those six values; then no fractional linear transformation carries $\{\infty\}\union P$ onto $\{\infty\}\union Q_\mu$, and
$$
\AA^1\setminus P
\not\cong
\AA^1\setminus Q_\mu,
$$
although both have three punctures.
Thus equality of the numbers of punctures is necessary but not sufficient.
:::

:::

::: pf-qed
Step [](#r-equals-s){.pf-ref} proves the required invariant, while steps [](#isomorphism-iff-fractional-linear-equivalent){.pf-ref} and [](#converse-fails){.pf-ref} answer the converse question.
:::

:::
:::

::: {.remark title="Published solution"}
The facts used are printed in Anders Kock, *Abstract Projective Lines* (4 December 2009): Theorem 1 on printed p. 6, that a projectivity is determined by the images of three distinct points; the paragraph before display (8) on printed p. 5, that projectivities preserve cross ratios; the permutation laws (4)--(7) on printed p. 4, giving the six values; and Section 4 on printed pp. 8--11, the identification of $\PP^1$ with an abstract projective line with its projectivities the fractional linear transformations. The accepted answer 834758 to Mathematics Stack Exchange question 834693 computes the same six values from three transpositions generating $S_4$.

Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 6.7, PDF p. 8, and Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.6.7, PDF p. 55, answer $r=s$ and state the threshold as $r\le3$: Borcherds's reason is "because any set of at most $3$ distinct points in $\PP^1$ can be mapped to any other set of the same size under $\operatorname{Aut}(\PP^1)$", and Egbert's is "by virtue of the fact that mobius transformations can take at most $3$ distinct points in $\PP^1$ to any other $3$ distinct points". Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, Exercise I.6.7, PDF p. 25, state it as $r>3$ and add that "any isomorphism between $\PP^1$ and $\PP^1$ fixes at most $2$ points, so if $r>3$, the map must be the identity isomorphism".

The threshold $r\le3$ is wrong, and $r=3$ is where it fails: the automorphism of $\PP^1$ produced in step [](#isomorphism-iff-fractional-linear-equivalent){.pf-ref} carries the $(r+1)$-point set $\{\infty\}\cup P$ onto $\{\infty\}\cup Q$ as a set, sending $\infty$ to whatever point of that set is its image, and for $r=3$ the two four-point sets of step [](#converse-fails){.pf-ref} are already separated by the cross ratio. So the converse of $r=s$ holds for $r\le2$, where $3$-transitivity of $\PGL(1)$ carries $\{\infty\}\cup P$ to $\{\infty\}\cup Q$, and fails for $r\ge3$. Cutrone--Marshburn's premise, that a non-identity automorphism of $\PP^1$ fixes at most two points, is true; the inference is not, since an isomorphism carrying $\{\infty\}\cup P$ to $\{\infty\}\cup Q$ need not fix either set pointwise, and on four points acts as a permutation of them.

Shichijo's converse, printed p. 6, is that an element of $\PGL(1)$ is determined by the images of three points and that, $\AA^1$ being infinite, one may choose the two finite sets outside the reach of any one element; that is the assertion rather than a proof, and his footnote replaces it by a configuration in $\AA^3$.
:::
