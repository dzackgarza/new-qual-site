---
schema: qual/card@1
id: P-AGH5217CONORMALSPLIT
kind: problem
title: Splitting type of the conormal bundle of rational space curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.2.17* and the retained Egbert companion, which marks the
    exercise starred but supplies no solution. The proof below puts both
    parametrized curves on the smooth quadric x_0 x_3-x_1 x_2=0. They are
    graphs of the degree-n power map for n=2 and n=3. A direct two-chart
    calculation of the conormal sequence shows that its extension class is
    (n-1) times the generator of H^1(O_{P^1}(-2)); this is always nonzero for
    n=2, while for n=3 it vanishes exactly in characteristic 2. Birkhoff--
    Grothendieck then gives the requested splitting types.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed starred exercise at Hartshorne, Algebraic Geometry (1977),
    V.2, exercise 2.17, printed pages 385-386, with its printed answer for part
    (b). Rechecked the determinant of the conormal sheaf from the conormal
    sequence of C in P^3: deg = -4(n+1)-(-2) = -4n-2, the sum of the two ranks
    in the card's extension, so -10 for the twisted cubic and -14 for the
    quartic, matching -5,-5 and both -7,-7 and -6,-8. Rechecked the two-chart
    Cech computation of s3 including the binomial coefficients: the numerator of
    h' is (n-1)a^{n(n-1)}h + (n-1)a^{n(n-1)-1}q - n a^{n(n-1)}h + ..., giving
    -a^{n(n-1)}h + (n-1)a^{n(n-1)-1}q and the off-diagonal (n-1)s^{-1} in every
    characteristic; for n = 3 the term n a^{n(n-1)}h vanishes identically in
    characteristic 3 but the resulting coefficient of h is 2 = -1, so the class
    is still 2 eta. Searched outside the twelve retained sets: Yang Pi-Yeh,
    Hartshorne Solutions, exercise 5.2.17, printed pp. 106-107
    (tmp/sources/lfwin-hartshorne-solutions.pdf), computes both parts by the
    Jacobian presentation and adds characteristic 3 to the split case, which
    contradicts its own 2 eta; Algebraic Geometry II, National Taiwan
    University, 2020 Spring, has no entry for Exercise 17 of section 2. Egbert,
    PDF p. 273, enters the starred exercise with no argument. Not checked:
    whether the charts x_1 = 0 or x_2 = 0 add a generator of the ideal of C_n;
    the two charts used suffice because the transition matrix between them
    determines the Cech class.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Located two published treatments of part (a) on 2026-11-16, both saved in
    tmp/sources in this pass. Math StackExchange answer 1583486 by Ted Shifrin, to
    question 1583326, "Normal bundle of twisted cubic", in
    tmp/sources/mse-1583326-hart77-v217-twisted-cubic-normal-bundle.md, computes
    the conormal bundle of the twisted cubic in the charts [1,x,y,z] and
    [X,Y,Z,1], writes the two frames on the overlap, and reads the splitting
    O(-5) + O(-5) off the transition matrix, which is a complete argument for
    l = m = -5. Georges Elencwajg's answer 569653 to question 569237, in
    tmp/sources/mse-569237-hart77-v217-twisted-cubic-normal-bundle-2.md, records
    that the splitting of the normal bundle as O(5) + O(5) is Proposition 6 of
    Eisenbud and Van de Ven, On the normal bundles of smooth rational space
    curves, a published theorem not in tmp/sources. Math StackExchange answer
    2664944 by Sasha, to question 2664333, in
    tmp/sources/mse-2664333-hart77-v217-conormal-sheaf-twisted-cubic.md, gets the
    conormal sequence and the Jacobian presentation of the twisted cubic and stops
    at "it is easy to check that the conormal sheaf is O(-5) squared"; the degree
    count 4(-3) - 2(-1) = -10 admits O(-4) + O(-6) as well, so that entry is not
    complete. No published treatment of part (b) was located,
    in particular none of the characteristic-two answer minus six and minus eight.
    Steps s2 and s3 are the card's own general computation for both parts; step
    s5 now carries Shifrin's frame computation of part (a) beside the card's, with
    the change of coordinates between the two charts and the two elementary
    operations on the transition matrix, which his answer leaves as "here is where
    you have to do some work".
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected step s5's two elementary operations on 2026-11-16. The matrix
    relates the two frames, (tau_1, tau_2) = (sigma_1, sigma_2)M, so changing the
    first frame is a row operation with a matrix over k[t], the coordinate ring of
    the chart x_0 != 0 that carries sigma, and changing the second is a column
    operation with a matrix over k[t^{-1}], the ring of the chart x_3 != 0 that
    carries tau; the step had them the other way round, and the two operations it
    wrote -- (2/3)t^{-1} times the first row added to the second and -(2/3)t times
    the first column added to the second -- are then not changes of frame at all,
    so as it stood the reduction proved nothing even though its answer was right.
    The valid pair, verified by multiplying the two matrices out, is 2t times the
    second row added to the first, which is a row operation over k[t] and gives
    [[t^{-5}, 0], [2t^{-6}, t^{-5}]], and then -2t^{-1} times the first column
    added to the second, a column operation over k[t^{-1}], which gives t^{-5}
    times the identity. Equivalently M = t^{-5}AB with A = [[1,-2t],[0,1]] and
    B = [[1,0],[2t^{-1},1]], of determinant one, A over k[t] and B over k[t^{-1}],
    so the sheaf is O(-5) + O(-5) and l = m = -5, which steps s3 and s4 already
    give. The remark now states the two operations in the same order, and names
    the saved file of Elencwajg's answer 569653. The event of 2026-11-11 above is
    restored to its text of that date, the text-version name a later commit of
    2026-11-16 put into it being removed; Yang Pi-Yeh's text version is
    tmp/sources/lfwin-hartshorne-solutions.md and Egbert's is
    tmp/sources/hartshorne-solutions-egbert.md.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Transcription pass for issue #121 on 2026-11-16: parts (a) and (b) now cite
    the published arguments at the steps that use them, and the two steps no
    source carries are marked as this card's own. Read at the cited places: Ted
    Shifrin's answer 1583486 to Math StackExchange question 1583326, text
    version tmp/sources/mse-1583326-hart77-v217-twisted-cubic-normal-bundle.md,
    for part (a) by transition functions; Yang Pi-Yeh, Hartshorne Solutions,
    text version tmp/sources/lfwin-hartshorne-solutions.md, Solution 5.2.17,
    printed pp. 106-107, for both parts by the Jacobian presentation; and
    Eisenbud and Van de Ven, On the Normal Bundles of Smooth Rational Space
    Curves, Math. Ann. 256 (1981), 453-463, text version
    tmp/sources/eisenbud-van-de-ven-1981-normal-bundles-rational-space-curves.md
    with its PDF, Proposition 6, whose statement and the two proofs run from
    printed p. 458 to p. 460, the printed page being the PDF page plus 452.
    Checked against the book in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    where printed p. N is PDF p. N+15: V.2.17 as printed on pp. 385-386, starred,
    with its answer "If char k != 2, then l = m = -7; if char k = 2, then
    l, m = -6, -8". Three things this pass establishes beyond the events
    above. Part (a): Shifrin's frames and transition matrix are printed in
    step s5, and Eisenbud and Van de Ven's Proposition 6 is an independent
    published statement of the same answer for a smooth rational curve of
    degree at least 3 on a smooth quadric, over a field of characteristic 0 as
    that paper assumes. Part (b), as this event now states and at first stated
    wrongly: Yang's 5.2.17(b) is a published argument in every characteristic
    except 2 and 3, and Eisenbud and Van de Ven, Proposition 6 at n = 4, gives
    l = m = -7 in characteristic 0. This event at first called Yang's argument
    complete in characteristic 2 as well, and that is withdrawn: his
    presentation is not the conormal's in characteristic 2, his own matrix for
    the twisted cubic there having kernel R(-6) + R(-4) where the printed answer
    is O(-5) squared, so the method fails at a case whose answer is known.
    Comparable, and also withdrawn here: the earlier reading that the reduction
    of step s5 is Shifrin's. It is the card's own, his answer leaving the row
    and column operations as an exercise and printing the diagonal
    (-3t^{-5}, -(1/3)t^{-5}), a form whose constants need 3 invertible; what is
    his is the two frames and their transition matrix, and the page of his
    sketch quoted at step s1 is p. 460 and not p. 459. The correction of the
    second elementary
    operation of step s5 was written the wrong way round, as adding -2t^{-1}
    times the FIRST column to the SECOND, which leaves the entry -2t^{-6} and
    does not reduce the matrix; the operation that does reduce it, and the one
    now stated, is adding -2t^{-1} times the SECOND column to the FIRST, over
    k[t^{-1}], which leaves t^{-5} times the identity. The event of 2026-11-16
    above states the earlier direction and is left as it was written. Part (b)
    in characteristics 2 and 3 has no published proof in the sources read, and
    the card's own step s3, the extension class (n-1) eta, is what decides it;
    a COMPLAINTS record of this date names that. Not checked: no source beyond
    the three named and the book was read in this pass, and no machine
    computation was run.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report on the transcription, and three repairs. (i) The
    characteristic-3 sentence of step s5 was wrong and is gone. It read the
    matrix mod 3 as [[0,-t^-4],[-t^-6,t^-5]] where the reduction of
    [[-3t^-5,-2t^-4],[2t^-6,t^-5]] mod 3 is [[0,t^-4],[-t^-6,t^-5]], since
    -2 = 1 there, and it then had "t times the second row added to the first"
    giving (-1,0), which that operation does not give: it gives
    (-t^-5, 2t^-4). The step now records the reduction as the identity
    M = t^-5 A B over Z[t,t^-1] with A = [[1,-2t],[0,1]] and
    B = [[1,0],[2t^-1,1]], both of determinant one, A over k[t] and B over
    k[t^-1], which is characteristic-free and needs no case check; the two
    elementary operations written above it are that identity's factors, and
    the characteristic-2 observation, that the matrix is then already t^-5
    times the identity, stands. (ii) Part (a) was called published without
    restriction in the solution's preamble and in the remark, and no cited
    source covers it in characteristic 3: Shifrin's answer ends at the diagonal
    (-3t^-5,-(1/3)t^-5), whose constants need 3 invertible, Eisenbud and Van de
    Ven's introduction assumes a field of characteristic 0, and Yang's
    presentation gives the twisted cubic's conormal only away from
    characteristic 2, as the remark itself states. The preamble and the remark
    now restrict each attribution: Shifrin in a form whose constants need 3
    invertible, Yang for (a) away from characteristic 2 and for (b) away from
    characteristics 2 and 3, Eisenbud and Van de Ven in characteristic 0. Part
    (a) in characteristic 3 is therefore without a published proof, and a
    COMPLAINTS record of this date for this batch names it; on the card it is
    step s3's class eta, which is nonzero over every field, with steps s2 and
    s4, and those steps are marked as this card's. (iii) Out of the remark went
    the sentences that stated publication status and the card's own share of
    the argument --- that part (b) is "without a published argument" in
    characteristics 2 and 3, and that the reduction of Shifrin's matrix is "the
    card's own, as is its check in characteristics 2 and 3" --- since a mark of
    a step as the card's own belongs on the step, where steps s2, s3, s4 and s5
    carry it, and not on the rendered page; and out of the preamble and the
    remark went the tmp/sources paths, which are this VM's bookkeeping. What
    was read for this pass, and where: Shifrin's answer 1583486 to question
    1583326 in
    tmp/sources/mse-1583326-hart77-v217-twisted-cubic-normal-bundle.md;
    Yang Pi-Yeh's Solution 5.2.17 in tmp/sources/lfwin-hartshorne-solutions.md,
    printed pp. 106--107; Eisenbud and Van de Ven in
    tmp/sources/eisenbud-van-de-ven-1981-normal-bundles-rational-space-curves.md
    beside its PDF, whose introduction, printed p. 453, states the
    characteristic-0 hypothesis and whose Proposition 6 is on the folio
    numbered 458 with its proofs on pp. 458--460; and the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, V.2.17 on printed
    pp. 385--386 with its answer on p. 386. Not checked: no search was made for
    a published computation of the conormal sheaf of the twisted cubic in
    characteristic 3 beyond the three sources above, and no machine computation
    was run; the card's proof of part (a) in characteristic 3 is unchanged and
    remains its own.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's second report on this card, and two repairs. (i) The preamble
    said Yang Pi-Yeh's Jacobian presentation "settles (a) in every
    characteristic other than 2", which includes characteristic 3, and the
    event above and the COMPLAINTS record of this date both say that no cited
    source covers part (a) in characteristic 3. The two cannot both hold, and
    the preamble no longer makes the claim: it now attributes to him part (b)
    in every characteristic other than 2 and 3, which is what his own text
    states and what his characteristic-2 collapse shows. The clause of the
    event above that reads "Yang for (a) away from characteristic 2" is
    superseded here; the remark's sentence about his twisted cubic now reports
    his presentation and his kernel as he writes them, rather than concluding
    from them that the conormal of part (a) is O(-5) + O(-5), so nothing on the
    card asserts a published proof of part (a) in characteristic 3. (ii) The
    identity M = t^-5 A B over Z[t,t^-1], with the two matrices displayed, is
    withdrawn from step s5, together with the sentence that read it as holding
    over every field and covering characteristic 3. The identity is correct and
    the reduction it formalises is the card's own work of this round; but part
    (a) in characteristic 3 has no published proof, and the round's rule is
    that a proof of such a part already on the card stays marked as the card's
    own and no new one is written. The card's proof of part (a) in every
    characteristic is steps s2 to s4, unchanged: the extension class is
    (n-1) eta, and at n = 2 that is eta, nonzero over every field, so step s4
    gives E_2 = O(-5) + O(-5). What step s5 keeps is Shifrin's two frames, the
    change of coordinates and the transition matrix, his own conclusion in the
    form he prints it, whose constants need 3 invertible, and the card's two
    elementary operations on the matrix, marked there as the card's own.
    Nothing else on the card changed. Not checked: no further search for a
    published proof of part (a) in characteristic 3, and the withdrawal rests
    on the sources read above, not on a computation of this card's own.
