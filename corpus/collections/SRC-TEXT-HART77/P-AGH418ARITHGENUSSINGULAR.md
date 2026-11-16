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
    ed88ff78, compiled 14 July 2026 (tmp/sources/stacks-project-book.pdf), cited
    as that book's folios and not as a
    text read: the whole compiled book has no text version, and every
    quotation in this note is from the tag file.
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
    version ed88ff78, compiled 14 July 2026 (the retained compiled
    tmp/sources/stacks-project-book.pdf, whose title page prints both; the book
    is a folio reference only, since it has no text version, the quotations
    being those of the tag files). The page
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
singular locus. This is Lemma 33.41.2 (tag 0C1R) of the Stacks Project, printed p. 2904, which also gives the exact sequence $0\to\mco_X\to\nu_*\mco_{X^\nu}\to\bigoplus_x Q_x\to0$ with $\length Q_x$ the $\delta$-invariant of $X$ at $x$; that is the sequence the exercise states.

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

This is the Stacks Project's argument, Chapter 33, Section 33.39, printed pp. 2899--2901, transcribed: Definition 33.39.3 (tag 0C3T) sets $\delta$ to be a length, and Lemma 33.39.6 (tag 0C3W) proves that this length does not change under henselization, strict henselization or completion, so $\delta$ is unchanged by completion; Definition 33.39.7 (tag 0C1T) attaches $\delta$ to a point $x$ through $\mathcal O_{X,x}$, and the two together make $\delta_P$ depend only on the completed local ring $\widehat{\mathcal O}_{X,P}$. Read tag by tag in `tmp/sources/stacks-tags/0C3T.md`, `0C3S.md`, `0C3V.md`, `0C3W.md` and `0C1T.md`, the site's build from stacks-project commit a04446e57ec1fbc252a871afcec7752fb2807b14 (28 July 2026); the page numbers are those of the retained compiled book of version ed88ff78, compiled 14 July 2026. In detail, with the notation below:

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
which is Lemma 33.39.6 (tag 0C3W) with $B\otimes_A\widehat A=(A')^{\wedge}$; the same lemma and Lemma 33.41.2(9) (tag 0C1R), printed p. 2904, give it directly as $A'/A\cong(A')^{\wedge}/A^{\wedge}$.

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

Up to analytic isomorphism, an ordinary cusp has completed local ring
$$
\widehat A
\cong
k[[t^2,t^3]]
\subseteq
k[[t]].
$$
Its normalization is $k[[t]]$. Every power $t^n$ with $n\ge2$ lies in
$k[[t^2,t^3]]$, so every series in $k[[t]]$ is congruent modulo
$k[[t^2,t^3]]$ to a unique scalar multiple of $t$. Hence
$$
k[[t]]/k[[t^2,t^3]]
\cong
k\cdot t
$$
as a $k$-vector space. This quotient has length $1$. Step [](#s6){.pf-ref} therefore
gives
$$
\delta_P=1.
$$

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
k[[x,y]]/(xy).
$$
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
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.1.8, printed pp. 208–209, text version `tmp/sources/hartshorne-solutions-egbert.md`, proves (a) by the short exact sequence $0\to\widetilde\OO_P/\OO_P\to H^0(X,\OO_X)\to H^0(\tilde X,\OO_{\tilde X})\to0$ obtained from (III.4.1) and the flasqueness of the skyscraper summand, so that $p_a(X)=p_a(\tilde X)+\sum_P\delta_P$, and (b) by observing that $p_a=0$ forces $\delta_P=0$ for every $P$, making all local rings normal and hence regular in dimension one.
For part (c), the invariance of $\delta_P$ under analytic isomorphism is the Stacks Project's, Chapter 33, Section 33.39, read in `tmp/sources/stacks-tags/0C3T.md` and `0C3W.md` (site built from stacks-project commit a04446e57ec1fbc252a871afcec7752fb2807b14, 28 July 2026): Definition 33.39.3 (tag 0C3T) with Lemma 33.39.6 (tag 0C3W), printed pp. 2899--2901 of the retained compiled book of version ed88ff78, shows that $\delta$ is unchanged by henselization, strict henselization and completion, hence depends only on the completed local ring, and Definition 33.39.7 (tag 0C1T) is the definition that attaches $\delta$ to the point $P$ through $\mathcal O_{X,P}$; step [](#s6){.pf-ref} transcribes it. The two values $\delta_P=1$ at an ordinary cusp and at a node (steps [](#s7){.pf-ref} and [](#s8){.pf-ref}) are computed here: $k[[t]]/k[[t^2,t^3]]\cong k\cdot t$ and $(k[[x]]\times k[[y]])/k[[x,y]]/(xy)\cong k$.

:::
