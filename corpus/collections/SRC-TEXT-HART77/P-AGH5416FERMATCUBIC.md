---
schema: qual/card@1
id: P-AGH5416FERMATCUBIC
kind: problem
title: The 27 lines and the automorphism group of the Fermat cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.16 as transcribed here, the retained Andrew Egbert
    companion calculation, the 27-line configuration in V.4.10--4.11, and
    the anticanonical model of a cubic surface. The companion correctly
    points to the 6+15+6 blowup description but its final "Automorphism
    group? E6" conflates the order-51840 abstract symmetry group of the
    27-line incidence configuration with the automorphism group of the
    Fermat surface itself. The standalone problem also has a characteristic
    issue: in characteristic 3 the equation is a nonreduced triple plane,
    and in characteristic 2 the smooth Fermat cubic has an exceptional,
    larger automorphism group. The solution below gives the 27 lines and
    their incidence relations for characteristic not 3 and computes the full
    automorphism group separately in characteristic 2 and in characteristic
    not 2,3.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read all three 9-line families and solved each pairwise linear system
    independently, confirming the four incidence criteria and the 10-meets,
    16-skew count. Rechecked that the anticanonical system forces every
    surface automorphism to be projective linear. In characteristic not 2,3,
    the Hessian is the coordinate-hyperplane arrangement, forcing a monomial
    stabilizer and hence (mu_3^4/mu_3) semidirect S_4 of order 648. In
    characteristic 2, expanding F(Ax) gives A^(2)T A=cI; scalar
    normalization forces entries into F_4, and the unit-vector count
    120*36*6*3/3 gives the projective unitary order 25920. Characteristic 3
    is explicitly excluded because the equation is a triple plane.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    A published attempt located and checked on a third pass over issue #121;
    the exercise stays open on it. Algebraic Geometry II, National Taiwan
    University, 2020 Spring (course of Chin-Lung Wang), Chapter V Surfaces
    homework, Exercise 16 of section 4 (by Po-Sheng Wu), printed pp. 18-19 of
    tmp/sources/ntu-ag2-chapter5.pdf, whose printed folio is the PDF page
    number, read also in its MinerU text version
    tmp/sources/ntu-ag2-chapter5.md, gives the 27 lines as
    x_0 + w^i x_1 = x_2 + w^j x_3 = 0 over the three coordinate pairings, which
    agrees with this card's first step, and describes the automorphism group as
    diag(1, w^i, w^j, w^k) composed with a coordinate permutation, which agrees
    with the group computed below. Three defects: the displayed identity equates
    the two products instead of adding them, the Fermat cubic being
    x_0^3 + x_1^3 + x_2^3 + x_3^3 = 0; it assumes char k != 2 where the lines
    need char k != 3; and the group is computed only among the automorphisms
    induced by Aut(P^3), with no order stated. Its incidence count is right:
    "18 x 3 + 27 x 3 = 27 x 10 / 2" adds 18 x 3 = 54 pairs at its 18 points
    lying on three of the lines to its 27 listed points (1, -w^i, w^j, -w^k)
    and their permutations, which are the 81 points lying on two of the lines,
    one pair each; 54 + 81 = 135 = 27 x 10 / 2. Recomputed here over Q(w): 135
    intersecting pairs, 18 points of multiplicity three and 81 of multiplicity
    two, the 81 being the points with all four coordinates of the form +-w^r
    and exactly two minus signs, of which there are binom(4,2) 3^4 / 6 = 81 --
    no or four minus signs make the sum of the cubes +-4 and one or three make
    it +-2, neither 0 in characteristic not 2. A fourth defect is its list of
    the 18 triple points as (1, w^i, 0, 0) and its permutations, which are not
    on the surface, the sum of their cubes being 2; the triple points are
    (1, -w^i, 0, 0) and its permutations, i = 0,1,2, which is 18 points, and not
    the six of (1, -1, 0, 0). The set
    therefore supplies the explicit lines and the shape of the
    group, not a proof of the incidence relations nor of the group. No card claim
    changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the count of the eighteen triple points on 2026-11-16. The event
    above and the remark both gave them as (1, -1, 0, 0) and its permutations,
    which is six points, not eighteen; the triple points are
    (1, -omega^i, 0, 0) and their permutations for i = 0, 1, 2, eighteen of
    them. The two zero coordinates pick the pair of positions in binom(4,2) = 6
    ways, and the two nonzero entries have cubes summing to zero exactly when
    one is -omega^i times the other, which is three more classes. A point of the
    surface with exactly two zero coordinates lies on the three lines of one
    pairing through it, and one with all four coordinates nonzero lies on at
    most two, so these are exactly the points of multiplicity three, which is
    what the National Taiwan University set's own count 18 x 3 + 27 x 3 =
    27 x 10 / 2 needs: its list of them is wrong only in the sign. The 81 points
    of multiplicity two are unchanged, all four coordinates nonzero with exactly
    two negative cubes.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Under issue #121 the solution is now a transcription, one step per printed
    statement. Read at the printed places: A. Gathmann, Algebraic Geometry,
    Lemma 11.1, printed p. 90, with its proof, for the twenty-seven lines and
    their equations; Corollary 11.2(a),(b), printed pp. 90--91, for the
    incidence relations; I. Dolgachev and A. Duncan, Automorphisms of cubic
    surfaces in positive characteristic, Theorem 1.1 with Table 1, printed
    pp. 3--4, and Lemma 5.1, printed p. 25, for the two answers for the
    automorphism group, with Lemma 5.2 and its Hessian proof, printed p. 25, for
    the characteristic not 2, 3 case and Section 5.1, printed pp. 25--28, for
    the characteristic 2 case; and I. Dolgachev, Topics in Classical Algebraic
    Geometry, Theorem 9.5.7 with Table 9.4, printed pp. 386--387, whose type I is
    the Fermat cubic with group 3^3 : S_4 of order 648, as a second printed
    statement of the characteristic zero answer. Checked against the sources:
    Gathmann's coefficient argument is carried out over C and needs only a
    primitive cube root of unity and 3 not zero, which is why the card states
    char k not 3; Dolgachev--Duncan print at Section 5, p. 24, and at Section 1.3,
    p. 2, that the Fermat cubic is not reduced in characteristic 3 and that the 3C
    stratum is empty there, which is the card's reason for excluding it.
    Dolgachev--Duncan's Lemma 5.2 is printed for a Fermat hypersurface in P^n with
    n at least 4 and displays the group d^(n-1) : S_n; for the Fermat cubic, whose
    ambient space is P^3 with four coordinates, its n is 4 and the displayed
    group is 3^3 : S_4, which is Lemma 5.1's group, and the card says so instead
    of quoting the display for P^3. What this transcription does not keep is the
    card's earlier pair-by-pair congruence criterion for the incidence of the
    three families, which is not printed in the sources; what it keeps is the
    count they prove, ten lines meeting a given one and sixteen skew to it, and
    their count of five lines meeting two given skew lines.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Checked against the book before the transcription: the exercise is printed
    on p. 409 (PDF p. 424) and asks for the equations of the twenty-seven lines,
    a verification of their incidence relations, and the group of
    automorphisms. Checked in Gathmann's Lemma 11.1 that the three displayed
    families are exactly the twenty-seven lines of the Fermat cubic in its
    normalisation, that the count of nine per coordinate pairing is the count of
    pairs of cube roots of minus one, and that the four coefficient equations are
    equivalent to membership. Checked in Dolgachev--Duncan Section 5 that the
    Hermitian form H(x,y) = sum x_i F(y_i) has H(x,x) equal to the Fermat
    equation, which is what puts PSU_4(2) inside the automorphism group in
    characteristic 2, and that the order 25920 and the index two in W(E_6) are
    printed there. Not verified here: the printed page of Gathmann's own numbering
    beyond the two the card cites, since its text version marks only five-page
    blocks; and no second source was found for the incidence count beyond
    Gathmann's.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report of this day on the transcription, repaired on the card.
    (i) The exercise's second request, "verify their incidence relations", is
    not answered by the two counts the card carries. The relations are those of
    the configuration of the twenty-seven lines in the labelling E_i, F_ij, G_j,
    as the book prints them for its own cubic: the E_i mutually skew and the G_j
    mutually skew, E_i meeting F_jk exactly when i = j or i = k, E_i meeting G_j
    exactly when i and j differ, F_ij meeting F_kl exactly when i, j, k, l are
    all distinct, and F_ij meeting G_k exactly when k = i or k = j. From them a
    line meets 5 + 5 = 10 others, two skew lines have 3 + 2 = 5 common
    transversals (checked here on the printed list, by cases), and two lines that
    meet have exactly one, which the card's counts do not touch; and no source
    listed prints a criterion deciding, pair by pair, which lines of the three
    families meet, nor a result that the counts determine the configuration. The
    part is now named open in a step of its own, and the qed step no longer says
    the relations are verified.
    (ii) The step for the count of five was labelled a transcription of
    Gathmann's Corollary 11.2(b) while describing a check that neither the source
    nor the card carries out: Gathmann's proof of (b) is the sentence "The proof
    of part (b) is analogous", printed p. 91. The step now states the count as
    his and says the check is not carried out.
    (iii) Dolgachev--Duncan's Section 1.3 is printed on p. 6, not p. 2, and
    Table 1, printed p. 4, gives the 3C row PSU_4(2) of order 25920 in
    characteristic 2 and 3^3 : S_4 of order 648 in characteristic not 2 or 3,
    with no characteristic-3 entry; the step on characteristic 3 said the table
    gave the 3C stratum as empty in characteristic 2, which contradicted the
    card's own characteristic-2 step. The step now says what the table prints
    and takes the emptiness of the 3C stratum in characteristic 3 from Section
    1.3, printed p. 6, which is where it is printed.
    (iv) Lemma 5.2, printed p. 25, is stated for x_0^d + ... + x_n^d in P^n with
    n at least 4 and displays d^(n-1) : S_n; the card set up Z in P^n with
    coordinates x_0, ..., x_n and then read the lemma at n = 4, which is outside
    the printed hypothesis for a surface. The step now says that the display is
    the group of a Fermat hypersurface with n coordinates in P^(n-1), that the
    cubic in P^3 sits at n = 3 below the printed bound, and that the group used
    is Lemma 5.1's, stated without indexing.
    (v) The remark's provenance --- the tmp/sources paths and the sentence that
    the printed page is the marker minus fifteen --- is removed from the rendered
    page and recorded here. Read for this pass: Hartshorne's exercise on printed
    p. 409 and his Remark 4.10.1 with the incidence list, printed p. 404, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, whose marker is the PDF
    page and whose printed page is the marker minus fifteen; Gathmann's Lemma
    11.1 and Corollary 11.2 with its proofs, printed pp. 90--91, in
    tmp/sources/gathmann-2014-alggeom-ch11-27-lines.md, whose markers are
    five-page blocks, so the two pages are the card's and were not re-read off
    the PDF on this pass; Dolgachev--Duncan's Theorem 1.1 with Table 1, printed
    pp. 3--4, Section 1.3, printed p. 6, Lemma 5.1, Lemma 5.2 and Section 5.1,
    printed pp. 25--28, in
    tmp/sources/dolgachev-duncan-2017-automorphisms-cubic-surfaces-char-p.md,
    whose first marker is the block of PDF pages 1--20, so those printed pages
    are the reader's and were not re-read off the PDF's folios on this pass.
    Read in the same file: the paragraph of Section 1.3 that names the Fermat
    cubic the unique 3C surface and states both groups in words. Not read here:
    the National Taiwan University set's pages were not re-read, and nothing was
    searched for a published verification of the incidence relations beyond the
    sources listed, so that part stays open.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report of this day, repaired here. (i) Two events of this day ---
    the solution-written and the source-checked ones above --- had been rewritten
    in place by 1a3e3c52dd, which a dated record does not allow; they are
    restored to the text they were introduced with, and what that commit changed
    is recorded in the event it appended, which stands. (ii) The first of the
    orchestrator's decisions for this repair was not applied to the incidence
    relations: the card's own pair-by-pair computation, in the steps
    same-family-incidence, ab-family-incidence, ac-family-incidence and
    bc-family-incidence of 83d33296ae with the counting step that closes them, had
    been dropped when the solution was turned into a transcription. It is
    restored, marked in the steps as the card's own, and the notation A_ab, B_ab,
    C_ab it uses is declared there as the twenty-seven lines already found, with
    the exponents renamed; no source listed prints that computation.
    (iii) The step that named the part open also asserted, with no source and no
    proof, that the two counts do not determine the configuration; that sentence
    is withdrawn, since the restored criteria decide every pair, and what remains
    true is only that no source listed prints such a criterion.
    (iv) The rendered remark said that Gathmann's chapter works over C "which the
    card's field k replaces", which is bookkeeping; it now says that his argument
    uses only a primitive cube root of unity and 3 not zero. Read for this pass:
    Gathmann, printed pp. 90--91, in
    tmp/sources/gathmann-2014-alggeom-ch11-27-lines.md, whose markers are
    five-page blocks, so the pages are those of the events above and were not
    re-read off the PDF; and Dolgachev--Duncan, printed pp. 3--6 and 24--28, in
    tmp/sources/dolgachev-duncan-2017-automorphisms-cubic-surfaces-char-p.md,
    whose first marker is the block of PDF pages 1--20, so those pages are not
    re-read off the folios either. Nothing else on the card changed.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report of this day on the count of five, repaired here. The step
    two-skew-lines-meet-five stated the count as Gathmann's and said that his
    proof is the sentence "The proof of part (b) is analogous" and that no check
    was carried out on the card, so the count stood on no argument of the card's
    own. It is now derived there from the pair-by-pair criteria of the four steps
    above it and marked as the card's own, and the step sits after
    incidence-count-ten-sixteen so that every step it cites comes before it. The
    derivation runs the two positions a skew pair can occupy: in one family, where
    the two lines of that family meeting both give 2 and exactly one of the
    conditions a-b = c-d and a+b = c+d holds, giving 3 more; and in two families,
    where the transposition of x_1 and x_2 preserves S and carries A to B, so that
    A_ab, B_cd with a+d not b+c is the general case, and it is met by 2 A-lines, 2
    B-lines and 1 C-line. Gathmann's Corollary 11.2(b), printed p. 91, states the
    count and nothing more; the qed and the remark now say that the derivation is
    the card's. The count was also confirmed exhaustively: over GF(7), where 2 is a
    primitive cube root of unity and 3 is invertible, the 27 lines of the three
    families are distinct, each meets exactly 10 of the others, every pair of the
    four criteria of the card holds for all 27 x 27 pairs, and every one of the
    216 skew pairs, 54 within one family and 162 across two, has exactly 5 common
    transversals. Read for this pass: Gathmann's Lemma 11.1 and Corollary 11.2
    with their proofs, printed pp. 90--91, in
    tmp/sources/gathmann-2014-alggeom-ch11-27-lines.md, whose first marker is the
    block of PDF pages 1--5, so those two printed pages were not re-read off the
    folios of tmp/sources/gathmann-2014-alggeom-ch11-27-lines.pdf here. Not read
    here: the National Taiwan University set, untouched by this repair, and
    Dolgachev--Duncan, whose events above stand. Nothing was searched for a
    published pair-by-pair incidence criterion, and none was found in the sources
    listed, so the criteria and the count stay the card's own.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report of this day on the event above, repaired here. That event
    described the two-family case of the count of five as reducing by the
    transposition of x_1 and x_2, and the step said the same. That transposition
    does not reduce the two remaining pairings: it interchanges the A- and
    B-families and keeps the C-family, carrying C_ab to C_{a,-b}, so it carries an
    A-C pair to a B-C pair and a B-C pair to an A-C pair and never to the form
    A_ab, B_cd. The step now names the transpositions that do the reduction: that
    of x_2 and x_3 keeps the A-family, sending A_ab to A_{a,-b}, and interchanges
    B and C, sending B_ab to C_ab and C_ab to B_ab, so it carries an A-C pair to
    an A-B pair; and that of x_1 and x_3 keeps the B-family, sending B_ab to
    B_{a,-b}, and interchanges A and C, so it carries a B-C pair to an A-B pair.
    The step also states what makes the relabelling legitimate, that a projectivity
    maps the 27 lines to themselves and preserves incidences, so the pair and its
    image have equally many common transversals. Checked on the equations of the
    three families as the card prints them, line by line, and confirmed by the
    exhaustive GF(7) computation recorded in the event above, whose family actions
    are these and whose counts are 5 for every skew pair of every pairing. What
    stands from the event above: the derivation from the four criteria, the two
    lines and the one C-line of the A-B case, and the placement of the step after
    incidence-count-ten-sixteen. Read for this event: the three family definitions
    of the step three-line-families and the four criteria, on the card, and
    nothing further in the sources; Gathmann's printed pp. 90--91 continue to be
    read as the event above records.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The batch's fourth retained set read at this exercise. Read Yang Pi-Yeh,
    Hartshorne Solutions (9 June 2019), Solution 5.4.16, printed p. 112,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page (folio 112 at the foot). Checked against the book: Hartshorne
    V.4.16, printed p. 409, asks for the equations of the 27 lines, for the
    incidence relations, and for the group of automorphisms, and the entry
    gives the first only. Recomputed: the four coefficient equations
    a_0^3 + a_1^3 = -1, b_0^3 + b_1^3 = -1, a_0^2 b_0 + a_1^2 b_1 = 0 and
    a_0 b_0^2 + a_1 b_1^2 = 0 obtained by substituting
    x_0 = a_0 x_2 + b_0 x_3, x_1 = a_1 x_2 + b_1 x_3 into the Fermat cubic;
    that no line has all four coefficients nonzero, since the last two give
    a_0/b_0 = a_1/b_1 and then b_0^3 + b_1^3 = 0 against b_0^3 + b_1^3 = -1;
    and that its case a_0 = 0 gives the family x_0 + omega^k x_3 =
    x_1 + omega^j x_2 = 0, whose three coordinate pairings give the 27 lines
    of step twenty-seven-lines. Not checked: Yang's Solutions outside printed
    p. 112, and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 5.4.16 at printed p. 112 as
    covering part (a) of the exercise and neither (b) nor (c), with its
    coefficient analysis, the vanishing-coefficient argument it leaves out, and
    its three line families matched to step twenty-seven-lines. No step,
    statement or hypothesis of the card changes.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read for issue #168 and recomputed: steps twenty-seven-lines,
    incidence-ten-and-sixteen, the two bodies ac-family-incidence and
    bc-family-incidence, automorphism-group-not-two-three, and the closing
    paragraph of automorphism-group-characteristic-two.

    Gathmann's Lemma 11.1 and Corollary 11.2 were re-read in the retained
    extraction and carry the coefficient argument and the four-three-three list
    that the two incidence steps transcribe, together with the reduction by
    permuting coordinates and multiplying them by cube roots of unity.
    Recomputed over F_7, in which 2 is a primitive cube root of unity: the three
    families of step three-line-families are 27 distinct lines, each of them on
    the Fermat cubic; every line meets exactly ten of the other twenty-six; the
    four criteria of steps same-family-incidence, ab-family-incidence,
    ac-family-incidence and bc-family-incidence hold on every pair they cover,
    108 same-family pairs and 81 in each of the three mixed cases, so the two
    bodies ac and bc are right; the ten lines meeting C_00 are C_01, C_02, C_10,
    C_20, B_00, B_12, B_21, A_00, A_12, A_21, which is the four-three-three list
    of step incidence-ten-and-sixteen; every skew pair has exactly five common
    transversals; and the orbit of A_00 under coordinate permutations and
    cube-root scalings is all 27 lines, the transitivity that step
    incidence-ten-and-sixteen uses. The coefficient argument of step
    twenty-seven-lines was recomputed from the four relations
    a_2^3+b_2^3=-1, a_3^3+b_3^3=-1, a_2^2a_3=-b_2^2b_3 and
    a_2a_3^2=-b_2b_3^2, with the vanishing of one coefficient argued as the step
    argues it.

    For automorphism-group-not-two-three: Dolgachev and Duncan's Lemma 5.1 was
    read in the retained extraction and states both groups; their Lemma 5.2 with
    its Hessian display was read too. The Hessian of x_0^3+x_1^3+x_2^3+x_3^3 was
    computed as 6^4 x_0x_1x_2x_3, a nonzero scalar multiple of that display, and
    the monomial maps x_i -> z_i x_sigma(i) preserving the cubic were counted
    over F_7: 1944 of them, which is 648 projectively, that is 3^3 times 4!, the
    order the step asserts. The step's reading of Lemma 5.2's indexing, that the
    display d^{n-1} rtimes S_n is the group for n coordinates in P^{n-1}, was
    checked against the printed formula and is the only reading under which the
    formula is consistent, as the step says.

    For the closing paragraph of automorphism-group-characteristic-two: PSU_4(2)
    was computed of order 77760/3 = 25920, the incidence graph of the 27 lines
    was built and its automorphism group computed, of order 51840, and 25920 is
    half of that, so the index-two statement holds. The paragraph's argument was
    read and is valid: a subgroup of W(E_6) containing a subgroup of index two is
    one of the two, and the larger alternative would make the Frobenius
    geometric, which it is not. The same conclusion is the last sentence of the
    retained passage, that the automorphism group of the Fermat cubic cannot be
    larger than PSU_4(2). Not checked: nothing outside the retained files was
    read in this pass, and the parenthetical of the printed exercise's part (c)
    is not part of what these steps claim.
