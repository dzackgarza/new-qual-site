---

schema: qual/card@1
id: E-HAT-3.3-21
kind: problem
title: Compactly supported cohomology and one-point compactification
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 21; it matches the printed text. The printed bracketed question about $X=\ZZ\times\RR$ was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: excision identifies $H^n(X^+,U_K;G)$ with $H^n(X,X-K;G)$, cone-shaped
    neighbourhoods are cofinal, and on each of them the point $\infty$ is a homotopy equivalence,
    so the limit is $H^n(X^+,\infty;G)$.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The print says "let $X^+$ be the one-point compactification" without hypotheses; that object is
    a compact Hausdorff compactification only when $X$ is locally compact Hausdorff, which the
    solution now states instead of using silently. The sets $U_K$ were also said to "range over all"
    neighbourhoods of $\infty$, which is false — they are cofinal, and the cofinality is now proved.
    DEFERRED, recorded not dropped: the printed bracketed question for $X=\ZZ\times\RR$ is not
    answered. Its hypothesis fails there, since the complement of a compact set meets infinitely many
    lines in unbounded intervals, and the card says only that; whether the isomorphism still holds is
    open on this card.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The bracketed question is now answered from Stanford Math 215C Solution Set 4, Hatcher 3.3.21,
    printed p.1. H_c^1(Z x R) is countable because cofinal rectangles K_N have finite relative
    cohomology Z^{2N+1}: each of the 2N+1 lines in K_N contributes one H^1(R,R-J_m)=Z summand. In
    contrast the circle retractions give H^1((Z x R)^+) containing Hom of the product of Z over N,
    hence uncountable. So no such isomorphism exists; the earlier lim^1 remark was unnecessary and
    has been removed.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Withdraws the incorrect counterexample and its audit claim. A surjection H_1(X+) to the product
    of Z gives an injection on the corresponding Hom groups, not uncountability; and the Hom group
    of the product is itself countable by Specker's theorem. Frankland, Cohomology of the Hawaiian
    Earring (2017), Theorems 1.2 and 1.3 (p.2) gives H^1(E;Z) equal to the countable direct sum,
    and Theorem 1.4 (p.3) the induced dual iso. Stanford Solution Set 4's false counterexample is
    removed. The definite answer to Hatcher's bracketed question is not established from this
    source and remains deferred.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Answers the bracketed question negatively in degree two with integer coefficients. The
    cofinal-rectangle calculation gives H_c^2(Z x R; Z) = 0. The compactification is the
    Hawaiian earring E, whose H_1 has a Q direct summand by Eda-Kawamura, Theorem 3.1,
    pp.307-310 (also stated as Frankland Theorem 2.1, p.3). Universal coefficients and
    Wiegold's nonzero Ext(Q,Z), pp.341-342, then give H^2(E; Z) != 0, so the natural map is not
    an isomorphism. Replaces the deferred and H^1-only discussion with an argument assembled from
    separately published theorems, not with a published complete exercise solution. The #105
    published-solution obligation stays open; the cone-neighborhood proof in the first part is
    unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read Hatcher pp.243-244 and the complete Eda-Kawamura and Wiegold papers. Checked that
    H^2(E, infinity; Z) agrees with H^2(E; Z) by the pair sequence, that Ext is additive over
    the Q direct summand, and that the cofinal relative intervals make all degree-two compactly
    supported groups vanish. Thus this is a counterexample already for n = 2 and G = Z, not a
    claim that H^1 fails or that no coefficient group could work.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Removed the unsupported assertion that inverse stereographic projection proves the absence
    of a cone neighborhood. The final paragraph now uses the justified implication instead: the
    degree-two contradiction proves that the cone-neighborhood hypothesis of the first part cannot
    hold for Z x R. Eda-Kawamura and Wiegold remain supporting citations only; a complete published
    solution to the exercise has not been located, so the #105 source obligation remains open.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Located and checked the complete published solution of the first part: Stanford Math 215C,
    Solution Set 4, Hatcher 3.3.21, printed p. 1, served at
    http://math.stanford.edu/~ralph/math215c/solution4.pdf and held as
    tmp/sources/stanford-math215c-spring2009-solution4.pdf, 59584 bytes, sha256
    b4c348109162ed7e97309e15f1b153efa363cd0338800e8d251f64f335eef470, the local size matching the
    served content length. Checked its steps: excision of the point infinity out of the open set
    X^+ - K is legitimate because the closure of {infinity} is {infinity}, contained in that open
    set, and gives H^n(X^+, X^+ - K) = H^n(X, X - K); the exact sequence of the pair (X^+, U_K) is
    reduced and legitimate as both entries are nonempty; for K the complement of a cone-shaped
    neighbourhood U_K is a cone, hence contractible with vanishing reduced cohomology, which is
    what makes the restriction H^n(X^+, U_K) -> H^n(X^+, infinity) an isomorphism; the K's of this
    form are cofinal among compact subsets since cone-shaped neighbourhoods can be shrunk inside any
    neighbourhood of infinity, and the isomorphisms are compatible with inclusions, so they pass to
    the direct limit. That is the argument already in steps excision-limit and cone-case, so this
    citation confirms rather than replaces them, and it discharges the published-solution
    obligation for the first part. This supersedes the closing sentence of the previous event,
    which said no complete published solution had been located. NOT used and explicitly rejected in
    the card: the source's paragraph on Z x R, which infers uncountability of H^1 from a surjection
    H_1 -> product of Z, whereas dualizing a surjection gives an injection and Hom(product Z, Z) is
    the countable direct sum by Specker's theorem. The bracketed question therefore still rests on
    the assembled degree-two counterexample from Eda-Kawamura and Wiegold, not on a published
    complete exercise solution, and that narrower obligation stays open.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    Re-read for the published-solution obligation. The card's first part is the complete published solution of Stanford Math 215C, Spring 2009, Solution Set 4, Hatcher §3.3 Exercise 21, printed p. 1: excision to move $H^n(X^+,X^+-K;G)$ to $H^n(X,X-K;G)$, cone-shaped neighbourhoods of $\infty$ as a cofinal system of compact sets, the exact sequence of the pair forcing $\tilde H^m(U_K;G)=0$, and the direct limit over the cofinal system. Checked against the book: the exercise's printed statement on p. 262 with its cone hypothesis, and the definition of compactly supported cohomology. Not claimed: the set's own paragraph on $X=\ZZ\times\RR$ is rejected on the card and the card's counterexample there stands; the citation covers the first part only.
