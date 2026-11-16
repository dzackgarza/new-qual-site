---
schema: qual/card@1
id: E-HAT-4.1-9
kind: problem
title: "Extending the long exact sequence to $\\pi_0$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A local reader found the pair sequence's two remaining windows mislabelled and left unproved,
    and part (b)'s set-valued tail untreated. All three are repaired. (1) The display at the old
    "Which windows these are" paragraph labelled $\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)$
    as the window centered at $\pi_1(A,x_0)$; it is the window centered at $\pi_1(X,x_0)$, its third
    term. The corrected paragraph gives the whole sequence and both windows, and the window centered
    at $\pi_1(A,x_0)$ is $\pi_2(X)\to\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)$. (2) Both windows
    are now proved. The group chase's step $h(\gamma(c)^{-1}c')=1$ needs a homomorphism out of the
    centre, which these windows lack; the replacement uses exactness at the centre's target instead,
    with the two-sided invertibility of the bijections at the surrounding terms. The only
    non-abstract step is the observation that two loops at $y_0$ with the same class in
    $\pi_1(Y,C,y_0)$ differ by the image of a loop in $C$, read off the boundary of the homotopy
    through paths from $C$ to $y_0$. (3) Part (b) now treats the set-valued tail: it names the two
    windows that exist, centred at $\pi_1(A,B,x_0)$ and $\pi_1(X,B,x_0)$, proves the injectivity half
    at each by the same chase, and states that the surjectivity halves are not established, with the
    reason (the difference of two classes over the same image in $\pi_1(Y,D)$ is a path in $C$
    between interior points, not a class ending at the basepoint). Neither half is asserted without
    proof. Every citation now names its text version: Hatcher in
    `tmp/sources/hatcher-2002-algebraic-topology.md`, Brown already in
    `tmp/sources/brown-1970-fibrations-of-groupoids.md`. Not checked: the Lean declarations the card
    links were not re-elaborated in this pass, and the printed pagination of the 2002 printing is
    quoted from its text version.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher Section 4.1 Exercise 9 and the 2021-06-02 correction; corrected i^* to i_* in the stored statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct in its two parts. The extension by `pi_0(X,A,x_0) = pi_0(X,x_0) /
    i_* pi_0(A,x_0)` is exact at the tail because the components of `X` mapping to the distinguished
    relative class are precisely those meeting `A`, and the quotient map is onto. (a) The five-lemma in
    degrees `>= 2` is the ordinary one; in the pointed-set tail the argument is the appropriate
    replacement — exactness says that the fiber of the next map over the distinguished element is the
    image of the preceding map — and the hypothesis that the four surrounding maps are bijections *for all
    basepoints* is exactly what allows rebasing at an arbitrary component, which is the one place the
    naive group-theoretic version fails. (b) The triple sequence stops at `pi_0(A,B,x_0)` because there is
    no distinguished element of `pi_0(B)` to feed the next term. No correction was needed.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The printed part (a) is not correct as stated, and the earlier note's claim that "the hypothesis
    that the four surrounding maps are bijections for all basepoints is exactly what allows rebasing"
    does not repair it: rebasing is not available, because the basepoint of the pair $(Y,B)$ must lie
    in $B$ while the component of $B$ whose surjectivity is in question need not meet the image of
    $A$. Counterexample on the card: $X$ the disjoint union of a point $x_0$ and a point $a$ with
    $A=\{x_0,a\}$, $Y$ the disjoint union of a point $y_0$ and the interval $[0,1]$ with
    $B=\{y_0,0,1\}$, and $\varphi(x_0)=y_0$, $\varphi(a)=0$. Then the vertical maps at
    $\pi_1(X,A,x_0)$, $\pi_1(X,x_0)$, $\pi_0(X,x_0)$ and $\pi_0(X,A,x_0)$ are all bijections of
    one-point or two-point sets, while $\pi_0(A,x_0)\to\pi_0(B,y_0)$ is 2 points into 3 and is not
    onto. The card now states the exercise as printed and proves what is true: the five-lemma at
    every term in degrees $\ge1$ (both chases written out), the bijectivity of the vertical at
    $\pi_0(X,A,x_0)$ from those at $\pi_0(A,x_0)$ and $\pi_0(X,x_0)$, and the surjectivity at
    $\pi_0(A,x_0)$ for the components of $B$ lying in the component of $y_0$ in $Y$. Part (b) is
    correct as printed and its example is checked point by point.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Read Hatcher's published errata list for *Algebraic Topology*
    (pi.math.cornell.edu/~hatcher/AT/ATerrata.pdf) for this exercise, as #123 asks. The only entry
    bearing on it is "§4.1, page 358, Exercise 9, first line. To avoid an abuse of notation, replace
    $\pi_0(A,x_0)$ by $i_*(\pi_0(A,x_0))$. (The previous version of this correction mistakenly said
    $i^*$ instead of the correct $i_*$.)" That is a notational correction of the displayed term and
    changes no hypothesis. The current online text of the book (AT.pdf, printed p. 358) carries it
    and is otherwise identical to the 2002 printing: part (a) still concludes that one of the maps
    is a bijection "if the four surrounding maps are bijections for all choices of $x_0$". So the
    errata supplies no corrected statement and does not repair the failure at the $\pi_0(A,x_0)$
    term; the counterexample on this card survives the corrected notation, since
    $i_*\pi_0(A,x_0)$ is the whole of $\pi_0(X,x_0)$ in it. The repaired statement proved above
    therefore stands as the card's own. Not established here: a published proof of that repaired
    statement. Searched without result in the retained sets (Sam, Li, DeMason, Poulsen, Stanford
    Math 215C Solution Sets 1--5, the UCR Math 205B help file, May's *Concise Course* §4, Maxim's
    Math 752 notes) and in Hatcher's text and errata.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    Withdraws the counterexample recorded on 2026-11-07, which does not satisfy the hypothesis it is
    offered against. That hypothesis is that the four surrounding maps are bijections for every
    choice of basepoint, and the basepoints admissible for the pair $(X,A,x_0)$ are the points of
    $A$. In the withdrawn example $X=\{x_0\}\sqcup\{a\}$ is discrete with $A=X$, while
    $Y=\{y_0\}\sqcup[0,1]$ and $B=\{y_0,0,1\}$; at the basepoint $a\in A$ the vertical map at
    $\pi_1(X,A,a)$ is one point into two, since the only path from $A$ to $a$ in the discrete $X$ is
    the constant one, while $\pi_1(Y,B,\varphi(a))=\pi_1(Y,B,0)$ contains the classes of the constant
    path at $0$ and of a path from $1$ to $0$, both starting in $B$. The example therefore fails the
    hypothesis at a basepoint in $A$, exactly as the brief for #123 asked to be checked, and it is
    withdrawn. It is replaced by two examples that do satisfy the hypothesis at every basepoint: for
    the term $\pi_1(X,A,x_0)$, $X=\RR\sqcup\RR$ with $A=\{1\}\cup\{2\}$ one point in each copy,
    $Y=\RR$ with $B=\{0,3\}$, and $\varphi$ equal to $0$ on the first copy and $3$ on the second; and
    for the term $\pi_0(A,x_0)$, $X=Y=\RR$ with $A=(-1,0]\cup(2,3)$, $B=(-1,1)$ and the piecewise map
    that is the identity on $(-\infty,0]$, $0$ on $[0,2]$ and $t-2$ on $[2,\infty)$. In each case the
    four surrounding maps are computed on the card, at every basepoint, and the conclusion fails.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    Corrects the claim, carried since 2026-11-07, that the printed five-lemma holds "at every term in
    degrees $\ge1$". The group chase on the card is a chase of five group terms, and in the pair
    sequence the windows of five group terms are exactly those centered at a term of degree $\ge2$;
    the window centered at the pointed set $\pi_1(X,A,x_0)$ is not one of them, and the first new
    example shows that the printed claim is false there too. So the printed (a) fails at two terms,
    $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$, and the card now says so. What survives is stated as Claim 1
    ($\pi_0(X,A,x_0)$ from $\pi_0(A,x_0)$ and $\pi_0(X,x_0)$), Claim 2 (unchanged), and a new Claim 3:
    surjectivity at $\pi_0(A,x_0)$ is forced by the hypothesis, using $\pi_1(X,A,x)$ onto at the
    relevant basepoints and $\pi_0(X,A,x_0)$ injective, so the failure at $\pi_0(A,x_0)$ is
    injectivity only and not, as the withdrawn example suggested, surjectivity. The windows centered
    at $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$ are recorded on the card as not settled there. Part (b) is
    unchanged and still checked as printed.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    Read Brown, *Fibrations of groupoids*, Journal of Algebra 15 (1970) 103--132, in the text
    version `tmp/sources/brown-1970-fibrations-of-groupoids.md`, for the $\pi_0$ five-lemma the #123
    brief names: Theorem 4.9 on printed p. 121, whose (a) gives surjectivity of $f:\pi_0F\to\pi_0F'$
    from surjectivity of $h:H(v)\to H'(v')$ and of $g:\pi_0G\to\pi_0G'$ together with injectivity of
    $h:\pi_0H\to\pi_0H'$, and whose (b) gives injectivity of $f$ on $\ker(\pi_0F\to\pi_0G)$; and
    Corollary 4.11 on printed pp. 122--123, that equivalences $h:H\to H'$ and $g:G\to G'$ force
    $f:F\to F'$ to be an equivalence, hence $f:\pi_0F\to\pi_0F'$ bijective, by 4.9 followed by the
    ordinary five-lemma for groups on diagram 4.8. Cited on the card in a remark for exactly that,
    and not used in the argument: Brown's hypotheses are those of a fibration of groupoids with
    equivalences of the total groupoids and bases, which is stronger than the exercise's "for all
    choices of $x_0$", and the map of pairs $(X,A)\to(Y,B)$ is not a fibration of groupoids. No
    claim is made that Brown's theorem settles Hatcher's exercise. The extracted text of the paper
    writes some symbols as glyph substitutions (it is a scan of the 1970 print); the statements
    above were read against the displayed formulas of 4.9, 4.10 and 4.11, not from the running text
    alone.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    Withdraws the two counterexamples added earlier today and the claim they supported, that the
    printed (a) fails at the terms $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$. Both are disputed and neither
    is established. Against the first ($X=\RR\sqcup\RR$ with $A=\{1\}\cup\{2\}$, $Y=\RR$ with
    $B=\{0,3\}$): its vertical map $\pi_0(X)\to\pi_0(Y)$ is two components into one. Against the
    second ($X=Y=\RR$, $A=(-1,0]\cup(2,3)$, $B=(-1,1)$): $\pi_1(X,A,x_0)$ is read as having one class
    per component of $A$ rather than one per point of $A$, and then it is the surrounding map at
    $\pi_1(X,A,x_0)$ that fails rather than the one at $\pi_0(A,x_0)$. The second objection is about
    the definition of $\pi_1$ of a pointed pair, not about an example, so this reading is established
    neither on the card nor in prose: the question goes to a Lean declaration at
    <https://github.com/dzackgarza/lean-categories/issues/156>. The card now states the question as
    open at those two terms and asserts neither direction. The withdrawal of the 2026-11-07 example
    and the reason for it stand unchanged, and Claims 1, 2 and 3 stand: Claim 3 uses only that the
    map at $\pi_1(X,A,x)$ is onto at the relevant basepoints, so it holds under either reading of
    that set. Not claimed: that the printed (a) is correct, or that it is false; not verified: the
    contested reading of $\pi_1(X,A,x_0)$, which is what the issue is for.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    The printed (a) is now stated as proved at both set-valued terms, and the card carries the
    certificate. lean-categories#156 is merged at `9b8b85840c`, and `relativePiOne_map_bijective`
    and `zerothHomotopySubtypeMap_bijective` in `LeanCategories/Topology/PairHomotopySequence.lean`
    prove the printed claim at $\pi_1(X,A,x_0)$ and at $\pi_0(A,x_0)$, each from exactly the four
    surrounding maps of its own term, bijective at every basepoint of $A$, with
    $\pi_1(X,A,x_0)$ built as Hatcher's quotient in which the start point moves inside $A$ (printed
    p. 343) — the reading the earlier dispute turned on. Both declarations were re-elaborated here
    on the pinned baseline, Lean 4.33.0 with Mathlib `db584cd6`: exit 0, axioms only `propext`,
    `Classical.choice`, `Quot.sound`, no `sorryAx`. The card now carries the two arguments in the
    required form and Claim 1, and no longer discusses either withdrawn counterexample; Claims 2
    and 3 are dropped with the question they served. The claim that injectivity at
    $\pi_1(X,x_0)$ follows from injectivity at $\pi_1(X,A,x_0)$ is dropped as well: under the
    quotient reading a relative class of a loop at $x_0$ need not be its loop class, so that
    inference is not established. The windows centred at $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$ are not
    treated, and the card says so. Checked against Hatcher (2002), §4.1 Exercise 9 on printed
    p. 358, the errata's $i_*$ correction, and the definition of $\pi_n(X,A,x_0)$ on printed p. 343.
    Not claimed: that the printed (a) holds at $\pi_1(A,x_0)$ or at $\pi_1(X,x_0)$, or that a
    published treatment of the exercise exists.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Three statements were wrong and are repaired. (1) The remark cited Brown's Corollary 4.11 on
    "printed pp. 122--123"; it is printed on p. 123 only. In the text version
    `tmp/sources/brown-1970-fibrations-of-groupoids.md` the page marker `<!-- PDF pages 21-30 -->`
    stands immediately before it, so 4.11 opens the run of pages beginning at PDF page 21, printed
    p. 123 of Journal of Algebra 15 (1970) 103--132; Theorem 4.9, which the card also cites, precedes
    that marker, on printed p. 121. (2) The last paragraph of part (b) invoked "the analogue of
    Claim 2", a claim the card no longer has — Claims 2 and 3 were dropped in the 2026-11-14 rewrite
    that kept Claim 1 only — and it asserted rather than proved a five-lemma for the ladder of triple
    sequences. It is replaced by what the card establishes and by a statement of what it does not:
    the windows of five group terms (degrees $\ge2$) are the chase of part (a), applied to the triple
    ladder, which is exact by Theorem 4.3 (p. 344) and commutative by naturality (p. 345); no window
    of five group terms is centred at $\pi_1(A,B,x_0)$, $\pi_1(X,B,x_0)$, $\pi_1(X,A,x_0)$ or
    $\pi_0(A,B,x_0)$, the first three being pointed sets and the last the terminal term, at which
    there is no map out and hence no exactness obligation; and a set-valued five-lemma for the triple
    is not proved on this card, its two set-valued statements being the pair sequence's. What is
    proved about the terminal term is the quotient statement Claim 1 rests on, that a bijection
    $\pi_0(A,x_0)\to\pi_0(C,y_0)$ carrying $i_*\pi_0(B,x_0)$ onto $i'_*\pi_0(D,y_0)$ induces a
    bijection $\pi_0(A,B,x_0)\to\pi_0(C,D,y_0)$, since the two are $\pi_0(A,x_0)/i_*\pi_0(B,x_0)$ and
    its image. (3) The paragraph on which windows are group windows now names the pointed sets in
    them, rather than leaving the count implicit. Checked, against a reader's claim that the windows
    centred at $\pi_1(A,x_0)$ and at $\pi_1(X,x_0)$ are windows of groups: they are not. The sequence
    in degrees $1$ and $0$ reads
    $\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)\to\pi_0(X)\to\pi_0(X,A)\to0$, so the
    window centred at $\pi_1(A,x_0)$ contains $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$ and the one centred
    at $\pi_1(X,x_0)$ contains those two and $\pi_0(X,x_0)$; Hatcher defines $\pi_1(X,A,x_0)$ as a set
    of path classes and states on printed p. 343 that it is in general not a group in any natural way,
    so the group five-lemma does not apply to either window and the card's statement that they are not
    treated stands. Not claimed: a five-lemma at those two windows, in either direction.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass on this card. The text of the `source-corrected` event of this
    date above is restored from commit 6db04ca88a, which rewrote it in place after commit 857554a9b3 had
    pushed it, with no event of its own; the restored sentences stand as they were written and are
    corrected here. (1) The restored text says the chase's step "$h(\gamma(c)^{-1}c')=1$ needs a
    homomorphism out of the centre, which these windows lack". That is false of the first of the two
    windows, the one centred at $\pi_1(A,x_0)$: its chase runs exactly as the paragraph on
    $\pi_1(A,x_0)$ below has it, and it goes through. The step that needs a homomorphism is at the
    **second** window, where the map out of the centre's target is $k'=j':\pi_1(Y,y_0)\to\pi_1(Y,B,y_0)$,
    a map of pointed sets. The card now names $k'$ there; it had called that map $h'$, which is
    $i'_*:\pi_1(B,y_0)\to\pi_1(Y,y_0)$, and had therefore used one letter for two maps. (2) The same
    restored paragraph said of part (b) that it "names the two windows that exist": there are three
    windows of the triple ladder that contain a pointed set, and the one centred at $\pi_2(X,A,x_0)$ ---
    $\pi_2(A,B)\to\pi_2(X,B)\to\pi_2(X,A)\to\pi_1(A,B)\to\pi_1(X,B)$ --- was missing from the card. It is
    now stated and its chase is written out. (3) The restored text, and the card, said the injectivity
    half is proved at each of those windows. It is not: the chase shows that a class with $\gamma(c)=1$
    is trivial, which is triviality of the fibre over the base point, whereas injectivity of a map of
    pointed sets says that two classes with the same image are equal, and the fix-up that would give it
    multiplies by the difference of two such classes, which a pointed set does not supply. The card now
    says that, for all three windows and in the remark. (4) The sentence "Every one of the six windows
    is therefore settled on this card, and none of them by the group chase alone" contradicted the
    paragraph after it; the window centred at $\pi_2(X,A,x_0)$ is settled by the chase, the other five
    are not, and the sentence now says so. (5) The term $\pi_0(X,x_0)$ was said to be settled "by
    Claim 1", and Claim 1 was the statement about $\pi_0(X,A,x_0)$; bijectivity at $\pi_0(X,x_0)$ from
    its own four surrounding maps is now proved, as the new Claim 1, and the old statement is Claim 2.
    (6) Part (a) denoted the target pair $(Y,C,y_0)$ while the problem and the rest of the card use
    $(Y,B,y_0)$; part (a) now uses $(Y,B,y_0)$ throughout, and $C$, $D$ appear only in part (b), for the
    triple. Also repaired: the surjectivity step at $\pi_1(X,x_0)$ wrote the correction of $\delta(c)$
    to $c'$ as $\delta(c)^{-1}c'$ and multiplied on the right, which fails under Hatcher's convention,
    the first path traversed first; the correction is now $\omega=c'\delta(c)^{-1}$ and $c''=h(a)\cdot c$,
    with the convention stated, and the square at $\pi_1(Y,B,y_0)$ now reads $[a][b]^{-1}=[\lambda]$
    with $\lambda$ a loop in $B$, not $a^{-1}b$. Unchanged: the statement as printed on p. 358 with the
    errata's $i_*$, part (b)'s example that the triple sequence stops at $\pi_0(A,B,x_0)$, part (a)'s
    two set-valued arguments with their certificate on `lean-categories` main, and the citation of
    Brown's Theorem 4.9 and Corollary 4.11 as a related and unused statement. Not verified in this
    pass: the Lean declarations linked below, which were not re-elaborated.
