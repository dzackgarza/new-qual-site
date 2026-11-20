---
schema: qual/card@1
id: P-AGH5215FROBENIUSRULED
kind: problem
title: A ruled surface in characteristic 3 with a nonample divisor satisfying the numerical criterion
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.2.15, the retained Egbert companion calculation, the
    earlier characteristic-three quartic computation, the purely inseparable
    curve theorem, and the ruled-surface intersection formulas. Parts (a) and
    (b) admit a direct cohomological proof. In part (c), Frobenius pullback of
    the extension splits and produces an integral degree-three purely
    inseparable multisection of class 3C_0-3f. The printed adjective
    "nonsingular" is incompatible with adjunction: this class has arithmetic
    genus 4, while its normalization is the genus-3 quartic C. The proof below
    records and proves the corrected statement.
- event: source-corrected
  by: chatgpt
  date: 2026-09-19
  note: >-
    Part (c)'s "nonsingular curve" is corrected by an erratum to "integral
    curve whose normalization is C"; adjunction gives p_a(Y)=4 whereas the
    normalization has genus 3.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Hartshorne V.2.15(c) asks for a nonsingular curve Y = 3C_0-3f; adjunction gives p_a(Y)=4 while its normalization C has genus 3. The statement now asks for an integral curve of that class with normalization C.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.2,
    exercise 2.15, printed page 385. Rechecked the adjunction count recorded in
    the erratum: with e = -1 from deg det E = deg P = 1 and K = -2C_0+5f on a
    ruled surface over a genus-three curve, Y = 3C_0-3f has Y^2 = -9 and
    Y.K = 15, so p_a(Y) = 4, while the normalization is C of genus 3, so no
    nonsingular Y of that class exists and the printed adjective cannot hold.
    Checked the Cech computation of s3: H^2(P^2,O(-4)) has the three monomials
    x^{-2}y^{-1}z^{-1}, x^{-1}y^{-2}z^{-1}, x^{-1}y^{-1}z^{-2} as a basis, and
    all six monomials of F^2 = (x^3y+y^3z+z^3x)^2 give a nonnegative exponent
    after multiplication by the cube of the first. Checked the dimension count
    of s4 and s5, the normalization of E in s6 including the case
    M = O_C(-P), the splitting of s7, and the class computation of s9 which
    leaves (m,a,b) = (1,3,-3) or (3,1,-1) and excludes the second because a
    section of class C_0-f would have b = -1 < 0. Searched outside the twelve
    retained sets: NTU 2020 has no entry for Exercise 15 of section 2; Yang
    Pi-Yeh, Hartshorne Solutions, printed pp. 105-106
    (tmp/sources/lfwin-hartshorne-solutions.pdf), has the (a) computation and
    garbled (b) and (c). Egbert, PDF pp. 271-273, cites Miyanishi for (c). Not
    checked: whether Y as constructed is singular with delta = 1; the card
    asserts it from p_a(Y) - p_a(C) = 1 and does not compute the singularity.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The text version of the NTU Chapter V homework now exists: it is read in
    tmp/sources/ntu-ag2-chapter5.pdf and in its MinerU text version
    tmp/sources/ntu-ag2-chapter5.md. The event above predates that file, records
    what was read from the PDF alone, and is left as it was dated.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes and Pedreira (arXiv:math/0006204v3) on 2026-11-16: the paper has
    no Frobenius statement and no characteristic-p discussion, so it does not
    reach this exercise. Math StackExchange
    question 4553266, saved as
    tmp/sources/mse-4553266-hart77-v215c-genus-inseparable.md, asks about the genus
    of exactly the curve of part (c) and has
    no answer. The citation carried by the retained Egbert entry, Miyanishi, Open
    Algebraic Surfaces, Lemma 2.5.2.2, was not read because that book is not in
    tmp/sources. No complete published argument located; steps s7 to s10 remain
    the card's, and the defect of the printed "nonsingular", recorded at the head
    of the solution, stands.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Restored the event of 2026-11-11 above to its text of that date, removing the
    text-version name that a later commit of 2026-11-16 inserted into it. Yang
    Pi-Yeh's text version is tmp/sources/lfwin-hartshorne-solutions.md beside his
    PDF, and the remark's citation of him names that file; Egbert's is
    tmp/sources/hartshorne-solutions-egbert.md. The event of 2026-11-16 above,
    which records that the National Taiwan University set's text version had
    arrived, stays as it was written.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Transcription pass for issue #121 on 2026-11-16: the solution is now the
    published argument, and every step names its source, numbered statement and
    printed page. Read at the cited places: Robin Hartshorne, Ample vector
    bundles on curves, Nagoya Math. J. 43 (1971), 73-89, text version
    tmp/sources/hartshorne-1971-ample-vector-bundles-curves.md with its PDF,
    Lemma 3.1 printed pp. 84-85 and Example 3.2 printed pp. 85-86; and Qihong
    Xie, Counterexamples to the Kawamata-Viehweg Vanishing on Ruled Surfaces in
    Positive Characteristic, text version
    tmp/sources/xie-2007-kawamata-viehweg-counterexamples-ruled-surfaces.md
    with its PDF, Example 3.1 printed pp. 5-6 and Lemma 4.4 printed pp. 10-11.
    Pages were fixed from the PDFs page by page and not from the extractions,
    which mark only 20-page ranges; the pages given for Xie in the batch brief,
    4-5 and 9-10, are one page low, the PDFs carrying their own folios.
    Checked against the book in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    where printed p. N is PDF p. N+15: V.2.15 as printed on p. 385, with (a),
    (b), the curve Y of (c) and D = 2C_0; and Proposition 2.21(b) with Remark
    2.21.1, both printed p. 382, whose hypotheses are e < 0 with char k = 0 or g
    at most 1, which this X with e = -1, char k = 3 and g = 3 fails while D
    satisfies its two numerical conditions. What the sources establish: part
    (a) is Hartshorne 1971 Lemma 3.1, its identification with
    H^2(P^2,O(-4)), the composition with g^2 and the vanishing checked
    monomial by monomial, the composition and the vanishing both printed on
    p. 85; part (b) is his Example 3.2, with its two Riemann-Roch dimensions,
    both printed on p. 85, and his dimension count, whose printed diagram is
    the naturality square of f^* and whose count the card's step carries out
    with those two numbers and the kernel dimension; the curve of (c), its
    class and its disjointness from the section are Xie's Example 3.1, printed
    p. 5 for that sentence, and its purely inseparable projection is his Lemma
    4.4(iii) applied to Y^2 = -9 < 0.
    What no source establishes, and what the COMPLAINTS record of 2026-11-16
    names: the printed "nonsingular" of (c) has no published proof and can
    have none, since adjunction gives p_a(Y) = 4 while the normalization of Y
    is C of genus 3, and Xie's own assertion that his C' is smooth over k,
    printed p. 5, is false for p = 3 and L of degree one by that same count.
    What this event had wrong and now states correctly: the diagram Hartshorne
    1971 prints there is clean, the mangling being the extraction's, and the
    card no longer calls it garbled; and e = -1 for X was first argued here
    from the book's Theorem V.2.15, which is a theorem about elliptic curves
    and does not apply to C of genus 3. That argument is withdrawn and step s6
    again carries the card's own normalization proof, H^0(C, E(-P)) = 0
    through the connecting map, marked there as the card's own. The statement
    of part (c) was also repaired in this pass, which the event of 2026-10-29
    says was done but was not: the book prints "X contains a nonsingular curve
    Y = 3C_0 - 3f, such that pi: Y -> C is purely inseparable", the word
    "nonsingular" being false by step s9, and the statement now asks for an
    integral curve of that class whose normalization is C. Not
    checked: no source beyond the two named and the book was read in this
    pass, and whether Y has exactly one singular point was not verified
    independently of delta = p_a - g = 1.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report on the transcription, and the rendering repairs it
    required. (i) The solution's preamble read "Every step below transcribes a
    published argument", which steps s6, s9 and s10 contradict, each of them
    marked on the card as its own; it now says that a step naming a source
    transcribes that source and that a step no source carries is marked as this
    card's. (ii) The paragraph that stood after the genus-three sentence was an
    account of how the statement of part (c) was repaired --- the book's
    "nonsingular" replaced by "integral with normalization C" --- and
    belongs in this record, not on the rendered page: it is here, and it reads
    as the event above states it, the book printing "X contains a nonsingular
    curve Y = 3C_0 - 3f, such that pi: Y -> C is purely inseparable" and
    adjunction giving p_a(Y) = 4 against the genus 3 of the Frobenius twist
    C^(3) = C; the rendered solution now carries the statement without the
    account of the repair. (iii) Out of the preamble and the remark went the
    tmp/sources paths, which are this VM's bookkeeping and not part of a
    citation, and out of the remark went the words "a source not in
    tmp/sources" after Egbert's citation of Miyanishi, Open Algebraic Surfaces,
    lemma 2.5.2.2 --- that book was not read for this card, which is the fact
    worth recording and is recorded here. What was read, in this pass and in
    the pass above, and where: Hartshorne 1971 in
    tmp/sources/hartshorne-1971-ample-vector-bundles-curves.md beside
    tmp/sources/hartshorne-1971-ample-vector-bundles-curves.pdf, Lemma 3.1 on
    the folios numbered 84 and 85 with the identification and the composition
    on p. 85, and Example 3.2 on pp. 85 and 86 with both Riemann--Roch
    dimensions on p. 85; Xie in
    tmp/sources/xie-2007-kawamata-viehweg-counterexamples-ruled-surfaces.md
    beside its PDF, Example 3.1 on the folios numbered 5 and 6 --- its
    smoothness sentence, "It is easy to verify that both E and C' are smooth
    over k", is on p. 5, as the step quoting it says --- and Lemma 4.4 on
    pp. 10 and 11; Egbert in tmp/sources/hartshorne-solutions-egbert.md, which
    paginates by PDF page, pp. 271 to 273; Yang Pi-Yeh in
    tmp/sources/lfwin-hartshorne-solutions.md, exercise 5.2.15 on printed
    pp. 105--106; and the National Taiwan University 2020 Spring set in
    tmp/sources/ntu-ag2-chapter5.md, which has no entry for Exercise 15 of §2.
    The COMPLAINTS record of this date for this batch said Xie's smoothness
    sentence stands on printed p. 6; the folio carrying it is p. 5, and the
    correction is stated in a record of this date rather than in that one.
    Nothing else on the card was changed, and no mathematics was altered by
    this repair.
