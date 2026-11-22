---
schema: qual/card@1
id: P-AGH525INVARIANTE
kind: problem
title: Which values of the invariant $e$ occur for ruled surfaces over a curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.5, the retained Egbert companion argument for all four
    parts, and the surrounding ruled-surface normalization conventions. The
    proof below replaces the companion's elementary-transform construction in
    (a) by explicit nonsplit normalized extensions. In (b) it makes precise
    the Serre-dual pullback criterion behind the subspaces L_E. Part (c) uses
    the intended incidence variety in P H^1(O_C(-D)); its dimension is at most
    2d-3, strictly below g+d-2 when d<=g. For (d), both the printed exercise
    note and the retained companion cite Nagata's general theorem e>=-g.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.2,
    exercise 2.5, printed page 384, with the printed hint to the proof of (2.15)
    for part (b) and the printed Note for part (d). Checked every step of the
    card: Serre duality in steps s1 and s10; nonspeciality of K+D and of K+D-E
    from degree > 2g-2 for the Riemann-Roch counts of s10 and s11; the pullback
    square of s6 is the identification used in the book's proof of 2.15, and the
    projectivised image of multiplication by the canonical section of O(F) is
    |K+D-F|+F; the incidence variety of s12 sits in Sym^{d-1}C x P(V^*), so its
    dimension is at most 2d-3 against dim P(V^*) = g+d-2, and both the dimension
    and the properness of the image were checked. Searched outside the twelve
    retained sets: Algebraic Geometry II, National Taiwan University, 2020
    Spring, Chapter V homework (tmp/sources/ntu-ag2-chapter5.pdf), which has no entry for Exercise 5 of
    section 2; Yang Pi-Yeh, Hartshorne Solutions, exercise 5.2.5, printed p. 103
    (tmp/sources/lfwin-hartshorne-solutions.pdf), which treats all four parts
    and whose (a) infers a nonzero section from nonnegative degree, an inference
    that fails for e >= g-1, so (a) is not a complete published proof; Egbert,
    PDF pp. 263-264, proves (b) and cites Fuentes-Pedreira and Maruyama for (a)
    and (c). Not checked: Nagata's theorem quoted in step s15 is not in
    tmp/sources, so part (d) rests on the printed Note alone.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes and Pedreira (arXiv:math/0006204v3) on 2026-11-16. Its Theorem
    3.2, printed p. 15, restates the book's Theorem V.2.12 with the sharper lower
    bound: a decomposable normalized bundle forces e at least zero, and an
    indecomposable one gives -g <= e <= 2g-2, where the book's own proof reaches
    only e >= -2g and sends the stronger restriction to its Exercise 2.5. Its proof is the citation "See [8], V, 2.12 and [15]", so it
    adds no argument of its own and does not reach part (a)'s existence statement
    for every e in the interval from 0 to 2g-2, nor part (c)'s range from -g to
    below zero. The lower bound is Nagata's, cited as the printed Note, as the
    paper's reference [15] and in its introduction, where it says the theorem of
    Segre that e >= -g was proved by Nagata in [15]; that reference is M. Nagata,
    "On self-intersection number of a section on a ruled surface", Nagoya Math.
    J. 37 (1970), 191-196, which is also Hartshorne's own reference [8] for the
    Note, and it is not readable from here. Math StackExchange question 4398506,
    saved as tmp/sources/mse-4398506-hart77-v25-linear-system-notation.md,
    concerns only the notation of part (b). No complete published argument for
    (a) or (c) was located; steps s1 to s3 and s10 to s12 remain the card's.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes--Pedreira's Theorem 4.12(4), printed pp. 31--32, which Egbert
    cites for part (a), and Nagata's coordinates for part (d), on 2026-11-16.
    Theorem 4.12(4): for a decomposable geometrically ruled surface, an
    elementary transformation at a point x outside both X_0 and X_1, over a point
    P of the base that is a base point of -e, produces an indecomposable surface
    with e' = e - 1 and minimum self-intersection curve X_0'. That is the paper's
    only construction of an indecomposable ruled surface, and it moves the
    invariant down by one from a decomposable surface rather than producing every
    value in 0 <= e <= 2g-2 from one statement; Egbert's citation of it for part
    (a) is therefore a pointer to one step of a construction, not an argument for
    the exercise. The lower bound used everywhere above is e >= -g, not -2g: the
    paper's Theorem 3.2(2), printed p. 15, gives -g <= e <= 2g-2 for an
    indecomposable normalized bundle and cites Hartshorne V.2.12 and its own
    reference [15], and its introduction attributes the theorem e >= -g to Segre
    and its proof to Nagata in [15]. Reference [15] is M. Nagata, "On
    self-intersection number of a section on a ruled surface", Nagoya Math. J. 37
    (1970), 191-196, the same paper Hartshorne's Note cites as his [8]. Nagata's
    statement itself was not read: Project Euclid serves an automated-access check
    for its PDF and Cambridge Core holds the article for subscribers, so part (d)
    still rests on the printed Note, on the paper's Theorem 3.2(2) and on that
    introduction, and it is listed open in COMPLAINTS for that reason. Not
    checked: whether Theorem 4.12(4) iterates, since its hypothesis asks for a
    decomposable surface and its conclusion is an indecomposable one.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read Theorem 4.12(4) against its proof in the text version of Fuentes and
    Pedreira on 2026-11-16 and corrected the earlier reading of it, and made step
    s15 say what it is. That theorem does not need to be iterated: applied once
    to the decomposable surface with invariant e+1 it returns an indecomposable
    surface with invariant (e+1)-1 = e, and the decomposable surfaces of every
    invariant e >= 0 exist by the book's Theorem 2.12(a) and by the paper's own
    Theorem 3.2(1), so one application reaches every 0 <= e <= 2g-2. What the
    theorem asks for and the paper does not construct is the point P of the base
    that is a base point of the linear system of -me; it exists whenever h^0(-me) = 1, the system
    then having the single member -me whose support is its base locus, and in
    general it is a condition on the divisor class. The events above say that the
    theorem is "one step of a construction" and this card's remark said the same;
    both now say that one application suffices given such a P, and the card does
    not claim part (a) closed on the theorem. Step s15 is now what it should have
    been: part (d) is the case g = 2 of the printed Note and of Nagata's paper
    behind it, nothing in tmp/sources proves it, and the book's own argument in
    Theorem 2.12 reaches only e >= -2g, that is e >= -4 at g = 2, the dimension
    count of step s12 covering d <= g only. The events above and the earlier
    step said nothing false about the bound itself but the qed claimed part (d)
    proved, which it is not.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcribed all four parts on 2026-11-16 from sources read in their text
    versions, and re-read the printed exercise at Hartshorne, Algebraic
    Geometry (1977), V.2, exercise 2.5, printed p. 384 (PDF p. 399), with its
    hint and its Note. (a) is Gunning, Lectures on vector bundles over Riemann
    surfaces, Theorem 13, printed pp. 71-74, which identifies extension classes
    with a first cohomology group and the split extension with the zero class,
    and Theorem 14, printed pp. 87-90, which parametrizes the indecomposable
    bundles with a given subbundle and determinant by the points of a projective
    space; with phi = O and xi of degree -e the space is P H^1(L^{-1}), nonzero
    by Serre duality once an effective A of degree 2g-2-e is chosen, which is
    the duality half of the book's own proof of Theorem 2.12, printed p. 376.
    The normalization argument of steps s2 and s3 is Example 2.11.6, printed
    p. 375, whose exceptional case M = L(-P) is shown on the card not to arise
    when deg L is at most 0. (b) is Lange-Narasimhan Proposition 1.1, printed
    p. 57, and Lemma 2.3, printed pp. 58-59, whose displayed criterion is the
    kernel of the canonical map H^0(K tensor L)^* to H^0(K tensor L(-D))^*, in
    both directions; the book's proof of Theorem 2.15, printed pp. 377-379,
    uses the normalized implies injective half. Pages were established from the
    PDFs' printed folios, printed page = PDF page + 53 for Lange-Narasimhan.
    (c) is their Corollary 1.2, printed p. 58, applied to line bundles of
    degrees d and 2d with d = -e, so that the extension's subbundle has degree
    d and its twist by the inverse of that subbundle is normalized with
    determinant of degree d; the genus one case e = -1 is Example 2.11.6 and
    Theorem 2.15, printed pp. 375 and 377-378. (d) is Lange, Higher secant
    varieties of curves and the theorem of Nagata on ruled surfaces, §1 Theorem,
    printed p. 266, and §2 Theorem s(E) at most g, printed pp. 267-268, with
    s(E) = c_1(E) - 2 max c_1(L), which for a normalized bundle is
    deg det = -e, giving e at least -g and hence e at least -2 at g = 2. Read
    check: the paper's proof begins by reducing to extensions with quotient of
    degree d > 3 and does not spell the reduction out; its §1 needs only d at
    least 2 when g is at least 2. Not checked: Nagata's own paper, still behind
    an automated-access check; nothing on the card now rests on it.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the card against its sources again on 2026-11-16, after the event
    above of the same date. Four corrections. Gunning's Theorem 13 is now quoted
    with his convention: phi_1 is the subbundle and phi_2 the quotient, and the
    classes lie in H^1(phi_1 phi_2^{-1}), which for the extension 0 to O to E to
    L to 0 is H^1(L^{-1}) directly, not H^1(L) as the previous wording had it.
    Part (b) no longer cites Lemma 2.3: that lemma characterizes a degree-zero
    line bundle M, other than O, being a maximal subbundle of an E with
    s(E) = d, and it is not the criterion of (b); Proposition 1.1, printed
    p. 57, is, and it is now cited alone, with its standing hypothesis d at
    least 2 for g at least 2 of the paper's section 1, so that d = 1 and g = 1
    lie outside it. Step s3 now states the inclusion O = A tensor A^{-1} inside
    E tensor A^{-1} that carries a section of A to one of the twist. The
    hypotheses of the quoted statements are stated where they are used: Gunning
    works over a compact Riemann surface, Lange and Narasimhan over an
    algebraically closed field of characteristic zero (their introduction), and
    part (d)'s paper over an algebraically closed field of arbitrary
    characteristic. Part (d) is now stated as proved: the text version's OCR
    reads "d > 3" in the paper's reduction, while the scan of printed p. 267
    reads "d >= 3", so the earlier claim that the reduction is unargued is
    withdrawn, the case s(E) at most 2 being trivial for g at least 2. The
    remark's step references are renumbered to the present steps, and it no
    longer carries machine paths or says which sources were not read. Not
    checked: (b) at d = 1 and at g = 1, and parts (a), (b), (c) in positive
    characteristic; nothing read supplies them, and the card does not claim
    them.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the card again on 2026-11-16 on the reader's report, after the
    event above of the same date, which is left as written. Four corrections.
    First, part (d) now rests on the statement of Lange's Theorem s(E) at most
    g, §2, printed pp. 267-268, and not on an argument of the card's: the case
    split the event above records, in which s(E) at most 2 settles g at least 2
    and the remaining case is reduced to a quotient of large degree, was the
    card's own and incomplete, since it did not say how a bundle with s(E) at
    least 3 acquires an exact sequence with quotient of degree at least 3. Step
    s11 now names the paper's reduction as stated and unargued and uses the
    Theorem as printed. The text version read here gives that reduction as a
    quotient of degree d > 3; the event above says the scan of printed p. 267
    reads d at least 3, and that sentence is left as written, nothing on the
    card now turning on which of the two the page prints, the PDF beside the
    text version having no text layer to re-read here. Second, steps s7 and s8
    are marked as the card's own: they run the pullback square and use no
    hypothesis on d or g, so they carry part (b) at d = 1 and at g = 1, the
    cases outside Proposition 1.1's section, and the qed and the remark now say
    which steps carry them. Third, the qed states the field and the range of
    each part, and claims nothing in positive characteristic for (a), (b) and
    (c). Fourth, the remark's sentence "step s11 now gives that bound ...
    instead" is change narration and is removed. Not checked: Nagata's paper,
    still unread, and nothing on the card rests on it.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected one number in step s11 on 2026-11-16 on the reader's second
    report, after the events above of the same date, which are left as written.
    The step quoted the paper's reduction as a quotient of degree d > 3, which
    is what the text version prints. Printed p. 267 reads "with a line bundle L
    of degree d greater than or equal to 3 on X", and the page was read here as
    an image rendered from the retained PDF: PDF page 6 of
    tmp/sources/lange-1984-higher-secant-varieties-nagata.pdf, which carries the
    running head LANGE, the Theorem s(E) at most g, the reduction and the folio
    267 at its foot, rendered at 150 dpi. So "d > 3" is an OCR error in the text
    version, and the step now quotes the page. Nothing else changes: the
    reduction is still stated and not argued, and part (d) still rests on the
    statement of the Theorem and not on the derivation that follows it, so the
    number decides nothing on the card. The PDF has no text layer, which is why
    the page was rendered rather than extracted.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Part of #160's row for this card: parts (a) and (b) are characteristic-free,
    and the card's qed and remark now say so instead of restricting them to
    characteristic zero. Checked on the steps: s1 uses Ext^1(L,O) = H^1(L^-1)
    and Serre duality H^1(K-A) = H^0(A)^*, both over any field; s2 the long
    exact sequence of the twist, s3 the splitting of an extension and the
    normalization degree bounds, s4 the invariant e = -deg det; s5 the duality
    between extension classes and H^0(K+D); s6 the pullback square and its
    dual multiplication by s_F; s7 the splitting followed by the inclusion;
    s8 the saturation of a subsheaf and an effective divisor T of degree a-1.
    None uses characteristic zero or the compact-Riemann-surface theory; the
    Gunning and Lange--Narasimhan statements are the standard forms of these
    identifications. Part (c) for g at least 2 still rests on Lange--
    Narasimhan's Corollary 1.2, printed p. 58, whose dimension count is stated
    over characteristic zero; the genus-one case is Hartshorne's Example
    2.11.6, printed p. 375, and is characteristic-free; part (d) is Lange's
    Theorem over an algebraically closed field of arbitrary characteristic,
    printed pp. 267--268. So (a), (b), (c) at g = 1 and (d) now stand over any
    algebraically closed field; (c) at g at least 2 remains characteristic
    zero. Not checked: no source outside those already on the card was read,
    and the steps were checked for their field hypotheses, not re-derived.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Part (c) at g at least 2 is now proved in every characteristic, and the card
    no longer depends on Lange--Narasimhan for it. The argument is the one the
    printed hint asks for: for d = -e with 1 <= d <= g and D of degree d,
    extension classes lie in V = H^1(O(-D)) of dimension g-1+d. For an
    effective E of degree d-1 the bad classes are ker(beta_E), of dimension
    d-1, since h^0(K+D-E) = g by Riemann--Roch at degree 2g-1. For d at least
    2 the bad pairs form a family of dimension (d-1)+(d-2) = 2d-3 in P V, and
    for d = 1 the only E is 0, whose kernel is zero; since 2d-3 < g-2+d for
    d <= g, a general class avoids every kernel. Part (b) makes the extension
    normalized, and a nonzero class makes it indecomposable because a splitting
    would realize O_C and O_C(D) as summands. Checked: the dimensions and the
    inequality, and that the determinant is O_C(D). The Lange--Narasimhan
    Corollary 1.2 route is kept in the remark as the characteristic-zero
    alternative. No statement changes.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Reader's finding on the event above, repaired here; that event is left as
    written. Its last inference is false: a non-split extension of O_C(D) by
    O_C need not be indecomposable. A standard non-split extension realises
    O_C(P) + O_C(Q) for distinct points P, Q of C: the diagonal O_C inside that
    sum has quotient of degree 2 and hence isomorphic to O_C(P+Q), so
    O_C(P) + O_C(Q) is a non-split extension of O_C(P+Q) by O_C, and at
    g = 3 with d = 2 it is normalized, h^0 being nonzero and h^0 of a twist by
    O_C(-R) vanishing unless R is P or Q. Non-splitting gives only that the
    bundle is not O_C + O_C(D), which is what the argument proves. Part (c)
    asks for a ruled surface of invariant e and not for an indecomposable
    bundle, that being the condition of part (a), so step s9 now states the
    non-splitting, and its use of Notation 2.8.1, printed p. 373, that the
    invariant of P(E) is minus the degree of the determinant for a normalized
    E, is unchanged. Checked in this pass, from the printed statements: that
    h^0(K_C+D-E) = g for an effective E of degree d-1, the degree 2g-1 being
    greater than 2g-2, so that ker(beta_E) has dimension d-1 inside the
    (g-1+d)-dimensional H^1(C,O_C(-D)); that the bad pairs form a family of
    dimension 2d-3, the effective divisors of degree d-1 forming a family of
    that dimension minus one and each kernel a linear subspace of dimension
    d-2 projectively; and the inequality 2d-3 < g-2+d for d <= g. Read for this
    pass: Hartshorne V.2, exercise 2.5 with Notation 2.8.1 and Proposition 2.8,
    printed pp. 372-377, in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    and step s6 of this card. Not checked: Lange and Narasimhan's Corollary
    1.2 beyond the statement and page the card records, and no printing of the
    book other than the text version.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Part (d) is proved on the card without the reduction that the issue names
    as unargued in Lange's paper, and the claim "and more generally e >= -g",
    which needed that reduction, leaves step s11's statement; the exercise's
    part (d), e >= -2 at g = 2, is unchanged. Lange's proof of his Theorem
    opens "For the proof we may suppose without loss of generality that there
    is an exact sequence 0 -> O_X -> E -> L -> 0 with a line bundle L of
    degree d > 3", and it does not argue that passage; the card previously
    used the Theorem as a black box. It now uses only the two results of the
    paper that are argued. Let E be normalized, so e = -deg det E and E sits
    in 0 -> O_C -> E -> L -> 0 with deg L = d = -e, the maximum of c_1 over
    sublinebundles being 0 by normalization. If d <= 2 there is nothing to
    prove; if d >= 3, |K_C tensor L| is very ample of degree 2+d >= 2g+1
    (Hartshorne, Corollary IV.3.2(b), printed p. 308) and embeds C
    nondegenerately in P^N with N = d; the nonzero extension class is a point
    of P^N and lies in Sec_n(C) for n = floor((2+d)/2) because the dimension
    theorem of Lange's §1, printed p. 266, gives dim Sec_n(C) =
    min(2n-1, N) = N; the Lemma of his §2, printed p. 267, then gives
    s(E) <= 2n-d <= 2 = g, against s(E) = d >= 3. So d <= 2. Read for this:
    the introduction (field statement), §1's Theorem and its Lemmas 1-3, and
    §2's Theorem, Lemma and their proofs, in
    tmp/sources/lange-1984-higher-secant-varieties-nagata.md, together with
    Hartshorne IV.3.2(b) at the printed page. Not checked: the printed paper,
    only the retained text version, whose scan carries no per-page markers, so
    the printed pages 266-267 are the ones the card's earlier events recorded;
    and no other proof of Nagata's bound was read.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The event above quoted the reduction that opens Lange's proof as "a line
    bundle L of degree d > 3". That was a regression: the card's event of
    2026-11-16 had already read printed p. 267 as an image and recorded that
    the page prints "d >= 3", the bar being lost in the text version's OCR, and
    the step it corrected quoted d >= 3; rewriting the step in this pass took
    the OCR reading instead. Re-read here from a rendering of the retained PDF
    at 220 dpi: PDF p. 6 of
    tmp/sources/lange-1984-higher-secant-varieties-nagata.pdf is printed
    p. 267 and carries §2's Theorem "s(E) <= g", the sentence "For the proof
    we may suppose without loss of generality that there is an exact sequence
    O -> O_X -> E -> L -> 0 (e) with a line bundle L of degree d >= 3 on X",
    and the Lemma "If (e) in Sec_n(X) for an n in N, then s(E) <= 2n-d";
    PDF p. 5 is printed p. 266 and carries the theorem of §1,
    dim Sec_n(X) = min(2n-1, N). The step now quotes d >= 3, and the separate
    sentence about a standing supposition d > 3 and the coverage of d = 3 is
    withdrawn, since the Lemma is stated for the same d >= 3 as the
    contradiction assumes. No mathematics changes: the proof assumes d >= 3
    and the Lemma applies there. Read for this: the same rendering at PDF
    pp. 5-6, and the field statement "an algebraically closed field of
    arbitrary characteristic" on printed p. 263. Not checked: any printing of
    the paper other than the retained PDF.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Two repairs. (i) Part (d) of the remark described Lange's reduction as
    one to a quotient of degree > 3; the printed source has d >= 3, which is the
    hypothesis step s11 assumes and states, and the remark now reads d >= 3. The
    events above record that the text version's "d > 3" is an OCR error and that the
    scan of the page reads d >= 3. (ii) No page locator remained in the rendered text
    of this card, so none was removed; the audit events above keep the pages they
    name, as the citation rule requires. Checked in this pass: the two occurrences of
    the reduction in the rendered text, at step s11 and in the remark, both of which
    now say d >= 3, and the absence of a page locator from that text. Not checked:
    any printing of Lange's paper, only the PDF retained in tmp/sources.