---

::: {.problem}
Suppose we define $\pi_0(X, A, x_0)$ to be the quotient set $\pi_0(X, x_0) / i_*\bigl(\pi_0(A, x_0)\bigr)$ so that the long exact sequence of homotopy groups for the pair $(X, A)$ extends to $\cdots \to \pi_0(A, x_0) \stackrel{\iota_*}{\longrightarrow} \pi_0(X, x_0) \to \pi_0(X, A, x_0) \to 0$.

(a) Show that with this extension, the five-lemma holds for the map of long exact sequences induced by a map $(X, A, x_0) \to (Y, B, y_0)$, in the following form: One of the maps between the two sequences is a bijection if the four surrounding maps are bijections for all choices of $x_0$.

(b) Show that the long exact sequence of a triple $(X, A, B, x_0)$ can be extended only to the term $\pi_0(A, B, x_0)$ in general, and that the five-lemma holds for this extension.
:::

::: {.solution}
Define, for a pointed pair $(X,A,x_0)$,
$$
\pi_0(X,A,x_0)=\pi_0(X,x_0)\big/\,i_*\pi_0(A,x_0),
$$
the quotient pointed set, so that every component of $X$ meeting $A$ becomes the distinguished element. Then
$$
\pi_0(A,x_0)\xrightarrow{i_*}\pi_0(X,x_0)\xrightarrow{j_*}\pi_0(X,A,x_0)\longrightarrow0
$$
is exact as a sequence of pointed sets: the components mapping to the distinguished relative class are exactly those meeting $A$, and $j_*$ is onto. Exactness of the whole extended sequence at every other term is Hatcher's Theorem 4.3 (printed p. 344, read in the text version `tmp/sources/hatcher-2002-algebraic-topology.md`).