- event: source-corrected
  by: claude
  date: 2026-11-17
  note: >-
    Markup only, no change of statement or proof. Six spans wrote the
    restriction of a morphism to a curve in the postfix form
    `\pi\restrictionof_Y` and `f\restrictionof_R`. That is a misuse of the
    preamble's two-argument macro `\restrictionof{A}{B}`: TeX takes its first
    argument to be the `_` of the subscript and its second to be the
    subscript's letter, and the preamble's definition rejects the result with
    "Missing { inserted", checked by typesetting that definition beside the
    spans with `pdflatex`. The six now read $\restrictionof{\pi}{Y}$ and
    $\restrictionof{f}{R}$; no new macro was added, since this is the existing
    semantic macro for the restriction of the first argument to the second.
    `qualc check` did not report these, because its undefined-command check
    tests the command's name and not how many arguments it is given. Not
    checked: the rendered page in a browser, and no mathematics was read or
    altered by this repair.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Two corrections, read for issue #164; no conclusion of the card moves.
    (i) Step s4 justified the surjectivity of H^1(C,O_C(-3P)) -> H^1(C,O_C)
    by saying that the H^0 part of 0 -> O_C(-3P) -> O_C -> O_{3P} -> 0 is an
    isomorphism h^0(O_C) = h^0(O_{3P}) = 1. That is false: O_{3P} is the
    structure sheaf of the length-3 subscheme 3P, so h^0(O_{3P}) = 3, and
    H^0(O_C) -> H^0(O_{3P}) is injective and not surjective. The conclusion is
    right, for a reason the step now gives: H^1(C,O_{3P}) = 0 because 3P is
    zero-dimensional, so the map on H^1 is surjective and its kernel has
    dimension 5 - 3 = 2. (ii) Step s10 cited Remark 2.21.1 as printed p. 382.
    Proposition 2.21 and its hypotheses are on printed p. 382, the folio at the
    foot of PDF p. 397 of tmp/sources/hartshorne-1977-algebraic-geometry.pdf;
    Remark 2.21.1, "In the remaining case e < 0, char k = p > 0, g >= 2, we
    cannot get necessary and sufficient conditions", is on printed p. 383, the
    folio at the foot of PDF p. 398. The step now says p. 383; the dated event
    above that gives "Proposition 2.21(b) with Remark 2.21.1, both printed
    p. 382" is left as written. Everything else on the card was checked in this
    pass and stands: the printed statement on p. 385 with the correction of
    "nonsingular" recorded in the remark; s1 to s3, including the monomials of
    F^2 and their vanishing exponents; the Riemann-Roch dimensions 3 and 5;
    s5's dimension count; s6's e = -1 and the normalized-bundle argument; s7
    and s8, Y^2 = -9 and Y.f = 3; s9's adjunction p_a = 1 + (-9+15)/2 = 4
    against genus 3; and s10's non-ampleness of D = 2C_0 from C_0.Y = 0.
    Checks: qualc.authoring check P-AGH5215FROBENIUSRULED, "schema and Markdown
    parsing OK (single card)"; tools/check_macros.py on the card, OK; tmp/lam.sh
    numbering the steps 1 to 10 with QED labels present and no unknown step
    label. Not checked: the printed copies of Hartshorne, Xie or Hartshorne
    1971; the text layers of the retained PDFs only.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The irreducibility of Xie's curve, read for issue #164 and recorded rather
    than repaired. Example 3.1, printed p. 5, writes "The section t determines
    an irreducible curve C' on X" and gives no argument for it, and this card's
    steps s7 to s10 use the integrality of Y: s9 computes one singular point
    and the normalization from it, and s10 meets D with Y as an irreducible
    curve. The assertion is not a consequence of the data the construction
    supplies. Y.f = 3 and Y.C_0 = 0, so a decomposition Y = Y_1 + Y_2 would
    give a component with Y_1.f = 1, that is a section, of class C_0 + bf, and
    Y_1.C_0 = 0 reads 1 + b = 0, so b = -1 and Y_1^2 = 1 + 2b = -1; nothing in
    the construction excludes a section of that class, and Xie does not argue
    that none occurs. What stands as computed: the zero locus Y of his t has
    class 3C_0 - 3f and is disjoint from C_0, and pi: Y -> C has degree
    Y.f = 3. The remark now says that the irreducibility is his assertion; the
    statement of (c) keeps "integral", which is the form the corrected statement
    can have if his assertion holds. Not checked: whether Y is irreducible for
    this X, for which no proof was found in the paper and no other source was
    searched; the printed Xie was not read, only the retained PDF's text layer
    at pp. 5-6.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Xie's Lemma 4.4(iii), printed pp. 10-11, whose last step the paper leaves
    unargued, read in full. After showing that the components R_1, ..., R_n of
    psi^{-1}(R) have equal negative self-intersection, it concludes "Since rho(X_B)
    = 2, we have deg h(x) = n = 1". The step is correct, and the argument is
    this. X_B is a P^1-bundle over B by Lemma 4.4(i), so Num(X_B) has rank two,
    with a fibre f_B and a section sigma as basis, f_B^2 = 0 and f_B.sigma = 1;
    the classes orthogonal to f_B are the multiples of f_B. Each R_i maps
    finitely onto B, so a_i := R_i.f_B > 0. If R_1 and R_2 are distinct
    irreducible curves with R_1^2 = R_2^2 < 0, the class alpha = a_2R_1 - a_1R_2
    has alpha.f_B = 0, hence alpha = m f_B for some rational m; pairing with R_1
    gives alpha.R_1 = a_2R_1^2 - a_1(R_1.R_2) < 0 and pairing with R_2 gives
    alpha.R_2 = a_2(R_1.R_2) - a_1R_2^2 > 0, since distinct irreducible curves on
    a surface meet nonnegatively. But alpha.R_i = m a_i with a_i > 0, so the
    first inequality forces m < 0 and the second m > 0, a contradiction. So no
    two components exist and n = 1. The earlier half of (iii) was checked too:
    the R_i meet pairwise nonnegatively, so (sum R_i)^2 >= 0 if their
    self-intersections are nonnegative, while sum R_i = psi^*R has square
    deg(psi) R^2 < 0. Not checked: that the multiplicities on psi^{-1}(R) are 1,
    which the argument needs, and Xie's citation of [Sc01, Proposition 3.3] for
    (iii) itself; the printed paper was not read, only the retained PDF's text
    layer at pp. 10-11.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A shape for Y that the card does not consider, and that every number it
    computes is consistent with. Xie's section t is the image of 1 under
    H^0(C,O_C) -> H^0(C,F^*E \otimes L^{-3}) -> H^0(C,S^3(E) \otimes L^{-3}), and the
    second map is the adjoint of the p-th power map M -> F_*M^p, so the image of
    the pulled-back section is its cube. Concretely: E \otimes L^{-1} is the
    nonsplit extension 0 -> L^{-1} -> E \otimes L^{-1} -> O_C -> 0, so
    H^0(E \otimes L^{-1}) = k, spanned by the section s mapping to 1 in H^0(O_C);
    F^*s maps to s^3 under the second arrow, and the kernel L^{-3} of the
    sequence 0 -> L^{-3} -> F^*E \otimes L^{-3} -> O_C -> 0 has no global section,
    so t = s^3 up to a scalar. Then Y = div(t) = 3D with D = div(s) the zero
    locus of a section of O_X(1) \otimes f^*L^{-1}: a section of the ruled surface,
    isomorphic to C, of self-intersection D^2 = 1 + 2(-1) = -1, disjoint from
    C_0. That reproduces every number on the card -- Y^2 = 9D^2 = -9,
    Y.f = 3 deg(D -> C) = 3, Y.K_X = 3(2g-2-D^2) = 15 and p_a = 4 -- and it
    makes Y non-reduced: the normalization is D = C, but the divisor is a
    triple section, not an integral curve with one singular point. If that
    reading is right, the "integral" of the corrected statement and the "one
    singular point of delta = 1" of step s9 are both wrong, and the truth is
    that 3C_0 - 3f is 3 times the section D, which is also why the printed
    "nonsingular" cannot hold. Not established here: that Xie's second arrow is
    the adjoint p-th power map -- his paper does not say which map it is, and
    the printed paper was not read; and no example was computed. Recorded rather
    than repaired: the card's step s9 keeps its claim, and this event is the
    reason it should be re-read against the printed paper before it is relied
    on.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Part (c) corrected: Xie's C' is the triple of a section, not an integral
    curve, and the statement and steps s7 to s10 now say so. The printed p. 5
    was read as an image -- pdftoppm at 150 dpi of PDF p. 5 of the retained Xie
    PDF -- and it writes only "through the maps ..." with an inclusion into
    S^p, naming no map; the second arrow is the adjoint of the cube map, the
    only natural inclusion, so t is the cube of a section of a line bundle. The
    section s of E \otimes L^{-1} mapping to 1 in H^0(O_C) is unique up to scale,
    and it must vanish, since otherwise it would split the extension and
    contradict step s5; its zero locus Sigma is a curve of class C_0 - f with
    Sigma.f = 1 over C, hence irreducible and a section, isomorphic to C, with
    Sigma^2 = -1 and Sigma disjoint from C_0; and Y = div(t) = 3Sigma. What
    changed: the statement of (c) is the book's words again, since "integral" is
    not what the construction gives; s7 now proves the section and the triple;
    s8 no longer cites Lemma 4.4(iii), whose hypothesis is an irreducible R,
    and instead observes that 3Sigma -> C is an isomorphism followed by the
    triple thickening; s9 keeps the adjunction count and the argument that no
    nonsingular curve has the class -- IV.2.5 for the purely inseparable case,
    Riemann-Hurwitz for the separable one, both with printed pages -- and states
    that Xie's divisor is not reduced; s10 meets 2C_0 with the irreducible
    Sigma instead of with Y. Not checked: whether some other, reduced curve in
    the class 3C_0 - 3f exists, since the argument here decides Xie's divisor
    only; and no example was computed.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The question the event above left open is settled: the class 3C_0 - 3f has
    exactly one effective divisor, 3Sigma, so there is no other curve in it and
    none that is reduced. The computation is in step s9: a divisor of
    O_X(3) ot f^*L^{-3} is a section of it, whose space is
    H^0(C, S^3E ot L^{-3}); the subbundle O_C of E gives S^3E a filtration with
    successive quotients L^3, L^2, L and O_C, so the twisted bundle is filtered
    with quotients O_C, L^{-1}, L^{-2} and L^{-3}, and h^0 is at most
    1 + 0 + 0 + 0 = 1 because deg L = 1; it is at least 1 because t = s^3 is
    nonzero. Hence the section is unique up to scale and 3Sigma is the only
    effective divisor in the class. The adjunction and IV.2.5 / Riemann-Hurwitz
    argument stays as an independent proof that no nonsingular curve has the
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Reading step s9 for its mathematics found a notation collision, and the
    step is repaired. The solution's preamble fixes L(A) = O_C(A) for a divisor
    A, under which the bare symbol L is O_C, of degree 0. Step s7 then writes
    "L = O_C(P)", of degree 1, for the bundle of Xie's quotation, and the bound
    of step s9, "deg L = 1 makes each of the last three negative", holds only of
    that second reading: read with the preamble's convention the four summands
    are all h^0(O_C) = 1 and the count is 4, which does not give the uniqueness
    the step concludes, while the second reading gives 1 + 0 + 0 + 0. The step
    now names the line bundles O_C(-P), O_C(-2P) and O_C(-3P) and the sheaf of
    the class, O_X(3) ot f^*O_C(-3P), so that the filtration's quotients
    O_C(3P), O_C(2P), O_C(P) and O_C are exactly those of the extension
    0 -> O_C -> E -> O_C(P) -> 0 of step s6, and the bound stands on its own
    terms. No number changes: p_a(Y) = 4 by adjunction, 3Sigma is the unique
    effective divisor of the class, and the separable and purely inseparable
    cases of the last paragraph are as they were. Checked in this pass:
    Hartshorne V.2.15(b)-(c) as printed on printed p. 385, read on the PDF's
    own folio (PDF p. 400), whose extension is 0 -> O_C -> E -> L(P) -> 0 with
    his L the trivial bundle, so that his L(P) is O_C(P) and his L(-P) is
    O_C(-P); and Hartshorne 1971, Example 3.2, printed p. 85, "The degree of E
    is 1", which fixes deg E = 1 and hence C_0^2 = -e = 1. Not checked in this
    pass: Xie's Example 3.1 was not re-read, and the statement repair the printed
    "nonsingular" needed is the one the earlier events of this card record and
    is not re-decided here.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #164, the reader's second NOT MET item, which has two halves. The
    numbered-source half is a version difference, and the citation is right
    against the file the card owns. The reader read
    arxiv.org/pdf/math/0702554v3, where the construction is Theorem 3.1 and
    begins on printed p. 4; the retained file is v5, whose first page carries
    the arXiv stamp "math/0702554v5 [math.AG] 8 Oct 2008", and there the same
    statement, word for word, is Example 3.1 on printed p. 5. Both were read
    for this event: the v3 PDF was downloaded and its printed p. 4 reads
    "Theorem 3.1. If C is a Tango curve, then there are a P1-bundle f: X -> C,
    ...", and the v5 text of Example 3.1 is at the place in the proof the card
    cites. The provenance paragraph now names the version and records the v3
    numbering, so the two are not confused again. The second half stands: the
    card's identification of Xie's divisor with 3 Sigma is not a transcription,
    because Xie's claim that C' is irreducible and smooth fails here -- his
    divisor is three times a section, so irreducibility can only name the
    support and smoothness is false -- and no published solution covers the
    case. That part of step s7 is now marked as the card's own, as step s9 and
    the last paragraph of s10 already were. Not checked: the printed paper,
    only the two arXiv PDFs.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Issue #164, the demand that the proof of V.2.15 be transcribed from a
    published solution set. No such set exists, and none can prove the printed
    statement. The retained Hartshorne sets were swept: Egbert, Exercise
    V.2.15, writes for (c) only "To see the curve
    Y = 3C_0-3f is inseparable is Miyanishi, Open Algebraic Surfaces, lemma
    2.5.2.2" and then calls Y "some section of C", which is a pointer and not a
    proof; Yang Pi-Yeh, Exercise 5.2.15, begins (c) with
    "Clearly deg pi = Y.f = 3" and concludes that pi is not separable, which
    assumes the curve and does not follow; Park has only V.5; Reiser's Chapter
    V is "Coming soon"; the remaining retained sets stop before Chapter V
    (Borcherds and Troiani at I, Cais, Cutrone-Marshburn, Lomont and Sam at IV,
    Kim at III, Stein and Saglam-Chris at III, Okamoto at II.9); NTU AG II 2020
    has no entry for Exercise 15 of section 2. Searched online beyond them, with
    no solution set containing a proof of (c) found: the GitHub repositories of
    Hartshorne solutions checked (mikeleew, corn-muffin, nilaykumar,
    jmoellermath, maths644311798, reiserb) stop before Chapter V or omit
    V.2.15, as do the web-compiled manuals checked. The only other treatment of
    (c) is Xie's own Example 3.1, which asserts that C' is
    irreducible and smooth and proves neither, and Math StackExchange 4553266,
    which has no answer. That no correct proof can exist is step s9: the class
    3C_0-3f has p_a = 4 by adjunction, while a purely inseparable degree-3 map
    to C forces g(Y) = g(C) = 3 by IV.2.5 and a separable one is excluded by
    Riemann-Hurwitz, so the printed "nonsingular" cannot hold. What this pass
    changed: step s7's own argument named "the section of E \otimes L^{-1}
    mapping to 1 in H^0(O_C)", and no such section exists, because the
    connecting map of 0 -> L^{-1} -> E \otimes L^{-1} -> O_C -> 0 sends 1 to the
    nonzero extension class xi, so H^0(E \otimes L^{-1}) = 0. The step now
    computes t locally as the cube of the local section f_2 + a f_1 of
    E \otimes L^{-1} and reads off its zero locus as the section Sigma
    directly; the conclusion Y = 3 Sigma and all the numbers after it are
    unchanged. A correction to that paragraph, made in the commit after this
    one: the cube must be taken in S^3(E \otimes L^{-1}), since F^*L^{-1} =
    L^{-3} identifies F^*E \otimes L^{-3} with F^*(E \otimes L^{-1}); cubing a
    section of E \otimes L^{-1} directly would land in L^{-9} and is wrong. The
    rendered remark no longer says that part (c) is published in
    the form the steps correct. Citations on the rendered page are by numbered
    statement --- the exercise number in Hartshorne's book, Example 3.1 and
    Lemma 2.5.2.2 of Xie, Lemma 3.1 and Example 3.2 of Hartshorne 1971, and
    IV.2.4, IV.2.5, V.1.5, Corollary V.2.11, Proposition 2.21(b) of the book ---
    and this event's own locators were replaced by the statements in the commit
    that follows it; the earlier dated events of this card keep the printed
    pages they were read in and are left as they were written. Not checked: the
    printed copies of Xie, Egbert
    or Yang, only the retained text layers and, for Xie, the arXiv v5, v6 and
    v7 PDF text.

