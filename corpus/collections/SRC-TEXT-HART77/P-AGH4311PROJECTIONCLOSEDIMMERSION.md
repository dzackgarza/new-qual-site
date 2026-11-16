---
schema: qual/card@1
id: P-AGH4311PROJECTIONCLOSEDIMMERSION
kind: problem
title: Projection embeds a smooth $r$-fold into $\PP^{n-1}$ when $n>2r+1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Very Ample Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.11 together with the projection/linear-system
    criterion II.7.3 and the Veronese construction II.7.7. Part (a) uses
    separate secant and embedded-tangent-space incidence bounds. Part (b)
    reduces each secant to the plane conic obtained from the corresponding
    line in P^2 and checks the lower dimension bound for the secant variety by
    an explicit four-rank local parametrization, valid in every
    characteristic.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), IV.3.11(a),
    printed p. 309. The closed-embedding criterion the last step invokes is
    stated in R. Vakil, The Rising Sea: Foundations of Algebraic Geometry,
    21 October 2025 version, as Theorem 19.1.1, printed p. 536, text version `tmp/sources/vakil-rising-sea-2025-10-21.md`, with the
    hypotheses "injective on closed points" and "injective on tangent vectors at
    closed points" and no other; he reduces it at 19.1.3, printed p. 537, to
    Theorem 19.1.2 and proves that at 19.1.4, but the reduction's last step is
    Exercise 19.1.D, "Show that the degree of pi is at most 1 at all closed
    points of Y", left to the reader and the only place where the tangent-vector
    hypothesis enters. Step s6 cites Vakil with that limit recorded and rests on
    Hartshorne II.7.3 (T-DIVMAPPN), which is the same statement. What is not in
    Vakil is the existence of the centre:
    the secant and tangent loci are closed of dimension at most 2r+1, so a point O
    outside them exists when n > 2r+1, and that count is the card's own. Egbert's
    entry for (a) is a citation to Shafarevich, and Shafarevich was not consulted.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Named the text version of Vakil's book at the citation of Theorem 19.1.1 in
    the remark on 2026-11-16, where it cited the PDF alone: it is
    tmp/sources/vakil-rising-sea-2025-10-21.md. No page or claim changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Part (a) has a complete published proof, located for this batch, and the
    printed exercise was read with it: Hartshorne, Algebraic Geometry (1977),
    IV Ex. 3.11(a), printed p. 316 -- not printed p. 309, which the event of
    2026-11-15 above gives for it; the exercise stands on PDF p. 331 of the
    text version tmp/sources/hartshorne-1977-algebraic-geometry.md, where
    printed p. N is PDF p. N+15. Read at its cited places in the text version
    tmp/sources/shafarevich-2013-basic-algebraic-geometry-1-pp129-138.md:
    Theorem 2.25 on printed p. 134, the lemma on isomorphic embeddings on
    printed pp. 134-135, Corollary 2.7 on printed p. 135, and the proof of
    Theorem 2.25 on printed pp. 135-136, whose folios were checked against the
    PDF (PDF p. 149 is printed p. 133, so printed p. N is PDF p. N+16 in that
    copy). Checked against the book: Shafarevich's Theorem 2.25 is stated for a
    nonsingular projective n-dimensional variety in P^N with N > 2n+1 and
    concludes an isomorphic embedding into P^{N-1}, which is assertion (a) of
    the exercise with N = n and n = r; the closed immersion follows since a
    projective X has closed image. Not checked: Shafarevich's Theorem 1.15,
    which Corollary 2.7 cites for the finiteness of the projection, and
    Theorem 1.25, which the dimension count cites; the retained copy holds
    printed pp. 129-138 only, so neither statement was read, and the card says
    so at the step that uses 1.15. For (b) the published treatment located is
    Egbert's entry 4.3.21, printed p. 223, which argues the clause for a
    general point of a secant line and not for every point of every secant
    line.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Part (a) is now the transcription of Shafarevich's proof, one step per
    published step, each naming the numbered statement and printed page, with
    his sentences quoted at the steps that carry his argument: steps secants
    and tangent-locus for the two incidence varieties and their dimensions,
    step centre for the choice of the point, step lemma-criterion for the lemma
    on isomorphic embeddings with its Nakayama proof, and step corollary for
    Corollary 2.7 and the conclusion of (a). Part (b) keeps its steps, now
    labelled veronese-conic, infinitely-many-secants, secant-dim-upper,
    secant-dim-lower, secant-dim and closed-immersion-b, and its last step now
    cites step corollary, which is the criterion it uses, instead of the three
    former steps of (a). What left the card with the former steps s1-s6 is the
    card's own secant and tangent dimension count, of which step centre now
    quotes Shafarevich's; the Vakil citation and the paragraph on Exercise
    19.1.D leave the card with them, and so does the remark's statement that
    part (a) has no complete published solution in the retained sets, which
    Shafarevich's Theorem 2.25 answers. Nothing in the problem statement
    changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's report, and the record of what
    the three events of this date above left out. (i) The secant bound of part
    (a) is published: J. Harris, Algebraic Geometry: A First Course (1992),
    Lecture 11, Proposition 11.24, states that the secant variety of an
    irreducible k-dimensional variety in P^n is irreducible of dimension at
    most 2k+1, with equality if and only if the general point lying on a
    secant line lies on only finitely many of them, and its Example 11.22
    supplies the dimension 2k of the variety of secant lines that the count
    uses; the proposition's proof is the incidence correspondence of pairs
    (l,p) with p in l, over the variety of secant lines, which is the honest
    secant lines and not the pairs with equal entries. Read at Example 11.22,
    the incidence display before Proposition 11.24, Proposition 11.24 and the
    Veronese paragraph after Exercise 11.25, in the text version
    tmp/sources/harris-1992-algebraic-geometry-first-course-pp128-149.md. That
    text version carries no printed folios, so the printed page of these
    statements is not established; it lies within printed pp. 128-149, the
    range that version retains. The card cites them by lecture and number and
    gives no page. (ii) The card's own proof of the bound, the incidence
    variety over the complement of the diagonal in X x X, stood at step s1
    before 9a5cd235da and was deleted by that commit; 16894bb15f did not
    restore it, so the card carried (a) with the bound assumed. It is back in
    step secants, marked there as the card's own, and the step now proves the
    bound instead of reporting on the source. (iii) Corrected here, the events
    of this date not being rewritable: their sentence "Part (a) has a complete
    published proof", which is true of the exercise but not of Shafarevich's
    count of it; their description of step secants as carrying "the two
    incidence varieties with their dimensions", which Shafarevich's secant
    passage does not do; and their sentence that the card's own secant and
    tangent dimension count "left the card with the former steps s1-s6".
    Also recorded here: commit 16894bb15f, which named the defect, quoted the
    lemma and Corollary 2.7 in full and marked the (b) steps as the card's
    own, had no event of its own until this one. (iv) The erratum and the
    provenance sentences that stood inside the solution are now in the remark
    on the published solution, where the account of a defective published
    argument belongs: the defect itself, the opening sentence "his printed
    count for the secant locus is defective, and step secants says where", and
    a sentence that mixed Shafarevich's P^N with this card's P^n. The
    solution's steps now prove the exercise. Not read in this pass:
    Shafarevich's Theorem 1.15 and Theorem 1.25, as before, and no other part
    of Harris's Lecture 11; no page of either text version was re-read beyond
    the passages named. Checked against the book in this pass: Hartshorne
    IV Ex. 3.11(a) on printed p. 316, unchanged.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's second report. (i) The two bounds
    on the secant variety of the Veronese surface, which (b) asserts, are
    transcribed. P. Harris, Algebraic Geometry: A First Course (1992),
    Lecture 11, Example 11.22, in its Veronese paragraph, prints the upper
    bound from the general point of a secant line lying on a one-dimensional
    family of them and the equality, with the cones over S(X) with vertex a
    point of it as the reason for the lower bound; A. Egbert, Solutions to
    Hartshorne's Algebraic Geometry (2013), IV.3.11, entry 4.3.21, printed
    p. 223, prints the same two bounds from the same argument. Both are quoted
    at steps secant-dim-upper and secant-dim-lower, and step secant-dim is now
    the conclusion the two texts draw. Read for this pass: the Veronese
    paragraph of Example 11.22 in
    tmp/sources/harris-1992-algebraic-geometry-first-course-pp128-149.md, at
    the passages named in the event above, and entry 4.3.21 in the Egbert text
    version named there. Harris's text version still carries no printed folios,
    so the page of Example 11.22 is not established; Egbert's is printed
    p. 223. (ii) The card's own proofs of those two bounds are withdrawn: the
    incidence variety of triples (P,Q,O) with O on the line PQ over the
    complement of the diagonal, with the fibre inequality, for the upper bound,
    and the four-parameter local computation through the chart of the Veronese
    embedding for the lower. A published proof covers that part, so these are
    not the card's-own proofs that a part no source proves keeps; they remain
    readable at commit 2cd5db74ad. What no source proves in (b) is the clause
    that every point of every secant line lies on infinitely many secant
    lines, which steps veronese-conic and infinitely-many-secants prove and
    mark as the card's own. (iii) The remark's sentence "that bound is
    Harris's, and in this card's letters it is the incidence count of step
    secants" confused two different counts: Harris's correspondence lies over
    the variety of secant lines, and the count in step secants over the
    complement of the diagonal in X x X, which is the card's own. The remark
    now says so. (iv) The remark's "the argument above uses" is replaced by
    the two step references it meant, and the solution's opening sentence that
    all the steps of (b) are the card's own now says which ones are, since
    steps secant-dim-upper, secant-dim-lower and secant-dim transcribe two
    printed texts. Not read in this pass: Harris's other lectures, and
    Shafarevich's Theorem 1.15 and Theorem 1.25, as before. Checked against
    the book in this pass: Hartshorne IV Ex. 3.11(b) on printed p. 316,
    unchanged.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's third report, and the record of
    what the passes of this date left out or got wrong. (i) Harris's printed
    pages are established, and they replace the "not established" of the
    event of this date that records the second report. Read off the retained
    PDF tmp/sources/harris-1992-algebraic-geometry-first-course.pdf at PDF
    pp. 157-160, whose running heads read 142, 143, 144 and 145, so printed
    p. N is PDF p. N+15 in that copy, the offset Hartshorne's text version
    also has: Example 11.22 opens on printed p. 143, and the incidence
    correspondence, Proposition 11.24 and the Veronese paragraph are on
    printed p. 144. The text version
    tmp/sources/harris-1992-algebraic-geometry-first-course-pp128-149.md
    carries one range marker, "PDF pages 145-164", and no folios, which is
    why the earlier pass recorded no page. The citations of Harris on this
    card now give those pages. (ii) The quotation at step secant-dim-upper
    changed Harris's words inside quotation marks: he prints "r will lie on
    the plane Lambda spanned by C. But then every line through r in Lambda
    will be a secant line", and the text version renders Lambda as "A". The
    quote now carries his words, read off printed p. 144, and the remark's
    paraphrase of the same passage uses Lambda. (iii) Step secant-dim-upper's
    sentence from the one-dimensional family to the bound 4 is the card's
    own and now says so; Proposition 11.24 states the bound 2k+1 and the
    criterion for equality, not a fibre inequality, and what the step now
    does is apply the equality criterion at k=2. (iv) The sentence "Both
    texts print the bound as immediate, and Harris's parenthetical is the
    only reason either gives" is out of the rendered solution: commentary on
    the sources belongs in neither a solution nor a remark, and the two
    quotations in that step show what each text prints. (v) One symbol for
    one object: the solution opens by declaring Sec(X) the closure in P^n of
    the union of the secant lines, which Harris writes S(X), and steps
    secants, secant-dim and closed-immersion-b use it; step
    closed-immersion-b says that Sec(X) is closed, which both the choice of O
    outside it and the tangent-space argument need, and no longer speaks of
    "the closure of the secant variety". (vi) The part of (b) with no
    published proof is the closed immersion into P^4, which step
    closed-immersion-b proves and marks as the card's own: Egbert's entry
    4.3.21, printed p. 223, stops at the two bounds, and Harris's Example
    11.22, printed p. 144, gives the dimension and no projection. The
    exercise's own parenthetical points to (II, Ex. 7.7), whose part (b),
    printed p. 170, asks the reader to show that the subsystem of conics
    spanned by x^2, y^2, z^2, y(x-z) and (x-y)z gives a closed immersion of
    P^2 into P^4; that is a reference to an exercise, with no printed
    solution, and not a published proof of this step. The part is named open
    in the COMPLAINTS record of this date. (vii) The event of this date that
    ba3057319b added writes "P. Harris"; the author of Algebraic Geometry: A
    First Course is J. Harris, as every other citation of him on this card
    has it. (viii) QUAL-11: no event of this card and no record of
    COMPLAINTS.md was rewritten in this pass; the audit hunks of ba3057319b
    and 9496081602 add lines only, 8cf37922b8 touches no audit block, and the
    text above is the correction of the earlier text, which stands as
    written. Not read in this pass: the printed book itself, any other part
    of Harris's Lecture 11, and Shafarevich's Theorem 1.15 and Theorem 1.25,
    as before; the printed exercise IV Ex. 3.11 is unchanged on printed
    p. 316.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's fourth report, and the correction
    of two things the event above does. (i) The quotation of Proposition 11.24
    was extended by ee563ab9bb and the extension changed Harris's words: he
    prints "the general point p in the line qr lying on a secant line to X
    lies on only a finite number of secant lines to X", with the bar over qr,
    where the card printed p in P^n. That substitution is this card's, not the
    source's. Read off printed p. 144 of the retained PDF, that is PDF p. 159
    of tmp/sources/harris-1992-algebraic-geometry-first-course.pdf, on the
    line after "at most 2k+1, with equality holding if and only if"; the text
    version tmp/sources/harris-1992-algebraic-geometry-first-course-pp128-149.md
    agrees at line 346, and the crude pdftotext rendering of the same line
    gives "p E qr". The quote now carries Harris's qr, and the sentence
    applying the equality criterion at k=2 uses the same letters. (ii) The
    notation repair recorded at (v) of the event above is completed: steps
    centre and corollary still named the closure of the union of the secant
    lines by the second symbol Sigma with a subscript sec, while the solution
    declares Sec(X) and Harris's Sigma names his incidence correspondence of
    pairs (l,p). Both steps now write Sec(X), the display in step centre no
    longer carries the overlined Sigma, and the only Sigma left on the card is
    Harris's correspondence, in steps secants and secant-dim-upper. Not read
    in this pass: any page of either text beyond printed p. 144 of Harris and
    its text version, and nothing of Shafarevich's Theorem 1.15 and 1.25, as
    before. No statement changes; the printed exercise is unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's fifth report, and the correction
    of the last clause of (i) in the event above. That event closed its first
    item "the sentence applying the equality criterion at k=2 uses the same
    letters", and the sentence did, writing p in the line qr outside any
    quotation, where those letters are not bound on this card: r is the
    dimension of X in the statement and in the solution's opening, and in the
    quotation of the same step r is a general point of P^5 and q a point of
    P^2. Harris's letters belong inside the quotation at printed p. 144, which
    now carries them; the card's own sentence names the general point of a
    general secant line of X in words, and introduces no letter of its own, so
    that nothing collides with r as a dimension. That sentence is still the
    card's own and still says so. Not read in this pass: no source was read
    again; the quotation and its page stand as the event above records them.
    No statement changes, and no step's claim changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's whole-card reading, and the
    correction of a misreading the event of this date that ba3057319b added
    carries. That event records "the cones over S(X) with vertex a point of it
    as the reason for the lower bound". Harris, Example 11.22, printed p. 144,
    writes "the cones p-bar,S over S with vertex a point p in S would all have
    to coincide", in the paragraph that has just introduced X as the Veronese
    surface; his letters are ambiguous as printed, and the remark paraphrasing
    him resolved them the wrong way. With S read as the secant variety the
    argument does not run: nothing on this card or in Harris puts the cone
    over S(X) with a vertex on it inside S(X). With S read as the surface, it
    does: for p in X every line joining p to a point of X is a secant line, so
    the cone lies in S(X), and it is three-dimensional, being the union of a
    surface's worth of lines through p; were dim S(X) 3, each such cone would
    be S(X) and the cones, whose vertices differ, would coincide. The
    published-solution remark now carries the cones over X, with the
    containment that makes the argument run, and Harris's own sentence is
    quoted unchanged at step secant-dim-lower, as his words and inside
    quotation marks. The event of this date stands as written, and the record
    of this date in COMPLAINTS.md that repeats the misreading is corrected in
    a new record of today. Not read in this pass: no page of Harris beyond
    printed p. 144 already read, and no other source; the paragraph of
    Example 11.22 in the text version at line 352 was checked for the same
    sentence.