- event: source-corrected
  by: claude
  date: 2026-11-13
  note: >-
    The page in the preceding note is wrong and is corrected here: the exercise is on printed p. 259,
    the last page of §3.3, not p. 262, which is in §3.A. Read again in Hatcher, *Algebraic Topology*
    (2002), printed p. 259 and in the current online text at the same page: the statement there is
    "For a space $X$, let $X^+$ be the one-point compactification. If the added point, denoted
    $\infty$, has a neighborhood in $X^+$ that is a cone with $\infty$ the cone point, show that the
    evident map $H_c^n(X;G)\to H^n(X^+,\infty;G)$ is an isomorphism for all $n$. [Question: Does this
    result hold when $X=\ZZ\times\RR$?]", matching the card. The bracketed part remains as recorded:
    no published solution of it was located, in the retained sets or elsewhere, and the card answers
    it with its own degree-two counterexample. Searched without result for the bracketed part in the
    retained sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C Solution Sets 1--5, the UCR Math
    205B help file, May's *Concise Course*, Bredon, Maxim's Math 752 notes) and in Hatcher's text and
    errata; Hatcher's errata has no entry for §3.3 near this page.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    The degree-one cohomology of the compactification, which the card had only asserted to be
    uncountable-then-countable in a rejected argument, is now cited from a published source, supplied
    by the owner for #123 and read in the text version: Martin Frankland, *Cohomology of the Hawaiian
    Earring* (dated February 22, 2017), Theorem 1.3 and the sentence immediately after it, both on
    printed p. 2 of the note. Theorem 1.3 states that the map $H^1(E;\ZZ)\to\operatorname{Hom}_{\ZZ}
    (\bigoplus_\NN\ZZ,\ZZ)$ dual to $H_1(\iota)$ is injective with image $\bigoplus_\NN\ZZ$, and the
    sentence after it draws the conclusion $H^1(E)\cong\bigoplus_{n\in\NN}\ZZ$, "a free abelian group
    on countably many generators". Read only in degree one and only with integer coefficients, which
    is the part the note proves; the card does not cite it for any other degree. The reading copy is
    `tmp/sources/frankland-2017-cohomology-hawaiian-earring.md`; the PDF already held as
    `tmp/sources/frankland-hawaiian-earring-2017.pdf` is the same note, and Theorem 2.1 of it was
    already cited on this card for the $\QQ$ summand.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Added step "degree-one" to the solution: $H_c^1(\ZZ\times\RR;\ZZ)$ from the card's own cofinal
    rectangle computation, and $H^1((\ZZ\times\RR)^+,\infty;\ZZ)$ from Frankland's Theorem 1.3,
    printed p. 2, together with the exact sequence of the pair $(E,\infty)$. The step's point is
    negative and is what the rejected Stanford paragraph got wrong: both sides in degree one are free
    abelian on countably many generators, so no countability argument in degree one can decide the
    bracketed question, and the card's counterexample has to be, and is, in degree two. The card's
    closing paragraph now also says which part of the exercise is published (the first part, Stanford
    Math 215C Solution Set 4) and which is not (the bracketed question, whose answer here is assembled
    from Eda--Kawamura, Wiegold and Frankland). Not claimed: a published solution of the bracketed
    question; none was located, and the earlier events recording that stand.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    One step of the degree-one comparison was reasoned wrongly and is corrected. It derived the
    isomorphism $H^1(E,\infty;\ZZ)\cong H^1(E;\ZZ)$ from the vanishing of $H^0(E,\infty;\ZZ)$ alone,
    which gives injectivity only; surjectivity of $H^1(E,\infty;\ZZ)\to H^1(E;\ZZ)$ comes from
    $H^1(\{\infty\};\ZZ)=0$, since exactness at $H^1(E;\ZZ)$ identifies the image with the kernel of
    $H^1(E;\ZZ)\to H^1(\{\infty\};\ZZ)$, which is everything. The card now gives both reasons and
    states the resulting short exact sequence $0\to H^1(E,\infty;\ZZ)\to H^1(E;\ZZ)\to0$. The
    conclusion of the step is unchanged. Checked against Hatcher (2002), §3.3 Exercise 21 on printed
    p. 259 and the long exact sequence of a pair in cohomology, and against Frankland's Theorem 1.3
    with the sentence after it on printed p. 2, which supplies the value $H^1(E;\ZZ)\cong
    \bigoplus_{\NN}\ZZ$ used by the step.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    A second complete published solution of the first part is now cited on the card: C. Kottke, *Math
    2420 Problem Set 3 solutions*, Brown University, Spring 2012, Problem 2, printed p. 2 of
    `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.pdf` (5 pp., sha256
    e84fd60496037db45bb18457b7c922233f5912a41b5d067112ba75a8211c22a7). Read at that page and checked
    step by step: the disjoint neighbourhoods $U$ of $K$ and $V$ of $\infty$, $V$ shrunk inside the
    cone neighbourhood so that it deformation retracts to $\infty$, $L=X\setminus V$ compact with
    $K\subset L$, and $H^n(X,X\setminus L)=H^n(X,V)\cong H^n(X^+,V)\cong H^n(X^+,\infty)$ by
    excision of $\infty$ and the deformation retraction, then the direct limit over the cofinal
    family. It agrees with steps excision-limit and cone-case, which transcribe the Stanford set and
    are unchanged. The page claims already on the card were re-read at the sources this pass: Stanford
    Math 215C Solution Set 4, printed p. 1 (59584 bytes, sha256
    b4c348109162ed7e97309e15f1b153efa363cd0338800e8d251f64f335eef470); Frankland, Theorem 1.3 with
    the sentence after it on printed p. 2 and Theorem 2.1 on printed p. 3; Eda--Kawamura, Theorem 3.1
    on printed p. 307, whose third summand is $\bigoplus_\kappa\QQ$ with $\kappa=\cardinality{I^{\NN}}$, hence
    continuum many copies of $\QQ$ for $I=\NN$, which is the $\QQ$ summand the step uses and which the
    extracted text of that paper renders only as a stray glyph; Wiegold, pp. 341--342. The bracketed question
    still has no published solution, and the sources read for it this pass are recorded in
    `COMPLAINTS.md`: the accepted answer to Math Stack Exchange question 4224576 shows only that
    $\infty$ has no cone neighbourhood in the compactification of $\ZZ\times\RR$, which is not the
    question; question 4812778 poses the exercise and has no answers; Kottke's set has no paragraph on
    $\ZZ\times\RR$; and the Stanford set's paragraph is the rejected one. Checked against Hatcher
    (2002), §3.3 Exercise 21 on printed p. 259, and against Hatcher's errata, which carries no entry
    for that page.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Two corrections to the transcription of Kottke's solution and one to the citations. (1) The
    transcription followed the source's own slip in writing $H^n(X,V)$ for a group in which $V$ is an
    open set of $X^+$ containing $\infty$, and so is not a subset of $X$; the card now writes
    $H^n(X,V\setminus\{\infty\})\cong H^n(X^+,V)$ and says that the middle isomorphism is excision of
    the point $\infty$, closed in $X^+$ and contained in the open $V$, hence with closure inside the
    interior of $V$, so that excision is legitimate. The two outer groups are unchanged. (2) The
    duplicate PDF name `tmp/sources/frankland-hawaiian-earring-2017.pdf`, which was cited in step
    earring-degree-two, is the same note as `tmp/sources/frankland-2017-cohomology-hawaiian-earring.md`
    (identical bytes, checked with `md5sum`); the card now cites the text version and no longer names
    the duplicate. Theorem 1.3 with the sentence after it on printed p. 2 and Theorem 2.1 on printed
    p. 3 were re-read in that text version this pass, and the $\QQ$ direct summand is Theorem 2.1's
    $\bigoplus_{\mathfrak c}\QQ$ with $\mathfrak c=2^{\aleph_0}$. (3) Text versions are now named on
    every citation: Hatcher in `tmp/sources/hatcher-2002-algebraic-topology.md`, Frankland in its
    `.md`; Eda--Kawamura, Wiegold, Stanford Solution Set 4 and Kottke have no text version in
    `tmp/sources` and are named as read from their PDF text layers. Checked against Hatcher (2002),
    §3.3 Exercise 21 on printed p. 259, and against the exercise's cone hypothesis, which the
    $X=\ZZ\times\RR$ counterexample is used to show fails. Not claimed: a published solution of the
    bracketed question, which is still absent.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    #123 transcription batch: every step now names its source with the numbered statement and the
    printed page, and each of the six sources the batch lists was read at that place in its text
    version. Stanford Math 215C, Spring 2009, *Solution Set 4*, Hatcher 3.3.21, printed p. 1
    (`tmp/sources/stanford-math215c-spring2009-solution4.md`): steps excision-limit and cone-case
    transcribe it, and the rectangle computation of step compact-degree-two is its closing
    paragraph. C. Kottke, *Math 2420 Problem Set 3 solutions*, Problem 2, printed p. 2
    (`tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.md`): the second complete solution of
    the first part. Frankland, Theorem 1.3 with the sentence after it on printed p. 2 and
    Theorem 2.1 on printed p. 3 (`tmp/sources/frankland-2017-cohomology-hawaiian-earring.md`), the
    two pages confirmed against `tmp/sources/frankland-2017-cohomology-hawaiian-earring.pdf`.
    Eda--Kawamura, Theorem 3.1 on printed p. 307 with the proof on printed p. 310
    (`tmp/sources/eda-kawamura-hawaiian-earring-2000.md`), where the statement's $\kappa$ is
    $\abs{I^{\NN}}$ and so the continuum for $I=\NN$. Wiegold, printed pp. 341--342
    (`tmp/sources/wiegold-ext-q-z-1969.md`), where the last paragraph of the note concludes that
    $\operatorname{Ext}(\QQ,\ZZ)$ has the cardinal of the continuum, is torsion-free and
    divisible, hence is the additive group of $\RR$. Math Stack Exchange answer 4391062
    (Thorgott, 2022-02-25) to question 4390308
    (`tmp/sources/mse-4390308-cech-cohomology-manifold-complement-hatcher-3321.md`) for the pair
    sequence at a one-point subspace, and the accepted answer 4224683 (Eric Wofsey, 2021-08-14) to
    question 4224576 (`tmp/sources/mse-4224576-hatcher-3321-what-is-a-cone.md`) for the
    identification of the compactification with the Hawaiian earring and for the absence of a cone
    neighbourhood there. Two corrections to the body's own citations: it said that Eda--Kawamura,
    Wiegold, Stanford *Solution Set 4* and Kottke have no text version in `tmp/sources` and were
    read from PDF text layers; all four have a `.md` text version beside the PDF, and the body now
    names it. The bracketed question still has no published solution — none of these six sources
    treats it, the Stanford set's own paragraph on $\ZZ\times\RR$ being the rejected one, and
    answer 4224683 settling only that the cone hypothesis fails — and `COMPLAINTS.md` carries a
    record of this date naming it. Checked against Hatcher (2002), §3.3 Exercise 21 on printed
    p. 259, in `tmp/sources/hatcher-2002-algebraic-topology.md` and at PDF page 268 of
    `tmp/sources/hatcher-2002-algebraic-topology.pdf`, which carries that exercise. Not claimed: a
    published solution of the bracketed question.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report on this round: four repairs, and the rendered solution now carries
    citations and mathematics only. (1) The degree-two step said the rectangle count's "vanishing in
    the other degrees" is the source's. It is not: Stanford *Solution Set 4*, printed p. 1, computes
    $H^1(X,X\setminus K_N)=\ZZ^{2N+1}$ and says nothing about degree two or any other degree, and
    the $H_c^2=0$ the counterexample needs is the card's own; the step now says the argument is the
    card's and cites the rectangle family alone. (2) Answer 4391062 to question 4390308 was cited
    for the identification $H^n(E,\infty)=H^n(E)$ and used at $n=2$. What that answer states for
    singular cohomology is $H^1(X,S)\cong H^1(X)$ for a singleton $S$, from the long exact sequence
    of the pair; its general paragraph is about \v{C}ech cohomology of nerves. The citation is now
    confined to degree one, where the card also had it, and the degree-two identification is given
    as the card's own long-exact-sequence argument at the pair $(E,\infty)$. (3) The final
    step's opening, "the card's assembly of three published theorems and is not a transcription of
    any published treatment of the question", and its closing about "the previously rejected
    countability argument", are out of the rendered text; the step keeps its mathematics, opens with
    the marker that the argument is the card's own, and cites the three theorems by statement and
    printed page. (4) The four closing paragraphs of bookkeeping are gone from the rendered solution:
    the served URL with the byte count and sha256, the summary of the Stanford argument already
    transcribed in the steps, "Which part is published and which is not", and the list of text
    versions. What is kept is mathematics: Kottke's second route with its construction, his slip
    $H^n(X,V)$ named with the group meant, and the Stanford paragraph on $\ZZ\times\RR$ named as an
    inference that does not hold, with Specker's theorem as the reason. Where and how the sources
    were read this pass: `tmp/sources/stanford-math215c-spring2009-solution4.md`, whose 3.3.21 block
    is its page 1 (the `.md` marks the PDF's page ranges, not the set's folios, and the set prints
    none); `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.md`, where Problem 2 opens on its
    page 2; `tmp/sources/frankland-2017-cohomology-hawaiian-earring.md`, Theorem 1.3 with the
    sentence after it on its page 2 and Theorem 2.1 on its page 3, both confirmed on pages 2 and 3
    of `tmp/sources/frankland-2017-cohomology-hawaiian-earring.pdf`, which carry their own folios;
    `tmp/sources/eda-kawamura-hawaiian-earring-2000.md`, Theorem 3.1 stated on printed p. 307 and
    proved on printed p. 310 (PDF pages 3 and 6); `tmp/sources/wiegold-ext-q-z-1969.md`, printed
    pp. 341--342; `tmp/sources/mse-4224576-hatcher-3321-what-is-a-cone.md` and
    `tmp/sources/mse-4390308-cech-cohomology-manifold-complement-hatcher-3321.md`, the two threads'
    text versions, from which the answer bodies were read in full. Frankland's note computes
    $H^1$ and reviews $H_1$ but says nothing about $H^2$, so it is not a source for the degree-two
    nonvanishing; neither solution set treats the bracketed question. The bracketed question has no
    published solution in what was read, and `COMPLAINTS.md` records that on this date.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report on this round: the citation this day's event says is "confined to degree
    one" was not on the card at all. Commit 60cb0e4c52 removed the sentence that cited answer 4391062
    from step `degree-one` as well as the one that cited it in degree two, so the rendered body named
    it nowhere, and the event's parenthetical "where the card also had it" was false of the text
    committed. Answer 4391062 (Thorgott, 2022-02-25) to Math Stack Exchange question 4390308, read in
    `tmp/sources/mse-4390308-cech-cohomology-manifold-complement-hatcher-3321.md`, states for
    singular cohomology that $H^1(X,S)\cong H^1(X)$ for a singleton $S$, from the exact sequence of
    the pair $(X,S)$, which is exactly the identification step `degree-one` uses at $(E,\infty)$;
    the step cites it there again, and only there, so the citation is confined to degree one as the
    event said it would be. The degree-two identification stays the card's own long-exact-sequence
    argument, which is what that event required, and the answer's general paragraph on \v{C}ech
    cohomology of nerves is not used. Also read for this event: the step's opening, which said the
    whole argument was the card's, now says that the comparison of the two values is, the pair
    sequence being the answer's statement. Not checked in this pass: the answer was read in the API's
    text of question 4390308 and not at the site; `COMPLAINTS.md` carries the correction in a new
    record of this date, and no dated record is edited in place.

- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule applied to step #cone-case, whose proof said "those two pages"
    without naming them: it is now cited to Stanford Math 215C, Spring 2009, Solution Set 4,
    Hatcher 3.3.21, printed p. 1, and C. Kottke, Math 2420 Problem Set 3 solutions, Problem 2,
    printed p. 2. Checked: both places, and that they are the pages the two arguments are on.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165: the two events of 2026-11-07 that disagree about Hatcher's
    bracketed question are reconciled here, in a new event; neither is
    rewritten. The first, whose note reads "DEFERRED, recorded not dropped: the
    printed bracketed question for X = ZZ x RR is not answered ... whether the
    isomorphism still holds is open on this card", states the status before the
    degree-two counterexample and is superseded by the events of the same day
    that give it. The card now answers the question, negatively, and no
    rendered sentence says it is open. The second, whose note reads "The
    bracketed question is now answered from Stanford Math 215C Solution Set 4",
    is the withdrawn one: the next event of that day ("Withdraws the incorrect
    counterexample and its audit claim") says why, a surjection
    H_1(X^+) -> prod_N Z dualising to an injection and Hom(prod_N Z, Z) being
    the countable direct sum by Specker's theorem, so the Stanford paragraph
    establishes nothing about the question and is not used. What the card
    proves, and all that it claims, is the negative answer in degree two with
    G = Z: H_c^2(Z x R; Z) = 0 from the cofinal rectangles in step
    compact-degree-two, against H^2((Z x R)^+, infinity; Z) != 0 in step
    earring-degree-two through Ext_Z(Q, Z) = R and the Q direct summand of the
    H_1 of the earring, the two values assembled in the closing step. The
    bracketed question has no published solution in anything read, which is
    what the last paragraphs of the card say. Checked in this pass: Hatcher,
    section 3.3 Exercise 21 on printed p. 259 (PDF p. 268), with its cone
    hypothesis; the first part's transcription against Stanford Math 215C,
    Spring 2009, Solution Set 4, printed p. 1, and C. Kottke, Math 2420 Problem
    Set 3 solutions, Problem 2, printed p. 2; and the two computations above
    with the pair sequence at (E, infinity). Not checked in this pass: the
    Eda--Kawamura and Wiegold papers were not re-read, and no source outside
    those already named on the card was searched for the bracketed question.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, the correctness read of this card's own part, which is the answer to the bracketed
    question. No defect found. Checked in the first part: $H_c^n(X;G)$ is the direct limit of
    $H^n(X,X\setminus K;G)$ over compact $K$; excision of the point $\infty$, whose closure lies in
    the interior of $U_K=X^+\setminus K$, gives $H^n(X^+,U_K)\cong H^n(X,X\setminus K)$; the sets
    $U_K$ are cofinal among the neighbourhoods of $\infty$; inside a cone neighbourhood, the
    subcones are cofinal and radial scaling contracts each to the cone point, so the restriction
    $H^n(X^+,U)\cong H^n(X^+,\infty)$ for those $U$, and the isomorphisms are compatible with
    shrinking. Checked in step `compact-degree-two`: on $K_N$ the pair $(X,X\setminus K_N)$ splits
    over the lines, the $2N+1$ lines meeting $K_N$ contribute $H^q(\RR,\RR\setminus J_N)$, which is
    $\ZZ$ for $q=1$ and zero otherwise, and every other line contributes a pair of equal spaces; so
    $H^q=\ZZ^{2N+1}$ for $q=1$ and $0$ for $q\neq1$, and the direct limit vanishes in degree two.
    Checked in step `earring-degree-two`: the one-point compactification of $\ZZ\times\RR$ is the
    Hawaiian earring, since a neighbourhood of $\infty$ contains all but finitely many whole lines
    and each line closes up to a circle through $\infty$; the pair sequence gives
    $H^2(E,\infty)\cong H^2(E)$ because $H^1(\{\infty\})=H^2(\{\infty\})=0$; universal coefficients
    gives an injection $\operatorname{Ext}(H_1(E),\ZZ)\hookrightarrow H^2(E)$; and with
    $H_1(E)\cong\prod^\sigma_I\ZZ\oplus\prod_pA_p\oplus\bigoplus_\kappa\QQ$, read at
    Eda--Kawamura's Theorem 3.1 statement with $\kappa=\abs{I^{\NN}}$ the continuum, together with
    $\operatorname{Ext}(\QQ,\ZZ)\cong\RR$ from Wiegold, the target is nonzero. Checked in step
    `degree-one`: both sides are the free abelian group on countably many generators, the left from
    the same rectangle family, the right from Frankland's Theorem 1.3, so degree one does not decide
    the question — the point the rejected Stanford paragraph missed. Not claimed: a published
    solution of the bracketed question; the reading here is of the card's own assembly from those
    three theorems.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, referee read of this card's own part, the answer to the bracketed question. Checked
    that the two sides really separate in degree two. Left: $H_c^2(\ZZ\times\RR;\ZZ)$ is the direct
    limit of $H^2(X,X\setminus K)$ over compact $K$; the rectangles $K_N$ are cofinal and
    $X\setminus K_N$ meets every line, so the pair splits over the lines and only the $2N+1$ lines
    meeting $K_N$ contribute, each by $H^q(\RR,\RR\setminus J_N)$, which is $\ZZ$ at $q=1$ and $0$
    at $q=0,2$ because $\RR$ is connected and contractible; every stage of the degree-two limit is
    therefore $0$, not merely eventually $0$. Right: $X^+$ is the Hawaiian earring, since a
    neighbourhood of $\infty$ contains all but finitely many whole lines and each line closes up to a
    circle through $\infty$; in the pair sequence of $(E,\infty)$ the terms $H^q(\{\infty\})$
    vanish for $q\ge1$, so $H^2(E,\infty)\to H^2(E)$ is injective and, the next term being
    $H^2(\{\infty\})=0$, also surjective; universal coefficients injects
    $\operatorname{Ext}(H_1(E;\ZZ),\ZZ)$ into $H^2(E;\ZZ)$; and if $H_1(E)\cong\QQ\oplus K$, which is
    what Eda--Kawamura's Theorem 3.1, printed p. 307, gives with the $\kappa=\abs{I^{\NN}}$ terms
    $\QQ$, then $\operatorname{Ext}(H_1(E),\ZZ)\cong\operatorname{Ext}(\QQ,\ZZ)\oplus
    \operatorname{Ext}(K,\ZZ)$, and $\operatorname{Ext}(\QQ,\ZZ)\cong\RR\ne0$ by Wiegold, printed
    pp. 341--342. So the two groups differ and the evident map is not an isomorphism: the answer to
    the bracketed question is no. Checked that this is the degree in which the card claims it and
    that nothing is claimed in degree one, where both sides are free on countably many generators
    (Frankland, Theorem 1.3, printed p. 2, for the right-hand side) and the card says only that the
    question cannot be decided there. Not claimed: a published solution of the bracketed question.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165, reader's report on the card: four rendered sentences are corrected and the earlier
    notes this supersedes are named. (1) Step cone-case's proof said the Stanford set "reads
    H~^m(U_K;G)=0 from the exact sequence of the pair (X^+,U_K)"; the vanishing is that U_K is a
    cone and hence contractible, and the exact sequence is what converts it into the isomorphism.
    (2) The same proof said a smaller cone-shaped neighbourhood contracts to the cone point "by
    radial scaling", which is false: a neighbourhood of the cone point need not contain the image of
    any uniform scaling, the cone on a countable discrete set with shrinking radii being a
    counterexample; the sentence now reparametrizes each ray by an interval chosen inside the
    neighbourhood, which gives a subspace homeomorphic to the cone and contracting along the rays.
    The event of this date added under issue #170, whose note reads "the subcones are cofinal and
    radial scaling contracts each to the cone point", endorses the sentence corrected here. (3) The
    closing paragraph's "as step degree-one computes directly" is replaced by the citation the claim
    needs, Frankland, Theorem 1.2 (Specker's theorem), printed p. 2; step degree-one computes
    H^1(E), not Hom(prod_N Z, Z). (4) Step degree-one's claim said the two groups "are both free
    abelian on countably many generators, so degree one does not separate the two sides", which
    overclaims: abstract isomorphism is not an isomorphism of the evident map. It and the closing
    step now say that no invariant of the two groups as abstract groups can decide the question in
    degree one, and that nothing asserts the degree-one map fails. (5) Earlier notes the card no
    longer holds, named with their text: the 2026-11-07 event whose note says "The definite answer
    to Hatcher's bracketed question ... remains deferred" states a status the card left behind when
    it answered the question in degree two, and is superseded as the first deferral was; the
    2026-11-14 event saying "The card's closing paragraph now also says which part of the exercise
    is published ... and which is not" describes a paragraph removed on 2026-11-16; the 2026-11-16
    event saying answer 4224683 "shows only that infinity has no cone neighbourhood ... which is not
    the question" is false of the answer, which also identifies the compactification with the
    Hawaiian earring, as the rendered step uses it; the event saying Eda--Kawamura, Wiegold,
    Stanford Solution Set 4 and Kottke "have no text version in tmp/sources" is false, all four
    having a .md beside the PDF; the event saying the Stanford and Kottke transcriptions "are
    unchanged" was overtaken by the 2026-11-18 change to cone-case and by this one; and the event
    saying "every step now names its source with the numbered statement and the printed page" is
    inexact, three of the six steps citing a paragraph of a set that has no numbered statements.
    (6) The event of this date above whose note says "The bracketed question has no published
    solution in anything read, which is what the last paragraphs of the card say" attributes to the
    rendered text something it does not carry: the card's last paragraphs record what the Stanford
    paragraph gets wrong and that the question is settled, and the statement that no published
    solution exists is this audit trail's and COMPLAINTS', not the page's. Checked in this pass:
    Hatcher, section 3.3 Exercise 21 on printed p. 259 (PDF 268); the cone on a countable discrete
    set as the counterexample to uniform radial scaling; Stanford, printed p. 1, and Kottke,
    Problem 2, printed p. 2; Frankland's Theorems 1.2 and 1.3, printed p. 2. Not checked: the
    Eda--Kawamura and Wiegold papers were not re-read.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165, the item the last report left unverified: the two papers the
    degree-two counterexample rests on were read at the pages the card cites.
    Eda--Kawamura, Theorem 3.1, printed p. 307, states that for an index set I
    of infinite cardinality and kappa = |I^N|, H_1(H_I) is isomorphic to
    prod^sigma_I Z + prod_{p prime} A_p + direct-sum_kappa Q, where A_p is the
    p-adic completion of direct-sum_kappa J_p; for I = N, kappa is the
    continuum, so the direct-sum_kappa Q is the Q direct summand the step uses.
    The proof is on printed p. 310 ("Proof of Theorem 3.1"), where Ker(sigma) is
    a direct summand isomorphic to p-part plus direct-sum_kappa Q by Lemma 3.4
    ("The maximal divisible subgroup of Ker(sigma) is isomorphic to
    direct-sum_kappa Q"). Wiegold, printed pp. 341--342: the title is the
    result, and the last paragraph concludes that Ext(Q,Z) is torsion-free and
    divisible of the cardinal of the continuum, hence isomorphic to the
    additive group of R; the conclusion stands on printed p. 342. Both are as
    the card says, so the degree-two step's two citations are confirmed at their
    printed pages and nothing on the card changes. Not checked: the rest of
    either paper, and no other source bearing on the bracketed question was
    searched this pass.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165, the second item the last report left open: a further search for
    a published solution of Hatcher's bracketed question, the answer to which
    the card gives in degree two. Searched were Ceramic for the exercise's own
    wording and Linkup for the exercise and its Z x R question; the hits were
    Stanford Math 215C, Spring 2009, Solution Set 4 (printed p. 1, already
    transcribed at steps excision-limit and cone-case and rejected in its
    Z x R paragraph), Math Stack Exchange 4224576 (the cone failure, already
    recorded) and 4812778 (the exercise, no answers), and Hatcher's errata
    page. No new source and no published solution of the bracketed question was
    located, so nothing on the card changes and the statement that no published
    solution exists stands. Not done: the Scribd compilations returned by the
    same search were not readable, and no print or library source was
    consulted.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Locator repair, no mathematics: the live text cites each source by its numbered statement alone. The
    cofinal rectangles are those of Stanford *Solution Set 4*; the rational summand of $H_1(E;\ZZ)$ is K. Eda
    and K. Kawamura, *The Singular Homology of the Hawaiian Earring*, Theorem 3.1; $\Ext_\ZZ(\QQ,\ZZ)\cong\RR$
    is James Wiegold, *Ext(Q,Z) is the additive group of real numbers*; and the degree-one value and the same
    summand are Martin Frankland, *Cohomology of the Hawaiian Earring* (2017), Theorem 2.1 and Theorem 1.3
    with the sentence after it. Every page reference is gone from the problem, the steps and the remarks —
    including the two inside the bolded attributions, which now end at the theorem number. The split the card
    draws between published theorems and its own assembly is unchanged, and no step changed. The dated events
    above keep their text, page references included, as QUAL-11 requires. `qualc.authoring check` passes.

- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Issue #165, the residual sentence of step degree-one: it closed "no argument in
    degree one can decide the bracketed question", which claims more than the two
    computations above it give. They give that $H_c^1(\ZZ\times\RR;\ZZ)$ and
    $H^1(E,\infty;\ZZ)$ are both free abelian on countably many generators, hence
    abstractly isomorphic, so no invariant of the two groups as abstract groups, and
    in particular no countability argument, decides whether the evident map is an
    isomorphism; an argument that computes the map itself is not excluded by them.
    The sentence now says that and nothing more, and agrees with the claim of the
    step, with step earring-degree-two's degree-two comparison, and with the closing
    step's "nothing here asserts that the degree-one map fails". Checked in this
    pass: the degree-one value of the compactification from Frankland, Theorem 1.3
    with the sentence after it, and from the exact sequence of the pair
    $(E,\infty)$; the compactly supported value from the cofinal rectangles $K_N$.
    Searched the retained sets again for a published solution of the bracketed
    question, without result: Guanyu Li's set covers Ex. 3.3.1 to 3.3.9 of the
    section, Koukpari's has no exercises in it, Stanford Math 215C Solution Set 4
    proves the first part and its paragraph on $\ZZ\times\RR$ is the rejected
    inference, and Kottke's Problem 2 proves the first part. So the answer to the
    bracketed question is the card's own assembly from Eda--Kawamura, Wiegold and
    Frankland, as the closing step says, and no published solution of it was
    located. Not checked in this pass: no source outside those sets was read.

- event: source-corrected
  by: claude
  date: 2026-11-22
  note: >-
    Issue #165, one refinement of the step's claim: it read "no invariant of the two groups as
    abstract groups, and in particular no countability argument, can separate the two sides in
    degree one". What the two computations give is that both groups are free abelian on countably
    many generators, so every invariant of them as abstract groups agrees, their cardinality
    included; "no countability argument" was wider than that, since an argument that counts the
    image of the map is not an invariant of the two groups. The claim now says "no comparison of
    their cardinalities". The proof's closing sentence and the closing step are unchanged.
---

::: {.problem}
For a space $X$, let $X^+$ be the one-point compactification.
If the added point, denoted $\infty$, has a neighborhood in $X^+$ that is a cone with $\infty$ the cone point, show that the evident map $H_c^n(X; G) \to H^n(X^+, \infty; G)$ is an isomorphism for all $n$.
[Question: Does this result hold when $X = \ZZ \times \RR$?]
:::

::: {.solution}
Assume that $X$ is locally compact Hausdorff, so that $X^+$ is a compact Hausdorff space with $X$ open in it.

::: pf

::: {.pf-step #excision-limit}
Excision identifies $H_c^n(X;G)$ with the direct limit of $H^n(X^+,U;G)$ over all neighborhoods $U$ of $\infty$.

::: pf-proof
This step is the first paragraph of Stanford Math 215C, Spring 2009, *Solution Set 4*, Hatcher 3.3.21; C. Kottke, *Math 2420 Problem Set 3 solutions*, Spring 2012, Problem 2, reaches the same limit over a cofinal family built the other way round. For a compact $K\subset X$, let $U_K=X^+\setminus K$, an open neighborhood of $\infty$. Excision of the point $\infty$, whose closure lies in the interior of $U_K$, gives
$$
H^n(X^+,U_K;G)\cong H^n(X,X\setminus K;G).
$$
As $K$ ranges over compact subsets of $X$, the neighborhoods $U_K$ are cofinal among the neighborhoods of $\infty$: every neighborhood $U$ of $\infty$ has compact complement $X\setminus U$, and $U_{X\setminus U}\subset U$. Since the direct limit defining $H_c^n(X;G)$ can be taken over this cofinal family,
$$
H_c^n(X;G)\cong\varinjlim_{\infty\in U}H^n(X^+,U;G).
$$
:::

:::

::: {.pf-step #cone-case}
If $\infty$ has a cone neighborhood in $X^+$, then the evident map $H_c^n(X;G)\to H^n(X^+,\infty;G)$ is an isomorphism for all $n$.

::: pf-proof
This is the remainder of the first paragraph of Stanford Math 215C, Spring 2009, *Solution Set 4*, Hatcher 3.3.21, and of C. Kottke, *Math 2420 Problem Set 3 solutions*, Problem 2: the Stanford set restricts to those compact sets whose complement is cone-shaped, notes that they are cofinal among the compact subsets, uses that each $U_K$ is a cone and therefore contractible, so that $\widetilde H^m(U_K;G)=0$ for all $m$, and then reads the isomorphism off the exact sequence of the pair $(X^+,U_K)$; Kottke absorbs each compact $K$ into a compact $L=X\setminus V$ with $V$ a cone neighbourhood of $\infty$ that deformation retracts to $\infty$, which is the cofinality assertion read backwards. Inside the cone neighborhood from the hypothesis, every neighborhood $W$ of the cone point contains a smaller cone-shaped neighborhood: choose on each ray of the cone an interval ending at the cone point and lying in $W$, and reparametrize the ray by that interval, which turns their union with the cone point into a subspace homeomorphic to the cone, contained in $W$, and contracting to the cone point along the rays. These contractible neighborhoods are cofinal among the neighborhoods of $\infty$. For each such $U$, the inclusion $\{\infty\}\hookrightarrow U$ is a homotopy equivalence. The map of long exact sequences for the pairs $(X^+,U)$ and $(X^+,\{\infty\})$ therefore shows that restriction is an isomorphism
$$
H^n(X^+,U;G)\xrightarrow{\cong}H^n(X^+,\infty;G).
$$
These isomorphisms commute with restriction to smaller cone neighborhoods. Taking the direct limit and using step [](#excision-limit){.pf-ref} gives the asserted isomorphism $H_c^n(X;G)\cong H^n(X^+,\infty;G)$.
:::

:::

::: {.pf-step #compact-degree-two}
For $X=\ZZ\times\RR$ and integer coefficients, $H_c^2(X;\ZZ)=0$.

::: pf-proof
The argument of this step is the card's own, on the family of rectangles that Stanford *Solution Set 4* uses as its cofinal compact sets. Let $J_N=[-N-1/2,N+1/2]$ and $K_N=([-N-1/2,N+1/2]^2)\cap X$ for $N\ge1$. These compact rectangles are cofinal among compact subsets of $X$. On each of the $2N+1$ lines meeting $K_N$, the relative cohomology is $H^q(\RR,\RR-J_N;\ZZ)$, which is $\ZZ$ for $q=1$ and zero otherwise. Hence
$$
H^q(X,X-K_N;\ZZ)\cong
\begin{cases}
\ZZ^{2N+1},&q=1,\\
0,&q\ne1.
\end{cases}
$$
In particular, the direct limit in step [](#excision-limit){.pf-ref} vanishes in degree two.
:::

:::

::: {.pf-step #earring-degree-two}
The compactification $E=(\ZZ\times\RR)^+$ has $H^2(E,\infty;\ZZ)\ne0$.

::: pf-proof
That the one-point compactification of $\ZZ\times\RR$ is the Hawaiian earring is answer 4224683 (Eric Wofsey, 2021-08-14) to Math Stack Exchange question 4224576: every neighbourhood of $\infty$ contains all but finitely many of the full lines $\{n\}\times\RR$, and adding $\infty$ turns those into circles. The pair sequence of $(E,\infty)$ then gives $H^2(E,\infty;\ZZ)\cong H^2(E;\ZZ)$, since $H^1(\{\infty\};\ZZ)=H^2(\{\infty\};\ZZ)=0$ and $H^1(E;\ZZ)\to H^1(\{\infty\};\ZZ)=0$ is onto; this is the degree-two case of the argument step [](#degree-one){.pf-ref} gives in degree one. Each line becomes a circle in $E$, with all circles sharing $\infty$, and every neighborhood of $\infty$ contains all but finitely many whole circles. Thus $E$ is the Hawaiian earring. Universal coefficients gives an injection
$$
\operatorname{Ext}_{\ZZ}(H_1(E;\ZZ),\ZZ)\hookrightarrow H^2(E;\ZZ).
$$
By **K. Eda and K. Kawamura, *The Singular Homology of the Hawaiian Earring*, Theorem 3.1**, $H_1(E;\ZZ)$ has a direct summand isomorphic to $\QQ$, the index $\kappa$ of the statement being $\abs{I^{\NN}}$ and so the continuum; the same summand is stated as Theorem 2.1 of **Martin Frankland, *Cohomology of the Hawaiian Earring***. Consequently $\operatorname{Ext}_{\ZZ}(\QQ,\ZZ)$ is a direct summand of the left-hand group above. By **James Wiegold, *Ext(Q,Z) is the additive group of real numbers*, $\operatorname{Ext}_{\ZZ}(\QQ,\ZZ)\cong\RR\ne0$. The target group is therefore nonzero.
:::

:::

::: {.pf-step #degree-one}

For $X=\ZZ\times\RR$ and integer coefficients, $H_c^1(X;\ZZ)$ and $H^1(X^+,\infty;\ZZ)$ are both free abelian on countably many generators, so no invariant of the two groups as abstract groups, and in particular no comparison of their cardinalities, can separate the two sides in degree one.

::: pf-proof

The comparison of the two values is the card's own. Step [](#compact-degree-two){.pf-ref} computes $H^q(X,X\setminus K_N;\ZZ)=\ZZ^{2N+1}$ for $q=1$ and $0$ otherwise, and the family $\{K_N\}$ is cofinal, so the direct limit of step [](#excision-limit){.pf-ref} in degree one is the free abelian group on countably many generators. For the right-hand side, step [](#earring-degree-two){.pf-ref} identifies $X^+$ with the Hawaiian earring $E$, and **Martin Frankland, *Cohomology of the Hawaiian Earring* (2017), Theorem 1.3 with the sentence following it**, gives

$$
H^1(E;\ZZ)\cong\bigoplus_{n\in\NN}\ZZ,
$$

"a free abelian group on countably many generators": the map $H^1(E;\ZZ)\to\operatorname{Hom}_{\ZZ}(\bigoplus_{\NN}\ZZ,\ZZ)$ induced by $H_1(\iota)$ is injective with image $\bigoplus_{\NN}\ZZ$, and $H^1(E;\ZZ)\cong\operatorname{Hom}_{\ZZ}(H_1(E;\ZZ),\ZZ)$ because $H_0(E;\ZZ)$ is free. That the pair sequence of a one-point subspace identifies the relative group with the absolute one is **answer 4391062 (Thorgott, 2022-02-25) to Math Stack Exchange question 4390308**, which states for singular cohomology that $H^1(X,S)\cong H^1(X)$ for a singleton $S$, from the exact sequence of the pair $(X,S)$. The exact sequence of the pair $(E,\infty)$ then gives $H^1(E,\infty;\ZZ)\cong H^1(E;\ZZ)$: the map $H^0(E;\ZZ)=\ZZ\to H^0(\{\infty\};\ZZ)=\ZZ$ is onto, so the image of $H^0(\{\infty\};\ZZ)$ in $H^1(E,\infty;\ZZ)$ is $H^0(\{\infty\};\ZZ)$ modulo the image of $H^0(E;\ZZ)$, which is zero, and $H^1(E,\infty;\ZZ)\to H^1(E;\ZZ)$ is injective by exactness; while $H^1(\{\infty\};\ZZ)=0$ makes it surjective. The tail of that sequence is thus the short exact sequence $0\to H^1(E,\infty;\ZZ)\to H^1(E;\ZZ)\to0$. Both groups are thus free abelian on countably many generators, so no invariant of theirs as abstract groups decides the bracketed question in degree one.

:::

:::

::: pf-step
The answer to the bracketed question is no, already for $G=\ZZ$ and $n=2$.

::: pf-proof
The argument of this step is the card's own, on three published theorems: **K. Eda and K. Kawamura, *The Singular Homology of the Hawaiian Earring*, Theorem 3.1**, for the $\QQ$ direct summand of $H_1(E;\ZZ)$; **James Wiegold, *Ext(Q,Z) is the additive group of real numbers***, for $\operatorname{Ext}_{\ZZ}(\QQ,\ZZ)\cong\RR$; and **Martin Frankland, *Cohomology of the Hawaiian Earring* (2017), Theorem 2.1 and Theorem 1.3 with the sentence after it**, for the same summand and for the degree-one value. Steps [](#compact-degree-two){.pf-ref} and [](#earring-degree-two){.pf-ref} give
$$
\boxed{H_c^2(\ZZ\times\RR;\ZZ)=0,\qquad H^2((\ZZ\times\RR)^+,\infty;\ZZ)\ne0,}
$$
so the evident map cannot be an isomorphism, and the cone-neighborhood hypothesis of step [](#cone-case){.pf-ref} cannot hold for $\ZZ\times\RR$. The separation is in degree two; step [](#degree-one){.pf-ref} shows only that the two groups in degree one are abstractly isomorphic, and nothing here asserts that the degree-one map fails.
:::

:::

:::

A second route to the first part, which absorbs each compact set into a larger one instead of using the vanishing of $\widetilde H^m(U_K;G)$, is Kottke's, Problem 2. Let $K\subset X$ be compact. Since $X^+$ is Hausdorff there are disjoint open sets $U\supset K$ and $V\ni\infty$; shrinking $V$ inside the cone-shaped neighbourhood of the hypothesis, one may assume that $V$ deformation retracts to $\infty$. Put $L=X\setminus V$. Then $L$ is compact and $K\subset L$, and since $X\setminus L=V\setminus\{\infty\}$,
$$
H^n(X,X\setminus L)=H^n(X,V\setminus\{\infty\})\cong H^n(X^+,V)\cong H^n(X^+,\infty),
$$
the first group by the identity just written, the middle isomorphism by excision of the point $\infty$ — closed in $X^+$ and contained in the open set $V$, so that its closure lies in the interior of $V$ — and the last by the deformation retraction of $V$ onto $\infty$. The $L$ so obtained are cofinal among the compact subsets of $X$, so the direct limit over them is $H_c^n(X;G)$, and the isomorphisms are compatible with inclusions, which is the theorem. Kottke writes the middle group as $H^n(X,V)$, where $V$ is an open set of $X^+$ containing $\infty$ and so is not a subspace of $X$; the excision removes $\infty$ from it, and the group meant is the one written above.

Stanford's closing paragraph on $X=\ZZ\times\RR$ concludes that $H^1$ of the compactification is uncountable from a surjection $H_1\twoheadrightarrow\prod_\NN\ZZ$. That inference does not hold: dualizing a surjection gives an injection, and $\operatorname{Hom}(\prod_\NN\ZZ,\ZZ)\cong\bigoplus_\NN\ZZ$ is countable by Specker's theorem, stated as Theorem 1.2 of Frankland, *Cohomology of the Hawaiian Earring*. The bracketed question is settled above, in degree two with $G=\ZZ$.

:::
