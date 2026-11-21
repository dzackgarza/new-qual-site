---
schema: qual/card@1
id: P-AGH4311PROJECTIONCLOSEDIMMERSION
kind: problem
title: Projection embeds a smooth $r$-fold into $\PP^{n-1}$ when $n>2r+1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Very Ample Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.11 together with the projection/linear-system
    criterion II.7.3 and the Veronese construction II.7.7. Part (a) uses
    separate secant and embedded-tangent-space incidence bounds. Part (b)
    reduces each secant to the plane conic obtained from the corresponding
    line in P^2 and checks the lower dimension bound for the secant variety by
    an explicit four-rank local parametrization, valid in every
    characteristic.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), IV.3.11(a),
    printed p. 309. The closed-embedding criterion the last step invokes is
    stated in R. Vakil, The Rising Sea: Foundations of Algebraic Geometry,
    21 October 2025 version, as Theorem 19.1.1, printed p. 536, text version `tmp/sources/vakil-rising-sea-2025-10-21.md`, with the
    hypotheses "injective on closed points" and "injective on tangent vectors at
    closed points" and no other; he reduces it at 19.1.3, printed p. 537, to
    Theorem 19.1.2 and proves that at 19.1.4, but the reduction's last step is
    Exercise 19.1.D, "Show that the degree of pi is at most 1 at all closed
    points of Y", left to the reader and the only place where the tangent-vector
    hypothesis enters. Step s6 cites Vakil with that limit recorded and rests on
    Hartshorne II.7.3 (T-DIVMAPPN), which is the same statement. What is not in
    Vakil is the existence of the centre:
    the secant and tangent loci are closed of dimension at most 2r+1, so a point O
    outside them exists when n > 2r+1, and that count is the card's own. Egbert's
    entry for (a) is a citation to Shafarevich, and Shafarevich was not consulted.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Named the text version of Vakil's book at the citation of Theorem 19.1.1 in
    the remark on 2026-11-16, where it cited the PDF alone: it is
    tmp/sources/vakil-rising-sea-2025-10-21.md. No page or claim changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Part (a) has a complete published proof, located for this batch, and the
    printed exercise was read with it: Hartshorne, Algebraic Geometry (1977),
    IV Ex. 3.11(a), printed p. 316 -- not printed p. 309, which the event of
    2026-11-15 above gives for it; the exercise stands on PDF p. 331 of the
    text version tmp/sources/hartshorne-1977-algebraic-geometry.md, where
    printed p. N is PDF p. N+15. Read at its cited places in the text version
    tmp/sources/shafarevich-2013-basic-algebraic-geometry-1-pp129-138.md:
    Theorem 2.25 on printed p. 134, the lemma on isomorphic embeddings on
    printed pp. 134-135, Corollary 2.7 on printed p. 135, and the proof of
    Theorem 2.25 on printed pp. 135-136, whose folios were checked against the
    PDF (PDF p. 149 is printed p. 133, so printed p. N is PDF p. N+16 in that
    copy). Checked against the book: Shafarevich's Theorem 2.25 is stated for a
    nonsingular projective n-dimensional variety in P^N with N > 2n+1 and
    concludes an isomorphic embedding into P^{N-1}, which is assertion (a) of
    the exercise with N = n and n = r; the closed immersion follows since a
    projective X has closed image. Not checked: Shafarevich's Theorem 1.15,
    which Corollary 2.7 cites for the finiteness of the projection, and
    Theorem 1.25, which the dimension count cites; the retained copy holds
    printed pp. 129-138 only, so neither statement was read, and the card says
    so at the step that uses 1.15. For (b) the published treatment located is
    Egbert's entry 4.3.21, printed p. 223, which argues the clause for a
    general point of a secant line and not for every point of every secant
    line.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Part (a) is now the transcription of Shafarevich's proof, one step per
    published step, each naming the numbered statement and printed page, with
    his sentences quoted at the steps that carry his argument: steps secants
    and tangent-locus for the two incidence varieties and their dimensions,
    step centre for the choice of the point, step lemma-criterion for the lemma
    on isomorphic embeddings with its Nakayama proof, and step corollary for
    Corollary 2.7 and the conclusion of (a). Part (b) keeps its steps, now
    labelled veronese-conic, infinitely-many-secants, secant-dim-upper,
    secant-dim-lower, secant-dim and closed-immersion-b, and its last step now
    cites step corollary, which is the criterion it uses, instead of the three
    former steps of (a). What left the card with the former steps s1-s6 is the
    card's own secant and tangent dimension count, of which step centre now
    quotes Shafarevich's; the Vakil citation and the paragraph on Exercise
    19.1.D leave the card with them, and so does the remark's statement that
    part (a) has no complete published solution in the retained sets, which
    Shafarevich's Theorem 2.25 answers. Nothing in the problem statement
    changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's report, and the record of what
    the three events of this date above left out. (i) The secant bound of part
    (a) is published: J. Harris, Algebraic Geometry: A First Course (1992),
    Lecture 11, Proposition 11.24, states that the secant variety of an
    irreducible k-dimensional variety in P^n is irreducible of dimension at
    most 2k+1, with equality if and only if the general point lying on a
    secant line lies on only finitely many of them, and its Example 11.22
    supplies the dimension 2k of the variety of secant lines that the count
    uses; the proposition's proof is the incidence correspondence of pairs
    (l,p) with p in l, over the variety of secant lines, which is the honest
    secant lines and not the pairs with equal entries. Read at Example 11.22,
    the incidence display before Proposition 11.24, Proposition 11.24 and the
    Veronese paragraph after Exercise 11.25, in the text version
    tmp/sources/harris-1992-algebraic-geometry-first-course-pp128-149.md. That
    text version carries no printed folios, so the printed page of these
    statements is not established; it lies within printed pp. 128-149, the
    range that version retains. The card cites them by lecture and number and
    gives no page. (ii) The card's own proof of the bound, the incidence
    variety over the complement of the diagonal in X x X, stood at step s1
    before 9a5cd235da and was deleted by that commit; 16894bb15f did not
    restore it, so the card carried (a) with the bound assumed. It is back in
    step secants, marked there as the card's own, and the step now proves the
    bound instead of reporting on the source. (iii) Corrected here, the events
    of this date not being rewritable: their sentence "Part (a) has a complete
    published proof", which is true of the exercise but not of Shafarevich's
    count of it; their description of step secants as carrying "the two
    incidence varieties with their dimensions", which Shafarevich's secant
    passage does not do; and their sentence that the card's own secant and
    tangent dimension count "left the card with the former steps s1-s6".
    Also recorded here: commit 16894bb15f, which named the defect, quoted the
    lemma and Corollary 2.7 in full and marked the (b) steps as the card's
    own, had no event of its own until this one. (iv) The erratum and the
    provenance sentences that stood inside the solution are now in the remark
    on the published solution, where the account of a defective published
    argument belongs: the defect itself, the opening sentence "his printed
    count for the secant locus is defective, and step secants says where", and
    a sentence that mixed Shafarevich's P^N with this card's P^n. The
    solution's steps now prove the exercise. Not read in this pass:
    Shafarevich's Theorem 1.15 and Theorem 1.25, as before, and no other part
    of Harris's Lecture 11; no page of either text version was re-read beyond
    the passages named. Checked against the book in this pass: Hartshorne
    IV Ex. 3.11(a) on printed p. 316, unchanged.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's second report. (i) The two bounds
    on the secant variety of the Veronese surface, which (b) asserts, are
    transcribed. P. Harris, Algebraic Geometry: A First Course (1992),
    Lecture 11, Example 11.22, in its Veronese paragraph, prints the upper
    bound from the general point of a secant line lying on a one-dimensional
    family of them and the equality, with the cones over S(X) with vertex a
    point of it as the reason for the lower bound; A. Egbert, Solutions to
    Hartshorne's Algebraic Geometry (2013), IV.3.11, entry 4.3.21, printed
    p. 223, prints the same two bounds from the same argument. Both are quoted
    at steps secant-dim-upper and secant-dim-lower, and step secant-dim is now
    the conclusion the two texts draw. Read for this pass: the Veronese
    paragraph of Example 11.22 in
    tmp/sources/harris-1992-algebraic-geometry-first-course-pp128-149.md, at
    the passages named in the event above, and entry 4.3.21 in the Egbert text
    version named there. Harris's text version still carries no printed folios,
    so the page of Example 11.22 is not established; Egbert's is printed
    p. 223. (ii) The card's own proofs of those two bounds are withdrawn: the
    incidence variety of triples (P,Q,O) with O on the line PQ over the
    complement of the diagonal, with the fibre inequality, for the upper bound,
    and the four-parameter local computation through the chart of the Veronese
    embedding for the lower. A published proof covers that part, so these are
    not the card's-own proofs that a part no source proves keeps; they remain
    readable at commit 2cd5db74ad. What no source proves in (b) is the clause
    that every point of every secant line lies on infinitely many secant
    lines, which steps veronese-conic and infinitely-many-secants prove and
    mark as the card's own. (iii) The remark's sentence "that bound is
    Harris's, and in this card's letters it is the incidence count of step
    secants" confused two different counts: Harris's correspondence lies over
    the variety of secant lines, and the count in step secants over the
    complement of the diagonal in X x X, which is the card's own. The remark
    now says so. (iv) The remark's "the argument above uses" is replaced by
    the two step references it meant, and the solution's opening sentence that
    all the steps of (b) are the card's own now says which ones are, since
    steps secant-dim-upper, secant-dim-lower and secant-dim transcribe two
    printed texts. Not read in this pass: Harris's other lectures, and
    Shafarevich's Theorem 1.15 and Theorem 1.25, as before. Checked against
    the book in this pass: Hartshorne IV Ex. 3.11(b) on printed p. 316,
    unchanged.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's third report, and the record of
    what the passes of this date left out or got wrong. (i) Harris's printed
    pages are established, and they replace the "not established" of the
    event of this date that records the second report. Read off the retained
    PDF tmp/sources/harris-1992-algebraic-geometry-first-course.pdf at PDF
    pp. 157-160, whose running heads read 142, 143, 144 and 145, so printed
    p. N is PDF p. N+15 in that copy, the offset Hartshorne's text version
    also has: Example 11.22 opens on printed p. 143, and the incidence
    correspondence, Proposition 11.24 and the Veronese paragraph are on
    printed p. 144. The text version
    tmp/sources/harris-1992-algebraic-geometry-first-course-pp128-149.md
    carries one range marker, "PDF pages 145-164", and no folios, which is
    why the earlier pass recorded no page. The citations of Harris on this
    card now give those pages. (ii) The quotation at step secant-dim-upper
    changed Harris's words inside quotation marks: he prints "r will lie on
    the plane Lambda spanned by C. But then every line through r in Lambda
    will be a secant line", and the text version renders Lambda as "A". The
    quote now carries his words, read off printed p. 144, and the remark's
    paraphrase of the same passage uses Lambda. (iii) Step secant-dim-upper's
    sentence from the one-dimensional family to the bound 4 is the card's
    own and now says so; Proposition 11.24 states the bound 2k+1 and the
    criterion for equality, not a fibre inequality, and what the step now
    does is apply the equality criterion at k=2. (iv) The sentence "Both
    texts print the bound as immediate, and Harris's parenthetical is the
    only reason either gives" is out of the rendered solution: commentary on
    the sources belongs in neither a solution nor a remark, and the two
    quotations in that step show what each text prints. (v) One symbol for
    one object: the solution opens by declaring Sec(X) the closure in P^n of
    the union of the secant lines, which Harris writes S(X), and steps
    secants, secant-dim and closed-immersion-b use it; step
    closed-immersion-b says that Sec(X) is closed, which both the choice of O
    outside it and the tangent-space argument need, and no longer speaks of
    "the closure of the secant variety". (vi) The part of (b) with no
    published proof is the closed immersion into P^4, which step
    closed-immersion-b proves and marks as the card's own: Egbert's entry
    4.3.21, printed p. 223, stops at the two bounds, and Harris's Example
    11.22, printed p. 144, gives the dimension and no projection. The
    exercise's own parenthetical points to (II, Ex. 7.7), whose part (b),
    printed p. 170, asks the reader to show that the subsystem of conics
    spanned by x^2, y^2, z^2, y(x-z) and (x-y)z gives a closed immersion of
    P^2 into P^4; that is a reference to an exercise, with no printed
    solution, and not a published proof of this step. The part is named open
    in the COMPLAINTS record of this date. (vii) The event of this date that
    ba3057319b added writes "P. Harris"; the author of Algebraic Geometry: A
    First Course is J. Harris, as every other citation of him on this card
    has it. (viii) QUAL-11: no event of this card and no record of
    COMPLAINTS.md was rewritten in this pass; the audit hunks of ba3057319b
    and 9496081602 add lines only, 8cf37922b8 touches no audit block, and the
    text above is the correction of the earlier text, which stands as
    written. Not read in this pass: the printed book itself, any other part
    of Harris's Lecture 11, and Shafarevich's Theorem 1.15 and Theorem 1.25,
    as before; the printed exercise IV Ex. 3.11 is unchanged on printed
    p. 316.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's fourth report, and the correction
    of two things the event above does. (i) The quotation of Proposition 11.24
    was extended by ee563ab9bb and the extension changed Harris's words: he
    prints "the general point p in the line qr lying on a secant line to X
    lies on only a finite number of secant lines to X", with the bar over qr,
    where the card printed p in P^n. That substitution is this card's, not the
    source's. Read off printed p. 144 of the retained PDF, that is PDF p. 159
    of tmp/sources/harris-1992-algebraic-geometry-first-course.pdf, on the
    line after "at most 2k+1, with equality holding if and only if"; the text
    version tmp/sources/harris-1992-algebraic-geometry-first-course-pp128-149.md
    agrees at line 346, and the crude pdftotext rendering of the same line
    gives "p E qr". The quote now carries Harris's qr, and the sentence
    applying the equality criterion at k=2 uses the same letters. (ii) The
    notation repair recorded at (v) of the event above is completed: steps
    centre and corollary still named the closure of the union of the secant
    lines by the second symbol Sigma with a subscript sec, while the solution
    declares Sec(X) and Harris's Sigma names his incidence correspondence of
    pairs (l,p). Both steps now write Sec(X), the display in step centre no
    longer carries the overlined Sigma, and the only Sigma left on the card is
    Harris's correspondence, in steps secants and secant-dim-upper. Not read
    in this pass: any page of either text beyond printed p. 144 of Harris and
    its text version, and nothing of Shafarevich's Theorem 1.15 and 1.25, as
    before. No statement changes; the printed exercise is unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's fifth report, and the correction
    of the last clause of (i) in the event above. That event closed its first
    item "the sentence applying the equality criterion at k=2 uses the same
    letters", and the sentence did, writing p in the line qr outside any
    quotation, where those letters are not bound on this card: r is the
    dimension of X in the statement and in the solution's opening, and in the
    quotation of the same step r is a general point of P^5 and q a point of
    P^2. Harris's letters belong inside the quotation at printed p. 144, which
    now carries them; the card's own sentence names the general point of a
    general secant line of X in words, and introduces no letter of its own, so
    that nothing collides with r as a dimension. That sentence is still the
    card's own and still says so. Not read in this pass: no source was read
    again; the quotation and its page stand as the event above records them.
    No statement changes, and no step's claim changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's whole-card reading, and the
    correction of a misreading the event of this date that ba3057319b added
    carries. That event records "the cones over S(X) with vertex a point of it
    as the reason for the lower bound". Harris, Example 11.22, printed p. 144,
    writes "the cones p-bar,S over S with vertex a point p in S would all have
    to coincide", in the paragraph that has just introduced X as the Veronese
    surface; his letters are ambiguous as printed, and the remark paraphrasing
    him resolved them the wrong way. With S read as the secant variety the
    argument does not run: nothing on this card or in Harris puts the cone
    over S(X) with a vertex on it inside S(X). With S read as the surface, it
    does: for p in X every line joining p to a point of X is a secant line, so
    the cone lies in S(X), and it is three-dimensional, being the union of a
    surface's worth of lines through p; were dim S(X) 3, each such cone would
    be S(X) and the cones, whose vertices differ, would coincide. The
    published-solution remark now carries the cones over X, with the
    containment that makes the argument run, and Harris's own sentence is
    quoted unchanged at step secant-dim-lower, as his words and inside
    quotation marks. The event of this date stands as written, and the record
    of this date in COMPLAINTS.md that repeats the misreading is corrected in
    a new record of today. Not read in this pass: no page of Harris beyond
    printed p. 144 already read, and no other source; the paragraph of
    Example 11.22 in the text version at line 352 was checked for the same
    sentence.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's final whole-batch report, and
    seven repairs of the card. (i) The problem statement of (b) now carries
    Hartshorne's parentheses and his reference number around the Severi
    sentence: printed p. 316 reads "(A theorem of Severi [1] states ... with
    transversal tangent planes.)", and the statement had dropped both. Read
    at line 9900 of tmp/sources/hartshorne-1977-algebraic-geometry.md, between
    the markers of PDF pages 330 and 331, that is on printed p. 316. (ii) One
    letter for the centre: steps centre and corollary called it xi, which is
    Shafarevich's letter, while the exercise calls it O and step
    closed-immersion-b already used O. Both steps now use O and say that his
    letter is xi. (iii) Corollary 2.7 requires its centre to lie outside X,
    and step corollary now says why the point it takes does: it is taken in
    the complement of X cup Sec(X) cup the closure of U_2, which is how step
    centre chooses it; for r >= 1 that also follows from X contained in
    Sec(X), a point of X being a limit of the secant lines through it. (iv)
    Step secant-dim-lower now carries the reason Harris's parenthetical is
    elementary, which the card had left in COMPLAINTS.md only: for p in X the
    union of the planes of the conics nu_2(l) over the pencil of lines l
    through the preimage of p is three-dimensional and lies in Sec(X), so a
    three-dimensional Sec(X) would be a cone with vertex at every point of X,
    and adjoining points of X one at a time puts the span of X, which is P^5,
    inside it. That paragraph is marked the card's own and Harris's sentence
    is still quoted unchanged; the published-solution remark, which stopped
    at "would all have to coincide", now carries the same reason. (v) The
    card's own incidence count leaves step secants, on the ground the event of
    this date recording the reader's second report used for the card's own
    proofs of the two bounds of (b): a published proof covers that part, and
    the two parts were being treated inconsistently. The count stood at
    2cd5db74ad and was restored to the card earlier today; it remains readable
    there. (vi) The pf-qed said which steps came from which text; it now says
    what the steps prove. (vii) QUAL-11: the event of 2026-11-15 above, whose
    note begins "Printed exercise read", was extended in place on 2026-11-16 by
    commit f67ed2b29e, which inserted the path of Vakil's text version into the
    sentence naming Vakil's Theorem 19.1.1; no later commit restored it. Its
    text on its day is the text of 73272357f3, the last revision of that day,
    in which the citation reads "as Theorem 19.1.1, printed p. 536, with the
    hypotheses ...", and the sentence that commit inserted is here: the
    citation of Vakil in that event, and in the remark added on 2026-11-16,
    was read in the text version tmp/sources/vakil-rising-sea-2025-10-21.md.
    That restoration is not made: the shared gate refuses a commit that
    changes an audit event of an earlier day unless the replacement is every
    text ever introduced for that day, kind and author, and the only text
    introduced there is the event's text at 9eadf0c884. The edit is disclosed
    here instead, as 9daa803569 disclosed what that commit could not restore.
    Checked in this pass: the
    printed exercise of IV.3.11 on printed p. 316 in the text version;
    Harris's sentence at printed p. 144, Shafarevich's Corollary 2.7 at
    printed p. 135 and the proof of Theorem 2.25 at printed p. 136, all as
    already read in this batch; and this card's audit trail in git, commit by
    commit. Not read in this pass: Shafarevich's Theorem 1.15 and Theorem
    1.25, as before, and the printed book itself; no step outside (iv) was
    re-derived.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's report of commit 23a6edd0ef, and
    the correction of three defects that commit introduced. (i) Step
    secant-dim-lower said that two distinct lines through p_0 give planes
    meeting "along the tangent line of X at p". X is a surface and has a
    tangent plane at p, not a tangent line, and the two planes do not meet in
    a line: the paragraph now argues from the reducible conic Q = l union l',
    which is a conic in P^2, so that nu_2(Q) is a hyperplane section of X, and
    on Q = P^1 the map nu_2 is the complete linear system |O_Q(2)| of degree 4
    and dimension 4, so <nu_2(Q)> = <Pi_l, Pi_l'> is a P^4; the two planes are
    therefore distinct and meet in a single point, namely p. The conclusion
    that C_p is three-dimensional is unchanged. (ii) The published-solution
    remark presented the card's own completion of the lower bound as
    Harris's; Harris prints only the parenthetical "the cones p-bar,S over S
    with vertex a point p in S would all have to coincide", in Example 11.22,
    printed p. 144, text version
    tmp/sources/harris-1992-algebraic-geometry-first-course-pp128-149.md at
    line 352. The remark now gives Harris the upper bound and that
    parenthetical, and marks the span argument as the card's own, as step
    secant-dim-lower does; the solution's opening sentence, which called the
    two bounds Harris's and Egbert's, now says that both state them and that
    the lower one is proved in neither. (iii) Step closed-immersion-b said the
    criterion of step corollary "needs exactly" two conditions, against that
    step's three requirements; it now says that O does not lie on X, since X
    is contained in Sec(X) and O lies outside Sec(X), along with the other
    two. Checked in this pass: the containment X in Sec(X) and the two-plane
    computation above, Harris's sentence at the line named, and the three
    places on the card. Not read in this pass: no source beyond that sentence
    was read again; no step outside these three was re-derived, and the
    printed book was not reopened.
