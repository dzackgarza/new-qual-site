---
schema: qual/card@1
id: P-AGH562CHERNGRIFFITHS
kind: problem
title: Chern-Griffiths theorem bounding the geometric genus by the degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Canonical Divisor
  - Adjunction
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Hartshorne V.6.2 transcription and collection context,
    and the retained Hartshorne V migration ledger, which records that the
    V.6.2 statement and its Clifford/Riemann--Roch/Kodaira hint were compared
    with the source. The retained Hartshorne solution attachment ends in
    Chapter IV, so there is no V.6.2 source solution to incorporate. The
    proof below is an independent argument using a general hyperplane
    section, Clifford's theorem, adjunction, surface Riemann--Roch, and
    Kodaira vanishing.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the complete argument. Checked the hyperplane restriction bound
    h^0(C,O_C(1))>=n+1, the iterative restriction argument that nonspeciality
    forces p_g=0, and the Clifford equality case at d=2n. In the hyperelliptic
    equality case, deg L=2n and h^0(L)=n+1 make all sections pullbacks of
    H^0(P^1,O(n)), contradicting very ampleness. In the canonical equality
    case, K_X.H=0 and a nonzero canonical section force K_X~0; surface
    Riemann--Roch plus Kodaira vanishing then gives
    h^0(O_X(1))=n+2-q, while nondegeneracy gives at least n+2 sections, so
    q=0 and X is K3.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Read for issue #121 and cited the published proof of the strict-inequality
    half on the card: J. Harris, A bound on the geometric genus of projective
    varieties, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 8 (1981), §2, printed
    pp. 42--44, read in
    tmp/sources/harris-1981-bound-geometric-genus.md, whose page markers place
    §2 in its first twenty pages. Step harris-bound transcribes Harris's
    displays: M and epsilon at printed p. 42, the curve bound and the Poincaré
    residue sequence at printed p. 43, the surface bound and the corollary
    p_g = 0 for d <= k(N-k)+1 at printed p. 44; it replaces the step
    nonspecial-below-2n of the 2026-09-20 solution, whose conditional
    derivation of H^1(C,L) = 0 is subsumed. Checked against the exercise and
    its hint at Hartshorne V.6.2, printed p. 423 (PDF p. 438, printed = PDF
    minus 15), and against the book pages the other steps now name: Proposition
    8.20 printed p. 182, Theorem 5.4 printed p. 343, Theorem 1.6 printed
    p. 362 and Remark 7.15 printed p. 248. Read for the equality case: Yang
    Pi-Yeh, solution 5.6.2, printed p. 115 of
    tmp/sources/lfwin-hartshorne-solutions.pdf, read in
    tmp/sources/lfwin-hartshorne-solutions.md, both halves present and two
    steps unproved, namely H.K >= 0 in his chain 2n+2 <= 2-2g+2d <= d and the
    passage from p_a = 1 to p_g = 1. The card keeps its own steps for those
    two, and the gap is recorded in COMPLAINTS.md today. Not checked: Harris's
    §1 and §§3--5, which the card does not use, and no other published proof
    of the equality case was sought.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The event above, of the same day, had been rewritten in place by
    8e0b780484; it is restored here to the text it carried when d2786e384b
    wrote it, and this event carries the corrections, that one's and this
    pass's.

    Read for this pass: J. Harris, A bound on the geometric genus of
    projective varieties, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 8 (1981),
    §2, in tmp/sources/harris-1981-bound-geometric-genus.md, whose markers
    cover twenty pages at a time, so the display at printed p. 44 was located
    from the run of §2; Yang Pi-Yeh, solution 5.6.2, printed p. 115 of
    tmp/sources/lfwin-hartshorne-solutions.pdf, read in
    tmp/sources/lfwin-hartshorne-solutions.md; A. Egbert, V.6.2, printed
    p. 303 of tmp/sources/hartshorne-solutions-egbert.md, read in full; and
    Hartshorne V.6.2 with its hint, printed p. 423, with Proposition 8.20,
    printed p. 182, Theorem 5.4, printed p. 343, Theorem 1.6, printed p. 362
    and Remark 7.15, printed p. 248.

    Corrected: the previous text of this note named the wrong gap. Both
    entries assume p_g(X) not zero, so K_X is effective and H.K_X >= 0 is
    immediate for them, and neither leaves that step unproved. What they do
    leave out is the equality case of Clifford's theorem, and the card now
    transcribes their argument step by step for everything else: H.K_X = 0 in
    step canonical-meets-hyperplane-zero from adjunction with 2g-2 = d + H.K_X
    and d = 2g-2; the triviality of omega_X and p_g = 1 in step
    trivial-canonical-pg-one from an effective divisor of class K_X meeting
    the ample class in zero, which is Yang's and Egbert's argument through
    12K; and q = 0 in step irregularity-zero through Nakai--Moishezon, Kodaira
    vanishing, Serre duality and Riemann--Roch, which is theirs. Step
    main-dichotomy says the assembly is theirs. Step
    clifford-equality-canonical, the equality case of Clifford's theorem with
    the hyperelliptic alternative excluded by very ampleness, remains the
    card's own; it was on the card before this batch.

    Egbert's entry, printed p. 303, is a full sketch of both halves and not a
    garbled one; the earlier description of it in COMPLAINTS.md is that
    record's and is corrected in a new record of this date there. The remark
    no longer carries text-version paths, an account of what the two entries
    do not prove, or a list of which steps are the card's own (QUAL-08).
    Also corrected: Hartshorne's Theorem 6.1 is on printed p. 422, not p. 421.

    Not checked: Harris's §1 and §§3--5, which the card does not use, and no
    published proof of the equality case of Clifford beyond these two entries
    was sought. Yang's extraction prints the inequality "n+1 <= h^0(O_H(d)) =
    1-g+d", which cannot hold at d = 2n and g = n+1 with h^0(O_C(1)) = n+1,
    so the card transcribes his conclusion and Egbert's statement of the same
    steps rather than that line.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repaired on a reader's third report of this date, which is right on every
    point. The previous repair attributed to Yang and Egbert steps they do not
    print, and it left one published case marked as the card's own. Corrected,
    step by step, from the two entries read again in
    tmp/sources/lfwin-hartshorne-solutions.md (solution 5.6.2, printed p. 115
    of tmp/sources/lfwin-hartshorne-solutions.pdf) and
    tmp/sources/hartshorne-solutions-egbert.md (V.6.2, printed p. 303):

    Step nonspecial-implies-pg-zero: the case is published. Yang writes
    h^2(X,O_X) = h^1(C,O_C(1)), so a nonzero p_g makes L special, and
    Clifford's theorem with h^0(C,L) >= n+1 gives d >= 2n; Egbert states the
    same dichotomy. The step now says that, and the computation from
    adjunction, Serre duality and the omega_X(-m) chain is marked as the
    card's verification of the inequality the two of them use. "This step is
    the card's own" is removed.

    Step canonical-meets-hyperplane-zero: neither entry uses the equality case
    of Clifford's theorem. Yang's d = 2g - 2 comes from 2g-2 = d + H.K >= d,
    n+1 <= h^0(C,L) and 2n+2 <= 2-2g+2d <= d; Egbert's H.K >= 0 comes from
    D ~ rK_X with D effective for X not ruled, not from a nonzero canonical
    section. Both are now stated as they are, and the card's own route from
    omega_X restricted to C is marked as its own.

    Step trivial-canonical-pg-one: neither entry derives omega_X = O_X or
    p_g = 1. Yang has "Since X is not contained in any hyperplane, it is not a
    ruled surface. Then by theorem 6.2, we have |12K| != 0. So since
    12K = 0, kappa = 0 by theorem 6.3", and Egbert reaches |12K| nonempty from
    non-ruledness the same way. The step now records that and only that, and
    the passage from an effective divisor of class K_X meeting A in zero to
    omega_X = O_X and p_g = 1 is marked as the card's own.

    Step irregularity-zero: neither entry has h^0(X,A) >= n+2 or q = 0. Yang
    writes "then by 5.1.6, p_a(X) = 1, hence X is a K3 surface by theorem 6.3"
    and Egbert "using thm V.1.6, Riemann-Roch we get that p_a(X) = 1". The
    step now quotes those and derives q = 0 separately from p_a = p_g - q with
    p_g = 1; the count of h^0(X,A) is marked as the card's own route.

    The remark is rewritten to state what the two entries print, at their
    pages, and no longer says the steps transcribe them, no longer recites the
    card's own argument as theirs, and no longer carries the sentence about
    the one step a solution has to supply (QUAL-08, SEC-7).

    Also corrected, in this event and not in the event it corrects: the
    previous event of this date read Yang's "n+1 <= h^0(O_H(d)) = 1-g+d" as a
    claim about the equality case that cannot hold. It is the non-special
    hypothesis of his chain, which that chain refutes, and nothing in the card
    turns on it.

    Not checked: Harris's §1 and §§3--§5, which the card does not use, and no
    published proof of the equality case of Clifford's theorem beyond these two
    entries was sought.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    One sentence of step trivial-canonical-pg-one is corrected in the event
    above this one: it repeated Yang's reason for |12K| nonempty without
    naming it as his. Yang, printed p. 115, has "Since X is not contained in
    any hyperplane, it is not a ruled surface. Then by theorem 6.2, we have
    |12K| != 0." A ruled surface in PP^{n+1} can be nondegenerate -- P^1 x P^1
    in PP^3 is, of degree 2 = 2n for n = 2 -- so the inference is false as a
    general statement, and Egbert, printed p. 303, assumes X not ruled instead
    of deriving it. The step now names the inference as Yang's and not true in
    general, and records that the card does not need it: p_g(X) > 0 makes K_X
    effective, hence |12K_X| nonempty, in this case. Nothing else changes; no
    other step or line was read in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repaired on a reader's fourth report of this date, which is right on every
    one of its five points. Read for this pass: the card; Yang Pi-Yeh,
    solution 5.6.2, printed p. 115 of tmp/sources/lfwin-hartshorne-solutions.pdf,
    read in tmp/sources/lfwin-hartshorne-solutions.md; A. Egbert, V.6.2,
    printed p. 303, read in tmp/sources/hartshorne-solutions-egbert.md; and
    Hartshorne V.6 with exercises 6.1 and 6.2 on printed pp. 422--423, read in
    tmp/sources/hartshorne-1977-algebraic-geometry.md.

    Step canonical-meets-hyperplane-zero presented Yang's chain as a
    derivation. He prints "n+1 <= h^0(O_H(d)) = 1-g+d", and the card had
    dropped the "= 1-g+d"; with it, the chain's last inequality at d = 2n
    reads 2n+2 <= 2-2g+2d <= d, which with g >= n+1 from 2g-2 >= d is
    contradictory, so the chain refutes the non-special case, the case it was
    eliminating, and yields no d = 2g-2. His "so here we must have d=2g-2" is
    a non sequitur. The step now says that neither entry derives d = 2g-2 in
    this case, gives what each writes and takes, and marks the card's own
    derivation, from omega_X restricted to C and deg omega_C = 2g-2.

    The attribution "whence the same d=2g-2 and H.K_X=0" to Egbert is
    withdrawn: from 2g-2 = d + (1/r)H.D >= d he excludes the non-special case
    only, then writes "Then d=2n, g=n+1 so d=2(g-1)=2g-2" with no argument,
    and gets H.K = 0 from the genus formula n+1 = p_a(H) = 1 + (1/2)(2n + HK).

    Step trivial-canonical-pg-one cited Theorem 6.2 for the nonemptiness of
    the linear system of 12K. The book's Theorem 6.1, printed p. 422, is the
    criterion kappa = -1 iff that linear system is empty iff X is rational or
    ruled; Theorem 6.2, printed on the same page, is Castelnuovo's criterion
    p_a = P_2 = 0. Both entries print "theorem 6.2" here, the card had
    repeated their number as the book's, and the correction a remark of
    0d013c480b carried was lost in the later rewrite. The step now cites
    Theorem 6.1, and the remark records the number each entry prints.

    Step irregularity-zero misquoted the two entries' closing. They take
    H - K_X ample by Nakai--Moishezon; Kodaira vanishing on that ample class
    gives H^1(O_X(H)) = 0, and Serre duality H^1(O_X(K_X-H)) = 0, and the two
    entries print these two vanishings in the opposite order, naming Kodaira
    vanishing for the second group and Serre duality for the first. The card
    had attributed to Kodaira vanishing H^1(O_X(A)) = H^1(O_X(K_X+A)) = 0 and
    to Serre duality H^1(O_X(K_X-A)) = 0, which swaps the two, and it used
    K_X trivial, which neither entry has at that point. The step now states
    the chain that way, and records that both cite Exercise V.1.1 for the
    vanishing of h^0(X, O_X(K_X-H)), whose reason is that (K_X-H).H < 0 with
    H ample; the book's Exercise V.1.1 is the intersection-number identity and
    states no such vanishing.

    Step nonspecial-implies-pg-zero said the two entries use "this implication
    in the same form". Yang's printed form is the equality h^2(X,O_X) =
    h^1(C,O_C(1)), which his entry does not prove and which fails in general,
    h^1(C,L) being h^0(C, omega_X restricted to C) by adjunction and Serre
    duality; and Egbert's dichotomy is special against non-special for O_H(d),
    with no relation of p_g(X) to h^1(C,L). The step now states each route as
    printed and marks its own proof of the implication it states.

    The remark no longer says the equality case is published twice. No
    published derivation of it was located in the two entries read, and the
    case is named open in the COMPLAINTS.md record of this date headed "V.6.2's
    equality case is open in the sources read, and items (i) and (iv) of this
    date's earlier V.6.2 report are withdrawn". The card's own proof of it is
    kept, and steps clifford-equality-canonical and canonical-meets-hyperplane-zero
    say that it is the card's own.

    Not checked: Harris's section 1 and sections 3--5, which the card does not
    use; Yang's and Egbert's other V.6 entries; and no published proof of the
    equality case of Clifford's theorem beyond these two entries was sought.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repaired on a reader's fifth report of this date. It found the reading of
    the two entries right and moved three things off the rendered card: a
    misattributed argument in step trivial-canonical-pg-one, the attribution
    of step main-dichotomy, and the reading notes below, which the rendered
    solution and remark no longer carry (QUAL-08, SEC-7). No proof is added
    in this pass, and the equality case stays the card's own and open.

    How the two entries and the book were read here. Yang Pi-Yeh, solution
    5.6.2, at tmp/sources/lfwin-hartshorne-solutions.md line 2876, a single
    paragraph, printed p. 115 of tmp/sources/lfwin-hartshorne-solutions.pdf.
    A. Egbert, V.6.2, at tmp/sources/hartshorne-solutions-egbert.md, section
    "5.6.2 V.6.2 x g", lines 12941--12947, printed p. 303 of
    tmp/sources/hartshorne-solutions-egbert.pdf. Hartshorne's Theorem 6.1,
    Theorem 6.2 and Theorem 6.3 at
    tmp/sources/hartshorne-1977-algebraic-geometry.md lines 13078--13100,
    exercises V.6.1 and V.6.2 at lines 13107--13109, and Exercise V.1.1 at
    line 11467, printed pp. 422--423 and p. 366, the offset printed = PDF
    minus 15 holding from the PDF page markers in that file.

    Step trivial-canonical-pg-one no longer puts an argument into the
    entries' hands. It said that Yang and Egbert get 12K ~ 0 from H.(12K) = 0
    with H ample, and neither entry says that: Yang writes "So since 12K = 0,
    we have kappa = 0 by theorem 6.3" and Egbert "But then 12K ~ 0 so at
    least kappa = 0", each taking 12K ~ 0 as given once the nonemptiness is
    had. The step now records only what they print, the nonemptiness by
    Theorem 6.1 for X not ruled, 12K_X ~ 0, and kappa = 0 by Theorem 6.3, and
    quotes the two sentences. The observation that an effective divisor in
    the linear system of 12K meeting the ample class in zero must vanish is
    the card's, and the record of this date in COMPLAINTS.md already noted
    that Yang argues without it.

    Step main-dichotomy now says that the step is the card's own, and no
    longer that this is how the two entries conclude. Neither establishes
    that omega_X is O_X or that q = 0; both conclude from p_a(X) = 1 by
    Theorem 6.3, which step irregularity-zero records.

    Reading notes moved from the rendered text into this event, where they
    belong (QUAL-08, SEC-7). (1) Yang's identity h^2(X,O_X) =
    h^1(C,O_C(1)) is unproved in his entry and false in general: adjunction
    and Serre duality on C give h^1(C,L) = h^0(C, omega_X restricted to C),
    and the restriction H^0(X, omega_X) -> H^0(C, omega_X restricted to C)
    has kernel H^0(X, omega_X(-C)) and cokernel inside H^1(X, omega_X(-C)),
    neither of which vanishes in general. (2) Yang's reason for the
    nonemptiness, that X is not contained in a hyperplane and so is not
    ruled, is false in general: a ruled surface in PP^{n+1} can be
    nondegenerate, PP^1 x PP^1 in PP^3 being one. Neither entry needs it here
    and the card does not, p_g(X) > 0 making K_X effective. (3) Both entries
    name Kodaira vanishing for H^1(X,O_X(K_X - H)) and Serre duality for
    H^1(X,O_X(H)); with H - K_X ample, omega_X tensor O_X(H - K_X) is O_X(H),
    so Kodaira vanishing gives H^1(X,O_X(H)) = 0 and Serre duality
    H^1(X,O_X(K_X - H)) = 0. The step now states the two vanishings once,
    with the two theorems named and no order asserted. (4) Both cite
    Exercise V.1.1 for h^0(X,O_X(K_X - H)) = 0; the book's V.1.1, at line
    11467 above, is the identity C.D = chi(O_X) - chi(L^{-1}) -
    chi(M^{-1}) + chi(L^{-1} tensor M^{-1}), and the vanishing holds instead
    because (K_X - H).H = -d < 0 with H ample. (5) Both entries print
    "theorem 6.2" for the book's Theorem 6.1, the book's Theorem 6.2 being
    Castelnuovo's criterion; the remark no longer names their numbering, and
    the erratum stands here.

    What remains open is unchanged: no published derivation of the equality
    case of Clifford's theorem for V.6.2 was located, the case is the card's
    own in steps clifford-equality-canonical and
    canonical-meets-hyperplane-zero, and it is open under issue 121, as the
    records of this date in COMPLAINTS.md say.

    Not read here: Harris's section 1 and sections 3--5, which the card does
    not use, and Yang's and Egbert's other V.6 entries. Not searched: any
    other publication for a proof of the equality case.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The equality case is published after all: Hartshorne, Algebraic Geometry
    (1977), Theorem 5.4 (Clifford), statement printed p. 343 and proof
    printed pp. 343--345 (text version
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N is
    PDF p. N+15; PDF pp. 358--360), states the equality clause in full:
    equality holds exactly for D=0, D=K, or X hyperelliptic with D a multiple
    of the unique g^1_2, and proves it. Step clifford-equality-canonical
    applies that theorem and excludes the hyperelliptic alternative because
    O_C(1) is very ample. The earlier events of this card that record no
    published derivation of the equality case were looking for a published
    solution set and missed the book's own theorem; they stand as written on
    their dates and are superseded on this point by this event and by the
    record of this date in COMPLAINTS.md. The rendered step now cites the
    theorem and its pages instead of calling the step the card's own, and the
    remark states the same. With the strict case on Harris's bound, printed
    pp. 42--44, the card's proof of V.6.2 is on published sources throughout.
    Checked in this pass: the statement and proof of Theorem 5.4 at the pages
    named, and the application in step clifford-equality-canonical. Not
    checked: no other printed proof of the equality case was searched for,
    and the card's other steps were not re-derived.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Step trivial-canonical-pg-one's attribution is corrected: it said Yang and
    Egbert "record |12K_X| nonempty by Theorem 6.1", which is the book's number
    and not the number either source prints. Read in the text versions of
    tmp/sources/lfwin-hartshorne-solutions.md, Solution 5.6.2, and
    tmp/sources/hartshorne-solutions-egbert.md at its 5.6.2 entry: Yang writes
    "Then by theorem 6.2., we have |12K| != 0. So since 12K = 0, we have
    kappa = 0 by theorem 6.3", and Egbert "Assuming F is not ruled, then by thm
    V.6.2, 6.3, there is r > 0, D >= 0 with D ~ rK_X" and then "Since X is
    non-ruled then |12K| nonempty by thm 6.2". Both cite Theorem 6.2, and the
    statement they use is the book's Theorem 6.1, printed p. 422:
    kappa = -1 iff |12K| is empty iff X is rational or ruled. Theorem 6.2 on
    the same page is Castelnuovo's criterion p_a = P_2 = 0. The step now says
    which number each source prints and which theorem states what they use.
    The mathematics of the step was read in this pass and is unchanged: A.D = 0
    for the effective canonical divisor D because A is ample, hence D = 0, hence
    omega_X is trivial and p_g = 1 over C. Read and unchanged in this pass:
    steps clifford-equality-canonical, canonical-meets-hyperplane-zero,
    irregularity-zero and main-dichotomy, and the statement against the printed
    V.6.2, printed p. 423 (PDF p. 438, folio read). Not checked in this pass:
    the two sources' printed pages 115 and 303 were not re-read, the numbered
    statement being quoted in the text versions above.