---

::: {.problem}
(a) If $X$ is a nonsingular variety of dimension $r$ in $\PP^n$, and if $n>2r+1$, show that there is a point $O \notin X$, such that the projection from $O$ induces a closed immersion of $X$ into $\PP^{n-1}$.

(b) If $X$ is the Veronese surface in $\PP^5$, which is the 2-uple embedding of $\PP^2$ (I, Ex.
2.13), show that each point of every secant line of $X$ lies on infinitely many secant lines.
Therefore, the secant variety of $X$ has dimension 4, and so in this case there is a projection which gives a closed immersion of $X$ into $\PP^4$ (II, Ex.
7.7).

A theorem of Severi states that the Veronese surface is the only surface in $\PP^5$ for which there is a projection giving a closed immersion into $\PP^4$.
Usually one obtains a finite number of double points with transversal tangent planes.
:::


::: {.solution}

Let $X\subseteq\PP^n$ be nonsingular of dimension $r$.
Write $\operatorname{Sec}(X)$ for the closure in $\PP^n$ of the union of the secant lines $\overline{PQ}$ of $X$ over pairs of distinct points $P,Q\in X$; it is closed, and Harris writes $S(X)$ for it.
Part (a) is I. R. Shafarevich, *Basic Algebraic Geometry 1*, third edition (2013), §5.4, printed pp. 134--136, for the tangent bound, the lemma on isomorphic embeddings, Corollary 2.7 and the projection, and J. Harris, *Algebraic Geometry: A First Course* (1992), Lecture 11, Example 11.22, printed pp. 143--144, and Proposition 11.24, printed p. 144, for the secant bound.
The steps of part (b) that rest on no published argument are the card's own and each says so; the two bounds on $\dim\operatorname{Sec}(X)$ are Harris's and Egbert's.