- event: source-corrected
  by: kimi
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's latest report. Item (i) of the
    preceding event identifies the reducible conic Q = l union l' with P^1 and
    repeats that error from step secant-dim-lower; both are corrected here,
    and the preceding event stands unchanged. In the step, Q is treated as
    two lines meeting at p_0: restriction from conics on P^2 to Q is
    surjective, with one-dimensional kernel generated by an equation of Q, so
    h^0(Q,O_Q(2)) = 5 and the span of nu_2(Q) is P^4. The assertion that the
    union of two planes is three-dimensional is removed. Their meeting only
    at p establishes that they are distinct, while C_p is three-dimensional
    as a one-parameter family of distinct planes, equivalently the cone over
    X with vertex p. This remains the card's own completion of Harris's
    parenthetical. Checked against Hartshorne IV Ex. 3.11(b), printed p.
    316, and II Ex. 7.7, printed p. 170, in the text version
    tmp/sources/hartshorne-1977-algebraic-geometry.md; neither exercise is
    credited with these two computations. No other step was re-derived.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.3.11, printed p. 89,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.3.11, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed the two dimensions in (a) ($2r+1$ for secants, $2r$ for tangent spaces) against $n>2r+1$, the chordal-plane argument in (b), and the count $4+1-1=4$ for the secant variety of the Veronese surface.
    Not checked: Yang's Solutions outside printed p. 89; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.3.11 at printed
    p. 89 beside the entries already there. No step, statement or
    hypothesis of the card changes.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read for issue #168: steps centre, lemma-criterion, corollary,
    veronese-conic, secant-dim-lower, and the bodies of secant-dim and
    closed-immersion-b.

    Harris's Proposition 11.24 and the Veronese paragraph of his Example 11.22
    were re-read in the retained extraction: the bound 2k+1 with its equality
    criterion, and the passage concluding that the secant variety of the Veronese
    surface is at most four-dimensional, with the parenthetical that it cannot be
    smaller. Shafarevich's Lemma, his Corollary 2.7 and the proof of his Theorem
    2.25 were re-read in the retained extraction and are as the steps quote them,
    including the tangent-locus count and the final step of the dimension count;
    the remark's observation that the printed Gamma contains the diagonal, and so
    has image all of P^N, is right, since for b=c every a is collinear with them.
    centre: with dim Sec(X) at most 2r+1 and dim U_2 at most 2r, the union of X,
    Sec(X) and the closure of U_2 is a proper closed subset when n>2r+1, and a
    point outside it is a centre of the kind required.
    lemma-criterion: the Nakayama argument was read line by line and is a
    faithful transcription: m_x=f^*(m_y)O_x follows from Nakayama, O_x is finite
    over f^*(O_y) by the Nullstellensatz argument separating y from f(V(alpha)),
    the quotient O_x/f^*(m_y)O_x is the residue field so the second Nakayama step
    gives f^*(O_y)=O_x, and a principal open set then carries a basis to the
    smaller ring. corollary: the three hypotheses on O were checked against the
    three closed sets removed; the projection is finite by the cited Theorem
    1.15, so the lemma applies, and the image is closed because X is projective.
    veronese-conic: recomputed. The restriction of the quadratic Veronese
    embedding to a line is [s:t] -> [s^2:st:t^2], a smooth conic spanning a
    plane, so the secant line joining two of its points lies in that plane.
    secant-dim-lower: recomputed. For a reducible conic Q in P^2, h^0(P^2,O(2))
    is 6 and h^0(Q,O_Q(2)) is 5, so the span of nu_2(Q) is a P^4; that span is
    the span of the planes of the two lines, which therefore meet only in p; the
    planes over the pencil of lines through p_0 form a three-dimensional union;
    were the secant variety three-dimensional it would equal that union for every
    p, so joining a point of Sec(X) to a point of X would stay inside it, and
    adjoining the points of X one at a time would put the linear span of X, which
    is P^5, inside Sec(X). One wording repair was made here: the step read "for k
    large enough that p_0,...,p_k span X", which a finite set of points cannot
    do, and now reads "span P^5", which is what the next clause uses.
    secant-dim and closed-immersion-b: both bodies were read; the first is the
    conjunction of the two bounds with both sources' statements of them, and the
    second chooses a point outside the four-dimensional secant variety, notes
    that secant lines and embedded tangent planes both lie inside it, and applies
    the criterion of step corollary, the image being closed because X is proper.
    Not checked: Shafarevich's Theorem 1.15 and the earlier chapters, cited for
    the finiteness of the projection and not retained; and the entries of Egbert
    and of Yang Pi-Yeh, quoted in the bodies and recorded by earlier events.
