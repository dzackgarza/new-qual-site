---
schema: qual/card@1
id: P-AGH549MINGENUS
kind: problem
title: Minimal positive genus of a curve of given degree on the cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Adjunction
  - Intersection Theory
relations: []
review: reviewed
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.9 and the retained Egbert coordinate attempt, then
    used the immediately preceding V.4.8 classification/global-generation
    lemma. A positive-genus smooth curve is in case (c) of V.4.8. Contracting
    any line of intersection zero preserves its degree, self-intersection,
    and genus. If one stops on X_r with r>=3 and all line intersections
    positive, writing N=D+K shows N is effective by Riemann-Roch with
    chi(N)=g>0, and that N is nef because a component C of N with N.C<0
    would satisfy C^2=-1 and C.A=1 by adjunction, contradicting line
    positivity; hence N^2>=0 and D^2>=2d-6. If the contraction reaches
    X_2=Bl_{P_1,P_2} P^2, write
    D=c h+b_1(h-e_1)+b_2(h-e_2); then d=3c+2(b_1+b_2) and adjunction gives an
    explicit genus formula. Its parity cases yield the stated lower bounds,
    and explicit X_2 classes realize equality. General smooth members can be
    chosen away from the four points whose blowups recover the fixed cubic
    surface.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof against V.4.9, the V.4.8 contraction and
    global-generation lemma, and the X_2 intersection form. Checked the
    even/odd parity algebra and both equality families. Added the explicit
    justification that the globally generated remainder N has N^2>=0; no
    later-card input is used.
- event: source-checked
  by: claude
  date: 2026-11-17
  note: >-
    Read Gruson-Peskine II in its supplied text version: the definitions of
    r(O_S(C)) and F_d(r), Proposition 2.1 (printed p. 407), the proof of
    Proposition 2.1 through Lemma 2.2, Theorem 2.5 (printed p. 409), its
    necessity argument with Lemmas 2.6, 2.7, 2.9 and Proposition 2.10, and the
    table of gaps (printed p. 411). Read Bourbaki 592 printed pp. 301-302,
    Theorems 0.1-0.3 and Remark 2, and its Sections 1 and 5. Derived the case
    r = 2 of the criterion by hand from F_d(1) = 5/8 and F_d(2) = (d-1)/2 and
    checked it against all 32 rows of the table, whose F_d(2) column is the
    initial segment below (d-6)/2 for even d and below (d-5)/2 for odd d.
    Confirmed the printed statement of Ex. V.4.9 in the book text and the
    standing hypothesis of an algebraically closed field. What was not
    checked: the article body was read as an extraction whose Section 2
    statements carry a rendered-page check but whose remaining formulas do
    not, so Lemma 2.6, the Appendices and Corollary 2.3 are read from the
    extraction only; no independent file of Gruson-Peskine was consulted; and
    whether Bourbaki's Theorem 5.1 transports the attainment to characteristic
    p in this setting is not settled here.
- event: solution-reviewed
  by: claude
  date: 2026-11-17
  note: >-
    Read the whole proof and repaired two missing justifications in step
    repeat-contraction-until-x2-or-positive, which stated its conclusion for
    (-1)-curves and argued for lines: a (-1)-curve is the same curve as a line
    of X_r by adjunction, and every line of X_{r-1} is the strict transform of
    a line of X_r because a nonzero multiplicity would give an effective curve
    of nonpositive anticanonical degree. Nothing else in the proof changed,
    and the arithmetic of the even and odd cases and of both equality
    families was rechecked and stands. The remark on published solutions now
    carries Gruson-Peskine and Bourbaki 592 with their printed pages, and it
    corrects the earlier description of Egbert's V.4.9, which is a draft and
    not a proof. Not checked here: certification, and the characteristic p
    question recorded in the source-checked event above.
- event: source-checked
  by: claude
  date: 2026-11-17
  note: >-
    Checked the hypotheses of every statement now used for existence, in the
    text versions. Hartshorne: Proposition V.4.1 and Corollary V.4.2(a), that
    the conics through at most four points, no three collinear, have no
    unassigned base points and dimension 5-r; Exercise V.4.1, that X_2 is a
    nonsingular quadric with one point blown up; the use in Lemma 4.12 of the
    very-ampleness of a very ample class plus base-point-free classes;
    Corollary III.7.9 with its proof from the lemma of Enriques-Severi-Zariski
    III.7.8, both without a hypothesis on the characteristic and over an
    algebraically closed field; Remark III.7.9.1; Theorem V.1.10; and
    II.8.18, whose characteristic-zero hypothesis is exactly what Bourbaki's
    Theorem 5.1 replaces. Bourbaki 592 Section 5 whole: the definition of
    almost very ample as the condition that the locus where the differential
    has rank at most i have codimension at least i, the remark that a very
    ample system is almost very ample, and Theorem 5.1, which holds in every
    characteristic and produces reduced nonsingular but not necessarily
    irreducible divisors. Corrected the attainment tuple of the odd minimum:
    the minimum needs 8(F_d(2)-g)=16 and is attained by (2,2,2,2,0), while
    (2,2,0,0,0) gives 8 and so attains (d-3)/2. Not checked: no folio for
    Section 5 of the expose, whose printed pages 301-303 were not consulted,
    so the remark about it carries no page; and no computation in
    characteristic p was run.
- event: solution-written
  by: claude
  date: 2026-11-17
  note: >-
    Replaced the existence half of the attainment with an argument that needs
    no separability: the new step equality-members-exist, with substeps
    quadric-model, almost-very-ample, members-connected and members-smooth,
    shows that each equality class contains a nonsingular irreducible curve in
    every characteristic and that the curve avoids the four contraction
    points. It descends the even class to the quadric as the very ample
    O_Y(2,s-2), verifies that the morphism of the odd system is immersive by a
    jet computation, obtains ampleness of the odd class from Nakai's criterion
    V.1.10 and connectedness of both families from Corollary III.7.9, and gets
    smoothness from Bourbaki's Theorem 5.1. The two realization steps now cite
    it and keep the book's characteristic-zero route through V.4.8 as an
    alternative; the lower bounds, the contraction steps and every earlier
    event are unchanged. The hypotheses verified in the steps are the card's
    own, the theorems are the sources'; the identification of X_2 with a
    blowup of a quadric is Exercise V.4.1 and is flagged as an exercise.
- event: source-corrected
  by: claude
  date: 2026-11-17
  note: >-
    Corrects two claims of the source-checked event of this date by appending,
    and leaves that event as written. First, Bourbaki's Section 5 does not
    define almost very ampleness by a bound on the rank. Printed folio 312,
    read here from the scan of the expose at PDF page 13 and not from the
    extraction alone, sets Sigma_i = {x in X : dim Ker T_{phi,x} >= i} for the
    tangent map of the morphism phi, and calls a base-point-free system almost
    very ample when codim(Sigma_i, X) >= i for every i > 0, adding that a very
    ample system is almost very ample. The condition is on the dimension of
    the kernel, equivalently on rank <= dim X - i over the locus of index i,
    and is not the condition that the locus of rank <= i have codimension at
    least i: on a surface the printed definition asks codim >= 1 of the
    rank-at-most-one locus and codim >= 2 of the rank-zero locus, whereas the
    discarded reading asks codim >= 2 of the whole surface at i = 2. The step
    almost-very-ample now states the printed definition and its two surface
    conditions; the systems it treats are immersive, so every Sigma_i is
    empty. Second, II.8.18 is not a characteristic-zero theorem and is not
    what Theorem 5.1 replaces. It is Bertini for hyperplane sections of a
    nonsingular subvariety of P^n, concluding that the section is regular at
    every point, and it is the very ample case that Bourbaki's proof of
    Theorem 5.1 invokes at printed p. 312 as "[4, II, 8.18]". The Bertini
    theorem for systems without base points is the one stated in
    characteristic zero, Corollary III.10.9, which the expose cites at printed
    p. 312 as "[4, III, 10.9]", and that is the statement Theorem 5.1
    replaces. The members-smooth step now says this. Theorem 5.1 and the
    definition carry printed p. 312, which the earlier event recorded as
    missing. Not checked: no characteristic p computation was run; the
    remaining claims of the corrected event, including its use of Remark
    III.7.9.1 as the irreducibility argument, stand as written and were not
    re-read beyond what the card states.
- event: source-checked
  by: claude
  date: 2026-11-17
  note: >-
    Read the proof of Exercise V.4.1 on P-AGH541CONICSQUADRIC, steps
    conics-through-two-points-basis through graph-is-blowup-both-ways, against
    the use the attainment makes of it. That card gives the four-monomial
    basis of the conics through the two points, the base locus {P_1, P_2}, the
    base-point-freeness of the strict transforms 2H - E_1 - E_2, containment
    of the image in y_0y_3 = y_1y_2, nonsingularity of that quadric from its
    four partials, birationality onto it by the projection y_0 != 0, the
    contraction of the strict transform of x_0 = 0 alone with class
    H - E_1 - E_2 of square -1, the projection from the image point as the
    inverse rational map, the closure of the graph as simultaneously the
    blowup of the quadric at that point and X', and a proper birational map
    with finite fibres onto a nonsingular surface as an isomorphism. That is
    the identification of X_2 with a nonsingular quadric blown up at one
    point which step quadric-model needs, and its steps carry no hypothesis on
    the characteristic, which is what the attainment needs. The card now cites
    that proof there and in the remark instead of quoting the exercise, and
    the two further facts it uses, that the exceptional curve is
    F_12 = h - e_1 - e_2 and that h - e_1 and h - e_2 are the pullbacks of
    the rulings, continue to be derived on this card from intersection
    numbers. Not checked: the proof on the other card was read, not
    re-derived, and its review status is not asserted here; the citation of
    Hartshorne Proposition V.4.1 and Corollary V.4.2(a) for base-point-freeness
    and dimension three is unchanged.
- event: solution-written
  by: claude
  date: 2026-11-17
  note: >-
    Rewrote the statement of step almost-very-ample to carry Bourbaki's
    printed definition of almost very ampleness in place of the rank-at-most-i
    description, with the two conditions it comes to on a surface, and changed
    the first sentence of step members-smooth to attribute the characteristic
    zero base-point-free Bertini theorem to Corollary III.10.9 and to describe
    II.8.18 as the very ample, characteristic-free one. The citation of
    Exercise V.4.1 in step quadric-model and in the remark now links the corpus
    proof of it. The very ampleness and the immersiveness of the two systems,
    the jet computation that proves the second, the ampleness, connectedness
    and irreducibility arguments, both equality classes and both realization
    steps, the lower bounds and the contraction steps are unchanged; no step,
    label, hypothesis, bound or equality class was added, removed or weakened,
    and no earlier audit event was edited.
