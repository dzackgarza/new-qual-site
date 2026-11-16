---
schema: qual/card@1
id: E-HAT-3.B-4
kind: problem
title: "Cross product of fundamental classes"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.B, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.B, Exercise 4; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.B Exercise 4, printed p. 280; the statement
    matches the print. The gap was the last step: the card asserted that "the cross product of the
    two standard local generators is the standard generator in dimension $m+n$; this follows directly
    from the relative Künneth theorem, or from the product orientation on Euclidean space", which is
    exactly the content. It is now computed over $\ZZ$ from the relative Künneth formula printed on
    p. 276 applied to the CW pairs $(D^m,S^{m-1})$ and $(D^n,S^{n-1})$, where only one group on the
    left survives and no Tor term occurs, so the cross product is an isomorphism $\ZZ\otimes\ZZ\to\ZZ$
    on the top group; the passage to an arbitrary coefficient ring $R$ is by naturality in the
    coefficients, not by a second Künneth argument. Also supplied: the definition of fundamental class
    and the existence of $[M]$ for closed $R$-orientable $M$ from Theorem 3.26(a) (p. 236), the
    equality $(M-x)\times N\cup M\times(N-y)=M\times N-\{(x,y)\}$, the excision hypotheses for the
    inclusion of $(B_x\times B_y,B_x\times B_y-\{(x,y)\})$ into $(M\times N,M\times N-\{(x,y)\})$ with
    the excised closed set named, and the role of the charts $u,v$ in making $\iota_m\otimes\iota_n$
    correspond to $[M]_x\otimes[N]_y$. No published solution of this exercise is in the retained
    sets — Sam has no §3.B, Stanford 215C solution2 covers §3.B exercises 1 and 3 only, Li stops at
    §3.3, the Math 538 sheets are §3.3 only — recorded in COMPLAINTS.md.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Re-read the printed statement for #123: the exercise is Exercise 4 of §3.B on printed p. 280,
    identical in the current online text, and the card states it word for word. The obligation that
    #123 records is unchanged and stays open: no published solution of this exercise was located.
    Searched without result in the retained sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C
    Solution Sets 1--5, the UCR Math 205B help file, May, Bredon, Maxim's Math 752 notes) and in
    Hatcher's text and errata; the Math 538 set held here is a scan with no text layer and opens at
    §3.2 (Borsuk--Ulam), not at §3.B.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    The published solution of the exercise has now been located and read: C. Kottke, *Math 2420
    Problem Set 3 solutions* (Brown University, Spring 2012),
    `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.pdf`, 3 pp., sha256
    e84fd60496037db45bb18457b7c922233f5912a41b5d067112ba75a8211c22a7, Problem 1, printed p. 1. Its
    Problem 1 states both that $M$ and $N$ are orientable if and only if $M\times N$ is and that
    $\alpha\times\beta$ is a fundamental class when $\alpha,\beta$ are, and proves them: the local
    cross product $H_m(M|x)\otimes H_n(N|y)\to H_{m+n}(M\times N|x\times y)$ is an isomorphism by the
    relative Künneth theorem, for $R=\ZZ$ at a point and after replacing points by closed balls; the
    product of orientations is an orientation of $M\times N$; and for closed manifolds the Künneth
    formula for $M\times N$ leaves $H_m(M)\otimes H_n(N)$. So this is a complete published solution
    of Exercise 4 of §3.B, printed p. 280, which is the second of its two statements. Checked against
    Hatcher: the printed statement on p. 280, the definition of fundamental class and Theorem 3.26(a)
    on p. 236, the relative Künneth statement on p. 276, the relative singular chains' freeness on
    p. 261, the universal coefficient theorem for homology on p. 264, the topological Künneth theorem
    on p. 275 and Corollary A.12 on p. 529. This supersedes the preceding note's closing sentence,
    which said no published solution was in the retained sets; it was not, and the owner supplied it.
