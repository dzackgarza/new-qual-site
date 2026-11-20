---
schema: qual/card@1
id: P-AGH467MULTISECANTS
kind: problem
title: Curves without multisecants in characteristic zero
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Genus
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.6.7, the projection exercises IV.3.10--3.11, the
    low-degree curve classification IV.3.4 and IV.3.6, Castelnuovo's bound,
    and the retained Egbert working notes. The projection argument below
    requires a separate tangent-contact hypothesis.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: >-
    Hartshorne IV.3 defines a multisecant by three distinct points. The
    earlier proof counted tangential length-three intersections and therefore
    did not establish the stated converse. The retained argument proves a
    conditional reduction; the tangent-contact implication remains open.
- event: source-corrected
  by: chatgpt
  date: 2026-10-31
  note: >-
    The unqualified converse in IV.6.7 is false in positive characteristic.
    The Frobenius graph of degree p+1 on a smooth quadric is a smooth
    nonplanar curve with no lines through three distinct points for p at
    least 3. The card states the characteristic-zero theorem and proves
    the counterexample.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    The proof below already existed in full but sat inside the `remark` block, so the card carried no
    solution section and `just unsolved` counted it as unsolved. This event moves it into a solution
    block. What was checked here: the block structure (sixteen steps, `pf-qed` closing, all renderer
    checks pass); the two steps that the earlier audit left open — `tangent-char-zero`, which now
    cites Kaji's theorem on tangentially degenerate curves for the finiteness of tangent lines meeting
    the curve again, together with a characteristic-zero argument that contact order at least three at
    the generic point would make the two remaining coordinates affine in a local parameter and put
    $X$ on a line; and `positive-char-counterexample`, which supplies the failure in
    characteristic $p\ge3$. **Not checked here:** steps `s1`--`s13` were not re-derived line by line
    in this pass, and the mathematical review on record remains the earlier sequence of events.
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    The Kaji citation in `tangent-char-zero` is now checked at the level of the paper's own abstract,
    which was retrieved from a bibliographic index (the full text is behind a publisher paywall and
    was not obtained). The abstract defines the notion and states the result: *"A projective curve
    $X$ in $\PP^N$ is said to be tangentially degenerate if a tangent line to $X$ at a general point
    $P$ meets $X$ again at a point other than $P$. In this article, we prove that if $X$ is
    tangentially degenerate in characteristic zero, then $X$ is contained in a 2-plane under a certain
    condition on singularities of $X$."* (H. Kaji, *On the tangentially degenerate curves*, J. London
    Math. Soc. (2) **33** (1986), 430--440, doi:10.1112/jlms/s2-33.3.430.) For a **smooth** curve the
    condition on singularities is vacuous, so the contrapositive is exactly the step's claim: a smooth
    nonplanar curve in characteristic zero is not tangentially degenerate, that is, its tangent line at
    a general point does not meet the curve again. What remains unchecked: the precise form of the
    singularity condition, which is irrelevant here, and the body of the paper.
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    SUPERSEDES the event of even date above that claimed the Kaji citation was checked "at the level of
    the paper's own abstract". That abstract is not this paper's. The text quoted there -- tangentially
    degenerate defined, characteristic zero forcing the curve into a 2-plane under a condition on
    singularities, and a counter-example of Esteves and Homma -- is the abstract of the SEQUEL: Kaji, On
    the tangentially degenerate curves, II, Bull. Braz. Math. Soc. (N.S.) 45 (2014) 745-752,
    doi:10.1007/s00574-014-0072-8. Three checks: the Waseda University Pure record for the 1986 paper
    carries no abstract field, while its record for the 2014 paper carries exactly that text; the Crossref
    deposit of the 1986 DOI has no abstract, and the 2014 DOI's reference list cites the 1986 paper as its
    own reference [8]; and the text names Esteves-Homma, whose method dates from 1994 and is the 2014
    article's reference [3]. The earlier inference "for a smooth curve the singularity condition is
    vacuous" was thus reasoning about the wrong paper and is withdrawn, not relied on. What is now known
    about the 1986 theorem comes from a secondary source: Fukasawa, A generalization of Esteves-Homma's
    example of tangentially degenerate curves, arXiv:2108.00650 (Atti Accad. Naz. Lincei 33 (2022)
    959-966), whose introduction states that "for the case where p = 0 and the morphism X -> P^N induced
    by the normalization phi: X -> C is unramified, the nonexistence of such curves was proved by Kaji
    [6] in 1986", and which calls the 2014 paper a generalization of it. That hypothesis is satisfied by
    the smooth curve of step tangent-char-zero, whose normalization is an isomorphism. It is however a
    third party's restatement, NOT the body of the paper, and it is not treated as verification here.
    NOT VERIFIED: the body of JLMS (2) 33 (1986) 430-440. The access operations tried, and how each
    failed: doi.org resolves to doi.wiley.com, which answers with a Cloudflare human check; the only
    machine-readable link in the Crossref record, api.wiley.com/onlinelibrary/tdm/v1/articles/...,
    requires a Wiley text-and-data-mining token; the same archive at academic.oup.com/jlms answers with a
    Cloudflare human check; zbmath.org answers with a Cloudflare human check and the zbMATH API record
    3900930 returns with its review text withheld ("contents unavailable due to conflicting licenses");
    the 2014 sequel at link.springer.com redirects to idp.springer.com/authorize, i.e. institutional
    login; there is no arXiv copy of either paper. What would close it: institutional or library access
    to JLMS (2) 33 (1986) 430-440. Until then step tangent-char-zero remains a citation step and the
    obligation stays open. Also unchanged: steps s1--s13 were not re-derived.
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Correction to step tangent-char-zero, whose incidence formulation was wrong as written earlier the
    same day. The step had said the bad locus is the image of the CLOSED subset of X x X on which
    X(P), X'(P), X(Q) become dependent. That subset contains the diagonal: for Q = P the three columns
    are X(P), X'(P), X(P), whose rank is at most 2, so every 3x3 minor vanishes. Hence its projection to
    the first factor is all of X, it does contain the generic point, and the appeal to constructibility
    proved nothing at all. The second-point condition Q != P is not a convenience in the statement but
    the substance of it. The step now uses the LOCALLY CLOSED set Z* = {Q != P and X(Q) in
    <X(P),X'(P)>} = Z minus the diagonal, notes explicitly that Z itself is useless for this reason,
    and applies Chevalley's theorem to the constructible set Z* -- not the image of a closed set -- to
    conclude that B = pr_1(Z*) is constructible. Kaji says B does not contain the generic point, and a
    constructible subset of a curve omitting the generic point is finite. Checked separately and
    unchanged: the dependence condition is the vanishing of the 3x3 minors of the 4x3 matrix, and
    Q in T_P X for Q != P is equivalent to X(Q) lying in the projective span of X(P) and X'(P), which
    is that line. The second paragraph of the step, on contact order at least 3, needed no change: it
    is a condition on P alone, via the dependence of X(P), X'(P), X''(P), so it has no diagonal issue.
    UNCHANGED AND STILL OPEN: the body of Kaji, J. London Math. Soc. (2) 33 (1986) 430-440, remains
    unread; the hypothesis available to us is a third party's restatement (Fukasawa, arXiv:2108.00650,
    Sec. 1: p = 0 with the normalization unramified, which a smooth curve satisfies), not the paper.
    Step tangent-char-zero therefore remains a CITATION step, not a verified one, and the portal or
    library access recorded in the preceding event is still required to close it.