---

::: {.problem}
Prove the following theorem of Chern and Griffiths.
Let $X$ be a nonsingular surface of degree $d$ in $\PP_{\CC}^{n+1}$, which is not contained in any hyperplane.
If $d<2 n$, then $p_g(X)=0$.
If $d=2 n$, then either $p_g(X)=0$, or $p_g(X)=1$ and $X$ is a K3 surface.

Hint: Cut $X$ with a hyperplane and use Clifford's theorem (IV, 5.4). For the last statement, use the Riemann-Roch theorem on $X$ and the Kodaira vanishing theorem (III, 7.15).
:::

::: {.solution}
Put
$$
A=\OO_X(1).
$$
Choose a general hyperplane section
$$
C\in\linearsystem{A}.
$$
By [[T-BERTINI|Bertini's theorem]], $C$ is a smooth irreducible curve.
Write
$$
L=A\restrict_C=\OO_C(1).
$$
Then
$$
\deg L=C^2=A^2=d.
$$

::: pf

::: {.pf-step #hyperplane-restriction-sections}
The hyperplane line bundle satisfies
$$
\boxed{h^0(C,L)\ge n+1.}
$$

::: pf-proof
Since $X$ is not contained in any hyperplane, restriction of ambient
linear forms gives an injection
$$
H^0(\PP^{n+1},\OO(1))
\hookrightarrow
H^0(X,A).
$$
Thus
$$
h^0(X,A)\ge n+2.
$$

The section defining $C$ gives the exact sequence
$$
0\longrightarrow\OO_X
\longrightarrow A
\longrightarrow L
\longrightarrow0.
$$
Since $X$ is an irreducible projective variety,
$$
h^0(X,\OO_X)=1.
$$
The image of $H^0(X,A)$ in $H^0(C,L)$ therefore has dimension
$$
h^0(X,A)-1\ge n+1.
$$
Hence $h^0(C,L)\ge n+1$.

This is the opening move of the book's hint for V.6.2, printed p. 423: cut
$X$ with a hyperplane and count sections of $\OO_C(1)$.
:::

:::

::: {.pf-step #harris-bound}
If $d<2n$, then
$$
\boxed{p_g(X)=0.}
$$

::: pf-proof
This is Harris's bound on the geometric genus. J. Harris, *A bound on the
geometric genus of projective varieties*, Ann. Scuola Norm. Sup. Pisa Cl.
Sci. (4) 8 (1981), §2, printed pp. 42--44.
Written for a surface in $\PP^{n+1}$, with $N=n+1$, the argument is as
follows.

Put
$$
M=\left[\frac{d-1}{N-2}\right],
\qquad
\varepsilon=d-1-M(N-2).
$$
The generic hyperplane section is a nondegenerate curve $C$ of degree $d$ in
$\PP^{N-1}$ (Harris, printed p. 42), and Riemann--Roch with the count
$h^0(C,\OO_C(l))-h^0(C,\OO_C(l-1))\ge l(N-2)+1$ for $l\le M$ gives
$$
h^0(C,\omega_C(-M+l))
\le
l\varepsilon+\binom{l}{2}(N-2)
$$
(Harris, printed p. 43).

The Poincaré residue sequence of the pair $C\subset X$,
$$
0\longrightarrow\Omega^2_X(-l)
\longrightarrow\Omega^2_X(-l+1)
\longrightarrow\omega_C(-l)
\longrightarrow0,
$$
gives $h^0(X,\Omega^2_X(-M+1))=0$ and then, summing the resulting
inequalities,
$$
h^0(X,\Omega^2_X(-M+l))
\le
\sum_{i=1}^{l-1}h^0(C,\omega_C(-M+i))
$$
(Harris, printed p. 43). At $l=M$ this reads
$$
p_g(X)
=
h^0(X,\Omega^2_X)
\le
\binom{M}{3}(N-2)+\binom{M}{2}\varepsilon,
$$
which is Harris's bound at printed p. 44 for dimension two.

Now $d<2n$ means $d\le2N-3$, so
$$
M=\left[\frac{d-1}{N-2}\right]\le2.
$$
If $M\le1$, both binomial coefficients vanish and the bound is $0$. If
$M=2$, then
$$
\varepsilon=d-1-2(N-2)\le 2N-3-1-2N+4=0,
$$
while $\varepsilon\ge0$ by its definition, so $\varepsilon=0$ and the bound
is $0$ again. Hence
$$
p_g(X)=0.
$$
:::

:::

::: {.pf-step #nonspecial-implies-pg-zero}
Whenever $H^1(C,L)=0$, one has
$$
\boxed{p_g(X)=0.}
$$

::: pf-proof
Adjunction (Hartshorne, Proposition 8.20, printed p. 182) gives
$$
\omega_C
\cong
(\omega_X\otimes A)\restrict_C,
$$
and therefore
$$
\omega_X\restrict_C
\cong
\omega_C\otimes L^{-1}.
$$
Serre duality on $C$ gives
$$
H^0(C,\omega_C\otimes L^{-1})
\cong
H^1(C,L)^\vee
=0.
$$

For every $m\ge0$, tensor the hyperplane-section sequence by
$\omega_X\otimes A^{-m}$:
$$
0
\longrightarrow
\omega_X\otimes A^{-(m+1)}
\longrightarrow
\omega_X\otimes A^{-m}
\longrightarrow
\omega_C\otimes L^{-(m+1)}
\longrightarrow0.
$$
The right-hand sheaf has no nonzero global section. Indeed, if it had a
section, multiplying by any nonzero section of $L^m$ would give a nonzero
section of
$$
\omega_C\otimes L^{-1},
$$
which has none. Hence for every $m\ge0$,
$$
H^0(X,\omega_X\otimes A^{-(m+1)})
\xrightarrow{\sim}
H^0(X,\omega_X\otimes A^{-m}).
$$
Iterating,
$$
h^0(X,\omega_X)
=
h^0(X,\omega_X\otimes A^{-m})
$$
for every $m$.

For $m\gg0$, the latter space is zero. Otherwise an effective divisor
$D_m$ would satisfy
$$
D_m\sim K_X-mA,
$$
so ampleness of $A$ would give
$$
0\le A\cdot D_m
=
A\cdot K_X-mA^2,
$$
which is impossible for sufficiently large $m$ because $A^2=d>0$.
Therefore
$$
p_g(X)=h^0(X,\omega_X)=0.
$$

Yang Pi-Yeh, printed p. 115, and Egbert, printed p. 303, reach the
non-special case by different routes. Yang writes
$h^2(X,\OO_X)=h^1(C,\OO_C(1))$, so a nonzero $p_g(X)$ makes $L$ special,
and Clifford's theorem with $h^0(C,L)\ge n+1$ gives $d\ge2n$, so that
$d<2n$ forces $p_g(X)=0$. Egbert splits on $\OO_H(d)$ itself, the case
$h^1\ne0$ giving $d\ge2n$ and $g-1\ge n$. The computation above, from
adjunction, Serre duality and the chain $\omega_X\otimes A^{-m}$, is the
card's own proof of the implication the step states.
:::

:::

::: {.pf-step #clifford-equality-canonical}
If $d=2n$ and $L$ is special, then
$$
\boxed{L\cong\omega_C.}
$$

::: pf-proof
Clifford's theorem (Hartshorne, Theorem 5.4, printed p. 343) and step [](#hyperplane-restriction-sections){.pf-ref} give
$$
n+1
\le
h^0(C,L)
\le
\frac d2+1
=
n+1.
$$
Thus equality holds in Clifford's theorem.

The divisor class $L$ is nonzero.
If equality came from the hyperelliptic case, then $L$ would be a
multiple of the unique $g^1_2$:
$$
L\cong f^*\OO_{\PP^1}(n)
$$
for the hyperelliptic double cover
$$
f:C\to\PP^1.
$$
Pullback gives an injective map
$$
H^0(\PP^1,\OO_{\PP^1}(n))
\hookrightarrow
H^0(C,L).
$$
Both spaces have dimension $n+1$: the source has that dimension, and
equality in the preceding Clifford estimate gives
$$
h^0(C,L)=n+1.
$$
Thus every section of $L$ is pulled back from $\PP^1$ and takes the same
value on the two points of each fiber of $f$. Hence $L$ could not be very
ample.
But $L=\OO_C(1)$ is very ample because it is the restriction of the
projective embedding.

The only remaining equality case in Clifford's theorem is therefore
$$
L\cong\omega_C.
$$

Clifford's theorem with its equality clause is Hartshorne, Theorem 5.4, printed
p. 343 and proved on pp. 343--345; the exclusion of the hyperelliptic case by
very ampleness is the one-line argument above.
:::

:::

::: {.pf-step #canonical-meets-hyperplane-zero}
In the special case of step [](#clifford-equality-canonical){.pf-ref},
$$
\boxed{K_X\cdot A=0.}
$$

::: pf-proof
Adjunction gives
$$
\omega_X\restrict_C
\cong
\omega_C\otimes L^{-1}.
$$
Step [](#clifford-equality-canonical){.pf-ref} identifies the right-hand side with $\OO_C$. Consequently
$$
\deg(\omega_X\restrict_C)=0.
$$
Since $C\sim A$, this degree is
$$
K_X\cdot A.
$$

Yang Pi-Yeh, solution 5.6.2, printed p. 115, and Egbert, V.6.2, printed
p. 303, reach this case too, and both assert $d=2g-2$ in it rather than
deriving it. Yang reads $2g-2=d+H\cdot K_X\ge d$ off adjunction, $K_X$ being
effective because $p_g(X)\ne0$, together with $n+1\le h^0(C,L)$ off
Clifford's theorem, and takes $d=2g-2$, $g=n+1$ and $H\cdot K_X=0$. Egbert
takes a nonzero effective $D$ with $D\sim rK_X$, which exists because $X$ is
not ruled, reads $2g-2=d+(1/r)H\cdot D\ge d$ off adjunction, then sets
$d=2n$, $g=n+1$ and $d=2g-2$, and reads $H\cdot K_X=0$ off the genus
formula $n+1=p_a(H)=1+\frac12(2n+H\cdot K_X)$. The computation above, from
$\omega_X\restriction_C\cong\OO_C$ and $\deg\omega_C=2g-2$, is the card's
own derivation of this step and of $d=2g-2$ in this case.
:::

:::

::: {.pf-step #trivial-canonical-pg-one}
If $d=2n$, $L$ is special, and $p_g(X)>0$, then
$$
\boxed{\omega_X\cong\OO_X}
$$
and
$$
\boxed{p_g(X)=1.}
$$

::: pf-proof
Choose a nonzero canonical section.
Its zero divisor $D$ is effective and satisfies
$$
D\sim K_X.
$$
By step [](#canonical-meets-hyperplane-zero){.pf-ref},
$$
A\cdot D
=
A\cdot K_X
=0.
$$
Since $A$ is ample, every nonzero effective curve has positive
intersection with $A$. Hence $D=0$.

A nowhere-vanishing section of $\omega_X$ trivializes it, so
$$
\omega_X\cong\OO_X.
$$
Because $X$ is an irreducible projective variety over $\CC$,
$$
h^0(X,\OO_X)=1.
$$
Thus
$$
p_g(X)
=
h^0(X,\omega_X)
=1.
$$

Yang, printed p. 115, and Egbert, printed p. 303, both cite "theorem 6.2" for the nonemptiness of $\linearsystem{12K_X}$ on a surface that is not ruled --- Yang's "Then by theorem 6.2., we have $\abs{12K}\neq0$" and Egbert's "$\abs{12K}\neq\emptyset$ by thm 6.2" --- and that statement is the book's Theorem 6.1, printed p. 422, $\kappa=-1\Leftrightarrow\linearsystem{12K}=\emptyset\Leftrightarrow X$ rational or ruled, while Theorem 6.2 on the same page is Castelnuovo's criterion. With it $12K_X\sim0$, and $\kappa(X)=0$ by Theorem 6.3, printed p. 422; Yang writes "So since $12K=0$, we have $\kappa=0$ by theorem 6.3" and Egbert "But then $12K\sim0$ so at least $\kappa=0$". The passage above,
from an effective divisor of class $K_X$ meeting the ample class $A$ in zero
to $\omega_X\cong\OO_X$ and $p_g(X)=1$, is the card's own.
:::

:::

::: {.pf-step #irregularity-zero}
Under the hypotheses of step [](#trivial-canonical-pg-one){.pf-ref},
$$
\boxed{q(X)=h^1(X,\OO_X)=0.}
$$

::: pf-proof
Put
$$
q=h^1(X,\OO_X).
$$
Step [](#trivial-canonical-pg-one){.pf-ref} gives $p_g=1$, so
$$
\chi(\OO_X)
=
1-q+p_g
=
2-q.
$$

Apply surface Riemann--Roch (Hartshorne, Theorem 1.6, printed p. 362)
[[T-SRFRR]] to $A$.
Since $K_X\sim0$ and
$$
A^2=\deg X=d=2n,
$$
one obtains
$$
\chi(A)
=
\chi(\OO_X)+\frac12A\cdot(A-K_X)
=
(2-q)+n
=
n+2-q.
$$

By Kodaira vanishing (Hartshorne, Remark 7.15, printed p. 248)
[[T-KODVAN]], using
$$
A\cong\omega_X\otimes A
$$
and the ampleness of $A$,
$$
H^i(X,A)=0
\qquad
(i>0).
$$
Hence
$$
h^0(X,A)
=
\chi(A)
=
n+2-q.
$$

The given nondegenerate embedding
$$
X\hookrightarrow\PP^{n+1}
$$
supplies $n+2$ linearly independent global sections of $A$. Therefore
$$
n+2
\le
h^0(X,A)
=
n+2-q.
$$
Thus $q\le0$, and hence
$$
q=0.
$$

Yang, printed p. 115, and Egbert, printed p. 303, close as follows. By
Nakai--Moishezon $H-K_X$ is ample, and Kodaira vanishing and Serre duality
give $H^1(X,\OO_X(H))=H^1(X,\OO_X(K_X-H))=0$, since
$\omega_X\otimes\OO_X(H-K_X)\cong\OO_X(H)$. Since $(K_X-H)\cdot H=-d<0$ with
$H$ ample, $H^0(X,\OO_X(K_X-H))=0$; Riemann--Roch then gives $p_a(X)=1$, in
Yang's words "then by 5.1.6, $p_a(X)=1$, hence $X$ is a K3 surface by
theorem 6.3" and in Egbert's "using thm V.1.6, Riemann--Roch we get that
$p_a(X)=1$", after which Theorem 6.3, printed p. 422, makes $X$ a K3
surface. With $p_a=p_g-q$ and $p_g=1$ this gives $q=0$. The count of
$h^0(X,A)$ above is the card's own route to the same number, and it uses
$K_X\sim\OO_X$ from step [](#trivial-canonical-pg-one){.pf-ref}.
:::

:::

::: {.pf-step #main-dichotomy}
If $d<2n$, then $p_g(X)=0$. If $d=2n$, then either
$p_g(X)=0$, or $p_g(X)=1$ and $X$ is a K3 surface.

::: pf-proof
For $d<2n$, step [](#harris-bound){.pf-ref} gives
$$
p_g(X)=0.
$$

Now assume $d=2n$.
If $L$ is nonspecial, step [](#nonspecial-implies-pg-zero){.pf-ref} again gives $p_g(X)=0$.
If $L$ is special, step [](#clifford-equality-canonical){.pf-ref} gives $L\cong\omega_C$.
If in addition $p_g(X)=0$, this is the first alternative in the theorem.
Otherwise steps [](#trivial-canonical-pg-one){.pf-ref} and [](#irregularity-zero){.pf-ref} give
$$
\omega_X\cong\OO_X,
\qquad
p_g(X)=1,
\qquad
q(X)=0.
$$
A smooth projective surface over $\CC$ with trivial canonical bundle and
$H^1(X,\OO_X)=0$ is a K3 surface, which is how Theorem 6.3, printed p. 422,
defines one. Hence the second alternative is exactly that $X$ is K3. This
step is the card's own.
:::

:::

::: pf-qed
Step [](#harris-bound){.pf-ref}, Harris's bound, proves the strict inequality case. Steps [](#clifford-equality-canonical){.pf-ref}, [](#canonical-meets-hyperplane-zero){.pf-ref}, [](#trivial-canonical-pg-one){.pf-ref}, [](#irregularity-zero){.pf-ref} and [](#main-dichotomy){.pf-ref}
analyze the equality case and give precisely the two alternatives stated
in the theorem.
:::

:::
:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.6, exercise 6.2, printed p. 423, with the hint printed there: cut $X$ with a hyperplane and use Clifford's theorem (IV, 5.4, printed p. 343), and for the last statement use Riemann--Roch on $X$ (Theorem 1.6, printed p. 362) and Kodaira vanishing (Remark 7.15, printed p. 248).

The strict inequality is Harris's theorem. J. Harris, *A bound on the geometric genus of projective varieties*, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 8 (1981), §2, printed pp. 42--44, bounds the geometric genus of a nondegenerate variety of dimension $k$ and degree $d$ in $\PP^N$ by
$$p_g\le\binom{M}{k+1}(N-k)+\binom{M}{k}\varepsilon,\qquad M=\left[\frac{d-1}{N-k}\right],\quad \varepsilon=d-1-M(N-k),$$
and records that the geometric genus vanishes whenever $d\le k(N-k)+1$ (printed p. 44). For a surface, $k=2$ and $N=n+1$, so $d<2n$ is $d\le2n-1=2(N-2)+1$ and gives $p_g(X)=0$; step [](#harris-bound){.pf-ref} transcribes the two displays this uses, at printed pp. 42--44.

The equality case $d=2n$ is treated by Yang Pi-Yeh, *Hartshorne Solutions*, solution 5.6.2, printed p. 115, and by A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.6.2, printed p. 303. Yang reads $h^2(X,\OO_X)=h^1(C,\OO_C(1))$ and applies Clifford's theorem to get $d\ge2n$ when that group is nonzero; for $d=2n$ he writes $2g-2=d+H\cdot K_X\ge d$ from adjunction and $n+1\le h^0(\OO_H(d))=1-g+d$, and takes $d=2g-2$, $g=n+1$ and $H\cdot K_X=0$; he records $12K\sim0$ and $\kappa(X)=0$ by Theorem 6.3, printed p. 422, having got $\linearsystem{12K}$ nonempty by Theorem 6.1, printed p. 422; and he closes with $(K_X-H)\cdot H<0$, Exercise V.1.1, $H-K_X$ ample by Nakai--Moishezon, Kodaira vanishing, Serre duality, Riemann--Roch on $X$ (his 5.1.6, Theorem 1.6 printed p. 362) giving $p_a(X)=1$, and Theorem 6.3. Egbert splits on $\OO_H(d)$ itself, takes a nonzero effective $D\sim rK_X$ for $X$ not ruled, and reads $2g-2=d+(1/r)H\cdot D\ge d$ from adjunction; he writes $d=2n$, $g=n+1$ and $d=2(g-1)$, gets $H\cdot K_X=0$ from the genus formula $n+1=p_a(H)=1+\frac12(2n+H\cdot K_X)$, and closes through Theorem V.1.6 with $p_a(X)=1$ and Theorem 6.3.

The equality case itself is the book's own Theorem 5.4: its statement, including the classification of equality as $D=0$, $D=K$, or $C$ hyperelliptic with $D$ a multiple of the $g^1_2$, is printed on p. 343 and its proof on pp. 343--345. Step [](#clifford-equality-canonical){.pf-ref} applies it and excludes the hyperelliptic alternative because $\OO_C(1)$ is very ample. Neither entry above supplies that argument: Yang's chain in the equality case reads $2g-2=d+H\cdot K_X\ge d$ against $n+1\le h^0(\OO_H(d))=1-g+d$, which at $d=2n$ gives $g\le n$ and $g\ge n+1$ and so refutes only the non-special case, while Egbert's $d=2(g-1)$ is the Clifford equality step left unstated.
:::