- event: solution-written
  by: claude
  date: 2026-11-13
  note: >-
    The solution is now the transcription of that published solution, with the page cited in the
    opening sentence of the solution as well as here. Written out from the source: the local cross
    product and the identity of complements, the integral case at a point by the relative Künneth
    formula on the ball pairs, the multiplication of orientations with the compatibility condition
    carried by products of closed balls, the integral computation $H_{m+n}(M\times N)\cong
    H_m(M)\otimes H_n(N)$ for closed manifolds, and the two routes the source gives to the
    fundamental class, of which the second --- $(\alpha\times\beta)_{(x,y)}=\alpha_x\times\beta_y$
    together with Hatcher's local definition on p. 236 --- is the one used to conclude. Filled, since
    the source leaves it to one sentence: the passage from $R=\ZZ$ to an arbitrary commutative ring,
    done on the card from Theorem 3A.3 (printed p. 264) applied to the free complex $C_*(M,M-x)$,
    which gives $H_m(M|x;R)\cong\ZZ\otimes_\ZZ R$ with the generator $\zeta_x\otimes1$, together with
    Proposition 3B.1 and the tensor identification used on p. 276 for the coefficient change. The
    earlier proof is replaced, not kept alongside: it reached the same conclusion through charts and
    excision of the pair $(M\times N,M\times N-\{(x,y)\})$, and its ring step, on the ball pair, was
    the same argument as the fill made here. Not rewritten into `pf` steps; the source's paragraph
    order is kept so the transcription can be checked against p. 1.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The source's length is 5 pp., not the 3 pp. of the 2026-11-13 note: `pdfinfo` reports 5 pages and
    the set's own footers number its pages 1--5, Problem 1 on printed p. 1, Problem 2 (Hatcher 3.3.21)
    on printed p. 2, Problem 3 on printed p. 3 and exercises from M&T on pp. 2--3. Problem 1, the
    transcription on this card, is on printed p. 1 as stated, and the sha256 in that note matches the
    bytes. Read again at printed p. 1 this pass, with the Hatcher pages the card cites checked against
    the book: Exercise 4 of §3.B on printed p. 280, Theorem 3B.6 on printed p. 275, the relative
    Künneth formula on printed p. 276, Theorem 3.26(a) on printed p. 236, the freeness of $C_*(X,X-x)$
    on printed p. 261, Theorem 3A.3 on printed p. 264, Proposition 3B.1 on printed p. 269, and
    Corollary A.12 on printed p. 529. Hatcher's errata carries no entry bearing on any of these: its
    §3.B entries are pp. 268, 272, 273, 274, 275, 276 (a numbering note about a Corollary 3B.2, absorbed
    in later versions) and 280 (the line before the exercises, and Exercise 5). Nothing in the card's
    proof changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Four defects of this card repaired, three of them in what earlier notes here called the statement
    and the citations. (1) The printed statement was not word for word: from the card's creation until
    this pass the `problem` block rendered Hatcher's coefficient ring as $\RR$ --- bold R, the real
    numbers --- in "closed $\RR$-orientable manifolds", where the book prints $R$. The statement now
    reads $R$-orientable, as Exercise 4 of §3.B on printed p. 280 has it, read in
    `tmp/sources/hatcher-2002-algebraic-topology.md`. The "matches the print word for word" claims of
    the 2026-10-31 and both 2026-11-13 notes were therefore false of the statement as it then stood,
    and they are true only after this correction. (2) The note of 2026-11-16 said Kottke's set
    contains "exercises from M&T on pp. 2--3". It does not: the set is Problems 1, 2 and 3 only, on
    printed pp. 1, 2 and 3, respectively Hatcher 3.B.4, 3.3.21 and 3.B.3. The M&T exercises named in
    that claim, 8.2, 8.5, 8.6 and 9.1, are in Stanford Math 215C Solution Set 4, printed pp. 2--3, not
    in Kottke. (3) The errata sentence of the same note was incomplete: Hatcher's errata also carries
    entries for printed p. 236 (§3.3, "for B any open ball in $M$" to "in $M$ containing $x$"), p. 264
    (§3.A, $\ker i_{n-1}$ to $\ker(i_{n-1}\otimes 1)$ in the proof of Theorem 3A.3) and p. 529
    (Appendix, a cross-reference before Corollary A.12 and a revision note after it), as well as the
    §3.B entries it listed. None of them changes a statement the card cites: the definition of a
    fundamental class on p. 236, Theorem 3A.3 on p. 264 and Corollary A.12 on p. 529 read as the card
    uses them. (4) Two uses of a global computation assumed connectedness without saying so. Theorem
    3.26(a) on printed p. 236 is stated for a closed *connected* manifold, so it gives the isomorphism
    $H_{m+n}(M\times N;R)\to H_{m+n}(M\times N\,||\,(x,y);R)$ only for connected $M$ and $N$; and
    $H_{m+n}(M\times N;\ZZ)\cong\ZZ$ needs $M$ and $N$ connected as well as $\ZZ$-orientable, an
    $R$-orientable manifold with $R=\ZZ/2$ such as $\RP^2$ having $H_2(\RP^2;\ZZ)=0$
    and so no $\ZZ$ fundamental class. The card now states both hypotheses where they are used, and
    states the componentwise argument by which the exercise's conclusion holds without them, which is
    also the reason the exercise is printed with no connectedness hypothesis. Nothing is weakened: the
    conclusion for the exercise as printed is unchanged, and the two paragraphs that need the extra
    hypothesis are marked as the source's second route, not as steps of the proof. Text versions:
    Hatcher is cited from `tmp/sources/hatcher-2002-algebraic-topology.md`, and Kottke from the text
    layer of `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.pdf`, which has no `.md` version in
    `tmp/sources`. Not verified: nothing on this card was read from a rendered page.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Markup only, no change of statement or proof. Hatcher's local group was written `M\,||\,x` on this
    card, which is not what the book prints --- p. 234 and p. 236 print `H_n(M|x;R)`, a single bar ---
    and is a raw bar in mathematics, which STYLE-04 forbids and the shared pre-commit hook rejects for
    a changed card. It is now written with the vocabulary macro, $H_n(M\mid x;R)$, which is also how
    $E-HAT-3.3-15$ writes the same symbol. All ten raw-bar spans of the card are converted, and the
    sentence calling `M\,||\,x` Hatcher's notation is now true of $M\mid x$. Checked with
    `tools/qualc/authoring.py`'s `raw_notation`, which reports no remaining raw form on this card, and
    with `qualc.authoring check`.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass on this card. Six repairs. (1) This event stands after restoring
    the `source-corrected` event of this date that commit 58a42f4703 pushed: commit eb71d67906 rewrote
    that pushed event in place with no event of its own, and its text is restored here verbatim, its
    sentences "respectively Hatcher 3.B.4, 3.3.21 and 3.B.3" included. Those three words are the one
    false statement in the restored text: §3.B of the book stops at Exercise 5, printed p. 280, and
    Kottke's Problem 3 is the cap and cross product formula, not a Hatcher exercise. (2) The note of
    this date said "the hyphen joining the book's R orientable is the card's". It is not: printed
    p. 280 prints **R-orientable**, with the hyphen, which the text extraction drops because the hyphen
    is a separate glyph. Checked by rendering PDF page 289 of
    `tmp/sources/hatcher-2002-algebraic-topology.pdf` --- printed p. 280, Hatcher's printed pages being
    nine fewer than the PDF's --- at 400 dpi: the line reads "closed R-orientable mani-". So the
    statement matches the print including the hyphen, and the claim that it differs there is
    withdrawn. (3) Kottke's Problem 3 runs over printed **pp. 3--5**, not p. 3: the PDF's page breaks
    place its opening on printed p. 3 and its last lines on p. 5, which is the set's last page. (4) The
    errata list in the note of this date omitted the entry for printed **p. 234** (§3.3, line 7:
    "neighborhood of A" to "neighborhood of the closure of A"), which bears on a page the card cites for
    the local group; the other entries it lists (pp. 236, 264, 529, and the §3.B entries) stand. The
    card cites p. 234 only for the notation $H_n(M\mid x;R)$, which the correction does not touch. (5)
    The claim that "the two paragraphs that need the extra hypothesis are marked as the source's second
    route" was false of the card: only the paragraph on integral coefficients carried the label. The
    connectedness sentence of the paragraph on multiplying orientations now carries it too, and both say
    that they are not steps of the proof. (6) The sentence "Theorem 3.26(a) is then a consequence of the
    exercise for connected $M\times N$, not a step in it" is false and is replaced: the exercise gives a
    class whose images in the local groups are generators, which is Hatcher's definition of a
    fundamental class on printed p. 236, while Theorem 3.26(a) asserts that for a closed connected
    $R$-orientable manifold the map $H_n(M;R)\to H_n(M\mid x;R)$ is an isomorphism, which nothing on the
    card proves. Also disclosed here: the card identifier `E-HAT-3.3-15` was written in math mode in the
    markup event of this date and is now a code span, and the markup changes commit 039cb8ebb9 made in
    the 2026-11-13 notes of this card are disclosed here, that commit carrying none of its own.
    Unchanged and re-checked: the statement as printed on p. 280, the local cross product, the
    coefficient-ring step, and the coefficientwise argument for disconnected manifolds.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, third pass on this card: the record of the earlier events, not the
    mathematics. Three disclosures. (1) Commit 039cb8ebb9 changed, in place, two mathematics spans of
    the `source-checked` events of 2026-11-13: the span `H_m(M|x)\otimes H_n(N|y)\to H_{m+n}(M\times N|x\times y)`
    became the same span with `\mid` for each bar, and `H_m(M|x;R)\cong\ZZ\otimes_\ZZ R` likewise.
    QUAL-11 forbids rewriting an event dated before the commit, so those events are not restored;
    their original spans are quoted here, in code, and the change is disclosed. (2) Commit eb71d67906
    rewrote the `source-corrected` event of 2026-11-16 that 58a42f4703 had pushed, with no event of
    its own; commit e945aab1c4 rewrote it again. The text now standing is the text e945aab1c4 left,
    not the text of 58a42f4703: it keeps the `\mid` substitution of 039cb8ebb9 in the span
    `H_{m+n}(M\times N\mid(x,y);R)`, and it changed `$E-HAT-3.3-15$` to the code span
    `E-HAT-3.3-15`. The word "verbatim" in that event is therefore withdrawn: what was restored is
    the text as it stood before eb71d67906, not the event 58a42f4703 pushed. (3) The two sentences
    eb71d67906 added and e945aab1c4 removed --- "the hyphen joining the book's 'R orientable' is the
    card's" and "Problem 3, the cap and cross product formula with the cap products of $S^m\times S^n$,
    is not one of Hatcher's §3.B exercises" --- are not in the current text; both were false, and
    their removal is the correction, but the removal was an in-place edit of a dated event and is
    disclosed here rather than presented as a restoration. Nothing in the statement or the proof
    changes: the statement as printed on p. 280, Kottke's Problem 1 on printed p. 1, and the
    five-page length of the set stand as the card has them.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A wording correction to the event immediately above: it says that 039cb8ebb9 changed "two
    mathematics spans of the `source-checked` events of 2026-11-13". The second of the two spans is in
    the `solution-written` event of that date, not in a `source-checked` one; the two events are the
    two dated 2026-11-13 events named in the reader's report, and the substitution and its original
    text are as that event gives them. Nothing else changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, fourth pass on this card: the dated record, and one citation.
    Four dated events are restored to the text they carried at their date, each of which
    a later commit had rewritten in place, and the corrections those restorations make
    necessary are stated here. (1) The `source-checked` and `solution-written` events of
    2026-11-13 are restored to the text they had before commit 039cb8ebb9, with the raw
    `|` of Hatcher's local group as the session of that day wrote it; 039cb8ebb9
    substituted `\mid` in both spans, and the third-pass event of this date recorded the
    substitution instead of undoing it. (2) The `source-corrected` event of 2026-11-16
    that commit 58a42f4703 pushed is restored to that commit's text; eb71d67906 rewrote
    it in place and e945aab1c4 rewrote it again. The second-pass event of this date says
    of that text that it stands "verbatim" with its sentence "respectively Hatcher 3.B.4,
    3.3.21 and 3.B.3" included, and that sentence is now true of the record. The third
    attribution in it is false, and this is its correction: §3.B of the book stops at
    Exercise 5 on printed p. 280, and Kottke's Problem 3 is the cap and cross product
    formula of the set, whose opening line on printed p. 3 carries the set's own update
    about its sign, not a Hatcher exercise. The two sentences eb71d67906 added --- that
    the hyphen of the book's "R-orientable" is the card's, and that Problem 3 is not a
    §3.B exercise --- do not reappear: they were never in the event 58a42f4703 pushed,
    and the first of them is false, printed p. 280 carrying the hyphen. (3) The `Markup
    only` event of 2026-11-16 is restored to the text commit 039cb8ebb9 wrote, with the
    card identifier in math mode as that session wrote it; e945aab1c4 changed it to a
    code span in place. (4) Kottke's set does have a text version, and the card now names
    it in both places where it cites the set: `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.md`,
    whose header reads "PDF pages 1-5", Problem 1 opening on its first page, the same five
    pages as the PDF of that name. The restored 2026-11-16 event says the set "has no
    `.md` version in `tmp/sources`", and the closing citation of the solution said the
    same; the record stands as its session wrote it, and this event and that citation are
    the correction. (5) The audit block is a record, so the style rules are no longer
    applied to it: the raw bars restored in (1) stand as written, and the card's body,
    which keeps the vocabulary macro $H_n(M\mid x;R)$, is still checked. Checked in this
    pass: the text of each restored event against the commit named for it, and the text
    version of Kottke's set, `PDF pages 1-5` and Problem 1 on its opening page. Not
    checked: no page of any source was read from a rendered page in this pass, and
    nothing in the statement or the proof changed.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The event above places Kottke's sign update on printed p. 3, at the opening line of
    Problem 3. That is wrong, and this is its correction: in
    `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.md` the line "Update 3/12:
    There is some sign involved in the cap/cross product formula in problem 3" stands on
    the set's first page, directly under the title "Math 2420 -- Problem Set 3, due Monday
    3/12", and before Problem 1; printed p. 3 begins directly with Problem 3, whose own
    text carries no update. So the update belongs to the set's head on printed p. 1, and
    what the reader's report said of the attribution to Problem 3 is right: Problem 3, on
    printed pp. 3--5, is the cap and cross product formula and is not a Hatcher §3.B
    exercise. The attribution itself, and the reason §3.B stops at Exercise 5 on printed
    p. 280, stand as the event above states them.