- event: source-checked
  by: claude
  date: 2026-11-22
  note: >-
    Published-solution pass for issue #160, on the transcription rule. The
    remark already recorded what each retained solution set does with
    V.2.5; the paragraph added in this pass states that no retained set
    proves all four parts, and names the sets that carry no Chapter V §2
    exercise. Read in this pass, at their own numbering: Yang Pi-Yeh,
    Solution 5.2.5, all four parts, whose (a) bounds h^0(omega_C tensor L) by
    nonnegativity of the degree, which does not give a section for e >= g-1,
    and whose (d) reads "all ker xi form the Grassmannian G^{d+1}_d ... so we
    have d <= 2(d-1)"; Egbert's entries 5.2.9 and 5.2.10, which give (c) as
    "This is given by 3.13 in Maruyama" and (d) as "By Theorem 1 in Nagata
    'Self-intersection number'", together with his entry on (b) and his
    citation of Fuentes--Pedreira's Theorem 4.12(4) for (a); the exercise list
    of the National Taiwan University Chapter V §2 homework, whose entries are
    exercises 1, 2, 3, 4 and 6, so that it has none for Exercise 5; and, for
    absence, Borcherds (through IV.1), Cais (through Chapter 4),
    Cutrone--Marshburn (Chapters 1 and 2), Ionita--Kumar (Chapter I), Kim
    (§2.4), Lomont, Okamoto (§II.9), Park (Chapter 4 and §V.5), Saglam--Chris (Chapter III),
    Sam (through IV.6), Stein (III.7), Troiani (Chapter II) and Reiser
    (IV.2.5). No statement and no proof step changed in this pass, and the
    card's own parts remain steps s7 and s8 of (b) and the avoidance count of
    step s9 of (c), as the preamble and those steps state. Not read in this
    pass: Gunning's Theorems 13 and 14, Lange and Narasimhan's Proposition
    1.1 and Lange's §1 and §2 beyond the statements the card quotes; and any
    printing of Hartshorne, only the text version in tmp/sources.