Throughout, a map of pairs $\varphi:(X,A,x_0)\to(Y,B,y_0)$ induces a ladder between the two sequences, commutative by naturality of the long exact sequence (p. 345), and "exact" for pointed sets means that the image of one map is the fiber of the next over the distinguished element.

### (a) The five-lemma

*Terms of degree $\ge2$: the group case.* The standard five-lemma argument applies verbatim in a window of five group terms, since every map there is a homomorphism. Write the ladder as
$$
A\xrightarrow{f}B\xrightarrow{g}C\xrightarrow{h}D\xrightarrow{k}E
\quad\text{over}\quad
A'\xrightarrow{f'}B'\xrightarrow{g'}C'\xrightarrow{h'}D'\xrightarrow{k'}E'
$$
with all four squares commutative and both rows exact.

- *Injectivity of $\gamma:C\to C'$*, given $\alpha$ onto and $\beta,\delta$ one-to-one: if $\gamma(c)=1$ then $\delta h(c)=h'\gamma(c)=1$, so $h(c)=1$ and $c=g(b)$ for some $b$. Then $g'\beta(b)=\gamma g(b)=1$, so $\beta(b)=f'(a')$ for some $a'$, and $a'=\alpha(a)$ because $\alpha$ is onto. Hence $\beta(b)=\beta f(a)$, so $b=f(a)$ by injectivity of $\beta$, and $c=g(b)=gf(a)=1$.
- *Surjectivity of $\gamma$*, given $\beta$ and $\delta$ onto and $\varepsilon$ one-to-one: for $c'\in C'$ put $d'=h'(c')$ and choose $d\in D$ with $\delta(d)=d'$. Then $\varepsilon k(d)=k'\delta(d)=k'h'(c')=1$, so $k(d)=1$ because $\varepsilon$ is injective, and hence $d=h(c)$ for some $c\in C$. Now $h'(\gamma(c))=\delta h(c)=d'=h'(c')$, so $h'(\gamma(c)^{-1}c')=1$ and therefore $\gamma(c)^{-1}c'=g'(b')$ for some $b'\in B'$; choose $b\in B$ with $\beta(b)=b'$ and put $c''=c\,g(b)$. Then $\gamma(c'')=\gamma(c)g'(b')=c'$.