- event: source-corrected
  by: claude
  date: 2026-11-17
  note: >-
    Markup only, no change of statement or proof, and no new macro. The card
    wrote the restriction of the tangent sheaf of $\PP^3$ to $C$ in Yang
    Pi-Yeh's quoted conormal sequence as `\mathcal T_{\PP^3}\restrictof_C`, and
    twice wrote `\Omega^1\PP^3\restrictionof_C` and
    `\Omega_{\PP^3}\restrictionof_C` for the same construction; `qualc check` reported the first as a command
    neither the preamble nor MathJax defines. The preamble's macro for this
    meaning is `\restrictionof{A}{B}`, which sets $\left.A\right|_B$ and which
    the corpus uses on 70 cards; `\restrictof` is one character away from it
    and occurs nowhere else in the corpus, so this was a mistyped use of that
    macro rather than a second meaning, and no macro was added for it. The
    three spans now read $\restrictionof{\mathcal T_{\PP^3}}{C}$,
    $\restrictionof{\Omega^1\PP^3}{C}$ and
    $\restrictionof{\Omega_{\PP^3}}{C}$. The postfix form was not merely
    undefined: TeX takes its first argument to be the `_` of the subscript and
    its second to be the subscript's letter, which the preamble's definition
    rejects with "Missing { inserted"; typesetting that definition beside the
    three spans with `pdflatex` produced a fatal error before the repair and a
    PDF after it. Not checked: the rendered page in a browser, and no
    mathematics was read or altered by this repair.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Part (b) in characteristics 2 and 3, the part of this card that #160
    records as open. Read for it: Hartshorne, Algebraic Geometry (1977),
    V.2.17, printed p. 386, with the printed Answer "If char k neq 2, then
    l = m = -7; if char k = 2, then l, m = -6, -8" (text version
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N is
    PDF p. N+15 and the exercise stands under the marker of PDF p. 401).
    Checked against the card's own step s3, line by line: with q = c - ab and
    h = b - a^n, the substitutions b = a^n + h and c = a^{n+1} + ah + q give
    a c^{n-1} - b^n = -a^{n^2-n}h + (n-1)a^{n^2-n-1}q modulo (q,h)^2 and
    c^n = a^{n^2+n}, so h' = -s^{-2n}h + (n-1)s^{-2n-1}q; after the diagonal
    transition factors the class is (n-1)eta, a generator of
    H^1(P^1,O(-2)) multiplied by n-1. For n = 3 this is 2eta, zero exactly
    when 2 = 0: characteristic 3 gives the non-split O(-7) + O(-7), the
    book's answer for char k neq 2, and characteristic 2 gives the split
    O(-6) + O(-8) by step s4. The card's own proof therefore decides both
    characteristics and agrees with the printed answer. No published proof
    of them is claimed: Yang Pi-Yeh, Solution 5.2.17, printed p. 107, is
    sound away from 2 and 3, is wrong in characteristic 3 (he prints the
    split answer there), and his Jacobian presentation is not the conormal's
    in characteristic 2, as the remark says. Not checked: the card's other
    steps were not re-derived in this pass; only step s3's computation was
    verified line by line.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Characteristics 2 and 3 re-checked, and the splitting settled without the
    splitting theorem, so that the row of issue #160 for this exercise is met.
    Step s3's substitution was redone by hand from b = a^n + h and
    c = a^{n+1} + ah + q: c^{n-1} = a^{n^2-1} + (n-1)a^{n^2-n-2}(ah+q) and
    (a^n+h)^n = a^{n^2} + n a^{n^2-n}h, so the numerator is
    -a^{n^2-n}h + (n-1)a^{n^2-n-1}q, and dividing by c^n congruent to
    a^{n^2+n} gives h' congruent to -s^{-2n}h + (n-1)s^{-2n-1}q; the class is
    (n-1)s^{-1} in H^1(O(-2)), whose generator is s^{-1}. Hence n = 3 gives
    2s^{-1}, nonzero in characteristic 3 and zero in characteristic 2, which is
    l = m = -7 in characteristic 3 as the printed answer on p. 386 says and
    O(-6) + O(-8) in characteristic 2. The transition identity was also checked
    mechanically over Z in the truncated ring Z[a^{+-1},h,q]/(h,q)^2 for
    n = 2,...,7, and the splitting follows from it by an explicit change of
    frames rather than from Birkhoff-Grothendieck: with c = n-1 nonzero,
    M = s^{-2n-1}AB where A = [[c,0],[-s,1]] has determinant c and entries in
    k[s], and B = [[s^{-1}/c,1],[1/c,0]] has determinant -1/c and entries in
    k[s^{-1}], so the frames over the two charts can be changed to make the
    gluing scalar. Yang Pi-Yeh, Hartshorne Solutions, Solution 5.2.17(b),
    printed p. 107, prints "If char(k) = 2,3, F(phi) is given by (t^3,u^3,0).
    So ker F(phi) = R(-8) + R(-6)", and the characteristic 3 half of that
    sentence is false by the computation above; its characteristic 2 half
    agrees with the book although the degenerate row it comes from also gives
    O(-4) + O(-6) for part (a) in characteristic 2, where the answer is
    O(-5) + O(-5). Read for this pass: Hartshorne V.2, exercise 2.17 with its
    printed answer, printed pp. 385-386, and Yang's Solution 5.2.17 in
    tmp/sources/lfwin-hartshorne-solutions.md. Not checked: any printing other
    than the text versions, and steps s1, s2, s4, s5 and s6 were read for their
    field hypotheses only, not re-derived.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Two claims about the cited sources were wrong, and the mathematics of no
    step changes. (i) The remark said Yang Pi-Yeh writes the twisted cubic's
    presentation as R(-4)^{oplus3} -> R(-2)^{oplus4}. Read on printed p. 107
    (PDF p. 107, the folio printed at the foot, of
    tmp/sources/lfwin-hartshorne-solutions.pdf) he writes two maps: the
    Jacobian matrix F(kappa): R(-4)^{oplus3} -> R(-3)^4, a 4-by-3 matrix, and
    F(phi): R(-4)^{oplus3} -> R(-2) given by (t^2, u^2, 2tu), and it is the
    kernel of the second that he takes, getting R(-5)^{oplus2}. "R(-2)^{oplus4}"
    occurs nowhere in his text, and a target of a 3-generator presentation does
    not have that form. The remark now gives both maps. (ii) The solution's
    preamble gave Eisenbud and Van de Ven's Proposition 6 as on printed p. 458
    "with its proofs on pp. 458--460". The statement of Proposition 6 is the
    last item on printed p. 458 (the page carries no proof text after it) and
    "Proof of Proposition 6" opens printed p. 459, with the algebraic sketch on
    p. 460; the range now reads pp. 459--460. The dated event above that says
    "numbered 458 with its proofs on pp. 458--460" is left as written. Read for
    this event: the two Yang pages at the text layer of the retained PDF, the
    Eisenbud--Van de Ven pages 5 to 8 of the retained PDF (folios 457 to 460),
    and the card. Checked on the card alone: qualc.authoring check,
    "schema and Markdown parsing OK (single card)", and tools/check_macros.py,
    both exit 0. Not checked: the printed copies, and no other page of either
    paper.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #164, the reader's third NOT MET item, does not hold, and no
    mathematical change follows from it. The reader reads Proposition 6 as
    assuming degree n > 3; the printed statement assumes n >= 3. PDF p. 6 of
    tmp/sources/eisenbud-van-de-ven-1981-normal-bundles-rational-space-curves.pdf,
    folio 458, was rendered at 600 dpi and read as an image: "Proposition 6. A
    smooth rational space-curve C of degree n >= 3 which is contained in a
    smooth quadric has normal bundle N_C = O(2n-1) + O(2n-1)." The glyph is the
    two-stroke greater-or-equal, and the text layer prints ">" because the
    lower bar is dropped in extraction, which is what the reader read. The
    paper also treats degree 3 in its own right: Section 2, "Realising the
    Splitting of the Normal Bundle", printed p. 462, opens "Let C be a smooth
    rational curve of degree 3" and states "In fact, N = O_c(5) + O_c(5)". The
    introduction's n >= 4 is qualified as not holding for the auxiliary curves
    and is not the hypothesis of the proposition. Lines 371 and 707 therefore
    stand, and the application at n = 3 is the paper's degree 3, which is the
    card's n = 2 for the twisted cubic. Not checked: the printed journal, only
    the retained PDF.
- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    One arithmetic sentence repaired, with no change to the computation or the
    answer. Step s1's closing paragraph compared its degree with "the value
    deg c_1(N) = 4n-2 that Eisenbud and Van de Ven record for a smooth rational
    curve of degree n", which mixes two meanings of n: the paper's n is the
    degree of the curve, while in this card the curve C_n has degree n+1. With
    deg E_n = -(2n+2) - 2n = -4n-2, the normal bundle has degree 4n+2, which is
    4(n+1)-2, the paper's value at the card's degree. The sentence now says
    that. Read for it: the extension 0 -> O(-2n-2) -> E_n -> O(-2n) -> 0 of
    step s1 and the value 4d-2 from deg c_1(PP^3) = 4 and deg c_1(PP^1) = 2.
    Not read in this pass: Eisenbud and Van de Ven's Proposition 6 in the
    original, only as this card records it.
- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Two open items recorded and closed. (i) As the card stood at 3c27927314,
    line 520 drew the conormal sequence of C_n in Q in P^3 with no argument
    for its exactness on the left, though step s2 subtracts the two degrees in
    it. Step s2 now derives it: the two inclusions are regular immersions of
    codimension 1 between nonsingular varieties, so Theorem II.8.17 gives
    0 -> I_Q/I_Q^2 -> Omega_{P^3} tensor O_Q -> Omega_Q -> 0 and the same for
    C_n exact with locally free left terms, and tensoring the first by O_{C_n}
    and applying the theorem again to C_n in Q identifies I_Q/I_Q^2 restricted
    to C_n with the kernel of I_{C_n}/I_{C_n}^2 -> I_{C_n/Q}/I_{C_n/Q}^2. (ii)
    At line 683 the proof read the extension class (n-1)eta off the transition
    matrix with no statement of why a matrix entry is the class. Step s3 now
    gives the two inputs: Chapter III §6 Exercise 1, that extensions are
    classified by Ext^1 and that on a two-chart cover the class is the Čech
    class of the transition matrix with the diagonal entries removed; and
    Theorem III.5.1(c) with its proof, that H^1(P^1, O(-2)) is one-dimensional
    with basis the negative monomial x_0^{-1}x_1^{-1}, which is s^{-1} in the
    frame of the diagonal factor s^{-2}; so the class is (n-1)eta with eta
    nonzero and vanishes exactly when n-1 = 0 in k. Read for this: Theorem
    II.8.17 and Proposition II.8.12, Chapter III §6 Exercise 1, and Theorem
    III.5.1 with its proof, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md. No step's computation
    changed, and no claim was weakened; the answers O(-7)^2 away from
    characteristic 2 and O(-6) + O(-8) in characteristic 2 stand. Not read:
    any printing of the book, only the text version in tmp/sources.
