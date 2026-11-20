---
schema: qual/card@1
id: P-AGH528STABLEBUNDLE
kind: problem
title: Stability of rank two bundles and classification of the unstable indecomposables
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
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.8 and the retained companion proof. The corpus
    transcription in part (c) said "up to isomorphism"; that statement is
    false because tensoring by any line bundle preserves rank, indecomposability,
    and (non-)semistability while generally changing the isomorphism class.
    The companion proof itself twists the unique maximal destabilizing line
    subbundle to O_C before extracting the extension data. The selected card is
    therefore repaired to the mathematically coherent classification up to
    tensoring by an invertible sheaf. The proof below also supplies the
    boundedness and uniqueness of the maximal destabilizing line subbundle.
- event: source-corrected
  by: chatgpt
  date: 2026-09-18
  note: Replaced the impossible "up to isomorphism" in part (c) by "up to tensoring with an invertible sheaf".
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
    exercise 2.8, printed page 384. Checked every step: the slope
    rearrangement of s1, with the saturation case added because a line
    subbundle whose quotient has torsion is not one of the quotients the
    printed definition tests; the boundedness of degrees of line subbundles in
    s7 via E-dual(n) globally generated; the uniqueness of the maximal-degree
    subbundle in s8 from the nonzero map A tensor B -> det E; the Ext
    identification of s10; and the Serre-duality bound e <= 2g-2 of s11.
    Confirmed the printed defect independently: tensoring by a line bundle of
    degree m preserves indecomposability, non-semistability and the normalized
    data (e, L, xi) while changing the degree from -e to 2m-e, so the printed
    "up to isomorphism" cannot hold and the classification is up to tensor
    equivalence. Searched outside the twelve retained sets: Algebraic Geometry
    II, National Taiwan University, 2020 Spring, Chapter V homework, Exercise 8
    of section 2, PDF p. 8 (tmp/sources/ntu-ag2-chapter5.pdf), whose (c) is the sentence "This is just
    the proof of Theorem 2.12, combined with (b)"; Yang Pi-Yeh, Hartshorne
    Solutions, exercise 5.2.8, printed pp. 103-104
    (tmp/sources/lfwin-hartshorne-solutions.pdf), which repeats "up to
    isomorphism"; and Egbert, PDF pp. 265-266. None repairs the printed clause.
    Not checked: whether Hartshorne intended the clause to classify the
    normalized models only; the card states the printed wording and proves the
    tensor-equivalence reading.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes and Pedreira (arXiv:math/0006204v3) on 2026-11-16: it states no
    stability condition for locally free sheaves on a curve, so it does not reach
    part (c); its Theorem 3.2 is a citation of the book's Theorem V.2.12. Two
    Math StackExchange threads were saved for the section, neither bearing on (c):
    4398506, tmp/sources/mse-4398506-hart77-v25-linear-system-notation.md, asks
    only what the notation $\linearsystem{D+K-E}+E$ of V.2.5(b) means, and 5101697,
    tmp/sources/mse-5101697-hart77-v2-elementary-transformation.md, asks how
    Hartshorne's E' = pi_*(O(1) x I_P) realises the elementary transformation of
    Example V.5.7.1, printed p. 416, which the questioner proves and KReiser's
    accepted answer confirms, with a proof that a section through the blown-up
    point exists. No complete published argument for (c) was located, and the
    printed "up to isomorphism" stays defective as recorded at the head of the
    solution: a bundle and its twist by a line bundle of nonzero degree carry the
    same triple and have different determinants.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the reference in the event above and restored the event of
    2026-11-11 to its text of that date. The elementary transformation is the
    book's Example V.5.7.1, printed p. 416, where the monoidal transform at a
    point of a fibre is blown down along the strict transform of that fibre; it
    is not V.2.11, which is the base-point-freeness and very-ampleness criterion
    for C_0 + bf. The page was read in the text version of the book: the example
    sits on the PDF page before the marker for PDF p. 432, so printed p. 416 at
    the offset 15 this book's extractions take. The text-version names that a
    later commit of 2026-11-16 put into the event of 2026-11-11 are removed, and
    every source cited in the remark names its text version. Nothing else in the
    audit changes: no complete published argument for (c) was located, and the
    printed "up to isomorphism" stays defective.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcribed all three parts on 2026-11-16 from Gunning, Lectures on vector
    bundles over Riemann surfaces, read in the text version
    tmp/sources/gunning-1967-vector-bundles-riemann-surfaces-pp69-92.md, whose
    OCR corrupts most displayed formulas but whose statements and arguments are
    legible in outline, and from the book's own Theorem 2.12 and Example 2.11.6;
    re-read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.2,
    exercise 2.8, printed p. 384 (PDF p. 399), whose part (c) still reads "up to
    isomorphism". Printed pages of Gunning were established from the PDF's
    folios, printed page = PDF page - 9: Theorem 13 on printed pp. 71-74,
    Lemma 14 on pp. 81-82, the stability definitions and div Phi on pp. 82-83,
    Lemma 15 on pp. 83-85, Theorem 14 on pp. 87-90. (a) is Gunning's remark that
    div Phi is at least (1/rank)c(det Phi) for a decomposable bundle, from his
    Lemma 14; (b) is his "Phi is stable precisely when div Phi < half c(xi)"
    together with div E = 0 for a normalized E; the uniqueness of the maximal
    subbundle is Lemma 15(i), whose proof by the two diagonal bundles is carried
    in step s8; and the classification of (c) is Theorem 14, with phi = O and
    xi = L, so that the parameter space is P H^1(C, L^dual) and proportional
    classes give isomorphic middle bundles. The bound 0 < e <= 2g-2 is the
    argument of the book's Theorem 2.12, printed p. 376. Checked that
    non-semistability is div E > half deg E, not the weak inequality, which is
    what makes Lemma 15(i) apply. Not checked: whether Gunning's displayed
    computations in Lemma 15 and Theorem 14 are free of error, which the OCR
    does not permit; the steps that depend on them are carried by their
    statements alone and by the rank-two arguments written on the card. The
    printed "up to isomorphism" stays defective, and the card classifies
    tensor-equivalence classes.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the card against its sources again on 2026-11-16, after the event
    above of the same date. Part (a) is now proved for any rank, as the exercise
    states it: Gunning's Lemma 14, printed pp. 81-82, gives div Phi at least
    (1/m)c(det Phi) for a decomposable Phi of rank m, and the passage from line
    subbundles to locally free quotients for m greater than 2 is marked as the
    card's own. The bound on subbundle degrees that step s7 needs is Gunning's,
    printed p. 80 in the paragraph before his (9), where he shows c(phi) at most
    max c(Psi_j) over the diagonal bundles of a complete reduction and says that
    those Chern classes are bounded from above; the earlier sentence calling
    that bound the card's is withdrawn, and the card's global-generation proof
    is kept as a second proof. Semistability is the exercise's definition, not
    Gunning's, who defines stability and instability only; step s6 now says so
    and is marked as the card's own. The proof of Proposition 2.8 ends on
    printed p. 372, not p. 373. Theorem 14 is stated for a compact Riemann
    surface, so step s12 says which part of it carries the classification
    without that setting, namely the direct rank-two argument. Not checked:
    whether the classification of part (c) holds in positive characteristic;
    nothing in the sources read states it there, and the card does not claim it.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the card again on 2026-11-16 on the reader's report, after the
    event above of the same date, which is left as written. Three corrections.
    First, part (a) is proved again in rank two only, as the card proved it
    before this batch. The argument the event above records for any rank is
    withdrawn and was wrong twice: Gunning's Lemma 14, printed pp. 81-82,
    treats a decomposable bundle written as a direct sum of line bundles, and a
    decomposable bundle of rank three or more is not in general such a sum; and
    the translation written on the card exhibited a rank-one quotient of slope
    at least mu(Phi), which is not the inequality that contradicts stability,
    since stability requires every quotient's slope to exceed mu(Phi). Step s2
    now carries the rank-two argument through step s1, is marked as the card's
    own, and states Lemma 14 with its hypothesis. Part (a) for a decomposable
    bundle of higher rank is not proved here, and no source read proves it.
    Second, the remark's sentence that the rank-two argument of step s12
    carries part (c) without Gunning's setting is withdrawn: step s12's
    rank-two argument proves only that the constructed bundle is
    indecomposable, and the injectivity of the classification rests on Theorem
    14, a statement about a compact Riemann surface. Steps s12, s13, the qed
    and the remark now say that part (c) is established for a curve over the
    complex numbers, which is what the record of this date says as well.
    Third, the same remark sentence is where the card claimed the setting
    without giving it; the remark now names what Theorem 14 supplies and what
    step s12 supplies. Read for this repair: Gunning's §(c), Lemma 14 and
    Theorem 14 in the text version
    tmp/sources/gunning-1967-vector-bundles-riemann-surfaces-pp69-92.md, whose
    OCR garbles the displays, so the statements were taken from its sentences
    and the mathematics checked on the card. Not checked: whether Gunning's
    displayed computations in Lemma 14 and Theorem 14 are free of error, and
    whether part (a) holds in rank above two, which is a question about the
    exercise and not about the sources read.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Repaired the card on 2026-11-19 for issue #159. Re-read the printed exercise
    at Hartshorne, Algebraic Geometry (1977), V.2, exercise 2.8, printed p. 384
    (PDF p. 399): its (c) reads "classified, up to isomorphism, by giving (1) an
    integer 0 < e <= 2g-2, (2) an element L in Pic C of degree -e, and (3) a
    nonzero xi in H^1(L^dual) determined up to a nonzero scalar multiple", and
    the printed "up to isomorphism" is false, since tensoring by an invertible
    sheaf of nonzero degree preserves indecomposability and non-semistability
    and leaves the triple (e, L, xi) fixed while changing the determinant. Under
    QUAL-01 the statement now reads "up to tensoring with an invertible sheaf",
    which is what steps s9 to s13 prove, and it records the field: "for C a
    curve over C", Gunning's Theorem 14 being a statement about a compact
    Riemann surface. Part (a) is now proved in every rank, where the event above
    of 2026-11-16 says it was not and no source read proves it; that event is
    left as written and this one supersedes it. The proof is Yang Pi-Yeh,
    Hartshorne Solutions, Solution 5.2.8(a), printed pp. 103-104, read on the
    retained PDF: the solution displays the weighted mean
    mu(E) = (r'/(r'+r''))mu(E') + (r''/(r'+r''))mu(E'') at its head on printed
    p. 104 and argues "If E = F (+) G is stable, we may assume mu(F) <= mu(G).
    Then consider the morphism E -> F -> 0, we have mu(E) < mu(F). Since
    mu(F) <= mu(E) <= mu(G), we have mu(E) < mu(F) <= mu(E), which is
    impossible". The two summand quotient sequences are also in Algebraic
    Geometry II, National Taiwan University, 2020 Spring, Chapter V Surfaces
    homework, Exercise 8 of section 2 (Tzu-Yang Chou), PDF p. 8 of
    tmp/sources/ntu-ag2-chapter5.pdf, which concludes that "looking at the
    slopes we see that E can not be stable". Read for the rank-two statements:
    Gunning, printed p. 82 for the decomposable clause of Lemma 14 with its
    hypothesis, a direct sum phi_1 (+) ... (+) phi_m of line bundles, which the
    card now states with (13) as its proof; printed p. 85 for "every
    decomposable bundle is unstable"; printed pp. 83-85 for Lemma 15; and
    printed pp. 87-90 for Theorem 14. The pages were checked on rendered pages
    of tmp/sources/gunning-1967-vector-bundles-riemann-surfaces.pdf at 150 dpi,
    printed page = PDF page - 9, the folio "-85-" on PDF p. 94 confirming the
    offset there; the text version
    tmp/sources/gunning-1967-vector-bundles-riemann-surfaces-pp69-92.md has no
    page markers and its OCR garbles the displays. Not checked: whether part (c)
    holds in positive characteristic, which nothing read here states and which
    the statement does not claim.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The card used the word "normalized" in parts (b) and (c) and in its steps
    without saying what it means. Read on 2026-11-19 in
    tmp/sources/hartshorne-1977-algebraic-geometry.md: Notation 2.8.1, printed
    p. 373, names a rank-two bundle normalized when it satisfies the hypothesis
    of Proposition 2.8, printed p. 372, which is H^0(C, E) nonzero and
    H^0(C, E (x) M) = 0 for every invertible sheaf M of negative degree; the
    book's own index enters the word at printed p. 373. The solution now states
    that condition before the proof and writes the degree of a normalized bundle
    as -e. Step s4 now derives "O_C is a line subbundle" from the first clause,
    with step s3 bounding its degree, and step s3 cites printed p. 373 for the
    vanishing rather than Proposition 2.8 alone. Nothing else on the card
    changes, and no claim is weakened: a normalized bundle may have negative
    degree, as Example 2.11.3, printed p. 374, shows for O_C (+) L with
    deg L < 0.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Part (c) was stated for a curve over C only because steps s12 and s13 rested
    on Gunning's Theorem 14, printed pp. 87-90, a theorem about a compact
    Riemann surface. Read for this repair on 2026-11-19: the chapter's standing
    convention, that "curve" means a complete nonsingular curve over an
    algebraically closed field k, Chapter IV, printed p. 294, checked on the
    page rendered at 130 dpi from tmp/sources/hartshorne-1977-algebraic-geometry.pdf
    (PDF p. 309, folio 294); and Gunning's Theorem 14 with its proof, printed
    pp. 87-90, read in
    tmp/sources/gunning-1967-vector-bundles-riemann-surfaces-pp69-92.md with its
    statement and the outset of the proof on printed pp. 87-88 rendered at
    150 dpi from the PDF beside it (PDF pp. 96-97, folios -87- and -88-), where
    the correspondence is stated as a one-to-one correspondence between the
    bundles of rank 2 with subbundle phi and determinant xi and the points of
    P^n of dimension n = dim H^1(M, O(phi^2 xi^{-1})) - 1, and where the
    equivalence of bundles is (20), Phi'_{alpha beta} = theta_alpha Phi_{alpha
    beta} theta_beta^{-1}, which is what makes the criterion at (24) the
    proportional-classes criterion. That reading confirms the card's earlier
    description of Lemma 14 and Theorem 14 and changes nothing in it. What
    changes is that the classification no longer needs that setting: in rank two
    the injectivity is available over any algebraically closed field, so part
    (c) now reads as the exercise prints it, with the chapter's convention as
    its only hypothesis, and a new step s12b proves that two extensions of an
    invertible sheaf L of negative degree have isomorphic middle terms exactly
    when their classes differ by a nonzero scalar. Its argument: the composite
    of a line subbundle M of the middle term with the quotient map to L is
    either zero, forcing M into O_C and deg M <= 0 with equality only at O_C, or
    injective, forcing deg M <= deg L < 0; so O_C is the unique line subbundle
    of degree 0, an isomorphism of middle terms must carry O_C to O_C, and the
    scalars it induces on O_C and on L move the extension class by a nonzero
    scalar. Steps s12 and s13 cite that step in place of Theorem 14, the qed
    says part (c) over an algebraically closed field of any characteristic, and
    the remark keeps Theorem 14 as the published argument over C. Parts (a) and
    (b), the bound 0 < e <= 2g-2, and the boxed data of part (c) are unchanged.
    Not checked: whether section V.2 restates the chapter's convention anywhere,
    which its opening pages do not; and whether the classification extends to a
    ground field that is not algebraically closed, which nothing here claims.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The published-solution remark's sentence on Egbert said that his route
    through "E stable implies every nonzero morphism E -> E is an isomorphism"
    "fails for the endomorphism id + 0 of a decomposable bundle", which reads as
    a defect of his argument. Read on 2026-11-19 in the retained extraction
    tmp/sources/hartshorne-solutions-egbert.md at his entries 5.2.13 to 5.2.15,
    which carry V.2.8(a)-(c) and name PDF p. 265: his (a) states "A decomposable
    E is a direct sum of two invertible sheaves", proves the claim from the
    slope inequalities by factoring a nonzero endomorphism through its image,
    and applies it to id_G + 0 on a decomposition. The claim is true of a stable
    bundle and uses no rank hypothesis, so nothing in his argument fails for
    id + 0; what restricts his (a) is the sentence with which he states it. The
    remark now says that his statement of (a) is the rank-two case and that his
    argument as written uses nothing about the ranks, and it no longer imputes a
    failure to the argument.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read on 2026-11-19 the Gunning pages this card cites outside printed
    pp. 81-82 and 87-90, and repaired four page references. Printed p. 71
    carries (1) and (2), which define an extension and the equivalence of two
    extensions; Theorem 13 opens printed p. 72 with "the trivial extension
    phi_1 (+) phi_2 corresponds to the zero element of the group", so the
    theorem is printed pp. 72-74, not 71-74 as step s10 had it. Printed p. 80
    carries (9), div Psi = max c(phi) over subbundles, which step s1 had
    attributed to pp. 82-83. Printed p. 83 carries the definitions of stable and
    unstable; the sentence "phi is stable precisely when div phi < (1/2)c(xi)"
    and (16) open printed p. 84, where Lemma 15 states its parts (i) and (ii),
    so step s5 now gives p. 84 for that sentence and step s8 and the remark give
    pp. 84-85 for Lemma 15. Lemma 14, printed pp. 81-82; section (c) on printed
    p. 83; Theorem 14, printed pp. 87-90; and "every decomposable bundle is
    unstable" on printed p. 85 stand as the card has them. The pages were read
    as renders at 150 dpi of
    tmp/sources/gunning-1967-vector-bundles-riemann-surfaces.pdf, PDF pp. 80,
    81, 90, 91, 92, 93, 94, 96, 97, 98 and 99, printed page = PDF page - 9, the
    folios -71- to -90- read on those renders. No mathematical claim changes.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Step s6 said that the semistable criterion "is the card's own" because
    Gunning states no semistable one. Both directions of part (b) are in the
    published sets, and the sentence now names them: Yang Pi-Yeh, Hartshorne
    Solutions, Solution 5.2.8(b), printed p. 104, which runs the two directions
    with the parentheses "(> )" and "(>=)" carrying the strict and weak cases
    and contradicts normalization by a section of E (x) F^vee with deg F^vee
    negative; and Exercise 8(b) of the National Taiwan University set (Tzu-Yang
    Chou), PDF p. 8, which gives the same two directions in the same order. Read
    on 2026-11-19 in tmp/sources/lfwin-hartshorne-solutions.md at printed
    pp. 103-104, the folios checked on the retained PDF, and in
    tmp/sources/ntu-ag2-chapter5.md at PDF p. 8. The argument of steps s3 to s6
    is unchanged; what changes is that the card no longer claims the semistable
    direction as its own.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Part (c) checked for its ground field, the row of issue #160 for this
    exercise, which recorded that Gunning is a book about compact Riemann
    surfaces. The classification is carried by steps s10, s11, s12 and s12b,
    none of which uses more than Ext^1 = H^1, Serre duality and the elementary
    theory of line bundles on a complete curve, and Gunning's Theorem 14,
    printed pp. 87-90, is named only as the characteristic-zero alternative.
    Checked on this pass: step s11's bound, h^1(L^v) nonzero implies
    deg L^v <= 2g-2 by IV.1.3.4, equivalently a nonzero section of K_C + L of
    degree 2g-2-e; and step s12b's injectivity in rank two, where the point
    that needs the sign is that a line subbundle M of a middle term either maps
    injectively to L, giving deg M <= deg L < 0, or lies in the kernel O_C,
    giving deg M <= 0 with equality only for O_C itself, so O_C is the unique
    line subbundle of degree 0 and an isomorphism carries it to the
    corresponding one; the automorphisms of O_C and of L are then nonzero
    constants because H^0(C,O_C) = k, so the two classes differ by a scalar.
    The same sign is what makes the indecomposability argument of step s11
    valid: a decomposition of the middle term would put O_C on one side and a
    summand isomorphic to L of negative degree on the other, so the given
    inclusion would be the summand one and the class would vanish. Read for
    this pass: steps s10, s11, s12 and s12b of this card, Hartshorne's
    Theorem 2.12 with its proof, printed pp. 375-376, and the statements of
    Gunning's Theorem 13 and Theorem 14 at the printed pages the card records,
    in tmp/sources/gunning-1967-vector-bundles-riemann-surfaces-pp69-92.md.
    Not checked: steps s3 to s9 were read for their field hypotheses only, not
    re-derived, and no printing other than the text versions beside the
    retained PDFs.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    A sign in the remark on the printed part (c) is corrected, and no
    mathematics of the proof changes. The remark wrote det E = L^{-1} of
    degree -e, which is inconsistent with its own data: part (c) gives L of
    degree -e and xi in H^1(L^v), the extension 0 -> O_C -> E -> L -> 0
    attached to xi has det E = L, as step s12 also states, so the degree of
    the determinant is -e and the range [-2g+2,-1] is the range of -e. The
    corrected sentence is what the twisting comparison uses: det(E tensor M) =
    L tensor M^2, of degree -e + 2 deg M. Read for this: the printed exercise
    on printed p. 384 and steps s10, s11, s12, s12b and s13 of this card, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md. Not checked: any
    printing of the book, only the text version retained in tmp/sources.