- event: source-checked
  by: claude
  date: 2026-11-02
  note: >-
    CLOSES the open citation requirement recorded in the events above, on the owner's instruction that
    the original publication need not be obtained merely because it is the original. The step now cites
    the restatement actually consulted: Fukasawa, A generalization of Esteves-Homma's example of
    tangentially degenerate curves, arXiv:2108.00650v3, section 1, retrieved and read in full. Its two
    sentences are the definition and the theorem used: an irreducible projective curve C in P^N with
    N >= 3, not contained in any plane, over an algebraically closed field of characteristic p >= 0, is
    tangentially degenerate if (T_P C minus P) meets C for a general P; and "for the case where p = 0
    and the morphism X -> P^N induced by the normalization phi: X -> C is unramified, the nonexistence
    of such curves was proved by Kaji [6] in 1986". Each hypothesis was checked against this step:
    N = 3, the field is algebraically closed of characteristic 0, X is not contained in a plane, and X
    is smooth so its normalization is an isomorphism, hence unramified. The conclusion is therefore the
    non-tangential-degeneracy this step needs, and the passage from "general point" to "all but
    finitely many" is the constructible-set argument that follows it. Kaji's own paper is retained as
    the primary reference and is not claimed to have been read: the attempts are the ones recorded
    above (Wiley and Oxford Academic answered with human checks, the Wiley TDM endpoint needs a token,
    zbMATH withholds the review text under licence, the 2014 sequel is behind institutional login, and
    no arXiv copy exists). The earlier misattribution of the 2014 sequel's abstract to the 1986 paper
    stands corrected as recorded. Not checked: the body of Kaji 1986, and steps s1--s13 of this card.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The printed definition of multisecant, Hartshorne IV.3 printed p. 310, is a line meeting X in
    three or more distinct points, and it does not exclude the line X itself when X is a line. A
    line meets itself in every one of its points, so under the letter of that definition the printed
    first sentence of IV.6.7, that the line has no multisecants, is false with X itself as the
    counterexample, and holds only for secant lines proper. The card's statement now defines a
    multisecant as a line not contained in X meeting X in at least three distinct points, and its
    remark records the discrepancy. The clause changes nothing else: no line is contained in a
    planar curve of degree at least 2 or in a nonplanar curve, and the printed second sentence is
    unaffected. The same remark now records that smoothness and integrality are not hypotheses this
    card adds, since the Terminology of the book reserves the word curve, in Chapter IV, for a
    nonsingular projective curve; the one hypothesis added to the printed second sentence is
    characteristic zero, whose necessity is the Frobenius-graph counterexample recorded in the
    event of 2026-10-31.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    SUPERSEDES, as the current state of this card, the clauses "Not checked ... steps s1--s13" in
    the events of 2026-11-01 and 2026-11-02 above; those notes are records of their own passes and
    are left as written (QUAL-11). Every step s1--s13 was read in this pass against the printed book
    and is correct as the card now states it; where the prose did not support its claim, the step is
    repaired, and the repairs are listed below.

    Read for this pass in `tmp/sources/hartshorne-1977-algebraic-geometry.md`, where printed page N
    is PDF page N+15 and the page starts are marked in the file: IV.6.7 printed p. 355 with its
    printed hint; the definition of multisecant and Proposition 3.7, printed pp. 310--311; IV.3.1
    printed pp. 307--308; IV.3.4(a) and (b) printed p. 315; IV.3.6(b) printed pp. 316--317; IV.6.4
    printed p. 351; II.7.3, the closed-immersion criterion, printed p. 152; and II.8.20.3 for
    the genus of a nonsingular plane curve, printed p. 183. The two printed exercises the solution cites were also
    checked against a published solution set: Egbert's solutions of IV.3.4 and IV.3.6, retained at
    `tmp/sources/hartshorne-solutions-egbert.md`, which prove the quadratic generation of the
    rational normal curve's homogeneous ideal and the complete-intersection statement for the
    elliptic quartic. No retained solution set contains a solution of IV.6.7 itself: a search of the
    retained Hartshorne sets for the word multisecant returns only Borcherds's solution of IV.3.9,
    and Lomont's Chapter IV stops at 6.4. The thirteen steps are therefore checked against the book
    and the results it proves, and not transcribed from a published solution of this exercise.

    Per step. s1 correct as now written; the line half needed the convention of the source-corrected
    event above. s2 correct: a section of O_l(2) whose zero scheme on the line has length at least 3
    is zero, so every quadric through the twisted cubic contains the line, and quadratic generation
    of the ideal makes their scheme-theoretic intersection the curve. s3 correct, cited as
    IV.3.6(b) with the printed word irreducible restored: the two quadrics restricted to the line
    vanish on a subscheme of length at least 3, hence on the line. s4 correct, with the added
    justification that the lines meeting a smooth plane curve non-transversely are exactly its
    tangents and form the dual curve, a proper closed subset of the dual plane, so the transverse
    lines are dense and infinite. s5 repaired: the statement now names the three properties of P
    that s7 and s8 use -- P on no multisecant, P on no tangent line T_Q X with Q different from P,
    and T_P X meeting X only at P and there with length exactly 2 -- and the proof derives each of
    them from the choice of P outside the finitely many intersections with X of the lines of the two
    finite families. Previously only the first was stated, and the other two were used silently.
    s6 repaired: the restriction of the plane sections through P is injective because X is not
    contained in a plane, and the subsystem is now said to lie in H^0(X, H-P) instead of being
    "divided" by the fixed zero. s7 correct, with the justification added that pi_P(P) is the
    tangent direction because all sections of the system vanish at P, so their value there is their
    derivative; the second case now cites property (iii). s8 correct: the first case cites (ii) and
    the local computation at P cites (iii), and the computation itself checks out -- with
    x = t + O(t^2), y = a_2 t^2 + O(t^3), z = b_2 t^2 + O(t^3), the differential at P vanishes
    exactly when a_2 = b_2 = 0, which is contact order at least 3. s9 repaired: the step now
    identifies the two conditions of the closed-immersion criterion with the injectivity of pi_P on
    closed points and of its differential at closed points, which is the form s7 and s8 establish
    them in; the degree computation pi_P^* O(1) = H-P of degree d-1 is correct. s10 correct, with
    the plane-curve genus formula cited as II.8.20.3. s11 correct: Castelnuovo's printed hypotheses
    are degree d, genus g and not contained in a plane, and the two comparisons multiply out to
    (d-2)(d-4) <= 0 and (d-3)^2 <= 0, which with d >= 3 give d = 4 in the even case and d = 3 in
    the odd one; cited as IV.6.4. s12 correct, on IV.3.4(b) for degree 3 and IV.3.6(b) for degree 4.
    s13 correct: it assembles s4, s12 and the tangent finiteness supplied by tangent-char-zero.

    The step tangent-char-zero was also read: its hypotheses are the ones the cited sentences
    require (N = 3, algebraically closed of characteristic 0, X nonplanar, X smooth so that its
    normalization is an isomorphism and hence unramified), and the passage from "general point" to
    "all but finitely many" is sound, since Z* is locally closed, its image under the first
    projection is constructible by Chevalley, and a constructible subset of a curve that omits the
    generic point is finite.

    Not checked in this pass: the body of Kaji, J. London Math. Soc. (2) 33 (1986) 430--440, which
    remains a citation of the restatement in Fukasawa, arXiv:2108.00650v3, section 1, as recorded in
    the event of 2026-11-02; and the positive-characteristic counterexample of the last step, which
    was read but not re-derived. Its two points that would need a check of their own are the closed
    immersion (separation of points and of tangent vectors on both charts of P^1) and the
    injectivity of [s:t] to [s^p:t^p].
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A further pass over the same text, after the first event of this date recorded the read of
    s1--s13. It corrects one page reference of that event, and it repairs the one mathematical
    defect that the thirteen steps do not contain but that their end rests on.

    Page correction. IV.3.6 is printed p. 315, not pp. 316--317: in
    `tmp/sources/hartshorne-1977-algebraic-geometry.md` the whole exercise block 3.1--3.6 lies
    between the page starts PDF 330 and PDF 331. The other references of the first event stand:
    the definition of multisecant and Proposition 3.7 on printed pp. 310--311, IV.3.1 on
    pp. 307--308, IV.3.4 on p. 315, IV.6.4 on p. 351, IV.6.7 on p. 355, II.7.3 on p. 152, and
    II.8.20.3 on p. 183.

    The repaired defect. The second paragraph of tangent-char-zero, on the finiteness of the
    locus where the tangent line has contact order at least 3, argued at the generic point by
    "writing the other affine coordinates as $y(x)$ and $z(x)$". That notation presumes
    $k(X)=k(x)$, which fails for every curve of positive genus -- the elliptic quartic among
    them -- so as written the argument reaches its conclusion only for rational $X$, and s13
    inherits the gap, because it uses this step for the second finiteness hypothesis of s5. The
    claim is true, and the paragraph is now proved: contact order at least 3 at $P$ is the linear
    dependence of $X(P)$, $X'(P)$, $X''(P)$, a closed condition; at the generic point,
    characteristic zero makes $k(X)/k(x)$ separable, so the derivation $d/dx$ with $d(x)/dx=1$
    exists and the condition is $d^2y/dx^2=d^2z/dx^2=0$; the kernel of $d/dx$ is $k$, being a
    subfield containing $k$ and not the nonconstant $x$ while $k(X)$ has transcendence degree
    1; hence $y=cx+d$ and $z=ex+f$, and $X$ lies on a line.

    Also repaired in this pass, each a clause rather than a claim. s2 and s3 now open with the
    multisecant hypothesis that $\ell\not\subseteq X$, which is what their closing contradiction
    uses, and they justify the vanishing of a section of $\OO_\ell(2)$ over a subscheme of length
    3, which they had asserted. s5 says why each of the finitely many lines meets $X$ in finitely
    many points, namely that otherwise $X$ would be a line. s6 no longer calls the planes through
    $P$ a three-dimensional linear system -- a linear system of that dimension would be a
    $\PP^3$ of divisors -- but a $\PP^2$ of planes, that is, a three-dimensional space of
    sections. s10 cites Remark 6.4.1 beside II.8.20.3, that remark being the place in Chapter IV
    where the genus of a nonsingular plane curve of degree $d$ is stated. s12 and s13 carry the
    words smooth integral that the problem statement already had, so that neither is false of a
    singular curve. The closing remark no longer says that the statement "carries the hypotheses
    the argument uses, characteristic zero and the curve smooth and integral"; it records instead
    that characteristic zero is the one hypothesis the card adds, that smoothness and integrality
    are the book's Chapter IV convention for the word curve, and that dropping them makes the
    second sentence false, with the singular rational quartic $X=Q_1\cap Q_2$, where
    $Q_1=X_0X_3-X_1^2$ and $Q_2=X_1X_3-X_2^2$, as the counterexample: it is integral, nonplanar
    and of degree 4, singular at $[1:0:0:0]$ where the gradient of $Q_2$ vanishes, has no
    multisecants because a trisecant would lie on both quadrics and hence in $X$, and is neither
    the twisted cubic nor the elliptic quartic.

    Not checked in this pass, unchanged: the body of Kaji 1986, the citation resting on the
    restatement in Fukasawa, arXiv:2108.00650v3, section 1; and the positive-characteristic
    counterexample of the last step, which was re-read but whose two delicate points, the closed
    immersion and the injectivity of $[s:t]\mapsto[s^p:t^p]$, were not re-derived here. Two
    sentences are tightened in the same pass, both mine: the remark now says that the clause
    $\ell\not\subseteq X$ is the reading that holds for all four curves, instead of calling it the
    only possible reading, and s9 says that the criterion's two conditions are equivalent to the two
    injectivities rather than identical with them.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    CLOSES the one item the first event of this date left open short of the body of Kaji: the
    positive-characteristic counterexample, there "read but not re-derived", is re-derived here,
    and the sentences whose reasons it had left implicit now carry them.

    The step, re-derived. The map $[s:t]\mapsto[s^{p+1}:s^pt:st^p:t^{p+1}]$ is given by four
    linearly independent forms of degree $p+1$, so its image has degree $p+1$. On $s\ne0$ it reads
    $u\mapsto(1,u,u^p,u^{p+1})$ and on $t\ne0$ $v\mapsto(v^{p+1},v^p,v,1)$; the derivatives
    $(0,1,0,u^p)$ and $(v^p,0,1,0)$ never vanish, so the differential is injective everywhere, and
    with injectivity on points and $\PP^1$ proper the map is a closed immersion. Hence $C$ is smooth
    of degree $p+1$, and the independence of $1,u,u^p,u^{p+1}$ makes it nonplanar. $C$ lies on the
    smooth quadric $X_0X_3=X_1X_2$. A trisecant would meet that quadric in three points, hence lie
    on it, since a line not contained in a quadric surface meets it in at most two points; every
    point of the quadric is $(s^p,t^p)^T(s,t)$ because Frobenius is bijective on the algebraically
    closed field; a ruling line fixes one of the two factors; and both $[s:t]$ and $[s^p:t^p]$ are
    determined by the point of $C$, the second because $x^p=y^p$ forces $x=y$. So each ruling meets
    $C$ once and no line meets it three times. Since $p+1\ge4$ and $C$ is rational, it is none of
    the four curves of the exercise.

    Added in this pass, with no claim changed: the two derivatives, the Bezout bound for a line and
    a quadric surface, the bijectivity of Frobenius used to write every point of $Q$ as a rank-one
    matrix, and the reason the $p$-th power map on $\PP^1$ is injective.

    Not checked: the body of Kaji 1986, unchanged, the citation resting on Fukasawa,
    arXiv:2108.00650v3, section 1.

- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Citation form, on the rule that a card cites a numbered statement rather than a page (#184).
    Every reference in this card's statement, remarks and steps is now carried by its numbered
    statement: Exercise IV.6.7; the definition of multisecant in IV.3 with Proposition IV.3.7;
    Proposition IV.3.1; Exercise IV.3.4(a) and (b); Exercise IV.3.6(b); Theorem IV.6.4;
    Proposition II.7.3; Example II.8.20.3; and Fukasawa, arXiv:2108.00650v3, section 1, for the
    Kaji restatement. No page, PDF page or page offset appears in the card's text. The page
    locators that the events of 2026-11-01, 2026-11-02 and 2026-11-19 carry are records of those
    passes and are left as written (QUAL-11); this event is the card's statement of the form its
    citations now take. No mathematical claim changed in this pass.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Status of the card, stated once so that no reader has to date-order the events. Every step
    s1--s13 is read and correct as the card now writes it; the assertions of the earlier events that
    they "were not re-derived" are records of those passes and are superseded by the events of
    2026-11-19 above, which name them. Two further sentences of earlier events are superseded in
    substance and are named here, because the 2026-11-19 event quotes only the "Not checked ...
    s1--s13" clauses: the 2026-10-31 sentence that "the tangent-contact implication remains open" is
    discharged by the step tangent-char-zero, whose characteristic-zero input is cited to Fukasawa,
    arXiv:2108.00650v3, section 1, and whose contact-order paragraph is now proved on the card; and
    the 2026-11-01 sentence recording that the card had no solution section is discharged by the
    solution block the card now carries.

    What is not checked, and is not a step of this card: the body of Kaji, J. London Math. Soc. (2)
    33 (1986) 430--440. The step that uses his theorem cites the restatement it actually read, and
    the paper is kept as the primary reference without any claim to have been read.

    Citation form: every reference in the card's statement, remarks and steps is to a numbered
    statement -- Exercise IV.6.7; the definition of multisecant in IV.3 with Proposition IV.3.7;
    Proposition IV.3.1; Exercise IV.3.4(a), (b); Exercise IV.3.6(b); Theorem IV.6.4;
    Proposition II.7.3; Example II.8.20.3; Remark IV.6.4.1(d) with Exercise V.2.9; and Fukasawa,
    arXiv:2108.00650v3, section 1. No page locator appears in the card's own text.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Two corrections found by an independent audit of this card's citations, both mine.

    (i) The step tangent-char-zero cited Fukasawa's definition as "§1, p. 1". That is a page
    locator in the body of the card, which the citation rule forbids: the reference is now
    "§1" alone, which is where both sentences the step uses stand. A sweep of every card of this
    section for the same form, including "pp." and bare "p. <number>", finds no other occurrence in
    a card's body.

    (ii) An event of 2026-11-01 records that the solution block was moved out of a remark block and
    says that block has "sixteen steps". The card has fifteen: s1--s13, tangent-char-zero and
    positive-char-counterexample. The count in that dated record is wrong and is left as written
    (QUAL-11); this event is the correction of record.

    Nothing mathematical changes: the steps, their claims and their proofs are the ones read in the
    events above.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Five results the steps use were named without a number, and two earlier events of today
    overstated the citation state of the card. Both are corrected here.

    The five, now cited as numbered statements: Bezout's theorem, Corollary I.7.8, in s1; the dual
    curve, Exercise I.7.3, in s4; Chevalley's theorem, Exercise II.3.19, in tangent-char-zero; the
    closed-immersion criterion, Proposition II.7.3 with Remark II.7.8.2, in s9, where the step had
    only an internal card link; and the bound that a line not contained in a quadric surface meets
    it in at most two points, Theorem I.7.7, in the positive-characteristic counterexample. Also
    changed for accuracy: the remark now attributes the book's use of the word curve to the opening
    paragraph of IV.1, which states it, instead of to a section heading.

    The overstatement, recorded because it was mine. The two events of today each listed the
    references of the card and said that every one was a numbered statement. The lists named
    Proposition IV.3.1 and Exercise V.2.9, which this card does not cite, and they omitted the five
    results above, so the claim was false when written; and the first of them also asserted that no
    page locator appeared in the card's text while the Kaji restatement was still cited as "section
    1, p. 1", which the event of the same day removes. The card's references are now: Exercise
    IV.6.7; the definition of multisecant in IV.3 with Proposition IV.3.7; Exercise IV.3.4(a), (b);
    Exercise IV.3.6(b); Theorem IV.6.4; Proposition II.7.3 with Remark II.7.8.2;
    Remark IV.6.4.1(a) with Exercise II.8.4(f) for the plane-curve genus; Corollary I.7.8;
    Exercise I.7.3; Exercise II.3.19; Theorem I.7.7; and Fukasawa, arXiv:2108.00650v3, section 1.

    Not checked: the body of Kaji 1986, as before.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Three defects found by an audit of the steps' mathematics, all outside s1--s13 and all mine; no
    step of s1--s13 changes.

    (i) The counterexample said "every point of Q is" the matrix (s^p,t^p)^T(s,t), with the p-th
    power map's bijectivity offered as the reason. That is false: the image of [s:t] under that
    formula is the curve C, a one-dimensional subset of the surface Q, and for p = 3 the point
    [2:1:0:0] of Q lies on it for no [s:t], since X_2 = t^p s and X_3 = t^{p+1} vanish only when
    t = 0, which forces X_1 = 0. The argument is now made correctly: every point of Q is some
    rank-one matrix, the two rulings are the loci where one of its two factors is fixed, C is the
    set of these matrices with (u_0,u_1) = (s^p,t^p) and (v_0,v_1) = (s,t), and each ruling meets C
    once. Frobenius's bijectivity is used where it belongs: to write the fixed factor of a ruling
    as (a^p:b^p), and to take the p-th root of the scalar relating two proportional pairs. Both
    rulings are now treated separately, and the step no longer asserts that C is all of Q.

    (ii) The closing remark's singular rational quartic read [s^4 : s^2t^2 : s^3t : t^4], which does
    not lie on Q_2 = X_1X_3 - X_2^2: substituting gives s^2t^2(t^4 - s^4), not zero. The curve
    intended is [s^4 : s^2t^2 : s t^3 : t^4], whose substitution into both quadrics is identically
    zero, which is singular at [1:0:0:0] (in the chart s = 1 it is u -> (u^2,u^3,u^4)) and which
    is the counterexample the remark needs. Corrected.

    (iii) The kernel-of-d/dx sentence in tangent-char-zero stated its ingredients but not the step
    that uses them. It now says that the kernel has transcendence degree 0 over k, hence is
    algebraic over k, hence is k itself because k is algebraically closed in k(X).

    What the audit confirmed, unchanged: s1--s13 are each a complete argument for its claim as the
    card now writes them. Its decisive checks are recorded with it: that Exercise IV.3.4(a) is
    literally "its homogeneous ideal can be generated by forms of degree 2" for d = 3, that
    Exercise IV.3.6(b) is literally "a complete intersection of two irreducible quadric surfaces" in
    the case g = 1, that Theorem IV.6.4 itself carries "Then d >= 3" so s11 assumes nothing, and
    that s9 says the criterion's conditions are "equivalently" the two injectivities.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The three items of issue #162, from the reader's report on this card at
    141b8c9c4d.

    (1) The kernel of d/dx. The step tangent-char-zero inferred that the kernel is
    k because it is a subfield of k(X) containing k and not containing the
    nonconstant x, hence of transcendence degree 0. That inference is false, and
    the reader's counterexample is the one to keep: k(t^2) is a subfield of k(t)
    of transcendence degree 1 that omits t. The step now proves the equality. If
    f in k(X) has df/dx = 0 and f is not in k, then f is transcendental over k
    because k is algebraically closed, so k(f) has transcendence degree 1 and
    k(X) is a finite separable extension of k(f), finite because a finitely
    generated extension of transcendence degree 0 is finite and separable because
    the characteristic is 0; d/dx vanishes on k(f); and a derivation of a finite
    separable extension that vanishes on the base field is zero, by the
    primitive-element argument now written on the card. That contradicts
    d(x)/dx = 1, so the kernel is k, and the rest of the step -- dy/dx and dz/dx
    in k, hence y = cx+d and z = ex+f, hence X on a line -- is unchanged. The
    existence of d/dx is now attributed to the separability of k(X)/k(x) alone,
    which is what gives it; the sentence had offered that separability as the
    reason x is a local parameter at the generic point, which it is not. With
    this, step s13 rests on a proved step: the second finiteness hypothesis of s5
    is what tangent-char-zero supplies, and the first is the Kaji citation,
    unchanged.

    (2) Page locators. The card's statement, remark and steps carry none: every
    reference is to a numbered statement, and the transcription added under (3) is
    cited as Andrew Egbert, Solutions to Hartshorne's Algebraic Geometry, Exercise
    IV.6.7, with no page. The reader's line numbers 159, 182--187 and 247--252
    are not in the card's text: they lie inside the dated events of 2026-11-19,
    which record what those passes read and where. A dated event is append-only
    under QUAL-11, and tools/qualc/authoring.py refuses a commit that changes or
    deletes one, so those locators remain as the record of their day; this event
    is the card's statement that no page locator stands in its own text.

    (3) The published solution. The event of 2026-11-19 recorded that no retained
    solution set contains a solution of IV.6.7 itself. That is false, and it is
    superseded. Andrew Egbert, Solutions to Hartshorne's Algebraic Geometry
    (October 3, 2013), Exercise IV.6.7, is a solution of the exercise, retained at
    assets/attachments/Andrew Egbert.pdf and extracted at
    tmp/sources/hartshorne-solutions-egbert.md. It is now transcribed as the first
    solution on the card, in Egbert's order and with his claims, and checked
    against the book: Remark IV.6.4.1(a) for the plane-curve genus, Theorem IV.6.4
    for Castelnuovo's bound, Exercise IV.3.4(b) for degree 3, Exercise IV.3.6(a)
    and (b) for degree 4, Example II.7.8.6 for the rational quartic and Remark
    IV.6.4.1(c) for its type (1,3) on the quadric, whose rulings are the fibres of
    the two projections. Two claims of his text are terse rather than proved -- the planar
    case, where an inflection point is not an argument, and the projection from a
    general point being an isomorphism onto a nonsingular plane curve of degree
    d-1 -- and the card's own proof, now the second solution and labelled as
    such, supplies both. What the transcription does not do is derive Egbert's
    argument afresh: it is his steps in his order.

    Checked for this pass: each numbered statement above in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, and Egbert's text of the
    exercise in tmp/sources/hartshorne-solutions-egbert.md. Not checked: the body
    of Kaji 1986, as before, the step resting on the restatement in Fukasawa,
    arXiv:2108.00650v3, section 1.

---

::: {.problem}
Over an algebraically closed field of characteristic zero, the line, the
conic, the twisted cubic and the elliptic quartic in $\PP^3$ have no
multisecants. Every other smooth integral curve in $\PP^3$ has infinitely
many multisecants.

A multisecant of $X$ is a line $\ell\not\subseteq X$ meeting $X$ in at least
three distinct points.

Hint: Consider a projection from a point of the curve to $\PP^2$.
:::

::: {.remark}
Hartshorne IV.6.7 states the converse without a characteristic restriction.
It fails in characteristic $p\ge3$, as the final step shows.

As in Hartshorne IV.3, in the definition that precedes Proposition IV.3.7, a multisecant is a
line meeting $X$ in at least three distinct points, and a tangent with intersection length $3$ at
one point is not a multisecant under that definition. The printed definition
does not exclude the line $X$ itself when $X$ is a line, and a line meets
itself in every one of its points, so under the letter of the definition the
first sentence of the exercise fails for the line alone. The statement above
therefore requires $\ell\not\subseteq X$: with that clause the printed first
sentence holds for all four curves, and without it the line is the one
exception. The clause changes nothing for
a planar curve of degree at least $2$ or for a nonplanar curve, since no line
is contained in one of those. Smoothness and integrality are not extra
hypotheses: the opening paragraph of IV.1 reserves the word curve, in that chapter,
for a nonsingular projective curve. The only hypothesis this card adds to the
printed second sentence is characteristic zero, and the final step shows that
it is needed.
:::

::: {.solution title="Published solution"}
The exercise is Hartshorne IV.6.7. The published solution transcribed here is
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013),
Exercise IV.6.7, and this block follows his argument in his order and with his
claims. Every result he invokes is cited below by the book's numbered statement;
the paragraph after the proof records what that check found, including the two
places where his text is terse rather than complete. The second solution on this
card is the card's own, and it supplies those two places.