- event: solution-reviewed
  by: claude
  date: 2026-11-17
  note: >-
    Certified the arithmetic of the six r = 2 tuple assignments, and nothing
    else, in `proofs/cards/V49FiveSquaresTuples.sage`: 40 exact checks, exit
    0, run twice on the shared Sage development image (11.0.beta5, Python
    3.14.10, source HEAD 6301b4e43e), 1.8 s and 1.5 s of wall time, with the
    outputs, the command and the script's sha256 retained in
    `proofs/cards/V49FiveSquaresTuples.out`. Checked symbolically over $\QQ[m]$
    with $d=2m$ and $d=2m+1$: that $F_d(2)=(d-1)/2$; that the squared sums are
    4, 12, 20 for $(2,0,0,0,0)$, $(2,2,2,0,0)$, $(2,2,2,2,2)$ and 0, 8, 16 for
    $(0,0,0,0,0)$, $(2,2,0,0,0)$, $(2,2,2,2,0)$; the identity
    $\sum x_i^2=8(F_d(2)-g)$ for the genus each tuple carries; that each tuple
    is of one parity with $\abs{x_i}\le2$; that the three genera of each parity
    are exactly the integral values at $r=2$; and that the printed odd minimum
    $(d-5)/2$ needs 16, while the rejected $(2,2,0,0,0)$ gives 8 and so attains
    $(d-3)/2$. Not checked and not claimed here: the existence, smoothness,
    connectedness and irreducibility arguments of the attainment, the lower
    bound, the three printed exceptional triples, the attribution
    $r(\OO_S(C))=2$, and any geometric statement of (2.1) or (2.5); no step of
    the proof was changed, the `review:` field stays `draft`, and this event
    records no review of the geometry.