---

::: {.problem}
Throughout, $C$ is a complete nonsingular curve over an algebraically closed field $k$, as the chapter's convention has it (IV, printed p. 294). A locally free sheaf $\mathcal{E}$ on a curve $C$ is said to be **stable** if for every quotient locally free sheaf
$$
\mathcal{E} \rightarrow \mathcal{F} \rightarrow 0, \qquad \mathcal{F} \neq \mathcal{E}, \mathcal{F} \neq 0
,$$
we have
$$
(\deg \mathcal{F}) / \rank \mathcal{F}>(\deg \mathcal{E}) / \rank \mathcal{E}
.$$
Replacing $>$ by $\geqslant$ defines **semistable**.

(a) A decomposable $\mathcal{E}$ is never stable.

(b) If $\mathcal{E}$ has rank 2 and is normalized, then $\mathcal{E}$ is stable (respectively, semistable) if and only if $\deg \mathcal{E}>0$ (respectively, $\geqslant 0$).

(c) Show that the indecomposable locally free sheaves $\mathcal{E}$ of rank 2 that are not semistable are classified, up to tensoring with an invertible sheaf, by giving

   (1) an integer $0<e \leqslant 2 g-2$,

   (2) an element $\mathcal{L} \in \Pic C$ of degree $-e$, and

   (3) a nonzero $\xi \in H^1\left(\dualof{\mathcal{L}}\right)$, determined up to a nonzero scalar multiple.