---

::: {.problem}
For the Fermat cubic surface $x_0^3+x_1^3+x_2^3+x_3^3=0$, find the equations of the 27 lines explicitly, and verify their incidence relations.
What is the group of automorphisms of this surface?
:::

::: {.solution}
Let
$$
S=V(F)\subseteq\PP_k^3,\qquad F=x_0^3+x_1^3+x_2^3+x_3^3,
$$
with $k$ algebraically closed, and let $\omega\in k$ be a primitive cube root of unity.

In characteristic $3$ one has
$$
F=(x_0+x_1+x_2+x_3)^3,
$$
so the displayed scheme is a nonreduced triple plane and not the nonsingular cubic surface to which the $27$-line theory and the automorphism question apply; Dolgachev and Duncan print this at the opening of Section 5, printed p. 24, and record in Section 1.3, printed p. 6, that the $3C$ stratum is empty in characteristic $3$. The transcription below therefore assumes throughout that
$$
\operatorname{char}k\ne3,
$$
and it separates characteristic $2$ from the other characteristics at the automorphism group, which is also what Dolgachev and Duncan's Lemma 5.1 does.

::: pf

::: {.pf-step #twenty-seven-lines}
$S$ contains exactly $27$ lines, namely
$$
x_0+x_3\omega^k=x_1+x_2\omega^j=0,\qquad
x_0+x_2\omega^k=x_3+x_1\omega^j=0,\qquad
x_0+x_1\omega^k=x_3+x_2\omega^j=0,
$$
for $0\le j,k\le2$.

::: pf-proof
This is Lemma 11.1 of Gathmann, printed p. 90, carried out for the ground field $k$; its argument uses only that a primitive cube root of unity exists and that $3\ne0$. Up to a permutation of the coordinates every line of $\PP^3$ is given by two equations
$$
x_0=a_2x_2+a_3x_3,\qquad x_1=b_2x_2+b_3x_3
$$
with $a_2,a_3,b_2,b_3\in k$, and such a line lies in $S$ exactly when
$$
(a_2x_2+a_3x_3)^3+(b_2x_2+b_3x_3)^3+x_2^3+x_3^3=0
$$
as a polynomial in $k[x_2,x_3]$, that is exactly when
$$
a_2^3+b_2^3=-1,\qquad a_3^3+b_3^3=-1,\qquad a_2^2a_3=-b_2^2b_3,\qquad a_2a_3^2=-b_2b_3^2.
$$
If all four of $a_2,a_3,b_2,b_3$ are nonzero, then dividing the square of the third relation by the fourth gives $a_2^3=-b_2^3$, contradicting the first. So at least one is zero, and after renumbering the coordinates one may assume $a_2=0$; then the first relation gives $b_2^3=-1$, the third gives $b_3=0$, and the second gives $a_3^3=-1$. Conversely such values give a line on $S$. With $b_2=-\omega^j$ and $a_3=-\omega^k$, $0\le j,k\le2$, this is the $9$ lines $x_0+x_3\omega^k=x_1+x_2\omega^j=0$ of this coordinate pairing, and allowing the three pairings of the coordinates gives the $27$ displayed lines.
:::

:::

::: {.pf-step #incidence-ten-and-sixteen}
Each line of $S$ meets exactly $10$ of the other $26$ lines and is skew to the remaining $16$.

::: pf-proof
This is Corollary 11.2(a) of Gathmann, printed p. 91, whose proof is the verification: knowing all the lines from step [](#twenty-seven-lines){.pf-ref}, and using that permuting the coordinates and multiplying them by cube roots of unity takes any line of $S$ to any other, one may assume the given line is $L:\ x_0+x_3=x_1+x_2=0$. The lines of $S$ meeting $L$ are then exactly
$$
x_0+x_3\omega^k=x_1+x_2\omega^j=0\quad\text{with } (j,k)=(1,0),(2,0),(0,1),(0,2),
$$
which are $4$, together with
$$
x_0+x_2\omega^j=x_3+x_1\omega^j=0\quad (0\le j\le2),\qquad
x_0+x_1\omega^j=x_3+x_2\omega^j=0\quad (0\le j\le2),
$$
which are $3$ and $3$ more. That is $4+3+3=10$ lines meeting $L$, and $L$ was an arbitrary line of $S$. Since there are $26$ other lines, $16$ of them are skew to $L$.
:::

:::

::: {.pf-step #three-line-families}
For $a,b\in\ZZ/3$ put
$$
A_{ab}=V(x_0+\omega^a x_1,\ x_2+\omega^b x_3),\quad
B_{ab}=V(x_0+\omega^a x_2,\ x_1+\omega^b x_3),\quad
C_{ab}=V(x_0+\omega^a x_3,\ x_1+\omega^b x_2).
$$
These are the $27$ lines of step [](#twenty-seven-lines){.pf-ref} with the exponents renamed, and every incidence question about them is decided by their equations.

::: pf-proof
Each family has $3\cdot3=9$ members. $A_{ab}$ pairs $x_0$ with $x_1$ and $x_2$ with $x_3$, $B_{ab}$ pairs $x_0$ with $x_2$ and $x_1$ with $x_3$, and $C_{ab}$ pairs $x_0$ with $x_3$ and $x_1$ with $x_2$; those are the three pairings of the displayed list, the second equation of each line carrying the cube roots of minus one, and the exponents of the first equation ranging independently over the three cube roots of unity. The four criteria that follow are the card's own computation: no source listed for this card prints them.
:::

:::

::: {.pf-step #same-family-incidence}
For two distinct lines in the same family,
$$
\boxed{
A_{ab}\cap A_{cd}\ne\varnothing
\iff
a=c\text{ or }b=d,
}
$$
and the identical criterion holds in the $B$- and $C$-families.

::: pf-proof
Suppose first that
$$
a=c,
\qquad
b\ne d.
$$
The two equations involving $x_2,x_3$ then force
$$
x_2=x_3=0,
$$
while the common first equation gives the point
$$
[-\omega^a:1:0:0].
$$
Thus the lines meet. If instead $b=d$ and $a\ne c$, they meet at
$$
[0:0:-\omega^b:1].
$$

If $a\ne c$ and $b\ne d$, the first pair of equations forces $x_0=x_1=0$ and the second pair forces $x_2=x_3=0$, so there is no projective point of intersection. The other two families are obtained by permuting the coordinates.
:::

:::

::: {.pf-step #ab-family-incidence}
Lines from the $A$- and $B$-families satisfy
$$
\boxed{
A_{ab}\cap B_{cd}\ne\varnothing
\iff
a+d\equiv b+c\pmod3.}
$$

::: pf-proof
On a common point we may write, from the equations of $A_{ab}$ and $B_{cd}$,
$$
x_2=-\omega^b x_3,
\qquad
x_1=-\omega^d x_3.
$$
Then the two expressions for $x_0$ are
$$
x_0=-\omega^a x_1=\omega^{a+d}x_3
$$
and
$$
x_0=-\omega^c x_2=\omega^{b+c}x_3.
$$
A nonzero common point therefore exists exactly when
$$
\omega^{a+d}=\omega^{b+c},
$$
which is the displayed congruence. When it holds, taking $x_3=1$ gives the unique point of intersection.
:::

:::

::: {.pf-step #ac-family-incidence}
Lines from the $A$- and $C$-families satisfy
$$
\boxed{
A_{ab}\cap C_{cd}\ne\varnothing
\iff
c\equiv a+b+d\pmod3.}
$$

::: pf-proof
The equations give
$$
x_2=-\omega^b x_3
$$
and then
$$
x_1=-\omega^d x_2=\omega^{b+d}x_3.
$$
Consequently the $A$-equation gives
$$
x_0=-\omega^{a+b+d}x_3,
$$
whereas the $C$-equation gives
$$
x_0=-\omega^c x_3.
$$
These are compatible exactly under the displayed congruence.
:::

:::

::: {.pf-step #bc-family-incidence}
Lines from the $B$- and $C$-families satisfy
$$
\boxed{
B_{ab}\cap C_{cd}\ne\varnothing
\iff
a+b\equiv c+d\pmod3.}
$$

::: pf-proof
Put $x_2=t$. The $C$-equation gives
$$
x_1=-\omega^d t,
$$
and comparison with
$$
x_1=-\omega^b x_3
$$
gives
$$
x_3=\omega^{d-b}t.
$$
Now
$$
x_0=-\omega^a t
$$
from $B_{ab}$, while $C_{cd}$ gives
$$
x_0=-\omega^c x_3=-\omega^{c+d-b}t.
$$
Compatibility is therefore equivalent to
$$
a+b\equiv c+d\pmod3.
$$
:::

:::

::: {.pf-step #incidence-count-ten-sixteen}
The criteria of steps [](#same-family-incidence){.pf-ref}, [](#ab-family-incidence){.pf-ref}, [](#ac-family-incidence){.pf-ref} and [](#bc-family-incidence){.pf-ref} give the complete incidence configuration of the $27$ lines. In particular every line meets exactly $10$ of the other lines and is skew to the remaining $16$.

::: pf-proof
Fix $A_{ab}$. By step [](#same-family-incidence){.pf-ref} it meets exactly four other $A$-lines: two with the same first exponent and two with the same second exponent.

For each $c\in\ZZ/3$, step [](#ab-family-incidence){.pf-ref} determines a unique $d$ for which $A_{ab}$ meets $B_{cd}$. Thus it meets exactly three $B$-lines. Likewise, for each $d$, step [](#ac-family-incidence){.pf-ref} determines a unique $c$, so it meets exactly three $C$-lines.

Hence $A_{ab}$ meets
$$
4+3+3=10
$$
other lines. Coordinate symmetry gives the same count for every $B$- and $C$-line. Since there are $26$ other lines in total, each line is skew to $16$. The congruences decide every possible pair, so they give the full incidence relations.
:::

:::

::: {.pf-step #two-skew-lines-meet-five}
Two skew lines of $S$ are met by exactly $5$ further lines of $S$.

::: pf-proof
Gathmann states this as Corollary 11.2(b), printed p. 91, and prints "The proof of part (b) is analogous" for it, so the count is derived here from the criteria of steps [](#same-family-incidence){.pf-ref}, [](#ab-family-incidence){.pf-ref}, [](#ac-family-incidence){.pf-ref} and [](#bc-family-incidence){.pf-ref}, and that derivation is the card's own.

Two skew lines lie either in one family or in two. If they are $A_{ab}$ and $A_{cd}$ in the first family, then $a\ne c$ and $b\ne d$ by step [](#same-family-incidence){.pf-ref}. The $A$-lines meeting both are exactly $A_{ad}$ and $A_{cb}$, one for each way of matching the two first exponents with the two second ones. A $B$-line $B_{a'b'}$ meets $A_{ab}$ exactly when $a'-b'\equiv a-b$ and meets $A_{cd}$ exactly when $a'-b'\equiv c-d$, by step [](#ab-family-incidence){.pf-ref}, so it meets both exactly when $a-b\equiv c-d$, and then all three such $B$-lines do; a $C$-line $C_{a'b'}$ meets $A_{ab}$ exactly when $a'\equiv a+b+b'$ and $A_{cd}$ exactly when $a'\equiv c+d+b'$, by step [](#ac-family-incidence){.pf-ref}, so it meets both exactly when $a+b\equiv c+d$, and then all three such $C$-lines do. Writing $x=a-c$ and $y=b-d$, both nonzero, the first condition is $x\equiv y$ and the second is $x\equiv-y$, and $y$ and $-y$ are the two nonzero residues modulo $3$: exactly one of them holds, and the count is $2+3=5$.

If the two lines lie in different families, a transposition of two coordinates preserves $S$, the equation being symmetric in them, and carries one two-family pairing to another; being a projectivity it maps the $27$ lines to themselves and preserves incidences, so a pair and its image have the same number of common transversals. The transposition of $x_2$ and $x_3$ keeps the $A$-family, sending $A_{ab}$ to $A_{a,-b}$, and interchanges the other two, sending $B_{ab}$ to $C_{ab}$ and $C_{ab}$ to $B_{ab}$; the transposition of $x_1$ and $x_3$ keeps the $B$-family, sending $B_{ab}$ to $B_{a,-b}$, and interchanges $A$ and $C$. An $A$--$C$ pair is therefore carried to an $A$--$B$ pair by the first of them and a $B$--$C$ pair to an $A$--$B$ pair by the second, with the exponents relabelled, so it suffices to treat $A_{ab}$ and $B_{cd}$, which is skew exactly when $a+d\not\equiv b+c$ by step [](#ab-family-incidence){.pf-ref}. Such a pair is met by the two $A$-lines $A_{a,\,a+d-c}$ and $A_{b+c-d,\,b}$ and the two $B$-lines $B_{c,\,b+c-a}$ and $B_{a+d-b,\,d}$, each of which is distinct from $A_{ab}$ and from $B_{cd}$ because $a+d\not\equiv b+c$, and by one $C$-line, the one with $b'\equiv2(c+d-a-b)$ and $a'\equiv a+b+b'$, since $C_{a'b'}$ meets $A_{ab}$ exactly when $a'\equiv a+b+b'$ and meets $B_{cd}$ exactly when $a'+b'\equiv c+d$. That is $2+2+1=5$ further lines.
:::

:::

::: {.pf-step #incidence-relations-open}
No source listed for this card prints a criterion deciding, pair by pair, which lines of the three families meet, nor a result that the two counts determine the configuration.

::: pf-proof
Gathmann verifies the incidence relations of the Fermat cubic as the counts of his Corollary 11.2, printed pp. 90--91, and leaves the proof of part (b) as "analogous"; the National Taiwan University set counts intersecting pairs and points of multiplicity three and settles no pair. The criteria above are therefore the card's own, and they answer the exercise's second request without a cited source.
:::

:::

::: {.pf-step #automorphism-group-not-two-three}
If $\operatorname{char}k\ne2,3$, then
$$
\boxed{\Aut(S)\cong3^3\rtimes\Sigma_4,\qquad \cardinality{\Aut(S)}=648.}
$$

::: pf-proof
The statement is Lemma 5.1 of Dolgachev and Duncan, printed p. 25, and the proof they give for this case is Lemma 5.2 with its proof, printed p. 25. Let $Z=V(x_0^d+\cdots+x_n^d)\subseteq\PP^n$ with $d\ge3$ and $p\nmid d(d-1)$; the Hessian hypersurface of $Z$ is
$$
\operatorname{He}(Z)=\left\{(d(d-1))^n x_0^{d-2}\cdots x_n^{d-2}=0\right\},
$$
which is nontrivial under those hypotheses. The Hessian is intrinsic to the projective embedding and not to the choice of coordinates, so a projective automorphism of $Z$ induces one of $\operatorname{He}(Z)$. The automorphisms of the union of the coordinate hyperplanes are generated by permutations of the coordinates and by multiplying coordinates by constants, and for such a transformation to preserve $Z$ those constants must be $d$-th roots of unity. Lemma 5.2, printed p. 25, is stated for the hypersurface $x_0^d+\cdots+x_n^d=0$ in $\PP^n$ with $n\ge4$ and displays the group $d^{n-1}\rtimes\Sigma_n$: as indexed, the group carries one factor of $d$ fewer than the hypersurface has coordinates, and the cubic in this step's coordinates, $x_0^3+\cdots+x_n^3$, is a surface only at $n=3$, below the printed bound. The display is the group of a Fermat hypersurface with $n$ coordinates, which lies in $\PP^{n-1}$, and at four coordinates --- the Fermat cubic in $\PP^3$ --- it gives $3^3\rtimes\Sigma_4$, of order $3^3\cdot4!=648$. That reading, and not the printed indexing of the ambient space, is what is used here, and Lemma 5.1 states the same group for the cubic without any indexing. The same group is printed independently by Dolgachev, Theorem 9.5.7 with Table 9.4, printed pp. 386--387, whose type I is the Fermat surface: its proof reads that an automorphism permutes the planes $t_i+\varepsilon t_j=0$ and that $\Aut(S)$ therefore "consists of permutations of the variables and multiplying the variables by cube roots of unity".
:::

:::

::: {.pf-step #automorphism-group-characteristic-two}
If $\operatorname{char}k=2$, then
$$
\boxed{\Aut(S)\cong\operatorname{PSU}_4(2),\qquad \cardinality{\Aut(S)}=25920.}
$$

::: pf-proof
This is the second case of Lemma 5.1 of Dolgachev and Duncan, printed p. 25, proved in Section 5.1, printed pp. 25--28. Let $\varphi\colon\FF_4\to\FF_4$ be the Frobenius automorphism $\varphi(x)=x^2$ and let $H$ be the Hermitian form
$$
H(x,y)=\sum_{i=0}^3x_i\varphi(y_i)
$$
on $\FF_4^4$, nondegenerate of dimension $4$. Its diagonal value is
$$
H(x,x)=x_0^3+x_1^3+x_2^3+x_3^3,
$$
which is the defining equation of $S$, so the projective special unitary group $\operatorname{PSU}_4(2)$ lies in $\Aut(S)$; it has order $25920$ and index $2$ in the Weyl group $W(\mathbf E_6)$. The map
$$
\sigma(x_0:x_1:x_2:x_3)=(\varphi(x_0):\varphi(x_1):\varphi(x_2):\varphi(x_3))
$$
preserves $S(\FF_4)$ in its diagonal form and permutes the $27$ lines preserving their configuration, so $\sigma$ acts as an element of $W(\mathbf E_6)$, and no element of $\operatorname{PSU}_4(2)$ acts in this way: the action of $\sigma$ is not geometric. Hence $\sigma$ and $\operatorname{PSU}_4(2)$ generate all of $W(\mathbf E_6)$.

The source's last step, unpacked: the action on the $27$ lines gives an injection $\Aut(S)\to W(\mathbf E_6)$ (Section 1, printed pp. 3--4), and $\operatorname{PSU}_4(2)$ has index $2$ in $W(\mathbf E_6)$, so a subgroup of $W(\mathbf E_6)$ containing $\operatorname{PSU}_4(2)$ is either $\operatorname{PSU}_4(2)$ itself or all of $W(\mathbf E_6)$. The second alternative would make every element of $W(\mathbf E_6)$ geometric and in particular $\sigma$, which the previous paragraph denies. So $\Aut(S)=\operatorname{PSU}_4(2)$.
:::

:::

::: {.pf-step #characteristic-three}
If $\operatorname{char}k=3$, the equation defines a nonreduced triple plane and the exercise's question has no smooth surface to ask it of.

::: pf-proof
In characteristic $3$ the Frobenius is additive, so $x_0^3+x_1^3+x_2^3+x_3^3=(x_0+x_1+x_2+x_3)^3$. Dolgachev and Duncan record this at the opening of Section 5, printed p. 24, and in Section 1.3, printed p. 6, where the Fermat cubic is named as the unique surface carrying an automorphism of class $3C$ and is said not to be reduced when $p=3$, the $3C$ stratum then being empty. Their Table 1, printed p. 4, gives the $3C$ row the group $3^3\rtimes\Sigma_4$ of order $648$ in characteristic not $2$ or $3$ and $\operatorname{PSU}_4(2)$ of order $25920$ in characteristic $2$, and has no entry in characteristic $3$.
:::

:::

::: pf-qed
Step [](#twenty-seven-lines){.pf-ref} gives the equations of the $27$ lines; steps [](#same-family-incidence){.pf-ref}, [](#ab-family-incidence){.pf-ref}, [](#ac-family-incidence){.pf-ref} and [](#bc-family-incidence){.pf-ref} decide every pair, and step [](#incidence-count-ten-sixteen){.pf-ref} draws the counts $10$ and $16$ from them, which is the card's own computation and answers the exercise's second request; step [](#incidence-relations-open){.pf-ref} records that no source listed prints such a criterion; Gathmann's count of $10$ is step [](#incidence-ten-and-sixteen){.pf-ref}, and his count of $5$, step [](#two-skew-lines-meet-five){.pf-ref}, is derived there from the criteria, since he states it and leaves its proof as analogous. Step [](#automorphism-group-not-two-three){.pf-ref} gives $\Aut(S)\cong3^3\rtimes\Sigma_4$ of order $648$ when $\operatorname{char}k\ne2,3$, and step [](#automorphism-group-characteristic-two){.pf-ref} gives $\Aut(S)\cong\operatorname{PSU}_4(2)$ of order $25920$ when $\operatorname{char}k=2$. In characteristic $3$ the equation is a triple plane, as step [](#characteristic-three){.pf-ref} records, so the smooth cubic surface question does not arise.
:::

:::
:::

::: {.remark title="Published solutions"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.4, exercise 4.16, printed p. 409: the equations of the twenty-seven lines, a verification of their incidence relations, and the group of automorphisms.

Andreas Gathmann, *Algebraic Geometry* (2014), Chapter 11, is the source of the lines and of the incidence count. Lemma 11.1, printed p. 90, contains the whole coefficient argument that produces exactly $27$ lines on the Fermat cubic and prints the three families; Corollary 11.2, printed pp. 90--91, then proves that exactly $10$ other lines meet a given one, working one line out in full after reducing by a coordinate permutation and multiplications by cube roots of unity, and states that exactly $5$ lines meet two given skew ones with the proof given as "analogous", which step [](#two-skew-lines-meet-five){.pf-ref} derives from the criteria of the three families. What Gathmann does not print is a criterion deciding, for each pair of the three families, whether the two lines meet; the incidence relations he verifies are the two counts. His chapter works over $\CC$; the argument uses only a primitive cube root of unity and $3\ne0$.

Igor V. Dolgachev and Alexander Duncan, *Automorphisms of cubic surfaces in positive characteristic*, gives the automorphism group in every characteristic. Theorem 1.1 with Table 1, printed pp. 3--4, lists the possible groups by stratum: the row $3C$ has $3^3\rtimes\mathfrak S_4$ of order $648$ for $\operatorname{char}k\ne2,3$ and $\operatorname{PSU}_4(2)$ of order $25920$ for $\operatorname{char}k=2$, and has no entry for $\operatorname{char}k=3$. Lemma 5.1, printed p. 25, states both values for the Fermat cubic itself; Lemma 5.2 with its proof, printed p. 25, is the Hessian argument for the first, and Section 5.1, printed pp. 25--28, is the Hermitian-form and Frobenius argument for the second. Section 1.3, printed p. 6, records the same two facts in words: the Fermat cubic is the unique surface with an automorphism of class $3C$, it is not reduced when $p=3$ and the $3C$ stratum is then empty, its group is generated by permutations and by multiplying coordinates by third roots of unity when $p\ge5$, and it is $\operatorname{PSU}_4(2)$ of order $25920$ when $p=2$.

Igor V. Dolgachev, *Topics in Classical Algebraic Geometry*, Theorem 9.5.7 with Table 9.4, printed pp. 386--387, classifies all automorphism groups of nonsingular cubic surfaces in characteristic zero and lists the Fermat surface as type I with group $3^3:\mathfrak S_4$ of order $648$; his proof of that row is the permutation-of-planes argument quoted at step [](#automorphism-group-not-two-three){.pf-ref}. That duplicates the characteristic-zero half of Dolgachev--Duncan's Lemma 5.1 in a second printed place.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 5.4.16, printed p. 112, covers the
exercise's first part only. Writing a line of $\PP^3$ as $a_0x_2+b_0x_3-x_0=a_1x_2+b_1x_3-x_1=0$
and substituting into $x_0^3+x_1^3+x_2^3+x_3^3$, it gets $a_0^3+a_1^3=-1$, $b_0^3+b_1^3=-1$,
$a_0^2b_0+a_1^2b_1=0$ and $a_0b_0^2+a_1b_1^2=0$, and lists the $27$ lines as
$x_0+\omega^kx_3=x_1+\omega^jx_2=0$, $x_0+\omega^kx_2=x_3+\omega^jx_1=0$ and
$x_0+\omega^kx_1=x_3+\omega^jx_2=0$ over $0\le j,k\le2$, the three coordinate pairings of step
[](#twenty-seven-lines){.pf-ref}. Its reduction to $a_0=0$ omits the argument that some coefficient
must vanish — if all four are nonzero the last two equations give $a_0/b_0=a_1/b_1$ and then
$b_0^3+b_1^3=0$ — and the coordinate symmetry of the Fermat cubic supplies the rest. It says nothing
of the incidence relations or of the automorphism group, so it covers part (a) of the exercise and
neither (b) nor (c).

The nearest published attempt at the exercise itself remains Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework, exercise 16 of Section 4 (by Po-Sheng Wu), printed pp. 18--19. It gives the $27$ lines as $x_0+\omega^ix_1=x_2+\omega^jx_3=0$ over the three coordinate pairings, which agrees with step [](#twenty-seven-lines){.pf-ref}, and describes the group as $\operatorname{diag}(1,\omega^i,\omega^j,\omega^k)$ composed with a permutation of the coordinates, which agrees with step [](#automorphism-group-not-two-three){.pf-ref}; it states no order, assumes $\operatorname{char}k\ne2$ where the lines need $\operatorname{char}k\ne3$, equates the two products $(x_0+x_1)(x_0+\omega x_1)(x_0+\omega^2x_1)$ and $(x_2+x_3)(x_2+\omega x_3)(x_2+\omega^2x_3)$ where the Fermat cubic is their sum, and lists the $18$ triple points as $(1,\omega^i,0,0)$ and its permutations, which are not on the surface, their cubes summing to $2$ rather than $0$.
:::