- event: source-checked
  by: claude
  date: 2026-11-22
  note: >-
    Published-solution pass for issue #160, on the transcription rule. Part (b)
    in characteristics 2 and 3 is proved by no retained solution set, and the
    "Published solution" remark now says so and names the sets searched. Read
    in this pass, at their own numbering: the printed Exercise V.2.17, both
    parts, with the printed answer "if char k != 2, then l = m = -7; if
    char k = 2, then l, m = -6, -8"; Yang Pi-Yeh, Solution 5.2.17, whose
    Jacobian presentation gives kernel R(-7) + R(-7) when 6 != 0 and
    R(-8) + R(-6) when char k = 2, 3, so it settles every characteristic but 2
    and 3; Egbert's entry for Exercise V.2.17, which reads only "starred"; the
    exercise list of the National Taiwan University Chapter V §2 homework,
    whose entries are exercises 1, 2, 3, 4 and 6, so that it has none for
    Exercise 17; and, for absence, Borcherds (through IV.1), Cais (through
    Chapter 4), Cutrone--Marshburn (Chapters 1 and 2), Ionita--Kumar
    (Chapter I), Kim (§2.4), Lomont, Okamoto (§II.9), Park (Chapter 4 and §V.5), Saglam--Chris
    (Chapter III), Sam (through IV.6), Stein (III.7), Troiani (Chapter II) and
    Reiser (IV.2.5). The remark now states that the argument in characteristics
    2 and 3 is step s3, the card's own. No statement and no proof step changed
    in this pass. Not read in this pass: Shifrin's and Elencwajg's answers
    beyond the sentences the card quotes, Eisenbud and Van de Ven's
    Proposition 6 other than as the remark records it, and any printing of
    Hartshorne, only the text version in tmp/sources.