:::

::: {.solution}
For a nonzero locally free sheaf $\mathcal F$ on $C$, write
$$
\mu(\mathcal F)=\frac{\deg\mathcal F}{\rank\mathcal F}.
$$

A rank-two bundle $\mathcal E$ is normalized when $H^0(C,\mathcal E)\ne0$ and $H^0(C,\mathcal E\tensor\mathcal M)=0$ for every invertible sheaf $\mathcal M$ of negative degree, the condition of Proposition 2.8, which the book names at Notation 2.8.1, printed p. 373; its degree is then written $-e$, so $e=-\deg\mathcal E$.

The data of part (c) are the data of the normalized model of a bundle, and tensoring by an invertible sheaf moves the bundle without moving them. Let $\mathcal E_0$ be normalized, not semistable, with data $(e,\mathcal L,\xi)$, and let $\mathcal A$ be a line bundle of degree $m\ne0$. Tensoring by $\mathcal A$ shifts every slope by $m$, so the maximal-degree line subbundle of $\mathcal E_0\tensor\mathcal A$ is $\OO_C\tensor\mathcal A$, and the data read off from it are
$$
\det(\mathcal E_0\tensor\mathcal A)\tensor(\OO_C\tensor\mathcal A)^{-2}
\cong\det\mathcal E_0,\qquad
(\mathcal E_0\tensor\mathcal A)\tensor(\OO_C\tensor\mathcal A)^{-1}\cong\mathcal E_0,
$$
so $e$, $\mathcal L$ and $\xi$ are unchanged, while $\deg(\mathcal E_0\tensor\mathcal A)=2m-e\ne-e=\deg\mathcal E_0$ and the two bundles have different determinants, hence are not isomorphic. Part (c) therefore classifies these bundles up to tensoring with an invertible sheaf, which is the form step [](#s13){.pf-ref} proves.

::: pf

::: {.pf-step #s1}
For a rank-two bundle $\mathcal E$, stability is equivalent to
$$
\deg\mathcal A<\frac12\deg\mathcal E
$$
for every line subbundle $\mathcal A\subsetneq\mathcal E$, and semistability to the same inequalities with $\le$.

::: pf-proof
Gunning, *Lectures on vector bundles over Riemann surfaces*, §(c), printed p. 83, defines $\Phi$ to be stable when $c(\varphi)<\frac12c(\det\Phi)$ for every line bundle $\varphi\subset\Phi$, and unstable otherwise, and sets $\operatorname{div}\Phi=\max_{\varphi\subset\Phi}c(\varphi)$, which is his (9), printed p. 80; the exercise states the same condition for locally free quotients. A rank-two bundle with a locally free nonzero proper quotient
$$
0\longrightarrow\mathcal A\longrightarrow\mathcal E\longrightarrow\mathcal F\longrightarrow0
$$
has $\rank\mathcal A=\rank\mathcal F=1$ and $\deg\mathcal F=\deg\mathcal E-\deg\mathcal A$, so $\deg\mathcal F>\frac12\deg\mathcal E$ is equivalent to $\deg\mathcal A<\frac12\deg\mathcal E$. A line subbundle that is not saturated lies in its saturation, whose quotient is torsion-free and hence invertible on a curve and whose degree is at least as large, so the inequalities for invertible quotients imply them for every line subbundle. The semistable statement is the same rearrangement with weak inequalities.

:::

:::

::: {.pf-step #s2}
A decomposable bundle is never stable, in any rank. This is part (a).

::: pf-proof
Write $\mathcal E\cong\mathcal F\oplus\mathcal G$ with $\mathcal F,\mathcal G$ locally free of ranks $r_{\mathcal F},r_{\mathcal G}\ge1$, and interchange the summands if necessary so that $\mu(\mathcal F)\le\mu(\mathcal G)$. The projection $\mathcal E\twoheadrightarrow\mathcal F$ with kernel $\mathcal G$ is a nonzero locally free quotient of $\mathcal E$ other than $\mathcal E$, so it is one of the quotients the definition of stability tests. Since $\deg\mathcal E=\deg\mathcal F+\deg\mathcal G$ and $\rank\mathcal E=r_{\mathcal F}+r_{\mathcal G}$,
$$
\mu(\mathcal E)=\frac{r_{\mathcal F}}{r_{\mathcal F}+r_{\mathcal G}}\mu(\mathcal F)+\frac{r_{\mathcal G}}{r_{\mathcal F}+r_{\mathcal G}}\mu(\mathcal G),
$$
a mean of $\mu(\mathcal F)$ and $\mu(\mathcal G)$ with positive weights, so $\mu(\mathcal F)\le\mu(\mathcal E)$; stability would require $\mu(\mathcal F)>\mu(\mathcal E)$, and $\mathcal E$ is therefore not stable. A decomposition into more than two summands is regrouped as a decomposition into two.

This is Solution 5.2.8(a) of Yang Pi-Yeh, *Hartshorne Solutions*, printed pp. 103--104, which displays the weighted mean at the head of the solution and reads the contradiction off the quotient $\mathcal E\twoheadrightarrow\mathcal F$; the same two quotient sequences, with kernels $\mathcal F$ and $\mathcal G$, are used in Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework, Exercise 8 of §2 (Tzu-Yang Chou), PDF p. 8, which concludes that "looking at the slopes we see that $\mathcal E$ can not be stable". In rank two the summands are line bundles, step [](#s1){.pf-ref} turns the quotient inequality of the exercise into the line-subbundle one, and Gunning records the conclusion for that case on printed p. 85, where Lemma 14 gives $\operatorname{div}\mathcal E\ge\frac12c(\xi)$ for a decomposable $\mathcal E$ and hence that "every decomposable bundle is unstable". The decomposable case of Lemma 14 itself, printed pp. 81--82, is stated for a direct sum $\varphi_1\oplus\cdots\oplus\varphi_m$ of line bundles, and its proof runs through (13), $\operatorname{div}(\varphi_1\oplus\cdots\oplus\varphi_m)=\max_jc(\varphi_j)$, so it does not reach a decomposable bundle of rank three or more; the mean of slopes does.

:::

:::

::: {.pf-step #s3}
If a rank-two bundle $\mathcal E$ is normalized, then every line subbundle $\mathcal A\subseteq\mathcal E$ satisfies
$$
\deg\mathcal A\le0 .
$$

::: pf-proof
The inclusion is a nonzero section of $\mathcal E\tensor\mathcal A^{-1}$; if $\deg\mathcal A>0$ then $\mathcal A^{-1}$ has negative degree, contrary to the normalization of printed p. 373. In Gunning's notation this says $\operatorname{div}\mathcal E\le0$, and $H^0(C,\mathcal E)\ne0$ gives the reverse inequality.

:::

:::

::: {.pf-step #s4}
If a rank-two bundle $\mathcal E$ is normalized, then it contains $\OO_C$ as a line subbundle.

::: pf-proof
Normalization gives $H^0(C,\mathcal E)\ne0$; a nonzero section gives an injective map $\OO_C\to\mathcal E$, and its image spans a line subbundle $\mathcal A\subseteq\mathcal E$, whose degree is at most $0$ by step [](#s3){.pf-ref} and at least $0$ because it carries the nonzero section, so $\mathcal A\cong\OO_C$. This is the last step of the proof of Proposition 2.8, where the quotient of $\mathcal E$ by that copy of $\OO_C$ is shown to be invertible.

:::

:::

::: {.pf-step #s5}
If $\mathcal E$ has rank two and is normalized, then
$$
\boxed{\mathcal E\text{ is stable}\iff\deg\mathcal E>0.}
$$

::: pf-proof
Gunning, §(c), printed p. 84: "$\Phi$ is stable precisely when $\operatorname{div}\Phi<\frac12c(\xi)$". A normalized bundle has $\operatorname{div}\mathcal E=0$ by step [](#s3){.pf-ref}, so that inequality is $0<\frac12\deg\mathcal E$. In the language of steps [](#s1){.pf-ref} and [](#s3){.pf-ref}: if $\deg\mathcal E>0$ then every line subbundle has $\deg\mathcal A\le0<\frac12\deg\mathcal E$ and stability follows, and if $\mathcal E$ is stable then the subbundle $\OO_C\subseteq\mathcal E$ of step [](#s4){.pf-ref} gives $0<\frac12\deg\mathcal E$.

:::

:::

::: {.pf-step #s6}
If $\mathcal E$ has rank two and is normalized, then
$$
\boxed{\mathcal E\text{ is semistable}\iff\deg\mathcal E\ge0.}
$$

::: pf-proof
Semistability is the exercise's definition, the weak inequalities of step [](#s1){.pf-ref}; Gunning defines stability and instability only and states no semistable criterion. With $\operatorname{div}\mathcal E=0$ by step [](#s3){.pf-ref} every line subbundle has $\deg\mathcal A\le0$, so $\deg\mathcal E\ge0$ gives the weak inequalities, and the subbundle $\OO_C$ of step [](#s4){.pf-ref} gives the converse. Both directions, with the parentheses of the sources carrying the weak inequality, are Solution 5.2.8(b) of Yang Pi-Yeh, *Hartshorne Solutions*, printed p. 104, and Exercise 8(b) of the National Taiwan University set (Tzu-Yang Chou), PDF p. 8: a line subbundle of degree at least half the degree of $\mathcal E$ gives a section of $\mathcal E\tensor\mathcal F^{-1}$, which the normalization of printed p. 373 forbids because $\mathcal F^{-1}$ has negative degree. Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (b).

:::

:::

::: {.pf-step #s7}
Let $\mathcal E$ be a rank-two bundle that is not semistable. Among all line subbundles of $\mathcal E$ there is one of maximal degree.

::: pf-proof
The maximum is what Gunning's $\operatorname{div}\Phi=\max_{\varphi\subset\Phi}c(\varphi)$ presupposes, and he proves the bound on printed p. 80, in the paragraph before his (9): for a line bundle $\varphi\subset\Psi$ he shows $c(\varphi)\le\max_jc(\Psi_j)$ over the diagonal line bundles of a fixed complete reduction of $\Psi$, "or in other words, the Chern classes $c(\varphi)$ of line bundles $\varphi$ which are subbundles of a fixed complex vector bundle $\Psi$, are bounded from above". The proof below is that bound in the form of a rank-two bundle on a curve, and is the card's own. Line subbundles exist, since a nonzero section of $\mathcal E(n)$ for $n\gg0$ saturates to an invertible subsheaf. Their degrees are bounded above: fix an ample $\OO_C(1)$ of degree $h>0$ and take $n\gg0$ so that $\mathcal E^\vee(n)$ is globally generated; dualizing the locally free quotient of a line subbundle $\mathcal A\subseteq\mathcal E$ gives a surjection $\mathcal E^\vee\twoheadrightarrow\mathcal A^\vee$, so $\mathcal A^\vee(n)$ is a quotient of a globally generated bundle and is globally generated, whence $-\deg\mathcal A+nh\ge0$ and $\deg\mathcal A\le nh$. The degrees are integers, so they have a maximum.

:::

:::

::: {.pf-step #s8}
A rank-two bundle $\mathcal E$ that is not semistable has a unique line subbundle $\mathcal A$ of maximal degree, and
$$
2\deg\mathcal A>\deg\mathcal E .
$$

::: pf-proof
This is Lemma 15 of Gunning, printed pp. 84--85. Non-semistability is $\operatorname{div}\mathcal E>\frac12c(\xi)$, that is $2\deg\mathcal A>\deg\mathcal E$ for a maximal subbundle, which is the case of the lemma's part (i). Its part (i) states and proves uniqueness: if $\varphi_1\subset\Phi$ realizes $\operatorname{div}\Phi$ and $\varphi\subset\Phi$ is another subbundle with $c(\varphi)=\operatorname{div}\Phi$, then $\varphi^{-1}\varphi_1$ has a nontrivial section while $\varphi^{-1}\varphi_2$ has none, $\varphi_2=\Phi/\varphi_1$, because $c(\varphi^{-1}\varphi_2)=-2c(\varphi_1)+c(\xi)<0$; so $\varphi=\varphi_1$. In rank-two terms, a second maximal subbundle $\mathcal B$ with $\deg\mathcal A=\deg\mathcal B=a$ and no common generic line gives a nonzero map $\mathcal A\tensor\mathcal B\to\det\mathcal E$ and hence $2a\le\deg\mathcal E$, contradicting $2a>\deg\mathcal E$.

:::

:::

::: {.pf-step #s9}
Let $\mathcal E$ be indecomposable and not semistable and let $\mathcal A$ be its unique maximal-degree line subbundle. Then
$$
\mathcal E_0=\mathcal E\tensor\mathcal A^{-1}
$$
fits into a nonsplit exact sequence
$$
0\longrightarrow\OO_C\longrightarrow\mathcal E_0\longrightarrow\mathcal L\longrightarrow0
$$
with $\deg\mathcal L=-e<0$.

::: pf-proof
This is the opening of the proof of Theorem 2.12: corresponding to a section of $\PP(\mathcal E)$ there is an exact sequence $0\to\OO_C\to\mathcal E\to\mathcal L\to0$ for some $\mathcal L$, and for an indecomposable $\mathcal E$ it "must be a nontrivial extension, so it corresponds to a nonzero element $\xi\in\Ext^1(\mathcal L,\OO_C)\cong H^1(C,\mathcal L^\vee)$". Tensoring the sequence of the subbundle $\mathcal A\subseteq\mathcal E$ by $\mathcal A^{-1}$ gives $\mathcal L\cong\det\mathcal E\tensor\mathcal A^{-2}$, so $\deg\mathcal L=\deg\mathcal E-2\deg\mathcal A<0$ by step [](#s8){.pf-ref}; write this degree as $-e$. A splitting would make $\mathcal E_0$, and hence $\mathcal E$, decomposable.

:::

:::

::: {.pf-step #s10}
The bundle $\mathcal E_0$ of step [](#s9){.pf-ref} is normalized, and its extension class is a nonzero $\xi\in H^1(C,\mathcal L^\vee)$ well defined up to nonzero scalar.

::: pf-proof
Normalization is the argument of Example 2.11.6: the inclusion $\OO_C\subseteq\mathcal E_0$ gives a nonzero section; for $\mathcal M$ of negative degree both end terms of the twisted sequence have negative degree because $\deg\mathcal L=-e<0$, so $H^0(C,\mathcal E_0\tensor\mathcal M)=0$. The identification of extension classes with $H^1(C,\mathcal L^\vee)$ is Theorem 13 of Gunning, printed pp. 72--74, whose equivalence of extensions is his (2), printed p. 71, whose statement also attaches the split extension to the zero class, so a nonsplit sequence has nonzero class. Rescaling the inclusion of $\OO_C$, or the quotient to $\mathcal L$, rescales the class without changing the middle bundle, so only its nonzero scalar class is intrinsic; Theorem 14 of Gunning, printed pp. 87--90, proves that proportional classes give isomorphic bundles and non-proportional ones do not.

:::

:::

::: {.pf-step #s11}
The integer $e$ of step [](#s9){.pf-ref} satisfies
$$
\boxed{0<e\le2g-2.}
$$

::: pf-proof
The degree $\deg\mathcal L=-e$ is negative by step [](#s9){.pf-ref}. For the upper bound, the proof of Theorem 2.12, argues from the nonvanishing of $H^1(C,\mathcal L^\vee)$: "in particular, $H^1(\mathcal L^\vee)\ne0$, so we must have $\deg\mathcal L^\vee\le2g-2$ (IV, 1.3.4). Since $e=-\deg\mathcal L$, we have $e\le2g-2$". Equivalently, Serre duality turns $0\ne\xi\in H^1(C,\mathcal L^\vee)$ into a nonzero section of $K_C\tensor\mathcal L$, whose degree $2g-2-e$ is therefore nonnegative.

:::

:::

::: {.pf-step #s12}
Conversely, given
$$
0<e\le2g-2,
\qquad
\deg\mathcal L=-e,
\qquad
0\ne\xi\in H^1(C,\mathcal L^\vee),
$$
let $0\to\OO_C\to\mathcal E_0\to\mathcal L\to0$ be the corresponding extension. Then $\mathcal E_0$ is normalized, indecomposable and not semistable.

::: pf-proof
Normalization is step [](#s10){.pf-ref}. The determinant is $\mathcal L$ of negative degree, so $\mathcal E_0$ is not semistable by step [](#s6){.pf-ref}. Indecomposability is the argument that follows, which uses nothing of the ground field; over $\CC$ it is also part of Gunning's Theorem 14, which parametrizes the indecomposable bundles with subbundle $\varphi$ and determinant $\xi$ by the points of $\PP H^1(C,\OO(\varphi^2\xi^{-1}))$, that space being $\PP H^1(C,\mathcal L^\vee)$ for $\varphi=\OO_C$. In rank two: if $\mathcal E_0\cong\mathcal B\oplus\mathcal C$ then one summand has a nonzero section, hence degree $0$ by step [](#s3){.pf-ref} and is $\OO_C$, the other is $\det\mathcal E_0\cong\mathcal L$ of negative degree and so has no sections, and the given inclusion is then the standard summand up to scalar, so the extension splits.

:::

:::

::: {.pf-step #s12b}
Let $\mathcal L$ be invertible of degree $-e<0$, and let $\mathcal E$ and $\mathcal E'$ be middle terms of extensions $0\to\OO_C\to\mathcal E\to\mathcal L\to0$ and $0\to\OO_C\to\mathcal E'\to\mathcal L\to0$ with classes $\xi$ and $\xi'$. Then $\mathcal E\cong\mathcal E'$ if and only if $\xi'$ is a nonzero scalar multiple of $\xi$, so the isomorphism class of the middle term depends exactly on the point $[\xi]\in\PP H^1(C,\mathcal L^\vee)$.

::: pf-proof
Two extensions with the same class are isomorphic as extensions, so their middle terms are isomorphic, and multiplying the inclusion $\OO_C\to\mathcal E$ by $\lambda\in k^*$ gives an extension of class $\lambda\xi$ whose middle term is $\mathcal E$; proportional classes therefore give isomorphic bundles. Conversely let $\varphi:\mathcal E\to\mathcal E'$ be an isomorphism. For a line subbundle $\mathcal M\subseteq\mathcal E$ the composite $\mathcal M\to\mathcal E\to\mathcal L$ is either zero or injective, so either $\deg\mathcal M\le\deg\mathcal L<0$, or $\mathcal M\subseteq\ker(\mathcal E\to\mathcal L)=\OO_C$ and the inclusion $\mathcal M\to\OO_C$, a nonzero map of invertible sheaves, gives $\deg\mathcal M\le0$ with equality exactly when $\mathcal M=\OO_C$. So $\OO_C$ is the unique line subbundle of $\mathcal E$ of degree $0$, and the same argument applies to $\mathcal E'$, whence $\varphi(\OO_C)=\OO_C$. The isomorphism $\varphi$ therefore carries the first extension to the second and induces an automorphism of $\OO_C$ and one of $\mathcal L$; an automorphism of an invertible sheaf on a complete curve is multiplication by a nonzero constant, since $H^0(C,\OO_C)=k$, so these are scalars, and the class of an extension changes by the scalar they contribute. Hence $\xi'$ is a nonzero multiple of $\xi$.

:::

:::

::: {.pf-step #s13}
The construction of steps [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref}, [](#s12){.pf-ref} and [](#s12b){.pf-ref} gives a bijection between tensor-equivalence classes of indecomposable non-semistable rank-two bundles and the data
$$
\boxed{\left(e,\mathcal L,[\xi]\right),\quad 0<e\le2g-2,\quad \deg\mathcal L=-e,\quad [\xi]\in\PP H^1(C,\mathcal L^\vee).}
$$

::: pf-proof
Starting from $\mathcal E$, step [](#s8){.pf-ref} gives its unique maximal-degree line subbundle $\mathcal A$, and tensoring by $\mathcal A^{-1}$ gives a normalized representative $\mathcal E_0$ of its tensor-equivalence class, whose maximal subbundle is $\OO_C$ and whose quotient is $\mathcal L=\det\mathcal E_0$. A normalized representative with maximal subbundle $\OO_C$ is unique in its tensor-equivalence class, because the maximal line subbundle of $\mathcal E_0\tensor\mathcal B$ is $\mathcal B$, the degrees of line subbundles shifting by $\deg\mathcal B$; so two bundles are tensor-equivalent exactly when their representatives with maximal subbundle $\OO_C$ are isomorphic. By steps [](#s9){.pf-ref}, [](#s10){.pf-ref} and [](#s11){.pf-ref} such a representative is the middle term of an extension of $\mathcal L$ by $\OO_C$ with $\deg\mathcal L=-e<0$, its data being $(e,\mathcal L,[\xi])$; step [](#s12){.pf-ref} shows that every displayed triple occurs, and step [](#s12b){.pf-ref} that two representatives are isomorphic exactly when their classes are proportional. That is the bijection. Tensoring by a line bundle preserves indecomposability and shifts every slope by the same degree, so it preserves non-semistability, while the determinant changes and the triple $(e,\mathcal L,[\xi])$ does not, so a bundle and its twist are not isomorphic; the classification is therefore of tensor-equivalence classes rather than of isomorphism classes.

:::

:::

::: pf-qed
Step [](#s2){.pf-ref} proves part (a) in every rank, steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (b), and steps [](#s7){.pf-ref} to [](#s13){.pf-ref} prove part (c) over an algebraically closed field of any characteristic, step [](#s12){.pf-ref} giving the parametrization of the classification and step [](#s12b){.pf-ref} its injectivity.

:::

:::

:::

::: {.remark title="Published solution"}
Gunning, *Lectures on vector bundles over Riemann surfaces*, §(c), printed pp. 82--83, states the stability condition in the form $c(\varphi)<\frac12c(\det\Phi)$ for every line subbundle, defines $\operatorname{div}\Phi=\max_{\varphi\subset\Phi}c(\varphi)$, and observes that $\Phi$ is stable exactly when $\operatorname{div}\Phi<\frac12c(\det\Phi)$; his Lemma 14, gives $\operatorname{div}\Phi\ge\frac1{\rank}c(\det\Phi)$ for a decomposable $\Phi=\varphi_1\oplus\cdots\oplus\varphi_m$, a direct sum of line bundles, which with his rank-two stability definition is part (a) in rank two, and on printed p. 85 he records that "every decomposable bundle is unstable"; in general $\operatorname{div}\Phi\ge\frac1{\rank}c(\det\Phi)-g$; his Lemma 15, is the uniqueness of the maximal-degree line subbundle; and his Theorem 14, parametrizes the indecomposable unstable bundles with a given subbundle $\varphi$ and determinant $\xi$ by the points of $\PP H^1(C,\OO(\varphi^2\xi^{-1}))$, which is the classification of part (c) with $\varphi=\OO_C$ and $\xi=\mathcal L$. Steps [](#s3){.pf-ref} to [](#s11){.pf-ref} follow that route, steps [](#s12){.pf-ref} and [](#s12b){.pf-ref} are the rank-two form of the same classification, and step [](#s2){.pf-ref} is the slope argument for part (a) in every rank, with the determinant bound $0<e\le2g-2$ of step [](#s11){.pf-ref} from the proof of Theorem 2.12, the normalization of step [](#s10){.pf-ref} from Example 2.11.6, and the existence of the maximum of step [](#s7){.pf-ref}, which Gunning establishes on printed p. 80 by bounding the Chern classes of subbundles from above, and which the card also proves by global generation. Gunning works over a compact Riemann surface, so his Theorem 14 is part (c) over $\CC$; the card proves it over an algebraically closed field of any characteristic, with step [](#s12){.pf-ref} constructing the middle term from the data and step [](#s12b){.pf-ref} deciding which classes give isomorphic bundles, and without the Riemann-surface theory.
Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.8, printed pp. 103--104, proves (a) in every rank from the weighted mean of the two slopes, which is step [](#s2){.pf-ref}, and (b) by the rearrangements of steps [](#s1){.pf-ref} to [](#s6){.pf-ref}, and concludes (c) with "all indecomposable locally free sheaves $\mathcal E$ of rank 2 that are not semistable are classified, up to isomorphism, by these three conditions" — the printed clause; its argument assumes the bundle has $\OO_C$ as a subbundle with $\deg\mathcal L<0$, that is, takes the bundle to be the normalized model, so the twist that changes the bundle and leaves the data fixed is not accounted for there.

Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework solutions, Exercise 8 of §2 (solution by Tzu-Yang Chou), proves (a) by exhibiting both summand quotients and (b) in both directions, "if $\mathcal E$ is unstable, say $\exists F\subseteq\mathcal E$ invertible with $\deg F\ge\frac12\deg\mathcal E>0$, then $0\to\OO\to\mathcal E\tensor F^{-1}$ but $H^0(\mathcal E\tensor F^{-1})=0$ by the normalized assumption". Its (c) is the single sentence "This is just the proof of Theorem 2.12, combined with (b)", so it gives no argument for (c) and does not treat the twist either.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.8. Part (a) he proves from the claim that a stable bundle has no nonzero non-invertible endomorphism of itself, which he derives from the slope inequalities and applies to $\id_{\mathcal G}\oplus0$ on a decomposition $\mathcal E\cong\mathcal G\oplus\mathcal F$; the claim and the argument use nothing about the ranks, but he states (a) with $\mathcal E$ a direct sum of two invertible sheaves, so what he records is the rank-two case. Part (b) he proves in both directions: a (semi)stable bundle of (negative) non-positive degree has no sections, so normalized forces degree $\ge0$, and conversely a line subbundle of degree $>\frac12\deg\mathcal E$ would give a section of $\mathcal E\tensor\mathcal F^\vee$ of negative degree. Part (c) he derives from a Harder--Narasimhan filtration, citing Potier for its uniqueness, concludes "Since the filtration was unique we have this up to isomorphism", and does not address the tensor twist: his $\mathcal L$ is the quotient $\mathcal E/F_1$ rather than the normalized determinant, and the subbundle $F_1$ is not among the data, so his last inference does not follow.

:::

::: {.remark}
The printed (c), on printed p. 384, reads "Show that the indecomposable locally free sheaves $\mathcal{E}$ of rank 2 that are not semistable are classified, **up to isomorphism**, by giving (1) an integer $0<e\leq 2g-2$, (2) an element $\mathcal{L}\in\Pic C$ of degree $-e$, and (3) a nonzero $\xi\in H^1\left(\dualof{\mathcal{L}}\right)$, determined up to a nonzero scalar multiple", and the phrase "up to isomorphism" is what the statement above replaces.  The three data carry $\det\mathcal{E}=\mathcal{L}$, of degree $-e$ lying in $[-2g+2,-1]$, so they classify the normalized representative of a twist class: for an invertible $\mathcal{M}$ of nonzero degree, $\mathcal{E}\otimes\mathcal{M}$ is indecomposable and, in rank two, semistable exactly when $\mathcal{E}$ is, while $\det(\mathcal{E}\otimes\mathcal{M})=\det\mathcal{E}\otimes\mathcal{M}^2$ has degree $-e+2\deg\mathcal{M}$, so it is not isomorphic to $\mathcal{E}$ and carries different data.  The classification is therefore up to tensoring with an invertible sheaf, and not up to isomorphism with $e$ ranging freely.  Yang Pi-Yeh, printed pp. 103--104, states the printed clause and argues it for the normalized model, as the published-solution remark above records.
:::
