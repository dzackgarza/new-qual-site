---
schema: qual/card@1
id: P-AGH434RATIONALNORMALCURVE
kind: problem
title: The rational normal curve of degree $d$ in $\PP^d$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Very Ample Divisors
  - Genus
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.4 together with the d-uple embedding from I.2.12 and
    the degree/genus comparison referenced in II.7.8.5. The proof below
    independently proves projective normality and quadratic generation by a
    monomial straightening argument, then proves the minimal-degree
    classification from h^0(L) <= deg L + 1 without invoking a stronger
    classification theorem.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Printed exercise read again for this pass: Hartshorne, Algebraic Geometry
    (1977), IV.3.4, printed p. 315 (PDF p. 330 of the checked-in extraction
    tmp/sources/hartshorne-1977-algebraic-geometry.md), parts (a) and (b) with
    the two sentences that follow (b), which the card's statement carries. The
    published solution named in the brief was read at the cited place in its text
    version: Chin-Lung Wang's Algebraic Geometry II (NTU, 2020 Spring), Chapter
    IV homework, section 3 Exercise 4 by Yu-Chi Hou,
    tmp/sources/ntu-ag2-chapter4.md; part (a) is on printed pp. 8--9 and parts
    (b), (c), (d) on printed p. 10, page positions fixed on
    tmp/sources/ntu-ag2-chapter4.pdf, whose printed folio is its PDF page. The
    brief names part (a) only; (b) is proved there too, at p. 10, and is
    transcribed with it.

    What the source proves and what it does not: its division of the ideal by the
    quadrics g_ij is complete, but the degree count that closes its
    integral-closure argument is garbled as printed (p. 8: "mn = m(n-1) +
    dk_{n-1} + ... = m + dk_1 = dk_0. Hence, m = dk_{n-1} => d | m", with n and
    d interchanged in the indices of the next display) and its toric restatement
    at pp. 8--9 gives a monoid that is not the one of the d-uple embedding. Both
    are recorded in COMPLAINTS.md under this date. What this pass did not do: it
    did not re-read Egbert, whose citation is that of an earlier event and stands
    unchanged.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the transcription of Hou's solution, one step per
    published argument, each step naming part and printed page: s1 and s8's
    identification S(X) = k[t_0^d,...,t_1^d] (Hou (a), printed p. 8, from I Ex
    2.12), s2 the integral-closure argument (p. 8; its garbled degree count
    replaced by the reason the conclusion follows, which is s1), s3 and s4 the
    quadrics (p. 9), s5--s8 part (b) (p. 10), s9 and s10 the degree-2 and
    degree-3 consequences (p. 10). The monomial count in s1, and the expansions
    of Hou's three compressed sentences -- that dim|D| = n is completeness of
    the system, that g(X)=0 gives X = P^1 and O_X(1) = O_{P^1}(d), and that the
    t_1-exponent ranges in s4 meet only at the multiples of n -- are marked in
    the text as the card's own where they replace the source's word; the
    mathematics they supply is a definition or a citation of IV.1.3.5 and IV
    Ex 1.5 in each case. The parts of the statement the source treats only by
    citation are (a)'s projective normality, whose proof is the source's
    integral-closure argument, and (b)'s final identification with nu_d, which
    the source states in one sentence. Checked against the book: (a)'s two
    assertions, (b)'s hypotheses d <= n and nondegeneracy, and the two "in
    particular" sentences, printed p. 315.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    #121 reader's report on this round, and the two events of this date
    restored. The step names s1--s10 in the restored events above are those of
    the card as it stood that day, before it was given named steps; the two
    steps this event changes are #strict-inequality and #genus-zero.
    Part (b)'s degree and genus are printed in Egbert, so they are
    transcribed rather than redone: steps #strict-inequality and #genus-zero now
    give A. Egbert, Solutions to Hartshorne's Algebraic Geometry (2013),
    IV.3.4(b), printed p. 220, his chain "l(D) = n+1 <= deg(D)+1 = d+1 <= n+1.
    Thus n = d. Since deg(D) = dim(D), and d != 0, then by exc IV.1.5, g = 0",
    and the identification in his closing sentence. The proof written earlier
    today, from h^0 <= e+1 by induction and then a degree-one map to P^1, is
    withdrawn: the same chain is printed, so the source governs. Two slips of
    his are named on the card, not copied: l(D) = n+1 is what nondegeneracy
    gives as l(D) >= n+1, and "deg(D) = dim(D)" compares the degree with the
    dimension of the linear system, where what the citation needs is
    deg D = dim|D|. The reader named the page as printed p. 219; part (a) is on
    that page and the proof of (b) is on the next, whose printed folio is 220.
    The restored source-checked event says Hou's (b) at printed p. 10 "is
    transcribed with it": Hou's (b) states dim|D| = n and does not establish it,
    and what the card takes from Hou in part (b) is the closing sentence of his,
    not the degree and genus. Three further corrections on this card: the
    solution's opening sentence said the whole solution was the transcription
    of Hou, where four of its ten steps are the card's own; the expansion of
    Hou's closing sentence said a divisor of degree d on P^1 "is d times a
    point", where a divisor of degree d is linearly equivalent to dP; and the
    remark's Egbert sentence said he checks the surjectivity of the restriction
    maps and identifies the quadrics Q_ij as generators, where printed p. 219
    asserts both halves of (a) in one sentence each and proves neither and names
    no Q_ij. The remark also called IV.1.3.5 an exercise, where it is an Example
    of the text; it is cited as one. Where and how the sources were read:
    Egbert in tmp/sources/hartshorne-solutions-egbert.md, section 4.3.6 for
    printed p. 219 and the section headed "4.3.7 b. x g" for printed p. 220, the
    page positions read off the folios of
    tmp/sources/hartshorne-solutions-egbert.pdf, whose printed folio is its PDF
    page; Hou in tmp/sources/ntu-ag2-chapter4.md, (a) on printed pp. 8--9 and
    (b)--(d) on printed p. 10, positions fixed on
    tmp/sources/ntu-ag2-chapter4.pdf; and the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, IV.3.4 on printed p. 315
    and IV.1.3.5 in the Examples of §IV.1. Not read in this pass: Egbert's
    IV.3.5, IV.3.6 and IV.3.7, which cite IV.3.4(b), and any search outside the
    brief's three sources for part (a)'s projective normality, which remains the
    card's own proof from Exercise II.5.14(d). The two events of this date above
    were rewritten in place by e4872b53d6; they are restored to the text they
    carried when written, and this event is the correction.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    #121 reader's report on this round: what the restored event of this date says
    step s2 does, the proof it calls written earlier today, the event one commit
    rewrote, and three sentences of the rendered card.

    What the restored event says step s2 does is not what the card does. That
    event's s2 is the projective-normality step in the numbering the card carried
    that day, now step #projective-normality; the event says it "keeps Hou's
    integral-closure route and supplies the conclusion of the garbled line", and
    that route is false. The card's projective normality is the card's own proof
    from Exercise II.5.14(d), in step #projective-normality with
    #surjective-restriction, which is the proof the card carried before this
    round. Three statements of Hou's part (a) are
    false and are named where they would otherwise be used, none of them named by
    any record of this date before this one: that Frac S(X) = k(t_0,t_1), where
    for d >= 2 Frac S(X) is a proper subfield of it; that d divides the t-degree
    of every element of k[t_0,t_1] integral over S(X), which fails at d = 2, where
    t_0 is a root of T^2 - t_0^2 over k[t_0^2,t_0t_1,t_1^2] and has degree 1;
    and that a lexicographic remainder by the quadrics g_ij contains no pure power
    x_i^l, whose leading monomial under g_{i-1,i} = x_{i-1}x_{i+1} - x_i^2 is
    x_{i-1}x_{i+1}. So the statement in the restored record of this date that
    projective normality is answered by Hou's integral-closure argument is not the
    card's; the part that remains the card's own is (a)'s projective normality
    proved from Exercise II.5.14(d), and the obligation under #121 stands as the
    record states it.

    The proof the restored event calls "written earlier today" is not the one
    written today. It is the card's own proof of 2026-09-18, which revision
    199b5eb36b^ carries: h^0(L) <= e+1 by induction on the degree, then the
    degree-one map to PP^1. What was written earlier today, at 199b5eb36b and
    revised at e4872b53d6, was the chain n <= dim|D| <= deg D = d <= n read off
    Exercise IV.1.5, and that is what is withdrawn, Egbert printing the same chain
    at printed p. 220. The 2026-09-18 proof of (b) was replaced when the card was
    transcribed, as the event of this date records, and its replacement is
    Egbert's chain.

    QUAL-11: commit d37c02e2b0 rewrote in place, minutes after df9cd73f42 wrote
    it, the event of this date that records the reader's report. The sentence it
    inserted -- that the text-version paths which stood in the rendered solution's
    opening sentence and in both remark paragraphs are out of them -- is stated
    here instead, and not there: that event now stands as the text it carried at
    df9cd73f42, byte for byte. Nothing else in these events was rewritten in this
    pass.

    Three sentences of the rendered card. The published-solution remark said the
    card proves "part (b)'s degree and genus from Exercise IV.1.5", which is what
    the card did before this round and contradicts the solution's opening sentence
    and steps #strict-inequality and #genus-zero, both of which transcribe Egbert;
    the remark now names Egbert's solutions, printed p. 220, with Exercise IV.1.5
    as the bound his chain uses. In the same remark the quotation of Egbert's
    part (a) entry ran "projectively normal; If theta is the corresponding ring
    homomorphism", where he prints a full stop between the two sentences; the
    quotation now has it. And step #projective-normality closed with "Neither
    statement is used above", the word the writing policy sends to a step
    reference or removes; it reads "in this proof".

    Where and how this pass read its source: the Egbert passage quoted in the
    remark was re-read in tmp/sources/hartshorne-solutions-egbert.md, in the
    section headed "4.3.6 IV.3.4 x g", where the two sentences stand on separate
    lines with a full stop after "projectively normal". His pages were not fixed
    again here: printed p. 219 for part (a) and printed p. 220 for part (b) are
    the pages of the event of this date above, read there off the folios of
    tmp/sources/hartshorne-solutions-egbert.pdf. Not read in this pass: Hou's text
    version, the book, and Egbert's entries 4.3.7 to 4.3.9 beyond the part (b)
    sentences that steps #strict-inequality and #genus-zero quote; the pages of
    Reiser's and Hou's IV.2.2 are corrected in the event of this date on
    P-AGH422GENUSTWOMODULI and not here. No step was re-derived and no rendered
    mathematics changes except the three sentences named above.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    #121 reader's report on the event of this date above, which is left as written:
    which commit took part (b) away from the card's own proof. That event says "The
    2026-09-18 proof of (b) was replaced when the card was transcribed, as the
    event of this date records, and its replacement is Egbert's chain", and the
    sentence before it dates what was written earlier today to "199b5eb36b and
    revised at e4872b53d6". Two commits are compressed into one there, and the
    first of them did not put Egbert on the card. What each revision carries:
    199b5eb36b^ holds the card's own proof of 2026-09-18, h^0 <= e+1 by induction
    on the degree and then a degree-one morphism to PP^1; 199b5eb36b, the round's
    first commit, replaced it with Hou's part (b) -- dim|D| = n taken from his
    remark, the fixed points of |D| removed one at a time for d = n, and Exercise
    IV.1.5 for g(X) = 0, all on printed p. 10 -- and cited Egbert in the
    published-solution remark only; e4872b53d6 replaced Hou's step with the chain
    n <= dim|D| <= deg D = d <= n read off Exercise IV.1.5, marked as the card's
    own; and it is df9cd73f42 that made part (b) the transcription of Egbert's
    printed p. 220. So the 2026-09-18 proof was displaced at 199b5eb36b and what
    displaced it there was Hou's part (b), Egbert's chain only replacing Hou's at
    df9cd73f42. The same clause stands in this date's COMPLAINTS record, which is
    corrected in a record of this date and not rewritten. Read for this: the card
    at 199b5eb36b and at e4872b53d6, each read as a revision of this path, and the
    four commits named. Not read in this pass: Hou's and Egbert's text versions,
    whose pages are those of the events above, and no rendered text of this card
    changes.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the #121 reader's report of this round, in the rendered text only:
    four step references written as positions, in three paragraphs. Step
    #hyperplane-divisor closed with "injectivity of the restriction gives the
    inequality above and not completeness", where the inequality is the display in
    the same step: it now gives that inequality as dim|D| >= n. The same paragraph
    ended "is obtained in the next step from the degree bound", which is now step
    #strict-inequality, named by reference. Step #genus-zero said "the equality the
    previous step leaves", which is the equality step #strict-inequality leaves, and
    its closing paragraph said Egbert's sentence "is the identification the next
    step states", which is the identification step #is-rational-normal states. No
    mathematics changes and no step's claim changes; the three steps the references
    name are the ones that were meant, checked by reading what each states. Not done
    in this pass: no source was re-read, no step re-derived, and Hou's and Egbert's
    pages are those of the events above.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the #121 reader's report of this round: Hou's two published proofs
    in part (a), which the card did not transcribe, and the event of this date
    that misdescribed one of them.

    The event of this date above says that Hou's toric restatement "gives a
    monoid that is not the one of the d-uple embedding". That is false, and this
    event is its correction, the earlier event standing as written.
    $\ZZ^2\cap\sigma$ for $\sigma=\RR_{\ge0}\langle e_1,e_1+de_2\rangle$ is
    generated by $(1,0),(1,1),\ldots,(1,d)$, and $(x,y)\mapsto(dx-y,y)$ carries
    it onto the exponent monoid of $S(X)$, generated by $(d-i,i)$, with inverse
    $(u,v)\mapsto((u+v)/d,v)$ defined there because every generator has
    coordinate sum $d$; so $k[\ZZ^2\cap\sigma]\cong S(X)$ and Hou's argument is
    a proof of projective normality. The same claim stands in this date's
    COMPLAINTS record and is corrected in a new record of this date, not
    rewritten.

    Rendered changes. Step #projective-normality now transcribes Hou's toric
    argument, printed pp. 8--9, with the misprint named: he prints
    $\RR_{>0}$, which omits the origin and is not a cone, for $\RR_{\ge0}$. The
    card's own route from Exercise II.5.14(d) stays beside it, marked as the
    card's own, and the two false statements of his integral-closure argument
    stay named. Step #quadrics-generate now transcribes his division argument,
    printed p. 9, and names his false first observation where it occurs: the
    leading monomial of $g_{i-1,i}$ is $x_{i-1}x_{i+1}$, which divides no pure
    power, so $x_i^l$ survives the division; the argument does not need it,
    every remainder monomial $x_i^{n-k}x_{i+1}^k$ going to a distinct
    $t_0^{nd-ni-k}t_1^{ni+k}$. The card's own straightening proof is kept after
    it, marked as the card's own. Two slips of his printed displays are named in
    that step and used nowhere: $x_1^d$ for $x_d^n$, and $t_1^{r+k}$ for
    $t_1^{i+k}$. In step #degree-three the quotation reads "It is indeed the
    twisted cubic curve up to a projective transform", as he prints it, where an
    "and" had been inserted. The published-solution remark now names the toric
    cone and the misprint and says which two arguments the card carries.

    Where and how this pass read its source: Hou in
    tmp/sources/ntu-ag2-chapter4.md, the paragraph opening "Alternatively, we see
    that $V:=\Spec(k[t_0^d,\ldots,t_1^d])$" at line 292 of that file, which is
    printed p. 9, and the division argument from "Obviously, $g_{ij}\in
    \ker(\theta)$" at line 300, also printed p. 9, the printed folios being the
    PDF pages of tmp/sources/ntu-ag2-chapter4.pdf. Not read in this pass: the
    book's IV.3.4, Egbert and Reiser, whose pages and citations are those of the
    events above.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Correction of the event above, on checking the page: it says Hou "prints
    $\RR_{>0}$, which omits the origin and is not a cone, for $\RR_{\ge0}$". The
    page prints $\RR_{\ge0}$. The printed page 9 of
    tmp/sources/ntu-ag2-chapter4.pdf carries "the cone $\sigma:=\RR_{\ge0}\langle
    e_1,e_1+de_2\rangle\subset\RR^2$", the character after $R$ being the
    greater-or-equal sign, so $\RR_{>0}$ is a defect of the text version
    tmp/sources/ntu-ag2-chapter4.md, where the sign is lost, and not a misprint of
    Hou's. The event above stands as written and this event is its correction.
    Nothing of the mathematics changes: $\RR_{\ge0}$ is the cone the argument
    needs, $\ZZ^2\cap\sigma$ is generated by $(1,0),\ldots,(1,d)$, and the lattice
    map $(x,y)\mapsto(dx-y,y)$ carries it onto the exponent monoid of $S(X)$.

    The rendered card changes in three places, none of the mathematics. Step
    #projective-normality prints $\RR_{\ge0}$ and no longer carries the sentence
    about a misprint. The published-solution remark no longer calls the symbol a
    misprint. In step #quadrics-generate his first observation is quoted with
    $x_i^n$, which is what the page prints (printed p. 9: "contains no term like
    $x_i^n$"), where the text version renders it $x_i^l$; the observation is false
    either way, the remainder being homogeneous of degree $n$.

    Re-read on the page for this event, and not taken from the text version: the
    two slips of his display of $h_0$ and $h_{d-1}$ and of $\theta(r)=0$, which
    the page carries as $c_d^{(d-1)}x_1^d$ and $t_1^{r+k}$, so those two are his.
    Where: tmp/sources/ntu-ag2-chapter4.pdf, PDF page 9, whose printed folio is 9,
    the folio read in its own footer. Not read in this pass: any other page, and
    the book, Egbert and Reiser, whose pages are those of the events above.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the #121 reader's final recheck of this batch, limited to its four
    blocking findings on this card and their records.

    The card's own alternative proofs of the two halves of (a) are withdrawn
    because Hou prints proofs of both, on the same source-governs ground on which
    the card's own proof of (b) was withdrawn above. Step
    #surjective-restriction and the Exercise II.5.14(d) route in
    #projective-normality are removed, as is the straightening route in
    #quadrics-generate. The published toric and division arguments remain.

    The two expansions that remain inside those transcriptions now say that they
    are the card's own: the generation of $\ZZ^2\cap\sigma$ by $(1,i)$ with its
    decomposition and the lattice map with its inverse, which verify Hou's
    printed identification of $V$ with the affine toric variety of $\sigma$; and
    the distinct-exponent completion with pure powers included, which his false
    exclusion of them had omitted. The lattice calculation and the exponent
    calculation were checked by hand; no alternative proof is added.

    Correction of the event immediately above and of this date's COMPLAINTS
    record headed "The cone's inequality sign is the text version's loss": both
    say that the text version renders Hou's $x_i^n$ as $x_i^l$. That is false.
    Printed p. 9, observation (1), reads "$r$ contains no monomial of the form
    $-x_i^l$, for $i=1,\ldots,d-1$". His later sentence after the decomposition
    says that each $h_i$ "contains no term like $x_i^n$". The text version
    faithfully carries the first at line 302 and the second at line 312. Only its
    loss of the cone's greater-or-equal sign stands as an extraction defect.
    Step #quadrics-generate now distinguishes the two sentences and no longer
    paraphrases observation (1) with $x_i^n$. The earlier event and record stand
    as written, and a new COMPLAINTS record of this date carries the correction.

    The solution's opening no longer says that four of ten steps are the card's
    own: after the removals there are nine steps, one wholly the card's own and
    three transcriptions carrying expansions marked as the card's own. The pf-qed
    and the published-solution remark no longer name the withdrawn routes.

    Read for this repair: the whole card; Hartshorne IV.3.4 on printed p. 315
    (PDF p. 330) in tmp/sources/hartshorne-1977-algebraic-geometry.md at lines
    9855--9863; Hou's complete §3 Exercise 4 in
    tmp/sources/ntu-ag2-chapter4.md at lines 276--340, and printed pp. 8--10 of
    tmp/sources/ntu-ag2-chapter4.pdf, with observation (1), the later $x_i^n$
    sentence and $\RR_{\ge0}$ checked on printed p. 9. Not re-read in this pass:
    Egbert, Reiser and any source outside those two; their unchanged citations
    are those of the earlier events. No statement or part of (b) changes.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.3.4, printed p. 88,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.3.4, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed the chain $\ell(D)=n+1\leq\deg D+1=d+1\leq n+1$ at $d\le n$, and the step from $\ell(D)=\deg D+1$ to $g=0$.
    Not checked: Yang's Solutions outside printed p. 88; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.3.4 at printed
    p. 88 beside the entry already there. No step, statement or
    hypothesis of the card changes.
---

::: {.problem}
Let $X$ be the $d$-uple embedding (I, Ex.
2.12) of $\PP^1$ in $\PP^d$, for any $d \geq 1$.
We call $X$ the \dfn{rational normal curve} of degree $d$ in $\PP^d$.

(a) Show that $X$ is projectively normal, and that its homogeneous ideal can be generated by forms of degree 2.

(b) If $X$ is any curve of degree $d$ in $\PP^n$, with $d \leq n$, which is not contained in any $\PP^{n-1}$, show that in fact $d=n$, $g(X)=0$, and $X$ differs from the rational normal curve of degree $d$ only by an automorphism of $\PP^d$.
Cf.
(II, 7.8.5).

In particular, any curve of degree 2 in any $\PP^n$ is a conic in some $\PP^2$.

A curve of degree 3 in any $\PP^n$ must be either a plane cubic curve, or the twisted cubic curve in $\PP^3$.
:::

::: {.solution}
Each step names the published argument it transcribes, or says that it is the card's own. The transcription is Chin-Lung Wang's Algebraic Geometry II (National Taiwan University, 2020 Spring), Chapter IV homework, §3 Exercise 4 by Yu-Chi Hou — part (a) on printed pp. 8--9 and parts (b)--(d) on printed p. 10 — and, for the degree and the genus of part (b), A. Egbert's *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.4(b), printed p. 220. One of the nine steps is wholly the card's own, and three transcribed steps carry expansions marked as the card's own.

Write $S(X)=k[x_0,\ldots,x_d]/I(X)$ for the homogeneous coordinate ring of
$$
X=\nu_d(\PP^1)\subseteq\PP^d,
$$
graded so that $\deg x_i=1$, and write $\theta:k[x_0,\ldots,x_d]\to k[t_0,t_1]$ for the substitution $x_i\mapsto t_0^{d-i}t_1^i$, so that $I(X)=\ker\theta$ and $S(X)=k[t_0^d,t_0^{d-1}t_1,\ldots,t_1^d]$ (I, Ex. 2.12). The degree-$m$ part of $S(X)$ is the image of $H^0(\PP^d,\mco_{\PP^d}(m))$ and is $H^0(\PP^1,\mco_{\PP^1}(md))$.

::: pf

::: {.pf-step #projective-normality}

$X$ is projectively normal.

::: pf-proof

This step transcribes Hou, §3 Exercise 4(a), printed pp. 8--9, in the second of
his two arguments.

$S(X)=k[t_0^d,t_0^{d-1}t_1,\ldots,t_1^d]$ is the semigroup algebra of the monoid
$M\subseteq\ZZ^2$ generated by the exponent pairs of its monomials,
$$
(d-i,\,i),\qquad 0\le i\le d,
$$
and $V=\Spec S(X)$ is the affine cone over $X$, whose cone is Hou's:
$$
\sigma=\RR_{\ge0}\bigl\langle e_1,\,e_1+de_2\bigr\rangle\subset\RR^2.
$$
The generation of $\ZZ^2\cap\sigma$, its decomposition, and the lattice map
with its inverse below are the card's own verification of Hou's identification.
The cone $\sigma$
is strongly convex polyhedral, and $\ZZ^2\cap\sigma$ is generated by
$(1,0),(1,1),\ldots,(1,d)$: a lattice point $(x,y)$ of $\sigma$ has
$0\le y\le dx$, and writing $y=qd+r$ with $0\le r<d$ gives
$(x,y)=(x-q-1)(1,0)+(1,r)+q(1,d)$. The lattice map
$$
(x,y)\longmapsto(dx-y,\,y)
$$
carries $(1,i)$ to $(d-i,i)$, hence carries $\ZZ^2\cap\sigma$ onto $M$, and its
inverse $(u,v)\mapsto\bigl((u+v)/d,\,v\bigr)$ is defined on $M$, every generator
of $M$ having coordinate sum $d$. So $k[\ZZ^2\cap\sigma]\cong S(X)$, and $V$ is
the affine toric variety of $\sigma$. A monoid cut out in $\ZZ^2$ by a strongly
convex polyhedral cone is saturated, and the algebra of a saturated monoid is
integrally closed in its fraction field; hence $k[\ZZ^2\cap\sigma]$ is normal and
$V$ is normal. Hou's closing sentence is the definition: an affine cone over a
projective variety is normal exactly when the variety is projectively normal.
So $X$ is projectively normal.

Hou's other argument at the same place, integral closedness of $S(X)$ through the
equation $f^n+a_{n-1}f^{n-1}+\cdots+a_0=0$, has two false statements in it. He
takes $\Frac S(X)=k(t_0,t_1)$; but $\Frac S(X)$ consists of the ratios of forms
of $t$-degree divisible by $d$, and for $d\ge2$ that is a proper subfield of
$k(t_0,t_1)$, the element $t_0$ not being such a ratio. He then concludes from
that equation that $d\mid\deg f$ for $f\in k[t_0,t_1]$ integral over $S(X)$, and
that is false: for $d=2$ the element $t_0$ is integral over
$S(X)=k[t_0^2,t_0t_1,t_1^2]$, being a root of $T^2-t_0^2$, while $\deg t_0=1$
is not divisible by $2$. Neither statement is used in this proof.

:::

:::

::: {.pf-step #quadrics-vanish}

For $0\le i<j\le d-1$ the quadric
$$
g_{ij}=x_ix_{j+1}-x_{i+1}x_j
$$
vanishes on $X$.

::: pf-proof

Hou, §3 Exercise 4(a), printed p. 9: "obviously $g_{ij}\in\ker(\theta)$". Under
$x_i\mapsto t_0^{d-i}t_1^i$ both $x_ix_{j+1}$ and $x_{i+1}x_j$ map to
$t_0^{2d-i-j-1}t_1^{i+j+1}$.

:::

:::

::: {.pf-step #quadrics-generate}

The $g_{ij}$ generate $I(X)$.

::: pf-proof

This step transcribes Hou, §3 Exercise 4(a), printed p. 9. His false exclusion
of pure powers is named, and the completion with pure powers included is marked
as the card's own.

Let $J$ be the ideal generated by the $g_{ij}$, so that $J\subseteq I(X)$ by step
[](#quadrics-vanish){.pf-ref}. For $f\in I(X)$ homogeneous of degree $n$, divide
by the $g_{ij}$ in the lexicographic order $x_0>x_1>\cdots>x_d$, getting
$r=f-\sum_{i<j}a_{ij}g_{ij}$; equating degrees makes $r$ homogeneous of degree
$n$, and $r\in I(X)$. His second observation: the leading monomial of
$g_{i,j-1}=x_ix_j-x_{i+1}x_{j-1}$ is $x_ix_j$, so a remainder carries no monomial
in which two indices differ by at least $2$, and is therefore a sum
$$
r=h_0(x_0,x_1)+h_1(x_1,x_2)+\cdots+h_{d-1}(x_{d-1},x_d)
$$
with each $h_i$ homogeneous of degree $n$. His observation (1) says that $r$
contains no monomial of the form $-x_i^l$ for $1\le i\le d-1$; after giving the
decomposition he separately writes that each $h_i$ contains no term like $x_i^n$.
Both sentences exclude pure powers, and that exclusion is false: the leading
monomial of $g_{i-1,i}=x_{i-1}x_{i+1}-x_i^2$ is $x_{i-1}x_{i+1}$, which divides
no pure power, so $x_i^n$ survives the division. The following completion of his
argument with pure powers included is the card's own. Every monomial of $r$ is
$$
x_i^{\,n-k}x_{i+1}^{\,k},\qquad 0\le i\le d-1,\quad 0\le k\le n,
$$
pure powers included, and $\theta$ carries it to
$$
t_0^{\,nd-ni-k}\,t_1^{\,ni+k}.
$$
Distinct such monomials have distinct exponent pairs: the two exponents sum to
$nd$, so $ni+k$ is recovered from the pair, and $ni+k$ recovers $i$ and $k$,
except that a pure power $x_j^n$ is written twice, as $(i,k)=(j,0)$ and as
$(j-1,n)$, with the same monomial and the same image either way. Hence
$\theta(r)=0$ forces $r=0$, that is $f\in J$. (His printed display of $h_0$ and
$h_{d-1}$ closes with $x_1^d$ where $x_d^n$ is meant, and his display of
$\theta(r)=0$ carries $t_1^{r+k}$ where $t_1^{i+k}$ is meant; neither is used.)

:::

:::

::: {.pf-step #hyperplane-divisor}

Let $X\subseteq\PP^n$ be a curve of degree $d$ not contained in any hyperplane,
and let $H$ be a hyperplane with $D=X.H$. Then
$$
\deg D=d,
\qquad
\dim\abs{D}\ge n.
$$

::: pf-proof

This step is the card's own. $\deg D=\deg(X.H)=\deg X=d$. The restriction
$H^0(\PP^n,\mco_{\PP^n}(1))\to H^0(X,\mco_X(1))$ is injective because no nonzero
linear form vanishes on $X$, so the hyperplane divisors cut on $X$ span an
$(n+1)$-dimensional subspace of $H^0(X,\mco_X(1))$ and
$$
\dim\abs{D}=h^0(X,\mco_X(1))-1\ge n.
$$
Hou, §3 Exercise 4(b), printed p. 10, states $\dim\abs{D}=n$ and justifies it by
the remark that otherwise "there exists a proper subspace
$V\subset h^0(X,\mco_X(D))$ such that $X\subset\PP(V^*)\subsetneq\PP^n$";
injectivity of the restriction gives $\dim\abs{D}\ge n$ and not completeness,
so the equality is not established by that remark and is obtained in step
[](#strict-inequality){.pf-ref} from the degree bound.

:::

:::

::: {.pf-step #strict-inequality}

For a curve of degree $d\le n$ in $\PP^n$ not contained in any hyperplane,
$$
d=n.
$$

::: pf-proof

This step transcribes A. Egbert, *Solutions to Hartshorne's Algebraic Geometry*
(2013), IV.3.4(b), printed p. 220: "We have
$\dim\abs{D}=n$, $\deg(D)=d$ and
$l(D)=n+1\le\deg(D)+1=d+1\le n+1$. Thus $n=d$." With step
[](#hyperplane-divisor){.pf-ref}, $d\le n$ is his last inequality and his
$l(D)\le\deg(D)+1$ is [[P-AGH415DIMLEQDEG|Exercise IV.1.5]] applied to $D$,
which reads $\dim\abs{D}\le\deg D$, with $l(D)=\dim\abs{D}+1$.

The equality he opens with is what the hypotheses give as an inequality:
$H^0(\PP^n,\mco_{\PP^n}(1))\to H^0(X,\mco_X(1))$ is injective because $X$ lies
in no hyperplane (step [](#hyperplane-divisor){.pf-ref}), so $l(D)\ge n+1$.
Read that way his chain is $n+1\le l(D)\le d+1\le n+1$ and yields the same
conclusion; printed with $l(D)=n+1$ first, as he writes it, the line asserts
what it proves. Hou, §3 Exercise 4(b), printed p. 10, writes the same equality
for the same inequality, which step [](#hyperplane-divisor){.pf-ref} names.

Hou's own route to $d=n$, §3 Exercise 4(b), printed p. 10, removes the fixed
points of $\abs{D}$ one at a time, reaching
$\dim\abs{D-P_1-\cdots-P_d}=n-d>0$ against degree $0$; that is a contradiction
only if $\dim\abs{D}=n$, which his remark there does not establish.

:::

:::

::: {.pf-step #genus-zero}

Under the hypotheses of step [](#hyperplane-divisor){.pf-ref},
$$
h^0(X,\mco_X(1))=n+1,
\qquad
g(X)=0.
$$

::: pf-proof

This step transcribes Egbert, IV.3.4(b), printed p. 220, who continues:
"Since $\deg(D)=\dim(D)$, and $d\ne0$, then by exc IV.1.5, $g=0$." Step
[](#strict-inequality){.pf-ref} gives $d=n$ and its chain gives $l(D)=n+1$, so
$\dim\abs{D}=n=\deg D$ with $D\ne0$; that is the equality case of
[[P-AGH415DIMLEQDEG|Exercise IV.1.5]], whence $g(X)=0$, and
$h^0(X,\mco_X(1))=l(D)=n+1$. His "$\deg(D)=\dim(D)$" compares the degree of $D$
with the dimension of the linear system, and what the citation needs is
$\deg D=\dim\abs{D}$, the equality step [](#strict-inequality){.pf-ref} leaves.

He closes, "Thus $D$ corresponds to an $(n+1)$ dimensional subspace in
$\Gamma(\PP^1,\mco(n))$", which is the identification step
[](#is-rational-normal){.pf-ref} states, and
Hou, §3 Exercise 4(b), printed p. 10, states both conclusions as well: "we then
must have $g(X)=0$ and $\mco_X(H)=\mco_{\PP^1}(dH)$".

:::

:::

::: {.pf-step #is-rational-normal}

The embedding of step [](#hyperplane-divisor){.pf-ref} is the $d$-uple embedding
of $\PP^1$, up to an automorphism of $\PP^d$.

::: pf-proof

Hou, §3 Exercise 4(b), printed p. 10: "Therefore $X\cong\nu_d(\PP^1)$ up to
$\Aut(\PP^n)$." The following expansion of that sentence is the card's own.
$g(X)=0$ forces $X\cong\PP^1$ (IV.1.3.5); on $\PP^1$ a divisor of degree $d$ is
linearly equivalent to $dP$ for a point $P$, so
$\mco_X(1)=\mco_X(H)\cong\mco_{\PP^1}(d)$ and $\abs{D}$ is the complete system
$\abs{dP}$; by step
[](#genus-zero){.pf-ref} the restriction
$H^0(\PP^d,\mco_{\PP^d}(1))\to H^0(X,\mco_X(1))$ is injective between spaces of
dimension $d+1$, hence an isomorphism, so the given embedding is the one defined
by the complete system $\abs{\mco_{\PP^1}(d)}$ and differs from $\nu_d$ only by
the choice of a basis of that space, that is, by an element of
$\PGL_{d+1}(k)=\Aut\PP^d$.

:::

:::

::: {.pf-step #degree-two}

A curve of degree $2$ in any $\PP^n$ is a conic in some $\PP^2$.

::: pf-proof

Hou, §3 Exercise 4(c), printed p. 10: if $X$ is not contained in any hyperplane,
then $n=2$ by part (b) as proved in steps
[](#hyperplane-divisor){.pf-ref}--[](#is-rational-normal){.pf-ref}; if a
hyperplane $H\cong\PP^{n-1}$ contains $X$, replace $n$ by $n-1$ and repeat. So
$X$ is a plane curve of degree $2$, that is, a conic in $\PP^2$.

:::

:::

::: {.pf-step #degree-three}

A curve of degree $3$ in any $\PP^n$ is either a plane cubic or the twisted
cubic in $\PP^3$.

::: pf-proof

Hou, §3 Exercise 4(d), printed p. 10: the descent of step
[](#degree-two){.pf-ref} shows $X\subseteq\PP^3$. If $X$ is not contained in any
plane, then $X\cong\nu_3(\PP^1)$ by part (b), "It is indeed the twisted
cubic curve up to a projective transform"; if $X$ lies in a plane, it is a plane
curve of degree $3$, hence a plane cubic. By [[P-AGH212DUPLE|Exercise I.2.12(d)]]
the image of $\nu_3$ is the twisted cubic.

:::

:::

::: pf-qed

Steps [](#projective-normality){.pf-ref}, [](#quadrics-vanish){.pf-ref} and
[](#quadrics-generate){.pf-ref} prove part
(a), steps [](#hyperplane-divisor){.pf-ref}, [](#strict-inequality){.pf-ref},
[](#genus-zero){.pf-ref} and [](#is-rational-normal){.pf-ref} prove part (b), and
steps [](#degree-two){.pf-ref} and [](#degree-three){.pf-ref} prove its two
consequences.

:::

:::

:::


::: {.remark title="Published solution"}
Chin-Lung Wang's Algebraic Geometry II (National Taiwan University, 2020 Spring), Chapter IV homework, §3 Exercise 4 by Yu-Chi Hou, printed pp. 8--10, solves the exercise: (a) at pp. 8--9, by the toric argument that $\Spec S(X)$ is the affine toric variety of the cone $\sigma=\RR_{\ge0}\langle e_1,e_1+de_2\rangle$, whose monoid $\ZZ^2\cap\sigma$ is isomorphic to the exponent monoid of $S(X)$ and is saturated, and by division of the ideal by the quadrics $g_{ij}$, and (b) with its degree-$2$ and degree-$3$ consequences at p. 10. Three statements of its part (a) are false and are named where they would otherwise be used: $\Frac S(X)=k(t_0,t_1)$, the conclusion $d\mid\deg f$ drawn from a degree comparison (for $d=2$, $t_0$ is integral over $S(X)$ and has degree $1$), and the claim that a lexicographic remainder by the $g_{ij}$ contains no pure power $x_i^n$, whose leading monomial under $g_{i-1,i}$ is $x_{i-1}x_{i+1}$. Its part (b) states $g(X)=0$ and the identification with the $d$-uple embedding, and states $\dim\abs{D}=n$ without proving it. The card carries both of Hou's arguments in (a), with his false first observation named, and takes part (b)'s degree and genus from Egbert's solutions of the same exercise, printed p. 220, with Exercise IV.1.5 for the bound that chain uses and IV.1.3.5, an Example of the text, for $X\cong\PP^1$.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.4, printed pp. 219--220, asserts both halves of part (a) without proof on printed p. 219 — "Since $\PP^1$ is projectively normal, then $d$-uple is projectively normal. If $\theta$ is the corresponding ring homomorphism, then the kernel is generated by quadrics" — and proves part (b) on printed p. 220 by the chain $l(D)=n+1\le\deg(D)+1=d+1\le n+1$ and Exercise IV.1.5, with the identification in the one closing sentence quoted in step [](#genus-zero){.pf-ref}.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.3.4, printed p. 88, does (a) by pulling projective normality back along the embedding: $\PP^1$ is projectively normal and the $d$-uple embedding is projectively normal (2.5.14), so the rational normal curve of degree $d$ in $\PP^d$ is projectively normal, and the kernel of its homogeneous coordinate ring is generated by the quadrics $x_ix_j-x_kx_l$ with $i+j=k+l$. Part (b) is the four-term chain: for $D=X.H$ one has $\dim\abs D=n$ and $\deg D=d$, so $\ell(D)=n+1\leq\deg D+1=d+1\leq n+1$, the first inequality being (4.1.5) and the second the exercise's hypothesis $d\leq n$. Hence $d=n$ and $\ell(D)=\deg D+1$; the entry reads $g(X)=0$ off that by (4.1.5), and the reading is right, since Riemann--Roch turns $\ell(D)=\deg D+1$ into $\ell(K-D)=g$, which no nonzero effective $D$ satisfies when $g\geq1$ --- $\abs K$ is base-point-free for $g\geq2$, and $\ell(-D)=0$ for $g=1$. With $X$ in no $\PP^{n-1}$ the restriction $H^0(\PP^n,\OO(1))\to H^0(X,\OO_X(1))$ is injective, and both sides now have dimension $n+1$, so $X\to\PP^n$ is induced by the complete linear system $\abs{\OO_{\PP^1}(n)}$ --- the rational normal curve of degree $n=d$, up to an automorphism of $\PP^d$.
:::
