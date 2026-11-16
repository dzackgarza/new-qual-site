---
schema: qual/card@1
id: P-AGH3117NONALGSHEAF
kind: problem
title: A nonalgebraizable invertible sheaf on a formal completion of the plane
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Functions
  - Formal Schemes
  - Picard Group
  - Plane Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.11.7 together with II.9.9.1 and the preceding Exercises
    III.11.5--11.6. The square-zero Picard sequence was cross-checked against
    Stacks Project Tag 0C6R. The source's assertion that the kernel is a
    k-vector space needs a characteristic-zero hypothesis: in characteristic
    p the multiplicative formal group need not be additive. The solution
    proves the correct arbitrary-characteristic filtration, proves the stated
    vector-space assertion in characteristic zero using the I-adic logarithm,
    and gives an explicit positive-characteristic counterexample on a line in
    P^2. Parts (b) and (c) are then proved in arbitrary characteristic.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-09
  note: 'Read III.11.7 against Hartshorne p. 281 and Dongryul Kim, Solutions to Hartshorne, p. 213. Steps s1-s5, s7 and s8 check out. Repaired step s6: its positive-characteristic argument claimed that the first nonzero Cech term of the transition function of L^p must be a coboundary, which does not exclude the cross terms of the formal units. Step s6 now compares coefficients in the two formal charts Spf k[t][[s]] and Spf k[t^{-1}][[s/t]] and shows that no power u^m of u = 1 + z^2/(xy) is a coboundary, so the class of L has infinite order in the kernel. Against Kim: his 11.7(a) asserts without proof that the kernel is a k-vector space and computes only H^2 vanishing and surjectivity; his remark that the k-vector-space structure is the inverse limit of k-vector spaces is the assertion under discussion.'
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    Second step-by-step pass. Checked s1 (H^0(X_r)=k), s2 (the square-zero
    Picard sequence and H^2(O_Y(-rd))=0), s3 (Pic Xhat = lim Pic X_r and
    K_r/K_{r+1} = V_r, the transition maps being surjective), s4 (dim V_r =
    r d^2 + d(d-3)/2 from the hypersurface sequence and h^2(P^2,O(-m)) =
    C(m-1,2)), s5 (char 0: log and exp identify 1+Ihat with Ihat, so K is a
    k-vector space with the infinite descending chain of subspaces K_r), and
    s7. Corrected s6: its coefficient comparison was written for 1 +
    s^{2m}/t^m, which equals u^m only for m a power of p; the step now
    reduces to m = p^a first (if u^M = A/B then u^{p^a M} = A^{p^a}/B^{p^a})
    and then runs the same comparison, and the sentence after it was
    adjusted to say so. The characteristic-p conclusion is unchanged and is
    the one recorded: the kernel is a filtered formal group with infinite-
    dimensional successive quotients, and it is not a k-vector space when
    char k = p.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second published-solution search for III.11.7(a) (issue #121); no
    complete published argument for the printed claim was located, and none
    can exist, since the claim is false in characteristic p. Read this
    pass: Yang Pi-Yeh, Hartshorne Solutions (9 June 2019), Solution 3.11.7,
    printed p. 82 of tmp/sources/lfwin-hartshorne-solutions.pdf, text
    version tmp/sources/lfwin-hartshorne-solutions.md. He writes the kernel
    as the inverse limit of the completions of the graded pieces and calls
    it "hence infinite dimensional", which is the same step the card
    records as false in characteristic p, and he does not identify the
    successive kernels with H^1(Y, O_Y(-nd)) either. Stack Exchange API
    searches for the exercise on site=math and site=mathoverflow
    (/search/advanced with the exercise's own phrases) returned nothing;
    the only Stack Exchange item the earlier pass found, question 4667761
    on III.11.5, computes the successive kernels of the H^1 terms and says
    nothing about the vector-space structure. Checked against the book in
    this pass: the printed exercise on printed p. 281, and Exercise II.9.6
    which it invokes. Not checked: nothing new; the card's own
    characteristic-p counterexample was not re-derived in this pass.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on the reader's report of this batch. Step s6's reduction is
    rewritten: a general exponent is written m = p^b m' with p not dividing
    m', the freshman's dream gives u^m = (1 + s^{2p^b}/t^{p^b})^{m'}, and
    the coefficient comparison is now made at s^{2p^b}, where the term
    m' t^{-p^b} has m' nonzero in k; the comparison at s^{2p^b} against
    t^{-2p^b}k[t^{-1}] is a contradiction. The earlier step excluded only
    the powers m = p^a and then asserted the general case, which its
    displayed identity does not give. Step s5 now says why the chain
    K = K_1 > K_2 > ... is a chain of k-subspaces: K_r is the image of
    H^1(Xhat, Ihat^r) under the logarithm. Corrected on the audit trail:
    the 2026-11-11 note's description of the reduction, the 2026-11-16
    note's description of Yang's argument, and the remark's citation of
    Kim, which now names its text version. Checked against the book:
    III.11.7 on printed p. 281, Exercise II.9.6. Not checked: nothing new
    in the characteristic-p example beyond the rewritten exponent, which
    was recalculated rather than machine-checked.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass on the reader's report of this batch. The mathematics of
    steps s5 and s6 was re-derived and stands: with b_j = 0 for 0 < j < 2q
    the coefficient of s^{2q} in B u^m is b_{2q} t^{-2q} + m' t^{-q}, and
    m' is nonzero in k because p does not divide m', so the comparison is a
    contradiction. No change is made to the proof. Restored, as the report
    asks, the two event descriptions the previous pass had rewritten in
    place: the note of 2026-11-11 reads again as written, without a
    2026-11-16 judgement spliced into it and without its reference to "the
    event of 2026-11-16 below", and the note of 2026-11-16 again carries the
    description of Yang's argument that was written on that date. The
    corrections those passages now lack are made here: the reduction to the
    exponents m = p^a recorded in the earlier note excludes nothing, as the
    later note says, and Yang writes the successive kernels as
    k[x_0,x_1,x_2]/(f^{n-1}), takes their projective limit, identifies it
    with the completion of k[x_0,x_1,x_2] at (f) and calls that "hence
    infinite dimensional", which is the k-vector-space inference the card
    records as false in characteristic p. Checked against the book in this
    pass: III.11.7 on printed p. 281 and Exercise II.9.6. Not checked:
    nothing new beyond those two re-derivations.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass on the reader's report of this batch, on the audit trail only.
    The solution-reviewed event of 2026-11-16 whose note begins "Repairs on
    the reader's report of this batch" is restored as it was written, and this
    event is appended after it rather than put in its place; the reference in
    the event above to the event "of 2026-11-16 above" whose note begins
    "Repairs on the reader's report" therefore has its referent again. The
    mathematics and the source descriptions stand as that event and the event
    above it record them, and the note of 2026-11-11 keeps the text it was
    written with. Checked in this pass: nothing new; no step was re-derived.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass, on the audit trail and the rule that a dated event is never
    edited. The event above whose note begins "Second pass on the reader's
    report of this batch" was extended in place by commit 15a20526df, which
    added that the pages it cites were read in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N is
    PDF p. N+15. It is restored as it was written in 1abd969bbb, and the
    addition is stated here. Checked in this pass: this card's audit trail in
    git, commit by commit. Not checked: no step was re-derived, and the pages
    named were not re-read.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcription pass for issue #121. Read at the cited places: Dongryul
    Kim, Exercise 3.11.7, PDF p. 213, text version
    tmp/sources/hartshorne-solutions-kim.md, and Yang Pi-Yeh, Solution
    3.11.7, printed p. 82, text version tmp/sources/lfwin-hartshorne-solutions.md;
    the latter was read in the PDF at the page named, since it is the page
    the earlier passes cite. Checked against the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N
    is PDF p. N+15: III.11.7(a) as printed on p. 281, and Exercise II.9.6
    which it invokes. What the pass establishes. Kim proves, and Yang
    repeats, the inverse limit Pic Xhat = lim Pic X_n from Exercise II.9.6,
    the exact sequence of Exercise III.4.6, the vanishing of its H^2 term
    on a curve, the surjectivity of Pic Xhat -> Pic Y, and the
    identification of the successive kernels with H^1(X_n, I^{n-1}); Kim
    gives them as the first cohomology of a coherent sheaf, Yang as
    k[x_0,x_1,x_2]/(f^{n-1}) and its projective limit. Neither proves the
    printed claim that the kernel is a k-vector space: Kim's parenthesis
    says the kernel "is the inverse limit of k-vector spaces, hence is a
    k-vector space", which is the assertion under proof and fails when the
    transitions are not linear, and Yang reads it off a completion. On the
    card, the steps that transcribe those two are s2, s3, s4, s7 and s8
    with the source named at each; the dimension count of s4, the
    identification K_r over K_{r+1} = V_r in s3, the characteristic-zero
    logarithm of s5, the characteristic-p counterexample of s6 and the
    passage from one non-generated twist to none in s8 are marked on the
    card as the card's own, and the 2026-11-16 COMPLAINTS record names the
    part of the printed statement that has no published proof. Not
    checked: no source outside the two named was searched in this pass,
    and no step was re-derived.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on the rule that a dated event is never
    edited. The event of 2026-11-16 above whose note begins "Transcription
    pass for issue #121" was rewritten in place by commit 181d588a15, and it
    is restored to the text it carried when written in 91eb357555; what that
    text says that does not hold is corrected here, and the two passages of
    the solution that said it with it. (i) Yang Pi-Yeh's equation for the
    successive kernels, H^1(X_n, I^{n-1}) = k[x_0,x_1,x_2]/(f^{n-1}), does
    not hold, and the restored event reads it as an identification of them.
    The left side is H^1(Y, O_Y(-(n-1)d)) by I^{n-1}/I^n = O_Y(-(n-1)d),
    a cohomology group of a coherent sheaf on the curve and finite
    dimensional over k; the right side is a ring with classes in every
    degree. Step s4 now says so, as the event of even date on this card
    already did. (ii) The card nowhere identifies the kernel of
    Pic Xhat -> Pic Y with the completion of k[x_0,x_1,x_2] at (f), and
    the solution said in step s4 that what is infinite dimensional is "the
    projective limit of the successive kernels, which is the completion he
    names". That identification is Yang's and is not proved here; the
    sentence is withdrawn, and step s4 now states what the card does prove,
    that dim_k V_r grows with r for V_r = K_r/K_{r+1}. (iii) The head of the
    solution said that Yang "writes the same argument and identifies the
    successive kernels", which read the false equation as a result; it now
    states what he writes and names step s4 for the failure. Checked against
    the book in tmp/sources/hartshorne-1977-algebraic-geometry.md (printed
    p. N is PDF p. N+15): III.11.7(a) on printed p. 281 and Exercise II.9.6,
    which it invokes; Yang's text was re-read in
    tmp/sources/lfwin-hartshorne-solutions.md at the passage quoted. Not
    checked: no other source was read in this pass, and steps s5 and s6 were
    not re-derived.

- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on the rendered card and on nothing else.
    Three places said what had been read rather than what the mathematics is:
    the opening sentence of step s5's proof, "No source read for this card
    proves this step"; the opening sentence of step s6's proof, "No source read
    for this card states or proves the failure in positive characteristic"; and
    the closing sentence of the remark, "no published source read here gives
    it". Each now carries the mark that the step is the card's own, which is
    what the reader's report asks for, and the description of what Kim and Yang
    do, and of what their arguments leave unproved, is kept as it stood. No
    mathematics changes: s5 and s6 are the card's own, as the events of even
    date above record and as the steps now say. Where and how the sources were
    read stays in those events, among them
    tmp/sources/lfwin-hartshorne-solutions.md for Yang and
    tmp/sources/hartshorne-solutions-kim.md for Kim, and it does not appear on
    the page. Not checked: no step was re-derived, no source was re-read, and no
    machine computation was run in this pass.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on the rendered card only, and the item the
    two passes above left: the head of the solution and the remark on the
    published solution still named the text versions of Kim and of Yang Pi-Yeh,
    tmp/sources/hartshorne-solutions-kim.md and
    tmp/sources/lfwin-hartshorne-solutions.md, beside the citations they
    support. Both passages now cite Kim by exercise, PDF page and source
    revision and Yang by solution and printed page, and neither names a file.
    What was read, and where, is in the transcription event of even date and in
    the events above, which keep their paths (PROSE-11, QUAL-08, SEC-7). No
    mathematics changes: the description of what Kim and Yang do, and of the
    step neither proves, stands word for word. Read in this pass: the two
    rendered sentences only; no source was reopened and no step was re-derived.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, four items. (i) QUAL-01: part (a) carried
    the printed claim that the kernel is an infinite-dimensional $k$-vector
    space with no hypothesis on $k$, which step s6 shows false in
    characteristic $p$. The printed text is "Use the method of (Ex. 11.5) to
    show that Pic \hat X \to Pic Y is surjective, and its kernel is an
    infinite-dimensional vector space over k", on printed p. 281; part (a) now
    reads that in characteristic $0$ the kernel is an infinite-dimensional
    vector space over $k$. The surjectivity is asked for in every
    characteristic, as it holds, and parts (b) and (c) are untouched. (ii)
    Kim's false step. The card reported his claim that Exercise III.4.6 holds
    for a nilpotent ideal "because (1+a)^{-1} = 1 - a + a^2 - \cdots" without
    saying that it is false, and it put the failure of his argument elsewhere,
    in "an inverse limit of k-vector spaces with non-linear transition maps",
    here and in the remark. Under his claim those transitions would be linear,
    so the failure is his nilpotent extension of III.4.6, and step s2 now says
    why: the geometric series is finite only when $a^2=0$, $a\mapsto1+a$ is not
    additive, $(1+a)(1+b)=1+a+b+ab$, and $(1+a)^p=1+a^p\ne1$ in characteristic
    $p$ while the additive group of a $k$-vector space is killed by $p$. The
    head of the solution and the published-solution remark now name that step
    as the false one and say that the inference from the kernels of
    $\Pic Y_n\to\Pic Y_1$ to the inverse limit would be valid on it. (iii)
    Yang's sequence. The head, step s3 and the remark said that he writes the
    same inverse limit and the same exact sequence as Kim. He does not: he
    writes $H^1(X_n,\mci^{n-1})\to\Pic X_n\to\Pic X_1\to
    H^2(X_n,\mci^{n-1})$, whose outer terms join $X_n$ to $X_1$ where those of
    III.4.6 join $X_n$ to $X_{n-1}$, and it is not exact in the middle for
    $n\ge3$, his left term being $V_{n-1}=\ker(\Pic X_n\to\Pic X_{n-1})$. Step
    s3 now states his sequence, proves that, and keeps his conclusion and the
    fact it really rests on. (iv) Kim's sentence in step s3 stopped at
    $Y_{n+1}$; it is now quoted through "and the ways of lifting is given by a
    nonzero $k$-vector space for large enough $n$". Checked against the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N is
    PDF p. N+15: III.11.7 on printed p. 281, its text standing between the
    markers of PDF pages 296 and 297. Read in this pass: Kim's Exercise 3.11.7,
    statement and Solution (a)--(c), in
    tmp/sources/dongryul-kim-hartshorne-solutions.md at line 9067 and the
    paragraphs after it, PDF p. 213, whose parenthesis on III.4.6 and the
    geometric series is quoted above in its own words; and Yang Pi-Yeh's
    Solution 3.11.7 in tmp/sources/lfwin-hartshorne-solutions.md at line 2138,
    printed p. 82, whose sequence and closing sentence are quoted as they
    stand there. Not checked: the printed pages were not in hand, the book,
    Kim and Yang being read in the three text versions named; Kim's page and
    Yang's page were not recollated against their PDFs in this pass; and no
    step beyond s2, s3 and the pf-qed's wording was re-derived.
---

::: {.problem}
Now let $Y$ be a curve in $X = \PP_k^2$, and let $\hat{X}$ be the formal completion of $X$ along $Y$.

(a) Use the method of (Ex.
11.5) to show that $\Pic \hat{X} \to \Pic Y$ is surjective, and that in characteristic $0$ its kernel is an infinite-dimensional vector space over $k$.

(b) Conclude that there is an invertible sheaf $\mcl$ on $\hat{X}$ which is not algebraizable.

(c) Conclude also that there is a locally free sheaf $\mcf$ on $\hat{X}$ such that no twist $\mcf(n)$ is generated by global sections.
Cf.
(II, 9.9.1).
:::

::: {.solution}
Let
$$
d=\deg Y,
\qquad
\mci=\mci_Y\cong\mco_X(-d),
$$
and for $r\ge1$ put
$$
X_r=\bigl(Y,\mco_X/\mci^r\bigr).
$$
Thus $X_1=Y$ and $\hat X=\varprojlim_rX_r$.

There is one characteristic issue in part (a). The successive kernels below are always finite-dimensional $k$-vector spaces, and they make the kernel of $\Pic\hat X\to\Pic Y$ an infinite-dimensional filtered formal group.
If $\operatorname{char}k=0$, the $I$-adic logarithm identifies that formal group with an additive $k$-vector space, giving the assertion in the source literally.
In positive characteristic the assertion that the *group itself* is a $k$-vector space is false; step [](#s6){.pf-ref} gives an explicit counterexample.
The surjectivity in (a), and all of (b)--(c), hold in every characteristic.

Neither source proves the printed claim of the exercise, that the kernel is a $k$-vector space.  Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Exercise 3.11.7, PDF p. 213, gives $\Pic\hat X=\varprojlim_n\Pic X_n$, the exact sequence of Exercise III.4.6, the vanishing of its $H^2$ term and the growth of its $H^1$ term, and hence the surjectivity of $\Pic\hat X\to\Pic Y$; the vector-space structure he argues for in a parenthesis, in two steps, that the kernel of $\Pic Y_n\to\Pic Y_1$ is the first cohomology of a coherent $\OO_Y$-module and that the kernel of $\Pic\hat X\to\Pic Y$, being an inverse limit of $k$-vector spaces, is one.  The second step is valid on the first, and the first is false: Exercise III.4.6 is a statement about a square-zero thickening, and step [](#s2){.pf-ref} says what fails when the ideal is only nilpotent.  Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 3.11.7, printed p. 82, writes the same inverse limit, and then a sequence joining $\Pic X_n$ to $\Pic X_1$ rather than to $\Pic X_{n-1}$; it is neither Kim's sequence nor a true one, as step [](#s3){.pf-ref} shows, and his equation for the successive kernels, $H^1(X_n,\mci^{n-1})=k[x_0,x_1,x_2]/(f^{n-1})$, does not hold either, as step [](#s4){.pf-ref} shows.  The characteristic-free statement is the filtered one of steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}; steps [](#s5){.pf-ref} and [](#s6){.pf-ref} are proved here and not transcribed.

::: pf

::: {.pf-step #s1}
For every $r\ge1$,
$$
H^0(X_r,\mco_{X_r})=k.
$$

::: pf-proof
Since $Y$ is an integral projective curve over the algebraically closed field $k$,
$$
H^0(Y,\mco_Y)=k.
$$
For $r\ge2$ there is an exact sequence
$$
0
\longrightarrow
\mci^{r-1}/\mci^r
\longrightarrow
\mco_{X_r}
\longrightarrow
\mco_{X_{r-1}}
\longrightarrow0.
$$
Because $Y$ is a hypersurface of degree $d$,
$$
\mci^{r-1}/\mci^r
\cong
\mco_Y(-(r-1)d).
$$
This line bundle has negative degree
$$
-(r-1)d^2<0,
$$
so it has no nonzero global section.
Hence
$$
H^0(X_r,\mco_{X_r})
\hookrightarrow
H^0(X_{r-1},\mco_{X_{r-1}}).
$$
The constants give a copy of $k$ in every term, so induction from $X_1=Y$ forces equality with $k$ at every stage.
:::

:::

::: {.pf-step #s2}
For every $r\ge1$ there is a short exact sequence of abelian groups
$$
0
\longrightarrow
V_r
\longrightarrow
\Pic X_{r+1}
\longrightarrow
\Pic X_r
\longrightarrow0,
\qquad
V_r\coloneqq H^1\bigl(Y,\mco_Y(-rd)\bigr).
$$

::: pf-proof
The immersion
$$
X_r\hookrightarrow X_{r+1}
$$
is a square-zero thickening whose ideal is
$$
\mci^r/\mci^{r+1}
\cong
\mco_Y(-rd).
$$
Kim, Exercise 3.11.7(a), PDF p. 213, writes this sequence as the one of Exercise III.4.6,
$$
H^1\bigl(Y,\OO_Y(-dn)\bigr)\longrightarrow\Pic X_{n+1}\longrightarrow\Pic X_n\longrightarrow H^2\bigl(Y,\OO_Y(-dn)\bigr),
$$
and reads off from $H^2=0$ that every class on $X_n$ lifts to $X_{n+1}$.  The Picard sequence for a square-zero thickening ([Stacks Project, Tag 0C6R](https://stacks.math.columbia.edu/tag/0C6R)) contains
$$
H^0(X_{r+1},\mco_{X_{r+1}}^\times)
\longrightarrow
H^0(X_r,\mco_{X_r}^\times)
\longrightarrow
H^1\bigl(Y,\mco_Y(-rd)\bigr)
$$
$$
\longrightarrow
\Pic X_{r+1}
\longrightarrow
\Pic X_r
\longrightarrow
H^2\bigl(Y,\mco_Y(-rd)\bigr).
$$
By step [](#s1){.pf-ref} the first two groups of units are both $k^\times$, and their map is the identity.
Since $Y$ has dimension $1$,
$$
H^2\bigl(Y,\mco_Y(-rd)\bigr)=0.
$$
Exactness therefore gives the displayed short exact sequence, and the thickening it is read on is square-zero: the ideal of $X_r$ in $X_{r+1}$ is $\mci^r/\mci^{r+1}$, whose square is $\mci^{2r}/\mci^{2r+1}=0$.  Kim writes the same sequence, for $Y_n\subset Y_{n+1}$, and adds in a parenthesis that the hypothesis of Exercise III.4.6 is unnecessary: he states that a nilpotent ideal suffices, "because $(1+a)^{-1}=1-a+a^2-\cdots$", and concludes that the kernel of $\Pic Y_n\to\Pic Y_1$ is the first cohomology of a coherent $\OO_Y$-module.  That is false as soon as the square of the ideal is nonzero.  The geometric series is finite only when $a^2=0$; for a nilpotent $a$ with $a^2\ne0$ the map $a\mapsto1+a$ is not a homomorphism, since $(1+a)(1+b)=1+a+b+ab$ carries the cross term $ab$, and the units of a nilpotent extension do not form an additive group, so no argument of this kind gives a $k$-vector space structure to a kernel built from them.  In characteristic $p$ the difference is visible in the torsion: the additive group of a $k$-vector space is killed by $p$, whereas $(1+a)^p=1+a^p\ne1$ for nilpotent $a\ne0$.  The sequence displayed above is the one for the square-zero pair, and that is the pair on which it holds.
:::

:::

::: {.pf-step #s3}
The natural map
$$
\Pic\hat X\longrightarrow\Pic Y
$$
is surjective.
If
$$
K=\ker(\Pic\hat X\to\Pic Y)
$$
and
$$
K_r=\ker(\Pic\hat X\to\Pic X_r),
$$
then
$$
K=K_1\supseteq K_2\supseteq\cdots
$$
and
$$
K_r/K_{r+1}\cong V_r.
$$

::: pf-proof
As in [[P-AGH3115PICFORMAL|Exercise III.11.5]], Exercise II.9.6 gives
$$
\Pic\hat X\cong\varprojlim_r\Pic X_r.
$$
Kim, Exercise 3.11.7(a), PDF p. 213, cites Exercise II.9.6 for this inverse limit too, and concludes the surjectivity from the same two facts: "Because $Y$ is 1-dimensional, we have that the $H^2$ term vanishes.  On the other hand, as $n$ gets larger, the term $H^1(Y,\OO_Y(-dn))$ gets larger.  This shows that we can always lift a line bundle over $Y_n$ to a line bundle over $Y_{n+1}$, and the ways of lifting is given by a nonzero $k$-vector space for large enough $n$."

Yang Pi-Yeh, Solution 3.11.7(a), printed p. 82, writes the same inverse limit, and then the sequence
$$
H^1(X_n,\mci^{n-1})\longrightarrow\Pic X_n\longrightarrow\Pic X_1\longrightarrow H^2(X_n,\mci^{n-1}),
$$
whose outer terms join $X_n$ to $X_1$ where those of Exercise III.4.6 join $X_n$ to $X_{n-1}$; its left term is the one of the sequence displayed in step [](#s2){.pf-ref}, with $r=n-1$.  It is not exact in the middle once $n\ge3$.  Since $\mci^n=0$ on $X_n$,
$$
H^1(X_n,\mci^{n-1})=H^1\bigl(Y,\OO_Y(-(n-1)d)\bigr)=V_{n-1}
=\ker(\Pic X_n\to\Pic X_{n-1}),
$$
so the image of his left-hand map is the subgroup of the classes trivial on $X_{n-1}$, while $\ker(\Pic X_n\to\Pic X_1)$ is strictly larger as soon as some $V_r$ with $1\le r\le n-2$ is nonzero: such a class lifts to $X_n$, the transitions being surjective by step [](#s2){.pf-ref}, and is then trivial on $X_1$ and not on $X_{n-1}$.  Step [](#s4){.pf-ref} makes $V_r\ne0$ for large $r$.  He notes that his $H^2$ term vanishes because $X_n$ is one-dimensional, and draws the surjectivity from that alone: "Hence in limit, we have $\Pic\hat X=\varprojlim\Pic X_n\to\Pic Y$ is surjective."  The conclusion is right, and what it rests on is the vanishing of the $H^2$ term of the correct sequence, which makes every transition surjective, as step [](#s2){.pf-ref} says.  He has no counterpart of Kim's sentence that the $H^1$ term grows.  The identification $K_r/K_{r+1}\cong V_r$ is the card's, and uses the surjectivity of the transitions: every transition map in this inverse system is surjective by step [](#s2){.pf-ref}. Starting with any class in
$$
\Pic X_1=\Pic Y,
$$
choose successively a lift to $X_2$, then to $X_3$, and so on.
The resulting compatible sequence is a class in $\Pic\hat X$, proving surjectivity.

Now fix $r$.
An element of $K_r$ has trivial restriction to $X_r$, so its restriction to $X_{r+1}$ lies in
$$
\ker(\Pic X_{r+1}\to\Pic X_r)=V_r.
$$
This gives a homomorphism
$$
K_r\longrightarrow V_r.
$$
Its kernel is exactly $K_{r+1}$.
It is surjective because a class in $V_r$ can first be regarded as a class on $X_{r+1}$ trivial on $X_r$, and then lifted successively through all higher $X_s$ using the surjectivity from step [](#s2){.pf-ref}. Thus
$$
K_r/K_{r+1}\cong V_r.
$$
:::

:::

::: {.pf-step #s4}
The dimensions $\dim_kV_r$ are unbounded.
More precisely, for $r\gg0$,
$$
\dim_kV_r
=
rd^2+\frac{d(d-3)}2.
$$

::: pf-proof
Kim, Exercise 3.11.7(a), PDF p. 213, states only that "as $n$ gets larger, the term $H^1(Y,\OO_Y(-dn))$ gets larger".  The dimension count below, which makes the growth explicit, is the card's.

Yang, Solution 3.11.7(a), printed p. 82, gives that growth in the form of an equation, $H^1(X_n,\mci^{n-1})=k[x_0,x_1,x_2]/(f^{n-1})$, and takes the projective limit to be the completion of $k[x_0,x_1,x_2]$ at $(f)$.  The left side is right and the equation is not: $\mci^{n-1}/\mci^n\cong\OO_Y(-(n-1)d)$, so
$$
H^1(X_n,\mci^{n-1})=H^1\bigl(Y,\OO_Y(-(n-1)d)\bigr),
$$
which is a cohomology group of a coherent sheaf on the curve $Y$ and is finite-dimensional over $k$, of the dimension computed below with $r=n-1$, while $k[x_0,x_1,x_2]/(f^{n-1})$ has classes in every degree and is infinite-dimensional.  The equality with the cohomology of a single $X_n$ is therefore a misprint, and the conclusion drawn from it does not follow: this card computes $\dim_kV_r$ below, where $V_r=H^1(Y,\OO_Y(-rd))$ is the quotient $K_r/K_{r+1}$ of step [](#s3){.pf-ref}, and it does not identify the kernel $K$ with the completion of $k[x_0,x_1,x_2]$ at $(f)$.

Let $F$ be the homogeneous equation of $Y$.
Twisting the hypersurface sequence by $-rd$ gives
$$
0
\longrightarrow
\mco_{\PP^2}(-(r+1)d)
\xrightarrow{\cdot F}
\mco_{\PP^2}(-rd)
\longrightarrow
\mco_Y(-rd)
\longrightarrow0.
$$
By [[T-IJW1K|the cohomology calculation on projective space]],
$$
H^1(\PP^2,\mco(q))=0
$$
for every $q$, and
$$
\dim_kH^2(\PP^2,\mco(-m))
=
\binom{m-1}{2}
$$
for $m\ge3$.
Since a curve has no $H^2$ for a quasicoherent sheaf, the long exact sequence gives, for $r\gg0$,
$$
0
\longrightarrow
V_r
\longrightarrow
H^2\bigl(\PP^2,\mco(-(r+1)d)\bigr)
\longrightarrow
H^2\bigl(\PP^2,\mco(-rd)\bigr)
\longrightarrow0.
$$
Therefore
$$
\begin{aligned}
\dim_kV_r
&=
\binom{(r+1)d-1}{2}
-
\binom{rd-1}{2}\\
&=
rd^2+\frac{d(d-3)}2.
\end{aligned}
$$
This tends to infinity with $r$.
In particular $V_r\ne0$ for all sufficiently large $r$, so the filtration in step [](#s3){.pf-ref} has infinitely many strict inclusions.
:::

:::

::: {.pf-step #s5}
If $\operatorname{char}k=0$, then $K$ is an infinite-dimensional $k$-vector space.

::: pf-proof
The argument below is the card's.  Kim, Exercise 3.11.7(a), PDF p. 213, asserts the $k$-vector-space structure in a parenthesis --- the kernel "is the inverse limit of $k$-vector spaces, hence is a $k$-vector space" --- which is the assertion under proof, and Yang, Solution 3.11.7(a), printed p. 82, deduces it from the identification with a completion.

Let
$$
\hat\mci=\ker(\mco_{\hat X}\to\mco_Y).
$$
The kernel of
$$
\mco_{\hat X}^\times\longrightarrow\mco_Y^\times
$$
is the sheaf of principal formal units
$$
1+\hat\mci.
$$
In characteristic zero the convergent $I$-adic series
$$
\log(1+a)
=
\sum_{m\ge1}(-1)^{m+1}\frac{a^m}{m}
$$
and
$$
\exp(a)
=
\sum_{m\ge0}\frac{a^m}{m!}
$$
are inverse isomorphisms of sheaves of abelian groups
$$
1+\hat\mci
\xrightarrow{\sim}
\hat\mci.
$$
Because the right-hand side is a sheaf of $k$-vector spaces, this transports a $k$-vector-space structure to $1+\hat\mci$ and hence to its cohomology.

Step [](#s1){.pf-ref} gives
$$
H^0(\hat X,\mco_{\hat X})=k,
$$
so
$$
H^0(\hat X,\mco_{\hat X}^\times)
\longrightarrow
H^0(Y,\mco_Y^\times)
$$
is the isomorphism $k^\times\to k^\times$.
The long exact sequence for
$$
1
\longrightarrow
1+\hat\mci
\longrightarrow
\mco_{\hat X}^\times
\longrightarrow
\mco_Y^\times
\longrightarrow1
$$
therefore identifies
$$
K
\cong
H^1(\hat X,1+\hat\mci)
\cong
H^1(\hat X,\hat\mci)
$$
as a $k$-vector space.

Under the identification just made, the two filtrations match: a class in $K_r$ is represented by a cocycle with values in $1+\hat\mci^r$, so its logarithm lies in $H^1(\hat X,\hat\mci^r)$ and $K_r$ is the image of $H^1(\hat X,\hat\mci^r)$ in $H^1(\hat X,\hat\mci)$. Each $K_r$ is therefore a $k$-subspace of $K$. A finite-dimensional $k$-vector space bounds the length of a strictly descending chain of subspaces, and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give the infinite chain
$$
K=K_1\supsetneq K_2\supsetneq\cdots
$$
of subspaces. Hence
$$
\boxed{\dim_kK=\infty}.
$$
This proves the vector-space assertion in part (a) when $\operatorname{char}k=0$.
:::

:::

::: {.pf-step #s6}
In characteristic $p>0$, the assertion that $K$ itself is a $k$-vector space is false in general.

::: pf-proof
The computation below is the card's; neither source states the failure in positive characteristic.

Take
$$
Y=\{z=0\}\subseteq\PP_k^2,
$$
so that $Y\cong\PP_k^1$, and let
$$
U_x=\operatorname{Spf} k[t][[s]],\qquad t=y/x,\ s=z/x,
\qquad
U_y=\operatorname{Spf} k[t^{-1}][[s']],\qquad s'=z/y=s/t
$$
be the two formal opens over $x\ne0$ and $y\ne0$. On their intersection
$$
\frac{z^2}{xy}=\frac{s^2}{t}=\frac{s'^2}{t^{-1}},
$$
so
$$
u=1+\frac{z^2}{xy}
$$
is a unit of $\OO(U_x\cap U_y)$ congruent to $1$ modulo the ideal of $Y$.
The formal scheme $\hat X$ is covered by the two opens $U_x,U_y$, which have no
triple intersection; by the Čech description of invertible sheaves on a formal
scheme, $u$ is therefore the transition function of an invertible sheaf
$\mathfrak L$ on $\hat X$ with $\restrictionof{\mathfrak L}{Y}\cong\OO_Y$.

What has to be shown is that no positive power $u^m$ is a Čech coboundary, that
is, that $u^m=A/B$ has no solution with
$$
A=\sum_{i\ge0}a_i(t)s^i\in k[t][[s]],\qquad
B=\sum_{j\ge0}b_j(t^{-1})s'^j\in k[t^{-1}][[s/t]]
$$
units of the respective rings.

Write $m=p^b m'$ with $p\nmid m'$ and put $q=p^b$. In characteristic $p$ one
has $(1+x)^{p^b}=1+x^{p^b}$, so
$$
u^m=\Bigl(1+\frac{s^{2q}}{t^{q}}\Bigr)^{m'}
=1+m'\frac{s^{2q}}{t^{q}}+\text{terms in higher powers of }\frac{s^{2q}}{t^{q}},
$$
and $m'\ne0$ in $k$ because $p\nmid m'$. Suppose $u^m=A/B$, so that
$$
A=B\,u^m .
$$
For $B\in k[t^{-1}][[s/t]]$ the coefficient of $s^j$ in $B$ is
$b_j(t^{-1})\,t^{-j}$ with $b_j\in k[t^{-1}]$; write $a_j\in k[t]$ for the
coefficient of $s^j$ in $A$. At $j=0$ the comparison gives $a_0=b_0$, and
$b_0=a_0\in k[t]\cap k[t^{-1}]=k$, so after multiplying $A$ and $B$ by the same
constant we may take $a_0=b_0=1$. For $1\le j<2q$ the expansion of $u^m$ has no
term in $s^j$, so the comparison reads
$$
a_j(t)=b_j(t^{-1})\,t^{-j},
$$
an identity between a polynomial in $t$ and an element of $t^{-j}k[t^{-1}]$;
hence $a_j=b_j=0$. At $j=2q$ the comparison reads
$$
a_{2q}(t)=b_{2q}(t^{-1})\,t^{-2q}+m'\,t^{-q},
$$
that is
$$
a_{2q}(t)-m'\,t^{-q}\in t^{-2q}k[t^{-1}].
$$
The left-hand side is a polynomial in $t$ plus the single monomial $-m't^{-q}$,
with $m'\ne0$, while every element of $t^{-2q}k[t^{-1}]$ is a $k$-linear
combination of $t^{-k}$ with $k\ge2q>q$. This is impossible. Hence $u^m$ is not a
coboundary, for any positive exponent $m$. In particular $\mathfrak L$ is nontrivial and
has infinite order in $K$.

The additive group of a $k$-vector space is killed by its prime $p$, so a group
containing an element of infinite order is not a $k$-vector space. Since the
group law of $K=\ker(\Pic\hat X\to\Pic Y)$ is the multiplicative structure of
$\Pic$, the kernel in part (a) is not a $k$-vector space in characteristic $p$.
The correct characteristic-free statement is the filtered statement of steps
[](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.
:::

:::

::: {.pf-step #s7}
There is a nonalgebraizable invertible sheaf on $\hat X$.

::: pf-proof
By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $K$ is nonzero in every characteristic.  Kim, Exercise 3.11.7(b), PDF p. 213, reaches the same conclusion: since $\Pic X=\ZZ$ and $\Pic\hat X$ is "too large", a line bundle not coming from $\OO_X(n)$ is not algebraizable.
Choose a nontrivial class
$$
[\mathfrak L]\in K.
$$
Thus
$$
\mathfrak L\restrict_Y\cong\mco_Y.
$$
Suppose that $\mathfrak L$ were algebraizable.
Then there would be a coherent sheaf $\mcg$ on $X$ with
$$
\hat\mcg\cong\mathfrak L.
$$

The local argument in [[P-AGH3116ALGEBRAIZABLE|Exercise III.11.6, steps 7--8]] applies to this single algebraization: faithfully flat completion shows that $\mcg$ is locally free of rank one on a neighbourhood of $Y$, and its reflexive hull
$$
\mcl=\mcg^{\vee\vee}
$$
is a rank-one reflexive sheaf on $X=\PP_k^2$.
Since projective space is regular and locally factorial, $\mcl$ is invertible; moreover $\mcl$ agrees with $\mcg$ near $Y$, so
$$
\hat\mcl\cong\mathfrak L.
$$

But
$$
\Pic\PP_k^2\cong\ZZ
$$
with generator $\mco_X(1)$, so
$$
\mcl\cong\mco_X(m)
$$
for some $m\in\ZZ$.
Restricting to $Y$ gives
$$
\mco_Y(m)
\cong
\mathfrak L\restrict_Y
\cong
\mco_Y.
$$
Now
$$
\deg\mco_Y(m)=md.
$$
Since $d>0$, triviality forces $m=0$.
Hence
$$
\mcl\cong\mco_X
$$
and therefore
$$
\mathfrak L\cong\mco_{\hat X},
$$
contrary to the choice of $[\mathfrak L]\ne0$.

Thus $\mathfrak L$ is not algebraizable, proving (b).
:::

:::

::: {.pf-step #s8}
There is a locally free sheaf $\mathfrak F$ on $\hat X$ such that no twist $\mathfrak F(n)$ is generated by global sections.

::: pf-proof
Condition (i) of [[P-AGH3116ALGEBRAIZABLE|Exercise III.11.6(b)]] says that *every* locally free sheaf on $\hat X$ is algebraizable.
Step [](#s7){.pf-ref} gives an invertible, hence locally free, counterexample.
Therefore condition (i) is false.

Exercise III.11.6(b) proves that condition (i) is equivalent to condition (ii).  Kim, Exercise 3.11.7(c), PDF p. 213, draws the same conclusion in one sentence: "By the equivalence of (i) and (ii) in part (b) of Exercise 3.11.6, we see that there are locally free sheaves $\mathfrak F$ on $\hat X$ such that no twist $\mathfrak F(n)$ is generated by global sections."  The passage from one non-generated twist to none at all, which follows because $\OO_{\hat X}(r)$ is globally generated, is the card's.
Hence condition (ii) is false.
Consequently there is a locally free sheaf $\mathfrak F$ on $\hat X$ for which no integer $n_0$ has the property that
$$
\mathfrak F(n)
$$
is generated by global sections for every $n\ge n_0$.

Suppose some twist $\mathfrak F(n_1)$ were generated by global sections.
For every $r\ge0$, the sheaf
$$
\mco_{\hat X}(r)
$$
is generated by global sections because it is the restriction of the globally generated sheaf $\mco_{\PP^2}(r)$.
Tensor products of globally generated sheaves are globally generated, so
$$
\mathfrak F(n_1+r)
=
\mathfrak F(n_1)\otimes\mco_{\hat X}(r)
$$
would be globally generated for every $r\ge0$.
Taking $n_0=n_1$ would then satisfy condition (ii) for $\mathfrak F$, a contradiction.

Therefore
$$
\boxed{\mathfrak F(n)\text{ is not generated by global sections for every }
n\in\ZZ}.
$$
This is the phenomenon announced in Hartshorne II.9.9.1.
:::

:::

::: pf-qed
Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, and [](#s4){.pf-ref} prove the characteristic-free surjectivity and infinite filtered kernel in (a), step [](#s5){.pf-ref} gives the stated infinite-dimensional vector-space conclusion in characteristic zero, and step [](#s6){.pf-ref} records the necessary correction in positive characteristic.
Step [](#s7){.pf-ref} proves (b), and step [](#s8){.pf-ref} proves (c).
:::

:::
:::

::: {.remark title="Published solution"}
Neither published solution proves the printed claim of (a).  Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter III §11, Exercise 11.7, PDF p. 213, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: he writes $\Pic\hat X=\varprojlim_n\Pic Y_n$ from Exercise II.9.6, the exact sequence of Exercise III.4.6, notes that its $H^2$ term vanishes because $Y$ is a curve and that its $H^1$ term grows, concludes that $\Pic\hat X\to\Pic Y$ is surjective with kernel "an infinite-dimensional $k$-vector space", and adds in a parenthesis the argument he intends for the vector-space structure: the kernel of $\Pic Y_n\to\Pic Y_1$ is the first cohomology of a coherent sheaf, "Now the kernel of $\Pic\hat X\to\Pic Y$ is the inverse limit of $k$-vector spaces, hence is a $k$-vector space".  Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 3.11.7, printed p. 82, gives the same inverse limit, proves the surjectivity from a sequence whose outer terms join $\Pic X_n$ to $\Pic X_1$, which is not the sequence of III.4.6 and is not exact in the middle, as step [](#s3){.pf-ref} shows, and writes the kernel as $\varprojlim k[x_0,x_1,x_2]/(f^{n-1})$, "the completion of $k[x_0,x_1,x_2]$ at $(f)$, hence infinite dimensional".

The false step in characteristic $p$ is the one before that inference, not the inference itself.  Kim extends Exercise III.4.6 from a square-zero ideal to a nilpotent one by the finite geometric series $(1+a)^{-1}=1-a+a^2-\cdots$, which is a finite sum only when $a^2=0$, and concludes that the kernel of $\Pic Y_n\to\Pic Y_1$ is the first cohomology of a coherent sheaf; the inference from that to the inverse limit would then be valid, the transition maps being $k$-linear.  What fails is the extension: for a nilpotent $a$ with $a^2\ne0$ the map $a\mapsto1+a$ is not additive, $(1+a)(1+b)=1+a+b+ab$, and in characteristic $p$ one has $(1+a)^p=1+a^p\ne1$, so the units of the thickening are not a $k$-vector space and neither is a kernel built from them.  The kernel of $\Pic X_r\to\Pic X_s$ is a filtered formal group and not an additive one, and step [](#s2){.pf-ref} states the sequence for the square-zero pair, which is where it holds.  Step [](#s6){.pf-ref} exhibits a line bundle of infinite order in the kernel on the line $z=0$.  In characteristic zero step [](#s5){.pf-ref} makes Kim's conclusion true by the $I$-adic logarithm, and that argument is the card's.  Kim's (b) and (c) agree with steps [](#s7){.pf-ref} and [](#s8){.pf-ref}.
:::