---

::: {.problem}
(a) If $X$ is a nonsingular variety of dimension $r$ in $\PP^n$, and if $n>2r+1$, show that there is a point $O \notin X$, such that the projection from $O$ induces a closed immersion of $X$ into $\PP^{n-1}$.

(b) If $X$ is the Veronese surface in $\PP^5$, which is the 2-uple embedding of $\PP^2$ (I, Ex.
2.13), show that each point of every secant line of $X$ lies on infinitely many secant lines.
Therefore, the secant variety of $X$ has dimension 4, and so in this case there is a projection which gives a closed immersion of $X$ into $\PP^4$ (II, Ex.
7.7).

(A theorem of Severi [1] states that the Veronese surface is the only surface in $\PP^5$ for which there is a projection giving a closed immersion into $\PP^4$.
Usually one obtains a finite number of double points with transversal tangent planes.)
:::


::: {.solution}

Let $X\subseteq\PP^n$ be nonsingular of dimension $r$.
Write $\operatorname{Sec}(X)$ for the closure in $\PP^n$ of the union of the secant lines $\overline{PQ}$ of $X$ over pairs of distinct points $P,Q\in X$; it is closed, and Harris writes $S(X)$ for it.
Part (a) is I. R. Shafarevich, *Basic Algebraic Geometry 1*, third edition (2013), §5.4, for the tangent bound, the lemma on isomorphic embeddings, Corollary 2.7 and the projection, and J. Harris, *Algebraic Geometry: A First Course* (1992), Lecture 11, Example 11.22, and Proposition 11.24, for the secant bound.
The steps of part (b) that rest on no published argument are the card's own and each says so; the two bounds on $\dim\operatorname{Sec}(X)$ are stated by Harris and by Egbert, the lower one with no proof in either text.