*Which windows these are.* The four terms of degree one or zero in the extended sequence are the pointed sets $\pi_1(X,A,x_0)$, $\pi_0(A,x_0)$, $\pi_0(X,x_0)$ and $\pi_0(X,A,x_0)$, and the whole sequence reads

$$
\cdots\to\pi_2(X)\to\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)\to\pi_0(X)\to\pi_0(X,A)\to0 .
$$

A window of five consecutive terms is one centered at its third term. So a window of five consecutive terms all of which are groups is exactly one centered at a term of degree $\ge2$; the window centered at $\pi_1(A,x_0)$ is $\pi_2(X)\to\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)$, which ends at the pointed set $\pi_1(X,A,x_0)$; and the window centered at $\pi_1(X,x_0)$ is $\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)$, which contains the two pointed sets $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$. The window centered at $\pi_1(X,A,x_0)$ is $\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)\to\pi_0(X)$ and the one centered at $\pi_0(A,x_0)$ is $\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)\to\pi_0(X)\to\pi_0(X,A)$. The last two are proved below, the term $\pi_0(X,x_0)$ by Claim 1 below, and the two centred at $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$ at the end of this part. Every one of the six windows is therefore settled on this card: the one centred at $\pi_2(X,A,x_0)$ by the group chase, all five of its terms being groups, and the other five by the arguments below, each of which replaces the chase at a point where a term is only a pointed set.

*The term $\pi_1(X,A,x_0)$, and which set that is.* Hatcher defines $\pi_n(X,A,x_0)$ as the homotopy classes of maps of triples $(I^n,\partial I^n,J^{n-1})\to(X,A,x_0)$ (printed p. 343); for $n=1$ the $0$-end of $I$ is constrained only to lie in $A$, so $\pi_1(X,A,x_0)$ is the set of path classes from a point of $A$ to $x_0$, modulo homotopies through such paths, in which the start point moves inside $A$ and two classes with different start points may agree. With that reading the four surrounding maps of the term are
$$
\pi_1(A,a)\to\pi_1(B,\varphi a),\qquad \pi_1(X,a)\to\pi_1(Y,\varphi a)\quad(a\in A),\qquad \pi_0(A)\to\pi_0(B),\qquad \pi_0(X)\to\pi_0(Y),
$$
and the printed claim is that bijectivity of these four families forces the vertical map $\pi_1(X,A,x_0)\to\pi_1(Y,B,\varphi x_0)$ to be bijective. It does.

