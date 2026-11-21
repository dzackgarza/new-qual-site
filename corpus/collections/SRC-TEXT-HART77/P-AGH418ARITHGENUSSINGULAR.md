---
schema: qual/card@1
id: P-AGH418ARITHGENUSSINGULAR
kind: problem
title: The arithmetic genus of a singular curve and the local invariants $\delta_P$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Curves
  - Riemann-Roch
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.1.8 and its normalization exact sequence. Parts (a)--(b)
    are derived directly from cohomology. For part (c), the completion argument
    and the node/cusp normalization quotients were checked independently against
    the local delta-invariant conventions in the corpus.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), IV.1.8(c),
    printed p. 299. Published proof of the decisive step located: the Stacks
    Project, Chapter 33, Section 33.39 (The delta invariant) and Section 33.41,
    tag by tag, read in tmp/sources/stacks-tags/0C3T.md and the other tag files
    named below, which are the site's build from stacks-project commit
    a04446e57ec1fbc252a871afcec7752fb2807b14 (28 July 2026); the printed pages
    quoted here and below are those of the retained compiled book of version
    ed88ff78, compiled 14 July 2026 (tmp/sources/stacks-project-book.pdf).
    Definition 33.39.3 (tag 0C3T),
    printed p. 2899, sets delta = length_A(A'/A) for a reduced Nagata
    one-dimensional local ring, after Lemma 33.39.2 (tag 0C3S) makes A'/A of
    finite length; Lemma 33.39.5 (tag 0C3V), printed p. 2900, shows A' tensor_A
    A^h, A^sh and A^wedge are the integral closures of those rings; Lemma 33.39.6
    (tag 0C3W), printed pp. 2900--2901, proves delta is unchanged by
    henselization, strict henselization and completion, and Definition 33.39.7
    (tag 0C1T), printed p. 2901, attaches delta to a point x of a locally
    algebraic k-scheme through the local ring O_{X,x}; with 0C3W that gives the
    exercise's hint "delta_P depends only on the analytic isomorphism class",
    since two points of varieties over an algebraically closed field are
    analytically isomorphic exactly when their completed local rings are. (The
    first version of this note made 0C1T itself the statement of invariance
    under completion; the definition states no such thing, and the invariance is
    0C3W's.) Lemma 33.41.2 (tag 0C1R), printed p. 2904, gives
    the exercise's exact sequence 0 -> O_X -> nu_*O_{X^nu} -> direct sum Q_x -> 0
    with length Q_x = delta, and item (9) there is A'/A = (A')^wedge/A^wedge, the
    isomorphism step s6 uses. Step s6 is now the transcription of 0C3V, 0C3W and
    0C1R(9); the two computations at the cusp and the node (steps s7, s8) are the
    card's own and are not in that section. Nothing was checked in Stacks about
    analytic isomorphism as such; the identification used is the card's.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    The Stacks citations now carry the copy's version and compilation date,
    version ed88ff78, compiled 14 July 2026 (the retained
    tmp/sources/stacks-project-book.pdf, whose title page prints both). The page
    numbers in the body and in the event above are those of that copy:
    tag 0C3S/0C3T on printed p. 2899, 0C3V/0C3W on pp. 2900--2901, 0C1T on
    p. 2901, and 0C1R item (9) on p. 2904. Re-checked in the text layer by tag
    search that each of those tags carries the statement attributed to it; the
    step s6 transcription is unchanged.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Re-read against the replaced text versions. Each tag cited on this card is
    now a file of its own, tmp/sources/stacks-tags/<TAG>.md, holding the tag
    page's statement and proof with its LaTeX, from the site's build of
    stacks-project commit a04446e57ec1fbc252a871afcec7752fb2807b14 (28 July
    2026); the earlier notes' single-file reference and their version are
    replaced accordingly, and their printed pages are the retained compiled
    book's and were re-checked there. Checked tag by tag that the file says what
    this card attributes to it: 0C3S (A'/A has finite length), 0C3T (delta =
    length_A(A'/A)), 0C3V (A' tensor A^h, A^sh, A^wedge are the integral
    closures), 0C3W (delta unchanged by henselization, strict henselization and
    completion), 0C1T (delta of X at x through O_{X,x}) and 0C1R (the exact
    sequence, and item (9) A'/A = (A')^wedge/A^wedge). Two attributions were
    wrong and are corrected above: the invariance under completion is 0C3W's,
    not 0C1T's, and the item (9) that step s6 uses belongs to 0C1R.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on the reader's report of this batch. The printed page of the
    exercise is 298, not 299: all of IV.1.8 including (c) stands on PDF p.
    313 of the text version tmp/sources/hartshorne-1977-algebraic-geometry.md
    and printed = PDF - 15. The Egbert entry is transcribed correctly: his
    short exact sequence is 0 -> H^0(X, sum_P Otilde_P/O_P) -> H^1(X, O_X)
    -> H^1(Xtilde, O_Xtilde) -> 0, not the H^0 sequence the remark gave, and
    the remark now carries his. Steps s7 and s8 now cite the analytic normal
    forms they assert: the cusp's k[[t^2,t^3]] is I Ex. 5.14(d) on printed
    pp. 38-39, which assumes char k != 2, and the node's k[[x,y]]/(xy) is I
    Ex. 5.6(b) on printed p. 37 together with I Ex. 5.14(c) on printed p. 39,
    which carries no characteristic hypothesis. The quotient computations in
    s7 and s8 are unchanged and use no characteristic hypothesis. Checked
    against the book in this pass: IV.1.8 on PDF p. 313, I Ex. 5.6 on printed
    p. 37, I Ex. 5.14 on printed pp. 38-39. Not checked: nothing new; the
    Stacks tags were not re-read in this pass.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass on the reader's report of this batch, checked against the
    book's text version. Corrected the printed page of I Ex. 5.14(c): the
    statement that any two ordinary double points are analytically
    isomorphic stands on printed p. 38, which is PDF p. 53 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, not p. 39. Ex.
    5.14(d), the part that assumes char k != 2, begins on printed p. 38 and
    its list of conclusions continues on p. 39, so "printed pp. 38-39" is
    right for 5.14(d) alone. The same page is corrected where the event of
    2026-11-16 above, whose note begins "Repairs on the reader's report of
    this batch", gives p. 39 for 5.14(c); that event is named here and left
    as written. Step s7 is rewritten: it no longer quotes a normal form for
    a general ordinary cusp and then claims delta_P = 1 in every
    characteristic. It computes Hartshorne's cusp y^2 = x^3 of I Ex. 5.1
    directly, in every characteristic, from the normalization k[[t]] of
    k[[x,y]]/(y^2-x^3), which leaves a quotient of length 1; and it deduces
    the general case only for char k != 2, from I Ex. 5.14(d) together with
    the analytic invariance of delta in step s6. The restored event of
    2026-11-15 again says that the exercise stands on printed p. 299, as it
    was written; the correct page is printed p. 298 (PDF p. 313), and this
    note is the correction. Checked against the book in this pass: I Ex.
    5.14 in the text version, PDF pp. 52-54 = printed pp. 37-39; I Ex.
    5.6(b) on printed p. 37; I Ex. 5.1; IV.1.8 on PDF p. 313. Not checked:
    the Stacks tags were not re-read in this pass.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass on the reader's report of this batch, on the audit trail only.
    The event of 2026-11-16 whose note begins "Repairs on the reader's report
    of this batch" is restored as it was written, and this event is appended
    after it rather than put in its place; the sentence of the event above
    that names it therefore has its referent again, and the page it gives for
    I Ex. 5.14(c), printed p. 39, is corrected there and here to printed
    p. 38. The mathematics stands as the event above records it. Checked in
    this pass: nothing new; the Stacks tags were not re-read.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fourth pass, on the audit trail. Two events of 2026-11-15 above were edited
    in place on that same day by commit 9a74181332, before the gate held dated
    events. Unlike the events restored elsewhere in this batch, these keep the
    corrected text and the edit is disclosed here, because what the earlier
    text names is a file that is not on this machine: it reads "read in
    tmp/sources/stacks-project-book.md", and tmp/sources holds the compiled
    book as a PDF only, with no text version, so restoring it would put a
    citation that does not resolve back into the record. The corrections the
    edit carries are these. (i) The event
    whose note begins "Printed exercise read: Hartshorne, Algebraic Geometry
    (1977), IV.1.8(c)" had its reading sentence changed from "read in
    tmp/sources/stacks-project-book.md" to the passage-by-passage reading in
    tmp/sources/stacks-tags/0C3T.md and the other tag files, with the compiled
    book cited for folios only, and it had its account of Definition 33.39.7
    (tag 0C1T) changed from "concludes that delta is an invariant of the
    complete local ring" to the definition attaching delta to a point through
    the local ring, the invariance being drawn from tag 0C3W, with a
    parenthetical recording that the earlier account was wrong; its citation of
    0C1T(9) for the step s6 transcription became 0C1R(9). The later text is the
    correct one: 0C1T is a definition and states no invariance under
    completion, which is 0C3W's, and the card's step s6 cites 0C3V, 0C3W and
    0C1R(9). (ii) The event whose note begins "The Stacks citations now carry
    the copy's version and compilation date" had its parenthetical about the
    retained compiled book extended to say that the book is a folio reference
    only, having no text version, the quotations being the tag files'. Checked
    in this pass: this card's audit trail in git, commit by commit; the
    substance of both corrections is what the third pass above records. Not
    checked: no tag and no page was re-read in this pass.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fifth pass, on the two events of 2026-11-15 that the event above left
    carrying their in-place edits. Both are now restored to the text they
    carried at 9a74181332^, and what that commit added is stated here instead.
    (i) What 9a74181332 did. Two hunks, both clarifications of the retained
    compiled book: the first event gained "cited as that book's folios and not
    as a text read: the whole compiled book has no text version, and every
    quotation in this note is from the tag file", and the second gained "the
    book is a folio reference only, since it has no text version, the
    quotations being those of the tag files". Both statements are true and are
    made here: the copy at tmp/sources/stacks-project-book.pdf has no text
    version on this machine, so it is cited for printed folios only, and the
    text read for every quotation in the two events is the tag file -
    tmp/sources/stacks-tags/0C3S.md, 0C3T.md, 0C3V.md, 0C3W.md, 0C1T.md and
    0C1R.md - each of which is on the machine, as is the compiled book whose
    folios they are matched to. (ii) What the event above attributes to
    9a74181332 and that commit did not do. It says the restoration was
    declined because the earlier text names a file that is not on the
    machine, "read in tmp/sources/stacks-project-book.md". That sentence was
    removed by 8e2a3b3ebd earlier on the same day, together with the rewriting
    of the Definition 33.39.7 account into a definition and of 0C1T(9) into
    0C1R(9), which the event also attributes to 9a74181332; 9a74181332 made
    the two additions in (i) alone. The text restored here therefore names no
    missing file: it cites the compiled book by its PDF and the tag files by
    their own paths. (iii) The mathematics is unchanged by the restoration.
    The corrections this card carries stand as this batch's earlier events of
    2026-11-16 record them: the exercise is printed on p. 298, which is PDF
    p. 313 of tmp/sources/hartshorne-1977-algebraic-geometry.md, I Ex. 5.14(c)
    is on printed p. 38, and step s7 computes Hartshorne's cusp y^2 = x^3 in
    every characteristic. Checked in this pass: the history of this card at
    8e2a3b3ebd, 9a74181332^ and 9a74181332, the presence of the six tag files
    named and of the compiled book, and the restored text against
    9a74181332^. Not checked: no tag was re-read against its statement in this
    pass, and no page was re-read.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.1.8, printed p. 84,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.1.8, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed
    the exact sequence of structure sheaves, the vanishing of
    H^1 of the skyscraper quotient, and the two consequences in part (b). Not checked: Yang's Solutions outside printed pp. 84-85; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.1.8 at printed
    p. 84 beside the entry already there. No step, statement or
    hypothesis of the card changes.
---

::: {.problem}
Let $X$ be an integral projective scheme of dimension 1 over $k$, and let $\tilde{X}$ be its normalization (II, Ex.
3.8). Then there is an exact sequence of sheaves on $X$,
$$
0 \to \OO_X \to f_* \OO_{\tilde X} \to \sum_{P \in X} \tilde\OO_P/\OO_P \to 0
$$
where $\tilde\OO_P$ is the integral closure of $\OO_P$.
For each $P \in X$, let $\delta_P=\length(\tilde\OO_P/\OO_P)$.

(a) Show that $p_a(X)=p_a(\tilde{X})+\sum_{P \in X} \delta_P$.
Hint: Use (III, Ex.
4.1) and (III, Ex.
5.3).

(b) If $p_a(X)=0$, show that $X$ is already nonsingular and in fact isomorphic to $\PP^1$.
This strengthens (1.3.5).

(c) \* If $P$ is a node or an ordinary cusp (I, Ex.
5.6, Ex.
5.14), show that $\delta_P=1$.
Hint: Show first that $\delta_P$ depends only on the analytic isomorphism class of the singularity at $P$.
Then compute $\delta_P$ for the node and cusp of suitable plane cubic curves.
See (V, 3.9.3) for another method.
:::

::: {.solution}
Let
$$
\nu:\widetilde X\longrightarrow X
$$
be the normalization and put
$$
\mathcal Q
=
\nu_*\mco_{\widetilde X}/\mco_X.
$$
Thus
$$
\mathcal Q_P
=
\widetilde\mco_P/\mco_P,
\qquad
\length_{\mco_P}\mathcal Q_P
=
\delta_P.
$$

::: pf

::: {.pf-step #s1}

The sheaf $\mathcal Q$ is supported at finitely many closed points and
$$
\dim_kH^0(X,\mathcal Q)
=
\sum_{P\in X}\delta_P.
$$

::: pf-proof

The normalization is an isomorphism over the regular locus of the
one-dimensional scheme $X$. Hence $\mathcal Q$ is supported on the finite
singular locus. This is Lemma 33.41.2 (tag 0C1R) of the Stacks Project, which also gives the exact sequence $0\to\mco_X\to\nu_*\mco_{X^\nu}\to\bigoplus_x Q_x\to0$ with $\length Q_x$ the $\delta$-invariant of $X$ at $x$; that is the sequence the exercise states.

At a closed point $P$, the residue field is $k$ because $k$ is
algebraically closed. A finite-length $\mco_P$-module therefore has
$k$-dimension equal to its length. Since a sheaf supported on finitely
many closed points is the direct sum of its stalk skyscraper sheaves,
$$
H^0(X,\mathcal Q)
\cong
\bigoplus_{P\in X}\mathcal Q_P.
$$
Taking dimensions gives the formula.

:::

:::

::: {.pf-step #s2}

There is a short exact sequence
$$
0
\longrightarrow
H^0(X,\mathcal Q)
\longrightarrow
H^1(X,\mco_X)
\longrightarrow
H^1(\widetilde X,\mco_{\widetilde X})
\longrightarrow
0.
$$

::: pf-proof

Apply cohomology to
$$
0
\longrightarrow
\mco_X
\longrightarrow
\nu_*\mco_{\widetilde X}
\longrightarrow
\mathcal Q
\longrightarrow
0.
$$
Because $\nu$ is finite,
$$
H^i(X,\nu_*\mco_{\widetilde X})
\cong
H^i(\widetilde X,\mco_{\widetilde X}).
$$
Also
$$
H^1(X,\mathcal Q)=0
$$
because $\mathcal Q$ has zero-dimensional support.

Both $X$ and $\widetilde X$ are integral and projective, so
$$
H^0(X,\mco_X)
\cong
H^0(\widetilde X,\mco_{\widetilde X})
\cong
k.
$$
The first map is the identity on constants. The long exact sequence
therefore reduces to the displayed short exact sequence.

:::

:::

::: {.pf-step #s3}

One has
$$
\boxed{
p_a(X)
=
p_a(\widetilde X)
+
\sum_{P\in X}\delta_P.
}
$$

::: pf-proof

For an integral projective curve $C$ over $k$,
$$
p_a(C)
=
1-\chi(\mco_C)
=
h^1(C,\mco_C)
$$
because $h^0(C,\mco_C)=1$. Thus step [](#s2){.pf-ref} and step [](#s1){.pf-ref} give
$$
p_a(X)
=
p_a(\widetilde X)
+
\sum_{P\in X}\delta_P.
$$
This proves part (a).

:::

:::

::: {.pf-step #s4}

If $p_a(X)=0$, then $X$ is nonsingular.

::: pf-proof

By step [](#s3){.pf-ref},
$$
0
=
p_a(\widetilde X)
+
\sum_P\delta_P.
$$
The normalization $\widetilde X$ is a smooth projective curve, so
$p_a(\widetilde X)\ge0$, and every $\delta_P$ is a nonnegative integer.
Hence
$$
p_a(\widetilde X)=0
\qquad\text{and}\qquad
\delta_P=0
$$
for every $P$.

Thus
$$
\widetilde\mco_P=\mco_P
$$
for every $P$, so every local ring of $X$ is integrally closed. A
one-dimensional noetherian integrally closed local domain is a DVR and
therefore regular. Hence $X$ is nonsingular.

:::

:::

::: {.pf-step #s5}

If $p_a(X)=0$, then
$$
X\cong\PP^1.
$$

::: pf-proof

By step [](#s4){.pf-ref}, $X$ is a smooth projective curve. Its genus is
$$
g=p_a(X)=0.
$$
Exercise
[[P-AGH416MAPTOP1DEGREE|IV.1.6]]
gives a finite morphism
$$
f:X\longrightarrow\PP^1
$$
of degree at most $1$. Since $f$ is nonconstant, its degree is positive,
so
$$
\deg f=1.
$$
A finite degree-one morphism of integral smooth projective curves is
birational, and a finite birational morphism to the normal curve $\PP^1$
is an isomorphism. This proves part (b).

:::

:::

::: {.pf-step #s6}

The number $\delta_P$ depends only on the analytic isomorphism class of the singularity.

::: pf-proof

This is the Stacks Project's argument, Chapter 33, Section 33.39, transcribed: Definition 33.39.3 (tag 0C3T) sets $\delta$ to be a length, and Lemma 33.39.6 (tag 0C3W) proves that this length does not change under henselization, strict henselization or completion, so $\delta$ is unchanged by completion; Definition 33.39.7 (tag 0C1T) attaches $\delta$ to a point $x$ through $\mathcal O_{X,x}$, and the two together make $\delta_P$ depend only on the completed local ring $\widehat{\mathcal O}_{X,P}$. Read tag by tag in `tmp/sources/stacks-tags/0C3T.md`, `0C3S.md`, `0C3V.md`, `0C3W.md` and `0C1T.md`, the site's build from stacks-project commit a04446e57ec1fbc252a871afcec7752fb2807b14 (28 July 2026); the page numbers are those of the retained compiled book of version ed88ff78, compiled 14 July 2026. In detail, with the notation below:

Put
$$
A=\mco_{X,P},
\qquad
B=\widetilde\mco_P.
$$
The quotient
$$
B/A
$$
has finite length: $A$ is reduced and Nagata of dimension one, and $B$ is the integral closure in its total ring of fractions, which is Lemma 33.39.2 (tag 0C3S). Lemma 33.39.5 (tag 0C3V) shows that $B\otimes_A\widehat A$ is the integral closure of $\widehat A$ in its total ring of fractions. Then completion is exact on finite $A$-modules, and a
finite-length module is unchanged by completion. Hence
$$
\length_A(B/A)
=
\length_{\widehat A}
\left(
(B\otimes_A\widehat A)/\widehat A
\right),
$$
which is Lemma 33.39.6 (tag 0C3W) with $B\otimes_A\widehat A=(A')^{\wedge}$; the same lemma and Lemma 33.41.2(9) (tag 0C1R) give it directly as $A'/A\cong(A')^{\wedge}/A^{\wedge}$.

The local ring $A$ is essentially of finite type over a field, hence
excellent. For such a one-dimensional reduced local ring, normalization
commutes with completion: $B\otimes_A\widehat A$ is the normalization of
$\widehat A$ in its total ring of fractions. Therefore
$$
\delta_P
=
\length_{\widehat A}
\left(
\overline{\widehat A}/\widehat A
\right).
$$
The right-hand side depends only on the isomorphism class of the completed
local ring $\widehat A$. Thus $\delta_P$ is an analytic invariant.

:::

:::

::: {.pf-step #s7}

If $P$ is an ordinary cusp, then
$$
\delta_P=1.
$$

::: pf-proof

The cusp of (I, Ex. 5.1) is the plane curve $y^2=x^3$, with completed local
ring
$$
A=k[[x,y]]/(y^2-x^3).
$$
The element $t=y/x$ of the fraction field of $A$ satisfies $t^2=x$ and
$t^3=y$: the series $y^2-x^3$ is irreducible in every characteristic, since
$x^3$ is not a square in $k((x))$ and the polynomial is monic of degree two in
$y$, so $A$ is a domain and $x\ne0$. The map $k[[x,y]]\to k[[t]]$ sending
$x\mapsto t^2$, $y\mapsto t^3$ has image $k[[t^2,t^3]]$, which is
one-dimensional, so its kernel is a height-one prime containing the irreducible
element $y^2-x^3$ and is therefore $(y^2-x^3)$ itself. That gives an inclusion
$$
k[[t^2,t^3]]\subseteq B\subseteq k[[t]]
$$
of the normalization $B$ of $A$ with equality throughout: $t$ is integral over
$k[[t^2,t^3]]$, and $k[[t]]$ is a discrete valuation ring, hence integrally
closed. Every power $t^n$ with $n\ge2$ lies in $k[[t^2,t^3]]$, so every series
in $k[[t]]$ is congruent modulo $k[[t^2,t^3]]$ to a unique scalar multiple of
$t$. Hence
$$
k[[t]]/k[[t^2,t^3]]
\cong
k\cdot t
$$
as a $k$-vector space, a quotient of length $1$, and step [](#s6){.pf-ref} gives
$\delta_P=1$ for this cusp in every characteristic, including
characteristic $2$.

For an arbitrary ordinary cusp take $\operatorname{char}k\ne2$. Then (I, Ex.
5.14(d)) puts the completed local ring in the form
$k[[x,y]]/(y^2-x^r)$ with $r=3$, which is the ring computed above, and
$\delta_P$ is an analytic invariant by step [](#s6){.pf-ref}. So every ordinary
cusp has $\delta_P=1$ when $\operatorname{char}k\ne2$. That exercise assumes
$\operatorname{char}k\ne2$ and its normal form is not used here in
characteristic $2$: the computation covers the cusp $y^2=x^3$ of (I, Ex. 5.1)
in every characteristic, and in characteristic $2$ no normal form for a
general ordinary cusp is asserted.

:::

:::

::: {.pf-step #s8}

If $P$ is a node, then
$$
\delta_P=1.
$$

::: pf-proof

Up to analytic isomorphism, a node has completed local ring
$$
\widehat A
\cong
k[[x,y]]/(xy) :
$$
a node is a double point of a plane curve with two distinct tangent
directions (I, Ex. 5.6(b)), and any two ordinary double points
are analytically isomorphic, which is (I, Ex. 5.14(c)), and
carries no characteristic hypothesis, so this computation holds in every
characteristic.
Its normalization is
$$
k[[x]]\times k[[y]],
$$
with the map
$$
k[[x,y]]/(xy)
\longrightarrow
k[[x]]\times k[[y]]
$$
sending the class of a power series $h(x,y)$ to
$$
\bigl(h(x,0),h(0,y)\bigr).
$$
Its image consists exactly of the pairs
$$
(a(x),b(y))
$$
with the same constant term:
$$
a(0)=b(0).
$$
Therefore the homomorphism
$$
k[[x]]\times k[[y]]
\longrightarrow
k,
\qquad
(a,b)\longmapsto a(0)-b(0)
$$
is surjective and has image of $\widehat A$ as its kernel. Thus
$$
\bigl(k[[x]]\times k[[y]]\bigr)/\widehat A
\cong
k,
$$
which has length $1$. Step [](#s6){.pf-ref} gives
$$
\delta_P=1.
$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (a), steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (b), and
steps [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove part (c).

:::

:::

:::

::: {.remark title="Published solution"}
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.1.8, text version `tmp/sources/hartshorne-solutions-egbert.md`, proves (a) by the short exact sequence $0\to H^0(X,\sum_{P}\widetilde\OO_P/\OO_P)\to H^1(X,\OO_X)\to H^1(\tilde X,\OO_{\tilde X})\to0$ obtained from (III.4.1) and the flasqueness of the skyscraper summand, whence $h^1(X,\OO_X)=h^1(\tilde X,\OO_{\tilde X})+\sum_P\delta_P$ and so $p_a(X)=p_a(\tilde X)+\sum_P\delta_P$, and (b) by observing that $p_a=0$ forces $\delta_P=0$ for every $P$, making all local rings normal and hence regular in dimension one.
For part (c), the invariance of $\delta_P$ under analytic isomorphism is the Stacks Project's, Chapter 33, Section 33.39, read in `tmp/sources/stacks-tags/0C3T.md` and `0C3W.md` (site built from stacks-project commit a04446e57ec1fbc252a871afcec7752fb2807b14, 28 July 2026): Definition 33.39.3 (tag 0C3T) with Lemma 33.39.6 (tag 0C3W) of the retained compiled book of version ed88ff78 shows that $\delta$ is unchanged by henselization, strict henselization and completion, hence depends only on the completed local ring, and Definition 33.39.7 (tag 0C1T) is the definition that attaches $\delta$ to the point $P$ through $\mathcal O_{X,P}$; step [](#s6){.pf-ref} transcribes it. The two values $\delta_P=1$ at an ordinary cusp and at a node (steps [](#s7){.pf-ref} and [](#s8){.pf-ref}) are computed here: $k[[t]]/k[[t^2,t^3]]\cong k\cdot t$ and $(k[[x]]\times k[[y]])/k[[x,y]]/(xy)\cong k$.


Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.1.8 takes (a) from the exact sequence $0\to\OO_X\to f_*\OO_{\widetilde X}\to\sum_P\widetilde\OO_P/\OO_P\to0$: both outer $H^0$ are $k$ for projective curves, the quotient is a sum of skyscrapers so its $H^1$ vanishes, and the long exact sequence gives $p_a(X)=p_a(\widetilde X)+\sum_P\delta_P$. Its (b): $p_a=0$ forces every $\delta_P=0$, so every local ring is normal and the curve nonsingular, and then $p_a=0$ means genus zero, so $X\cong\PP^1$ by (1.3.5). Its (c) reduces to a plane curve by projecting, and computes $\delta_P$ from the local equation at a node or cusp.
:::