---

::: {.problem}
(a) Let $\varphi: \PP_k^1 \rightarrow \PP_k^3$ be the 3-uple embedding (I, Ex. 2.12). Let $\mathcal{I}$ be the sheaf of ideals of the twisted cubic curve $C$ which is the image of $\varphi$. Then $\mathcal{I} / \mathcal{I}^2$ is a locally free sheaf of rank 2 on $C$, so $\varphi^*\left(\mathcal{I} / \mathcal{I}^2\right)$ is a locally free sheaf of rank 2 on $\PP^1$.
  By (2.14), therefore,
  $$
\varphi^*\left(\mathcal{I} / \mathcal{I}^2\right) \cong \OO(l) \oplus \OO(m)
  .$$
  for some $l, m \in \ZZ$. Determine $l$ and $m$.

(b) Repeat part (a) for the embedding $\varphi: \PP^1 \rightarrow \PP^3$ given by $x_0=t^4$, $x_1=t^3 u$, $x_2=t u^3$, $x_3=u^4$, whose image is a nonsingular rational quartic curve.

  Answer: If $\operatorname{char} k \neq 2$, then $l=m=-7$; if $\operatorname{char} k=2$, then $l, m=-6,-8$.
:::

::: {.solution}
A step that transcribes a published argument names the source and numbered statement it comes from; a step no source carries is marked as this card's. Ted Shifrin, Math StackExchange answer 1583486 to question 1583326, *Normal bundle of twisted cubic*, for (a) by transition functions, in a form whose constants need $3$ invertible; Yang Pi-Yeh, *Hartshorne Solutions*, Solution 5.2.17, for both parts by the Jacobian presentation, which settles (b) in every characteristic other than $2$ and $3$; and D. Eisenbud and A. Van de Ven, *On the Normal Bundles of Smooth Rational Space Curves*, Math. Ann. 256 (1981), 453--463, Proposition 6, for the normal bundle of a smooth rational curve of degree $n\ge3$ lying on a smooth quadric, over a field of characteristic $0$ as the paper assumes.

For $n\ge2$, consider the parametrized rational curve
$$
\varphi_n:\PP^1\longrightarrow\PP^3,
\qquad
[t:u]\longmapsto
[t^{n+1}:t^nu:tu^n:u^{n+1}].
$$
Thus $n=2$ is the twisted cubic of part (a), and $n=3$ is the quartic of
part (b).

::: pf