::: pf

::: {.pf-step #egbert-planar}
A curve with no multisecants that lies in a plane is a line or a conic.

::: pf-proof
Egbert's reason is that a plane curve of degree at least $3$ "would have at least
one inflection and thus a trisecant". An inflection point is not a trisecant, so
that sentence is not a proof of the step; the conclusion is true, and the book's
route is the dual curve of Exercise I.7.3, which step s4 of the second solution
follows. A plane curve of degree $1$ is a line and one of degree $2$ is a conic,
which is the rest of the claim.
:::

:::

::: {.pf-step #egbert-projection}
Let $X\subseteq\PP^3$ be a nonplanar curve of degree $d$ with no multisecants.
Then the projection of $X$ from a general point of $X$ is an isomorphism onto a
nonsingular plane curve of degree $d-1$, whose genus is $\frac12(d-2)(d-3)$.

::: pf-proof
The projection from a point $P\in X$ is given by the planes through $P$ and has
degree $d-1$, since a general plane through $P$ meets $X$ in $d$ points, one of
them $P$. Egbert takes the point general on $X$ and the projection an isomorphism
onto its image, and this is the claim his text does not prove; granted it, the
image is a nonsingular plane curve of degree $d-1$ isomorphic to $X$, and its
genus is $\frac12(d-2)(d-3)$ by Remark IV.6.4.1(a), which states the genus of a
nonsingular plane curve of degree $e$ for every $e\ge1$.
:::

:::

::: {.pf-step #egbert-castelnuovo}
Castelnuovo's bound forces $d=3$ or $d=4$.

::: pf-proof
By Theorem IV.6.4, a curve of degree $d$ and genus $g$ in $\PP^3$ not contained
in any plane has $d\ge3$ and
$$
g\le
\begin{cases}
\frac14d^2-d+1, & d\ \text{even},\\[2pt]
\frac14(d^2-1)-d+1, & d\ \text{odd}.
\end{cases}
$$
With $g=\frac12(d-2)(d-3)$ from step [](#egbert-projection){.pf-ref}, the even
case gives $\frac12(d-2)(d-3)\le\frac14d^2-d+1$, that is $d^2-6d+8\le0$, so
$2\le d\le4$ and $d=4$; the odd case gives
$\frac12(d-2)(d-3)\le\frac14(d^2-1)-d+1$, that is $(d-3)^2\le0$, so $d=3$.
:::

:::

::: {.pf-step #egbert-degree-three}
If $d=3$, then $X$ is the twisted cubic.

::: pf-proof
By step [](#egbert-projection){.pf-ref} the genus is $0$, and a curve of degree
$3$ in $\PP^3$ not contained in any plane differs from the rational normal curve
of degree $3$ only by an automorphism of $\PP^3$, by Exercise IV.3.4(b); that
curve is the twisted cubic.
:::

:::

::: {.pf-step #egbert-degree-four}
If $d=4$, then $X$ is the elliptic quartic.

::: pf-proof
By step [](#egbert-projection){.pf-ref} the genus is $1$, and a curve of degree
$4$ and genus $1$ in $\PP^3$ is a complete intersection of two irreducible quadric
surfaces, by Exercise IV.3.6(b), that is the elliptic quartic. Exercise IV.3.6(a)
is what exhausts the alternatives: a curve of degree $4$ in $\PP^3$ has genus $0$
or $1$, the genus-$0$ case being the rational quartic, which is the next step.
Egbert adds that the elliptic quartic "has no trisecants"; that is the first
sentence of the exercise, and step s3 of the second solution proves it.
:::

:::

::: {.pf-step #egbert-rational-quartic}
A rational quartic in $\PP^3$ has trisecants, so the genus-$0$ case of degree $4$
is no exception.

::: pf-proof
Egbert writes that a rational quartic lies on a smooth quadric surface as a curve
of type $(1,3)$ and that its trisecants are the lines of one of the two rulings.
The parametrization $(t^4:t^3u:tu^3:u^4)$ of the rational quartic in Example
II.7.8.6 satisfies $X_0X_3=X_1X_2=t^4u^4$, so the curve lies on the smooth quadric
$X_0X_3=X_1X_2$, whose two rulings are the fibres of the two projections to
$\PP^1$ that read off $[X_0:X_1]$ and $[X_1:X_3]$. On the curve those two
projections are $[t:u]\mapsto[t:u]$ and $[t:u]\mapsto[t^3:u^3]$, of degrees $1$
and $3$, so a line of the first ruling meets the curve in one point and a line of
the second in three: the lines of the second ruling are its trisecants, and the
curve is of type $(1,3)$ in the sense of Remark IV.6.4.1(c).
:::

:::

::: pf-qed
Steps [](#egbert-planar){.pf-ref}--[](#egbert-degree-four){.pf-ref} show that a
curve with no multisecants is a line, a conic, the twisted cubic or the elliptic
quartic. Egbert assumes that there are no multisecants where the exercise's second
sentence needs only finitely many, and takes the point of projection general on
$X$; with "no" read as "finitely many" and the point taken outside the finitely
many exceptional lines, the argument gives that sentence.
:::

:::

Checked against the book. The genus of a nonsingular plane curve of degree $e$ is
$\frac12(e-1)(e-2)$ by Remark IV.6.4.1(a), which states it for every $e\ge1$, and
that is the formula Egbert applies with $e=d-1$. Castelnuovo's bound is Theorem
IV.6.4, whose hypotheses are degree $d$ and genus $g$ in $\PP^3$ not contained in
any plane, and whose conclusion carries $d\ge3$; both branches are the ones Egbert
writes, and both of his simplifications are correct. The classifications of the
degree-$3$ and degree-$4$ cases are Exercise IV.3.4(b) and Exercise IV.3.6(a) and
(b). Two claims his text does not prove are named here rather than supplied: the
planar case of step [](#egbert-planar){.pf-ref}, where an inflection point is not
an argument, the book's route being the dual curve of Exercise I.7.3, and the
isomorphism of step [](#egbert-projection){.pf-ref}, which is the content of steps
s5--s9 of the second solution under the finiteness hypothesis. Those two are why
the second solution is kept.
:::

::: {.solution title="The card's own proof"}
This proof is the card's own, and it is what the transcription above leaves out:
the planar case, in its step s4, and the projection being a closed immersion, in
its steps s6--s9, both under the hypothesis that there are only finitely many
multisecants and finitely many exceptional tangents. It also proves the
counterexample in characteristic $p$ that the exercise, stated without a
characteristic hypothesis, requires.

::: pf

::: {.pf-step #s1}

A line and a nonsingular plane conic have no multisecants.

::: pf-proof

Let $X$ be a line. Under the convention of the remark above a multisecant of
$X$ is a line $\ell\not\subseteq X$, and such a line meets $X$ in at most one
point, since two distinct points of $X$ determine the line $X$. Under the
printed definition, which does not exclude $\ell=X$, the only line meeting
$X$ in three distinct points is $X$ itself.

Let $X$ be a nonsingular plane conic.  No line is contained in $X$, and any
line meets the degree-$2$ plane curve $X$ in scheme-theoretic length at most
$2$ by Bezout's theorem, Corollary I.7.8.  Hence no line is a multisecant.

:::

:::

::: {.pf-step #s2}

The twisted cubic has no multisecants.

::: pf-proof

By [[P-AGH434RATIONALNORMALCURVE|Exercise IV.3.4(a)]], the homogeneous ideal of
the twisted cubic is generated by quadrics.  Suppose a multisecant $\ell\not\subseteq X$
met the twisted cubic in length at least $3$.  Every quadric vanishing on the
curve restricts to a section of
$$
\OO_\ell(2)
$$
vanishing on a subscheme of length at least $3$.  Such a section must be
zero, since a nonzero section of $\OO_\ell(2)$ has at most $2$ zeros counted
with multiplicity, so every defining quadric contains $\ell$.  Since those quadrics
generate the ideal of the twisted cubic, their scheme-theoretic intersection
is the curve itself.  Thus $\ell$ would be contained in the twisted cubic,
impossible for a line $\ell\not\subseteq X$ having finite intersection with it.

:::

:::

::: {.pf-step #s3}

The elliptic quartic has no multisecants.

::: pf-proof

By [[P-AGH436CURVESOFDEGREEFOUR|Exercise IV.3.6(b)]], an elliptic quartic is a
complete intersection
$$
X=Q_1\cap Q_2
$$
of two irreducible quadric surfaces in $\PP^3$.

If a multisecant $\ell\not\subseteq X$ met $X$ in length at least $3$, then each
quadratic
equation $\restrictionof{Q_i}{\ell}$ would be a section of $\OO_\ell(2)$ vanishing on a
subscheme of length at least $3$.  Such a section is zero, as in step
[](#s2){.pf-ref}, so both restrictions would vanish
identically.  Thus
$$
\ell\subseteq Q_1\cap Q_2=X,
$$
again contradicting the requirement that a multisecant have finite
intersection with $X$.

:::

:::

::: {.pf-step #s4}

Suppose that a curve $X\subseteq\PP^3$ has only finitely many
multisecants.  If $X$ is planar, then $X$ is a line or a conic.

::: pf-proof

Let $X$ lie in a plane and have degree $d$.  If $d\ge3$, then a general line
in that plane meets the smooth curve $X$ transversely in $d$ distinct points:
the lines meeting $X$ non-transversely are exactly the tangent lines, and these
form the dual curve, a proper closed subset of the dual plane by Exercise I.7.3.  Hence the set of
transverse lines is a nonempty open subset of the dual plane, so
there are infinitely many such lines.  Each is a multisecant, contrary to
the finiteness hypothesis.

Therefore $d\le2$.  A smooth integral plane curve of degree $1$ is a line,
and one of degree $2$ is a conic.

:::

:::

::: {.pf-step #s5}

Now suppose $X$ is nonplanar and has only finitely many multisecants and
only finitely many tangent lines meeting $X$ again or having contact order
at least $3$.
There is a point
$$
P\in X
$$
with the three properties

(i) $P$ lies on no multisecant of $X$;

(ii) $P$ lies on no tangent line $T_QX$ with $Q\ne P$;

(iii) the tangent line $T_PX$ meets $X$ only at $P$, and there with length
exactly $2$,

and for this $P$ the projection is a closed immersion.

::: pf-proof

Each line of the two finite families meets the integral curve $X$ in a finite
set of points, since a line meeting $X$ in infinitely many points would be
contained in $X$ and so, $X$ being integral of dimension $1$, would make $X$ a
line, contrary to nonplanarity; the union of these finitely many finite sets is
finite.
Choose
$$
P\in X
$$
outside it, which is possible because a curve over an algebraically closed
field has infinitely many points.

Then (i) holds, because a multisecant through $P$ is one of the finitely many
multisecants, and $P$ lies on none of them. (ii) holds, because if
$P\in T_QX$ with $Q\ne P$, then $T_QX$ is a tangent line meeting $X$ again and
so belongs to the second family, and then $P\in T_QX\cap X$ would have been
excluded. (iii) holds, because if $T_PX$ met $X$ at a further point, or if its
contact order at $P$ were at least $3$, then $T_PX$ would belong to the second
family and $P\in T_PX\cap X$ would again have been excluded; the contact order
of a tangent line is at least $2$, so it is exactly $2$.

Steps [](#s6){.pf-ref}--[](#s9){.pf-ref} prove that projection from this point
is a closed immersion, using (i)--(iii).

:::

:::

::: {.pf-step #tangent-char-zero}

In characteristic zero, the tangent-line finiteness assumption in step
[](#s5){.pf-ref} holds for every smooth nonplanar curve $X$.

::: pf-proof

Kaji's theorem in characteristic zero, in the form stated and cited by Fukasawa (*A generalization of Esteves--Homma's example of tangentially degenerate curves*, [arXiv:2108.00650v3](https://arxiv.org/abs/2108.00650v3), §1, where both sentences used here stand): an irreducible projective curve $C\subset\PP^N$ with $N\ge3$, not contained in any plane, over an algebraically closed field of characteristic $0$, is *tangentially degenerate* when $T_PC$ meets $C$ away from $P$ for a general $P\in C$, and **no such curve is tangentially degenerate when the morphism $X\to\PP^N$ induced by the normalization $\phi\colon X\to C$ is unramified**. Each hypothesis holds here: $\PP^3$ has $N=3$, the field is algebraically closed of characteristic zero, $X$ is nonplanar, and $X$ is smooth, so its normalization is an isomorphism and hence unramified. So the tangent line at a general point does not meet the curve at a second point. (Kaji's original is *On the tangentially degenerate curves*, J. London Math. Soc. (2) **33** (1986) 430--440, [doi:10.1112/jlms/s2-33.3.430](https://doi.org/10.1112/jlms/s2-33.3.430); the restatement above is the source consulted.) That statement is about a general point; passing to
"all but finitely many" needs the second-point incidence, and the distinctness
$Q\ne P$ is essential to it. In homogeneous coordinates put
$$
Z=\{(P,Q)\in X\times X:\ X(Q)\in\langle X(P),X'(P)\rangle\},
$$
the vanishing locus of the $3\times3$ minors of the $4\times3$ matrix with
columns $X(P)$, $X'(P)$, $X(Q)$, so that $Z$ is closed. The diagonal is
contained in $Z$, because $X(P)$ lies in the span of $X(P)$ and $X'(P)$
trivially; for that reason $Z$ is useless here, its projection to the first
factor being all of $X$. Remove the diagonal, which is the locus excluded by the
statement, and take the second-point incidence
$$
Z^{*}=\{(P,Q)\in X\times X:\ Q\ne P,\ X(Q)\in\langle X(P),X'(P)\rangle\}
=Z\smallsetminus\Delta .
$$
This is locally closed, hence constructible, though not closed. Let
$$
B=\operatorname{pr}_1(Z^{*})
$$
be the set of points whose tangent line meets $X$ again at a point other than
$P$. Since $Z^{*}$ is constructible, $B$ is constructible, by Chevalley's
theorem, Exercise II.3.19, that the image of a constructible set under a morphism of varieties is
constructible; this is where the diagonal having been removed matters, since the
image of $Z$ itself is $X$. Kaji's theorem says that no point of $Z^{*}$ lies
over the generic point of $X$, so $B$ does not contain that generic point. A
constructible subset of a curve that omits the generic point is finite, so $B$
is finite: for all but finitely many $P$, the tangent line meets $X$ only at
$P$.

The points where the tangent line has contact order at least $3$ are also
finite. Again this is a closed condition on $X$: contact order at least $3$ at
$P$ means that $X(P)$, $X'(P)$ and $X''(P)$ are linearly dependent, which is the
vanishing of the $3\times3$ minors of the $4\times3$ matrix with those three
columns, and in a local parameter $t$ those minors are power series in $t$.
Suppose the condition held at the generic point $\eta$ of $X$. Fix affine
coordinates $x,y,z$ on a chart that $X$ meets, with $x$ nonconstant. Since $x$ is nonconstant, $k(X)$ is finite over
$k(x)$, and it is separable because the characteristic is $0$; the derivation of
$k(x)$ carrying $x$ to $1$ therefore extends uniquely to a derivation $d/dx$ of
$k(X)$, and at $\eta$ the condition is
$$
\frac{d^2y}{dx^2}=\frac{d^2z}{dx^2}=0 ,
$$
because $X''(\eta)$ is a multiple of $X'(\eta)$ exactly when
$y''x'-y'x''=z''x'-z'x''=0$, where $'=d/dt$, and $x'\ne0$ at $\eta$. The kernel
of $d/dx$ is $k$. It does not follow from the kernel omitting the nonconstant $x$:
a subfield of a function field of transcendence degree $1$ can omit a nonconstant
element and still have transcendence degree $1$, as $k(t^2)$ does in $k(t)$. Let
$f\in k(X)$ satisfy $df/dx=0$ and suppose that $f\notin k$. Then $f$ is
transcendental over $k$, since $k$ is algebraically closed, so $k(f)$ has
transcendence degree $1$ over $k$, equal to that of $k(X)$, and $k(X)$ is a
finite extension of $k(f)$, because a finitely generated extension of
transcendence degree $0$ is finite; that extension is separable, the
characteristic being $0$. The derivation $d/dx$ vanishes on $k(f)$, on $k$ by
definition and on $f$ by hypothesis, and a derivation of a finite separable
extension that vanishes on the base field is zero: if $k(X)=k(f)(\alpha)$ and
$g\in k(f)[T]$ is the minimal polynomial of $\alpha$, then applying $d/dx$ to
$g(\alpha)=0$ gives $g'(\alpha)\,d\alpha/dx=0$, because the coefficients of $g$
lie in $k(f)$, and $g'(\alpha)\ne0$ because $\alpha$ is separable over $k(f)$;
hence $d\alpha/dx=0$ and $d/dx=0$ on $k(X)$, contradicting $d(x)/dx=1$. So no such
$f$ exists and the kernel is $k$. Hence
$$
\frac{dy}{dx}=c\in k,
\qquad
\frac{dz}{dx}=e\in k,
$$
so that $y=cx+d$ and $z=ex+f$ with $c,d,e,f\in k$, and $X$ lies on the line
$\{y=cx+d,\ z=ex+f\}$, contrary to the nonplanarity assumption. The condition
therefore fails at the generic point, and being closed it is a proper closed
subset of the curve $X$, hence finite.

:::

:::

::: {.pf-step #s6}

Projection from the point $P$ of step [](#s5){.pf-ref} extends to a morphism
$$
\pi_P:X\longrightarrow\PP^2
$$
defined by the base-point-free linear system cut out by planes through $P$
after subtracting the fixed point $P$.  Its line bundle is
$$
H-P,
\qquad
H=\OO_X(1).
$$

::: pf-proof

The planes through $P$ are parametrized by a $\PP^2$, that is, by a
three-dimensional space of linear forms, and restriction to $X$ is injective
on that space because $X$ is not contained in a plane; so the planes through
$P$ cut out a three-dimensional space of sections of $H$.  Every
plane through $P$ contains $P$, so every one of these sections vanishes at
$P$, and the space lies in
$$
H^0(X,H\otimes\OO_X(-P))=H^0(X,H-P):
$$
after the common zero at $P$ is removed it is a three-dimensional space of
sections of $H-P$.

At a point $Q\ne P$, some plane through $P$ avoids $Q$, so these sections
have no base point there.  At $P$, choose a plane through $P$ not containing
the tangent line $T_PX$; its section vanishes to order exactly one at $P$,
and hence gives a nonzero value after subtracting $P$.  Thus the induced
linear system on $H-P$ is base-point free and defines the stated morphism.

:::

:::

::: {.pf-step #s7}

The morphism $\pi_P$ separates points of $X$.

::: pf-proof

For distinct points $Q,R\ne P$, equality
$$
\pi_P(Q)=\pi_P(R)
$$
means that $P,Q,R$ are collinear.  Their common line would meet $X$ in at
least three distinct points and hence be a multisecant through $P$, contrary
to property (i) of $P$ in step [](#s5){.pf-ref}.

The image of $P$ itself under the extended projection is the tangent direction
$T_PX$: all sections of the system vanish at $P$, so their value there is
their derivative, and the point they define is the image of the line $T_PX$.
If some $Q\ne P$ had
$$
\pi_P(Q)=\pi_P(P),
$$
then the line $PQ$ would be that same line through $P$, so $PQ=T_PX$.  Its
intersection with $X$ would
have length at least $2$ at $P$ and would also contain $Q$, which property
(iii) of $P$ in step [](#s5){.pf-ref} forbids. Thus $\pi_P$ separates all
points.

:::

:::

::: {.pf-step #s8}

The morphism $\pi_P$ separates tangent vectors of $X$.

::: pf-proof

Let $Q\ne P$.  The differential of projection at $Q$ fails to be injective
exactly when the center $P$ lies on the embedded tangent line $T_QX$.  In
that case $P$ lies on $T_QX$ with $Q\ne P$, which property (ii) of $P$ in step
[](#s5){.pf-ref} forbids.

At $P$, choose affine coordinates centered at $P$ in which the tangent line
is the $x$-axis and a local parameter $t$ on $X$ has expansions
$$
x=t+O(t^2),
\qquad
y=a_2t^2+O(t^3),
\qquad
z=b_2t^2+O(t^3).
$$
After cancelling the common factor $t$ in the projection from $P$, the
local map is represented near $P$ by
$$
[1+O(t):a_2t+O(t^2):b_2t+O(t^2)].
$$
Its differential at $P$ vanishes exactly when
$$
a_2=b_2=0.
$$
That condition says that both transverse coordinates vanish to order at
least $3$, so the tangent line meets $X$ at $P$ with length at least $3$,
which property (iii) of $P$ in step [](#s5){.pf-ref} forbids. Hence $\pi_P$
separates tangent vectors everywhere.

:::

:::

::: {.pf-step #s9}

The projection $\pi_P$ is a closed immersion, and its image is a
nonsingular plane curve of degree $d-1$, where $d=\deg X$.

::: pf-proof

Steps [](#s7){.pf-ref} and [](#s8){.pf-ref} show that the base-point-free linear system in step [](#s6){.pf-ref}
separates points and tangent vectors: the two conditions of the closed-immersion
criterion are, equivalently, the injectivity of $\pi_P$ on closed points and the
injectivity of its differential at each closed point, which is the form in which
steps [](#s7){.pf-ref} and [](#s8){.pf-ref} establish them.  By the
[[T-DIVMAPPN|closed-immersion criterion for a linear system]], Proposition II.7.3
with Remark II.7.8.2, $\pi_P$ is a
closed immersion.

Moreover,
$$
\pi_P^*\OO_{\PP^2}(1)\cong\OO_X(H-P),
$$
whose degree is
$$
d-1.
$$
Because $\pi_P$ is an embedding, its plane image therefore has degree
$d-1$ and is isomorphic to the smooth curve $X$.

:::

:::

::: {.pf-step #s10}

Under the assumptions of step [](#s5){.pf-ref},
$$
g(X)=\frac{(d-2)(d-3)}2.
$$

::: pf-proof

By step [](#s9){.pf-ref}, $X$ is isomorphic to a nonsingular plane curve of degree
$d-1$.  The plane-curve genus formula, Remark IV.6.4.1(a), which states it for every
$d\ge1$, and Exercise II.8.4(f), gives
$$
g(X)
=
\frac{((d-1)-1)((d-1)-2)}2
=
\frac{(d-2)(d-3)}2.
$$

:::

:::

::: {.pf-step #s11}

Castelnuovo's bound and step [](#s10){.pf-ref} force
$$
d=3\quad\text{or}\quad d=4.
$$

::: pf-proof

The curve is nonplanar, so [[T-CRVCAST|Castelnuovo's bound]], Theorem IV.6.4, applies.

If $d$ is even, steps [](#s10){.pf-ref} and Castelnuovo give
$$
\frac{(d-2)(d-3)}2
\le
\frac{d^2}{4}-d+1.
$$
After multiplying by $4$ and simplifying,
$$
(d-2)(d-4)\le0.
$$
Since a nonplanar curve has degree at least $3$, the even case gives
$$
d=4.
$$

If $d$ is odd, the corresponding inequality is
$$
\frac{(d-2)(d-3)}2
\le
\frac{d^2-1}{4}-d+1,
$$
which simplifies to
$$
(d-3)^2\le0.
$$
Hence
$$
d=3.
$$

:::

:::

::: {.pf-step #s12}

A smooth integral nonplanar curve satisfying the two finiteness assumptions in
step [](#s5){.pf-ref} is either the twisted cubic or the elliptic quartic.

::: pf-proof

If $d=3$, [[P-AGH434RATIONALNORMALCURVE|Exercise IV.3.4(b)]] says that a
nonplanar degree-$3$ curve in $\PP^3$ is the twisted cubic.

If $d=4$, step [](#s10){.pf-ref} gives
$$
g(X)=1.
$$
By [[P-AGH436CURVESOFDEGREEFOUR|Exercise IV.3.6(b)]], a nonplanar degree-$4$
curve of genus $1$ is the elliptic quartic, equivalently a complete
intersection of two irreducible quadric surfaces.

:::

:::

::: {.pf-step #s13}

In characteristic zero, a smooth integral curve with only finitely many
multisecants is one of the four listed curves.

::: pf-proof

Suppose a curve had only finitely many multisecants. If it were
planar, step [](#s4){.pf-ref} would make it a line or a conic.  If it were nonplanar,
step [](#s12){.pf-ref} would make it a twisted cubic or an elliptic quartic.

Step [](#tangent-char-zero){.pf-ref} supplies the tangent-contact hypothesis
of step [](#s5){.pf-ref}, so the conclusion holds in characteristic zero.

:::

:::

::: {.pf-step #positive-char-counterexample}

For every prime $p\ge3$, there is a smooth nonplanar curve of degree $p+1$
in characteristic $p$ with no multisecants.

::: pf-proof

Let $k$ be algebraically closed of characteristic $p$, and map $\PP^1$ to
$\PP^3$ by
$$
[s:t]\longmapsto
[s^{p+1}:s^pt:st^p:t^{p+1}].
$$
On $s\ne0$, the first two coordinates recover $t/s$; on $t\ne0$, the last
two recover $s/t$. These coordinates also separate tangent vectors on both
charts: on $s\ne0$ the map is $u\mapsto(1,u,u^p,u^{p+1})$ with derivative
$(0,1,0,u^p)$, and on $t\ne0$ it is $v\mapsto(v^{p+1},v^p,v,1)$ with
derivative $(v^p,0,1,0)$, neither of which vanishes. So the differential is
injective everywhere, and with injectivity on points and $\PP^1$ proper the
map is a closed immersion. Its image $C$ is smooth and has
degree $p+1$. The four coordinate sections are linearly independent, since
on $s\ne0$ they are $1,u,u^p,u^{p+1}$; hence $C$ is nonplanar. It lies on
the smooth quadric
$$
Q=\{X_0X_3=X_1X_2\}.
$$

A line meeting $C$ in three distinct points meets $Q$ in three distinct
points, and a line not contained in a quadric surface meets it in at most two
points by Theorem I.7.7, so it must lie on $Q$. Every point of $Q$ is a rank-one
matrix
$$
\begin{pmatrix}X_0&X_1\\X_2&X_3\end{pmatrix}
=
\begin{pmatrix}u_0\\u_1\end{pmatrix}
\begin{pmatrix}v_0&v_1\end{pmatrix},
$$
and the two rulings of $Q$ are the loci on which one of the two factors is
fixed. The curve $C$ is the set of these matrices with
$$
(u_0,u_1)=(s^p,t^p),
\qquad
(v_0,v_1)=(s,t).
$$

Let $L$ be a ruling of the first kind, on which $(u_0:u_1)=(a^p:b^p)$ for some
$[a:b]\in\PP^1$; every ruling of that kind has this form because $x\mapsto x^p$
is bijective on the algebraically closed field $k$. A point of $C$ on $L$
satisfies $(s^p,t^p)=\lambda(a^p,b^p)$ for some nonzero $\lambda$, and $\lambda$
has a $p$-th root $\mu$, so $s^p=(\mu a)^p$ and $t^p=(\mu b)^p$; since
$x^p=y^p$ forces $x=y$ in a field of characteristic $p$, $(s,t)=(\mu a,\mu b)$.
So $L$ meets $C$ in the single point $[a:b]$.

Let $M$ be a ruling of the second kind, on which $(v_0:v_1)=(a:b)$ for some
$[a:b]$. A point of $C$ on $M$ satisfies $(s,t)=\mu(a,b)$ for some nonzero
$\mu$, and then $(s^p,t^p)=(\mu^p a^p,\mu^p b^p)$, so the point of $C$ is
determined by $[a:b]$ alone. So $M$ meets $C$ in the single point $[a:b]$ as
well. No line contains three distinct points of $C$.

Since $p+1\ge4$ and $C$ has genus $0$, it is none of the four curves in the
exercise. This disproves the unrestricted converse.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove that
the four stated curves have no multisecants. Steps [](#s4){.pf-ref} and
[](#s13){.pf-ref} prove the characteristic-zero converse.
Step [](#positive-char-counterexample){.pf-ref} disproves its unrestricted
form.

:::

:::

:::

::: {.remark}
The exercise is Hartshorne, Exercise IV.6.7, printed without qualification: "The line, the conic, the twisted cubic curve and the elliptic quartic curve in $\PP^3$ have no multisecants.  Every other curve in $\PP^3$ has infinitely many multisecants."  Two qualifications are needed, and the statement above carries both.  In characteristic $p\ge3$ the second sentence is false: the graph of Frobenius of degree $p+1$ on a smooth quadric surface is a smooth nonplanar curve through which no line passes meeting it in three distinct points, and the last step proves this.  The second sentence also fails for singular curves in characteristic zero: the rational quartic $X$ parametrized by $[s:t]\mapsto[s^4:s^2t^2:st^3:t^4]$ is $Q_1\cap Q_2$ for $Q_1=X_0X_3-X_1^2$ and $Q_2=X_1X_3-X_2^2$, so it is integral, nonplanar and of degree $4$, and it is singular at $[1:0:0:0]$, where the gradient of $Q_2$ vanishes; it has no multisecants, since a trisecant would meet each quadric in three distinct points, hence lie on both, hence lie in $X$, impossible for a line contained in a curve of degree $4$; and it is neither the twisted cubic nor the elliptic quartic.  Neither qualification is an addition to the printed exercise as the book intends it, since the Terminology reserves the word curve, in Chapter IV, for a nonsingular projective curve: characteristic zero is the one hypothesis this card adds, and the printed hint, projection from a point of the curve to $\PP^2$, is the route the proof takes.
:::