- event: solution-reviewed
  by: claude
  date: 2026-11-17
  note: >-
    Narrows the event above of this date and leaves its text as written. A
    second reading of the two source statements and of the certificate's own
    labels found four claims wider than what the script computes. First, the
    script's introduction read the r = 2 case of the source as an unrestricted
    geometric equivalence; it now quotes Proposition 2.1 (printed p. 407) with
    0 <= r <= 2d/3 and F_d(r-1) < g <= F_d(r), and Theorem 2.5 (printed p. 409)
    with g <= 1 + d(d-3)/6, r the least integer such that g <= F_d(r), and the
    three printed triples, and says that it certifies one hypothesis's
    arithmetic and neither statement. Second, the label C3 said the three genera
    of each parity are exactly the integral values at r = 2; what the check does
    is that (d-1-j)/2 lies in ZZ[m] exactly for odd j when d = 2m and even j
    when d = 2m+1, over j in 0,...,5, and that the six rows' sums are the
    corresponding 4j: an arithmetic statement about those integers, not a
    classification of the tuples a curve can carry, and the earlier phrase is
    narrowed to that. Third, the label C4 said the odd branch is excluded; the
    check is that the representative tuple (1,1,1,1,1) has squared sum 5 and
    that 8F_d(2) = 4(d-1) is divisible by 4 while 5 is not, which states two
    divisibility facts and enumerates no odd tuple. Fourth, "exactly at
    g = (d-3)/2" was uniqueness language for one equality and one inequality,
    and a further check called itself a comparison with this card while
    comparing the script's own rows; both now say what is computed, and no check
    was added, removed or weakened. Still not done here, and unchanged: the
    existence, smoothness, connectedness and irreducibility arguments, the lower
    bound, the hypotheses of either statement as a whole, the three printed
    triples, and the attribution r(O_S(C)) = 2. The certificate and its recorded
    output are linked on the card at the commit that narrowed the script, and
    the review field stays draft with the earlier source-status events standing.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A fourth retained solution read and adjudicated. Read Yang Pi-Yeh,
    Hartshorne Solutions (9 June 2019), Solution 5.4.9, printed pp. 110-111,
    rendered as page images from tmp/sources/lfwin-hartshorne-solutions.pdf,
    whose PDF page is the printed page (folios 110 and 111 at the feet of
    those pages). Checked against the book: Hartshorne V.4.9, printed p. 408,
    asks for g >= (1/2)(d-6) for even d >= 8 and g >= (1/2)(d-5) for odd
    d >= 13, the minimum attained in each range, which is what the card
    proves from Gruson-Peskine. Recomputed: the identity
    a^2 - 6a + 14 >= sum (b_i - 1)^2 is equivalent to g >= (1/2)(d-6) given
    d = 3a - sum b_i and 2g - 2 = D^2 - d, and the entry's rewriting of it is
    right; its two configurations give g = a - 2 = (1/2)(d-5) at d = 2a + 1
    and g = a - 3 = (1/2)(d-6) at d = 2a, also right. Two lines are wrong as
    printed: with sum_{i >= 2} b_i = 0 it gives g = (1/2)(a(a-3) - b(b-1))
    for the value 1 + (1/2)(a(a-3) - b(b-1)), and it takes b = a from "we
    must take b to be big enough" with no argument. The entry states that the
    two computed values are the minimum ("clearly calculating") and does not
    show it. Not checked: Yang's Solutions outside printed pp. 109-111, and
    the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now adjudicates Yang Pi-Yeh's Solution 5.4.9 at printed
    pp. 110-111 as a sketch that reaches both printed values without proving
    either, with its two wrong lines named, alongside the Egbert paragraph
    that already stood there. No step, hypothesis, bound or equality class of
    the card changes.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read the printed pages of both sources from the PDF scans, not only their
    text versions. Gruson-Peskine II: printed p. 407, the genus formula
    g = F_d(r) - (1/2) sum_2^6 alpha_i^2, Proposition 2.1 with its proof,
    which puts 2 eta = sum_2^6 alpha_i^2 with eta = F_d(r) - g, and Lemma 2.2;
    printed p. 409, the definition of M_d, Theorem 2.5 and Lemma 2.6; and
    printed p. 411, the table, whose rows begin at d = 10. Bourbaki expose
    592: printed p. 312, the definition of presque tres ample and Theorem
    5.1. The M_d question is settled: the extraction did not drop a 1/2.
    Printed p. 409 defines M_d as the maximum of sum_2^6 alpha_i^2 with no
    factor, and that is what the page prints; the factor is forced by the
    printed p. 407 formula and by 2 eta = sum alpha_i^2 in the proof of
    Proposition 2.1, and by Lemma 2.6(1): 5t^2/8 is half of 5t^2/4, the
    maximum of the sum over five alpha_i at most t/2. The intended M_d is
    therefore the maximum of (1/2) sum alpha_i^2, and the omission is the
    print's, not the extraction's. No statement of this card uses M_d.
    Not checked: any page of Gruson-Peskine outside 407, 409 and 411; its
    Appendices; and no characteristic-p computation.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read the whole proof against the exercise, the two articles and the two
    companion cards it cites. Checked: the contraction of zero-intersection
    lines and the invariance of d, D^2 and g; the strict-transform argument
    for lines; the effectivity and nefness of N = D + K_{X_r} and the bound
    D^2 >= 2d - 6; the X_2 parametrization and the genus formula; the parity
    cases and both inequality chains; the two equality classes with their
    degrees, genera and squares; the quadric model of X_2; the
    base-point-freeness and very ampleness of O_Y(2, s-2), the immersiveness
    of the odd system, the dimension count that moves a member off finitely
    many points, and connectedness and irreducibility from Corollary III.7.9
    and Remark III.7.9.1. Checked the hypotheses of every cited theorem
    against its statement. Found no error and changed no step of the proof.
    Not checked: no Sage or Lean computation was run and no certificate is
    claimed by this event; the characteristic-p attainment remains through
    Bourbaki's Theorem 5.1 with the hypotheses verified on the card; and the
    printed pages of Hartshorne's book were not re-read, only its text
    version.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Completes the source-checked event above of this date, which is left as
    written. The printed Lemma 2.6 is inconsistent beyond its item (1): exact
    maximisation of sum alpha_i^2 over conditions (3) and (4) of Lemma 2.2 gives
    5t^2/4 for t <= d/3, 5(d-3t/2)^2/9 for d/3 <= t <= 4d/9,
    t^2/4+(d-2t)^2 for 4d/9 <= t <= d/2, and (d-3t/2)^2 for
    d/2 <= t <= 2d/3. The printed item (1) is half the first, items (2) and (4)
    are the next two unhalved, and item (3) prints (d-t)^2 where the maximum
    has (d-2t)^2; at t = d/3 items (1) and (2) differ by a factor 2. None of
    this touches the card, which uses neither M_d, m_d nor Lemma 2.6. Checked
    by exact vertex enumeration for every even d at most 60 and every
    1 <= t <= 2d/3, and by the displayed inequalities; not checked beyond that
    range.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Repairs five defects found by an independent audit of the solution-reviewed
    event above of this date, which is left as written. In step
    equality-members-exist the inference "dimension at least two since M^2>0"
    is replaced by the two computations h^0(M_ev)=3(s-1) and
    h^0(M_odd)>=chi(M_odd)=3s+2 via h^2=0. In step almost-very-ample the
    product-jet argument is replaced by the V+W case analysis, the citation
    V.4.12 becomes Lemma V.4.12 (II. Ex. 7.5), and "both differentials" is
    qualified as on Y for M_ev and on X_2 for M_odd. In step
    contraction-preserves-invariants Castelnuovo's criterion V.5.7 is cited. In
    step repeat-contraction the del Pezzo degree and uniqueness (V.4.7,
    Remark V.4.7.1) are stated and the positivity conclusion is placed at every
    surface of the process, in particular X_2. In step
    d-squared-bound-r-geq-3 ampleness of -K_{X_r} is cited to Corollary V.4.7.
    Two unsupported sentences are deleted: the claim that V.4.8 is proved for
    X_2 in even-equality-realized, and the alternative "in characteristic zero
    the lemma of V.4.8 gives one as well" in odd-equality-realized. The remark
    gains the parity reason in the r=2 paragraph and the Lemma 2.6
    qualification, and loses the false statement that Bourbaki Section 1's
    criterion is used by the contraction and equality steps. No statement,
    hypothesis, bound or equality class changes.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Re-read the repaired steps. Checked the new h^0 computations, the sign
    (K_{X_2}-M_odd).(-K_{X_2}) = -(2s+10), the V+W jet case analysis at the
    three kinds of points, the del Pezzo degree argument, and the two citations
    (Corollary V.4.7, Lemma V.4.12). The proof now closes the gap the earlier
    event of this date missed. Not checked: no Sage or Lean computation; the
    characteristic-p attainment is unchanged; the source pages are those of the
    earlier events.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    The published-solution question of issue #171 is settled. Read in Gruson-Peskine II, text
    version tmp/sources/gruson-peskine-1982-genre-courbes-espace-projectif-ii.md and the printed
    pages of the retained PDF: footnote (1), printed p. 401, which fixes an algebraically closed
    field of characteristic 0; the invariants d(L), r(L) and the genus formula, printed pp. 406-407;
    Proposition 2.1, printed p. 407; Theorem 2.5 with its three exceptions, printed p. 409, and the
    derivation of the exception (9,1,2) at printed p. 410. Read Hartshorne's Exercise V.4.9, printed
    p. 408, Exercise V.4.8, Theorem V.1.9, printed p. 364, and Theorem V.4.11 with its proof,
    printed pp. 405-406, in tmp/sources/hartshorne-1977-algebraic-geometry.md. Searched the
    retained solution sets: among those in tmp/sources only Egbert's entry (printed pp. 290-291)
    and Yang Pi-Yeh's Solution 5.4.9 (printed pp. 110-111) reach V.4.9, and both are the draft and
    the sketch the remark records; the other retained sets stop before Chapter V. The public sets
    checked in the same search (NTU Algebraic Geometry II 2020 Chapter V, Wikibooks, Park, the
    dokumen.pub and wordpress mirrors) have no V.4.9. Not checked: no printed copy of either
    article or of Hartshorne was read, only the retained text version and scan; no solution set
    outside those named was searched.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card now carries the transcription the reader asked for and corrects the sentence that
    denied it. A first solution, "Published solution", transcribes Gruson-Peskine's argument at
    r = 2, citing Proposition 2.1 and Theorem 2.5 by printed page and naming Hartshorne Exercise
    V.4.9, printed p. 408: its first step is the necessity half with the r = 2 five-squares
    computation and the exception (9,1,2), its second the two attainer tuples and Proposition 2.1.
    The former solution becomes the second, titled "Independent proof, in every characteristic",
    with a head saying that it is the card's own and uses neither r nor the criterion. The remark's
    sentence "The proof above is independent of both articles" is replaced: the independent proof
    uses Bourbaki's Theorem 5.1, printed p. 312, for the characteristic-p smoothness, so the
    sentence was false as written. The remark also records that no published solution set contains
    a complete proof, gives the characteristic-0 footnote of Gruson-Peskine, and connects the
    exception (9,1,2) to the exercise's hypothesis d >= 13, with the class 3l on X_6 as the actual
    curve. No statement, bound or equality class of the exercise changes.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Re-read both solutions. Checked the transcription against the printed statements: d(L) and
    r(L) on p. 406, F_d on p. 407, the hypotheses and conclusions of 2.1 and 2.5 on pp. 407 and
    409, the derivation of the exception on p. 410, and the r = 2 arithmetic (F_d(1) = 5/8,
    F_d(2) = (d-1)/2, 8(F_d(2)-g) = 4((d-1)-2g), the tuples (2,2,2,2,2) and (2,2,2,2,0)). Checked
    the Hodge-index bound 3D^2 <= d^2 that makes 2.5 applicable, and that "positive" in 2.1 is
    read as nonnegative, from the proof of 2.1 on p. 407. Re-read the independent proof's
    unchanged steps. Not checked: no certificate or computation was run in this pass; the
    characteristic-p attainment remains the independent proof's; no printed copy of a source was
    read.
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
    One mathematical error is repaired in the same pass. The first step of the published solution
    wrote the Hodge index theorem as the equality $3D^2=(D\cdot H)^2$; it is the inequality
    $3D^2\le(D\cdot H)^2=d^2$, and the bound $g\le1+\frac16d(d-3)$ that makes Theorem 2.5 of
    [@GP82] applicable is drawn from the inequality. Checked against Theorem V.1.9, which states
    $(D\cdot H)^2\ge D^2H^2$ for $H$ ample and $D^2>0$. Not checked: no printed copy of any source
    was read.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The congruence that rules out odd squares in the $r=2$ case of the published lower bound is
    corrected, and the last page locator in the body is deleted. The step claimed that
    $8(F_d(2)-g)$ is divisible by $8$, which is false: it equals $4((d-1)-2g)$, so at even $d$,
    where $(d-1)-2g$ is odd, it is $4$ modulo $8$, and $(d,g)=(8,1)$ gives $20$. What the argument
    needs is only that the value is not $5$ modulo $8$, and that holds: the value is divisible by
    $4$, while five odd squares sum to $5$ modulo $8$. Hence the five integers, which have one
    parity, are even; each square is then $0$ or $4$ because they are of absolute value at most
    $r=2$. The six tuples, the two bounds and both equality families are unchanged, and the remark
    below already stated the divisibility by $4$. The phrase "on the same page" after Proposition
    2.1 is replaced by the proof of the proposition, so the body of the card carries no printed or
    PDF page locator; the page locators inside the earlier dated events are left as written under
    QUAL-11, and they remain the record of what was read. Checked: the divisibility for both
    parities, the six tuple sums, and that no other step asserts divisibility by $8$. Not checked:
    no source was re-read for this event, and no geometric step of either solution was touched.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read the whole card as it now stands, the problem statement, the published solution, the
    independent proof and the remark, against Hartshorne V.4.9 and the numbered statements of the
    two articles and of the companion cards it cites, and found the proof correct; no step changed
    in this pass. Checked in the published solution: that Exercise V.4.8 gives D.L >= 0 on the 27
    lines and D^2 > 0; that the Hodge index theorem (V.1.9) gives 3D^2 <= (D.H)^2 = d^2 and hence
    g <= 1 + d(d-3)/6, which is the hypothesis of Theorem 2.5; that r >= 2 because F_d(1) = 5/8 < 1
    <= g; the repaired congruence, that 8(F_d(2)-g) = 4((d-1)-2g) is divisible by 4 and so is 0 or 4
    modulo 8 and never 5, so that five integers of one parity are even, each square is 0 or 4, and
    g = (d-1-j)/2 with j in 0..5, with the six values and their parities recomputed; that the two
    printed triples other than (9,1,2) have g > F_d(2) and so fall under r >= 3, and that d = 9 is
    excluded by the exercise's d >= 13; and, in the attainment step, the decompositions
    20 = 2^2+2^2+2^2+2^2+2^2 and 16 = 2^2+2^2+2^2+2^2+0^2 with F_d(2)-g equal to 5/2 and to 2, the
    bounds 0 <= r = 2 <= 2d/3 and F_d(1) < g <= F_d(2), and the passage from a smooth connected
    curve to an irreducible one. Checked in the independent proof: the reduction to alternative (c)
    by Exercise V.4.8, lines and conics being rational; the contraction step, with Castelnuovo's
    criterion (V.5.7), D = sigma^*D', the canonical formula -K = sigma^*(-K') - E, and the
    invariance of d, D^2 and g; the induction that the descended class stays nonnegative on the
    lines, including m = 0 from ampleness of -K, and the del Pezzo classification that ends the
    process (V.4.7 and Remark V.4.7.1); the bound D^2 >= 2d - 6 on X_r with r >= 3, with N = D + K
    effective from h^2 = h^0(-D) = 0 and chi(N) = g, nef by the (-1)-curve argument, and N^2 >= 0;
    the X_2 parametrization d = 3c + 2s, D^2 = c^2 + 2cs + 2p and g = 1 + c(c-3)/2 + (c-1)s + p,
    with c = D.F_12 and b_i = D.E_i nonnegative; the parity c = d modulo 2; the four bound steps,
    including the two subtractions from g and the arithmetic of the cases c = 0, c >= 2 and c = 1,
    c >= 3; and, in the attainment, the classes M_ev and M_odd with their degrees, genera and
    squares, their base-point-freeness and dimensions, the quadric model with
    M_ev = psi^*O_Y(2,s-2), very ampleness of O_Y(2,s-2) from II Ex. 7.5, the 1-jet computation that
    makes the morphism of |M_odd| immersive, ampleness of M_odd by Nakai's criterion (V.1.10),
    connectedness of the members from Corollary III.7.9, irreducibility from Remark III.7.9.1,
    reduced nonsingular members from Theorem 5.1 of the expose through the almost-very-ampleness
    conditions on the loci Sigma_i, and the pullback to the cubic surface. Also checked: the
    statements of V.1.6, V.1.9, V.1.10, V.5.7, V.4.7, Remark V.4.7.1, II Ex. 7.5, Corollary
    III.7.9, Remark III.7.9.1, Proposition V.4.1, Corollary V.4.2(a) and Exercise V.4.1, and that
    the companion card P-AGH541CONICSQUADRIC proves the exercise cited for the quadric model. Not
    checked: no printed copy of the book or of either article was read in this pass, the text
    versions retained in tmp/sources were; no certificate or computation is claimed for this card;
    and the evidence for the statements of the two articles and of Bourbaki's Theorem 5.1 is the
    earlier source-checked events on this card, not a new reading of the sources.
---

::: {.problem}
If $C$ is an irreducible non-singular curve of degree $d$ on the cubic surface, and if the genus $g>0$, then
$$
g \geqslant \begin{cases}\frac{1}{2}(d-6) & \text{if $d$ is even, } d \geqslant 8 \\ \frac{1}{2}(d-5) & \text{if $d$ is odd, } d \geqslant 13\end{cases}
$$
and this minimum value of $g>0$ is achieved for each $d$ in the range given.
:::

::: {.solution title="Published solution"}
The exercise is Hartshorne V.4.9. Its published solution is the case $r=2$ of
Gruson--Peskine [@GP82], Proposition 2.1 and Theorem 2.5. That
article works over an algebraically closed field of characteristic $0$ (footnote (1)), and the transcription below follows its argument at $r=2$; the characteristic-$p$
attainment, which its Bertini step does not give, is supplied by the second solution on this card,
which is the card's own.

::: pf