::: pf

::: {.pf-step #secants}

$\operatorname{Sec}(X)$ has dimension at most
$$
2r+1.
$$

::: pf-proof

J. Harris, *Algebraic Geometry: A First Course* (1992), Lecture 11, Proposition 11.24: "The variety $\mathcal S(X)\subset\Gr(1,n)$ of secant lines to an irreducible $k$-dimensional variety $X\subset\PP^n$ is irreducible of dimension $2k$. The secant variety $S(X)\subset\PP^n$ is irreducible of dimension at most $2k+1$, with equality holding if and only if the general point $p\in\overline{qr}$ lying on a secant line to $X$ lies on only a finite number of secant lines to $X$", with his note "that in this statement we need only consider points $p$ lying on honest secant lines, that is, secant lines actually spanned by points of $X$." His Example 11.22, defines the secant line map
$$
s\colon X\times X-\Delta\longrightarrow\Gr(1,n),\qquad (p,q)\longmapsto\overline{pq},
$$
on the complement of the diagonal and shows that its image $\mathcal S(X)$ has dimension $2k$, and closes with the incidence correspondence
$$
\Sigma=\{(l,p):p\in l\}\subset\mathcal S(X)\times\PP^n,
$$
whose image in $\PP^n$ is $S(X)$ and whose projection $\pi_1$ to the first factor is surjective with all fibres of dimension $1$; hence $\dim\Sigma=2k+1$, from which $\dim S(X)\le\dim\Sigma$, and he writes that the proposition "then follows". With this card's letters $k=r$, and a nonsingular variety is irreducible.

:::

:::

::: {.pf-step #tangent-locus}

The union of the embedded projective tangent spaces $T_PX$ of $X$ is the image $U_2$ of a closed subset $\Gamma'\subseteq\PP^n\times X$, and
$$
\dim U_2\le2r .
$$

::: pf-proof

Shafarevich, proof of Theorem 2.25: "In a similar way, to study the set $U_2$ we consider in $\PP^N\times X$ the set $\Gamma'$ consisting of points $(a,b)$ such that $a\in\Theta_b$. In exactly the same way we have projections $\psi:\Gamma'\to X$ and $\varphi:\Gamma'\to\PP^N$. For $b\in X$ we have $\dim\psi^{-1}(b)=n$ since $X$ is nonsingular, and hence $\dim\Gamma'=2n$, and since $U_2=\varphi(\Gamma')$, also $\dim U_2\le2n$."

Here $\Theta_b$ is the embedded tangent space $T_bX\subseteq\PP^N$, a linear subspace of dimension $n$ of $\PP^N$ when $X$ has dimension $n$ and is nonsingular at $b$; with this card's letters $\dim T_PX=r$, so the fibre of $\Gamma'\to X$ over $P$ has dimension $r$ and $\dim U_2\le2r$. Nothing in this passage uses the diagonal, and the identification $U_2=\varphi(\Gamma')$ is with the union of the tangent spaces itself.

:::

:::

::: {.pf-step #centre}

For $n>2r+1$ there is a point $O\in\PP^n$ lying on no secant line of $X$, in no embedded tangent space $T_PX$, and not on $X$.

::: pf-proof

Shafarevich writes $\xi$ for this point; the card uses the exercise's letter $O$.

Shafarevich, proof of Theorem 2.25, concludes: "We see that $\dim U_1\le\dim\Gamma=2n+1$ and $\dim U_2\le2n$; therefore if $N>2n+1$ then $U_1\cup U_2\ne\PP^N$, which was what we wanted."

The conclusion holds for the closures: $\operatorname{Sec}(X)$ is the closure of the union of the secant lines, and $U_2$ is the union of the embedded tangent spaces. By step [](#secants){.pf-ref} $\dim\operatorname{Sec}(X)\le2r+1$ and by step [](#tangent-locus){.pf-ref} $\dim\overline{U_2}\le2r$, so with $n>2r+1$ the two closed subsets $\operatorname{Sec}(X)$ and $\overline{U_2}$ of $\PP^n$ have dimension strictly below $n$, and $\dim X=r<n$. Hence
$$
X\cup\operatorname{Sec}(X)\cup\overline{U_2}
$$
is a proper closed subset of the irreducible $\PP^n$, and every point of its complement is a centre of the kind required: being outside $\operatorname{Sec}(X)$ it lies on no secant line, being outside $\overline{U_2}$ it lies in no embedded tangent space, and it is not on $X$.

:::

:::

::: {.pf-step #lemma-criterion}

Shafarevich, §5.4, Lemma (the one preceding Theorem 2.25): a finite map $f$ from a variety $X$ is an isomorphic embedding if and only if it is one-to-one and $d_xf$ is an isomorphic embedding of the tangent space $\Theta_x$ for every $x\in X$. The proof is a Nakayama argument.

::: pf-proof

The proof is Shafarevich's, §5.4, and runs as follows, with its own notation.

"Set $f(X)=Y$ and $\varphi=f^{-1}$. The lemma will be proved if we show that $\varphi$ is a regular map. The assertion is local in nature. For $y\in Y$, let $x\in X$ be such that $f(x)=y$. Write $U$ and $V$ for affine neighbourhoods of $x$ and $y$ with $f(U)=V$ and such that $k[U]$ is integral over $k[V]$, and continue to write $f:U\to V$ for the restriction of $f$. It is enough to prove that $f$ is an isomorphism for suitable choice of $U$ and $V$, since then $\varphi=f^{-1}$ is a regular map at $y$."

"Recall that the tangent space $\Theta_x$ is the dual vector space to $\mathfrak m_x/\mathfrak m_x^2$, where $\mathfrak m_x$ is the maximal ideal of the local ring $\mathcal O_x$. The second hypothesis of the lemma is that $f^*:\mathfrak m_y/\mathfrak m_y^2\to\mathfrak m_x/\mathfrak m_x^2$ is surjective. In other words, if $\mathfrak m_y=(u_1,\ldots,u_k)$, then the elements $f^*(u_i)+\mathfrak m_x^2$ generate $\mathfrak m_x/\mathfrak m_x^2$. We apply Nakayama's lemma (Proposition A.11) to $\mathfrak m_x$ as an $\mathcal O_x$-module. It then follows from this that $\mathfrak m_x=(f^*(u_1),\ldots,f^*(u_k))$, or in other words
$$
\mathfrak m_x=f^*(\mathfrak m_y)\mathcal O_x. \tag{2.40}
$$"

"We check that $\mathcal O_x$ is a finite module over $f^*(\mathcal O_y)$. Since $k[U]$ is a finite $k[V]$-module, it is enough to prove that each element of $\mathcal O_x$ can be expressed in the form $\xi/f^*(a)$ with $\xi\in k[U]$ and $a\notin\mathfrak m_y$. For this, it is enough to check that for $\alpha\in k[U]$ with $\alpha\notin\mathfrak m_x$ there exists an element $a\in k[V]$ with $a\notin\mathfrak m_y$ such that $f^*(a)=\alpha\beta$ with $\beta\in k[U]$. By Theorem 1.12 the set $f(V(\alpha))$ is closed, and since $f$ is one-to-one, $y\notin f(V(\alpha))$. Hence there exists a function $c\in k[V]$ such that $c=0$ on $f(V(\alpha))$ and $c(y)\ne0$. Then $f^*(c)=0$ on $V(\alpha)$ and $f^*(c)(x)\ne0$. By the Nullstellensatz, $f^*(c)^n=\alpha\beta$ for some $n>0$ and $\beta\in k[U]$. We can set $a=c^n$."

"Now we can apply Nakayama's lemma to $\mathcal O_x$ as a $f^*(\mathcal O_y)$-module. The equality (2.40) shows that $\mathcal O_x/f^*(\mathfrak m_y)\mathcal O_x=\mathcal O_x/\mathfrak m_x=k$, and hence is generated by the single element $1$. It now follows by Nakayama's lemma that $\mathcal O_x=f^*(\mathcal O_y)$."

"Let $u_1,\ldots,u_l$ be a basis of $k[U]$ as a module over $k[V]$. By what we have proved, $u_i\in\mathcal O_x=f^*(\mathcal O_y)$. Write $V'=V\setminus V(h)$ for a principal affine neighbourhood of $y$ such that all $(f^*)^{-1}(u_i)$ are regular in $U'=U\setminus V(f^*(h))$. Then $k[U']=\sum f^*k[V']u_i$. By assumption $u_i\in f^*(k[V'])$, and it follows that $k[U']=k[V']$, which means that $f:U'\to V'$ is an isomorphism. The lemma is proved."

:::

:::

::: {.pf-step #corollary}

Shafarevich, Corollary 2.7: let $X\subseteq\PP^N$ be a variety and $O\in\PP^N\setminus X$; if every line through $O$ intersects $X$ in at most one point and $O$ is not contained in the tangent space to $X$ at any point, then the projection from $O$ is an isomorphic embedding $\overline X\hookrightarrow\PP^{N-1}$ (his letter for the centre is $\xi$). Applied to a point $O$ of step [](#centre){.pf-ref} it gives a closed immersion of $X$ into $\PP^{n-1}$, which is assertion (a) of the exercise.

::: pf-proof

The statement is Corollary 2.7, and its proof there is one sentence: "It is enough to apply the lemma, together with Theorem 1.15."

Take a point $O$ of the open set of step [](#centre){.pf-ref}, which is the complement of $X\cup\operatorname{Sec}(X)\cup\overline{U_2}$ in $\PP^n$.
The corollary asks three things of it. First, $O\notin X$: that is because $X$ is one of the three closed sets removed, and for $r\ge1$ it also follows from $O\notin\operatorname{Sec}(X)$, since then $X\subseteq\operatorname{Sec}(X)$, a point of $X$ being a limit of the secant lines through it.
Second, $O$ lies outside $\operatorname{Sec}(X)$, so it lies on no line through two distinct points of $X$, and every line through $O$ therefore meets $X$ in at most one point.
Third, $O$ lies outside $\overline{U_2}$, so $O\notin T_PX$ for every $P\in X$.
The corollary's three requirements are met.

The lemma of step [](#lemma-criterion){.pf-ref} needs the projection $X\to\PP^{n-1}$ to be finite, which is what the cited Theorem 1.15 supplies. The conclusion is that the projection restricts to an isomorphism of $X$ onto its image in $\PP^{n-1}$; that image is closed, because a morphism from the projective variety $X$ is proper, so the isomorphism onto the image is a closed immersion.

:::

:::

::: {.pf-step #veronese-conic}

Now let
$$
\nu_2:\PP^2\longrightarrow X\subseteq\PP^5
$$
be the quadratic Veronese embedding. Every secant line to $X$ is contained
in the plane of a Veronese conic.

::: pf-proof

This step is the card's own.

Let a secant line join the two distinct points
$$
\nu_2(P),\nu_2(Q),
\qquad
P,Q\in\PP^2.
$$
Let
$$
\ell=\overline{PQ}\subseteq\PP^2.
$$
The restriction
$$
\nu_2\restrict_\ell:\ell\cong\PP^1\longrightarrow\PP^5
$$
is the complete quadratic Veronese embedding of $\PP^1$.
Its image
$$
C=\nu_2(\ell)
$$
is a nonsingular plane conic spanning a plane
$$
\Pi\cong\PP^2.
$$
Both endpoints of the secant lie on $C$, so their joining line lies in
$\Pi$.

:::

:::

::: {.pf-step #infinitely-many-secants}

Every point of every secant line of $X$ lies on infinitely many
secant lines of $X$.

::: pf-proof

This step is the card's own.

Let
$$
O
$$
be a point of the secant line in step [](#veronese-conic){.pf-ref}. Then
$$
O\in\Pi.
$$
Consider the pencil of all lines in $\Pi$ through $O$.

If $O\in C$, every member except the unique tangent line at the smooth point
$O$ meets $C$ in $O$ and one further distinct point.

Suppose $O\notin C$. Projection from $O$ gives a finite morphism
$$
C\longrightarrow\PP^1
$$
of degree $2$, where the target is the pencil of lines through $O$.
The original secant line from step [](#veronese-conic){.pf-ref} is one fibre containing two distinct
points. Hence this degree-two morphism is generically separable: a purely
inseparable degree-two map would be radicial and could not have such a
fibre. Therefore the geometric generic fibre consists of two distinct
points, and the same holds over a nonempty open subset of the pencil.

In either case infinitely many lines through $O$ are secants of the conic
$C$. Since
$$
C\subseteq X,
$$
they are also secant lines of the Veronese surface $X$.

:::

:::

::: {.pf-step #secant-dim-upper}

The secant variety of the Veronese surface has dimension at most $4$.

::: pf-proof

J. Harris, *Algebraic Geometry: A First Course* (1992), Lecture 11, Example 11.22, on $X=\nu_2(\PP^2)\subset\PP^5$: "suppose that $r\in\PP^5$ is a general point lying on a secant line to $X$; we may write the secant line as $\overline{\nu(p),\nu(q)}$ for some pair of points $p,q\in\PP^2$. Now, the line $L=\overline{pq}\subset\PP^2$ is carried, under the Veronese map $\nu$, to a plane conic curve $C\subset X\subset\PP^5$, and since $r\in\overline{\nu(p),\nu(q)}$, $r$ will lie on the plane $\Lambda$ spanned by $C$. But then every line through $r$ in $\Lambda$ will be a secant line to $C$, and hence to $X$. In particular, it follows that a general point lying on a secant line to $X$ lies on a one-dimensional family of secant lines to $X$. We may deduce from this that the dimension of $S(X)$ is at most $4$."

The passage from that family to the number is the card's own, and it is Proposition 11.24's equality criterion at $k=2$: his incidence correspondence $\Sigma=\{(l,p):p\in l\}$ over the variety of secant lines has dimension $2k+1=5$ at $k=2$, so $\dim\operatorname{Sec}(X)\le5$, and equality there would put the general point of a general secant line of $X$ on only finitely many secant lines, which the quoted passage denies in giving it a one-dimensional family; hence $\dim\operatorname{Sec}(X)\le4$.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.11, entry 4.3.21, prints the same bound from the same argument: after "Thus a general point on a secant line to $X$ lies on a one-dimensional family of secant lines to $X$" he writes "Since we are in $\PP^5$ at any rate, then the secant variety has dimension at most $4$."

:::

:::

::: {.pf-step #secant-dim-lower}

The secant variety has dimension at least $4$.

::: pf-proof

Harris, Example 11.22, prints it as immediate: "since it is clear on elementary grounds that $S(X)$ cannot have dimension less than $4$ (for example, the cones $\overline{p,S}$ over $S$ with vertex a point $p\in S$ would all have to coincide), we conclude that $\dim(S(X))=4$."

Egbert, entry 4.3.21, prints the same bound in one sentence: "On the other hand, the secant variety clearly has dimension at least $4$."

The completion of Harris's parenthetical is the card's own.
Write $\operatorname{Sec}(X)=\operatorname{Sec}(\nu_2(\PP^2))$ and fix $p=\nu_2(p_0)\in X$; for a line $\ell\subseteq\PP^2$ through $p_0$ let $\Pi_\ell$ be the plane of the conic $\nu_2(\ell)$, as in step [](#veronese-conic){.pf-ref}.
Every line joining $p$ to a point of the conic $\nu_2(\ell)$ is a secant line of $X$ and lies in $\Pi_\ell$; these lines sweep out $\Pi_\ell$, whose remaining points are limits of them, so $\Pi_\ell\subseteq\operatorname{Sec}(X)$ and hence
$$
C_p\coloneqq\bigcup_{\ell\ni p_0}\Pi_\ell\subseteq\operatorname{Sec}(X)
$$
over the pencil of lines through $p_0$.
Take two distinct lines $\ell,\ell'$ through $p_0$.
Their union $Q=\ell\cup\ell'$ is a (reducible) conic in $\PP^2$, so $\nu_2(Q)=\nu_2(\ell)\cup\nu_2(\ell')$ is a hyperplane section of $X$. Restriction $H^0(\PP^2,\OO(2))\to H^0(Q,\OO_Q(2))$ is surjective, with one-dimensional kernel generated by an equation of $Q$; hence $h^0(Q,\OO_Q(2))=5$, and $\langle\nu_2(Q)\rangle$ is a $\PP^4$.
That span is $\langle\Pi_\ell,\Pi_{\ell'}\rangle$, hence four-dimensional, so $\Pi_\ell$ and $\Pi_{\ell'}$ are distinct planes of it; two distinct planes of a $\PP^4$ meet in a single point, here $p$, which both contain.
The pencil through $p_0$ is one-dimensional, and the planes $\Pi_\ell$ are pairwise distinct; their union $C_p$ is the cone over $X$ with vertex $p$, hence is three-dimensional.
Were $\dim\operatorname{Sec}(X)$ equal to $3$, $C_p$ would therefore be all of $\operatorname{Sec}(X)$ for every $p\in X$: the secant variety would be a cone with vertex at each point of $X$, and for $x\in\operatorname{Sec}(X)$ and $p\in X$ the line $\overline{px}$ would lie in $\operatorname{Sec}(X)$, since $x$ lies in one of the planes $\Pi_\ell$ of $C_p$ and that plane contains $p$.
Now let $\Lambda\subseteq\operatorname{Sec}(X)$ be a linear subspace and $p\in X$; the span $\langle\Lambda,p\rangle$ lies in $\operatorname{Sec}(X)$, being the union of the lines $\overline{py}$ over $y\in\Lambda$, or $\Lambda$ itself when $p\in\Lambda$.
Adjoining points of $X$ one at a time to a first point $p_0\in X$, each span $\langle p_0,p_1,\dots,p_k\rangle$ therefore lies in $\operatorname{Sec}(X)$; for $k$ large enough that $p_0,\dots,p_k$ span $\PP^5$, which exists because $X$ spans $\PP^5$, the whole of $\PP^5$ lies in $\operatorname{Sec}(X)$, against $\dim\operatorname{Sec}(X)=3$.
Hence $\dim\operatorname{Sec}(X)\ge4$.

:::

:::

::: {.pf-step #secant-dim}

The secant variety of the Veronese surface has dimension exactly
$$
\boxed{4}.
$$

::: pf-proof

Steps [](#secant-dim-upper){.pf-ref} and [](#secant-dim-lower){.pf-ref} give the two inequalities
$$
\dim\operatorname{Sec}(X)\le4
\qquad\text{and}\qquad
\dim\operatorname{Sec}(X)\ge4,
$$
and both texts state the conclusion in that form: Harris's Example 11.22, closes "we conclude that $\dim(S(X))=4$", and Egbert's entry 4.3.21, carries the two bounds in one paragraph.

:::

:::

::: {.pf-step #closed-immersion-b}

There is a projection
$$
X\hookrightarrow\PP^4
$$
which is a closed immersion.

::: pf-proof

This step is the card's own.

By step [](#secant-dim){.pf-ref},
$$
\dim\operatorname{Sec}(X)=4,
$$
and $\operatorname{Sec}(X)$, being a closure, is a closed subset of the irreducible $\PP^5$ of dimension $5$, so
$$
\operatorname{Sec}(X)
\subsetneq
\PP^5.
$$
Choose
$$
O\in\PP^5\setminus\operatorname{Sec}(X).
$$
Every secant line of $X$ lies in $\operatorname{Sec}(X)$, and so does every embedded tangent space of the smooth surface $X$: every tangent direction is a limit of secant directions, and the projective tangent plane is the union of its tangent lines through the point.
Thus $O$ lies on neither a secant line nor an embedded tangent plane of $X$.

The criterion of step [](#corollary){.pf-ref} asks, besides that $O$ not lie on $X$, that $O$ lie on no secant line and in no embedded tangent space; both hold here, and $O\notin X$ as well, since $X\subseteq\operatorname{Sec}(X)$ for a surface and $O$ is outside $\operatorname{Sec}(X)$. Since $X$ is projective, projection from $O$ is therefore a closed immersion
$$
\boxed{X\hookrightarrow\PP^4}.
$$
This is the projection asserted in (b).

:::

:::

::: pf-qed

For (a): $\dim\operatorname{Sec}(X)\le2r+1$ and $\dim\overline{U_2}\le2r$, so for $n>2r+1$ a point $O$ lies outside $X$, outside $\operatorname{Sec}(X)$ and outside $\overline{U_2}$; every line through $O$ then meets $X$ in at most one point and $O$ lies in no embedded tangent space $T_PX$, so the projection from $O$ is one-to-one and injective on tangent spaces at closed points, hence an isomorphism of $X$ onto its image in $\PP^{n-1}$, which is closed because $X$ is projective.

For (b), with $X=\nu_2(\PP^2)$: each secant line joins two points of one Veronese conic and so lies in the plane of that conic, every point of that plane lies on infinitely many secant lines of the conic, and hence of $X$. The general point of a secant line therefore lies on a one-dimensional family of them, which bounds $\dim\operatorname{Sec}(X)$ by $4$; and the bound is attained, since $\operatorname{Sec}(X)$ three-dimensional would make the cone over $X$ with vertex at each of its points equal to $\operatorname{Sec}(X)$, and the span of $X$, which is $\PP^5$, would lie in it. A point outside that four-dimensional variety is a centre of the kind (a) produces, and projection from it embeds $X$ in $\PP^4$.

:::

:::

:::

::: {.remark title="Published solution"}
Part (a) is completed from two printed texts. The secant bound $\dim S(X)\le2r+1$ is J. Harris, *Algebraic Geometry: A First Course* (1992), Lecture 11, Proposition 11.24, which follows from the incidence correspondence over the variety of secant lines that closes his Example 11.22, the same example giving the dimension $2k$ of that variety. The rest is I. R. Shafarevich, *Basic Algebraic Geometry 1*, third edition (2013), §5.4: Theorem 2.25, states it, the lemma on isomorphic embeddings and Corollary 2.7 on the projection stand there, and the count that produces the centre is in the proof of Theorem 2.25, correctly in the tangent case.

His secant count is defective as printed. His $\Gamma$ is the set of triples $(a,b,c)$ of $\PP^N\times X\times X$ with $a,b,c$ collinear, and for $b=c$ the three points $a,b,b$ lie on a line for every $a$, so $\Gamma$ contains $\PP^N\times\Delta_X$ and its image $U_1=\varphi(\Gamma)$ is the whole of $\PP^N$, of dimension $N>2n+1$; the printed bound $\dim U_1\le\dim\Gamma=2n+1$ is then false of the set he identifies with $U_1$, and it bounds the ambient space rather than the locus of centres. The centres are the image of the part of $\Gamma$ with $b\ne c$, which the printed passage neither separates from the diagonal nor bounds. That bound is Harris's Proposition 11.24, whose incidence correspondence lies over the variety of secant lines and not over the pairs with equal entries, and step [](#secants){.pf-ref} quotes it.
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.11, gives (a) in entry 4.3.20 by citing Shafarevich's *Algebraic Geometry 1* as "theorem 9", the numbering of an earlier edition; in the 2013 edition the theorem is 2.25, and its proof contains the same secant count.

His entry 4.3.21, argues (b) for a general point of a secant line: "If $r\in\PP^5$ is a general point on a secant line $\overline{v(P)v(Q)}$ of $X$, then $\overline{pq}$ maps to a conic $C$ in $X$ and $r$ then lies on the plane spanned by $C$. Any other line on the plane passing through $r$ is also a secant line to $C$ and thus to $X$. Thus a general point on a secant line to $X$ lies on a one-dimensional family of secant lines to $X$. Since we are in $\PP^5$ at any rate, then the secant variety has dimension at most $4$. On the other hand, the secant variety clearly has dimension at least $4$."
Harris, Lecture 11, Example 11.22, takes the same route for the Veronese surface and carries it to the upper bound: the plane $\Lambda$ spanned by $C$ contains $r$, every line through $r$ in $\Lambda$ is a secant line to $C$ and hence to $X$, so a general point of a secant line to $X$ lies on a one-dimensional family of them, whence $\dim S(X)\le4$. For the lower bound he prints only the parenthetical quoted at step [](#secant-dim-lower){.pf-ref}, "the cones $\overline{p,S}$ over $S$ with vertex a point $p\in S$ would all have to coincide", and the argument that finishes it is the card's own there: were $\dim S(X)$ equal to $3$, the cone over $X$ with vertex a point $p\in X$ — three-dimensional, all of its lines joining $p$ to points of $X$ — would be the whole of $S(X)$, and that for every $p\in X$, so that joining a point of $S(X)$ to a point of $X$ would stay in $S(X)$; adjoining the points of $X$ one at a time then puts the span of $X$, which is $\PP^5$, inside $S(X)$. Both bounds are transcribed in steps [](#secant-dim-upper){.pf-ref}, [](#secant-dim-lower){.pf-ref} and [](#secant-dim){.pf-ref}, together with Egbert's statement of them in entry 4.3.21.
The clause for a general point of a secant line is what both texts give; the exercise asks it for every point of every secant line, and for those points the conic of the plane through the point is the one steps [](#veronese-conic){.pf-ref} and [](#infinitely-many-secants){.pf-ref} use.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.3.11, does (a) by taking the criterion from what it calls proposition 3.4 --- the projection from $O\notin X$ is a closed immersion exactly when $O$ lies on no secant line and in no embedded tangent space --- and then counting: the secant lines are locally a $(X\times X-\Delta)\times\PP^1$, of dimension $2r+1$, and the tangent spaces form a family of dimension $2r$, so when $n>2r+1$ a centre outside both exists. For (b) it shows every point of every secant line of the Veronese surface lies on infinitely many secant lines: if $R\in\overline{\rho(P)\rho(Q)}$ then $R$ lies in the plane of the conic $Y=\rho(\overline{PQ})$, and every line of that plane through $R$ meets the conic twice, hence is a secant again. The count that follows is right: secant lines are a $4$-parameter family, each carries a $\PP^1$ of points, and each point lies on a $1$-parameter subfamily, so $\dim\Sec\leq4+1-1=4$. Its lower bound is not an argument as printed --- four named points $\rho(1:0:0)$, $\rho(0:1:0)$, $\rho(0:0:1)$, $\rho(1:1:0)$ described as 'linearly independent' do not bound a dimension; what supplies it is that the planes of the conics $\rho(L)$, with $L$ ranging over the dual plane, form a $2$-parameter family of planes inside $\Sec$, which is the card's step [](#secant-dim-lower){.pf-ref}, the upper bound being [](#secant-dim-upper){.pf-ref}.
:::