---

::: {.problem}
Let $C$ be a curve of genus $g \geqslant 1$.

(a) Show that for each $0 \leqslant e \leqslant 2 g-2$ there is a ruled surface $X$ over $C$ with invariant $e$, corresponding to an indecomposable $\mathcal{E}$.
Cf.
(2.12).

(b) Let $e<0$, let $D$ be any divisor of degree $d=-e$, and let $\xi \in H^1(\mathcal{L}(-D))$ be a nonzero element defining an extension
$$
0 \rightarrow \OO_C \rightarrow \mathcal{E} \rightarrow \mathcal{L}(D) \rightarrow 0 .
$$
Let $H \subseteq\linearsystem{D+K}$ be the sublinear system of codimension 1 defined by $\ker \xi$, where $\xi$ is considered as a linear functional on $H^0(\mathcal{L}(D+K))$.
For any effective divisor $E$ of degree $d-1$, let $L_E \subseteq\linearsystem{D+K}$ be the sublinear system $\linearsystem{D+K-E}+E$.
Show that $\mathcal{E}$ is normalized if and only if for each $E$ as above, $L_E \nsubseteq H$.
Cf.
proof of $(2.15)$.

(c) Now show that if $-g \leqslant e<0$, there exists a ruled surface $X$ over $C$ with invariant $e$.