::: {.pf-step #s1}

The image $C_n$ lies on the smooth quadric
$$
Q=V(x_0x_3-x_1x_2)\subseteq\PP^3,
$$
and under
$$
Q\cong\PP^1\times\PP^1
$$
it is the graph of the power map
$$
[t:u]\longmapsto[t^n:u^n].
$$

::: pf-proof

The parametrization satisfies

$$
x_0x_3-x_1x_2
=
t^{n+1}u^{n+1}-t^nu\,tu^n
=0.
$$
The quadric is smooth because the four partial derivatives of its equation
are
$$
x_3,\qquad -x_2,\qquad -x_1,\qquad x_0,
$$
which have no common projective zero.

Eisenbud and Van de Ven, *Sketch of an Algebraic Proof of Proposition 6*, put the same reduction in published form: "Suppose $C$ is contained in the quadric $x_0x_2-x_1x_3=0$. Realising $C$ as the graph of an $(n-1)$-to-$1$ map, we may write it parametrically as $\PP^1\ni(s,t)\mapsto(p_0,p_1,p_2,p_3)\in\PP^3$, where each $p_i$ is a form of degree $n$ in 2 variables, and $p_0=sp$, $p_1=sq$, $p_2=tp$, $p_3=tq$ for some relatively prime forms $p$ and $q$", their quadric being this one after a permutation of coordinates.

Using the Segre coordinates
$$
[a:b]\times[c:d]
\longmapsto
[ac:ad:bc:bd],
$$
the curve is obtained by
$$
[a:b]=[t^n:u^n],
\qquad
[c:d]=[t:u].
$$
The second projection therefore identifies $C_n$ with $\PP^1$, even when
the first power map is inseparable.

:::

:::

::: {.pf-step #s2}

Let
$$
E_n=\varphi_n^*(\mathcal I_{C_n}/\mathcal I_{C_n}^2).
$$
There is an exact sequence
$$
\boxed{
0\longrightarrow\OO_{\PP^1}(-2n-2)
\longrightarrow E_n
\longrightarrow\OO_{\PP^1}(-2n)
\longrightarrow0.}
$$

::: pf-proof

This step and the next two are this card's own general computation for every $n$, and no source carries them; the degree they give agrees with the value $\deg c_1(N)=4d-2$ that Eisenbud and Van de Ven record for a smooth rational curve of degree $d$ in $\PP^3$, from $\deg c_1(\PP^3)=4$ and $\deg c_1(\PP^1)=2$, at $d=n+1$: here $\deg E_n=-4n-2$, the sum of the two degrees in the displayed sequence, so $\deg N=4n+2=4(n+1)-2$.

For the regular immersions
$$
C_n\subset Q\subset\PP^3,
$$
the conormal sequence is
$$
0
\longrightarrow
\mathcal I_Q/\mathcal I_Q^2\restrict_{C_n}
\longrightarrow
\mathcal I_{C_n}/\mathcal I_{C_n}^2
\longrightarrow
\mathcal I_{C_n/Q}/\mathcal I_{C_n/Q}^2
\longrightarrow0.
$$

The sequence is exact on the left as well, and its left term is locally free of rank $1$: $C_n$ and
$Q$ are nonsingular and the two inclusions are regular immersions of codimension $1$, so Theorem
II.8.17 gives
$$
0\to\mathcal I_Q/\mathcal I_Q^2\to\Omega_{\PP^3/k}\tensor\OO_Q\to\Omega_{Q/k}\to0,
\qquad
0\to\mathcal I_{C_n}/\mathcal I_{C_n}^2\to\Omega_{\PP^3/k}\tensor\OO_{C_n}\to\Omega_{C_n/k}\to0
$$
exact with locally free left terms; tensoring the first by $\OO_{C_n}$, and applying the theorem again
to $C_n\subset Q$, whose conormal sheaf is $\mathcal I_{C_n/Q}/\mathcal I_{C_n/Q}^2$, identifies
$\restrictionof{\mathcal I_Q/\mathcal I_Q^2}{C_n}$ with the kernel of
$\mathcal I_{C_n}/\mathcal I_{C_n}^2\to\mathcal I_{C_n/Q}/\mathcal I_{C_n/Q}^2$, which is the
displayed sequence.

The quadric is a hypersurface of degree $2$, so
$$
\mathcal I_Q/\mathcal I_Q^2\restrict_{C_n}
\cong
\OO_{C_n}(-2).
$$
Since
$$
\varphi_n^*\OO_{\PP^3}(1)=\OO_{\PP^1}(n+1),
$$
its pullback is
$$
\OO_{\PP^1}(-2n-2).
$$

As a divisor on $Q\cong\PP^1\times\PP^1$, the graph $C_n$ has type
$(1,n)$, hence
$$
C_n^2=2n.
$$
Therefore
$$
\mathcal I_{C_n/Q}/\mathcal I_{C_n/Q}^2
\cong
\OO_{C_n}(-C_n)
\cong
\OO_{\PP^1}(-2n).
$$
Pulling the conormal sequence back along the isomorphism
$\varphi_n:\PP^1\xrightarrow{\sim}C_n$ gives the displayed sequence.

:::

:::

::: {.pf-step #s3}

The extension class of step [](#s2){.pf-ref} is
$$
\boxed{(n-1)\eta}
$$
where
$$
0\ne\eta\in H^1(\PP^1,\OO_{\PP^1}(-2))
$$
is a generator.

::: pf-proof

Use the affine chart $x_0\ne0$ with coordinates
$$
a=\frac{x_1}{x_0},
\qquad
b=\frac{x_2}{x_0},
\qquad
c=\frac{x_3}{x_0}.
$$
Put
$$
q=c-ab,
\qquad
h=b-a^n.
$$
Then $q,h$ generate the ideal of $C_n$ on this chart. Along the
parametrization, with
$$
s=\frac ut,
$$
one has
$$
a=s,
\qquad
b=s^n,
\qquad
c=s^{n+1}.
$$

On the chart $x_3\ne0$, put
$$
\alpha=\frac{x_1}{x_3},
\qquad
\beta=\frac{x_2}{x_3},
\qquad
\gamma=\frac{x_0}{x_3},
$$
and take generators
$$
q'=\gamma-\alpha\beta,
\qquad
h'=\alpha-\beta^n.
$$
On the overlap,
$$
\alpha=\frac a c,
\qquad
\beta=\frac b c,
\qquad
\gamma=\frac1c.
$$
Thus, modulo the square of the ideal $(q,h)$,
$$
q'=\frac{q}{c^2}
\equiv
s^{-2n-2}q.
$$

For the second generator,
$$
h'
=
\frac{a c^{n-1}-b^n}{c^n}.
$$
Substitute
$$
b=a^n+h,
\qquad
c=ab+q=a^{n+1}+ah+q
$$
and retain only terms linear in $q,h$. The numerator becomes
$$
-a^{n^2-n}h
+
(n-1)a^{n^2-n-1}q
\pmod{(q,h)^2}.
$$
Since $c^n\equiv a^{n^2+n}$ to zeroth order, one gets
$$
h'
\equiv
-s^{-2n}h
+
(n-1)s^{-2n-1}q
\pmod{(q,h)^2}.
$$

The diagonal factors
$$
s^{-2n-2},
\qquad
s^{-2n}
$$
are precisely the transition functions of the two line bundles in step
[](#s2){.pf-ref}. After factoring them out, the off-diagonal term is represented by
$$
(n-1)s^{-1}.
$$
On the standard two-chart cover of $\PP^1$, $s^{-1}$ represents a generator
of
$$
H^1(\PP^1,\OO(-2)).
$$
Hence the extension class is $(n-1)\eta$.

The passage from the transition matrix to the class is what makes the computation above a
computation of the class rather than of a matrix, and it has two parts. First, for an extension of one
invertible sheaf by another over a two-element affine cover, the extension class in
$\Ext^1(\OO(-2n),\OO(-2n-2))$ is the Čech class of the transition matrix written in frames of the two
end terms, with the diagonal entries — the transition functions of those two sheaves — removed: this
is Chapter III §6 Exercise 1, extensions of $\OO(-2n)$ by $\OO(-2n-2)$ being classified by that
group, read in Čech cohomology for the cover. Second, that group is $H^1(\PP^1,\OO(-2))$, and in the
frames of the diagonal factors $s^{-2n-2}$ and $s^{-2n}$ the entry $(n-1)s^{-1}$ is $(n-1)$ times the
negative monomial $x_0^{-1}x_1^{-1}$, which generates $H^1(\PP^1,\OO(-2))\cong k$ by Theorem
III.5.1(c) and its proof. So the class is $(n-1)\eta$ with $\eta\ne0$, and it vanishes exactly when
$n-1=0$ in $k$.

:::

:::

::: {.pf-step #s4}

If the extension class in step [](#s3){.pf-ref} is zero, then
$$
E_n
\cong
\OO(-2n)\oplus\OO(-2n-2).
$$
If it is nonzero, then
$$
\boxed{E_n\cong\OO(-2n-1)\oplus\OO(-2n-1).}
$$

::: pf-proof

The zero-class assertion is exactly the definition of a split extension.
This step is also this card's own; it is the Birkhoff--Grothendieck argument that turns the extension class of step [](#s3){.pf-ref} into a splitting type.


Assume the class is nonzero and twist the exact sequence of step [](#s2){.pf-ref} by
$\OO(2n)$:
$$
0
\longrightarrow
\OO(-2)
\longrightarrow
E_n(2n)
\longrightarrow
\OO
\longrightarrow0.
$$
Its connecting map
$$
H^0(\OO)\longrightarrow H^1(\OO(-2))
$$
is the nonzero extension class. Both spaces are one-dimensional, so this map
is an isomorphism. Consequently
$$
H^0(E_n(2n))=0.
$$

By Birkhoff--Grothendieck, write
$$
E_n\cong\OO(l)\oplus\OO(m),
\qquad
l\ge m.
$$
Step [](#s2){.pf-ref} gives
$$
l+m=-4n-2.
$$
The vanishing of $H^0(E_n(2n))$ implies
$$
l+2n<0,
$$
so
$$
l\le-2n-1.
$$
But $l$ is at least the average $(l+m)/2=-2n-1$. Hence
$$
l=m=-2n-1.
$$

:::

:::

::: {.pf-step #s5}

For the twisted cubic,
$$
\boxed{l=m=-5.}
$$

::: pf-proof

Eisenbud and Van de Ven, Proposition 6: "A smooth rational space-curve $C$ of degree $n\ge3$ which is contained in a smooth quadric has normal bundle $N_C\cong\OO_C(2n-1)\oplus\OO_C(2n-1)$", over a field of characteristic $0$ as their introduction assumes. At $n=3$ that is $N\cong\OO(5)\oplus\OO(5)$, that is $l=m=-5$.

Here $n=2$. By step [](#s3){.pf-ref} the extension class is
$$
(2-1)\eta=\eta\ne0
$$
over every field. Step [](#s4){.pf-ref} therefore gives
$$
E_2\cong\OO(-5)\oplus\OO(-5).
$$
This proves part (a).

The same splitting is read off the transition matrix of the conormal bundle, and
the two computations are independent. The two frames and their relation are
Ted Shifrin's, answer 1583486, part (a): he writes the conormal sequence
$0\to N^*_{C/\PP^3}\to\restrictionof{\Omega^1\PP^3}{C}\to\Omega^1_C\to0$, the images
of the three coordinate differentials in each of the two charts, and the two
sections of the conormal bundle that the relations leave. What is this card's
own is the reduction of his matrix, which his answer leaves as "the usual row-
and column-operation (Smith normal form) game" and states as the diagonal
$(-3t^{-5},-\frac13t^{-5})$, a form whose constants need $3$ invertible. On the
chart $x_0\ne0$, with affine
coordinates $x,y,z$ and parametrization $(t,t^2,t^3)$, the conormal bundle is
generated by
$$
\sigma_1=-2t\,dx+dy,
\qquad
\sigma_2=-3t^2\,dx+dz,
$$
and on the chart $x_3\ne0$, with affine coordinates $X=x_0/x_3$,
$Y=x_1/x_3$, $Z=x_2/x_3$ and parametrization $(s^3,s^2,s)$, it is generated by
$$
\tau_1=-3t^{-5}dy+2t^{-6}dz,
\qquad
\tau_2=t^{-3}dx-2t^{-4}dy+t^{-5}dz.
$$

The change of coordinates is
$$
X=\frac1z,
\qquad
Y=\frac xz,
\qquad
Z=\frac yz,
$$
so that
$$
dX=-\frac{dz}{z^2},
\qquad
dY=\frac{z\,dx-x\,dz}{z^2},
\qquad
dZ=\frac{z\,dy-y\,dz}{z^2}.
$$
On $C$ one has $x=t$, $y=t^2$, $z=t^3$ and $s=t^{-1}$, so $z^{-1}=t^{-3}$ and
$z^{-2}=t^{-6}$, and the two relations of the second chart become
$$
dX-3Z^2dZ=-t^{-6}dz-3t^{-2}\left(t^{-3}dy-t^{-4}dz\right)
=-3t^{-5}dy+2t^{-6}dz=\tau_1
$$
and
$$
dY-2Z\,dZ=\left(t^{-3}dx-t^{-5}dz\right)-2t^{-1}\left(t^{-3}dy-t^{-4}dz\right)
=t^{-3}dx-2t^{-4}dy+t^{-5}dz=\tau_2 .
$$
Hence
$$
(\tau_1,\tau_2)=(\sigma_1,\sigma_2)
\begin{pmatrix}
-3t^{-5} & -2t^{-4}\\
2t^{-6} & t^{-5}
\end{pmatrix}.
$$

The matrix relates the two frames, so a change of the first frame is a row
operation and a change of the second is a column operation on it: replacing
$(\sigma_1,\sigma_2)$ by $(\sigma_1,\sigma_2)S$ with $S\in\GL_2(k[t])$,
which is a change of frame over the chart $x_0\ne0$ whose coordinate ring is
$k[t]$, replaces $M$ by $S^{-1}M$, and replacing $(\tau_1,\tau_2)$ by
$A(\tau_1,\tau_2)$ with $A\in\GL_2(k[t^{-1}])$, a change of frame over
$x_3\ne0$, replaces $M$ by $MA$. The row operations are therefore over $k[t]$
and the column operations over $k[t^{-1}]$.

Two of them reduce the matrix. Adding $2t$ times the second row to the first, a
row operation over $k[t]$, gives
$$
\begin{pmatrix}
t^{-5} & 0\\
2t^{-6} & t^{-5}
\end{pmatrix},
$$
and adding $-2t^{-1}$ times the second column to the first, a column operation
over $k[t^{-1}]$, gives
$$
t^{-5}
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}.
$$
So the conormal sheaf is $\OO(-5)\oplus\OO(-5)$ and $l=m=-5$. The two operations above are elementary, with determinant one, the first over $k[t]$ and the second over $k[t^{-1}]$; in characteristic $2$ the matrix is already $t^{-5}$ times the identity.

:::

:::

::: {.pf-step #s6}

For the rational quartic,
$$
\boxed{
E_3\cong
\begin{cases}
\OO(-7)\oplus\OO(-7),&\operatorname{char}k\ne2,\\
\OO(-6)\oplus\OO(-8),&\operatorname{char}k=2.
\end{cases}}
$$

::: pf-proof

Here $n=3$. Step [](#s3){.pf-ref} gives extension class
$$
2\eta.
$$
If $\operatorname{char}k\ne2$, this is nonzero, and step [](#s4){.pf-ref} gives
$$
E_3\cong\OO(-7)\oplus\OO(-7).
$$
If $\operatorname{char}k=2$, the class vanishes, so the sequence splits:
$$
E_3
\cong
\OO(-6)\oplus\OO(-8).
$$
This is exactly the answer stated in part (b).

The published argument for the same splitting is Yang Pi-Yeh, Solution 5.2.17(b): he computes it by the Jacobian presentation, "If $\operatorname{char}(k)\ne2,3$, all things are like (a). So $0\to\mathcal T_C\xrightarrow{\phi}\restrictionof{\mathcal T_{\PP^3}}{C}\to\mathcal N_C\to0$, and $F(\phi):R(-5)\oplus R(-5)\oplus R(-6)\to R(-2)$ given by matrix $(t^3,u^3,6t^2u^2)$. So here $\ker F(\phi)=R(-7)\oplus R(-7)$, i.e. $\varphi^*(\mathcal I/\mathcal I^2)=\OO_{\PP^1}(-7)\oplus\OO_{\PP^1}(-7)$. If $\operatorname{char}(k)=2,3$, $F(\phi)$ is given by $(t^3,u^3,0)$. So $\ker F(\phi)=R(-8)\oplus R(-6)$." That is a published argument for every characteristic other than $2$ and $3$, and it agrees with Eisenbud and Van de Ven, Proposition 6, which at $n=4$ gives $N\cong\OO(7)\oplus\OO(7)$, that is $l=m=-7$, in characteristic $0$. Its characteristic $3$ is wrong, the book printing the split case at $\operatorname{char}k=2$ alone; and its characteristic $2$ cannot be trusted either, since the presentation it uses is not the conormal's there: for the twisted cubic its matrix $(t^2,u^2,2tu)$ becomes $(t^2,u^2,0)$ in characteristic $2$, whose kernel is $R(-6)\oplus R(-4)$ and not $\OO(-5)^{\oplus2}$, so the method demonstrably fails at the answer the book prints for part (a). In neither characteristic does a published argument decide part (b); the class of step [](#s3){.pf-ref}, $2\eta$, does, and it vanishes exactly when $2=0$.

So part (b) is published in characteristic $0$ and in every characteristic other than $2$ and $3$; characteristics $2$ and $3$, and with them the printed answer's "$\operatorname{char}k\ne2$", rest on this card's step [](#s3){.pf-ref}, which is its own.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves part (a), and step [](#s6){.pf-ref} proves part (b).

:::

:::

:::

::: {.remark title="Published solution"}
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.17: the starred exercise is entered and the entry reads only "starred", so there is no argument to check. Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.17, computes the conormal sheaf as the kernel of the map of graded modules given by the Jacobian of the parametrization: for the twisted cubic he writes the Jacobian matrix as $F(\kappa)\colon R(-4)^{\oplus3}\to R(-3)^{\oplus4}$ and the map $F(\varphi)\colon R(-4)^{\oplus3}\to R(-2)$ given by $(t^2,u^2,2tu)$, and takes $\ker F(\varphi)=R(-5)^{\oplus2}$; for the quartic the kernel is $R(-7)^{\oplus2}$ when $6\ne0$, and it writes "if $\operatorname{char}(k)=2,3$, $F(\varphi)$ is given by $(t^3,u^3,0)$, so $\ker F(\varphi)=R(-8)\oplus R(-6)$". That is a sound argument for part (b) in every characteristic other than $2$ and $3$. The extra characteristic is wrong: in step [](#s3){.pf-ref} the extension class is $(n-1)\eta=2\eta$ for $n=3$, which vanishes exactly when $2=0$, and the printed answer for part (b) accordingly says $\operatorname{char}k=2$ and not $2$ or $3$; in characteristic $3$ the binomial coefficient $3$ vanishes in $(a^3+h)^3$, but the class $2\eta$ does not, so the splitting type is $\OO(-7)^{\oplus2}$ there as well. Nor does his characteristic-$2$ line stand: his presentation is not the conormal's in characteristic $2$, where his matrix for the twisted cubic becomes $(t^2,u^2,0)$ with kernel $R(-6)\oplus R(-4)$ instead of the printed $\OO(-5)^{\oplus2}$, so the method fails at a case whose answer is known.

The card's computation is checked against the book's own bracket: $E_n=\varphi_n^*(\mathcal I/\mathcal I^2)$ sits in $0\to\OO(-2n-2)\to E_n\to\OO(-2n)\to0$ with class $(n-1)\eta$, which is nonzero for $n=2$ and gives $l=m=-5$ for the twisted cubic, and for $n=3$ gives $l=m=-7$ when $\operatorname{char}k\ne2$ and $\OO(-6)\oplus\OO(-8)$ when $\operatorname{char}k=2$, exactly the answer printed for part (b).

Math StackExchange answer 1583486 by Ted Shifrin, to question 1583326 ("Normal bundle of twisted cubic"), gives an argument for part (a) by another route, in a form whose constants need $3$ invertible: from the conormal sequence $0\to N^\vee_{C/\PP^3}\to\restrictionof{\Omega_{\PP^3}}{C}\to\Omega_C\to0$ it writes the two frames of $N^\vee_{C/\PP^3}$ on the overlap of the charts $[1,x,y,z]$ and $[X,Y,Z,1]$ and reads the splitting off the transition matrix, ending at the diagonal $(-3t^{-5},-\frac13t^{-5})$. Step [](#s5){.pf-ref} carries his frames, the change of coordinates $X=1/z$, $Y=x/z$, $Z=y/z$ and the transition matrix, and adds one row operation over $k[t]$ and one column operation over $k[t^{-1}]$ that reduce it to exactly $t^{-5}$ times the identity, an identity over $\ZZ[t,t^{-1}]$ and so one that holds over every field. Georges Elencwajg's answer 569653 to question 569237 records the equivalent statement for the normal bundle, $N=\OO(5)\oplus\OO(5)$, as Proposition 6 of Eisenbud and Van de Ven, *On the normal bundles of smooth rational space curves*. Neither covers part (b).

The remaining retained sets carry no Chapter V §2 exercise: Borcherds, Cais, Cutrone--Marshburn,
Ionita--Kumar, Kim, Lomont, Okamoto, Park, Saglam--Chris, Sam, Stein, Troiani and Reiser. No retained solution
set therefore proves part (b) in characteristics $2$ or $3$: Egbert's entry carries no argument and
Yang Pi-Yeh's treatment is sound only away from those two, as the paragraph above records. The
argument for those characteristics is step [](#s3){.pf-ref}, the card's own, together with the
consequence step [](#s4){.pf-ref} draws from it, and the answer it gives agrees with the printed one
at $\operatorname{char}k=2$ and with Eisenbud and Van de Ven's Proposition 6 at characteristic $0$.
:::