- *Injectivity.* Two relative classes with the same image have the same class of start point in $B$, because $\partial$ commutes with the map of pairs; injectivity at $\pi_0(A)$ puts their start points in one component of $A$, so a path $\delta$ in $A$ joins them, and translating one class along $\delta$ puts both at the same start point $a$. Their images then differ by a loop in $B$ at $\varphi a$, which lifts to a loop $\varepsilon$ in $A$ at $a$ because $\pi_1(A,a)\to\pi_1(B,\varphi a)$ is surjective; correcting by $\varepsilon$, the two representative paths have the same image in $Y$ from $\varphi a$ to $\varphi x_0$, hence agree by injectivity at $\pi_1(X,a)$.
- *Surjectivity.* A target class starts at some $b\in B$. By surjectivity at $\pi_0(A)$ its start point is $\varphi a$ for some $a\in A$ up to a path in $B$, and prepending that path makes the target path run from $\varphi a$ to $\varphi x_0$; the target lies over the class of $\varphi x_0$ in $\pi_0(Y)$, so by injectivity at $\pi_0(X)$ the point $a$ lies in the component of $x_0$ in $X$. A path in $X$ from $a$ to $x_0$ can then be corrected by a loop at $a$ so that its image is the target path, by surjectivity at $\pi_1(X,a)$, and the corrected path represents a relative class mapping onto the target.

*The term $\pi_0(A,x_0)$.* Its four surrounding maps are
$$
\pi_1(X,A,a)\to\pi_1(Y,B,\varphi a),\qquad \pi_1(X,a)\to\pi_1(Y,\varphi a)\quad(a\in A),\qquad \pi_0(X)\to\pi_0(Y),\qquad \pi_0(X,A,x_0)\to\pi_0(Y,B,\varphi x_0),
$$
and bijectivity of these families forces the vertical map $\pi_0(A)\to\pi_0(B)$ to be bijective, which is the printed claim at that term.

- *Injectivity.* Two points of $A$ whose images lie in the same component of $B$ lie in the same component of $X$, by injectivity at $\pi_0(X)$; a path in $X$ between them can be corrected by a loop so that its image is a prescribed path in $B$, by surjectivity at $\pi_1(X,a)$. The relative class of the constant path at the first point and that of the reversed corrected path at the second then have the same image in $\pi_1(Y,B,\varphi a)$, so by injectivity at $\pi_1(X,A,a)$ they agree, and applying $\partial$ gives that the two points lie in the same component of $A$.
- *Surjectivity.* A component $\beta$ of $B$ is the component of some $b\in B$; since $\pi_0(X)\to\pi_0(Y)$ is surjective, some component of $X$ maps into the component of $b$, and the class of that component in $\pi_0(X,A,x_0)$ is the base class by injectivity at $\pi_0(X,A,x_0)$, so a path in $A$ joins some $a\in A$ to a point of it. The path in $Y$ from $b$ to $\varphi a$ is a relative class at $\varphi a$, and it lifts along $\pi_1(X,A,a)\to\pi_1(Y,B,\varphi a)$ by surjectivity there; the image under $\partial$ of the lift is a component of $A$ mapping onto $\beta$.

*The certificate for those two terms.* Both statements are proved formally on `lean-categories` main, and those declarations are this card's certificate: `relativePiOne_map_bijective` and `zerothHomotopySubtypeMap_bijective` in [`LeanCategories/Topology/PairHomotopySequence.lean`](https://github.com/dzackgarza/lean-categories/blob/9b8b85840c2b5cef55942b971c65e3b4bfc0d252/LeanCategories/Topology/PairHomotopySequence.lean), the merge of <https://github.com/dzackgarza/lean-categories/issues/156> at commit `9b8b85840c`. Each takes the four surrounding maps of its own term as hypotheses, bijective at every basepoint of $A$, and concludes bijectivity of the vertical map at that term; the same file builds $\pi_1(X,A,x_0)$ as that quotient and proves exactness at the two joins that are not group statements. Elaborated on the pinned baseline (Lean 4.33.0, Mathlib `db584cd6`), both are free of `sorryAx`, with axioms only `propext`, `Classical.choice` and `Quot.sound`.

*The terms $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$.* The first of the two windows is settled by the group chase of the group case, which does not in fact need all five terms to be groups: the fifth term $\pi_1(X,A,x_0)$ is a pointed set, but it enters the chase only through the bijection $\varepsilon$, while every product and inverse is taken in the groups $\pi_1(A,x_0)$ and $\pi_1(B,y_0)$. The second window is not: there the chase ends with the step $k'(\delta(c)^{-1}c')=k'\delta(c)^{-1}k'(c')$, which needs $k'$ to be a homomorphism, and at that window $k'$ is the map $j':\pi_1(Y,y_0)\to\pi_1(Y,B,y_0)$ of pointed sets. That one step is replaced below by a reading of the fibre of $k'$, and nothing else in the chase changes.

Write $\partial:\pi_2(X,A)\to\pi_1(A)$ and $\partial':\pi_2(Y,B)\to\pi_1(B)$ for the boundary maps of the two rows, $f:\pi_2(X)\to\pi_2(X,A)$ and $f':\pi_2(Y)\to\pi_2(Y,B)$ for the maps into their domains, $\beta:\pi_2(X,A)\to\pi_2(Y,B)$ for the vertical map there, and $h=i_*:\pi_1(A)\to\pi_1(X)$, $h'=i'_*:\pi_1(B)\to\pi_1(Y)$, $k=j:\pi_1(X)\to\pi_1(X,A)$, $k'=j':\pi_1(Y)\to\pi_1(Y,B)$ for the maps of the two rows at the two centres and to their right. The target pair is the problem's $(Y,B,y_0)$ throughout this part; the letters $C$ and $D$ are used only in part (b), for the triple $(X,A,B)$ over $(Y,C,D)$. All of $h$, $h'$, $k$ and $k'$ are maps of pointed sets; $h$ and $h'$ are group homomorphisms, and $k$ and $k'$ are not.

*The window centered at $\pi_1(A,x_0)$: the vertical map $\gamma:\pi_1(A,x_0)\to\pi_1(B,y_0)$.* Its four surrounding maps are $\alpha:\pi_2(X)\to\pi_2(Y)$, $\beta$, $\delta:\pi_1(X)\to\pi_1(Y)$ and $\varepsilon:\pi_1(X,A)\to\pi_1(Y,C)$.

- *Injectivity.* Let $\gamma(c)=1$. Then $\delta h(c)=h'\gamma(c)=1$, so $h(c)=1$ because $\delta$ is injective, hence $c=\partial(b)$ for some $b\in\pi_2(X,A)$ by exactness at $\pi_1(A)$. Then $1=\gamma(c)=\gamma\partial(b)=\partial'\beta(b)$, so $\beta(b)\in\ker\partial'=\operatorname{im}f'$, say $\beta(b)=f'(a')$; since $\alpha$ is onto, $a'=\alpha(a)$, so $\beta(b)=\beta f(a)$ and $b=f(a)$ because $\beta$ is injective. Therefore $c=\partial f(a)=1$ by exactness at $\pi_2(X,A)$.

