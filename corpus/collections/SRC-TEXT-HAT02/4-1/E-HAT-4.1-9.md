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
is exact as a sequence of pointed sets: the components mapping to the distinguished relative class are exactly those meeting $A$, and $j_*$ is onto. Exactness of the whole extended sequence at every other term is Theorem 4.3 (p. 344).

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

*Which windows these are.* The four terms of degree one or zero in the extended sequence are the pointed sets $\pi_1(X,A,x_0)$, $\pi_0(A,x_0)$, $\pi_0(X,x_0)$ and $\pi_0(X,A,x_0)$, and they occur in the order

$$
\cdots\to\pi_{n+1}(X)\to\pi_{n+1}(X,A)\to\pi_n(A)\to\pi_n(X)\to\pi_n(X,A)\to\pi_{n-1}(A)\to\cdots,
$$

so a window of five consecutive terms all of which are groups is exactly one centered at a term of degree $\ge2$. The windows centered at $\pi_1(A,x_0)$, $\pi_1(X,x_0)$, $\pi_1(X,A,x_0)$ and in degree $0$ contain a pointed set, and the group chase says nothing about them: the window centered at $\pi_1(A,x_0)$ reads $\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)$, whose last two terms are $\pi_1(X,A,x_0)$ — Hatcher's set of path classes in $X$ from a varying point of $A$ to $x_0$, which he notes on printed p. 343 is in general not a group in any natural way — and the pointed set $\pi_0(A,x_0)$; the window centered at $\pi_1(X,x_0)$ contains those same two together with $\pi_0(X,x_0)$. The windows centered at $\pi_1(X,A,x_0)$ and at $\pi_0(A,x_0)$ are proved below, and the one centered at $\pi_0(X,x_0)$ follows from the second of them by Claim 1; the two at $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$ are not proved, as recorded at the end of this part.

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

*The terms $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$.* The windows centered there have the group $\pi_1(A,x_0)$, respectively $\pi_1(X,x_0)$, as centre but the pointed set $\pi_1(X,A,x_0)$ among their four surrounding terms, so neither the group chase nor the two statements above reaches them; this card does not prove them and does not state them as true or as false. What it proves about the tail of the sequence is the two statements above together with the following.

*Claim 1.* If the vertical maps at $\pi_0(A,x_0)$ and at $\pi_0(X,x_0)$ are bijections, then so is the vertical map at $\pi_0(X,A,x_0)$. Indeed that map is induced by a bijection $\pi_0(X,x_0)\to\pi_0(Y,y_0)$ which carries the subset $i_*\pi_0(A,x_0)$ bijectively onto $i_*\pi_0(B,y_0)$, and a bijection of sets carrying one subset onto another induces a bijection of the quotients.

### (b) The triple sequence

For $B\subset A\subset X$ the triple sequence of Theorem 4.3 ends
$$
\cdots\longrightarrow\pi_1(X,A,x_0)\xrightarrow{\partial}\pi_0(A,B,x_0),
$$
and it cannot in general be continued by $\pi_0(X,B,x_0)$. Take $X$ the disjoint union of a point $b_0$ and an interval, $x_0=b_0$, and $B=\{b_0,b_1\}$ with $b_1$ a point of the interval; let $A=\{b_0,b_1,a_1\}$ with $a_1\neq b_1$ a further point of the interval, so that $b_1$ and $a_1$ lie in different components of the subspace $A$ while lying in the same component of $X$. Then the class of $a_1$ in $\pi_0(A,B,x_0)=\pi_0(A,x_0)/i_*\pi_0(B,x_0)$ is not the distinguished element, because its component of $A$ does not meet $B$; but its image in $\pi_0(X,B,x_0)$ is distinguished, because every component of $X$ that meets $B$ is collapsed and $a_1$ lies in the component of $b_1$. On the other hand the class of $a_1$ is not in the image of $\partial:\pi_1(X,A,x_0)\to\pi_0(A,B,x_0)$, since a path in $X$ starting in $A$ and ending at $x_0=b_0$ stays in the component $\{b_0\}$ of $X$, so its starting point lies in the component $\{b_0\}$ of $A$, which is collapsed. Hence appending $\pi_0(X,B,x_0)$ would destroy exactness at $\pi_0(A,B,x_0)$.