Hint: For any given $D$ in (b), show that a suitable $\xi$ exists, using an argument similar to the proof of (II, 8.18).

(d) For $g=2$, show that $e \geqslant-2$ is also necessary for the existence of $X$.

Note.
It has been shown that $e \geqslant-g$ for any ruled surface (Nagata [8]).

:::

::: {.solution}
Recall that a rank-two bundle $\mathcal E$ on $C$ is normalized when
$$
H^0(C,\mathcal E)\ne0
$$
but $H^0(C,\mathcal E\tensor\mathcal M)=0$ for every invertible sheaf $\mathcal M$ of negative degree, Proposition 2.8, and that for such a bundle the invariant of $X=\PP(\mathcal E)$ is $e=-\deg\det\mathcal E$, Notation 2.8.1.

Part (a) is transcribed from Gunning, *Lectures on vector bundles over Riemann surfaces*, Theorem 13, and Theorem 14, together with the duality half of Hartshorne's proof of Theorem 2.12; part (b) from Proposition 1.1, of Lange and Narasimhan, *Maximal subbundles of rank two vector bundles on curves*, whose statement is the criterion that the printed "Cf. proof of (2.15)" points at, that is the proof of Theorem 2.15; part (c) from the card's avoidance argument for $g\ge2$, with Lange and Narasimhan's Corollary 1.2, as the characteristic-zero alternative, and Example 2.11.6, for genus one; part (d) from the dimension theorem of Lange, *Higher secant varieties of curves and the theorem of Nagata on ruled surfaces*, §1, and the Lemma of its §2, applied in the case $d=-e\ge3$, so that the unargued reduction that opens the proof of his §2 Theorem is not used. Lange and Narasimhan work over an algebraically closed field of characteristic zero and Gunning over a compact Riemann surface; where a quoted statement's hypotheses are narrower than the exercise's, the step that quotes it says so. The arguments of parts (a), (b), (c) and (d) use only $\Ext^1\cong H^1$, Serre duality, the pullback square, the dimension count of step $s9$ and the two results of Lange cited for (d), all of which hold over an algebraically closed field of any characteristic; so all four parts hold there.