::: {.pf-step #published-lower-bound}
For an irreducible nonsingular curve $C$ of degree $d$ and genus $g>0$ on the cubic surface,
$$
g\ge \frac{d-6}{2}\ \text{for even } d,
\qquad
g\ge \frac{d-5}{2}\ \text{for odd } d .
$$

::: pf-proof
Let $D=[C]$. By Exercise V.4.8 the class $D$ meets every one of the $27$ lines nonnegatively and
$D^2>0$; in the notation of [@GP82], §2,
$$
d(\OO_S(D))=-D\cdot K_S=d,
\qquad
r(D)=d-\max\{D\cdot E:E^2=E\cdot K_S=-1\}.
$$
The Hodge index theorem, Theorem V.1.9, applied to $D$ with $D^2>0$ and to the ample class
$H=-K_S$, gives $3D^2\le(D\cdot H)^2=d^2$, so
$g=1+\frac12(D^2-d)\le 1+\frac16d(d-3)$. Theorem 2.5 of [@GP82],
therefore applies: with $r$ the least positive integer such that $g\le F_d(r)$, where
$F_d(r)=1+\frac12\bigl((r-1)d-\frac34r^2\bigr)$, and except for the three triples $(9,1,2)$,
$(23,22,4)$ and $(27,28,4)$, the number $8(F_d(r)-g)$ is a sum of squares of five integers of one
parity and of absolute value at most $r$. Since $F_d(1)=5/8<1\le g$, one has $r\ge2$, and since
$g\le F_d(2d/3)$ one has $r\le 2d/3$, since $F_d$ is increasing on that interval.

If $r=2$ the five integers all have the same parity, and that parity is not odd: five odd squares
sum to $5$ modulo $8$, whereas
$$
8(F_d(2)-g)=4\bigl((d-1)-2g\bigr)
$$
is divisible by $4$, hence congruent to $0$ or $4$ modulo $8$, and never to $5$. So all five are
even, and each square is $0$ or $4$ because the integers are of absolute value at most $r=2$:
$$
8(F_d(2)-g)=4\bigl((d-1)-2g\bigr)=4j,\qquad j\in\{0,\dots,5\},
$$
that is, $g=(d-1-j)/2$ with $j\equiv d-1\pmod 2$. For even $d$ this gives
$g\in\{(d-2)/2,(d-4)/2,(d-6)/2\}$, and for odd $d$ it gives
$g\in\{(d-1)/2,(d-3)/2,(d-5)/2\}$; hence the two bounds. If $r\ge3$, then
$g>F_d(r-1)\ge F_d(2)=(d-1)/2$, and since $g$ is an integer this already exceeds both bounds. The
triple $(9,1,2)$ is the only exception with $g\le F_d(2)$, and $d=9$ is excluded by the exercise's
hypothesis that $d\ge13$ when $d$ is odd; the other two exceptions have $g=22>F_{23}(2)=11$ and
$g=28>F_{27}(2)=13$, so they fall under the case $r\ge3$.
:::

:::

::: {.pf-step #published-attainment}
For every even $d\ge8$ the cubic surface contains an irreducible nonsingular curve of degree $d$
and genus $(d-6)/2$, and for every odd $d\ge13$ one of degree $d$ and genus $(d-5)/2$.

::: pf-proof
Proposition 2.1 of [@GP82] states that for integers $d,r$ with $0\le r\le2d/3$ and
a positive integer $g$ with $F_d(r-1)<g\le F_d(r)$ such that $8(F_d(r)-g)$ is a sum of squares of
five integers of one parity and of absolute value at most $r$, there is a smooth connected curve on
$S$ of degree $d$, genus $g$ and $r(\OO_S(C))=r$. "Positive" is read as nonnegative: the proof of
2.1 runs with $0\le\alpha_i\le r/2$, the five integers being $2\alpha_i$ in the
even case, so they may vanish.

Take $r=2$. For even $d$ put $g=(d-6)/2$; then $F_d(2)-g=5/2$ and
$8(F_d(2)-g)=20=2^2+2^2+2^2+2^2+2^2$. For odd $d$ put $g=(d-5)/2$; then $F_d(2)-g=2$ and
$8(F_d(2)-g)=16=2^2+2^2+2^2+2^2+0^2$. In both cases $0\le r=2\le2d/3$ for $d\ge3$, $F_d(1)=5/8<g$,
and $g\le F_d(2)=(d-1)/2$; Proposition 2.1 therefore produces a smooth connected curve of the
stated degree and genus. A smooth connected curve is irreducible, because a regular local ring is a
domain and two components of a connected curve would meet at a point whose local ring would then
have two minimal primes (Remark III.7.9.1); this is the exercise's attainment clause.
:::

:::

::: pf-qed
Steps [](#published-lower-bound){.pf-ref} and [](#published-attainment){.pf-ref} are Theorem 2.5 and
Proposition 2.1 of [@GP82] at $r=2$; they prove Exercise V.4.9, over an algebraically closed field of characteristic $0$.
:::

:::
:::

::: {.solution title="Independent proof, in every characteristic"}
This proof is the card's own. It uses neither the invariant $r$ nor the five-squares criterion of
[@GP82], and it covers every characteristic, in particular the characteristic-$p$ attainment that
the published argument above does not give.

Let
$$
S=X_6=\operatorname{Bl}_{P_1,\ldots,P_6}\PP^2
$$
be the cubic surface, and put
$$
H=-K_S.
$$
If $C\subseteq S$ is the given nonsingular irreducible curve, write
$$
D=[C],
\qquad
d=H\cdot D.
$$
Adjunction gives throughout
$$
\boxed{
g
=
1+\frac{D^2-d}{2}.}
$$

::: pf

::: {.pf-step #case-c-applies}
Since $g>0$, the class $D$ is in alternative (c) of V.4.8:
$$
\boxed{
D\cdot L\ge0\text{ for every line }L,
\qquad
D^2>0.}
$$

::: pf-proof
By [[P-AGH548IRREDCLASSES]], an irreducible curve on the cubic surface is
either a line, a square-zero conic, or has the displayed properties. Lines
and conics are rational, hence have genus zero. Since $g>0$, only case (c)
can occur.
:::

:::

::: {.pf-step #contraction-preserves-invariants}
If a line $E$ satisfies
$$
D\cdot E=0,
$$
then contracting $E$ preserves the degree, self-intersection, and genus of
the curve.

::: pf-proof
Because $C$ and $E$ are distinct irreducible curves with intersection zero,
they are disjoint. By Castelnuovo's criterion (V.5.7), the $(-1)$-curve $E$ can
be contracted; let
$$
\sigma:X_r\longrightarrow X_{r-1}
$$
be the contraction with exceptional curve $E$. Then
$$
D=\sigma^*D'
$$
for the image curve $C'$, and $C\to C'$ is an isomorphism because $C$ avoids
$E$. Thus the genus is unchanged and
$$
D^2=(D')^2.
$$

The canonical formula for a point blowup is
$$
-K_{X_r}=\sigma^*(-K_{X_{r-1}})-E.
$$
Since $D\cdot E=0$,
$$
(-K_{X_r})\cdot D
=
(-K_{X_{r-1}})\cdot D'.
$$
Thus the anticanonical degree $d$ is unchanged as well.
:::

:::

::: {.pf-step #repeat-contraction-until-x2-or-positive}
Repeat step [](#contraction-preserves-invariants){.pf-ref} while a zero-intersection line exists. The process
either reaches a surface isomorphic to $X_2$, or stops on some $X_r$ with $r\ge3$ at a class,
still denoted $D$, satisfying
$$
D\cdot E>0
$$
for every $(-1)$-curve $E$.

::: pf-proof
Each contraction lowers the Picard number by one and raises $K^2$ by one, so the
process stops after finitely many steps, on a del Pezzo surface of degree
$9-s$ with $0\le s\le6$. Every del Pezzo surface of degree at least $4$ is a
blowup $\operatorname{Bl}_s\PP^2$ of the plane at $s$ points, except that in
degree $8$ there is also $\PP^1\times\PP^1$ (V.4.7 and Remark V.4.7.1), and the
del Pezzo surface of degree $7$ is $\operatorname{Bl}_2\PP^2$ up to isomorphism.
Hence the chain either stops at one of the surfaces $X_6,X_5,X_4,X_3$, of degree
at most $6$, or it reaches a surface isomorphic to $X_2$ when it reaches degree
$7$ and may then continue to degree $8$ or $9$; in the first case the second
alternative of the step holds, and in the second the first does. Step
[](#contraction-preserves-invariants){.pf-ref} shows that $d,D^2,g$ are unchanged
throughout.

It remains to check that the descended class keeps nonnegative intersection
with every line, in the sense in which the claim speaks of $(-1)$-curves. On
$X_r$, a curve $L$ with $L^2=-1$ has $L\cdot K_{X_r}=-1$ exactly when
$p_a(L)=0$, by adjunction, so the $(-1)$-curves are the curves of
anticanonical degree $1$ and square $-1$; that is what a line on $X_r$ means,
and on $X_6$ these are the $27$ lines of the book's Theorem 4.9 (twenty-seven
lines). Let
$\sigma:X_r\to X_{r-1}$ contract the zero-intersection line $E$, let
$D=\sigma^*D'$, let $F'\subseteq X_{r-1}$ be a line and let
$F\subseteq X_r$ be its strict transform. Then
$$\sigma^*F'=F+mE$$
where $m\ge0$ is the multiplicity of $F'$ at the contracted point, hence
$$D'\cdot F'=\sigma^*D'\cdot\sigma^*F'=D\cdot F+m\,(D\cdot E)=D\cdot F,$$
because $D\cdot E=0$. Here $m=0$: if $m\ge1$ then, since
$-K_{X_r}=\sigma^*(-K_{X_{r-1}})-E$ and
$F\cdot\sigma^*(-K_{X_{r-1}})=F'\cdot(-K_{X_{r-1}})=1$, the effective curve
$F$ would have
$$F\cdot(-K_{X_r})=1-m\le0,$$
which ampleness of $-K_{X_r}$ forbids. So every line of $X_{r-1}$ is the
strict transform of a line of $X_r$, and the intersection numbers of the
descended class with the lines of the new surface are those of $D$ with the
corresponding strict transforms. Since $D\cdot L\ge0$ for all $27$ lines of
$X_6$ by step [](#case-c-applies){.pf-ref}, induction gives $D\cdot L\ge0$ for
every line $L$ of every surface of the process, in particular of $X_2$. On a
surface on which the process stops with $r\ge3$ no line has intersection zero,
so all these intersections are positive.
:::

:::

::: {.pf-step #d-squared-bound-r-geq-3}
If the process stops on $X_r$ with $r\ge3$, then
$$
\boxed{D^2\ge2d-6.}
$$

::: pf-proof
Put
$$
A=-K_{X_r},
\qquad
A^2=9-r\le6,
\qquad
N=D-A=D+K_{X_r}.
$$
The class $A$ is ample: $-K_{X_r}$ is very ample by Corollary V.4.7, since
$r\le6$.
Step [](#contraction-preserves-invariants){.pf-ref} identifies $A$ with the pullback of the
hyperplane class of the cubic surface, so $d=A\cdot D$ and $A\cdot N=d-A^2$.

*$N$ is effective.* Since $A$ is ample on $X_r$ and $d=A\cdot D>0$, no
effective divisor is linearly equivalent to $-D$, so
$$
h^2\bigl(X_r,\OO_{X_r}(N)\bigr)
=
h^0\bigl(X_r,\OO_{X_r}(K_{X_r}-N)\bigr)
=
h^0\bigl(X_r,\OO_{X_r}(-D)\bigr)
=
0 .
$$
The surface $X_r$ is rational, so Riemann--Roch gives
$$
\chi\bigl(\OO_{X_r}(N)\bigr)
=
1+\frac{N\cdot(N-K_{X_r})}{2}
=
1+\frac{N\cdot D}{2}
=
1+\frac{D^2-d}{2}
=
g>0,
$$
hence $h^0(N)\ge\chi(N)-h^2(N)=g>0$: the class $N$ is effective.

*$N$ is nef.* Let $C\subseteq X_r$ be an irreducible curve with
$N\cdot C<0$. Since $N$ is effective and $C$ is irreducible, $C$ is then a
component of $N$: a curve outside $\operatorname{Supp}N$ meets every
component of $N$ nonnegatively, hence meets $N$ nonnegatively. Writing
$N=aC+N'$ with $a\ge1$ and $N'$ effective and supported away from $C$, we get
$N\cdot C=aC^2+N'\cdot C$ with $N'\cdot C\ge0$, hence $C^2<0$. Adjunction and
ampleness of $A$ give
$$
2p_a(C)-2=C^2+C\cdot K_{X_r}=C^2-C\cdot A\ge-2,
\qquad
C\cdot A\ge1,
$$
so $C^2\ge C\cdot A-2\ge-1$, and $C^2<0$ forces $C^2=-1$ and $C\cdot A=1$.
Then $p_a(C)=1+\frac12(C^2-C\cdot A)=0$, so $C$ is a $(-1)$-curve, and
$$
N\cdot C=D\cdot C-A\cdot C=D\cdot C-1\ge0
$$
by the positivity proved in step [](#repeat-contraction-until-x2-or-positive){.pf-ref},
contradicting $N\cdot C<0$. Hence $N\cdot C\ge0$ for every irreducible curve
$C$, that is, $N$ is nef.

*A nef class has nonnegative self-intersection.* For an ample class $L$ and
$\epsilon>0$ the class $N+\epsilon L$ is ample while $N\cdot L\ge0$, so
$$
0<(N+\epsilon L)^2=N^2+2\epsilon\,N\cdot L+\epsilon^2L^2
$$
for every $\epsilon>0$; letting $\epsilon\to0$ gives $N^2\ge0$.

Since
$$
d=A\cdot D=A^2+A\cdot N,
$$
one has
$$
\begin{aligned}
D^2
&=(A+N)^2\\
&=A^2+2A\cdot N+N^2\\
&=2d-A^2+N^2\\
&\ge2d-A^2\\
&\ge2d-6.
\end{aligned}
$$
:::

:::

::: {.pf-step #genus-bound-r-geq-3}
In the situation of step [](#d-squared-bound-r-geq-3){.pf-ref},
$$
g\ge\frac{d-4}{2},
$$
which is stronger than either lower bound required in the problem.

::: pf-proof
Adjunction and step [](#d-squared-bound-r-geq-3){.pf-ref} give
$$
g
=
1+\frac{D^2-d}{2}
\ge
1+\frac{(2d-6)-d}{2}
=
\frac{d-4}{2}.
$$
For even $d$ this is larger than $(d-6)/2$, and for odd $d$ it is larger
than $(d-5)/2$.
:::

:::

::: {.pf-step #x2-degree-and-square-formulas}
It remains only to analyze the case in which the contraction process
reaches
$$
X_2=\operatorname{Bl}_{P_1,P_2}\PP^2.
$$
Write
$$
D
=
c h
+
b_1(h-e_1)
+
b_2(h-e_2),
$$
with
$$
c,b_1,b_2\ge0,
$$
Put
$$
s=b_1+b_2,
\qquad
p=b_1b_2.
$$
Then
$$
\boxed{
d=3c+2s,
\qquad
D^2=c^2+2cs+2p.}
$$

::: pf-proof
On $X_2$ the classes $h$, $h-e_1$, $h-e_2$ form a basis of $\Pic X_2$, and
$$c=D\cdot(h-e_1-e_2)=D\cdot F_{12},\qquad b_i=D\cdot E_i$$
for $i=1,2$, so $c,b_1,b_2\ge0$ because $D$ meets every line nonnegatively
(step [](#repeat-contraction-until-x2-or-positive){.pf-ref}).

The anticanonical class of $X_2$ is
$$
A_2=3h-e_1-e_2.
$$
The intersection table gives
$$
A_2\cdot h=3,
\qquad
A_2\cdot(h-e_i)=2.
$$
Hence
$$
d=A_2\cdot D=3c+2b_1+2b_2=3c+2s.
$$

Also
$$
h^2=1,
\qquad
(h-e_i)^2=0,
\qquad
h\cdot(h-e_i)=1,
\qquad
(h-e_1)\cdot(h-e_2)=1.
$$
Expanding $D^2$ gives
$$
D^2=c^2+2c(b_1+b_2)+2b_1b_2
=
c^2+2cs+2p.
$$
:::

:::

::: {.pf-step #x2-genus-formula}
In the notation of step [](#x2-degree-and-square-formulas){.pf-ref}, the genus is
$$
\boxed{
g
=
1+\frac{c(c-3)}2+(c-1)s+p.}
$$

::: pf-proof
Substitute the formulas of step [](#x2-degree-and-square-formulas){.pf-ref} into adjunction:
$$
\begin{aligned}
g
&=1+\frac{D^2-d}{2}\\
&=1+
\frac{c^2+2cs+2p-(3c+2s)}2\\
&=1+\frac{c(c-3)}2+(c-1)s+p.
\end{aligned}
$$
:::

:::

::: {.pf-step #even-d-even-c}
Suppose $d$ is even. Then $c$ is even.

::: pf-proof
The formula
$$
d=3c+2s
$$
shows
$$
d\equiv c\pmod2.
$$
Thus even $d$ forces even $c$.
:::

:::

::: {.pf-step #even-c-zero-genus-formula}
If $d$ is even and $c=0$, then
$$
\boxed{
g=(b_1-1)(b_2-1).}
$$
Moreover $g>0$ forces
$$
b_1,b_2\ge2.
$$

::: pf-proof
For $c=0$, step [](#x2-genus-formula){.pf-ref} gives
$$
g=1-s+p
=
1-(b_1+b_2)+b_1b_2
=
(b_1-1)(b_2-1).
$$

Also
$$
D^2=2b_1b_2>0,
$$
so $b_1,b_2>0$. If either were $1$, the displayed genus would be zero.
Thus positive genus forces both to be at least $2$.
:::

:::

::: {.pf-step #even-c-zero-bound}
If $d$ is even, $c=0$, and $g>0$, then
$$
\boxed{g\ge\frac{d-6}{2}.}
$$

::: pf-proof
Here
$$
d=2(b_1+b_2)=2s.
$$
By step [](#even-c-zero-genus-formula){.pf-ref}, put
$$
x=b_1-1\ge1,
\qquad
y=b_2-1\ge1.
$$
Then
$$
x+y=s-2
$$
and
$$
g=xy.
$$
Since
$$
xy-(x+y-1)=(x-1)(y-1)\ge0,
$$
we obtain
$$
g\ge x+y-1=s-3
=
\frac{d-6}{2}.
$$
:::

:::

::: {.pf-step #even-c-geq-two-bound}
If $d$ is even and $c\ge2$, then again
$$
\boxed{g\ge\frac{d-6}{2}.}
$$

::: pf-proof
Subtract the desired lower bound from the genus formula. Using
$$
d=3c+2s,
$$
one finds
$$
\begin{aligned}
g-\frac{d-6}{2}
&=
4+
\frac{c(c-6)}2
+
(c-2)s
+
p.
\end{aligned}
$$

The even integer $c$ is at least $2$. If $c=2$, the right-hand side is
$$
p\ge0.
$$
If $c=4$, it is
$$
2s+p\ge0.
$$
If $c\ge6$, every displayed term is nonnegative and the constant term is
positive. Thus the difference is always nonnegative.
:::

:::

::: {.pf-step #even-d-bound-established}
Therefore, for every even
$$
d\ge8,
$$
one has
$$
\boxed{g\ge\frac{d-6}{2}.}
$$

::: pf-proof
If the contraction process stops before $X_2$, step [](#genus-bound-r-geq-3){.pf-ref} is stronger. If it
reaches $X_2$, steps [](#even-d-even-c){.pf-ref}, [](#even-c-zero-genus-formula){.pf-ref}, [](#even-c-zero-bound){.pf-ref} and [](#even-c-geq-two-bound){.pf-ref} prove the displayed inequality. This covers
every possibility.
:::

:::

::: {.pf-step #odd-d-odd-c}
Suppose $d$ is odd. Then $c$ is odd.

::: pf-proof
Again
$$
d\equiv c\pmod2
$$
by step [](#x2-degree-and-square-formulas){.pf-ref}, so odd $d$ forces odd $c$.
:::

:::

::: {.pf-step #odd-c-one-bound}
If $d$ is odd and $c=1$, then
$$
g=p=b_1b_2.
$$
Since $g>0$, one has $b_1,b_2\ge1$, and therefore
$$
\boxed{g\ge\frac{d-5}{2}.}
$$

::: pf-proof
For $c=1$, step [](#x2-genus-formula){.pf-ref} gives
$$
g=p.
$$
Positive genus therefore forces both $b_i$ to be positive. Since
$$
(b_1-1)(b_2-1)\ge0,
$$
we have
$$
p=b_1b_2\ge b_1+b_2-1=s-1.
$$
But
$$
d=3+2s,
$$
so
$$
s-1=\frac{d-5}{2}.
$$
:::

:::

::: {.pf-step #odd-c-geq-three-difference}
If $d$ is odd and $c\ge3$, then
$$
g-\frac{d-5}{2}
=
\frac72+
\frac{c(c-6)}2
+
(c-2)s
+
p.
$$

::: pf-proof
This is a direct subtraction using the formulas of steps [](#x2-degree-and-square-formulas){.pf-ref} and [](#x2-genus-formula){.pf-ref}:
$$
\frac{d-5}{2}
=
\frac{3c+2s-5}{2}.
$$
Subtracting this from
$$
1+\frac{c(c-3)}2+(c-1)s+p
$$
gives the displayed expression.
:::

:::

::: {.pf-step #odd-c-geq-three-bound}
If $d$ is odd,
$$
d\ge13,
$$
and $c\ge3$, then
$$
\boxed{g\ge\frac{d-5}{2}.}
$$

::: pf-proof
If $c=3$, then step [](#odd-c-geq-three-difference){.pf-ref} becomes
$$
g-\frac{d-5}{2}
=
s+p-1.
$$
The degree condition gives
$$
13\le d=9+2s,
$$
so $s\ge2$, and therefore the difference is nonnegative.

If $c=5$, the difference is
$$
1+3s+p>0.
$$
For every odd $c\ge7$, one has
$$
\frac{c(c-6)}2>0,
\qquad
(c-2)s\ge0,
\qquad
p\ge0,
$$
so the difference is again positive.
:::

:::

::: {.pf-step #odd-d-bound-established}
Therefore, for every odd
$$
d\ge13,
$$
one has
$$
\boxed{g\ge\frac{d-5}{2}.}
$$

::: pf-proof
The case in which the contraction process stops before $X_2$ is covered by
the stronger bound in step [](#genus-bound-r-geq-3){.pf-ref}. On $X_2$, step [](#odd-c-one-bound){.pf-ref} treats $c=1$ and step
[](#odd-c-geq-three-bound){.pf-ref} treats every odd $c\ge3$.

We now construct curves attaining equality.
:::

:::

::: {.pf-step #contraction-pullback-preserves-invariants}
Contract the four pairwise disjoint exceptional lines
$$
E_3,E_4,E_5,E_6\subseteq S.
$$
This gives a morphism
$$
\pi:S\longrightarrow X_2
=
\operatorname{Bl}_{P_1,P_2}\PP^2.
$$
If a divisor $M$ on $X_2$ has a nonsingular irreducible member avoiding the
four contraction points, its pullback is a nonsingular irreducible curve on
$S$ with the same degree and genus.

::: pf-proof
The four exceptional curves are disjoint $(-1)$-curves, so they can be
contracted successively. If a curve $C_2\in\linearsystem{M}$ avoids the four image points,
its inverse image is its strict transform and is isomorphic to $C_2$.

If $D=\pi^*M$, then $D\cdot E_i=0$ for $i=3,\ldots,6$. Applying the
canonical blowup formula four times gives
$$
H_S\cdot D
=
(-K_{X_2})\cdot M.
$$
Self-intersection is also preserved under pullback:
$$
D^2=M^2.
$$
Hence adjunction gives the same genus on both surfaces.
:::

:::

::: {.pf-step #even-equality-class}
Let $d=2s$ be even with $d\ge8$, so $s\ge4$. On $X_2$ set
$$
\boxed{
M_{\mathrm{ev}}
=
2(h-e_1)
+
(s-2)(h-e_2).}
$$
Then
$$
\deg M_{\mathrm{ev}}=d,
\qquad
g(M_{\mathrm{ev}})=\frac{d-6}{2}.
$$

::: pf-proof
This is the notation of step [](#x2-degree-and-square-formulas){.pf-ref} with
$$
c=0,
\qquad
b_1=2,
\qquad
b_2=s-2.
$$
Thus
$$
d=2(2+s-2)=2s
$$
and, by step [](#even-c-zero-genus-formula){.pf-ref},
$$
g
=(2-1)((s-2)-1)
=
s-3
=
\frac{d-6}{2}.
$$
Also
$$
M_{\mathrm{ev}}^2=4(s-2)>0.
$$
:::

:::

::: {.pf-step #odd-equality-class}
Let $d=2s+3$ be odd with $d\ge13$, so $s\ge5$. On $X_2$ set
$$
\boxed{
M_{\mathrm{odd}}
=
h
+
(h-e_1)
+
(s-1)(h-e_2).}
$$
Then
$$
\deg M_{\mathrm{odd}}=d,
\qquad
g(M_{\mathrm{odd}})=\frac{d-5}{2}.
$$

::: pf-proof
Here
$$
c=1,
\qquad
b_1=1,
\qquad
b_2=s-1.
$$
Step [](#x2-degree-and-square-formulas){.pf-ref} gives
$$
d=3+2(1+s-1)=2s+3.
$$
Step [](#odd-c-one-bound){.pf-ref} gives
$$
g=b_1b_2=s-1
=
\frac{(2s+3)-5}{2}
=
\frac{d-5}{2}.
$$
The square is
$$
M_{\mathrm{odd}}^2
=
1+2s+2(s-1)
=
4s-1>0.
$$
:::

:::

::: {.pf-step #equality-members-exist}
Each of the two classes $M_{\mathrm{ev}}$ and $M_{\mathrm{odd}}$ contains a
nonsingular irreducible curve, in every characteristic, and such a curve can
be chosen to avoid any prescribed finite set of points of $X_2$, in particular
the four points that step [](#contraction-pullback-preserves-invariants){.pf-ref} contracts to.

::: pf-proof
Both classes are base-point-free --- $M_{\mathrm{ev}}$ is the pullback of the
very ample $\OO_Y(2,s-2)$, and $M_{\mathrm{odd}}=A+B$ is a sum of two
base-point-free classes --- so the members through a prescribed point
form a hyperplane of the linear system. The two systems have dimension at least
two: $M_{\mathrm{ev}}=\psi^*\OO_Y(2,s-2)$ has $h^0=3(s-1)$ and
$\dim\linearsystem{M_{\mathrm{ev}}}=3s-4\ge8$, while
$h^2(M_{\mathrm{odd}})=h^0(K_{X_2}-M_{\mathrm{odd}})=0$ because
$(K_{X_2}-M_{\mathrm{odd}})\cdot(-K_{X_2})=-(2s+3)-7<0$ and $-K_{X_2}$ is ample,
so Riemann--Roch gives
$h^0(M_{\mathrm{odd}})\ge\chi(M_{\mathrm{odd}})
=1+\frac12(M_{\mathrm{odd}}^2+2s+3)=3s+2$ and
$\dim\linearsystem{M_{\mathrm{odd}}}\ge3s+1\ge16$.
The nonsingular members of a linear system form an open subset: the pairs $(x,H)$ with $x$ a
singular point of $\varphi^{-1}(H)$ are closed in $X\times\linearsystem{L}$, and their image in
$\linearsystem{L}$ is closed because $X$ is proper. Hence finitely many nonempty open conditions in
a projective space have nonempty intersection, so it is enough to find one nonsingular irreducible
member of each system and then to move it off the prescribed points.

The two classes are treated by different routes because only
$M_{\mathrm{ev}}$ descends along a blowdown of $X_2$. In a presentation
$X_2=\operatorname{Bl}_{P_1,P_2}\PP^2$ a class
$D=c h+b_1(h-e_1)+b_2(h-e_2)$ has degree $d=3c+2(b_1+b_2)$, so $d\equiv c$
modulo $2$; a class of odd degree therefore meets the third line
$h-e_1-e_2$ positively, whereas $M_{\mathrm{ev}}$ meets it in $c=0$.

::: {.pf-step #quadric-model}
The system $\linearsystem{2h-e_1-e_2}$ is base-point-free of dimension three
and defines a morphism $\psi:X_2\to Y$ onto a nonsingular quadric surface
$Y\subseteq\PP^3$ that exhibits $X_2$ as $Y$ with one point blown up. Its
exceptional curve is $F_{12}=h-e_1-e_2$, the two rulings of $Y$ pull back to
$h-e_1$ and $h-e_2$, and
$$M_{\mathrm{ev}}=\psi^*\OO_Y(2,s-2).$$

::: pf-proof
Proposition 4.1 gives that the conics through $P_1$ and $P_2$ have no
unassigned base points, and Corollary 4.2(a) gives
$\dim\linearsystem{2h-e_1-e_2}=3$, so $\psi$ is a morphism to $\PP^3$; the
statement of [[P-AGH541CONICSQUADRIC|Exercise V.4.1]], proved on that card,
gives that its image is a nonsingular quadric surface and that $X_2$ is that
quadric with one point blown up. Exactly one curve is contracted, and
$$(2h-e_1-e_2)\cdot F_{12}=2-1-1=0,$$
while $(2h-e_1-e_2)\cdot(h-e_i)=1$ for $i=1,2$, so that curve is $F_{12}$.
The classes $h-e_1$ and $h-e_2$ have square zero, meet each other in one
point, are not contracted, and their sum is
$$(h-e_1)+(h-e_2)=2h-e_1-e_2=\psi^*H_Y,$$
so they are the pullbacks of the two rulings of $Y$; hence
$$M_{\mathrm{ev}}=2(h-e_1)+(s-2)(h-e_2)=\psi^*\OO_Y(2,s-2).$$
:::

:::

::: {.pf-step #almost-very-ample}
The class $\OO_Y(2,s-2)$ is very ample, and the morphism defined by
$\linearsystem{M_{\mathrm{odd}}}$ is immersive, its differential being
injective at every point of $X_2$. Both systems are therefore almost very
ample. For a base-point-free system on a surface $X$, with associated
morphism $\varphi$ and
$$
\Sigma_i=\{x\in X:\dim\ker T_{\varphi,x}\ge i\},
$$
almost very ampleness is the condition $\codim(\Sigma_i,X)\ge i$ for every
$i>0$ (Bourbaki's exposé 592, §5); on a surface it is the
pair of conditions that the locus where the differential has rank at most one
is of codimension at least one and the locus where it vanishes is of
codimension at least two. A very ample system is almost very ample, and here
both differentials are injective at every point --- on $Y$ for
$\OO_Y(2,s-2)$, on $X_2$ for $M_{\mathrm{odd}}$ --- so every $\Sigma_i$ is empty
and the condition holds.

::: pf-proof
For the first, write
$$\OO_Y(2,s-2)=\OO_Y(1,1)+\OO_Y(1,0)+(s-3)\OO_Y(0,1)$$
with $s-3\ge0$: the hyperplane class $\OO_Y(1,1)$ of the embedding of $Y$ in
$\PP^3$ is very ample, the two ruling classes are base-point-free, and a sum
of a very ample class and base-point-free classes is very ample, the form in
which the proof of Lemma V.4.12 uses this (II. Ex. 7.5).

For the second, write
$$M_{\mathrm{odd}}=(h-e_1)+(s-1)(h-e_2)+h=A+B,$$
where $A=\psi^*\OO_Y(1,s-1)$ and $B=h=\pi^*\OO_{\PP^2}(1)$ for the blowdown
$\pi:X_2\to\PP^2$. Both are base-point-free, and the product of a section of
$A$ and a section of $B$ is a section of $M_{\mathrm{odd}}$ whose $1$-jet at a
point $x$ is $a(x)\,db_x+b(x)\,da_x$. Let $V$ and $W$ be the spans of the
$1$-jets at $x$ of $A$ and of $B$. The product $ab$ has jet
$a(x)\beta+b(x)\alpha$ for $\alpha\in V$, $\beta\in W$. If either span is
two-dimensional it is the whole cotangent space; if both are one-dimensional
and distinct, a product with $a(x)b(x)\ne0$ is a nonzero combination of two
independent forms; and if they coincide, the products with $a(x)b(x)\ne0$ give
that line. Hence the $1$-jets of $H^0(M_{\mathrm{odd}})$ span the cotangent
space at every point: off $F_{12}$ or off $e_1\cup e_2$ because one of the two
spans is two-dimensional, and at a point of $F_{12}\cap e_i$ because the two
one-dimensional spans are distinct.

Now $A$ is the pullback of a very ample class along a morphism that is an
isomorphism away from $F_{12}$, so its jets span the cotangent space at every
$x\notin F_{12}$, and at $x\in F_{12}$ they span the line annihilating
$T_xF_{12}$; $B$ is the pullback of $\OO_{\PP^2}(1)$ along the blowdown
$\pi$, so its jets span the cotangent space at every $x\notin e_1\cup e_2$,
and at $x\in e_i$ they span the line annihilating $T_xe_i$. Hence off
$F_{12}\cup e_1\cup e_2$ either span is everything, on
$F_{12}\setminus(e_1\cup e_2)$ and on $e_i\setminus F_{12}$ one of the two
is, and at a point of $F_{12}\cap e_i$ the two lines are distinct, because
$F_{12}\cdot e_i=1$ means that the two curves meet transversally there. The
two spans therefore generate the cotangent space at every point, the
differential is injective everywhere, and the system is almost very ample.
:::

:::

::: {.pf-step #members-connected}
The support of every member of $\linearsystem{\OO_Y(2,s-2)}$ and of every
member of $\linearsystem{M_{\mathrm{odd}}}$ is connected.

::: pf-proof
$\OO_Y(2,s-2)$ is ample, being very ample. For $M_{\mathrm{odd}}$ one has
$M_{\mathrm{odd}}\cdot F_{12}=1$, and for an irreducible curve $C\ne F_{12}$
one has $A\cdot C=\OO_Y(1,s-1)\cdot\psi_*C>0$, because $\psi_*C$ is a nonzero
effective cycle and $\OO_Y(1,s-1)$ is ample, while $h\cdot C\ge0$; moreover
$$M_{\mathrm{odd}}^2=(s+1)^2-1-(s-1)^2=4s-1>0.$$
Nakai's criterion (V.1.10) therefore makes $M_{\mathrm{odd}}$ ample. Corollary
III.7.9 states that a closed subset of codimension one of an integral normal
projective surface is connected when it is the support of an effective ample
divisor, and the support of a member of an ample class is such a subset.
:::

:::

::: {.pf-step #members-smooth}
Each of the two systems has a member that is reduced and nonsingular, avoids
any prescribed finite set of points, and, by step [](#members-connected){.pf-ref}, is irreducible.

::: pf-proof
Theorem 5.1 of Bourbaki's exposé 592 states that an almost
very ample linear system on a nonsingular projective variety has a nonempty
Zariski open subset all of whose members are reduced nonsingular divisors, and
it imposes no hypothesis on the characteristic. What it replaces here is the
Bertini theorem for systems without base points, which is stated only in
characteristic zero (Corollary III.10.9), and not the earlier Bertini theorem
II.8.18: that one is Bertini for hyperplane sections of a nonsingular
subvariety of $\PP^n$, it concludes that the section is regular at every
point and needs no hypothesis on the characteristic, and it is the very ample
case that Bourbaki's proof of Theorem 5.1 invokes by citation. A regular
local ring is an integral domain, so at a point of a reduced scheme all of
whose local rings are regular exactly one irreducible component passes, the
components are pairwise disjoint, and a connected scheme with pairwise
disjoint components is irreducible, which is the argument of Remark
III.7.9.1.

Membership of a prescribed point is a hyperplane condition on the linear
system, so a member can be chosen inside the open set of that theorem and
outside finitely many hyperplanes. For $M_{\mathrm{ev}}$ the member is chosen
on $Y$, avoiding the point over which $F_{12}$ lies and the images of the
prescribed points that lie outside $F_{12}$; its pullback is a member of
$\linearsystem{M_{\mathrm{ev}}}$ by step [](#quadric-model){.pf-ref} and avoids all of them, since the
whole of $F_{12}$ lies over that one point.
:::

:::
:::

:::

::: {.pf-step #even-equality-realized}
A member of $\linearsystem{M_{\mathrm{ev}}}$ that is nonsingular and
irreducible can be chosen to avoid the four contraction points of
step [](#contraction-pullback-preserves-invariants){.pf-ref}, and its pullback to $S$ attains the even minimum.

::: pf-proof
Step [](#equality-members-exist){.pf-ref} supplies such a member in every characteristic, through the
descent $M_{\mathrm{ev}}=\psi^*\OO_Y(2,s-2)$ of step [](#quadric-model){.pf-ref}, the very ampleness of that
class in step [](#almost-very-ample){.pf-ref}, the connectedness of its members in step [](#members-connected){.pf-ref} and
the smoothness theorem of step [](#members-smooth){.pf-ref}. Step [](#contraction-pullback-preserves-invariants){.pf-ref} then pulls the curve back to a nonsingular
irreducible curve on the cubic surface, of degree $d$ and genus
$$\frac{d-6}{2},$$
the degree and genus of the class by step [](#even-equality-class){.pf-ref}.
:::

:::

::: {.pf-step #odd-equality-realized}
A member of $\linearsystem{M_{\mathrm{odd}}}$ that is nonsingular and
irreducible can be chosen away from the four contraction points, and its
pullback to $S$ attains the odd minimum.

::: pf-proof
$$M_{\mathrm{odd}}=h+(h-e_1)+(s-1)(h-e_2)$$
is a nonnegative integral combination of $h,h-e_1,h-e_2$, and its square is
positive by step [](#odd-equality-class){.pf-ref}. Step [](#equality-members-exist){.pf-ref} supplies a
nonsingular irreducible member in every characteristic, through the
immersiveness of the system in step [](#almost-very-ample){.pf-ref}, the ampleness of $M_{\mathrm{odd}}$ in
step [](#members-connected){.pf-ref} and the smoothness theorem of step [](#members-smooth){.pf-ref}. Step
[](#contraction-pullback-preserves-invariants){.pf-ref} then pulls the curve back to a nonsingular irreducible curve
on the cubic surface, of degree $d$ and genus
$$\frac{d-5}{2},$$
the degree and genus of the class by step [](#odd-equality-class){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#case-c-applies){.pf-ref}, [](#contraction-preserves-invariants){.pf-ref}, [](#repeat-contraction-until-x2-or-positive){.pf-ref}, [](#d-squared-bound-r-geq-3){.pf-ref}, [](#genus-bound-r-geq-3){.pf-ref}, [](#x2-degree-and-square-formulas){.pf-ref}, [](#x2-genus-formula){.pf-ref}, [](#even-d-even-c){.pf-ref}, [](#even-c-zero-genus-formula){.pf-ref}, [](#even-c-zero-bound){.pf-ref}, [](#even-c-geq-two-bound){.pf-ref}, [](#even-d-bound-established){.pf-ref}, [](#odd-d-odd-c){.pf-ref}, [](#odd-c-one-bound){.pf-ref}, [](#odd-c-geq-three-difference){.pf-ref}, [](#odd-c-geq-three-bound){.pf-ref} and [](#odd-d-bound-established){.pf-ref} prove the lower bounds. Steps [](#contraction-pullback-preserves-invariants){.pf-ref}, [](#equality-members-exist){.pf-ref}, [](#even-equality-class){.pf-ref} and [](#even-equality-realized){.pf-ref} construct an
equality curve for every even $d\ge8$, and steps [](#odd-equality-class){.pf-ref} and [](#odd-equality-realized){.pf-ref} construct one
for every odd $d\ge13$.
:::

:::
:::

::: {.remark title="Published solution"}
The published argument is [@GP82], read in the text version `tmp/sources/gruson-peskine-1982-genre-courbes-espace-projectif-ii.md`; it is characteristic $0$ by footnote (1), and the transcription of it at $r=2$ is the first solution above. No published solution set contains a complete proof of the exercise: the two retained sets that reach Chapter V, Egbert and Yang Pi-Yeh, are dealt with at the end of this remark, and every other retained set stops before Chapter V. For a class on a smooth cubic surface they set $d=-C\cdot K_S$, $r=d-\max\{C\cdot E: E^2=E\cdot K_S=-1\}$ and $F_d(r)=1+\frac12\bigl((r-1)d-\frac34r^2\bigr)$. Proposition 2.1 is the existence half: for integers $0\le r\le 2d/3$ and $g$ with $F_d(r-1)<g\le F_d(r)$ such that $8(F_d(r)-g)$ is a sum of squares of five integers of one parity and of absolute value at most $r$, there is a nonsingular connected curve of degree $d$ and genus $g$ on $S$. Theorem 2.5 is the converse, so the two decide every pair $(d,g)$ with $g\le1+d(d-3)/6$, the printed exceptions being $(d,g,r)=(9,1,2)$, $(23,22,4)$ and $(27,28,4)$. The five integers of the criterion are read as nonnegative: the proof of 2.1 runs with $0\le\alpha_i\le r/2$ in the even case, where the five entries are $2\alpha_i$ and may vanish, and with five odd $\beta_i$ of absolute value at most $r$ in the odd case. The $M_d(r)$ that the proof uses is the maximum of $\frac12\sum_2^6\alpha_i^2$: the definition prints the sum without the factor, but the genus formula is $g=F_d(r)-\frac12\sum_2^6\alpha_i^2$ and the proof of Proposition 2.1 there sets $2\eta=\sum_2^6\alpha_i^2$ with $\eta=F_d(r)-g$, while Lemma 2.6(1) gives $m_d(t)=5t^2/8$, half of the maximum $5t^2/4$ of the sum over five $\alpha_i\le t/2$; the factor is therefore forced, its absence is the print's, and no statement above uses $M_d$. The printed Lemma 2.6 is inconsistent for the same reason: its item (1) is in the halved normalization, items (2) and (4) are in the unhalved one, and item (3) is misprinted; no statement above uses any of them.

Both halves of the exercise are the case $r=2$. Since $F_d(1)=5/8$, a genus $g>0$ has $r\ge2$; and if $g\le F_d(2)=(d-1)/2$, the criterion reads $8(F_d(2)-g)=4\bigl((d-1)-2g\bigr)$; this is divisible by $4$, while five odd squares sum to $5$, so the five integers are even and each square is $0$ or $4$. Hence $(d-1)-2g\in\{0,\dots,5\}$ and $g\in\{(d-1)/2-j/2\}$. For even $d$ only $j=1,3,5$ give an integer, so the genera at most $(d-1)/2$ are $(d-2)/2$, $(d-4)/2$ and $(d-6)/2$, attained by the tuples $(2,0,0,0,0)$, $(2,2,2,0,0)$ and $(2,2,2,2,2)$; for odd $d$ only $j=0,2,4$ do, giving $(d-1)/2$, $(d-3)/2$ and $(d-5)/2$, attained by $(0,0,0,0,0)$, $(2,2,0,0,0)$ and $(2,2,2,2,0)$. In each parity it is the last tuple that has $\sum x_i^2=8(F_d(2)-g)$ with $g$ the printed minimum, $(d-6)/2$ and $(d-5)/2$ respectively, and the two smaller tuples give the genera above it. The arithmetic of these six assignments --- the squared sums and the identity $\sum x_i^2=8(F_d(2)-g)$ for $d=2m$ and $d=2m+1$ --- is certified exactly in [the certificate script](https://github.com/dzackgarza/new-qual-site/blob/d4122f28c509b86fb8f1ad5e9c80e7b72ccbae75/proofs/cards/V49FiveSquaresTuples.sage), whose recorded run, with the interpreter, the source revision and the timings, is [its recorded output](https://github.com/dzackgarza/new-qual-site/blob/d4122f28c509b86fb8f1ad5e9c80e7b72ccbae75/proofs/cards/V49FiveSquaresTuples.out); there the rejected $(2,2,0,0,0)$ has squared sum $8$, which is $8(F_d(2)-g)$ at $g=(d-3)/2$ and not at the minimum, while the minimum $(d-5)/2$ is where $8(F_d(2)-g)$ equals the squared sum $16$ of $(2,2,2,2,0)$. That certificate covers this arithmetic and no more: the squared-sum condition is one hypothesis of (2.1) and of (2.5), it proves neither statement, and it says nothing about the existence of a curve, about the lower bound, or about the classification. A genus above $F_d(2)$ is at least $\lfloor(d-1)/2\rfloor+1$, which already exceeds both bounds. So (2.5) gives the lower bound for every even $d\ge8$ and every odd $d\ge13$, and (2.1) the attainment; of the three exceptional triples only $(9,1,2)$ lies below $F_d(2)$, at the odd degree $9$ that the printed range excludes. The table is the independent check: its rows begin at $d=10$ --- no degree at most $9$ has a gap --- and in each of the $32$ rows the column headed $F_d(2)$ reads $\{1,\dots,(d-6)/2-1\}$ for even $d$ and $\{1,\dots,(d-5)/2-1\}$ for odd $d$, which leaves the bound itself as the least genus. The exception $(9,1,2)$ is the only one of the three with $g\le F_d(2)$: on $X_6$ the class $3l$ has $d=-K\cdot3l=9$, square $9$ and genus $1$, and it meets the $27$ lines nonnegatively, since $3l\cdot E_i=0$, $3l\cdot F_{ij}=3$ and $3l\cdot G_j=6$, so V.4.8(c) gives it an irreducible nonsingular member; the bound $(d-5)/2$ therefore fails at $d=9$, and the exercise's hypothesis $d\ge13$ in the odd case is exactly what excludes it. The article derives this exception.

The Bourbaki exposé [@Har82], text version `tmp/sources/hartshorne-1982-genre-courbes-bourbaki-592.md`, treats a different question and does not close the exercise. Theorem 0.1, classifies the pairs $(d,g)$ of a curve in $\PP^3$ according to the surface containing it, and Theorem 0.2, produces a curve of degree $d$ and genus $g$ on a smooth cubic surface only for $g>\frac{1}{\sqrt3}d^{3/2}-d+1$, which for $d\ge10$ exceeds $(d-6)/2$: it says nothing about the bottom of the range, where the exercise's minimum sits. What it supplies is the framework. Its §1 quotes the class criterion of Hartshorne's Lemma V.4.12 and Ex. V.4.8 in the form $a\ge b_1+b_2+b_3$, $b_1\ge\cdots\ge b_6\ge0$ imply an irreducible nonsingular member, except for the classes $(n;n,0,\dots,0)$ with $n>1$, a criterion the proof above does not invoke, since it uses the explicit classes on $X_2$ and Theorem 5.1 instead; and Remark 2, closing that section, states that the converse of its Lemma 1.1 is what computes the list of gaps for a given degree, and that converse is (2.5). Its §5 records that Gruson and Peskine assumed characteristic $0$ in order to apply Bertini, and supplies a characteristic-free substitute, Theorem 5.1 , which produces reduced nonsingular members of a system that is almost very ample --- the locus where the differential of the associated morphism has kernel of dimension at least $i$ being of codimension at least $i$, for every $i>0$ --- and says nothing about their irreducibility. The lower bound above uses no Bertini and holds in every characteristic. The attainment needs both properties, and the hypotheses that Theorem 5.1 does not check are supplied in the steps above: that $\OO_Y(2,s-2)$ is very ample, which makes the even system's general member smooth by the theorem applied on the quadric, and that the morphism of $\linearsystem{M_{\mathrm{odd}}}$ is immersive, which makes that system almost very ample. Connectedness comes from Hartshorne's Corollary III.7.9, whose proof rests on the lemma of Enriques--Severi--Zariski (III.7.8) and which is stated over an algebraically closed field of any characteristic, applied to the ample classes $\OO_Y(2,s-2)$ and $M_{\mathrm{odd}}$, the latter ample by Nakai's criterion (V.1.10); connectedness together with regularity gives irreducibility by the argument of Remark III.7.9.1. The one step of that chain that is not proved in Hartshorne's text is the identification of $X_2$ with a blowup of a quadric, which is his Exercise V.4.1; it is proved in the corpus at [[P-AGH541CONICSQUADRIC]], which the quadric-model step of the proof above cites, and the exceptional curve and the two rulings are derived from it there and on this card rather than quoted. Hartshorne's standing convention is that a variety is over an algebraically closed field, with no characteristic fixed, which is the setting of the exercise.

The card's independent proof, the second solution above, does not use either article's classification of the pairs $(d,g)$: it contracts the zero-intersection lines to $X_2$, uses Ex. V.4.8 once, on $X_6$, for the case (c) alternatives, and exhibits the equality curves as explicit classes on $X_2$ pulled back to $X_6$. It uses neither the invariant $r$, nor the five-squares criterion, nor the table. It does use Theorem 5.1 of Bourbaki's exposé 592 in its step on smoothness, for the smoothness of the equality members in every characteristic, in place of the characteristic-zero Corollary III.10.9.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, V.4.9 is a working draft and not a proof: its lower-bound half is a chain of unattributed algebraic manipulations that does not close, and its existence half fixes $b_6^2=3$ and then applies the five-squares lemma of Bourbaki's Proposition 2.1 with $k=a$, which does not respect the degree $d=3a-\sum b_i$ that it is meant to realize.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 5.4.9 reaches both printed values and proves neither. It writes $d=3a-\sum b_i$ and $g=\frac12(a-1)(a-2)-\frac12\sum b_i^2+\frac12\sum b_i$, uses $b_6\ge0$, $a\ge b_1+b_2$ and $2a\ge b_1+\cdots+b_5$ — which is what an irreducible curve gives, since $D\cdot E_i=b_i\ge0$, $D\cdot F_{ij}=a-b_i-b_j\ge0$ and $D\cdot G_j=2a-\sum_{i\ne j}b_i\ge0$ — and rewrites $g\ge\frac12(d-6)$ as $a^2-6a+14\ge\sum(b_i-1)^2$, correctly. It then computes the two configurations $(b_1,1,0,\ldots,0)$ and $(b_1,2,0,\ldots,0)$, getting $g=a-2=\frac12(d-5)$ at $d=2a+1$ and $g=a-3=\frac12(d-6)$ at $d=2a$, both correctly. What it does not do is show that the minimum over the feasible classes is attained in those two families; it writes only "clearly calculating, this two value is the minimal bound of $g$ when $g>1$". Two of its steps are also wrong as printed: with $\sum_{i\ge2}b_i=0$ it gives $g=\frac12\bigl(a(a-3)-b(b-1)\bigr)$, where the value is $1+\frac12\bigl(a(a-3)-b(b-1)\bigr)$, and it takes $b=a$ because "we must take $b$ to be big enough" with no argument that the minimum wants that end of the range. Its entry is a sketch, of the same standing as Egbert's, and what proves the exercise's two statements is the pair of articles above.
:::