With the sequence ending at $\pi_0(A,B,x_0)$, the five-lemma holds for the ladder of triple sequences at every window that exists and consists of groups, and that is all the card proves. *The group windows.* The terms of the triple sequence in degree $\ge2$ are groups and every map between them is a homomorphism, so a window of five consecutive terms which all lie in degree $\ge2$ is a window of five group terms, and the chase of part (a) applies to it verbatim; exactness of the triple sequence is Theorem 4.3 (p. 344) and the ladder commutes by naturality (p. 345). *The last four terms.* The terms $\pi_1(A,B,x_0)$, $\pi_1(X,B,x_0)$ and $\pi_1(X,A,x_0)$ are pointed sets, and $\pi_0(A,B,x_0)$ is the last term of the sequence, so no window of five group terms is centred at any of them; the sequence also carries no exactness assertion at $\pi_0(A,B,x_0)$, there being no map out of it. The card does not prove a set-valued five-lemma for the triple sequence: the two set-valued statements it proves in part (a) use the group structure of $\pi_1$ at a point and the injectivity of the vertical at $\pi_0(X,x_0)$, and their certificate is the pair sequence's, not the triple's. What it does prove about the terminal term is the quotient statement on which Claim 1 rests: $\pi_0(A,B,x_0)=\pi_0(A,x_0)/i_*\pi_0(B,x_0)$, and a bijection $\pi_0(A,x_0)\to\pi_0(C,y_0)$ which carries $i_*\pi_0(B,x_0)$ onto $i'_*\pi_0(D,y_0)$ induces a bijection $\pi_0(A,B,x_0)\to\pi_0(C,D,y_0)$; so bijectivity of the vertical maps at $\pi_0(A,x_0)$ and at $\pi_0(B,x_0)$ forces bijectivity at $\pi_0(A,B,x_0)$.
:::

::: {.remark title="Sources"}

The exercise is Exercise 9 of §4.1, printed p. 358, stated with the errata's $i_*$ in place of $i^*$. The printed claim (a) is proved on this card at every term of degree $\ge2$, by the group chase, and at both set-valued terms, $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$, where it is carried by the declarations `relativePiOne_map_bijective` and `zerothHomotopySubtypeMap_bijective` of [`LeanCategories/Topology/PairHomotopySequence.lean`](https://github.com/dzackgarza/lean-categories/blob/9b8b85840c2b5cef55942b971c65e3b4bfc0d252/LeanCategories/Topology/PairHomotopySequence.lean) on `lean-categories` main, with $\pi_1(X,A,x_0)$ read as Hatcher's quotient in which the start point moves inside $A$ (printed p. 343). The two windows centered at $\pi_1(A,x_0)$ and at $\pi_1(X,x_0)$ are not treated on this card. No published treatment of this exercise was located, in the retained sets or in the sources searched for it.

A related published statement, cited for exactly what it proves: **R. Brown, *Fibrations of groupoids*, Journal of Algebra 15 (1970), 103--132**, Theorem 4.9 on printed p. 121 and Corollary 4.11 on printed p. 123 (reading copy `tmp/sources/brown-1970-fibrations-of-groupoids.md`). For a fibration of groupoids $p:G\to H$ with fibre $F$ over an object $v$, Brown's 4.9(a) concludes that $f:\pi_0F\to\pi_0F'$ is surjective if the maps of vertex groups $h:H(v)\to H'(v')$ and of components $g:\pi_0G\to\pi_0G'$ are surjective and $h:\pi_0H\to\pi_0H'$ is injective, and 4.9(b) concludes that $f$ is injective on $\ker(i:\pi_0F\to\pi_0G)$ if $h:H(v)\to H'(v')$ is injective and $g:G(x)\to G'(x')$ is surjective; Corollary 4.11 concludes that $h:H\to H'$ and $g:G\to G'$ being equivalences of groupoids forces $f:F\to F'$ to be an equivalence, in particular $f:\pi_0F\to\pi_0F'$ to be a bijection, the proof applying 4.9 and then the ordinary five-lemma for groups to Brown's diagram 4.8. That is a five-lemma at the $\pi_0$ term, and its hypotheses are stronger than the exercise's: an equivalence of groupoids is a bijection on hom-sets at every object and on components, which is the exercise's "for all choices of $x_0$" in a setting where a fibration supplies the exact sequence. It is a statement about fibrations of groupoids, and the map of pairs $(X,A)\to(Y,B)$ is not one, so nothing on this card rests on it: it is the related statement, for groupoids, of the five-lemma at the $\pi_0$ term that the two declarations above prove for the pair sequence.

:::