- *Surjectivity.* Let $c'\in\pi_1(B)$. Put $d'=h'(c')\in\pi_1(Y)$ and choose $d\in\pi_1(X)$ with $\delta(d)=d'$, which is possible because $\delta$ is onto. Then $\varepsilon k(d)=k'\delta(d)=k'h'(c')=1$ because $\operatorname{im}h'\subseteq\ker k'$ by exactness at $\pi_1(Y)$, so $k(d)=1$ because $\varepsilon$ is injective, and hence $d=h(a)$ for some $a\in\pi_1(A)$ by exactness at $\pi_1(X)$. Now $h'\bigl(\gamma(a)^{-1}c'\bigr)=h'\gamma(a)^{-1}h'(c')=1$, because $h'$ is a homomorphism, so $\gamma(a)^{-1}c'\in\ker h'=\operatorname{im}\partial'$ by exactness at $\pi_1(B)$; write $\gamma(a)^{-1}c'=\partial'(\nu)$ and $\nu=\beta(\mu)$ with $\mu\in\pi_2(X,A)$, which is possible because $\beta$ is onto. Then $\gamma(a)^{-1}c'=\partial'\beta(\mu)=\gamma\partial(\mu)$, so $c''=a\cdot\partial(\mu)$ satisfies $\gamma(c'')=\gamma(a)\gamma\partial(\mu)=c'$.

*The window centered at $\pi_1(X,x_0)$: the vertical map $\delta:\pi_1(X,x_0)\to\pi_1(Y,y_0)$.* Its four surrounding maps are $\beta$, $\gamma$, $\varepsilon$ and $\theta:\pi_0(A,x_0)\to\pi_0(B,y_0)$.

- *Injectivity.* Let $\delta(c)=1$. Then $\varepsilon k(c)=k'\delta(c)=1$, so $k(c)=1$ because $\varepsilon$ is injective, hence $c=h(a)$ for some $a\in\pi_1(A)$ by exactness at $\pi_1(X)$. Then $1=\delta(c)=h'\gamma(a)$, so $\gamma(a)\in\ker h'=\operatorname{im}\partial'$, say $\gamma(a)=\partial'(\nu)=\partial'\beta(\mu)=\gamma\partial(\mu)$; hence $a=\partial(\mu)$ because $\gamma$ is injective, and $c=h\partial(\mu)=1$ by exactness at $\pi_2(X,A)$.

- *Surjectivity.* Let $c'\in\pi_1(Y)$ and put $d=\varepsilon^{-1}k'(c')\in\pi_1(X,A)$. Then $\theta\partial(d)=\partial'\varepsilon(d)=\partial'k'(c')=1$ because $\operatorname{im}k'\subseteq\ker\partial'$ by exactness at $\pi_1(Y,B)$, so $\partial(d)=1$ because $\theta$ is injective, and hence $d=k(c)$ for some $c\in\pi_1(X)$ by exactness at $\pi_1(X,A)$. Now $\delta(c)$ and $c'$ are loops at $y_0$ with the same image under $k'$, and that fixes the class only up to $\ker k'$. Products in $\pi_1$ are written in Hatcher's convention throughout this card, the first path traversed first, so $[a][b]^{-1}$ is $a$ followed by $b$ reversed. If $a$ and $b$ are loops at $y_0$ with $k'(a)=k'(b)$, a homotopy through paths from $B$ to $y_0$ joining them is a map of the square whose bottom edge is $a$, whose top edge is $b$, whose right edge is the constant loop at $y_0$ and whose left edge is a loop $\lambda$ in $B$ at $y_0$; reading the boundary of that square, the constant edge contributes nothing and $[a][b]^{-1}=[\lambda]$. Hence $[a][b]^{-1}\in\operatorname{im}i'_*=\ker k'$ by exactness at $\pi_1(Y)$, and with $a=\delta(c)$ and $b=c'$ this says
$$
\omega:=c'\cdot\delta(c)^{-1}=\bigl(\delta(c)\cdot c'^{-1}\bigr)^{-1}\in\operatorname{im}i'_* .
$$
Since $\gamma$ is onto, $\omega=i'_*\gamma(a)=\delta h(a)$ for some $a\in\pi_1(A)$, and then $c'':=h(a)\cdot c$ satisfies $\delta(c'')=\delta h(a)\cdot\delta(c)=\omega\cdot\delta(c)=c'\cdot\delta(c)^{-1}\cdot\delta(c)=c'$. The correction is therefore made on the left, $c''=h(a)\cdot c$, which is the order the convention requires: the earlier reading $\delta(c)^{-1}c'$ is the other of the two elements of the fibre, and its product with $\delta(c)$ on the right does not return $c'$.

Both arguments use one exactness assertion outside their window, at the centre's target, and both use the two-sided invertibility of the bijections at the surrounding terms; the products and inverses are taken in groups, and no map into a pointed set is treated as a homomorphism.

*Claim 1: the term $\pi_0(X,x_0)$.* If the vertical maps at $\pi_0(A,x_0)$ and at $\pi_0(X,A,x_0)$ are bijections, then so is the vertical map $\Phi:\pi_0(X,x_0)\to\pi_0(Y,y_0)$. These two, together with the terminal map $\pi_0(X,A,x_0)\to0$ and the map $0\to0$ after it, are the four surrounding maps of the window centred at $\pi_0(X,x_0)$.

- *Injectivity.* Let $\Phi[x_1]=\Phi[x_2]$. Then $\theta j[x_1]=\theta j[x_2]$ by commutativity of the ladder, so $j[x_1]=j[x_2]$ because $\theta$, the vertical map at $\pi_0(X,A,x_0)$, is injective. Two components of $X$ have the same class in $\pi_0(X,A,x_0)=\pi_0(X,x_0)/i_*\pi_0(A,x_0)$ exactly when they are the same component or both meet $A$; in the second case injectivity of the vertical map at $\pi_0(A,x_0)$ puts them in one component of $A$, hence of $X$. So $[x_1]=[x_2]$.
- *Surjectivity.* Let $[y]\in\pi_0(Y,y_0)$. If $[y]$ meets $B$, choose $b\in B$ and $[a]\in\pi_0(A,x_0)$ with $\Phi[a]=[b]=[y]$, which exists because the vertical map at $\pi_0(A,x_0)$ is onto. Otherwise $[y]$ does not meet $B$, so $j'[y]$ is not the base class, and $\theta$ is onto, so $j'[y]=\theta[x]$ for some $[x]\in\pi_0(X,A,x_0)$; for a representative $x_1$ of $[x]$, $j'\Phi[x_1]=\theta j[x_1]=j'[y]$, so $\Phi[x_1]$ meets $B$ exactly when $[y]$ does, and it does not, hence $\Phi[x_1]=[y]$.

*Claim 2: the term $\pi_0(X,A,x_0)$.* If the vertical maps at $\pi_0(A,x_0)$ and at $\pi_0(X,x_0)$ are bijections, then so is the vertical map at $\pi_0(X,A,x_0)$. Indeed that map is induced by a bijection $\pi_0(X,x_0)\to\pi_0(Y,y_0)$ which carries the subset $i_*\pi_0(A,x_0)$ bijectively onto $i_*\pi_0(B,y_0)$, and a bijection of sets carrying one subset onto another induces a bijection of the quotients.

The two claims are conditional statements about the same four surrounding maps and are not circular: Claim 1 uses the bijections at $\pi_0(A,x_0)$ and at $\pi_0(X,A,x_0)$, Claim 2 those at $\pi_0(A,x_0)$ and at $\pi_0(X,x_0)$, so under the exercise's hypothesis every one of the three $\pi_0$ terms is settled.

### (b) The triple sequence

For $B\subset A\subset X$ the triple sequence of Theorem 4.3 ends
$$
\cdots\longrightarrow\pi_1(X,A,x_0)\xrightarrow{\partial}\pi_0(A,B,x_0),
$$
and it cannot in general be continued by $\pi_0(X,B,x_0)$. Take $X$ the disjoint union of a point $b_0$ and an interval, $x_0=b_0$, and $B=\{b_0,b_1\}$ with $b_1$ a point of the interval; let $A=\{b_0,b_1,a_1\}$ with $a_1\neq b_1$ a further point of the interval, so that $b_1$ and $a_1$ lie in different components of the subspace $A$ while lying in the same component of $X$. Then the class of $a_1$ in $\pi_0(A,B,x_0)=\pi_0(A,x_0)/i_*\pi_0(B,x_0)$ is not the distinguished element, because its component of $A$ does not meet $B$; but its image in $\pi_0(X,B,x_0)$ is distinguished, because every component of $X$ that meets $B$ is collapsed and $a_1$ lies in the component of $b_1$. On the other hand the class of $a_1$ is not in the image of $\partial:\pi_1(X,A,x_0)\to\pi_0(A,B,x_0)$, since a path in $X$ starting in $A$ and ending at $x_0=b_0$ stays in the component $\{b_0\}$ of $X$, so its starting point lies in the component $\{b_0\}$ of $A$, which is collapsed. Hence appending $\pi_0(X,B,x_0)$ would destroy exactness at $\pi_0(A,B,x_0)$.

With the sequence ending at $\pi_0(A,B,x_0)$, the ladder of triple sequences has group windows, settled by the chase of part (a), and three windows that contain a pointed set. *The group windows.* The terms of the triple sequence in degree $\ge2$ are groups and every map between them is a homomorphism, so a window of five consecutive terms which all lie in degree $\ge2$ is a window of five group terms, and the chase of part (a) applies to it verbatim; exactness of the triple sequence is Theorem 4.3 (p. 344) and the ladder commutes by naturality (p. 345). *The set-valued windows.* The tail reads $\pi_2(A,B)\to\pi_2(X,B)\to\pi_2(X,A)\to\pi_1(A,B)\to\pi_1(X,B)\to\pi_1(X,A)\to\pi_0(A,B)$, and since the terminal term has no map out of it, the windows of five consecutive terms there that contain a pointed set are **three**: the one centred at $\pi_2(X,A,x_0)$, namely $\pi_2(A,B)\to\pi_2(X,B)\to\pi_2(X,A)\to\pi_1(A,B)\to\pi_1(X,B)$, whose centre is a group but whose last two terms are only pointed sets; and the two centred at $\pi_1(A,B,x_0)$ and at $\pi_1(X,B,x_0)$, namely $\pi_2(X,B)\to\pi_2(X,A)\to\pi_1(A,B)\to\pi_1(X,B)\to\pi_1(X,A)$ and $\pi_2(X,A)\to\pi_1(A,B)\to\pi_1(X,B)\to\pi_1(X,A)\to\pi_0(A,B)$. No window is centred at $\pi_1(X,A,x_0)$, only two terms following it, and none at $\pi_0(A,B,x_0)$, there being no exactness assertion at a last term with no map out of it. At each of the three the chase below shows that the fibre of the vertical map over the base point is trivial. That is not injectivity, and injectivity is not claimed: injectivity at a map of pointed sets says that two classes with the same image are equal, and the chase's fix-up multiplies by the difference of two such classes, which a pointed set does not provide.

- *The window centred at $\pi_2(X,A,x_0)$*, whose four surrounding maps are $\alpha:\pi_2(A,B)\to\pi_2(C,D)$, $\beta:\pi_2(X,B)\to\pi_2(Y,D)$, $\delta:\pi_1(A,B)\to\pi_1(C,D)$ and $\varepsilon:\pi_1(X,B)\to\pi_1(Y,D)$, and whose centre's neighbours are $h:\pi_2(X,A)\to\pi_1(A,B)$ and $h':\pi_2(Y,C)\to\pi_1(C,D)$. Let $\gamma(c)=1$. Then $\delta h(c)=h'\gamma(c)=1$, so $h(c)=1$ because $\delta$ is injective, hence $c=g(b)$ for some $b\in\pi_2(X,B)$ by exactness at $\pi_2(X,A)$; then $g'\beta(b)=\gamma g(b)=1$, so $\beta(b)=f'(a')$ for some $a'$, and $a'=\alpha(a)$ because $\alpha$ is onto, so $\beta(b)=\beta f(a)$ and $b=f(a)$ by injectivity of $\beta$; hence $c=gf(a)=1$ by exactness at $\pi_2(A,B)$. Every equality in this paragraph is an exactness statement at a group --- $\pi_2$ of a pair is a group for $n\ge2$ --- and the pointed sets enter only through the bijections at the surrounding terms. Its surjectivity half does fail for want of a group: it is the same step as at the second window of part (a), where the map out of the centre's target into a pointed set is not a homomorphism, and it is not proved here.
- *At $\pi_1(A,B,x_0)$*, with $i:\pi_1(A,B)\to\pi_1(X,B)$, $j:\pi_1(X,B)\to\pi_1(X,A)$ and $\partial:\pi_2(X,A)\to\pi_1(A,B)$ the boundary map of the triple, and the corresponding primed maps. Let $\gamma(c)=1$. Then $\delta i(c)=i'\gamma(c)=1$, so $i(c)=1$ because $\delta$ is injective, hence $c=\partial(b)$ for some $b$ by exactness at $\pi_1(A,B)$. Then $1=\gamma(c)=\partial'\beta(b)$, so $\beta(b)\in\ker\partial'=\operatorname{im}\bigl(\pi_2(Y,D)\to\pi_2(Y,C)\bigr)$, say $\beta(b)=f'(a')$, and $a'=\alpha(a)$ because $\alpha$ is onto, so $\beta(b)=\beta f(a)$ and $b=f(a)$ by injectivity of $\beta$; hence $c=\partial f(a)=1$ by exactness at $\pi_2(X,A)$.
- *At $\pi_1(X,B,x_0)$.* Let $\delta(c)=1$. Then $\varepsilon j(c)=j'\delta(c)=1$, so $j(c)=1$ because $\varepsilon$ is injective, hence $c=i(b)$ for some $b$ by exactness at $\pi_1(X,B)$. Then $1=\delta(c)=i'\gamma(b)$, so $\gamma(b)\in\ker i'=\operatorname{im}\partial'$ by exactness at $\pi_1(C,D)$, say $\gamma(b)=\partial'\beta(\mu)=\gamma\partial(\mu)$; hence $b=\partial(\mu)$ by injectivity of $\gamma$, and $c=i\partial(\mu)=1$ by exactness at $\pi_1(A,B)$.

So of the two halves at the three set-valued windows, the card proves the triviality of the fibre over the base point and neither direction of the exercise's claim as such. The surjectivity halves are not established, and nothing here asserts them. The chase's fix-up multiplies by the difference of two elements lying over the same class, which needs a group at the centre, and both centres at $\pi_1(A,B,x_0)$ and $\pi_1(X,B,x_0)$ are pointed sets; at the window centred at $\pi_2(X,A,x_0)$ the centre is a group but the chase's last step is the map into the pointed set $\pi_1(A,B,x_0)$, which is not a homomorphism; and the path fix-up that serves at $\pi_1(X,A,x_0)$ in part (a) turns on measuring the start point of a class in $\pi_0(A,x_0)$, whereas at these windows the difference of two classes with the same image in $\pi_1(Y,C)$ is a path in $B$ between two interior points of $B$, not a class ending at the basepoint, so it is not an element of $\pi_1(C,D,y_0)$ to correct by. What is proved about the terminal term is the quotient statement on which Claim 2 rests: $\pi_0(A,B,x_0)=\pi_0(A,x_0)/i_*\pi_0(B,x_0)$, and a bijection $\pi_0(A,x_0)\to\pi_0(C,y_0)$ which carries $i_*\pi_0(B,x_0)$ onto $i'_*\pi_0(D,y_0)$ induces a bijection $\pi_0(A,B,x_0)\to\pi_0(C,D,y_0)$; so bijectivity of the vertical maps at $\pi_0(A,x_0)$ and at $\pi_0(B,x_0)$ forces bijectivity at $\pi_0(A,B,x_0)$.
:::

::: {.remark title="Sources"}

The exercise is Exercise 9 of §4.1, printed p. 358, read in the text version `tmp/sources/hatcher-2002-algebraic-topology.md`, stated with the errata's $i_*$ in place of $i^*$. The printed claim (a) is proved on this card at every window: at every term of degree $\ge2$, by the group chase; at both set-valued terms $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$, where it is carried by the declarations `relativePiOne_map_bijective` and `zerothHomotopySubtypeMap_bijective` of [`LeanCategories/Topology/PairHomotopySequence.lean`](https://github.com/dzackgarza/lean-categories/blob/9b8b85840c2b5cef55942b971c65e3b4bfc0d252/LeanCategories/Topology/PairHomotopySequence.lean) on `lean-categories` main, with $\pi_1(X,A,x_0)$ read as Hatcher's quotient in which the start point moves inside $A$ (printed p. 343); at the term $\pi_0(X,x_0)$, by Claim 1; and at the two windows centered at $\pi_1(A,x_0)$ and at $\pi_1(X,x_0)$, by the argument of part (a), whose only non-group step is replaced by the exactness assertion at the centre's target. For part (b) the group windows are proved; at the three windows of the triple ladder that contain a pointed set --- those centred at $\pi_2(X,A,x_0)$, $\pi_1(A,B,x_0)$ and $\pi_1(X,B,x_0)$ --- the card proves that the fibre of the vertical map over the base point is trivial, and states that neither injectivity nor surjectivity is proved there as such, with the reason. No published treatment of this exercise was located, in the retained sets or in the sources searched for it.

A related published statement, cited for exactly what it proves: **R. Brown, *Fibrations of groupoids*, Journal of Algebra 15 (1970), 103--132**, Theorem 4.9 on printed p. 121 and Corollary 4.11 on printed p. 123 (reading copy `tmp/sources/brown-1970-fibrations-of-groupoids.md`). For a fibration of groupoids $p:G\to H$ with fibre $F$ over an object $v$, Brown's 4.9(a) concludes that $f:\pi_0F\to\pi_0F'$ is surjective if the maps of vertex groups $h:H(v)\to H'(v')$ and of components $g:\pi_0G\to\pi_0G'$ are surjective and $h:\pi_0H\to\pi_0H'$ is injective, and 4.9(b) concludes that $f$ is injective on $\ker(i:\pi_0F\to\pi_0G)$ if $h:H(v)\to H'(v')$ is injective and $g:G(x)\to G'(x')$ is surjective; Corollary 4.11 concludes that $h:H\to H'$ and $g:G\to G'$ being equivalences of groupoids forces $f:F\to F'$ to be an equivalence, in particular $f:\pi_0F\to\pi_0F'$ to be a bijection, the proof applying 4.9 and then the ordinary five-lemma for groups to Brown's diagram 4.8. That is a five-lemma at the $\pi_0$ term, and its hypotheses are stronger than the exercise's: an equivalence of groupoids is a bijection on hom-sets at every object and on components, which is the exercise's "for all choices of $x_0$" in a setting where a fibration supplies the exact sequence. It is a statement about fibrations of groupoids, and the map of pairs $(X,A)\to(Y,B)$ is not one, so nothing on this card rests on it: it is the related statement, for groupoids, of the five-lemma at the $\pi_0$ term that the two declarations above prove for the pair sequence.

:::