::: pf

::: {.pf-step #secants}

$\operatorname{Sec}(X)$ has dimension at most
$$
2r+1.
$$

::: pf-proof

J. Harris, *Algebraic Geometry: A First Course* (1992), Lecture 11, Proposition 11.24, printed p. 144: "The variety $\mathcal S(X)\subset\Gr(1,n)$ of secant lines to an irreducible $k$-dimensional variety $X\subset\PP^n$ is irreducible of dimension $2k$. The secant variety $S(X)\subset\PP^n$ is irreducible of dimension at most $2k+1$, with equality holding if and only if the general point $p\in\overline{qr}$ lying on a secant line to $X$ lies on only a finite number of secant lines to $X$", with his note "that in this statement we need only consider points $p$ lying on honest secant lines, that is, secant lines actually spanned by points of $X$." His Example 11.22, printed pp. 143--144, defines the secant line map
$$
s\colon X\times X-\Delta\longrightarrow\Gr(1,n),\qquad (p,q)\longmapsto\overline{pq},
$$
on the complement of the diagonal and shows that its image $\mathcal S(X)$ has dimension $2k$, and closes with the incidence correspondence
$$
\Sigma=\{(l,p):p\in l\}\subset\mathcal S(X)\times\PP^n,
$$
whose image in $\PP^n$ is $S(X)$ and whose projection $\pi_1$ to the first factor is surjective with all fibres of dimension $1$; hence $\dim\Sigma=2k+1$, from which $\dim S(X)\le\dim\Sigma$, and he writes that the proposition "then follows". With this card's letters $k=r$, and a nonsingular variety is irreducible.

The incidence count that follows is the card's own; it reaches the same bound over the complement of the diagonal directly.

Let
$$
\mathcal I=\{(P,Q,O):P,Q\in X,\ P\ne Q,\ O\in\overline{PQ}\}\subseteq X\times X\times\PP^n .
$$
For $r\ge1$ the base $(X\times X)\setminus\Delta$ is a nonempty open subset of the irreducible $X\times X$ and so is irreducible of dimension $2r$, and the fibre of $\mathcal I$ over $(P,Q)$ is the projective line $\overline{PQ}$, of dimension $1$; hence
$$
\dim\mathcal I=2r+1 .
$$
For $r=0$ there are no distinct pairs and the union of secant lines is empty, so the bound holds there too. The image of $\mathcal I$ under the projection to $\PP^n$ is the union of the secant lines, so the dimension of its closure is at most $\dim\mathcal I=2r+1$.

:::

:::

::: {.pf-step #tangent-locus}

The union of the embedded projective tangent spaces $T_PX$ of $X$ is the image $U_2$ of a closed subset $\Gamma'\subseteq\PP^n\times X$, and
$$
\dim U_2\le2r .
$$

::: pf-proof

Shafarevich, proof of Theorem 2.25, printed p. 136: "In a similar way, to study the set $U_2$ we consider in $\PP^N\times X$ the set $\Gamma'$ consisting of points $(a,b)$ such that $a\in\Theta_b$. In exactly the same way we have projections $\psi:\Gamma'\to X$ and $\varphi:\Gamma'\to\PP^N$. For $b\in X$ we have $\dim\psi^{-1}(b)=n$ since $X$ is nonsingular, and hence $\dim\Gamma'=2n$, and since $U_2=\varphi(\Gamma')$, also $\dim U_2\le2n$."

Here $\Theta_b$ is the embedded tangent space $T_bX\subseteq\PP^N$, a linear subspace of dimension $n$ of $\PP^N$ when $X$ has dimension $n$ and is nonsingular at $b$; with this card's letters $\dim T_PX=r$, so the fibre of $\Gamma'\to X$ over $P$ has dimension $r$ and $\dim U_2\le2r$. Nothing in this passage uses the diagonal, and the identification $U_2=\varphi(\Gamma')$ is with the union of the tangent spaces itself.

:::

:::

::: {.pf-step #centre}

For $n>2r+1$ there is a point $\xi\in\PP^n$ lying on no secant line of $X$, in no embedded tangent space $T_PX$, and not on $X$.

::: pf-proof

Shafarevich, proof of Theorem 2.25, printed p. 136, concludes: "We see that $\dim U_1\le\dim\Gamma=2n+1$ and $\dim U_2\le2n$; therefore if $N>2n+1$ then $U_1\cup U_2\ne\PP^N$, which was what we wanted."

The conclusion holds for the closures: $\operatorname{Sec}(X)$ is the closure of the union of the secant lines, and $U_2$ is the union of the embedded tangent spaces. By step [](#secants){.pf-ref} $\dim\operatorname{Sec}(X)\le2r+1$ and by step [](#tangent-locus){.pf-ref} $\dim\overline{U_2}\le2r$, so with $n>2r+1$ the two closed subsets $\operatorname{Sec}(X)$ and $\overline{U_2}$ of $\PP^n$ have dimension strictly below $n$, and $\dim X=r<n$. Hence
$$
X\cup\operatorname{Sec}(X)\cup\overline{U_2}
$$
is a proper closed subset of the irreducible $\PP^n$, and every point of its complement is a centre of the kind required: being outside $\operatorname{Sec}(X)$ it lies on no secant line, being outside $\overline{U_2}$ it lies in no embedded tangent space, and it is not on $X$.

:::

:::

::: {.pf-step #lemma-criterion}

Shafarevich, Lemma, printed p. 134: a finite map $f$ from a variety $X$ is an isomorphic embedding if and only if it is one-to-one and $d_xf$ is an isomorphic embedding of the tangent space $\Theta_x$ for every $x\in X$. The proof, printed pp. 134--135, is a Nakayama argument.

::: pf-proof

The proof is Shafarevich's, printed pp. 134--135, and runs as follows, with its own notation.

"Set $f(X)=Y$ and $\varphi=f^{-1}$. The lemma will be proved if we show that $\varphi$ is a regular map. The assertion is local in nature. For $y\in Y$, let $x\in X$ be such that $f(x)=y$. Write $U$ and $V$ for affine neighbourhoods of $x$ and $y$ with $f(U)=V$ and such that $k[U]$ is integral over $k[V]$, and continue to write $f:U\to V$ for the restriction of $f$. It is enough to prove that $f$ is an isomorphism for suitable choice of $U$ and $V$, since then $\varphi=f^{-1}$ is a regular map at $y$."

"Recall that the tangent space $\Theta_x$ is the dual vector space to $\mathfrak m_x/\mathfrak m_x^2$, where $\mathfrak m_x$ is the maximal ideal of the local ring $\mathcal O_x$. The second hypothesis of the lemma is that $f^*:\mathfrak m_y/\mathfrak m_y^2\to\mathfrak m_x/\mathfrak m_x^2$ is surjective. In other words, if $\mathfrak m_y=(u_1,\ldots,u_k)$, then the elements $f^*(u_i)+\mathfrak m_x^2$ generate $\mathfrak m_x/\mathfrak m_x^2$. We apply Nakayama's lemma (Proposition A.11) to $\mathfrak m_x$ as an $\mathcal O_x$-module. It then follows from this that $\mathfrak m_x=(f^*(u_1),\ldots,f^*(u_k))$, or in other words
$$
\mathfrak m_x=f^*(\mathfrak m_y)\mathcal O_x. \tag{2.40}
$$"

"We check that $\mathcal O_x$ is a finite module over $f^*(\mathcal O_y)$. Since $k[U]$ is a finite $k[V]$-module, it is enough to prove that each element of $\mathcal O_x$ can be expressed in the form $\xi/f^*(a)$ with $\xi\in k[U]$ and $a\notin\mathfrak m_y$. For this, it is enough to check that for $\alpha\in k[U]$ with $\alpha\notin\mathfrak m_x$ there exists an element $a\in k[V]$ with $a\notin\mathfrak m_y$ such that $f^*(a)=\alpha\beta$ with $\beta\in k[U]$. By Theorem 1.12 the set $f(V(\alpha))$ is closed, and since $f$ is one-to-one, $y\notin f(V(\alpha))$. Hence there exists a function $c\in k[V]$ such that $c=0$ on $f(V(\alpha))$ and $c(y)\ne0$. Then $f^*(c)=0$ on $V(\alpha)$ and $f^*(c)(x)\ne0$. By the Nullstellensatz, $f^*(c)^n=\alpha\beta$ for some $n>0$ and $\beta\in k[U]$. We can set $a=c^n$."

"Now we can apply Nakayama's lemma to $\mathcal O_x$ as a $f^*(\mathcal O_y)$-module. The equality (2.40) shows that $\mathcal O_x/f^*(\mathfrak m_y)\mathcal O_x=\mathcal O_x/\mathfrak m_x=k$, and hence is generated by the single element $1$. It now follows by Nakayama's lemma that $\mathcal O_x=f^*(\mathcal O_y)$."

"Let $u_1,\ldots,u_l$ be a basis of $k[U]$ as a module over $k[V]$. By what we have proved, $u_i\in\mathcal O_x=f^*(\mathcal O_y)$. Write $V'=V\setminus V(h)$ for a principal affine neighbourhood of $y$ such that all $(f^*)^{-1}(u_i)$ are regular in $U'=U\setminus V(f^*(h))$. Then $k[U']=\sum f^*k[V']u_i$. By assumption $u_i\in f^*(k[V'])$, and it follows that $k[U']=k[V']$, which means that $f:U'\to V'$ is an isomorphism. The lemma is proved."

:::

:::

::: {.pf-step #corollary}

Shafarevich, Corollary 2.7, printed p. 135: let $X\subseteq\PP^N$ be a variety and $\xi\in\PP^N\setminus X$; if every line through $\xi$ intersects $X$ in at most one point and $\xi$ is not contained in the tangent space to $X$ at any point, then the projection from $\xi$ is an isomorphic embedding $\overline X\hookrightarrow\PP^{N-1}$. Applied to a point $\xi$ of step [](#centre){.pf-ref} it gives a closed immersion of $X$ into $\PP^{n-1}$, which is assertion (a) of the exercise.

::: pf-proof

The statement is Corollary 2.7, printed p. 135, and its proof there is one sentence: "It is enough to apply the lemma, together with Theorem 1.15."

Take a point $\xi$ of the open set of step [](#centre){.pf-ref}. It lies outside $\operatorname{Sec}(X)$, so it lies on no line through two distinct points of $X$, and every line through $\xi$ therefore meets $X$ in at most one point; and it lies outside $\overline{U_2}$, so $\xi\notin T_PX$ for every $P\in X$. The two hypotheses of the corollary are met.

The lemma of step [](#lemma-criterion){.pf-ref} needs the projection $X\to\PP^{n-1}$ to be finite, which is what the cited Theorem 1.15 supplies. The conclusion is that the projection restricts to an isomorphism of $X$ onto its image in $\PP^{n-1}$; that image is closed, because a morphism from the projective variety $X$ is proper, so the isomorphism onto the image is a closed immersion.

:::

:::

::: {.pf-step #veronese-conic}

Now let
$$
\nu_2:\PP^2\longrightarrow X\subseteq\PP^5
$$
be the quadratic Veronese embedding. Every secant line to $X$ is contained
in the plane of a Veronese conic.

::: pf-proof

This step is the card's own.

Let a secant line join the two distinct points
$$
\nu_2(P),\nu_2(Q),
\qquad
P,Q\in\PP^2.
$$
Let
$$
\ell=\overline{PQ}\subseteq\PP^2.
$$
The restriction
$$
\nu_2\restrict_\ell:\ell\cong\PP^1\longrightarrow\PP^5
$$
is the complete quadratic Veronese embedding of $\PP^1$.
Its image
$$
C=\nu_2(\ell)
$$
is a nonsingular plane conic spanning a plane
$$
\Pi\cong\PP^2.
$$
Both endpoints of the secant lie on $C$, so their joining line lies in
$\Pi$.

:::

:::

::: {.pf-step #infinitely-many-secants}

Every point of every secant line of $X$ lies on infinitely many
secant lines of $X$.

::: pf-proof

This step is the card's own.

Let
$$
O
$$
be a point of the secant line in step [](#veronese-conic){.pf-ref}. Then
$$
O\in\Pi.
$$
Consider the pencil of all lines in $\Pi$ through $O$.

If $O\in C$, every member except the unique tangent line at the smooth point
$O$ meets $C$ in $O$ and one further distinct point.

Suppose $O\notin C$. Projection from $O$ gives a finite morphism
$$
C\longrightarrow\PP^1
$$
of degree $2$, where the target is the pencil of lines through $O$.
The original secant line from step [](#veronese-conic){.pf-ref} is one fibre containing two distinct
points. Hence this degree-two morphism is generically separable: a purely
inseparable degree-two map would be radicial and could not have such a
fibre. Therefore the geometric generic fibre consists of two distinct
points, and the same holds over a nonempty open subset of the pencil.

In either case infinitely many lines through $O$ are secants of the conic
$C$. Since
$$
C\subseteq X,
$$
they are also secant lines of the Veronese surface $X$.

:::

:::

::: {.pf-step #secant-dim-upper}

The secant variety of the Veronese surface has dimension at most $4$.

::: pf-proof

J. Harris, *Algebraic Geometry: A First Course* (1992), Lecture 11, Example 11.22, printed p. 144, on $X=\nu_2(\PP^2)\subset\PP^5$: "suppose that $r\in\PP^5$ is a general point lying on a secant line to $X$; we may write the secant line as $\overline{\nu(p),\nu(q)}$ for some pair of points $p,q\in\PP^2$. Now, the line $L=\overline{pq}\subset\PP^2$ is carried, under the Veronese map $\nu$, to a plane conic curve $C\subset X\subset\PP^5$, and since $r\in\overline{\nu(p),\nu(q)}$, $r$ will lie on the plane $\Lambda$ spanned by $C$. But then every line through $r$ in $\Lambda$ will be a secant line to $C$, and hence to $X$. In particular, it follows that a general point lying on a secant line to $X$ lies on a one-dimensional family of secant lines to $X$. We may deduce from this that the dimension of $S(X)$ is at most $4$."

The passage from that family to the number is the card's own, and it is Proposition 11.24's equality criterion at $k=2$: his incidence correspondence $\Sigma=\{(l,p):p\in l\}$ over the variety of secant lines has dimension $2k+1=5$ at $k=2$, so $\dim\operatorname{Sec}(X)\le5$, and equality there would put the general point of a general secant line of $X$ on only finitely many secant lines, which the quoted passage denies in giving it a one-dimensional family; hence $\dim\operatorname{Sec}(X)\le4$.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.11, entry 4.3.21, printed p. 223, prints the same bound from the same argument: after "Thus a general point on a secant line to $X$ lies on a one-dimensional family of secant lines to $X$" he writes "Since we are in $\PP^5$ at any rate, then the secant variety has dimension at most $4$."

:::

:::

::: {.pf-step #secant-dim-lower}

The secant variety has dimension at least $4$.

::: pf-proof

Harris, Example 11.22, printed p. 144, prints it as immediate: "since it is clear on elementary grounds that $S(X)$ cannot have dimension less than $4$ (for example, the cones $\overline{p,S}$ over $S$ with vertex a point $p\in S$ would all have to coincide), we conclude that $\dim(S(X))=4$."

Egbert, entry 4.3.21, printed p. 223, prints the same bound in one sentence: "On the other hand, the secant variety clearly has dimension at least $4$."

:::

:::

::: {.pf-step #secant-dim}

The secant variety of the Veronese surface has dimension exactly
$$
\boxed{4}.
$$

::: pf-proof

Steps [](#secant-dim-upper){.pf-ref} and [](#secant-dim-lower){.pf-ref} give the two inequalities
$$
\dim\operatorname{Sec}(X)\le4
\qquad\text{and}\qquad
\dim\operatorname{Sec}(X)\ge4,
$$
and both texts state the conclusion in that form: Harris's Example 11.22, printed p. 144, closes "we conclude that $\dim(S(X))=4$", and Egbert's entry 4.3.21, printed p. 223, carries the two bounds in one paragraph.

:::

:::

::: {.pf-step #closed-immersion-b}

There is a projection
$$
X\hookrightarrow\PP^4
$$
which is a closed immersion.

::: pf-proof

This step is the card's own.

By step [](#secant-dim){.pf-ref},
$$
\dim\operatorname{Sec}(X)=4,
$$
and $\operatorname{Sec}(X)$, being a closure, is a closed subset of the irreducible $\PP^5$ of dimension $5$, so
$$
\operatorname{Sec}(X)
\subsetneq
\PP^5.
$$
Choose
$$
O\in\PP^5\setminus\operatorname{Sec}(X).
$$
Every secant line of $X$ lies in $\operatorname{Sec}(X)$, and so does every embedded tangent space of the smooth surface $X$: every tangent direction is a limit of secant directions, and the projective tangent plane is the union of its tangent lines through the point.
Thus $O$ lies on neither a secant line nor an embedded tangent plane of $X$.

The criterion of step [](#corollary){.pf-ref} needs exactly that $O$ lie on no secant line and in no embedded tangent space, and both hold here; since $X$ is projective, projection from $O$ is therefore a closed immersion
$$
\boxed{X\hookrightarrow\PP^4}.
$$
This is the projection asserted in (b).

:::

:::

::: pf-qed

Steps [](#secants){.pf-ref}, [](#tangent-locus){.pf-ref}, [](#centre){.pf-ref}, [](#lemma-criterion){.pf-ref} and [](#corollary){.pf-ref} give (a): the secant bound is Harris's Proposition 11.24 with the card's own incidence count beside it in step [](#secants){.pf-ref}, the tangent bound, the lemma on isomorphic embeddings with its Nakayama proof and Corollary 2.7 are Shafarevich's, and step [](#corollary){.pf-ref} concludes the closed immersion into $\PP^{n-1}$.
Steps [](#veronese-conic){.pf-ref} and [](#infinitely-many-secants){.pf-ref} prove that each point of every secant line of the Veronese surface lies on infinitely many secant lines, steps [](#secant-dim-upper){.pf-ref}, [](#secant-dim-lower){.pf-ref} and [](#secant-dim){.pf-ref} transcribe Harris's and Egbert's two bounds on the dimension of its secant variety and conclude it, and step [](#closed-immersion-b){.pf-ref} gives the closed immersion into $\PP^4$ that (b) asks for.

:::

:::

:::

::: {.remark title="Published solution"}
Part (a) is completed from two printed texts. The secant bound $\dim S(X)\le2r+1$ is J. Harris, *Algebraic Geometry: A First Course* (1992), Lecture 11, Proposition 11.24, printed p. 144, which follows from the incidence correspondence over the variety of secant lines that closes his Example 11.22, printed pp. 143--144, the same example giving the dimension $2k$ of that variety. The rest is I. R. Shafarevich, *Basic Algebraic Geometry 1*, third edition (2013), §5.4, printed pp. 134--136: Theorem 2.25, printed p. 134, states it, the lemma on isomorphic embeddings and Corollary 2.7 on the projection are printed on pp. 134--135, and the count that produces the centre is on pp. 135--136, correctly in the tangent case.

His secant count on p. 136 is defective as printed. His $\Gamma$ is the set of triples $(a,b,c)$ of $\PP^N\times X\times X$ with $a,b,c$ collinear, and for $b=c$ the three points $a,b,b$ lie on a line for every $a$, so $\Gamma$ contains $\PP^N\times\Delta_X$ and its image $U_1=\varphi(\Gamma)$ is the whole of $\PP^N$, of dimension $N>2n+1$; the printed bound $\dim U_1\le\dim\Gamma=2n+1$ is then false of the set he identifies with $U_1$, and it bounds the ambient space rather than the locus of centres. The centres are the image of the part of $\Gamma$ with $b\ne c$, which the printed passage neither separates from the diagonal nor bounds. That bound is Harris's Proposition 11.24, whose incidence correspondence lies over the variety of secant lines; the count in step [](#secants){.pf-ref} is a second one, the card's own, over the complement of the diagonal in $X\times X$.
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.11, printed p. 223, gives (a) in entry 4.3.20 as "This is Shafarevich Algebraic Geometry 1, theorem 9, page 136", the numbering of an earlier edition of Shafarevich; in the 2013 edition the theorem is 2.25, and the proof on pp. 135--136 contains the same secant count.

His entry 4.3.21, printed p. 223, argues (b) for a general point of a secant line: "If $r\in\PP^5$ is a general point on a secant line $\overline{v(P)v(Q)}$ of $X$, then $\overline{pq}$ maps to a conic $C$ in $X$ and $r$ then lies on the plane spanned by $C$. Any other line on the plane passing through $r$ is also a secant line to $C$ and thus to $X$. Thus a general point on a secant line to $X$ lies on a one-dimensional family of secant lines to $X$. Since we are in $\PP^5$ at any rate, then the secant variety has dimension at most $4$. On the other hand, the secant variety clearly has dimension at least $4$."
Harris, Lecture 11, Example 11.22, printed p. 144, takes the same route for the Veronese surface and carries it to the dimension: the plane $\Lambda$ spanned by $C$ contains $r$, every line through $r$ in $\Lambda$ is a secant line to $C$ and hence to $X$, so a general point of a secant line to $X$ lies on a one-dimensional family of them, whence $\dim S(X)\le4$; and $\dim S(X)=4$, since otherwise the cones over $X$ with vertex a point $p\in X$, each of them three-dimensional and contained in the secant variety because its lines join $p$ to points of $X$, would all have to coincide. Both bounds are transcribed in steps [](#secant-dim-upper){.pf-ref}, [](#secant-dim-lower){.pf-ref} and [](#secant-dim){.pf-ref}, together with Egbert's statement of them, printed p. 223.
The clause for a general point of a secant line is what both texts give; the exercise asks it for every point of every secant line, and for those points the conic of the plane through the point is the one steps [](#veronese-conic){.pf-ref} and [](#infinitely-many-secants){.pf-ref} use.
:::