---

::: {.problem}
Let $C$ be the plane curve $x^3 y+y^3 z+z^3 x=0$ over a field $k$ of characteristic 3 (IV, Ex. 2.4).

(a) Show that the action of the $k$-linear Frobenius morphism $f$ on $H^1\left(C, \OO_C\right)$ is identically 0 (Cf. (IV, 4.21)).

(b) Fix a point $P \in C$, and show that there is a nonzero $\xi \in H^1(\mathcal{L}(-P))$ such that $f^* \xi=0$ in $H^1(\mathcal{L}(-3 P))$.

(c) Now let $\mathcal{E}$ be defined by $\xi$ as an extension
$$
0 \rightarrow \OO_C \rightarrow \mathcal{E} \rightarrow \mathcal{L}(P) \rightarrow 0,
$$
and let $X$ be the corresponding ruled surface over $C$. Show that $X$ contains a nonsingular curve $Y \equiv 3 C_0-3 f$, such that $\pi: Y \rightarrow C$ is purely inseparable.

    Show that the divisor $D=2 C_0$ satisfies the hypotheses of (2.21.b), but is not ample.
:::

::: {.solution}
A step that transcribes a published argument names the source and the numbered statement; a step no source carries is marked as this card's. Robin Hartshorne, *Ample vector bundles on curves*, Nagoya Math. J. 43 (1971), 73--89, Lemma 3.1, and Example 3.2, for parts (a) and (b); and Qihong Xie, *Counterexamples to the Kawamata-Viehweg Vanishing on Ruled Surfaces in Positive Characteristic*, arXiv:math/0702554v5 (8 October 2008), Example 3.1, and Lemma 4.4, for the curve of part (c). Every citation of Xie below is to that version, in which the construction is Example 3.1; in v3 (7 May 2007) the same statement is Theorem 3.1, so the number depends on the version. Hartshorne 1971 runs this example over a field of characteristic $3$ and its curve is the plane quartic of the exercise.

