---
schema: qual/card@1
id: P-AGH374COHOMCLASS
kind: problem
title: The cohomology class of a subvariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Duality
  - Sheaves of Differentials
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: "Read Exercise III.7.4, the definition and uniqueness of a dualizing sheaf with trace in III.7.1--7.2, the canonical-sheaf identification III.7.11--7.13, and Hartshorne's warning in III.7.14 that the preceding construction gives little explicit information about the trace. The source exercise suppresses a necessary normalization: scaling the trace on a smooth subvariety scales its class. The statement below makes the standard trace/Gysin normalization explicit before proving the four requested assertions."
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step pass against the book. III.7.1(a) printed p. 240 (Fix one
    such isomorphism), III.7.2 p. 241 (the trace is part of the dualizing
    pair), III.7.1.1 pp. 240-241 (the Cech cocycle generator), III.7.12 p.
    246, III.7.13 p. 247 (the duality isomorphism the exercise uses),
    III.7.14 p. 247 (the trace is known only to exist), III.7.14.1(c) p. 247
    (res_P f^-1 df = v_P(f)), Appendix A C1 p. 430 (c_1(L(D)) = D), II.8.18
    p. 179 (Bertini, every characteristic), I.7.7 p. 53 (Bezout), Exercise
    7.3 p. 249. Corrected two steps: in (b) the scalar was transferred from
    H^p(L,Omega^p) to H^p(P^n,Omega^p) by asserting that restriction carries
    the normalized generator to the normalized generator, and is now
    transferred by the projection formula t_Pn(beta cup i_*1) = t_L(i^*beta
    cup 1) with i_*1 spanning H^{n-p}; in (d) the residue input is now
    stated as the Poincare residue with its constant checked against
    III.7.14.1(c) and cross-checked for a hypersurface in P^n, where (b) and
    c(O(d)) = d must agree. Not checked: whether the printed exercise has a
    canonical normalization in the literature; none was found.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second published-solution search for III.7.4(b) and (d) (issue #121);
    nothing complete was located, and the card keeps its own derivation.
    Read this pass: Yang Pi-Yeh, Hartshorne Solutions (9 June 2019),
    Solution 3.7.4, printed p. 75 of tmp/sources/lfwin-hartshorne-solutions.pdf,
    text version tmp/sources/lfwin-hartshorne-solutions.md -- (a) as in
    step s1 here; (b) cuts Y down to its deg Y points by a general linear
    subspace and then asserts that k = H^p(H, Omega^p_H) = H^p(X,
    Omega^p_X) = k is the identity, which is the normalization step s3
    now supplies by the projection formula, and he never moves the count
    from the subspace back to P^n; (d) writes c(L_Y) as a Cech cocycle
    and then sends it by a map H^1(X, Omega_X) -> H^0(X, O_X) whose value
    is written as a sum of coordinate times partial derivatives, which is
    neither a defined map nor the duality pairing. Dongryul Kim, release
    PDF p. 170, lists Exercise 3.7.4 in his "problems I haven't solved".
    Stacks Project tags read: 0FWC, Section 50.22 (de Rham cohomology as
    a Weil cohomology theory, with the trace map Theta on H^{2d} and the
    statement that the cycle class followed by lambda_X is the degree
    map) and 0FLE, Section 50.9 (the dlog first Chern class into
    H^1(X, Omega^1)). 0FWC is a statement about H^{2p}_{dR}; the
    exercise's eta(Y) is the (p,p) Hodge component in H^p(X, Omega^p),
    and no tag read makes that identification. 0FLE supplies only the map
    c of part (c). Math StackExchange 1794757 and its accepted answer by
    the account S.M. (2016-05-22) prove (a) only. Checked against the
    book: the printed exercise, printed pp. 249--250; the trace and
    duality inputs III.7.1, III.7.2, III.7.12--7.14, printed pp. 240--247;
    Appendix A's C1, printed p. 430. Not checked: whether the printed
    exercise admits a normalizing convention in the literature; none was
    found in any of the sources read across both passes.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on the reader's report of this batch, three of substance. (1) The
    statement is the printed exercise again: the normalization paragraph is
    removed from the problem block and stated at the head of the solution,
    which is where a convention the book does not print belongs. (2) Step s3
    no longer applies the trace to the wrong degree: it names 1_V in
    H^{dim V} by t_V(1_V) = 1, observes that every point class on L equals
    1_L by step s1, and defines 1_{P^n} by t_{P^n}(1_{P^n} sm i_*1) = 1, that
    is, as the class pairing to 1 with the class of a linear P^p. The
    previous version defined 1_L by a trace applied to H^0 and 1_{P^n} by a
    trace applied to H^{n-p}, both ill-typed, and never stated the
    identification the transfer uses. (3) Step s6 is no longer circular. It
    states the divisor case (R) as an input, notes that part (d) is its case
    beta = 1, proves (R) in dimension one from the residue theorem and
    III.7.14.1(c) of the book, and says that for n >= 2 Hartshorne supplies no
    such statement (Remark III.7.14 says the trace is known only to exist).
    The withdrawn sentences are those that took the residue formula as the
    definition of the Gysin map by appeal to the problem statement, and the
    "independent check" for a hypersurface in P^n, which compared a class in
    H^1(Omega^1) with a point class. Also corrected: the audit description of
    Yang's (b) and (d) and of Kim's coverage, and the text versions named for
    Kim, MSE 1794757 and the two Stacks tags. Checked against the book in this
    pass: the printed exercise on pp. 249-250, III.7.1(a) p. 240, III.7.2
    p. 241, III.7.12-7.14 pp. 246-247, II.8.18 p. 179, I.7.7 p. 53, Exercise
    III.7.3 p. 249, Appendix A C1 p. 430. Not checked: no source proving (R)
    for n >= 2 was located, and the card does not claim one.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass on the reader's report of this batch, checked against the
    book and its text version. Restored the three events the report names as
    rewritten in place: the note of 2026-09-18 by chatgpt again ends where it
    ended, without the sentence about the 2026-11-16 move of the
    normalization; the note of 2026-11-11 again records the cross-check for a
    hypersurface in P^n as it was written on that date; and the note of
    2026-11-16 again carries the descriptions of Yang, of Kim and of Math
    StackExchange 1794757 written then. What those descriptions got wrong is
    corrected here and not in them: Yang's (b) does move the count back to
    P^n, by citing his own 3.7.3, though that citation is to a different
    identification; his (d) is a computation in homogeneous coordinates
    using Euler's formula, defined for X = P^n only; Kim's source has
    Exercise 3.7.4 on release PDF p. 170 with (a) and (c) proved, (b) a
    fragment and no (d), and his doubt stands in his list of problems he has
    not solved on PDF p. 1, not in a list of corrections; and the MSE answer
    is not recorded as accepted. The cross-check named in the note of
    2026-11-11 is not independent, as the note of 2026-11-16 says: it
    compares a class in H^1(Omega^1) with a class of a point.

    The mathematics of the card is repaired in four places. (1) The head of
    the solution now states four inputs and says which the book proves:
    (N) the trace at points, (G) the adjunction definition of Gysin maps,
    which is forced by the exercise's own definition of eta(Y), (R) the
    divisor case, and (B) base change for a transverse hyperplane section.
    The earlier text claimed the traces are "compatible with the Gysin
    maps", which with (G) is automatic and constrains nothing, and it called
    (R) part of the convention while stating only (N). (2) Step s3's use of
    "1" in H^p(P^n, Omega^p) before 1_{P^n} is defined, and of i^*1 = 1_L,
    is gone: alpha_0 = i_*(1) is the class of the linear subspace and is
    proved nonzero by restricting along the hyperplanes that cut L out, and
    the pairing then goes through (G) alone. (3) Step s5's transition
    convention is flipped to s_i = g_ij s_j, the one Hartshorne's Cech
    differential carries, so that the cocycle is df_j/f_j - df_i/f_i; with
    the earlier convention the constant in (R) is -1, as the reader
    computed. (4) Step s6 now compares the Cech class with the residue trace
    of Remark III.7.14 through the Cech complex of the flasque resolution,
    which is where the sign is decided, and states that (d) for n >= 2 is
    proved relative to (R) and that (R) itself is not proved there; "This
    proves part (d)" is no longer said without that qualification. Step s2's
    base change is named as input (B) instead of being asserted as a fact
    about "the normalized Gysin maps", and the card says that (B) is the
    step the printed hint uses and that no source proving it for n >= 2 was
    located. Checked against the book in this pass, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md: the printed exercise
    on pp. 249-250, the Cech complex of III.4 on p. 218, III.7.1(a) p. 240,
    III.7.1.1 pp. 240-241, III.7.2 p. 241, III.7.12-7.13 pp. 246-247,
    Remark III.7.14 and Theorems III.7.14.1, 7.14.2 on pp. 247-248,
    Exercise III.7.3 p. 249, Appendix A C1 p. 430. Not checked: no source
    proving (R) or (B) for n >= 2 was located.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass on the reader's report of this batch, on the items that the
    second pass left open, and on the audit trail. (i) The proof of
    alpha_0 nonzero introduced by the second pass was invalid and is
    replaced. It restricted alpha_0 along the n-p hyperplanes that cut L out
    and read the restriction as eta_L(L); but those hyperplanes contain L, so
    they do not meet it transversely, step s2 does not apply to the pair
    (L, H_i), and eta_L(L) is the class of L as a subvariety of itself, an
    element of H^0(L, O_L), not the class of degree n-p that a restriction of
    alpha_0 has. The step now proves alpha_0 nonzero by induction on the
    dimension of the linear subspace: for a point the class is nonzero by step
    s1, and for dimension at least one it applies step s2 to a hyperplane H
    with L not contained in H, which does meet L transversely in L cap H, and
    uses that a class with nonzero restriction is nonzero. (ii) The head of
    the solution now separates existence from compatibility. A trace
    satisfying (N) is unique, since H^n(X, Omega^n) is one-dimensional and
    eta(P) is nonzero by step s1, and a trace exists by Proposition III.7.5
    (printed p. 242); what is missing for (b) and (d) is the proof that the
    trace of III.7 satisfies (R) and (B), and the head states that instead of
    calling the consistency of the four inputs a theorem. (iii) The text
    versions of the sources of the event of 2026-11-16 whose note begins
    "Second published-solution search" are named here, because the second
    pass restored that event to a text written before the citations were
    added: tmp/sources/lfwin-hartshorne-solutions.md for Yang Pi-Yeh,
    tmp/sources/hartshorne-solutions-kim.md for Kim,
    tmp/sources/mse-1794757-cohomology-class-of-a-subvariety.md for Math
    StackExchange 1794757, and tmp/sources/stacks-tags/0FWC.md and
    tmp/sources/stacks-tags/0FLE.md for the two Stacks tags. (iv) The
    solution-reviewed event of 2026-11-16 whose note begins "Repairs on the
    reader's report of this batch" is restored as it was written, and this
    event is appended after it rather than put in its place. Checked against
    the book in this pass, in tmp/sources/hartshorne-1977-algebraic-geometry.md
    (printed p. N is PDF p. N+15): the printed exercise on pp. 249-250,
    Proposition III.7.5 on printed p. 242, Corollary III.7.12 on printed
    p. 246, Remark III.7.14 and Theorems III.7.14.1 and 7.14.2 on printed
    pp. 247-248, Exercise III.7.3 on printed p. 249. Not checked: no source
    proving (R) or (B) for n >= 2 was located in the two search passes
    recorded, and III.7.5 and III.7.12 were read in the text version only.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fourth pass on the reader's report of this batch, on the two inputs. The
    Gysin calculus of the Stacks Project was read at the tags in this pass, at
    https://stacks.math.columbia.edu/tag/0G82 and the tags named: Lemma
    50.23.9 (0G8C) gives gamma^{p,q}(alpha|_Z) = alpha cup gamma^{0,0}(1) for
    a Koszul regular closed immersion of codimension c in a smooth X over a
    base S; Lemma 50.23.10 (0G8D) gives the compatibility of gamma with a
    transverse cartesian square, hence the class-level form of (B); Remark
    50.23.1 with equation (50.23.1.1) (tags 0G83 and 0G84) gives gamma^0_f(1)
    = df/f for a local equation f, which with Section 50.9 (tag 0FLE) is the
    dlog class of a divisor, hence the class identity c_1(L(Y)) cup nu =
    gamma^{n-1,n-1}_Y(nu|_Y) behind (R). Neither lemma compares the abstract
    trace of III.7 with the Gysin class of a point; that comparison,
    t_X(gamma^{0,0}_{P/X}(1)) = 1, is the case of the residue theorem which
    the book proves only for curves (III.7.14.1, printed p. 247), and the head
    of the solution now says so. Checked in this pass: the Stacks pages named,
    read at the site, and III.7.14.1 in
    tmp/sources/hartshorne-1977-algebraic-geometry.md. Not checked: no proof
    of the comparison was found, and the functoriality of gamma for a
    composite of regular immersions was not read in the source.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Fifth pass on the reader's report, on the four items that pass named:
    the trace normalization, the reduction to one point identity, the dlog
    citation, and the text versions of the Stacks tags. (i) The claim that a
    trace satisfying (N) is unique is false and is withdrawn. It is false
    because (N) constrains only the traces of finite reduced k-schemes: with
    t_X replaced by lambda*t_X and every point trace left alone, (N) still
    holds, the pairing scales by lambda, the class eta(P) = j_*(1) of (G)
    scales by lambda^{-1}, and part (a) still reads 1, so part (a) holds for
    every scalar and constrains none. What replaces it is uniqueness up to a
    nonzero scalar, which is Lemma 50.24.3 (tag 0G8I) in the relative form:
    the trace is unique up to precomposition by a unit of H^0(X, O_X), and
    that ring is k for X projective and integral. The scalar is fixed by the
    point comparison t_X(gamma^{0,0}_{P/X}(1)) = 1, which is unique because
    H^n(X, Omega^n) is one-dimensional and the class is nonzero by Lemma
    50.23.11 (tag 0G8E); that is now what the head says, and the inference
    "one fixed trace" that stood after it is rewritten to match.
    (ii) The reduction to the single point identity is incomplete and is no
    longer asserted. Granting t_X(gamma^{0,0}_{P/X}(1)) = 1, applying 0G8C to
    a divisor Y leaves t_X(gamma^{n-1,n-1}_Y(nu|_Y)), and to read that one
    needs the composite functoriality gamma^{0,0}_{P/X} =
    gamma^{n-1,n-1}_{Y/X} o gamma^{0,0}_{P/Y}, not supplied by 0G8C or 0G8D
    and recorded as unread in the fourth pass above. The head now names it as
    the second half of the comparison, says what it would give, and says that
    (R) and (B) stay inputs. (iii) The dlog citation was wrong about the tags.
    Remark 50.23.1 with equation (50.23.1.1) (0G83, 0G84) defines gamma
    through c_{f_1,...,f_c} and carries no formula gamma^0_f(1) = df/f; that
    formula is at the end of the proof of Lemma 50.23.5 (tag 0G88), and
    Section 50.9 (tag 0FLE) defines the dlog class without comparing it with
    gamma. The card now says so, quotes the sentence from 0G88, and states
    the class identity c(L(Y)) cup nu = gamma^{n-1,n-1}_Y(nu|_Y) as an input
    made in the Cech model of steps s5 and s6, not as a theorem of the Stacks
    Project; 0G8D is now described as class-level for gamma, which becomes a
    statement about the trace only through the comparison. (iv) The text
    versions now exist and are named: tmp/sources/stacks-tags/0G82.md for the
    section, and 0G83.md, 0G84.md, 0G88.md, 0G8A.md, 0G8C.md, 0G8D.md,
    0G8E.md, 0G8I.md and 0FLE.md for the environments, each saved from the
    page as served on 2026-11-16 at stacks-project commit
    a04446e57ec1fbc252a871afcec7752fb2807b14, with the LaTeX label of each.
    The fourth pass's event above, which said 0G83 and 0G84 give gamma^0_f(1)
    = df/f and that the class identity and the class-level form of (B) are
    theorems, is a dated event and is left as written; the correction is this
    event. Checked in this pass: Section 50.23 and Section 50.24 as served at
    the site and in the tag files above, and in
    tmp/sources/hartshorne-1977-algebraic-geometry.md (printed p. N is PDF p.
    N+15) III.7.5 printed p. 242, III.7.12 printed p. 246, Remark III.7.14 and
    Theorem III.7.14.1 printed pp. 247-248. Not checked: no proof of the point
    comparison, of (R) or of (B) was found, and the composite functoriality of
    gamma was not located in the Stacks Project; nothing in this pass supplies
    the published solution of (b) and (d) that the exercise still needs.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Sixth pass on the reader's report, on one sentence at the head of the
    solution. That sentence said the point identity is necessary for (R) and
    (B) and not shown to be sufficient. The second half stands. The first is
    withdrawn: no implication between the point identity and those two inputs
    was established in either direction. What the fifth pass showed is that
    sufficiency fails for want of the composite functoriality
    gamma^{0,0}_{P/X} = gamma^{n-1,n-1}_{Y/X} o gamma^{0,0}_{P/Y}; nothing
    there, and nothing in the tags read, derives the point comparison
    t_X(gamma^{0,0}_{P/X}(1)) = 1 from (R) or from (B). The reason is that
    neither input is a statement about a point: (R) constrains the trace
    against the dlog class of a divisor and (B) constrains the square of a
    transverse pair, so the point comparison would have to be carried to them
    by a further identification, which this card does not make. The head now
    says that no implication in either direction is established and that (R)
    and (B) remain inputs. The same claim stands in the fifth-pass record of
    COMPLAINTS.md, which is a dated record and is left as written; the
    correction is a new record there of this date. Checked in this pass: the
    head against the text versions of the two lemmas it names,
    tmp/sources/stacks-tags/0G8C.md (Lemma 50.23.9, the projection formula) and
    tmp/sources/stacks-tags/0G8D.md (Lemma 50.23.10, the transverse square),
    neither of which mentions a trace, and the card's step s6. Not checked: no
    source was searched in this pass, and nothing new is proved here about the
    point comparison, (R) or (B).
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, third pass: the solution's paragraph on the
    composite functoriality of gamma carried a search record. It named the tag
    file tmp/sources/stacks-tags/0G82.md, listed what Section 50.23 holds, and
    said that the fourth pass's audit recorded the composite case as unread. A
    rendered solution carries the mathematics, not which file was read
    (PROSE-11, QUAL-08). The paragraph now states that the composite
    gamma^{0,0}_{P/X} = gamma^{n-1,n-1}_{Y/X} o gamma^{0,0}_{P/Y} is an input
    of this solution, that 0G8C and 0G8D state the class of one Koszul regular
    closed immersion and its compatibility with a transverse square and that
    neither states the composite of two immersions. No mathematical claim
    changes: (R) and (B) remain inputs and no implication between them and the
    point identity is established. The search record is COMPLAINTS.md's
    III.7.4(b),(d) entry. Nothing was re-read in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, fourth pass, on sixteen lines of the same
    solution. Two things are repaired. (i) The status of the class-level halves
    contradicted itself. The paragraph introducing the Gysin calculus said "the
    class-level part of the two inputs is published", while the two paragraphs
    after it make the identity c(L(Y)) cup nu = gamma^{n-1,n-1}_Y(nu|_Y) an
    input, the comparison of the dlog class with gamma^0(1) being nowhere in
    the tags, and the closing paragraph repeated the published claim for both.
    The tags supply the class-level part of (B), the compatibility of gamma with
    a transverse cartesian square, and they supply that part only: the opening
    paragraph now says so and names (R)'s identity as an input, and the closing
    paragraph says which half is published and why the other is not. (ii) The
    search record left in the rendered solution is removed: the inventory of tag
    files the passage was read in, "no tag read performs the comparison", "no
    source read derives" the point comparison, and "the two search passes
    recorded above" for (B). Those statements are COMPLAINTS.md's III.7.4(b),(d)
    entry, which records them. No step, page or tag changes, and (R) and (B)
    remain inputs of this solution.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcription pass for issue #121, on parts (a) and (c). Read at the
    cited places: Yang Pi-Yeh, Solution 3.7.4, printed p. 75, text version
    tmp/sources/lfwin-hartshorne-solutions.md, read in the PDF at that
    page; Dongryul Kim, Exercise 3.7.4, PDF p. 170, text version
    tmp/sources/hartshorne-solutions-kim.md; Math StackExchange 1794757,
    the answer by the account S.M. of 2016-05-22, text version
    tmp/sources/mse-1794757-cohomology-class-of-a-subvariety.md. Checked
    against the book in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    where printed p. N is PDF p. N+15: III.7.4 as printed on pp. 249--250,
    whose (a) reads "show that t_X(eta(P)) = 1" and whose (c) defines dlog
    as a homomorphism of sheaves of abelian groups and the induced map c
    on Pic, citing Exercise III.4.5. What the pass establishes. (a) is
    published three times and all three agree: Yang's restriction
    argument, Kim's Yoneda pairing evaluated at 1, and the S.M. answer,
    which additionally records that the point trace is a normalization
    (t_P(1) can be any element of k^*) and that the exercise needs
    t_P(1) = 1. (c) is published by Yang and Kim as the computation
    dlog(fg) = dlog f + dlog g with the citation of Exercise III.4.5.
    Parts (b) and (d) remain without a published proof: Yang's (b) moves
    the count back to P^n by citing his own 3.7.3, a different
    identification, and his (d) is a computation in homogeneous
    coordinates that uses Euler's formula, so only for X = P^n; Kim has a
    fragment for (b) and nothing for (d), and lists the exercise among the
    problems he has not solved on PDF p. 1. On the card, s1 and s4 now
    carry the three and two sources respectively, the head and the remark
    of 2026-11-16 say which parts are transcribed and which are the
    card's, and the COMPLAINTS record of 2026-11-16 names (b) and (d).
    Not checked: no source outside those named was searched in this pass,
    and steps s2, s3, s5 and s6 were not re-derived.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report. (i) The remark of the earlier pass said
    that Yang and Kim "both cite Exercise III.4.5" for (c); only Kim does,
    Yang giving the computation with no citation. The remark now says so,
    and the event of even date above is corrected on the same point. (ii)
    The remark called the projection formula "step s3"; the base-change
    identity is step s2, and s3 is the count in P^n. (iii) The remark
    repeated Yang's "linear subspace of dimension n - p" without a flag;
    the dimension that cuts Y down to points is p, as s3's L = PP^p has,
    and the remark now says so and quotes his words as his. (iv) The head
    of the solution and the closing sentence of the remark no longer say
    which steps were transcribed or refer to a COMPLAINTS record. Checked
    against the book in tmp/sources/hartshorne-1977-algebraic-geometry.md
    (printed p. N is PDF p. N+15): III.7.4 on printed pp. 249--250, whose
    (c) cites Exercise III.4.5. Not checked: no source was re-read beyond
    the passages quoted, and no step was re-derived.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on the rule that a dated event is never
    edited. The event of 2026-11-16 above whose note begins "Transcription
    pass for issue #121" was rewritten in place by commit 20dcbc5d82, and it
    is restored to the text it carried when written in 448470f1a6. What the
    restored text gets wrong is corrected here, in its own words: it reads
    (c) as "the computation dlog(fg) = dlog f + dlog g with the citation of
    Exercise III.4.5", which attributes the citation to both sources. Only
    Kim cites it; Yang gives the computation with no citation, and the
    exercise's own statement of III.7.4(c) is where the book makes the
    citation. The remark of the card already says so, and no rendered text
    changes with this event. Checked in this pass: Yang Pi-Yeh, Solution
    3.7.4(c), printed p. 75 of tmp/sources/lfwin-hartshorne-solutions.md,
    whose entry carries the computation and no citation, and Kim's Exercise
    3.7.4(c) in tmp/sources/hartshorne-solutions-kim.md, PDF p. 170, which
    cites Exercise III.4.5; and the printed exercise in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, printed pp. 249--250,
    whose (c) names Exercise III.4.5. Not checked: no step was re-derived,
    and no source beyond those two passages was read.

- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on the rendered card. Two sentences said that
    (b) and (d) are not proved in any source read for the card, which states
    what this card's reading reached and not what the mathematics is: one at the
    head of the solution, in the paragraph that attributes (a) and (c), and one
    opening the second paragraph of the published-solution remark. Both now mark
    the parts as the card's own, and each of the descriptions they open stands as
    written: Yang's (b) with its citation to his own 3.7.3 and his (d) in
    homogeneous coordinates by Euler's formula, Kim's fragment of (b) and no (d),
    and the class-level halves of the Stacks tags with no comparison with the
    trace of III.7. The closing sentences of the two paragraphs, which said that
    no source cited here proves the two parts, now say the same of the proofs:
    they are the card's, and steps s2, s3, s5 and s6 prove both relative to the
    inputs (R) and (B). No mathematics changes, and no step, page or tag moves.
    Not checked: no step was re-derived, no source was re-read, and no search was
    made in this pass.

- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on the rendered card only. (i) The head of the
    solution and the second paragraph of the published-solution remark still said
    that parts (b) and (d) "have no published proof" and "are not published",
    which claims more than was established: what the two search passes recorded,
    here and in the COMPLAINTS entry on III.7.4(b),(d), is that no published proof
    was found in the sources read and searched. Both sentences now mark the two
    parts as the card's own and say nothing more; the descriptions they open, of
    Yang's (b) with its citation to his own 3.7.3, his (d) in homogeneous
    coordinates by Euler's formula, Kim's fragment of (b) and no (d), and the
    class-level halves of the Stacks tags with no comparison with the trace of
    III.7, stand as written, and the closing sentences saying that steps s2, s3,
    s5 and s6 prove both relative to (R) and (B) are untouched. (ii) The proofs of
    (a), at the head of step s1 and in the remark, named the text versions of Yang
    Pi-Yeh, of Kim and of Math StackExchange 1794757,
    tmp/sources/lfwin-hartshorne-solutions.md, tmp/sources/hartshorne-solutions-kim.md
    and tmp/sources/mse-1794757-cohomology-class-of-a-subvariety.md; those paths
    stay in the transcription event of even date, which names all three, and the
    two rendered passages now cite each source by solution, PDF or printed page
    and, for the MSE answer, by question number, answer author and date
    (PROSE-11, QUAL-08, SEC-7). No mathematics changes, and no step, page or tag
    moves. Read in this pass: the two rendered paragraphs and the audit trail of
    this card; no source was reopened and no step was re-derived.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, five items. (i) QUAL-01: the statement was
    the printed exercise alone, and the printed exercise fixes no normalization
    of the trace, so that parts (b) and (d), which assert numerical identities,
    have no fixed meaning as printed; the card said so at the head of its
    solution and in the remark on the trace, which made the problem block ask
    for an assertion the card itself calls unfixed. The statement now carries
    the normalization, one sentence after the trace map: "These trace maps are
    normalized so that the trace at a closed point is the identity: for a closed
    point $P$ the map $t_P: H^0(P, O_P)\to k$ is the identity of $k$, and on a
    finite reduced $k$-scheme the trace is the sum of the traces at its
    points." The printed text it replaces is III.7.4, read in
    tmp/sources/hartshorne-1977-algebraic-geometry.md at printed pp. 249--250
    (PDF pp. 264--265): "Now $\Omega_Y^{n-p}=\omega_Y$ is a dualizing sheaf for
    Y, so we have the trace map $t_Y: H^{n-p}(Y,\Omega_Y^{n-p})\to k$.
    Composing, we obtain a linear map ... By (7.13) this corresponds to an
    element $\eta(Y)\in H^p(X,\Omega_X^p)$, which we call the cohomology class
    of Y", with no word on which trace is meant; III.7.1(a), which it builds on,
    says only "Fix one such isomorphism". This reverses the decision the
    solution-reviewed event of even date recorded, the one whose note begins
    "Repairs on the reader's report of this batch" and whose item (1) moved the
    normalization out of the problem block; that event is dated, is left as
    written, and this event is the correction, on the ground that QUAL-01 asks
    for a statement that is true and well posed rather than one the card calls
    unfixed. (ii) DEF-26: the definiendum mark stood on "cohomology class of
    $Y$" inside the problem statement; it is gone, the notion being defined
    only for the exercise, not on a definition card. (iii) QUAL-01: the printed
    hint is bracketed and says "reduce to the case Y is a finite set of points";
    the statement had dropped the brackets and added "where". The bracket and
    the printed words are back, and the exercise's closing sentence, "See
    Matsumura [1] for further discussion.", which the card had dropped, is after
    part (d). (iv) QUAL-08, on the head of the solution. It carried status text
    about the card rather than mathematics: that the printed exercise fixes no
    normalization (now moot, the statement carrying it), "What this solution
    uses is the following, and nothing else", that the class-level part of (B)
    "is published" and that the identity behind (R) "is not", that the
    functoriality of gamma "is an input of this solution", that the reduction
    "is therefore not made here", that parts (b) and (d) are "theorems relative
    to (R) and (B), and open with respect to the book alone", and that "The
    remark below records what the book does and does not determine". What the
    head now states is the mathematics: the normalization in force and that the
    trace at a point does not determine the trace on $X$; the three properties
    (G), (R) and (B) with what each says; the Gysin calculus of the Stacks
    Project with its tags and the two places where a comparison with the trace
    of III.7 would be needed; and that (b) and (d) hold relative to (R) and
    (B), with the marks that (b) and (d) are the card's own kept. Two phrases
    of the same kind outside the head went with them: step s3's "This is a
    normalization and not a consequence of the book" now says which generator
    the number $\deg Y$ is measured against, and step s6's "and relative to
    (R) alone: (R) itself is not proved here" now stops at "relative to (R)
    alone". (v) Yang is quoted as "are just identity" where he prints "is just
    identity", of "the morphism $k \cong H^p(H,O_H^p) \cong H^p(X,O_X) \cong k$";
    the remark now quotes his singular verb with his subject. Read in this pass:
    the printed exercise in the text version above, with III.7.1(a) and III.7.14
    around it; Yang Pi-Yeh, Solution 3.7.4(b), in
    tmp/sources/lfwin-hartshorne-solutions.md at line 1984, printed p. 75, for
    the quotation in (v). Not checked: the printed pages were not in hand; Kim's
    Exercise 3.7.4 and the Math StackExchange answer were not reopened; no step
    was re-derived, and no source was searched in this pass.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the latest reader's report, on the normalization in the
    statement. The preceding QUAL-01 repair added only the pointwise condition
    (N): identity of the trace at a closed point and additivity on finite
    reduced schemes. That condition leaves the trace on $X$ free by a nonzero
    scalar, so it did not make the scalar-sensitive assertions (b) and (d)
    well-posed. The statement now also imposes the point comparison (C),
    $t_V(\gamma^{0,0}_{Q/V}(1))=1$, on each nonsingular projective $V$ at a
    chosen closed point, with $\gamma^{0,0}$ the Gysin map of Stacks Project
    Remark 50.23.7 (tag 0G8A). Lemma 50.23.11 (tag 0G8E) proves that this
    Gysin class is nonzero, and uniqueness up to a unit is Lemma 50.24.3 (tag
    0G8I), already cited in the solution; hence (C), unlike (N), fixes the
    scalar. Part (b) now also stipulates the generator $1_{\PP^n}$ used in its
    identification with $k$, namely the generator of step s3 characterized by
    $t_{\PP^n}(1_{\PP^n}\smile\eta_{\PP^n}(L))=1$ for a linear
    $L\cong\PP^p$. The head and trace-normalization remark now distinguish (N)
    from (C), and step s3 no longer leaves the identification of Exercise
    III.7.3 unqualified. The added normalizations are the card's QUAL-01 repair,
    not printed text: the printed exercise, read in
    tmp/sources/hartshorne-1977-algebraic-geometry.md on printed pp. 249--250
    (PDF pp. 264--265), says only to identify $H^p(X,\Omega^p)$ with $k$ by
    Exercise III.7.3 and contains no point comparison or choice of generator.
    Checked in this pass: that exercise, Remark 50.23.7 and Lemma 50.23.11 in
    tmp/sources/stacks-tags/0G8A.md and 0G8E.md, and the card's complete
    solution and remarks. No source asserting (R) or (B) was added, and no
    other step was changed.

- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the latest reader's report, on the passage from the chosen point
    $Q$ in the statement to an arbitrary closed point $P$ in the solution. The
    preceding repair had proved only nonvanishing of each point class, which
    does not justify that passage. The solution head now argues independence
    of the class before using it. This argument is the card's specialization
    of the diagonal calculation in the proof of Lemma 50.24.4 (tag 0G8J): let
    $\eta_\Delta$ be the diagonal Gysin class and let $1\otimes\xi_V$ be the
    $H^0(V,\OO_V)\otimes H^{\dim V}(V,\Omega_V^{\dim V})$ component of its
    $\OO_V\boxtimes\Omega_V^{\dim V}$ part under Künneth. For each closed point
    $P$, Lemma 50.23.10 (tag 0G8D) gives
    $(P,\operatorname{id})^*\eta_\Delta=\gamma^{0,0}_{P/V}(1)$, while pullback
    through the point leaves only the component $1\otimes\xi_V$; hence
    $\gamma^{0,0}_{P/V}(1)=\xi_V$ for every $P$. The situation in tag 0G8G is
    proper smooth and equidimensional and imposes no characteristic-zero
    hypothesis. Read in this pass: the pages and text versions
    tmp/sources/stacks-tags/0G8G.md, 0G8D.md and 0G8J.md. Section 50.22's
    characteristic-zero de Rham cycle-class argument is not used. Checked:
    the Künneth component is independent of $P$, and the positive-differential
    and positive-first-cohomology components vanish under $(P,
    \operatorname{id})^*$. No other paragraph or mathematical input was
    changed.

- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner directed on 2026-11-18 that part (d), for a general X, stand as
    the card's own derivation rather than be recorded as owed, the disposition
    used on E-HAT-2.B-7, and that the remark state which part is a transcription
    and which is the card's own. The remark now says so: part (b) is transcribed
    from Yang Pi-Yeh, Solution 3.7.4(b), printed p. 75, with the transfer his
    proof asserts supplied at step s2, and part (d) is the card's own
    derivation, no published proof of the general case existing in the sources
    on this machine (Yang's (d) treats only X = P^n, at line 1988 of
    tmp/sources/lfwin-hartshorne-solutions.md, and Kim's set has no (d), its (b)
    being the fragment at line 6862 of tmp/sources/dongryul-kim-hartshorne-
    solutions.md). The same disposition was applied on 2026-11-18 to IV.4.22's
    group-scheme step, where Hartshorne IV.4, Theorem 4.11 is cited on that card
    at printed p. 325 for the fibre case, the page verified in the text version.
    Checked in this pass: both named text versions at the lines above, and the
    card's own steps s2, s3, s5 and s6 against the remark. Not checked: no
    further source was searched for part (d), and no step was re-derived.

- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Reviewer's report on issue #156, on the two steps that were not met. (i) The
    sign of the divisor cocycle. Step s6 derived $\{df_j/f_j-df_i/f_i\}$ from its
    own convention $s_i=g_{ij}s_j$ and then printed the negative cocycle,
    repeated in s7, while step s2 uses the derived sign; on the curve cover the
    printed statement gave $c_{12}=-df/f$ and the residue $-1$ against the
    constant $+1$ the card claims. The statement of s6 now carries the derived
    sign, and its proof reads off the coefficient $+1$ of the pole $dt_1/t_1$,
    which is Theorem III.7.14.1(c), printed p. 247. Step s2 is also stated in the
    form $t_X(c(\mathcal L(D))\smile\nu)=t_D(\nu|_D)$ for a class $\nu$ on $X$:
    its earlier form quantified over a lift of a class from $D$, which nothing
    supplied, and the general form follows from this one by the projection
    formula of s3, a consequence of the adjunction definition of the Gysin map
    with III.7.6. (ii) Base change. Step s3 took an arbitrary
    $w\in H^{n-1-q-p}(H,\Omega^{n-1-q-p})$ and a lift of it to $X$; restriction
    $H^r(X,\Omega^r)\to H^r(H,\Omega^r)$ is not surjective, being
    $0\to H^1(\PP^1,\Omega^1)=k$ for $i:\PP^1\hookrightarrow\PP^2$, and its
    application in s4 cut $\PP^n$ by $p$ hyperplanes where $L\cong\PP^p$ is cut
    out by $n-p$. The step is withdrawn. Step s3 now proves the projection
    formula for a divisor inclusion and the identity
    $\eta_{\PP^n}(L)=i_*(1)=c(\mathcal L(H_1))\smile\cdots\smile
    c(\mathcal L(H_{n-p}))$ for a linear subspace, and step s4 proves (b)
    without base change: it cuts $Y$ by $n-p$ general hyperplanes, which is the
    printed hint, has $\deg(Y\cap H_1\cap\cdots\cap H_k)=\deg Y$ by I.7.7,
    printed p. 53, applied successively, and counts
    $\langle\eta(Y),\alpha_0\rangle_{\PP^n}=t_Y(c_Y^{n-p})=d$ by iterating s2
    along the hyperplane sections of $Y$ and applying (N) at the $d$ points. The
    nonvanishing of $\alpha_0$, previously an induction on the dimension of $L$,
    is now the consequence $d\ne0$ of that count. Read in this pass: Hartshorne's
    II.8.18, printed p. 179, I.7.7, printed p. 53, III.7.6, printed p. 243 and
    III.7.14.1, printed p. 247, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md; and Lipman's Astérisque
    117 in the Numdam scan www.numdam.org/item/AST_1984__117__1_0.pdf, where PDF
    p. = printed p. + 3, at (0.4), printed pp. 22--23, (0.6), printed pp.
    24--25, (8.4) and (8.5), printed pp. 74--75, (12.1)--(12.2.3), printed pp.
    105--106, (13.1) and (13.5), printed pp. 111 and 113, and (13.12), printed
    p. 117, which are the pages steps s2 and the head cite. Not checked: no
    source for the base change the withdrawn s3 asserted was located in this
    pass, and the card no longer uses one.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The two pages step s2 rests on, and the status of the transverse-square base
    change. (i) Read on the printed pages, as page images of the Numdam scan,
    Theorem (13.5), printed p. 113: at any point where $X$ is locally
    Cohen-Macaulay the map (13.4) is an isomorphism of
    $\operatorname{Ext}^{n-d}_{\OO_X}(\OO_V,\tilde\omega_X)$ onto
    $\tilde\omega_V$; and Theorem (13.12), printed p. 117, with (13.12.1) and
    (13.12.2): for $\nu\in\Omega^d_{R/k}$ there is a $\nu'\in g\tilde\omega:P$
    satisfying (13.12.1), unique modulo $g\tilde\omega$, and it satisfies
    (13.12.2), that its residue is the residue of $\nu$. The assumptions are
    those of (13.11), $R=\OO_{X,v}$ Cohen-Macaulay, which holds at the points of
    a nonsingular divisor in a nonsingular $X$; Corollary (13.6) on printed
    p. 113 is the local complete intersection case and is not needed here. (ii)
    The divisor formula of step s2 has a second published proof in characteristic
    zero: Axiom (A9) of the Stacks Project's Section 50.22, printed pp. 4267--4268,
    proves the commutativity of the square joining restriction, cup with
    $c_1^{dR}(\OO_X(Y))$ and the two traces, which for
    $\nu\in H^{d-1}(X,\Omega^{d-1})$ is that formula, the two traces agreeing
    because both take the value $1$ on the class of a point; the section is over a
    field of characteristic $0$ (printed p. 4265), and its auxiliary statement,
    that the kernel of restriction is killed by $c_1^{dR}(\OO_X(Y))$, is Lemma
    50.15.6, printed p. 4240, which holds in every characteristic. (iii) The
    base change of the withdrawn step s3 is used by no step of the solution, and
    no proof of it for these Gysin maps was located. What the Stacks Project
    proves is base change for the $\gamma$-maps, Lemma 50.23.10, printed
    pp. 4272--4273, and it compares $\gamma$ with a trace only in the divisor case
    (Axiom (A9)) and at a point (Lemma 50.23.11, printed p. 4273). The identity is
    itself equivalent to the projection formula $j^*i_*w=c_1(\OO_Y(H))\smile j^*w$
    for every class $w$ on $H$: testing it against $w$, and applying the divisor
    formula to $Z\subset Y$, turns it into that identity, and the two sides of
    that identity agree whenever $w$ is the restriction of a class on $X$. Not
    checked in this pass: no other source was searched for the base change.

- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Step s3 was stated for hyperplanes of a projective space and is now stated
    for nonsingular divisors $D_1,\ldots,D_r$ of a nonsingular projective $X$
    whose partial intersections are nonsingular of the expected codimension. No
    step of the induction changes: the proof already used only the divisor case
    of s2, the composition of the adjunction Gysin maps and the projection
    formula, with $\mathcal L(D_k)|_{Y_{k-1}}=\OO_{Y_{k-1}}(Y_k)$ in place of the
    hyperplane restriction. The general statement carries a corollary that the
    hyperplane form did not, and it is the base change of the transverse square
    in the case where the subvariety is a complete intersection: if a nonsingular
    divisor $H$ meets every $Y_k$ transversely, the product formula in $H$ for
    the divisors $D_k\cap H$ and the multiplicativity of $i^*$ give
    $i^*\eta(Y)=\eta_H(Y\cap H)$, which is $i^*j_*=(j_H)_*i_Y^*$ on the class
    $1$. Read in this pass: Yang Pi-Yeh's Solution 3.7.4(b), printed p. 75, in
    the text version tmp/sources/lfwin-hartshorne-solutions.md, against the
    printed exercise, III.7.4(b) on printed p. 250, II.8.18 on printed p. 179 and
    Exercise III.7.3 on printed p. 249; the transcription and what it leaves out
    are recorded in COMPLAINTS.md, not on the card. Not checked: the base change
    in the case where the subvariety is not a complete intersection, which no
    step of this solution uses.

- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Step s8 is new and no part of the exercise needs it: on a subvariety of
    $\PP^n$ the class $\eta(Y)$ is the Gysin class of the Koszul construction,
    in every codimension, and the transverse base change
    $i^*j_*=(j_H)_*i_Y^*$ follows from it. The proof pairs both classes with
    $\alpha_0=\eta_{\PP^n}(L)=i_*(1)$ for a general linear subspace $L\cong\PP^p$,
    which detects them because $H^{n-p}(\PP^n,\Omega^{n-p})$ is one-dimensional
    (Exercise III.7.3, printed p. 249), $\alpha_0\ne0$ (step s4) and the pairing
    is perfect (III.7.6, printed p. 243); the trace side is the count of step s4,
    and the Koszul side is Lemma 50.23.10 of the Stacks Project (tag 0G8D,
    printed pp. 4272--4273), which carries $\gamma^{0,0}_{Y/\PP^n}(1)$ to
    $\gamma^{0,0}_{Z/L}(1)$ for $Z=Y\cap L$, together with the locality of the
    construction (Lemma 50.23.3, printed p. 4269) and the point normalization (C)
    at the $d$ points. The passage from the class $1$ to an arbitrary class $a$
    is the equivalence of that identity with the projection formula
    $j^*i_*w=c_1(\OO_Y(H))\smile j^*w$, by perfectness of the pairing on $Y$ and
    step s2 applied to the divisor $Z$ of $Y$. Read in this pass: Yang Pi-Yeh's
    Solution 3.7.4(d), printed p. 75, in the text version
    tmp/sources/lfwin-hartshorne-solutions.md, against II.6, printed
    pp. 141--142, the Cech differential of III.4, printed p. 218, Exercise
    III.7.3, printed p. 249, and Theorem III.7.14.1(c), printed p. 247; the
    transcription and what it leaves out are recorded in COMPLAINTS.md. Not
    proved here: the same comparison and base change for a general smooth
    ambient variety, where no detecting class of this kind is available.

- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Step s8 is restated for a nonsingular projective $X$ with
    $\dim_kH^{n-p}(X,\Omega^{n-p})=1$ instead of $\PP^n$, and the proof is the
    same one with a general complete intersection in place of the linear
    subspace: $L=D_1\cap\cdots\cap D_{n-p}$ for general divisors $D_j$ in an
    ample class, $\alpha_0=\eta_X(L)=\prod_jc(\mcl(D_j))$ by step s3, the trace
    side $\langle\eta(Y),\alpha_0\rangle=t_Y(c_1(\restrictionof{\mathcal
    L}{Y})^{\smile\dim Y})=N$ by step s2 iterated along the successive
    intersections of $Y$ with the $D_j$, and the Koszul side
    $t_L(\gamma^{0,0}_{Z/L}(1))=N$ by Lemma 50.23.10 iterated, the locality of
    the construction and (C); one nonzero class detects because the space
    $H^{n-p}(X,\Omega^{n-p})$ is one-dimensional. The case $p=n$ is the point
    comparison (C) with step s1 and is stated separately. The projective-space
    case is the instance in which the hypothesis is Exercise III.7.3, printed
    p. 249. Read in this pass: Kim's Exercise 3.7.4 at PDF p. 170 in
    tmp/sources/dongryul-kim-hartshorne-solutions.md, and Egbert's entry at
    printed p. 187 in tmp/sources/hartshorne-solutions-egbert.md; the
    transcription and what those sets contain are recorded in COMPLAINTS.md.
    Not proved: the two statements without the one-dimensionality hypothesis,
    for which no detecting class is available in general.

- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Step s8 is stated in its sharp form. The one-dimensionality was used only to
    pass from an equality of pairings to an equality of classes, and the equality
    of pairings needs no hypothesis: for a smooth complete intersection $L$ of
    dimension $p$ meeting $Y$ transversely in $N$ points,
    $\langle\eta(Y),\eta_X(L)\rangle=t_Y(\eta_X(L)|_Y)
    =t_Y(c_1(\restrictionof{\mathcal L}{Y})^{\smile\dim Y})=N$ by step s2
    iterated, and $\langle\gamma^{0,0}_{Y/X}(1),\eta_X(L)\rangle
    =t_L(\gamma^{0,0}_{Z/L}(1))=N$ by Lemma 50.23.10 iterated, the locality of
    $\gamma$ and (C). The difference is therefore annihilated by the span of the
    complete-intersection classes, and the comparison and the base change follow
    as soon as that span is the whole of $H^{n-p}(X,\Omega^{n-p})$; the case
    $p=n$ is settled directly by (C) with step s1. Read in this pass: the pages
    the proof cites, II.8.18 printed p. 179, III.7.3 printed p. 249, III.7.6
    printed p. 243, and Stacks' Lemma 50.23.3 and Lemma 50.23.10 at printed
    pp. 4269 and 4272--4273, all read on the printed pages earlier on this day.
    Not proved: the comparison when the complete-intersection classes span a
    proper subspace, and the base change in that case.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The spanning condition of step s8 is now named: the complete-intersection
    classes of codimension $n-p$ are exactly the $n-p$-fold products of first
    Chern classes of invertible sheaves, since every invertible sheaf is a
    difference of two very ample ones and a very ample class is a hyperplane
    class, so the condition is that $H^{n-p}(X,\Omega^{n-p})$ be generated by
    such products. Read in this pass, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. $N$ is
    PDF p. $N+15$: Theorem III.7.1 on printed p. 240, the definition of a
    dualizing sheaf with its trace and Proposition 7.2 on printed p. 241,
    Corollary 7.12 on printed p. 246, Remark III.7.14 and Theorem III.7.14.1 on
    printed p. 247, Appendix A's C1 on printed p. 430, Theorem III.5.1 on printed
    p. 225, Exercise II.5.16(d) and Corollary III.7.13 on printed p. 247, and in
    tmp/sources/lfwin-hartshorne-solutions.md Yang Pi-Yeh's Solution 3.7.3,
    printed p. 75, whose proof of Exercise III.7.3 is complete except that it
    cites Exercise II.5.16(c) where the exterior-power part (d) is meant; the
    transcription is recorded in COMPLAINTS.md. Not re-checked in this pass:
    Lipman's (0.1)(d) on printed p. 11 and (0.2A) on printed p. 14, which the
    scan did not yield within the pass.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Step s6's convention is checked on the page it cites: on printed p. 218 the
    coboundary of the Cech complex is
    $(d\alpha)_{i_0,\ldots,i_{p+1}}=\sum_k(-1)^k\alpha_{i_0,\ldots,\hat
    i_k,\ldots,i_{p+1}}$ of III.4, so $(d\alpha)_{i_0i_1}=\alpha_{i_1}-
    \alpha_{i_0}$ and the $1$-cocycle condition is $g_{ij}g_{jk}=g_{ik}$ in
    multiplicative notation, which is the convention step s6 uses. Step s8's
    criterion is specialised to curves: for $p=n-1$ the $n-p$-fold products are
    single first Chern classes, so the hypothesis is that the image of
    $c:\Pic X\otimes k\to H^1(X,\Omega^1)$ of part (c) be all of
    $H^1(X,\Omega^1)$, and then the comparison and the base change hold for
    every curve in $X$ and for every transverse pair with the same property in
    $H$. Read in this pass: Andrew Egbert's entry III.7.3 at printed p. 187 in
    tmp/sources/hartshorne-solutions-egbert.md, transcribed and checked against
    II.5.16(d), II.8.13 and Theorem III.5.1; his argument stops before the region
    $i>r$, where Corollary III.7.13 is needed, and the transcription is recorded
    in COMPLAINTS.md. Lipman's (0.1)(d) on printed p. 11 and (0.2A) on printed
    p. 14 were attempted a second time in this pass and the scan again did not
    arrive; they remain unread here.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The two pages of Lipman the head cites, which the earlier attempts could not
    fetch, are now read from a cached copy of the same Numdam scan on the machine
    (140 pages, printed p. = PDF p. $-3$, identified by its printed pp. 74, 113
    and 117 carrying (8.4), (13.5) and (13.12)). Printed p. 11, Theorem (0.1)(d):
    for a smooth proper $d$-dimensional $V$ the pair $(\Omega_V^d,\int_V)$ is
    dualizing, representing the functor
    $\operatorname{Hom}_k(H^d(V,\mathcal F),k)$ of coherent $\mathcal O_V$-modules.
    Printed p. 14, Theorem (0.2A) with statement (i): $\omega_V$ is the unique
    $\mathcal O_V$-submodule of the constant sheaf of meromorphic $d$-forms whose
    sections over $\operatorname{Spec}C$ are the $\Omega_{C/B}$, and the natural
    map $\Omega^d_V\to\Omega^d_{k(V)/k}$ lands in it with equality at smooth
    points. Both are exactly what the head cites them for. Read also in this pass:
    Dongryul Kim's Exercise 3.7.3 at PDF p. 170, transcribed and checked; his
    proof is complete and needs no Serre duality, where Yang's cites Exercise
    II.5.16(c) for the exterior-power filtration (d) and Egbert's stops before the
    region $i>r$. The transcription is recorded in COMPLAINTS.md. Not checked:
    nothing of the card's own text was changed in this pass.

- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Step s6 carries a second check of its transition convention, in codimension
    two, which the dimension-one computation against Theorem III.7.14.1(c) did
    not reach: for the lines $x_0=0$ and $x_1=0$ of $\PP^2$ the local equations
    give the same cocycle on the cover $x_i\ne0$, the cup product of the two
    classes is the $2$-cocycle $d\log(x_0/x_1)\wedge d\log(x_1/x_2)$ on the triple
    intersection, equal there to $d\log(x_1/x_0)\wedge d\log(x_2/x_0)$; in the
    three affine charts its residues are $+1$ at $[1:0:0]$, $-1$ at $[0:1:0]$ and
    $+1$ at $[0:0:1]$ and vanish elsewhere, so the trace is $1$, which is the
    intersection number $L_1\cdot L_2$ of I.7.7, printed p. 53. The opposite
    convention would give $-1$, so the sign of s6 is the one the intersection
    numbers require. Checked in this pass: the three chart computations, by hand
    and against the definitions of \S7 and (0.4) of Lipman; also read in this
    pass, on the printed pages of the same scan, Lipman's Residue Theorem (0.6)
    with its condition (a), the normalization at regular local rings, on printed
    p. 24 and its condition (d), the globalization reading
    $\int_V:H^d(V,\omega_V)\to k$ as the residue at each closed point, on printed
    p. 25, which is the form the head of the solution cites. No other step was
    re-derived, and the comparison of step s8 in the case where the products of
    first Chern classes do not span is untouched and remains open.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A whole read of the rendered solution after the repairs of this day, for
    internal consistency only; nothing was changed. Checked and unchanged: the
    head's four paragraphs against the steps they announce, in particular that
    the one compatibility property it says is used, the divisor formula of s2, is
    the only one any part rests on and that s8, which uses Lemma 50.23.10, is
    used by no part and is marked so in the q.e.d.; the statement's normalization
    paragraphs (N) and (C) against the head's proof of both; s1 against (N); s2
    against the pages it cites, (0.6)(a),(d) on printed pp. 24--25, (12.1)--(12.2.3)
    on printed pp. 105--106, (13.1), (13.5) and (13.12) on printed pp. 111, 113,
    117; s6's convention against printed p. 218 and its two checks; s3's degrees
    in the projection formula and its induction; s4 against the printed hint,
    II.8.18 on printed p. 179 and I.7.7 on printed p. 53; s8's hypothesis and its
    two specialisations; the two remarks against the steps they name, including
    III.7.1 on printed p. 240, the definition and Proposition 7.2 on printed
    p. 241, Corollary 7.12 on printed p. 246, Remark 7.14 and Theorem 7.14.1 on
    printed p. 247, Corollary 7.13 on printed p. 247 and Appendix A's C1 on
    printed p. 430. Searched for and not found: any surviving occurrence of a
    lift-dependent claim, of a step described as an input, or of a reference to
    the withdrawn form of s3. The one statement that is not proved anywhere on
    the card, the comparison of s8 off the span of the complete-intersection
    classes, is not used by any part and is recorded in COMPLAINTS.md.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The transverse base change of step s3 and step s8 in its general form is
    available in the retained Stacks book, in the duality language rather than in
    the Hodge-cohomology one used here. Read on the printed pages in this pass:
    Lemma 48.7.1, "Trace map and base change", printed p. 4100, which says that
    for a tor-independent cartesian square the two ways of pushing the relative
    trace through the square agree; the paragraph on printed p. 4111 that
    specialises it to $X'=Y'\times_YX$, $\omega^\bullet_{X'/Y'}=L(g')^*
    \omega^\bullet_{X/Y}$ and the trace of $f'$ being the base change of the
    trace of $f$; and Section 48.10, Lemmas 48.10.1 and 48.10.2 on printed
    p. 4107, base change for the right adjoint $i^!$ of a pseudo-coherent closed
    immersion. With Lemma 50.24.3 on printed p. 4274, which identifies the
    relative trace $t:Rf_*\Omega^n_{X/S}[n]\to O_S$ with the duality trace, these
    give the identity once $i^!$ is read as the Gysin map, $\Omega^n[n]$ as the
    dualizing complex and the Serre pairings as the duality pairings. That
    translation is not carried out on this card, and no step uses it. A
    qualification added the same day: Section 48.10's isomorphism, Lemma 48.10.2
    on printed p. 4107, is proved for $f$ flat, and in the square used here both
    horizontal maps are closed immersions, so that lemma does not apply as it
    stands; what applies is the criterion of Lemma 48.10.1 on the same page, which
    reduces the question to the compatibility
    $Lj^*R\mathcal H om_{\OO_X}(\OO_H,\omega^\bullet_X)\cong
    R\mathcal H om_{\OO_Y}(\OO_Z,Lj^*\omega^\bullet_X)$ for two transverse closed
    immersions, with Lemma 48.10.3 on the same page as the tool. That
    compatibility is the Koszul statement that a Koszul resolution restricts to a
    Koszul resolution; it is not stated as such in the places read, and it is what
    would have to be supplied. Nothing of the card's own text was changed in this
    pass.

- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Step s9 is new and no part of the exercise needs it: the transverse base
    change holds on $H^q(Y,\Omega_Y^q)$ for every $q\ge n-1-p$, hence on all of
    the cohomology of a curve, for any nonsingular projective $X$. In that range
    the test classes of the pairing computation of s8 lie in degree
    $r=n-1-q-p\le0$: the space is zero, or it is $H^0(H,\OO_H)=k$ by Theorem
    I.3.4(a), printed p. 18, where the one class is the unit, which lifts. The
    projection formula $j^*i_*(i^*\beta)=j^*\beta\smile c_1(\OO_Y(H))$ of steps s3
    and s7 then gives the identity for every test class, and s8's equivalence
    turns that into the base change. This is a range s8 does not reach: for a
    curve in a threefold with $h^{1,1}>1$ the complete-intersection classes do not
    span $H^1(X,\Omega^1)$ and the detecting argument is silent, while s9 settles
    the statement. No other step was touched, and what stays open is unchanged:
    codimension $p\le n-2$ with $q<n-1-p$ in a general $X$.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The statement block checked sentence by sentence against the printed
    exercise, III.7.4 on printed pp. 249--250, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. $N$ is
    PDF p. $N+15$. Faithful in the opening paragraph (the map
    $\Omega_X\otimes\OO_Y\to\Omega_Y$ of II.8.12, the induced map
    $H^{n-p}(X,\Omega_X^{n-p})\to H^{n-p}(Y,\Omega_Y^{n-p})$, the trace, and the
    correspondence with $\eta(Y)\in H^p(X,\Omega_X^p)$ by (7.13)), and in parts
    (a), (c) and (d), including (d)'s hypothesis $p=1$ and the closing reference
    to Matsumura. Two passages are the card's and were added deliberately: the
    paragraph normalizing the trace at a point and on a finite reduced scheme,
    which the printed text leaves open and without which the numerical
    assertions of (b) and (d) have no meaning, and the paragraph fixing the
    point comparison (C); in part (b) the card also says which generator the
    identification of (Ex. 7.3) takes to $1$, the printed instruction being
    silent on that choice. Nothing else differs. No change was made to the card
    in this pass.
---

::: {.problem}
Let $X$ be a nonsingular projective variety of dimension $n$ over an algebraically closed field $k$. Let $Y$ be a nonsingular subvariety of codimension $p$, hence of dimension $n-p$. From the natural map $\Omega_X \tensor \mco_Y \to \Omega_Y$ of (II, 8.12) we deduce a map $\Omega_X^{n-p} \to \Omega_Y^{n-p}$. This induces a map on cohomology
$$
H^{n-p}(X, \Omega_X^{n-p}) \to H^{n-p}(Y, \Omega_Y^{n-p})
.$$
Now $\Omega_Y^{n-p} = \omega_Y$ is a dualizing sheaf for $Y$, so we have the trace map
$$
t_Y: H^{n-p}(Y, \Omega_Y^{n-p}) \to k
.$$

These trace maps are normalized so that the trace at a closed point is the identity: for a closed point $P$ the map $t_P: H^0(P, \OO_P) \to k$ is the identity of $k$, and on a finite reduced $k$-scheme the trace is the sum of the traces at its points.

On each nonsingular projective variety $V$ over $k$, the trace used below is further normalized by the point comparison
$$t_V\bigl(\gamma^{0,0}_{Q/V}(1)\bigr)=1$$
at a chosen closed point $Q\in V$, where $\gamma^{0,0}_{Q/V}:H^0(Q,\OO_Q)\to H^{\dim V}(V,\Omega_V^{\dim V})$ is the Gysin map of the closed immersion $Q\hookrightarrow V$ ([Stacks Project, Remark 50.23.7](https://stacks.math.columbia.edu/tag/0G8A), printed p. 4272).

Composing, we obtain a linear map $H^{n-p}(X, \Omega_X^{n-p}) \to k$. By (7.13) this corresponds to an element $\eta(Y) \in H^p(X, \Omega_X^p)$, which we call the cohomology class of $Y$.

(a) If $P \in X$ is a closed point, show that $t_X(\eta(P)) = 1$, where $\eta(P) \in H^n(X, \Omega^n)$ and $t_X$ is the trace map.

(b) If $X = \PP^n$, identify $H^p(X, \Omega^p)$ with $k$ by (Ex. 7.3), taking $1$ to be the class $1_{\PP^n}$ characterized by $t_{\PP^n}(1_{\PP^n}\smile\eta_{\PP^n}(L))=1$ for a general linear subspace $L\cong\PP^p$ of $\PP^n$ that cuts $Y$ in its $\deg Y$ distinct intersection points, and show that $\eta(Y) = (\deg Y) \cdot 1$, where $\deg Y$ is the degree of $Y$ as a projective variety (I, §7).

   [Hint: Cut with a hyperplane $H \subseteq X$, and use Bertini's theorem (II, 8.18) to reduce to the case $Y$ is a finite set of points.]

(c) For any scheme $X$ of finite type over $k$, we define a homomorphism of sheaves of abelian groups $d\log: \mco_X^* \to \Omega_X$ by $d\log(f) = f^{-1} \, df$. Here $\mco_X^*$ is a group under multiplication, and $\Omega_X$ is a group under addition. This induces a map on cohomology
$$
\Pic X = H^1(X, \mco_X^*) \to H^1(X, \Omega_X)
,$$
which we denote by $c$. See (Ex. 4.5).

(d) Returning to the hypotheses above, suppose $p = 1$. Show that $\eta(Y) = c(\mcl(Y))$, where $\mcl(Y)$ is the invertible sheaf corresponding to the divisor $Y$.

See Matsumura [1] for further discussion.
:::

::: {.solution}
Write $j:Y\hookrightarrow X$ for the closed immersion, put $n=\dim X$ and $p=\operatorname{codim}Y$, and write $\iota:D\hookrightarrow X$ for a nonsingular divisor when one is under discussion.

**The trace.** A proper $d$-dimensional $k$-variety $W$ carries one canonical $k$-linear map
$$
\int_W: H^d(W,\omega_W)\longrightarrow k
$$
characterized by its residues at the closed points of $W$: for each closed point $Q\in W$ the composite of the localization map with $\int_W$,
$$
H^d_Q(\omega_W)\longrightarrow H^d(W,\omega_W)\xrightarrow{\ \int_W\ }k,
$$
is the residue at $Q$ (Lipman, *Dualizing sheaves, differentials and residues on algebraic varieties*, Astérisque 117 (1984), Residue Theorem (0.6), printed pp. 24--25, conditions (a) and (d)), and at a regular point the residue is the classical one (Theorem (0.4), printed pp. 22--23, whose purely local description is §7). For $W$ nonsingular the sheaf of regular $d$-forms equals $\Omega_W^d$ ((0.2A), printed p. 14), and the pair $(\Omega_W^d,\int_W)$ is dualizing ((0.1)(d), printed p. 11); so $\int_W$ is a trace for Serre duality on $W$ (III.7.2, printed p. 241; III.7.6, printed p. 243).

The two normalizations of the statement hold for this trace, and single it out. Let $V$ be nonsingular of dimension $m$ and $Q\in V$ a closed point. The local description of the Gysin map fixes $1\mapsto df_1\wedge\cdots\wedge df_c/(f_1\cdots f_c)$ (Stacks Project, Lemma 50.23.5, tag 0G88, printed p. 4270, whose proof gives that local formula), so $\gamma^{0,0}_{Q/V}(1)$ is the image of the local class $dt_1\cdots dt_m/(t_1\cdots t_m)$ of $Q$. On $\PP^m$ the residue of that class at a closed point is $1$: (8.4) (printed p. 74) is the canonical isomorphism $\int_{\PP^m}$ under which the generator $Dx_0\cdots Dx_m/(x_0,\ldots,x_m)$ goes to $1$, and (8.5) (printed p. 75) says that the residue at every closed point is $\int_{\PP^m}$ composed with the localization. For a general nonsingular $V$ the number is the same, by completion-invariance and the finite étale case of (0.4)(a),(b) (printed p. 22), applied to a finite separable map $V\to\PP^m$ that is étale at $Q$ (Appendix A, printed p. 130). Hence $t_V(\gamma^{0,0}_{Q/V}(1))=1$, which is (C); and (N) holds as well, the residue being additive over the points of a finite reduced $k$-scheme, again by (0.6)(d). Since $\gamma^{0,0}_{Q/V}(1)\ne0$ (Stacks Project, Lemma 50.23.11, tag 0G8E, printed p. 4273) and $H^m(V,\Omega_V^m)$ is one-dimensional, at most one trace satisfies (C). Parts (b) and (d) are numerical identities, and they are assertions about this trace.

The class $\gamma^{0,0}_{Q/V}(1)$ does not depend on $Q$, so (C) constrains the trace and not the point. Let $\eta_\Delta=\gamma^{0,0}_\Delta(1)\in H^m(V\times V,\Omega^m_{V\times V})$ be the Gysin class of the diagonal $\Delta$, and let $\eta_0$ be its component in $H^m(V\times V,\OO_V\boxtimes\Omega_V^m)$; under K\"unneth write the component of $\eta_0$ in $H^0(V,\OO_V)\otimes H^m(V,\Omega_V^m)$ as $1\otimes\xi_V$. For a closed point $Q\in V$ the scheme-theoretic inverse image of $\Delta$ under $(Q,\operatorname{id})$ is $Q$, so Lemma 50.23.10 (tag 0G8D, printed pp. 4272--4273) gives $(Q,\operatorname{id})^*\eta_\Delta=\gamma^{0,0}_{Q/V}(1)$; pullback through the point kills the components with positive differential degree on the first factor and, within $\eta_0$, those with positive cohomology degree on the first factor, so
$$
\gamma^{0,0}_{Q/V}(1)=(Q^*\otimes\operatorname{id})(\eta_0)=\xi_V
$$
for every $Q$. This is the diagonal calculation of the proof of Lemma 50.24.4 (tag 0G8J, printed p. 4275), whose situation is proper smooth and equidimensional over the base, with no hypothesis on the characteristic.

**The Gysin map.** For a nonsingular closed immersion $j:Y\hookrightarrow X$ of codimension $p$ the Gysin map
$$
j_*:H^q(Y,\Omega_Y^q)\longrightarrow H^{q+p}(X,\Omega_X^{q+p})
$$
is defined by adjunction with $j^*$ under the pairing $\langle\alpha,\beta\rangle_V=t_V(\alpha\smile\beta)$:
$$
\langle j_*(a),b\rangle_X=\langle a,j^*b\rangle_Y .
$$
The definition is forced by the exercise and is not a further choice: the exercise defines $\eta(Y)$ as the class of the functional $b\mapsto t_Y(j^*b)$, so $\eta(Y)=j_*(1)$. By III.7.6 the pairing is perfect, so this determines $j_*$.

One compatibility property is used, and it is proved below: the residue formula for a nonsingular divisor, step [](#s2){.pf-ref}, which relates the trace on $X$ to the trace on $D$. In class form it is part (d), the Gysin class of a divisor being the $c_1$ of its invertible sheaf; step [](#s7){.pf-ref} reads that form off. Step [](#s3){.pf-ref} then computes the Gysin class of a smooth complete intersection, in particular of a linear subspace, from it and from the projection formula, and step [](#s4){.pf-ref} proves part (b) by cutting $Y$ with $n-p$ general hyperplanes and iterating the divisor formula on $Y$ itself, which is the cut the printed hint asks for. Part (a) uses only (N).

::: pf

::: {.pf-step #s1}

For a closed point $P\in X$,
$$
\boxed{t_X(\eta(P))=1}.
$$

::: pf-proof

This is the published proof of (a), in three forms that agree.  Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 3.7.4(a), printed p. 75: for a point $p=n$, and $H^0(X,\OO_X)\cong H^0(P,\OO_P)\cong k$, the morphism $H^0(X,\OO_X)\to H^0(P,\OO_P)$ "is just the restriction $s\mapsto s_P$, which is just the identity on $k$.  Hence it corresponds to the element $1$ in $H^n(X,\omega_X)\cong k$, i.e. $t_X(\eta(P))=1$".  Dongryul Kim, Exercise 3.7.4(a), PDF p. 170, puts the same argument in the Yoneda pairing: $H^p(X,\OO_X)\times\Ext^{n-p}(\OO_X,\omega_X)\to H^n(X,\omega_X)\xrightarrow{t_X}k$, so for $p=0$ the composite $H^0(X,\OO_X)\xrightarrow{\eta(P)}H^0(X,\OO_X)\times\Ext^n(\OO_X,\omega_X)\to H^n(\omega_X)\xrightarrow{t_X}k$ is "equal to evaluation at $P$", and plugging in $1$ gives $t_X(\eta(P))=1\in k$.  Math StackExchange 1794757, answer by the account S.M. (2016-05-22), isolates the normalization the third form needs: with $j$ the inclusion of a point, the map of the exercise is $H^0(X,\OO_X)\to H^0(P,\OO_P)$, "which is actually the identity map on $k$", the class $\zeta$ corresponds to $x=i(\zeta)\circ\varphi$ under the double dual of the pairing, and hence $t_P(1)=t_X(\zeta)$; his closing paragraph notes that $t_P(1)$ can be any element of $k^*$ and that the answer requires $t_P(1)=1$.

Here $p=n$, so the functional defining $\eta(P)$ is the composite
$$
H^0(X,\OO_X)\xrightarrow{j^*}H^0(P,\OO_P)
\xrightarrow{t_P}k.
$$
Since $X$ is projective and integral over the algebraically closed field $k$,
$$
H^0(X,\OO_X)=k,
$$
and since $P\cong\Spec k$, the restriction map is the identity on $k$.
By (N), $t_P=\operatorname{id}_k$, so the functional sends $1$ to $1$.

Under Serre duality, evaluating that functional at $1\in H^0(X,\OO_X)$ is the same as pairing $\eta(P)$ with $1$:
$$
1
=\langle\eta(P),1\rangle_X
=t_X(\eta(P)).
$$
This proves part (a).

:::

:::

::: {.pf-step #s2}

Let $\iota:D\hookrightarrow X$ be a nonsingular divisor in a nonsingular projective variety $X$ of dimension $n$. For every $\nu\in H^{n-1}(X,\Omega_X^{n-1})$,
$$
\boxed{t_X\bigl(c(\mcl(D))\smile\nu\bigr)=t_D\bigl(\restrictionof{\nu}{D}\bigr)} .
$$
Both sides are computed from one class on $X$ and its restriction to $D$, so no class of $D$ has to be lifted, and by (III.7.6, printed p. 243) the identity is equivalent to the class identity $c(\mcl(D))=\iota_*(1)$: the class of a divisor is its Gysin class.

::: pf-proof

**The class.** By part (c), $c$ is the map on cohomology induced by $d\log$. On an open cover $(U_i)$ of $X$ carrying local equations $f_i$ of $D$, the class $c(\mcl(D))$ is represented by the Čech cocycle
$$
\Bigl\{\frac{df_j}{f_j}-\frac{df_i}{f_i}\Bigr\}_{ij}
$$
of step [](#s6){.pf-ref}, in the transition convention used there. On the cover of a neighbourhood of a closed point $Q\in D$ by $U_1=X\setminus D$, where $f_1=1$, and by an open $U_2$ on which $f_2=t_1$ is a local parameter cutting $D$ out transversally, the same cocycle reads
$$
c_{12}=\frac{dt_1}{t_1}=d\log t_1 ,
$$
so the local representative of $c(\mcl(D))$ at $Q$ is $d\log t_1$.

**The residue of the product.** The sheaf $\Omega_X^n(D)=\Omega_X^n\tensor\OO_X(D)$ of $n$-forms with at most a simple pole along $D$ sits in the exact sequence
$$
0\longrightarrow\Omega_X^n\longrightarrow\Omega_X^n(D)\xrightarrow{\ \operatorname{res}_D\ }\Omega_D^{n-1}\longrightarrow0 ,
$$
the last map being the Poincar\'e residue: on $U_2$ it sends $t_1^{-1}dt_1\wedge dt_2\wedge\cdots\wedge dt_n$ to $dt_2\wedge\cdots\wedge dt_n$. Near $Q$ the class $\nu$ has a holomorphic representative, so $c(\mcl(D))\smile\nu$ is represented by the product of that representative with $dt_1/t_1$, whose only pole is the simple pole $dt_1/t_1$ along $D$; the residue of that pole is the remaining factor, which is the local class of $\restrictionof{\nu}{D}$:
$$
\operatorname{res}_D\bigl(c(\mcl(D))\smile\nu\bigr)=\restrictionof{\nu}{D}.
$$

**The residues.** Both sides are computed by residues at the closed points. At a closed point $Q\notin D$ the class $c(\mcl(D))\smile\nu$ has a holomorphic representative, so its residue at $Q$ vanishes, and $t_D$ contributes nothing there. At a closed point $Q\in D$ choose coordinates $t_1,\ldots,t_n$ with $f=t_1$, and let $a\,dt_2\cdots dt_n/(t_2\cdots t_n)$ be the local class of $\restrictionof{\nu}{D}$ at $Q$, with $a\in k$; by the previous paragraph the local class of $c(\mcl(D))\smile\nu$ at $Q$ is $a\,dt_1\cdots dt_n/(t_1\cdots t_n)$, and the residues of the two classes at $Q$ are both $a$. So for every closed point $Q$ the two residues agree, those of the class $c(\mcl(D))\smile\nu$ at the points of $D$ being the numbers $a_Q$ and those of $\restrictionof{\nu}{D}$ the same numbers.

**The two traces.** The formula is the residue theorem for the pair $(D,X)$, and three statements of Lipman's compose to it. The first presents a class of $X$ by local data and computes its trace from the data: for a complex $C$ exact outside a finite set and a map $\psi:C_n\to\Omega_X^n$, (12.1) attaches to the class a family of local classes $[\psi/C]_Q$, Proposition (12.2) says that the sum of their residues vanishes when the class vanishes, and Remark (12.2.3) (printed pp. 105--106) reads (0.6)(d) as the consequence, that the sum of the residues of a presentation is the trace of the class presented; (12.2.2) allows $\omega$ and $\operatorname{res}$ to be replaced by their smooth-local counterparts. The second is the presentation of a class carried from $D$: the fundamental local homomorphism (13.1) with Theorem (13.5) (printed pp. 111, 113) identifies $\omega_D$ with $\operatorname{Ext}^1_{\OO_X}(\OO_D,\omega_X)$ and realizes the adjunction as (13.4). The third is the local agreement of the constants, Theorem (13.12) (printed p. 117): the residue at a closed point of the adjunction-lift of a class is the residue at that point of the class itself, which is the identity $\operatorname{res}_D(c(\mcl(D))\smile\nu)=\restrictionof{\nu}{D}$ computed in the previous paragraph. Composing, the class $c(\mcl(D))\smile\nu$ satisfies
$$
t_X\bigl(c(\mcl(D))\smile\nu\bigr)
=\sum_{Q\in D}a_Q
=t_D\bigl(\restrictionof{\nu}{D}\bigr),
$$
which is the asserted formula.

**The case of a curve, where the book fixes the constant.** For $n=1$ and $X$ a curve the formula is the computation of step [](#s7){.pf-ref} below: there $c(\mcl(D))$ is the class of $df/f$ at a point $D=\{Q\}$ with $f$ a local parameter, the trace is the residue of Theorem III.7.14.1 (printed p. 247), and the value is $+1$, which is the constant claimed here. With the opposite transition convention the cocycle of step [](#s6){.pf-ref} would be $-df/f$ and the formula would carry the sign $-1$ on the left, since the right hand side is unchanged; the convention of step [](#s6){.pf-ref} is the one under which the two sides agree.

:::

:::

::: {.pf-step #s3}

Let $D_1,\ldots,D_r$ be nonsingular divisors of a nonsingular projective variety $X$ such that every intersection $Y_k=D_1\cap\cdots\cap D_k$ is nonsingular of codimension $k$, and let $\iota_k:Y_k\hookrightarrow X$ be the inclusion; put $Y=Y_r$. Then
$$
\boxed{\eta(Y_k)=(\iota_k)_*(1)=c(\mcl(D_1))\smile\cdots\smile c(\mcl(D_k))}
$$
in $H^k(X,\Omega_X^k)$, the empty product for $k=0$ being $1$. If in addition $H\subseteq X$ is a nonsingular divisor meeting every $Y_k$ transversely, and $Z=Y\cap H$, then
$$
\boxed{i^*\eta(Y)=\eta_H(Z)},
$$
which is the base change $i^*j_*=(j_H)_*\,i_Y^*$ of the transverse square for the class $1$.

::: pf-proof

**The projection formula.** Let $\iota:D\hookrightarrow X$ be a nonsingular divisor in a nonsingular projective variety $X$ of dimension $n$. For $x\in H^q(D,\Omega_D^q)$ and $\gamma\in H^m(X,\Omega_X^m)$ with $q+m+1\le n$,
$$
\iota_*\bigl(x\smile\restrictionof{\gamma}{D}\bigr)=\iota_*(x)\smile\gamma .
$$
Both sides lie in $H^{q+m+1}(X,\Omega_X^{q+m+1})$, which is dual to $H^{n-q-m-1}(X,\Omega_X^{n-q-m-1})$. For $z$ in that space the adjunction identity that defines $\iota_*$, applied once with $y=x\smile\restrictionof{\gamma}{D}$ and once with $y=x$, gives
$$
t_X\bigl(\iota_*\bigl(x\smile\restrictionof{\gamma}{D}\bigr)\smile z\bigr)
=t_D\bigl(x\smile\restrictionof{\gamma}{D}\smile\restrictionof{z}{D}\bigr)
=t_X\bigl(\iota_*(x)\smile\gamma\smile z\bigr),
$$
the middle term being $t_D\bigl(x\smile\restrictionof{(\gamma\smile z)}{D}\bigr)$ because restriction is a ring homomorphism. The pairing is perfect (III.7.6, printed p. 243), so the two classes agree.

**The class of a complete intersection.** Put $Y_0=X$ and let $\nu_k:Y_k\hookrightarrow Y_{k-1}$ be the inclusion, so that $\iota_k=\iota_{k-1}\circ\nu_k$. The two adjunction Gysin maps compose, in the sense that
$$
(\iota_k)_*(1)=(\iota_{k-1})_*\bigl((\nu_k)_*(1)\bigr),
$$
because each side pairs with $w\in H^{n-k}(X,\Omega^{n-k})$ to $t_{Y_k}(\restrictionof{w}{Y_k})$: for the left side that is the definition of $(\iota_k)_*$, and for the right side that of $(\nu_k)_*$ followed by that of $(\iota_{k-1})_*$. The claim is $(\iota_k)_*(1)=c(\mcl(D_1))\smile\cdots\smile c(\mcl(D_k))$, by induction on $k$; the case $k=1$ is part (d) in the class form of step [](#s2){.pf-ref}. For $k\ge2$ the divisor $Y_k$ of $Y_{k-1}$ is cut out by $D_k$, so $\restrictionof{\mcl(D_k)}{Y_{k-1}}\cong\OO_{Y_{k-1}}(Y_k)$, and step [](#s2){.pf-ref} applied to the divisor $Y_k$ of $Y_{k-1}$ gives
$$
(\nu_k)_*(1)=c\bigl(\OO_{Y_{k-1}}(Y_k)\bigr)=\restrictionof{c(\mcl(D_k))}{Y_{k-1}} .
$$
The projection formula and the induction hypothesis then give
$$
(\iota_k)_*(1)
=(\iota_{k-1})_*\bigl(\restrictionof{c(\mcl(D_k))}{Y_{k-1}}\bigr)
=(\iota_{k-1})_*(1)\smile c(\mcl(D_k))
=c(\mcl(D_1))\smile\cdots\smile c(\mcl(D_k)).
$$
The case used in step [](#s4){.pf-ref} is $X=\PP^n$ with the $D_i$ hyperplanes, where $L=Y_r\cong\PP^{n-r}$.

**Base change in this case.** If $H$ meets every $Y_k$ transversely, then $Y_k\cap H$ is a nonsingular divisor of $Y_{k-1}\cap H$, cut out by the restriction of $D_k$, so the formula just proved applies in $H$ to the divisors $D_k\cap H$ and gives
$$
\eta_H(Z)=c\bigl(\mcl_H(D_1\cap H)\bigr)\smile\cdots\smile c\bigl(\mcl_H(D_r\cap H)\bigr).
$$
Since $\mcl_H(D_k\cap H)=i^*\mcl(D_k)$ and $i^*$ is a ring homomorphism on $H^*(\Omega^\bullet)$,
$$
i^*\eta(Y)=i^*\bigl(c(\mcl(D_1))\smile\cdots\smile c(\mcl(D_r))\bigr)
=c(i^*\mcl(D_1))\smile\cdots\smile c(i^*\mcl(D_r))=\eta_H(Z),
$$
which is the identity of the statement.

:::

:::

::: {.pf-step #s4}

If $X=\PP^n$ and $Y$ has codimension $p$, then
$$
\boxed{\eta(Y)=(\deg Y)\cdot1\in H^p(\PP^n,\Omega_{\PP^n}^p)\cong k}.
$$

::: pf-proof

Write $d=\deg Y$ and $m=n-p$, and choose hyperplanes $H_1,\ldots,H_m\subseteq\PP^n$ in general position, putting $L=H_1\cap\cdots\cap H_m\cong\PP^p$. Also put $Y_0=Y$ and $Y_k=Y\cap H_1\cap\cdots\cap H_k$ for $1\le k\le m$, so that $Y_m=Y\cap L$. By Bertini's theorem (II.8.18, printed p. 179), for a nonsingular $Y_{k-1}$ the hyperplanes $H$ with $H\cap Y_{k-1}$ regular at every point form a dense open subset of the dual space; choosing $H_1,\ldots,H_m$ successively, each in that open set and linearly independent of those already chosen, makes every $Y_k$ a nonsingular divisor of $Y_{k-1}$. Read $\deg$ of a nonsingular scheme as the sum of the degrees of its irreducible components; Bézout's theorem (I.7.7, printed p. 53), applied to $Y_{k-1}$ and $H_k$, gives
$$
\sum_j i(Y_{k-1},H_k;Z_j)\,\deg Z_j=\deg Y_{k-1}\cdot\deg H_k
$$
over the irreducible components $Z_j$ of $Y_k$, and each local ring of the regular scheme $Y_k$ has multiplicity $1$, so
$$
\deg Y_k=\deg Y_{k-1}\cdot\deg H_k=\deg Y_{k-1}=\cdots=\deg Y=d .
$$
For $k=m$ the scheme $Y_m\subseteq L$ has dimension $0$ and is reduced, so it is a set of $d$ distinct closed points,
$$
Y\cap L=\{P_1,\ldots,P_d\}.
$$

**The class of $L$.** Let $\alpha_0=\eta_{\PP^n}(L)=i_*(1)\in H^m(\PP^n,\Omega_{\PP^n}^m)$ be the class of the linear subspace, where $i:L\hookrightarrow\PP^n$. By step [](#s3){.pf-ref},
$$
\alpha_0=c(\mcl(H_1))\smile\cdots\smile c(\mcl(H_m)) ,
$$
the empty product for $m=0$ being $1$.

**The pairing of the two classes.** Write $D_k=Y\cap H_k$, which is a nonsingular divisor of $Y$ for every $k$, write $c_Y=c(\OO_Y(D_k))\in H^1(Y,\Omega_Y)$, the same class for every $k$ because $\OO_Y(D_k)\cong\OO_Y(1)$, and write $c_Y^{\,m}$ for its $m$-fold cup power. Since $\eta(Y)$ is the class of the functional $w\mapsto t_Y(\restrictionof{w}{Y})$, for every $w\in H^m(\PP^n,\Omega_{\PP^n}^m)$,
$$
\langle\eta(Y),w\rangle_{\PP^n}=t_{\PP^n}\bigl(\eta(Y)\smile w\bigr)=t_Y\bigl(\restrictionof{w}{Y}\bigr).
$$
Restriction is a ring homomorphism, and $\restrictionof{c(\mcl(H_k))}{Y}=c(\restrictionof{\mcl(H_k)}{Y})=c(\OO_Y(D_k))=c_Y$; so $\restrictionof{\alpha_0}{Y}=c_Y^{\,m}$, and
$$
\langle\eta(Y),\alpha_0\rangle_{\PP^n}=t_Y\bigl(c_Y^{\,m}\bigr).
$$

**The count on $Y$.** The variety $Y$ is nonsingular projective of dimension $m$, and $Y_1=D_1$ is a nonsingular divisor in it with $\mcl(Y_1)=\OO_Y(1)$. Step [](#s2){.pf-ref}, applied to the pair $(Y_1,Y)$ with $\nu=c_Y^{\,m-1}$, gives
$$
t_Y\bigl(c_Y^{\,m}\bigr)=t_Y\bigl(c(\mcl(Y_1))\smile c_Y^{\,m-1}\bigr)=t_{Y_1}\bigl(\restrictionof{c_Y^{\,m-1}}{Y_1}\bigr).
$$
Repeating this along $Y_1\supseteq Y_2\supseteq\cdots\supseteq Y_m$, whose members are nonsingular divisors of their predecessors with $\restrictionof{\OO_{Y_{k-1}}(1)}{Y_k}=\OO_{Y_k}(1)$, and then applying the normalization (N) to the finite reduced scheme $Y_m$,
$$
t_Y\bigl(c_Y^{\,m}\bigr)=t_{Y_m}(1)=\sum_{a=1}^d t_{P_a}(1)=d .
$$
The case $m=0$, where $Y=Y_m$ is already the set of $d$ points and the products are empty, is the same computation starting from $t_Y(1)=d$. In either case $\langle\eta(Y),\alpha_0\rangle_{\PP^n}=d\ne0$, and in particular $\alpha_0\ne0$.

**The scalar.** By Exercise III.7.3 the space $H^p(\PP^n,\Omega_{\PP^n}^p)$ is one-dimensional, and by (III.7.6, printed p. 243) the pairing is perfect. Since $\alpha_0\ne0$, the functional $u\mapsto\langle u,\alpha_0\rangle_{\PP^n}$ on that one-dimensional space is nonzero, hence injective, and the class $1_{\PP^n}$ of the statement, characterized by $t_{\PP^n}(1_{\PP^n}\smile\alpha_0)=1$, is the unique class pairing to $1$ with $\alpha_0$. Now $\langle d\cdot1_{\PP^n},\alpha_0\rangle_{\PP^n}=d=\langle\eta(Y),\alpha_0\rangle_{\PP^n}$, so $\eta(Y)-d\cdot1_{\PP^n}$ pairs to $0$ with $\alpha_0$ and vanishes:
$$
\eta(Y)=d\cdot1_{\PP^n},
$$
which is part (b).

:::

:::

::: {.pf-step #s5}

The rule
$$
d\log(f)=f^{-1}df
$$
is a morphism of sheaves of abelian groups
$$
d\log:\OO_X^*\longrightarrow\Omega_X.
$$

::: pf-proof

Yang Pi-Yeh, Solution 3.7.4(c), printed p. 75: "We just need to prove that $d\log$ is a morphism of sheaves of abelian groups.  Since on $\Omega_X$, we know $d(fg)=f\,dg+g\,df$", and then the three-line computation displayed below.  Kim, Exercise 3.7.4(c), PDF p. 170, writes the same verification and cites Exercise III.4.5 (printed p. 224) for $\Pic X=H^1(X,\OO_X^*)$.

For local units $f,g$,
$$
\begin{aligned}
d\log(fg)
&=(fg)^{-1}d(fg)\\
&=f^{-1}g^{-1}(f\,dg+g\,df)\\
&=f^{-1}df+g^{-1}dg\\
&=d\log(f)+d\log(g).
\end{aligned}
$$
The construction commutes with restriction to smaller open sets because Kähler differentiation does.
Therefore it is a morphism from the multiplicative sheaf $\OO_X^*$ to the additive sheaf $\Omega_X$.
Passing to first cohomology and using
$$
\Pic X\cong H^1(X,\OO_X^*)
$$
gives the homomorphism
$$
c:\Pic X\longrightarrow H^1(X,\Omega_X)
$$
required in part (c).

:::

:::

::: {.pf-step #s6}

If $Y\subseteq X$ is a nonsingular divisor with local equations $f_i=0$ on an open cover $(U_i)$, then $c(\mcl(Y))$ is represented by the Čech cocycle
$$
\left\{\frac{df_j}{f_j}-\frac{df_i}{f_i}\right\}_{ij}.
$$

::: pf-proof

The invertible sheaf $\mcl(Y)=\OO_X(Y)$ has local generator $e_i=f_i^{-1}$ on $U_i$.
Use the convention $s_i=g_{ij}s_j$ for the transition functions of a line
bundle, which is the one Hartshorne's Čech complex carries (printed p. 218):
its differential is $(d\alpha)_{i_0i_1}=\alpha_{i_1}-\alpha_{i_0}$, and
$g_{ij}g_{jk}=g_{ik}$ is the multiplicative form of
$(d\alpha)_{ijk}=0$. With $s_i=e_i$ this gives
$f_i^{-1}=g_{ij}f_j^{-1}$, that is
$$
g_{ij}=\frac{f_j}{f_i},
$$
and its image under $d\log$ is
$$
d\log\!\left(\frac{f_j}{f_i}\right)
=\frac{df_j}{f_j}-\frac{df_i}{f_i}.
$$
This is the displayed cocycle. On a curve with $Y=\{P\}$, on the cover $U_1=X\setminus P$, where $f_1=1$, and $U_2$ a neighbourhood of $P$ on which $f_2=f$ is a local parameter, it reads $c_{12}=df/f$, whose residue at $P$ is $1$ by Theorem III.7.14.1(c) (printed p. 247). The opposite convention $e_j=g_{ij}e_i$ gives
$g_{ij}=f_i/f_j$ and the cocycle with both signs reversed, $-df/f$, which is the class of
the inverse line bundle $\OO(-P)$; the sign matters, and step [](#s2){.pf-ref} fixes it.

**A second check of the sign, in codimension two.** For the lines $L_1=\{x_0=0\}$ and $L_2=\{x_1=0\}$ of $\PP^2$, on the affine opens $U_i=\{x_i\ne0\}$, the local equations $f^1=(1,x_0/x_1,x_0/x_2)$ and $f^2=(x_1/x_0,1,x_1/x_2)$ give, by the formula above, the same cocycle
$$
\Bigl(d\log\frac{x_0}{x_1},\ d\log\frac{x_0}{x_2},\ d\log\frac{x_1}{x_2}\Bigr)
$$
on the pairs $01,02,12$. The cup product of the two classes is the $2$-cocycle $a_{01}\wedge b_{12}$ with values in $\Omega^2$, and on $U_{012}$
$$
a_{01}\wedge b_{12}
=d\log\frac{x_0}{x_1}\wedge d\log\frac{x_1}{x_2}
=d\log\frac{x_1}{x_0}\wedge d\log\frac{x_2}{x_0},
$$
because $d\log(x_0/x_1)=-d\log(x_1/x_0)$ and $d\log(x_1/x_2)=d\log(x_2/x_0)-d\log(x_1/x_0)$. Its residues at the closed points are $+1$ at $[1:0:0]$, $-1$ at $[0:1:0]$ and $+1$ at $[0:0:1]$, computed in the affine coordinates $x_j/x_i,\ x_k/x_i$ at each, and $0$ everywhere else, where the form is holomorphic; so its trace is $1$, which is $L_1\cdot L_2$ by Bézout's theorem (I.7.7, printed p. 53). With the opposite transition convention both cocycles would change sign and the trace would be $-1$.

:::

:::

::: {.pf-step #s7}

For a nonsingular divisor $Y\subseteq X$,
$$
\boxed{\eta(Y)=c(\mcl(Y))\in H^1(X,\Omega_X)}.
$$

::: pf-proof

Both sides lie in $H^1(X,\Omega_X)$, which is dual to $H^{n-1}(X,\Omega_X^{n-1})$ under the Serre pairing (III.7.6). For $\nu\in H^{n-1}(X,\Omega_X^{n-1})$ the definition of $\eta(Y)$ gives
$$
\langle\eta(Y),\nu\rangle_X=t_X\bigl(j_*(1)\smile\nu\bigr)=t_Y(\restrictionof{\nu}{Y}),
$$
while step [](#s2){.pf-ref}, applied to the divisor $Y$, gives
$$
t_X\bigl(c(\mcl(Y))\smile\nu\bigr)=t_Y(\restrictionof{\nu}{Y}).
$$
By step [](#s6){.pf-ref} the class $c(\mcl(Y))$ is the cocycle $\{df_j/f_j-df_i/f_i\}$ of local equations of $Y$. The two classes pair equally with every $\nu$, and the pairing is perfect, so $c(\mcl(Y))=\eta(Y)$. This is part (d).

In dimension one the same computation is the residue theorem of the book. Let $X$ be a curve, $Y=\{P\}$, and take the cover $U_1=X\setminus P$ with $f_1=1$ and $U_2$ a neighbourhood of $P$ on which $f_2=f$ is a local parameter. By step [](#s6){.pf-ref} the class $c(\OO(P))$ is $c_{12}=df/f$ on $U_1\cap U_2$. The trace of Remark III.7.14 (printed p. 247) is the sum of the residues of the principal parts, the principal part of $df/f$ at $P$ is $df/f$ itself, and Theorem III.7.14.1(c) (printed p. 247) gives
$$
\operatorname{res}_P\left(\frac{df}{f}\right)=v_P(f)\cdot1=1 .
$$
So $t_X(c(\OO(P)))=+1=t_P(1)$, which is the case $n=1$ of the formula of step [](#s2){.pf-ref}, and confirms its constant.

:::

:::

::: {.pf-step #s8}

Let $X$ be a nonsingular projective variety of dimension $n$ over $k$ and let $Y\subseteq X$ be nonsingular of codimension $p$. For every smooth complete intersection $L\subseteq X$ of dimension $p$ that meets $Y$ transversely, in $N$ points,
$$
\boxed{\bigl\langle\eta(Y)-\gamma^{0,0}_{Y/X}(1),\,\eta_X(L)\bigr\rangle_X=0} .
$$
Consequently, if the classes $\eta_X(L)$ of such complete intersections span the space $H^{n-p}(X,\Omega_X^{n-p})$, then
$$
\eta(Y)=\gamma^{0,0}_{Y/X}(1)
\qquad\text{in } H^p(X,\Omega_X^p),
$$
and if $H\subseteq X$ is a nonsingular divisor with $Y\pitchfork H$ for which the same spanning holds in $H$ for the codimension $p$ of $Z=Y\cap H$, then $i^*j_*=(j_H)_*\,i_Y^*$. For $X=\PP^n$ the space $H^{n-p}(\PP^n,\Omega^{n-p})$ is one-dimensional (Exercise III.7.3, printed p. 249) and spanned by such a class, so the corollary covers subvarieties of projective space in every codimension; for a nonsingular projective $X$ of dimension at most two it holds in every codimension, $p=1$ being the divisor case of step [](#s2){.pf-ref} and $p=2$ having $H^0(X,\OO_X)=k$; and for $p=n$, where $Y$ is a point, the equality itself holds by (C) with step [](#s1){.pf-ref}.

::: pf-proof

**The vanishing.** Let $\mathcal L$ be ample and let $D_1,\ldots,D_{n-p}\in\linearsystem{\mathcal L}$ be general, so that $L=D_1\cap\cdots\cap D_{n-p}$ is nonsingular of dimension $p$ and meets $Y$ transversely in $N$ reduced points $Z=Y\cap L$; this is Bertini's theorem (II.8.18, printed p. 179) applied successively. By step [](#s3){.pf-ref} the class of the complete intersection is
$$
\alpha_0:=\eta_X(L)=i_*(1)=c(\mcl(D_1))\smile\cdots\smile c(\mcl(D_{n-p}))\in H^{n-p}(X,\Omega_X^{n-p}),
$$
where $i:L\hookrightarrow X$. The two pairings with $\alpha_0$ are computed as in the proof of step [](#s4){.pf-ref}.

**The trace side.** Since $\eta(Y)$ is the class of the functional $b\mapsto t_Y(\restrictionof{b}{Y})$,
$$
\langle\eta(Y),\alpha_0\rangle_X=t_X\bigl(\eta(Y)\smile\alpha_0\bigr)=t_Y\bigl(\restrictionof{\alpha_0}{Y}\bigr)
=t_Y\bigl(c_1(\restrictionof{\mathcal L}{Y})^{\smile\dim Y}\bigr)=N,
$$
the third equality because $\restrictionof{c(\mcl(D_j))}{Y}=c(\restrictionof{\mathcal L}{Y})$ for every $j$, and the last one iterating step [](#s2){.pf-ref} along the divisors $Y\cap D_1$, $Y\cap D_1\cap D_2,\ldots$ of the successive intersections and then applying (N) at the $N$ points.

**The Koszul side.** By the adjunction identity that defines $i_*$,
$$
\bigl\langle\gamma^{0,0}_{Y/X}(1),\alpha_0\bigr\rangle_X
=t_X\bigl(\gamma^{0,0}_{Y/X}(1)\smile i_*(1)\bigr)
=t_L\bigl(\restrictionof{\gamma^{0,0}_{Y/X}(1)}{L}\bigr).
$$
Each square $Y\cap D_1\cap\cdots\cap D_j$ over $D_1\cap\cdots\cap D_j$ and $Y\cap D_1\cap\cdots\cap D_{j-1}$ over $D_1\cap\cdots\cap D_{j-1}$ is cartesian and transverse, its vertical maps are Koszul regular immersions, and the ambient schemes are smooth over $k$; so Lemma 50.23.10 of the Stacks Project ([tag 0G8D](https://stacks.math.columbia.edu/tag/0G8D), printed pp. 4272--4273), applied successively to $D_1,\ldots,D_{n-p}$, gives
$$
\restrictionof{\gamma^{0,0}_{Y/X}(1)}{L}=\gamma^{0,0}_{Z/L}(1).
$$
The construction of $\gamma$ is local on its source (Lemma 50.23.3, printed p. 4269), so on the finite reduced scheme $Z$ it is the sum over its points, and the normalization (C) gives trace $1$ at each of them:
$$
\bigl\langle\gamma^{0,0}_{Y/X}(1),\alpha_0\bigr\rangle_X
=t_L\bigl(\gamma^{0,0}_{Z/L}(1)\bigr)
=\sum_{Q\in Z}t_L\bigl(\gamma^{0,0}_{Q/L}(1)\bigr)=N .
$$
The two pairings agree, which is the displayed vanishing for the class of this particular complete intersection; a general one is of this form for its own ample class and general members, and the pairing is linear in $\alpha_0$.

**The consequences.** The classes $\eta_X(L)$ of smooth complete intersections of codimension $n-p$ are exactly the $n-p$-fold products of first Chern classes of invertible sheaves: one inclusion is step [](#s3){.pf-ref}, and for the other it suffices that every invertible sheaf is a difference of two very ample ones, $c_1(\mathcal L)=c_1(\mathcal L\otimes\mathcal M)-c_1(\mathcal M)$ for $\mathcal M$ ample enough, and that a very ample class is the class of a hyperplane section, whose products are complete-intersection classes. So the spanning condition below says that $H^{n-p}(X,\Omega^{n-p})$ is generated by products of first Chern classes; for $p=n-1$, where $Y$ is a curve, the products are single classes, and the condition is that the image of $c:\operatorname{Pic}X\otimes k\to H^1(X,\Omega^1)$ of part (c) be the whole of $H^1(X,\Omega^1)$. If that holds, then $\eta(Y)-\gamma^{0,0}_{Y/X}(1)$ pairs to zero with every class of the space; by (III.7.6, printed p. 243) it is zero. Under the same spanning condition in $H$, the equality proved in $H$ gives $\eta_H(Z)=\gamma^{0,0}_{Z/H}(1)$, and Lemma 50.23.10 (printed pp. 4272--4273) for the square over $H$ gives
$$
i^*j_*(1)=i^*\eta(Y)=i^*\gamma^{0,0}_{Y/X}(1)=\gamma^{0,0}_{Z/H}(1)=\eta_H(Z)=(j_H)_*i_Y^*(1).
$$
For a class $a\in H^q(Y,\Omega_Y^q)$ and $w\in H^{n-1-q-p}(H,\Omega^{n-1-q-p})$, the left side pairs as $t_X(j_*a\smile i_*w)=t_Y(a\smile j^*i_*w)$ and the right side as $t_Z(i_Y^*a\smile j_H^*w)=t_Y(c_1(\OO_Y(H))\smile a\smile j^*w)$, the second equality by step [](#s2){.pf-ref} applied to the divisor $Z$ of $Y$. So the case $a=1$ says, by perfectness of the pairing on $Y$, that $j^*i_*w=c_1(\OO_Y(H))\smile j^*w$ for every $w$, and that identity gives the general $a$, hence the displayed base change.

For $p=n$ the class $\eta(Y)-\gamma^{0,0}_{Y/X}(1)$ lies in the one-dimensional space $H^n(X,\Omega_X^n)$ and has trace $t_X(\eta(Y))-t_X(\gamma^{0,0}_{Y/X}(1))=1-1=0$ by step [](#s1){.pf-ref} and by (C), so it is zero.

:::

:::

::: {.pf-step #s9}

Let $i:H\hookrightarrow X$ be a nonsingular divisor of a nonsingular projective variety $X$ of dimension $n$, let $j:Y\hookrightarrow X$ be nonsingular of codimension $p$ with $Y\pitchfork H$, and put $Z=Y\cap H$. Then
$$
\boxed{i^*j_*=(j_H)_*\,i_Y^*}
$$
on $H^q(Y,\Omega_Y^q)$ for every $q\ge n-1-p$. In particular, for a curve $Y\subseteq X$, where $p=n-1$, it holds on all of $H^*(Y,\Omega^\bullet_Y)$.

::: pf-proof

By the computation at the end of the proof of step [](#s8){.pf-ref}, the identity for a class $a\in H^q(Y,\Omega_Y^q)$ is equivalent to the projection formula
$$
j^*i_*w=c_1(\OO_Y(H))\smile j^*w
\qquad\text{for every } w\in H^{r}(H,\Omega_H^{r}),\quad r=n-1-q-p .
$$
For $q\ge n-1-p$ one has $r\le0$; the space is $0$ if $r<0$, and if $r=0$ it is $H^0(H,\OO_H)=k$ (Theorem I.3.4(a), printed p. 18), spanned by the unit. The unit is the restriction of the unit of $H^0(X,\OO_X)$, so the identity is needed only for $w=i^*\beta$ with $\beta\in H^0(X,\OO_X)$, where it is the projection formula of step [](#s3){.pf-ref} together with the class of a divisor,
$$
j^*i_*(i^*\beta)=j^*\bigl(\beta\smile i_*(1)\bigr)=j^*\beta\smile j^*\bigl(c_1(\OO_X(H))\bigr)=c_1(\OO_Y(H))\smile j^*\beta,
$$
the middle step by step [](#s7){.pf-ref}, $i_*(1)=c_1(\OO_X(H))$. Hence the projection formula holds for every $w$ in the range, and with it the identity.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a) from the normalization (N). Step [](#s5){.pf-ref} proves part (c). Step [](#s2){.pf-ref} proves the residue formula for a nonsingular divisor, valid in every dimension, and step [](#s7){.pf-ref} reads part (d) off it, the class of a divisor being the $c_1$ of its invertible sheaf. Step [](#s3){.pf-ref} identifies the Gysin class of a smooth complete intersection with the product of the $c_1$ of the divisors cutting it out, and step [](#s4){.pf-ref} pairs that class with the class of $Y$, counting $d=\deg Y$ by the divisor formula of step [](#s2){.pf-ref} along the hyperplane sections of $Y$, which is part (b). Step [](#s8){.pf-ref} adds two statements that no part of the exercise needs: $\eta(Y)$ and the Gysin class of the Koszul construction pair equally with the class of every smooth complete intersection of complementary dimension, hence are equal whenever those classes span, as they do for a subvariety of $\PP^n$ in every codimension, and the transverse base change $i^*j_*=(j_H)_*i_Y^*$ follows; step [](#s9){.pf-ref} adds that the base change holds on the top two Hodge degrees of $Y$ for any $X$, and hence on all of it when $Y$ is a curve, where the test classes are in $H^0$ and lift. Every assertion of the exercise is therefore a theorem about the one trace fixed by (N) and (C).

:::

:::

:::

::: {.remark title="The trace and the constant"}
As printed, the exercise names no normalization of the trace, and the numerical assertions of (b) and (d) need one. The passages are these.

III.7.1(a) is the assertion $H^n(X,\omega_X)\cong k$ for $X=\PP^n_k$, and it continues "Fix one such isomorphism"; the isomorphism is a choice, so the trace $t$ it determines is defined only up to a nonzero scalar. III.7.2 (printed p. 241) makes the trace part of the data: a dualizing sheaf is a *pair* $(\omega_X^\circ,t)$, uniqueness is uniqueness of the pair, and replacing $t$ by $ct$ gives a different pair representing the same functor. Corollary III.7.12 (printed p. 246) then says only that for $X$ projective and nonsingular $\omega_X^\circ$ is *isomorphic* to $\omega_X$; it does not normalize the isomorphism. Remark III.7.14 (printed p. 247) states the position: "even for a nonsingular projective variety $X$, we don't have much information about the trace map $t:H^n(X,\omega)\to k$. We know only that it exists."

A canonical normalization does exist, and the statement carries it: the trace is fixed by the point comparison (C), which singles out one trace because $H^n(X,\Omega_X^n)$ is one-dimensional and $\gamma^{0,0}_{Q/X}(1)\ne0$. This is the trace constructed from residues by Lipman (Residue Theorem (0.6), printed pp. 24--25), so the normalization is realized and not merely imposed. The other side, part (d), is canonical without any convention: Appendix A defines the Chern classes in the Chow ring $A(X)$, with the normalization C1 (printed p. 430), "If $\mathcal E\cong\mathcal L(D)$ for a divisor $D$, $c_t(\mathcal E)=1+Dt$", so $c_1$ of a line bundle is the class of its divisor with no scalar freedom. Part (a) uses (N) alone, with $Y=P$ a closed point; part (b) uses the class of a linear subspace from step [](#s3){.pf-ref} and the divisor formula of step [](#s2){.pf-ref} iterated along the hyperplane sections of $Y$; part (d) is the class form of step [](#s2){.pf-ref}.
:::

::: {.remark title="Published solutions"}
Parts (a) and (c) are published with complete arguments.  For (a): Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 3.7.4(a), printed p. 75, the two-line argument through $H^0(X,\OO_X)\cong H^0(P,\OO_P)\cong k$; Dongryul Kim, Exercise 3.7.4(a), PDF p. 170, the same argument as the Yoneda pairing evaluated at $1$; and Math StackExchange 1794757, answer by the account S.M. (2016-05-22), which supplies what the other two leave implicit, that $t_P(1)$ can be any element of $k^*$ and that $t_P(1)=1$ is the normalization the answer needs.  For (c): Yang, Solution 3.7.4(c), printed p. 75, and Kim, Exercise 3.7.4(c), PDF p. 170, both verify $d\log(fg)=d\log(f)+d\log(g)$; Kim alone cites Exercise III.4.5 for $\Pic X=H^1(X,\OO_X^*)$, and the citation is the book's own in its statement of III.7.4(c).

Parts (b) and (d) rest on the residue formula of step [](#s2){.pf-ref}, which is the residue theorem of Lipman's Astérisque 117 in the form needed here: (0.6)(a) and (0.6)(d) (printed pp. 24--25) identify the trace with the sum of the residues at the closed points, and the local computation at a point of the divisor identifies the residue of the $d\log$ class with that of the restricted class. In characteristic zero the same identity has a second proof, in the Stacks Project's verification that de Rham cohomology is a Weil cohomology theory: Axiom (A9) of Section 50.22, printed pp. 4267--4268, is the commutativity of the square joining restriction $H^{2d-2}_{dR}(X/k)\to H^{2d-2}_{dR}(Y/k)$, cup product with $c_1^{dR}(\mathcal O_X(Y))$, and the two traces $\lambda_X,\lambda_Y$, which for $\nu\in H^{d-1}(X,\Omega^{d-1})$ is the formula of step [](#s2){.pf-ref}. Its proof uses that the kernel of restriction is killed by $c_1^{dR}(\mathcal O_X(Y))$ (Lemma 50.15.6, printed p. 4240), reduces to the one class $c_1^{dR}(L)^{d-1}$ for ample $L$, where $H^{2d-2}_{dR}(Y/k)$ is one-dimensional by Poincaré duality for $Y$, and closes with the cycle identity $(Y\to X)_*(c_1(\restrictionof{L}{Y})^{d-1}\cap[Y])=c_1(\mathcal O_X(Y))\cap c_1(L)^{d-1}\cap[X]$. That section works over a field of characteristic $0$ (printed p. 4265), so the residue proof remains the one that holds in every characteristic. Yang's (b) cuts $Y$ down to its $\deg Y$ points by a general linear subspace, computes the factor there, and closes with the identification that carries the count back to $X$; step [](#s4){.pf-ref} carries that argument out, and the transfer his proof asserts is supplied there by pairing the class of the linear subspace, which step [](#s3){.pf-ref} computes, with the class of $Y$, which step [](#s2){.pf-ref} evaluates on the points. His (b) reads: cut $Y$ down to its $\deg Y$ points by a general linear subspace, which he writes as "a hyperplane $H$ of dimension $n-p$" where the dimension that leaves points is $p$, as $L\cong\PP^p$ of step [](#s4){.pf-ref}; compute the factor there; and then assert, of the morphism $k\cong H^p(H,\Omega_H^p)\cong H^p(X,\Omega_X^p)\cong k$, that it "is just identity from the proof in 3.7.3", a citation to a different identification. His (d) writes $c(\mathcal L_Y)$ as a Čech cocycle and evaluates it in homogeneous coordinates by $\sum f_ix_k\,\partial f_i/\partial x_k=d$, which uses Euler's formula and so treats $X=\PP^n$ only.
:::