::: pf

::: {.pf-step #s1}
Fix
$$
0\le e\le2g-2.
$$
There is an invertible sheaf $\mathcal L$ of degree $-e$ with
$$
\Ext^1_C(\mathcal L,\OO_C)\ne0 .
$$

::: pf-proof
Choose an effective divisor $A$ of degree $2g-2-e$ and put $\mathcal L=\OO_C(A-K_C)$; then $\deg\mathcal L=-e$ and
$$
\Ext^1_C(\mathcal L,\OO_C)\cong H^1(C,\mathcal L^{-1})=H^1\qty(C,\OO_C(K_C-A)),
$$
which is Theorem 13 of Gunning. In his notation an extension $0\to\OO(\varphi_1)\to\OO(\Phi)\to\OO(\varphi_2)\to0$ has $\varphi_1$ the subbundle and $\varphi_2$ the quotient, and its classes are the elements of $H^1(C,\OO(\varphi_1\varphi_2^{-1}))$; for $\varphi_1=\OO_C$ and $\varphi_2=\mathcal L$ that group is $H^1(C,\OO_C(\mathcal L^{-1}))$, the group of the extension above. Serre duality gives
$$
H^1\qty(C,\OO_C(K_C-A))^\vee\cong H^0(C,\OO_C(A)),
$$
which is nonzero because $A$ is effective. This is the duality step of the proof of Theorem 2.12, read in the other direction: there $H^1(\mathcal L^\vee)\ne0$ forces $\deg\mathcal L^\vee\le2g-2$, which for the present $\mathcal L$ is the inequality $e\le2g-2$.

:::

:::

::: {.pf-step #s2}
A nonzero class of step [](#s1){.pf-ref} defines a normalized extension
$$
0\longrightarrow\OO_C
\longrightarrow\mathcal E
\longrightarrow\mathcal L
\longrightarrow0 .
$$

::: pf-proof
The argument is that of Example 2.11.6. The inclusion of $\OO_C$ gives $H^0(C,\mathcal E)\ne0$. Let $\mathcal M$ have negative degree and tensor the sequence by it:
$$
0\longrightarrow\mathcal M
\longrightarrow\mathcal E\tensor\mathcal M
\longrightarrow\mathcal L\tensor\mathcal M
\longrightarrow0 .
$$
Both end terms have negative degree, $\deg\mathcal L\tensor\mathcal M=-e+\deg\mathcal M<0$ because $e\ge0$, so $H^0(\mathcal M)=H^0(\mathcal L\tensor\mathcal M)=0$ and the long exact sequence gives $H^0(C,\mathcal E\tensor\mathcal M)=0$. The exceptional case the book separates at $\mathcal M=\mathcal L(-P)$, where the end term is $\OO_C$ and the coboundary is the class $\xi$, does not arise here, since $\mathcal L\tensor\mathcal M\cong\OO_C$ forces $\deg\mathcal M=e\ge0$.

:::

:::

::: {.pf-step #s3}
The bundle $\mathcal E$ of step [](#s2){.pf-ref} is indecomposable.

::: pf-proof
Gunning, Theorem 13, attaches the split extension to the zero class, so a nonzero class gives a nonsplit sequence. Suppose then that $\mathcal E\cong\mathcal A\oplus\mathcal B$ with $\mathcal A,\mathcal B$ invertible. Since $H^0(C,\mathcal E)\ne0$, one summand, say $\mathcal A$, has a nonzero section and hence $\deg\mathcal A\ge0$; normalization bounds $\deg\mathcal A\le0$ because the inclusion $\OO_C=\mathcal A\tensor\mathcal A^{-1}\subseteq\mathcal E\tensor\mathcal A^{-1}$ carries a nonzero section of $\mathcal A$ to one of $\mathcal E\tensor\mathcal A^{-1}$, and $\deg\mathcal A^{-1}<0$. So $\mathcal A\cong\OO_C$ and $\mathcal B\cong\det\mathcal E\cong\mathcal L$. If $\mathcal L$ is not trivial then $H^0(C,\mathcal L)=0$, since $\deg\mathcal L=-e\le0$, so the injection $\OO_C\to\OO_C\oplus\mathcal L$ lands in the first summand and splits; if $\mathcal L\cong\OO_C$ it is a nonzero constant vector, and a constant change of basis splits it as well. Either way the extension splits, contradicting the choice of a nonzero class.

:::

:::

::: {.pf-step #s4}
For every $0\le e\le2g-2$ there is an indecomposable $\mathcal E$ with
$$
-\deg\det\mathcal E=e,
$$
so that $X=\PP(\mathcal E)$ is a ruled surface with invariant $e$. This proves part (a).

::: pf-proof
By step [](#s2){.pf-ref} the bundle is normalized, so the invariant of $\PP(\mathcal E)$ is $-\deg\det\mathcal E$ by Notation 2.8.1, and $\deg\det\mathcal E=\deg\mathcal L=-e$; step [](#s3){.pf-ref} gives indecomposability. Theorem 14 of Gunning, is the existence statement in this form: for line bundles $\varphi$ and $\xi$ with $c(\varphi)\ge\frac12c(\xi)$ and determinant $\xi$, the indecomposable bundles with subbundle $\varphi$ and determinant $\xi$ are parametrized by the points of $\PP H^1(C,\OO(\varphi^2\xi^{-1}))$, which for $\varphi=\OO_C$ and $\xi=\mathcal L$ is $\PP H^1(C,\mathcal L^{-1})$, nonempty by step [](#s1){.pf-ref}; the bundle produced there is the extension of step [](#s2){.pf-ref}, whose normalization and indecomposability are steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}
For part (b), the class $\xi$ of the extension
$$
0\longrightarrow\OO_C\longrightarrow\mathcal E\longrightarrow\OO_C(D)\longrightarrow0
$$
is a nonzero linear functional on $V=H^0(C,\OO_C(K_C+D))$, and the subsystem $H\subseteq\linearsystem{D+K}$ of codimension one is $\PP(\ker\xi)$.

::: pf-proof
The identification of extension classes with $H^1(C,\OO_C(-D))$ is Gunning, Theorem 13, and the duality $H^1(C,\OO_C(-D))^\vee\cong H^0(C,\OO_C(K_C+D))$ is Serre duality; that is the interpretation the exercise states, and the book's proof of Theorem 2.15 uses the class in exactly this form, as an element of $H^1(\mathcal L(-P-Q))$ dual to $H^0(\mathcal L(P+Q))$.

:::

:::

::: {.pf-step #s6}
For an effective divisor $F$ with $\deg F\le d-1$, pulling the extension back along $\OO_C(D-F)\hookrightarrow\OO_C(D)$ gives a class
$$
\beta_F(\xi)\in H^1(C,\OO_C(F-D)),
$$
and
$$
\boxed{\beta_F(\xi)=0\iff L_F\subseteq H},
\qquad
L_F=\linearsystem{K_C+D-F}+F.
$$

::: pf-proof
This is the criterion of Lange and Narasimhan, Proposition 1.1, in its two directions. The inclusion is multiplication by a section $s_F$ of $\OO_C(F)$, so under Serre duality the dual of $\beta_F$ is
$$
H^0(C,\OO_C(K_C+D-F))\xrightarrow{\cdot s_F}H^0(C,\OO_C(K_C+D)),
$$
whose projective image is $L_F$; hence the pullback splits exactly when $\xi$ annihilates that image, that is when $L_F\subseteq H$. Proposition 1.1 states them as the equivalence of $\mathrm{(i)}$ and $\mathrm{(ii)}$ for one extension $0\to\OO_X\to E\to L\to0$: the class lies in the span of an effective divisor $D$ exactly when $L(-D)$ is a subsheaf of $E$, which is the splitting of the pullback. Its §1 assumes $d\ge2$ when $g\ge2$ and a field of characteristic zero; the criterion as proved in steps [](#s7){.pf-ref} and [](#s8){.pf-ref} uses only the pullback square, so it is characteristic-free, and those steps also reach $d=1$ and $g=1$.

:::

:::

::: {.pf-step #s7}
If an effective divisor $E$ of degree $d-1$ satisfies $L_E\subseteq H$, then $\mathcal E$ is not normalized.

::: pf-proof
Step [](#s6){.pf-ref} gives $\beta_E(\xi)=0$, so the pullback
$$
0\longrightarrow\OO_C\longrightarrow\mathcal E_E\longrightarrow\OO_C(D-E)\longrightarrow0
$$
splits, and the splitting followed by $\mathcal E_E\to\mathcal E$ embeds $\OO_C(D-E)$ in $\mathcal E$; its inverse has degree $-1$, so a negative twist of $\mathcal E$ has a nonzero section. This is the implication the book uses in the proof of Theorem 2.15: normalization makes the map $\gamma$ injective, which is the statement that no $L_E$ lies in $H$. The step is the card's own: it runs the pullback square of step [](#s6){.pf-ref} and uses no hypothesis on $d$ or $g$, so it reaches $d=1$ and $g=1$, which the propositions quoted above exclude.

:::

:::

::: {.pf-step #s8}
Conversely, if $\mathcal E$ is not normalized, some effective divisor $E$ of degree $d-1$ satisfies $L_E\subseteq H$.

::: pf-proof
There is a line bundle $\mathcal M$ of negative degree and a nonzero morphism $\mathcal M^{-1}\to\mathcal E$; saturating its image gives a subbundle $\mathcal A\hookrightarrow\mathcal E$ of positive degree $a$. Its composite with the quotient $\mathcal E\to\OO_C(D)$ is nonzero, since a zero composite would factor $\mathcal A$ through $\OO_C$, whereas a nonzero section of $\mathcal A^{-1}$ would impose a negative twist on $\mathcal E$. A nonzero map $\mathcal A\to\OO_C(D)$ has an effective zero divisor $F$, so $\mathcal A\cong\OO_C(D-F)$ with $\deg F=d-a\le d-1$, and the inclusion already lifts to $\mathcal E$, so the pullback splits and $L_F\subseteq H$ by step [](#s6){.pf-ref}. Choosing an effective $T$ of degree $a-1$ and setting $E=F+T$ gives $\deg E=d-1$ and $L_E\subseteq L_F\subseteq H$. This is the converse implication of Proposition 1.1 of Lange and Narasimhan. The step is the card's own, as in step [](#s7){.pf-ref}: it runs the pullback square of step [](#s6){.pf-ref} and uses no hypothesis on $d$ or $g$, so it reaches the cases $d=1$ and $g=1$ that lie outside the proposition's section. Steps [](#s7){.pf-ref} and [](#s8){.pf-ref} prove part (b).

:::

:::

::: {.pf-step #s9}
If $-g\le e<0$ and $g\ge2$, there is a ruled surface over $C$ with invariant $e$. This is part (c) for $g\ge2$.

::: pf-proof
Put $d=-e$, so $1\le d\le g$, and fix a divisor $D$ of degree $d$. An extension
$$
0\longrightarrow\OO_C\longrightarrow\mathcal E\longrightarrow\OO_C(D)\longrightarrow0
$$
is determined by its class in $V=H^1(C,\OO_C(-D))$, a vector space of dimension $g-1+d$ by Riemann--Roch and Serre duality. For an effective divisor $E$ of degree $d-1$, the classes for which $L_E\subseteq H$ are the kernel of the pullback map $\beta_E\colon V\to H^1(C,\OO_C(-E))$ of step [](#s6){.pf-ref}, a linear subspace. Since $\deg(K_C+D-E)=2g-1$, Riemann--Roch gives $h^0(K_C+D-E)=g$; hence $\ker\beta_E$ has dimension $(g-1+d)-g=d-1$. For $d\ge2$ the pairs $(E,\xi)$ with $\xi\in\ker\beta_E$ form a family of dimension $(d-1)+(d-2)=2d-3$ in $\PP V$, and for $d=1$ the only effective $E$ is $0$, whose kernel is zero. Since $2d-3<g-2+d=\dim\PP V$ for $d\le g$, a general $\xi$ lies in no such kernel. By part (b) the extension is normalized, and a nonzero $\xi$ means that the extension does not split, that is $\mathcal E\not\cong\OO_C\oplus\OO_C(D)$. Its determinant is $\OO_C(D)$ of degree $d$, so $\PP(\mathcal E)$ has invariant $-d=e$ by Notation 2.8.1. Part (c) asks for the surface and its invariant, not for an indecomposable $\mathcal E$, which is the condition of part (a); non-splitting of the extension is what the argument gives, and it is all that the invariant needs. This is the avoidance argument the printed hint asks for; the genus-one case is step [](#s10){.pf-ref}.

:::

:::

::: {.pf-step #s10}
If $g=1$ and $-g\le e<0$, that is $e=-1$, there is a ruled surface over $C$ with invariant $e$.

::: pf-proof
This is Example 2.11.6, which constructs $\mathcal E$ as an extension $0\to\OO_C\to\mathcal E\to\mathcal L(P)\to0$ with $\xi\ne0$, shows it normalized by the long exact sequence of the twisted sequence, and concludes that $\PP(\mathcal E)$ is an elliptic ruled surface with $e=-1$; the proof of Theorem 2.15, repeats the construction and shows that it is the only one. Steps [](#s9){.pf-ref} and [](#s10){.pf-ref} prove part (c).

:::

:::

::: {.pf-step #s11}
For $g=2$ the inequality
$$
e\ge-2
$$
holds for every ruled surface over $C$. This is part (d).

::: pf-proof
Let $\mathcal E$ be the normalized bundle of $X$, so that $e=-\deg\det\mathcal E$ by Notation 2.8.1. A nonzero section of $\mathcal E$ spans a sub-line-bundle $\OO_C\subseteq\mathcal E$, and the quotient is a line bundle
$$
0\longrightarrow\OO_C\longrightarrow\mathcal E\longrightarrow\mathcal L\longrightarrow0,
\qquad
\deg\mathcal L=\deg\det\mathcal E=-e=:d,
$$
because $\det\mathcal E=\det\OO_C\otimes\det\mathcal L=\mathcal L$. The maximum of $c_1$ over the sublinebundles of $\mathcal E$ is $0$: $\OO_C$ has degree $0$, and a sublinebundle $\mathcal M$ of positive degree would give a nonzero section of $\mathcal E\otimes\mathcal M^{-1}$ with $\deg\mathcal M^{-1}<0$, against normalization; hence
$$
s(\mathcal E)=c_1(\mathcal E)-2\max c_1=\deg\det\mathcal E=d.
$$
If $d\le2$ there is nothing to prove, so suppose $d\ge3$. Then $\deg(K_C\otimes\mathcal L)=2g-2+d=2+d\ge5=2g+1$, so $\linearsystem{K_C\otimes\mathcal L}$ is very ample by Hartshorne, Corollary IV.3.2(b), and embeds $C$ nondegenerately in $\PP^N$ with $N=h^0(K_C\otimes\mathcal L)-1=(2+d)-2+1=d$ by Riemann--Roch and Serre duality. Since $d>0$, the extension does not split, or $\mathcal L$ would be a sublinebundle of $\mathcal E$ of positive degree; so its class $\xi\in H^1(C,\mathcal L^{-1})$ is nonzero, and by Serre duality it is a nonzero element of $H^0(C,K_C\otimes\mathcal L)^\vee$, that is a point of the dual $\PP^N$, which we identify with $\PP^N$.

Let $n=\lfloor (2+d)/2\rfloor$. By the theorem of Lange, §1, $\dim\mathrm{Sec}_n(C)=\min(2n-1,N)$ for a nondegenerate curve in $\PP^N$; here $2n-1\ge N=d$, since $n=(d+2)/2$ gives $2n-1=d+1$ for $d$ even and $n=(d+1)/2$ gives $2n-1=d$ for $d$ odd, so $\mathrm{Sec}_n(C)=\PP^N$ and $\xi\in\mathrm{Sec}_n(C)$.

By the Lemma of Lange, §2, if the class of an extension lies in $\mathrm{Sec}_n(C)$ then $s(\mathcal E)\le2n-d$. His proof, which he repeats there, is this: $\xi\in\mathrm{Sec}_n(C)$ means that there is an effective divisor $D$ of degree $n$ with $\xi$ in the kernel of $H^0(C,K_C\otimes\mathcal L)^\vee\to H^0(C,K_C\otimes\mathcal L(-D))^\vee$, that is, by Serre duality, in the kernel of $H^1(C,\mathcal L^{-1})\to H^1(C,\mathcal M^{-1})$ with $\mathcal M=\mathcal L(-D)$; then $\mathcal M\subseteq\mathcal E$ is a sublinebundle of degree $d-n$, so
$$
s(\mathcal E)=c_1(\mathcal E)-2\max c_1\le d-2(d-n)=2n-d.
$$
Hence
$$
d=s(\mathcal E)\le2n-d\le d+2-d=2=g,
$$
the middle inequality because $2n\le2+d$, a contradiction with $d\ge3$. So $d\le2$, that is $e=-d\ge-2$.

The Lemma is stated in the paper after that reduction, so for $d\ge3$, which is the case here; no separate argument for $d=3$ is needed.

The proof of the theorem in Lange's paper opens by supposing without loss of generality that $\mathcal E$ sits in an extension with quotient of degree $d\ge3$, a reduction it states and does not argue; that reduction is not used here. What is used is the part of his proof that is argued, the dimension theorem of §1 and the Lemma of §2, stated for $d\ge3$ as the paper's reduction gives it, over the algebraically closed field of arbitrary characteristic that the paper names in its introduction, and the hypothesis $d\ge3$ of the contradiction is exactly the case in which the reduction would have been needed.
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (a) over an algebraically closed field of any characteristic: the construction uses only $\Ext^1\cong H^1$ and Serre duality, and Gunning's Theorems 13 and 14 state the same identifications over a compact Riemann surface. Steps [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove part (b) over an algebraically closed field of any characteristic: [](#s5){.pf-ref} and [](#s6){.pf-ref} identify the extension class by Serre duality, and [](#s7){.pf-ref} and [](#s8){.pf-ref} are the card's own and run the pullback square, reaching also the cases $d=1$ and $g=1$ that the proposition's hypotheses exclude. Steps [](#s9){.pf-ref} and [](#s10){.pf-ref} prove part (c) for $g\ge2$ by the avoidance argument and for $g=1$ from Example 2.11.6, both characteristic-free. Step [](#s11){.pf-ref} proves part (d) at $g=2$ from the dimension theorem of Lange's §1 and the Lemma of his §2, both argued in the paper and stated there over an algebraically closed field of arbitrary characteristic, in the case $d=-e\ge3$, without the reduction that his §2 Theorem assumes without proof.

:::

:::

:::

::: {.remark title="Published solution"}
(a) Gunning's Theorem 13, identifies the extensions of one line bundle by another with a first cohomology group, and his Theorem 14, parametrizes the indecomposable bundles with a given subbundle $\varphi$ and determinant $\xi$ by the points of $\PP H^1(C,\OO(\varphi^2\xi^{-1}))$; with $\varphi=\OO_C$ and $\xi$ of degree $-e$ that space is $\PP H^1(C,\mathcal L^{-1})$, nonempty by Serre duality, which is steps [](#s1){.pf-ref} to [](#s4){.pf-ref}. Gunning works over a compact Riemann surface; the steps use only the characteristic-free identifications $\Ext^1\cong H^1$ and Serre duality, so they give part (a) over any algebraically closed field.

(b) Lange and Narasimhan, Proposition 1.1, is the criterion the printed "Cf. proof of (2.15)" points at, and the book's proof of Theorem 2.15, runs one direction of it: normalization makes the map $\gamma$ injective. Their Proposition 1.1 assumes $d\ge2$ when $g\ge2$, so the cases $d=1$ and $g=1$ lie outside it, and their field is an algebraically closed field of characteristic zero; the two directions in steps [](#s7){.pf-ref} and [](#s8){.pf-ref} use only the pullback square, so part (b) holds over any algebraically closed field, and they carry those two cases.

(c) Step [](#s9){.pf-ref} proves the existence for $g\ge2$ in every characteristic by the avoidance argument the hint names: the bad classes for the effective divisors $E$ of degree $d-1$ form a family of dimension $2d-3$ in $\PP H^1(\OO(-D))$, which has dimension $g-2+d$, and $2d-3<g-2+d$ because $d\le g$; a general class is therefore normalized and gives a non-split extension, the invariant being $-\deg\det=-d=e$. Lange and Narasimhan's Corollary 1.2, gives the same existence for $g\ge2$ over characteristic zero by the secant-variety count $\dim\mathrm{Sec}_{s-2}(X)\le2s-3<g+s-2=\dim\PP$.

(d) Lange, *Higher secant varieties of curves and the theorem of Nagata on ruled surfaces*: the dimension theorem of §1, that $\dim\mathrm{Sec}_n(C)=\min(2n-1,N)$ for a nondegenerate curve in $\PP^N$, and the Lemma of §2, that a class of an extension lying in $\mathrm{Sec}_n(C)$ forces $s(E)\le2n-d$; the paper states an algebraically closed field of arbitrary characteristic. For a normalized bundle $s(E)=\deg\det E=-e$, and with $d=-e\ge3$ one gets $d\le2$, so $e\ge-2$ at $g=2$. That is the bound the printed Note attributes to Nagata [8]. The reduction to a quotient of degree $d\ge3$ that opens the proof of his Theorem is stated there and not argued, and step [](#s11){.pf-ref} does not use it.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.5. Part (b) he proves: with $\xi\in H^1(\mathcal L(-D))$ the class of the extension and $\gamma:H^0(\mathcal L(D+K-E))\to H^1(\mathcal L(-E))$, injectivity of $\gamma$ is equivalent to $\mathcal E$ being normalized, and he runs the commutative square with $H^0(\OO_C)\to H^1(\mathcal L(-D))\to H^1(\mathcal L(-E))$ in both directions. For (a) he writes "This will get us all invariants for this problem with the help of thm V.2.12. This is F,P thm 4.12.4", a citation to Fuentes--Pedreira's Theorem 4.12(4), which takes a decomposable surface and an elementary transformation at a point outside $X_0$ and $X_1$ over a base point $P$ of $-\mfe$ and returns an indecomposable surface with invariant $e-1$; one application to the decomposable surface of invariant $e+1$ gives an indecomposable surface of invariant $e$, the base point $P$ being the one condition the theorem asks for. For (c) he writes "By proof of (a), I only need to find one with invariant $-g$ ... This is given by 3.13 in Maruyama", a citation to Maruyama. Part (d) he answers "By Theorem 1 in Nagata 'Self-intersection number'", which is the source of the printed Note, and step [](#s11){.pf-ref} gives the $g=2$ case from the dimension theorem of Lange's §1 and the Lemma of his §2.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.5, treats all four parts. For (a) it argues that $\Ext^1(\mathcal L,\OO_C)\cong H^0(C,\omega_C\tensor\mathcal L)$ "and $\deg\omega_C\tensor\mathcal L=2g-2-e\ge0$, hence $\Ext^1$ is nontrivial": a line bundle of nonnegative degree on a curve of genus $g$ need not have a section, and the correct bound is $h^0\ge\deg-g+1=g-1-e$, which is negative for $e\ge g-1$. Step [](#s1){.pf-ref} avoids the issue by taking $\mathcal L=\OO_C(A-K_C)$ with $A$ effective, so that $H^0(\OO_C(A))\ne0$ directly. Its (b) is the square of step [](#s6){.pf-ref} written out; its (c) is the dimension count of step [](#s9){.pf-ref}; its (d) is garbled ("all $\ker\xi$ form the Grassmannian $G^{d+1}_d$, which has dimension $d$ ... so we have $d\le2(d-1)$").

Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework solutions, has no entry for Exercise 5 of §2.

The remaining retained sets carry no Chapter V §2 exercise: Borcherds, Cais, Cutrone--Marshburn,
Ionita--Kumar, Kim, Lomont, Okamoto, Park, Saglam--Chris, Sam, Stein, Troiani and Reiser. No retained solution
set proves all four parts: Egbert's entry proves (b) and cites other sources for (a), (c) and (d),
and Yang Pi-Yeh's treats all four, with the defects recorded above in (a) and (d). The proof on the
card is therefore its own arrangement, and it rests on the numbered statements it names part by part:
Gunning's Theorem 13 and Theorem 14 and Hartshorne's Proposition 2.8, Notation 2.8.1, Theorem 2.12
and Example 2.11.6 for (a) and (c); Lange and Narasimhan's Proposition 1.1, in the two directions
steps [](#s7){.pf-ref} and [](#s8){.pf-ref} supply outside its hypotheses; Lange's §1 dimension
theorem and §2 Lemma for (d); and Riemann--Roch and Serre duality throughout. The parts the card
supplies itself are steps [](#s7){.pf-ref} and [](#s8){.pf-ref} of (b) and the avoidance count of step
[](#s9){.pf-ref} of (c).
:::