---

::: {.problem}
Show that the cross product of fundamental classes for closed $R$-orientable manifolds $M$ and $N$ is a fundamental class for $M \times N$.
:::

::: {.solution}
The proof below is **C. Kottke, *Math 2420 Problem Set 3 solutions*, Brown University, Spring 2012, Problem 1, printed p. 1** (text version `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.md`, extracted from the set's PDF), transcribed. That problem proves two things: that $M$ and $N$ are orientable if and only if $M\times N$ is, and that $\alpha\times\beta$ is a fundamental class for $M\times N$. The exercise here is the second, which is Exercise 4 of §3.B, printed p. 280. The one step the source leaves is its passage from $R=\ZZ$ to an arbitrary commutative ring, made in a single sentence --- "it still holds that the product of generators is a generator (i.e. $\pm1\times1=\pm1$ still holds in (1))" --- and it is filled in *The coefficient ring* below from Hatcher's universal coefficient theorem, printed p. 264.

Let $R$ be a commutative ring with identity, let $M^m$ and $N^n$ be closed $R$-orientable manifolds with fundamental classes $\alpha\in H_m(M;R)$ and $\beta\in H_n(N;R)$, and write $\alpha_x$, $\beta_y$ for their images in the local groups at $x\in M$ and $y\in N$. Write $H_m(M\mid x;R)=H_m(M,M-x;R)$, Hatcher's notation for the local group (printed p. 234).

*The local cross product.* Since
$$
(M-x)\times N\ \cup\ M\times(N-y)=M\times N-\{(x,y)\},
$$
the relative cross product of §3.B (printed p. 276) is a map
$$
\times:\ H_m(M\mid x;R)\otimes_R H_n(N\mid y;R)\longrightarrow H_{m+n}\bigl(M\times N\mid (x,y);R\bigr).
$$

*The integral case at a point.* Take $R=\ZZ$ and excise the charts, so that the local groups are those of the CW pairs $(D^m,S^{m-1})$, $(D^n,S^{n-1})$ and $(D^m\times D^n,\ S^{m-1}\times D^n\cup D^m\times S^{n-1})$, the product pair being reached by radial deformation of $D^m\times D^n-\{0\}$ onto that subcomplex. The relative Künneth theorem (printed p. 276) then gives
$$
H_{m+n}\bigl(D^m\times D^n,\ S^{m-1}\times D^n\cup D^m\times S^{n-1}\bigr)
\cong\bigoplus_{p+q=m+n}H_p(D^m,S^{m-1})\otimes H_q(D^n,S^{n-1})
\ \oplus\!\!\bigoplus_{p+q=m+n-1}\!\!\operatorname{Tor}\bigl(H_p(D^m,S^{m-1}),H_q(D^n,S^{n-1})\bigr),
$$
whose only surviving summands are the top ones; so the local cross product is an isomorphism over $\ZZ$. Replacing $x$ and $y$ by closed balls of finite radius gives the same statement for the groups $H_*(M\mid B_1)$ and $H_*(N\mid B_2)$ of a pair of balls, which is the form the compatibility condition of an orientation uses.

*The coefficient ring.* This is the step the source asserts. The relative chain complex $C_*(M,M-x)$ is free in each degree (printed p. 261), so the universal coefficient theorem for homology, Theorem 3A.3 (printed p. 264), gives the natural short exact sequence
$$
0\to H_m(M\mid x;\ZZ)\otimes_\ZZ R\to H_m(M\mid x;R)\to\operatorname{Tor}\bigl(H_{m-1}(M\mid x;\ZZ),R\bigr)\to 0 .
$$
By excision $H_m(M\mid x;\ZZ)\cong H_m(D^m,S^{m-1})\cong\ZZ$ and $H_{m-1}(M\mid x;\ZZ)=0$, so $H_m(M\mid x;R)\cong\ZZ\otimes_\ZZ R=R$, and the generator over $R$ is the image $\zeta_x\otimes 1$ of an integral generator $\zeta_x$; the same holds at $y$. By Proposition 3B.1 and the identification $C_*(X;R)\otimes_R C_*(Y;R)=C_*(X\times Y;R)$ used on printed p. 276, the cross product with coefficients in $R$ is the integral chain-level cross product followed by $-\otimes_\ZZ R$. Hence the local cross product carries $\zeta_x\otimes1$ and $\zeta_y\otimes1$ to $(\zeta_x\times\zeta_y)\otimes1=\pm1$: over $R$ it too is an isomorphism $R\otimes_R R\to R$, and the product of generators is a generator.

*Orientations multiply.* If $x\mapsto\mu_x$ and $y\mapsto\nu_y$ are $R$-orientations of $M$ and $N$, then $(x,y)\mapsto\mu_x\times\nu_y$ is an $R$-orientation of $M\times N$: it is a section of the local system by the two paragraphs above, and it satisfies the compatibility condition by passing to the product of closed balls $B_1\ni x$ and $B_2\ni y$. So $M\times N$ is $R$-orientable, with no hypothesis beyond the exercise's. If $M$ and $N$ are connected then so is $M\times N$, and Theorem 3.26(a) (printed p. 236, stated for a closed connected manifold) then gives that the map $H_{m+n}(M\times N;R)\to H_{m+n}(M\times N\mid (x,y);R)\cong R$ is an isomorphism. That sentence, and the paragraph two below on integral coefficients, are the source's first route to the conclusion: they need more than the exercise's hypotheses and are not steps of the proof given here. Connectedness is a hypothesis of Theorem 3.26 and is not needed for the exercise's conclusion, which is a statement about local groups. For a closed $R$-orientable $M$ with components $M_i$, a fundamental class is the sum $\sum_i\alpha_i$ of fundamental classes of the pieces $M_i$: $H_*(M)=\bigoplus_iH_*(M_i)$, and a class is a generator in every local group exactly when each summand $\alpha_i$ is. The cross product is bilinear, so $\alpha\times\beta=\sum_{i,j}\alpha_i\times\beta_j$, and $M\times N$ is the disjoint union of the closed connected manifolds $M_i\times N_j$. The statement for possibly disconnected $M$ and $N$ is therefore the statement for connected ones applied component by component, which is what the last paragraph below checks. Theorem 3.26(a) is not a consequence of the exercise: the exercise produces a class whose image in every local group is a generator, which by Hatcher's definition on printed p. 236 is exactly a fundamental class, while Theorem 3.26(a) is the different assertion that for a closed connected $R$-orientable manifold the map $H_n(M;R)\to H_n(M\mid x;R)$ is an isomorphism, and nothing here proves that.

*The closed manifolds, integral coefficients.* This is the source's second route to the conclusion, it needs more than the exercise's hypotheses, and the paragraph after this one does not use it. Take $R=\ZZ$, so that $M$ and $N$ are now $\ZZ$-orientable — an $R$-orientable manifold need not be: with $R=\ZZ/2$ the projective plane $\RP^2$ is $\ZZ/2$-orientable while $H_2(\RP^2;\ZZ)=0$, so it has no $\ZZ$ fundamental class — and suppose $M$ and $N$ connected, so that $H_m(M;\ZZ)\cong\ZZ\cong H_n(N;\ZZ)$. Kottke's next computation is the Künneth formula for the product, Theorem 3B.6 (printed p. 275), which applies since a closed manifold is homotopy equivalent to a CW complex (Corollary A.12, printed p. 529):
$$
H_{m+n}(M\times N)\ \cong\ H_m(M)\otimes H_n(N)\ \oplus\ \operatorname{Tor}\bigl(H_m(M),H_{n-1}(N)\bigr)\ \oplus\ \operatorname{Tor}\bigl(H_{m-1}(M),H_n(N)\bigr)\ =\ H_m(M)\otimes H_n(N),
$$
all other terms vanishing and the two Tor groups vanishing because the top degree groups are free. So $[M]\times[N]$ is a generator of $H_{m+n}(M\times N)\cong\ZZ$. The connectedness supposed here is doing real work in that last display: without it $H_{m+n}(M\times N;\ZZ)$ is not $\ZZ$ — for $M$ with $k$ components and $N$ with $\ell$ it is $\ZZ^{k\ell}$, one copy for each pair of components — and $[M]\times[N]$ is a generator of each summand, which is the componentwise form of the conclusion reached in the next paragraph.

*The fundamental class.* Finally, for each $(x,y)$ the naturality of the cross product in the pair variables gives
$$
(\alpha\times\beta)_{(x,y)}=\alpha_x\times\beta_y\ \in\ H_{m+n}\bigl(M\times N\mid (x,y);R\bigr),
$$
and by *The coefficient ring* this is a generator whenever $\alpha_x$ and $\beta_y$ are. So $\alpha\times\beta$ has a generator as its image in every local group, which by Hatcher's definition of a fundamental class (printed p. 236) is exactly that $\alpha\times\beta$ is a fundamental class for $M\times N$ with coefficients in $R$.

Hatcher's pages above are cited from the checked-in text of the book, `tmp/sources/hatcher-2002-algebraic-topology.md`, and Kottke's set from its text version, `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.md`, the extraction of the set's own five-page PDF `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.pdf` (sha256 e84fd60496037db45bb18457b7c922233f5912a41b5d067112ba75a8211c22a7).
:::