As in Hartshorne's notation, write
$$
\mathcal L(A)=\OO_C(A)
$$
for the invertible sheaf associated to a divisor $A$ on $C$, and
$$
F=x^3y+y^3z+z^3x.
$$
By [[P-AGH424FUNNYQUARTIC]] the plane quartic
$$
C=V(F)\subseteq\PP^2
$$
is nonsingular, hence has genus $3$.

::: pf

::: {.pf-step #s1}
There is an isomorphism
$$
H^1(C,\OO_C)\cong H^2(\PP^2,\OO_{\PP^2}(-4)),
$$
and the latter has a basis of the three negative monomials $\frac{1}{x^2yz}$, $\frac{1}{xy^2z}$, $\frac{1}{xyz^2}$.

::: pf-proof
Hartshorne 1971, Lemma 3.1: "Let $g=x^3y+y^3z+z^3x$. Then we have an exact sequence
$$
0\to\OO_P(-4)\xrightarrow{g}\OO_P\to\OO_X\to0,
$$
which gives rise to an isomorphism
$$
H^1(X,\OO_X)\xrightarrow{\cong}H^2(P,\OO_P(-4)).
$$
This latter vector space, according to the explicit calculations of cohomology on projective space, has a basis consisting of the 'negative monomials' of degree 4", and he lists the three above.
:::

:::

::: {.pf-step #s2}
Under that isomorphism the action of Frobenius on $H^1(C,\OO_C)$ becomes the composition
$$
H^2(\PP^2,\OO_{\PP^2}(-4))\xrightarrow{f^*}H^2(\PP^2,\OO_{\PP^2}(-12))\xrightarrow{g^2}H^2(\PP^2,\OO_{\PP^2}(-4))
$$
of Frobenius on $\PP^2$ with multiplication by $g^2$.

::: pf-proof
Hartshorne 1971, Lemma 3.1: "Under the isomorphism (1), the action of frobenius on $H^1(X,\OO_X)$ becomes the composition ... of frobenius on $\PP^2$ with multiplication by $g^2$." Then "frobenius takes our three monomials into their cubes", listed as $1/x^6y^3z^3$, $1/x^3y^6z^3$, $1/x^3y^3z^6$.

The thickening behind the map: pulling the displayed exact sequence back by the characteristic-$3$ Frobenius changes $\OO(-4)$ to $\OO(-12)$ and sends a class to its cube, and the restriction from the thickening cut out by $F^3$ to $C$ is multiplication by $F^{3-1}=F^2$ on the first term.
:::

:::

::: {.pf-step #s3}
The action of the $k$-linear Frobenius morphism on $H^1(C,\OO_C)$ is identically zero.

::: pf-proof
Hartshorne 1971, Lemma 3.1: "Every monomial of $g^2$ contains either $x^6$ or $y^3$ or $z^3$. Hence $g^2/x^6y^3z^3=0$ in $H^2(P,\OO_P(-4))$. By symmetry, $g^2$ also kills the other two monomials, so we find that frobenius on $H^1(X,\OO_X)$ is 0."

Carried out term by term, as the sentence says: the six monomial types of $F^2=(x^3y+y^3z+z^3x)^2$ are $x^6y^2$, $y^6z^2$, $z^6x^2$, $x^3y^4z$, $x^4yz^3$ and $xy^3z^4$, and after multiplication by $(x^6y^3z^3)^{-1}$ they leave respectively the $x$-, $y$-, $z$-, $y$-, $z$- and $y$-exponent at least zero, so each is zero in the top cohomology; the other two basis monomials are the cyclic permutations of the first, and $F$ is cyclically symmetric. This proves part (a).
:::

:::

::: {.pf-step #s4}
For a point $P\in C$,
$$
\dim H^1(C,\OO_C(-P))=3,
\qquad
\dim H^1(C,\OO_C(-3P))=5,
$$
and the kernel of $H^1(C,\OO_C(-3P))\to H^1(C,\OO_C)$ has dimension $2$.

::: pf-proof
Hartshorne 1971, Example 3.2, gives the first as "By Riemann--Roch, $H^1(X,\OO(-P))$ has dimension 3", and the second is his "By Riemann--Roch, $\dim H^1(X,\OO_X(-3P))=5$". Both are Riemann--Roch on a curve of genus $3$,
$$
h^1-h^0=g-1-\deg,
$$
with $h^0=0$ at negative degree: $h^1(\OO_C(-P))=2+1=3$ and $h^1(\OO_C(-3P))=2+3=5$.

The kernel is counted from the restriction sequence $0\to\OO_C(-3P)\to\OO_C\to\OO_{3P}\to0$: the quotient $\OO_{3P}$ is supported on the zero-dimensional scheme $3P$, so $H^1(C,\OO_{3P})=0$ and $H^1(C,\OO_C(-3P))\to H^1(C,\OO_C)$ is surjective, with kernel of dimension $5-3=2$. For $P$ the same sequence shows that $H^1(C,\OO_C(-P))\to H^1(C,\OO_C)$ is an isomorphism, which is the equality of dimensions the count below uses.
:::

:::

::: {.pf-step #s5}
There is a nonzero
$$
\xi\in H^1(C,\OO_C(-P))
$$
with $f^*\xi=0$ in $H^1(C,\OO_C(-3P))$.

::: pf-proof
Hartshorne 1971, Example 3.2: "Now frobenius is 0 on $H^1(X,\OO_X)$. So by counting dimensions, there is a $\hat\xi\ne0$ in $H^1(X,\OO_X(-P))$ with $f^*(\xi)=0$." The diagram he prints between those two sentences is the naturality square of $f^*$ over the two restriction maps to $H^1(X,\OO_X)$; the count it names is the one step [](#s4){.pf-ref} carries out, with the two printed numbers: $f^*$ maps a three-dimensional space into the two-dimensional kernel of $H^1(\OO_C(-3P))\to H^1(\OO_C)$, since the composite $H^1(\OO_C(-P))\to H^1(\OO_C)$ is an isomorphism and Frobenius vanishes on $H^1(\OO_C)$ by step [](#s3){.pf-ref}, so the map has a nonzero kernel. This proves part (b).
:::

:::

::: {.pf-step #s6}
Let $\mathcal E$ be the extension determined by $\xi$:
$$
0\to\OO_C\to\mathcal E\to\OO_C(P)\to0,
$$
and $X=\PP(\mathcal E)$. Then $\deg\mathcal E=1$, the quotient gives a section $C_0$ with $\OO_X(C_0)\cong\OO_X(1)$ and $C_0^2=1$, the bundle $\mathcal E$ is normalized, and the invariant of $X$ is
$$
\boxed{e=-1}.
$$

::: pf-proof
Hartshorne 1971, Example 3.2, gives the extension and "The degree of $E$ is 1". Xie, Example 3.1, writes for the same construction, with $\mathcal L=\OO_C(L)$ of degree $1$ and $X=\PP(\mathcal E)$: "The sequence (3) determines a section $E$ of $f$ through the map $H^0(C,\OO_C)\hookrightarrow H^0(C,\mathcal E)=H^0(X,\OO_X(1))$, hence $\OO_X(E)\cong\OO_X(1)$", and "$E^2=\deg\mathcal E=\deg\mathcal L>0$". Xie writes $E$ for the section and $\mathcal E$ for the bundle; the section is $C_0$, with $C_0^2=1$ and $C_0^2=-e$.

That the bundle is normalized is this card's own argument, and no source read carries it. Let $M$ be a line bundle of negative degree on $C$. If $\deg M\le-2$, then $M$ and $M(P)$ both have negative degree, so $\mathcal E\tensor M$ has no global section. If $\deg M=-1$ and $M\not\cong\OO_C(-P)$, then $M(P)$ is a nontrivial line bundle of degree $0$ and again has no section, while $M$ has none. Finally for $M=\OO_C(-P)$, the twisted sequence is $0\to\OO_C(-P)\to\mathcal E(-P)\to\OO_C\to0$, whose connecting map
$$
H^0(C,\OO_C)\to H^1(C,\OO_C(-P))
$$
sends $1$ to the extension class $\xi$, which is nonzero by step [](#s5){.pf-ref}; so the quotient section of the twisted sequence does not lift and $H^0(C,\mathcal E(-P))=0$. Hence $H^0(C,\mathcal E\tensor M)=0$ for every line bundle of negative degree, $\mathcal E$ is normalized, and
$$
e=-\deg\det\mathcal E=-\deg\mathcal E=-1
$$
by (2.8.1).
:::

:::

::: {.pf-step #s7}
$X$ contains the section
$$
\Sigma\equiv C_0-f,\qquad \Sigma\cong C,\qquad \Sigma^2=-1,
$$
disjoint from $C_0$, and the divisor $Y=3\Sigma$ satisfies
$$
Y\equiv3C_0-3f,
\qquad
\OO_X(Y)\cong\OO_X(3)\tensor f^*\OO_C(-3P),
\qquad
C_0\cap Y=\emptyset.
$$

::: pf-proof
Xie, Example 3.1. Pulling the extension back by Frobenius gives the split sequence
$$
0\to\OO_C\to F^*\mathcal E\to\mathcal L^3\to0
$$
"since the extension class of (4) is just $F^*\eta(\alpha)=0$", which here is the choice of $\xi$ in step [](#s5){.pf-ref}. From it he obtains the exact sequence $0\to\OO_C\to F^*\mathcal E\otimes\mathcal L^{-3}\to\mathcal L^{-3}\to0$, "which determines a section $t\in H^0(X,\OO_X(3)\otimes f^*\mathcal L^{-3})$ through the maps $H^0(C,\OO_C)\hookrightarrow H^0(C,F^*\mathcal E\otimes\mathcal L^{-p})\hookrightarrow H^0(C,S^p(\mathcal E)\otimes\mathcal L^{-p})=H^0(X,\OO_X(p)\otimes f^*\mathcal L^{-p})$", and "The section $t$ determines an irreducible curve $C'\subset X$ such that $\OO_X(C')\cong\OO_X(p)\otimes f^{*}\mathcal L^{-p}$". He adds "It is easy to verify that both $E$ and $C'$ are smooth over $k$, and $E\cap C'=\emptyset$"; the smoothness of $C'$ is false, by steps [](#s7){.pf-ref} and [](#s9){.pf-ref}.

Here $p=3$ and $\mathcal L=\OO_C(P)$ has degree $1$.

Everything from here to the end of the step is this card's own, and no source read carries it: Xie prints only that $t$ determines an irreducible curve $C'$ of that class, and in this case the divisor is three times a section, so his irreducibility can only name the support while his smoothness claim is false. The local computation that follows replaces an earlier argument of this card which named a section of $\mathcal E\otimes\mathcal L^{-1}$ mapping to $1\in H^0(\OO_C)$: no such section exists, because the connecting map of $0\to\mathcal L^{-1}\to\mathcal E\otimes\mathcal L^{-1}\to\OO_C\to0$ sends $1$ to the nonzero extension class $\xi$ of step [](#s5){.pf-ref}, so $H^0(\mathcal E\otimes\mathcal L^{-1})=0$.

The second arrow in that chain is the cube map. Since $F^*\mathcal L^{-1}=\mathcal L^{-3}$, the bundle $F^*\mathcal E\otimes\mathcal L^{-3}$ is $F^*(\mathcal E\otimes\mathcal L^{-1})$, and the arrow sends a local section $v$ to $v^3\in S^3(\mathcal E\otimes\mathcal L^{-1})=S^3\mathcal E\otimes\mathcal L^{-3}$. Tensoring $0\to\OO_C\to F^*\mathcal E\to\mathcal L^3\to0$ by $\mathcal L^{-3}$ gives $0\to\mathcal L^{-3}\to F^*(\mathcal E\otimes\mathcal L^{-1})\to\OO_C\to0$, which splits, and a splitting carries $1\in H^0(\OO_C)$ to a section $u$, unique because $H^0(\mathcal L^{-3})=0$. Choose a local frame $f_1,f_2$ of $\mathcal E\otimes\mathcal L^{-1}$ over an open $U$, with $f_1$ spanning the subbundle $\mathcal L^{-1}$ and $f_2$ mapping to a generator of $\OO_C$, and let $f_1^F,f_2^F$ be the induced frame of $F^*(\mathcal E\otimes\mathcal L^{-1})$. Then $u=\restrictionof{f_2^F}{U}+a\restrictionof{f_1^F}{U}$ for some $a\in\OO_C(U)$, and
$$
t=u^3=f_2^3+a^3f_1^3=(f_2+af_1)^3 ,
$$
the cross terms vanishing in characteristic $3$. In the fibre coordinate $[\alpha:\beta]$ for $\alpha f_1+\beta f_2$, the section $t$ reads $\beta^3+a^3\alpha^3=(\beta+a\alpha)^3$, which vanishes exactly where $\beta+a\alpha=0$: one point in each fibre, of multiplicity three. These local equations agree on overlaps because they cut out the zero locus of $t$, so that locus is a section $\Sigma$ of $X\to C$ isomorphic to $C$, and $Y=\operatorname{div}(t)=3\Sigma$. Since $\OO_X(Y)=\OO_X(3)\otimes f^*\mathcal L^{-3}$, the class of $\Sigma$ is $C_0-f$, so $\Sigma^2=(C_0-f)^2=1+2(-1)=-1$, and $C_0\cdot\Sigma=1-1=0$ with both curves effective and irreducible gives $C_0\cap Y=\emptyset$, Xie's $E\cap C'=\emptyset$ with his $E$ the section $C_0$ of step [](#s6){.pf-ref}.
:::

:::

::: {.pf-step #s8}
The morphism $\restrictionof{\pi}{Y}:Y\to C$ is purely inseparable of degree $3$.

::: pf-proof
By step [](#s7){.pf-ref}, $Y=3\Sigma$ and $\restrictionof{\pi}{\Sigma}:\Sigma\to C$ is an isomorphism, so $\restrictionof{\pi}{Y}$ is that isomorphism followed by the triple thickening $3\Sigma\to\Sigma$. It is finite of degree $3$ --- the degree is $Y\cdot f=3(\Sigma\cdot f)=3$, since a fibre meets $Y$ in $\deg(\restrictionof{\pi}{Y})$ points counted with multiplicity --- and it induces the trivial extension of function fields, so it is purely inseparable. This is the sense in which the exercise's $\pi:Y\to C$ is purely inseparable for Xie's divisor.
:::

:::

::: {.pf-step #s9}
The divisor $3\Sigma$ is the only effective divisor in the class $3C_0-3f$; in particular no nonsingular curve has that class, and Xie's $Y=3\Sigma$ is not reduced, its reduction being the section $\Sigma\cong C$ of genus $3$ while $p_a(Y)=4$.

::: pf-proof
This step is this card's own, and no source read carries it. The class has exactly one member. A divisor of $\OO_X(3)\otimes f^*\OO_C(-3P)$ is a section of that line bundle, and $H^0(X,\OO_X(3)\otimes f^*\OO_C(-3P))=H^0(C,S^3\mathcal E\otimes\OO_C(-3P))$; the subbundle $\OO_C\subset\mathcal E$ of step [](#s6){.pf-ref}, whose quotient is $\OO_C(P)$, gives $S^3\mathcal E$ a filtration whose successive quotients are $\OO_C(3P)$, $\OO_C(2P)$, $\OO_C(P)$ and $\OO_C$, so the twisted bundle has quotients $\OO_C$, $\OO_C(-P)$, $\OO_C(-2P)$ and $\OO_C(-3P)$, and
$$
h^0(C,S^3\mathcal E\otimes\OO_C(-3P))\le h^0(\OO_C)+h^0(\OO_C(-P))+h^0(\OO_C(-2P))+h^0(\OO_C(-3P))=1+0+0+0=1,
$$
because $\deg\OO_C(-P)=-1$ makes each of the last three negative. The space is not zero, since $t\ne0$ by step [](#s7){.pf-ref}; so it is one-dimensional and $3\Sigma=\operatorname{div}(t)$ is its only effective divisor.

Independently, for an effective divisor $Y$ in the class, adjunction gives
$$
p_a(Y)=1+\frac12\qty(Y^2+Y\cdot K_X),
$$
and with $C_0^2=1$ and $K_X\equiv-2C_0+(2g-2-e)f=-2C_0+5f$ the value is
$$
1+\frac12\qty(-9+15)=4.
$$

Suppose a nonsingular curve $Y$ had this class. Then $Y\cdot f=3$, so $\restrictionof{\pi}{Y}:Y\to C$ is finite of degree $3$, and it is either separable or purely inseparable. If it is purely inseparable, Hartshorne IV.2.5 makes it a composition of $k$-linear Frobenius morphisms and gives $g(Y)=g(C)=3$, against $g(Y)=p_a(Y)=4$. If it is separable, Riemann--Hurwitz, IV.2.4 gives $2\cdot4-2=3(2\cdot3-2)+\deg R$, that is $6=12+\deg R<0$. So no nonsingular curve has the class.

For Xie's divisor, step [](#s7){.pf-ref} gives $Y=3\Sigma$ with $\Sigma\cong C$ of genus $3$; the adjunction count above, read with $Y=3\Sigma$ and $\Sigma\cdot K_X=2g-2-\Sigma^2=4+1=5$, is $1+\frac12(-9+15)=4$, so $p_a(3\Sigma)=4$ while its reduction has genus $3$: the divisor is not reduced, and every point of $\Sigma$ is a singular point of it.
:::

:::

::: {.pf-step #s10}
The divisor
$$
D=2C_0
$$
satisfies the numerical hypotheses of (2.21.b), namely $a>0$ and $b>\frac12ae$, but is not ample.

::: pf-proof
Proposition 2.21(b), reads: a divisor $D\equiv aC_0+bf$ is ample if and only if $a>0$ and $b>\frac12ae$; the proposition's own hypotheses are $e<0$ together with char $k=0$ or $g\le1$. The numerics are the book's, and the passage from the disjoint curve to non-ampleness is this card's own. For $D=2C_0$ one has $a=2$, $b=0$ and $e=-1$, so $a>0$ and $b=0>-1=\frac12\cdot2\cdot(-1)$: the two numerical conditions hold, and the proposition cannot be applied to $X$, whose $e=-1$, char $k=3$ and $g=3$ fail its hypotheses. That is the case its Remark 2.21.1, sets aside: "In the remaining case $e<0$, char $k=p>0$, $g\ge2$, we cannot get necessary and sufficient conditions for $D$ to be ample".

For non-ampleness, step [](#s7){.pf-ref} gives $C_0\cap\Sigma=\emptyset$, Xie's $E\cap C'=\emptyset$ in his Example 3.1; in intersection numbers that is $C_0\cdot\Sigma=0$, consistently with $(C_0-f)\cdot C_0=1-1=0$. Since $\Sigma$ is an irreducible curve on $X$,
$$
D\cdot\Sigma=2\,C_0\cdot\Sigma=0,
$$
and an ample divisor meets every irreducible curve positively, by Nakai--Moishezon [[T-SRFNAKAI]]. Therefore
$$
\boxed{D\text{ is not ample}.}
$$
Hartshorne 1971 announces the same failure for the bundle: its Example 3.2, is "A bundle $E$ of rank 2 on $X$, such that every quotient bundle of $E$ has positive degree, but $E$ is not ample", the bundle whose projectivization is $X$.
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (a), steps [](#s4){.pf-ref} and [](#s5){.pf-ref} part (b), steps [](#s6){.pf-ref} to [](#s8){.pf-ref} the divisor $3\Sigma$ of part (c) with its purely inseparable projection, step [](#s9){.pf-ref} the correction of the printed \"nonsingular\", and step [](#s10){.pf-ref} the divisor $D=2C_0$.
:::

:::

:::

::: {.remark title="Published solution"}
Parts (a) and (b) have complete published arguments. For part (c) the published record contains the construction but no proof: Xie asserts that his $C'$ is an irreducible smooth curve, and both assertions fail here, steps [](#s7){.pf-ref} to [](#s9){.pf-ref} identifying his divisor as $3\Sigma$, the triple of a section, and correcting the printed statement.

Robin Hartshorne, *Ample vector bundles on curves*, Nagoya Math. J. 43 (1971), 73--89: Lemma 3.1, is part (a), the vanishing of Frobenius on $H^1(C,\OO_C)$ through the identification with $H^2(\PP^2,\OO(-4))$ and the multiplication by $g^2$; Example 3.2, is part (b), the bundle, the two Riemann--Roch dimensions and the dimension count, together with the reason $E$ is not ample. He does not construct the curve $Y$ of part (c) and says nothing about $D=2C_0$.

Qihong Xie, *Counterexamples to the Kawamata-Viehweg Vanishing on Ruled Surfaces in Positive Characteristic*, arXiv:math/0702554v5 (8 October 2008): Example 3.1, is the construction of part (c), the section with $\OO_X(E)\cong\OO_X(1)$ and $E^2=\deg\mathcal E$, the split Frobenius pullback, and the curve $C'$ with $\OO_X(C')\cong\OO_X(p)\otimes f^*\mathcal L^{-p}$ disjoint from the section, which he calls irreducible and smooth; step [](#s7){.pf-ref} identifies it as $3\Sigma$, the triple of a section, so his ``irreducible'' can only name the support and his smoothness claim is false; Lemma 4.4(iii) is the pure inseparability of $\restrictionof{f}{R}$ for an irreducible $R$ with $R^2<0$. His Example 3.1 is stated for a base curve satisfying the Tango condition, which is how he produces the extension class; here the class is $\xi$ of part (b), so the construction applies as it stands with $p=3$ and $\mathcal L=\OO_C(P)$. His assertion that $C'$ is smooth over $k$ is false in this case, by the adjunction count of step [](#s9){.pf-ref}; for $p=3$, $\deg\mathcal L=1$ and $g(C)=3$ his curve has arithmetic genus $4$ and normalization $C$ of genus $3$.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.15, computes (a) as Hartshorne 1971 does, and for (c) writes only "To see the curve $Y\equiv3C_0-3f$ is inseparable is Miyanishi, *Open Algebraic Surfaces*, lemma 2.5.2.2". Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.15 reproduces (a) and has garbled (b) and (c). Algebraic Geometry II, National Taiwan University, 2020 Spring, has no entry for Exercise 15 of §2.
:::

::: {.remark}
The book's (c), Exercise V.2.15(c), reads "Show that $X$ contains a nonsingular curve $Y\equiv3C_0-3f$, such that $\pi:Y\to C$ is purely inseparable", and the adjective is what fails: step [](#s9){.pf-ref} shows that the class $3C_0-3f$ has $3\Sigma$ as its only effective divisor --- the space of sections is one-dimensional --- so it contains no nonsingular curve at all, and that Xie's divisor is the triple of the section $\Sigma\cong C$ of step [](#s7){.pf-ref}, so it is not even reduced. The statement above keeps the book's words, and the printed "nonsingular" is recorded as false here rather than kept.  Xie's Example 3.1, asserts the smoothness of his curve as well, and it fails for him by the same count.
:::
