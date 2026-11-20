---
schema: qual/card@1
id: P-AGH213SURJLOCAL
kind: problem
title: Surjectivity of a sheaf morphism is a local lifting condition
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Surjectivity
  - Stalks
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry (1977), Chapter II, section 1,
    exercise 1.3, printed page 66 (PDF page 81 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, the checked-in
    extraction). The printed exercise reads: "(a) Let phi: F -> G be a morphism
    of sheaves on X. Show that phi is surjective if and only if the following
    condition holds: for every open set U of X, and for every s in G(U), there
    is a covering {U_i} of U and there are elements t_i in F(U_i) such that
    phi(t_i) = s|_{U_i} for all i. (b) Give an example of a surjective morphism
    of sheaves phi: F -> G, and an open set U such that phi(U): F(U) -> G(U) is
    not surjective." The card states exactly this. The proof of (a) was checked
    in both directions, and the example of (b), the exponential sequence on
    the punctured plane, was checked to be a morphism that is surjective on
    stalks (a disc is simply connected) but not on sections over the punctured
    plane.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read again for issue #164. The exercise is printed on p. 66 of Hartshorne,
    Algebraic Geometry (1977), II.1: the folio 66 is printed at the foot of PDF
    p. 81 of tmp/sources/hartshorne-1977-algebraic-geometry.pdf, whose text layer
    was read there, and the extraction
    tmp/sources/hartshorne-1977-algebraic-geometry.md carries the same exercise
    under its marker for PDF p. 81. The statement on the card is the printed one,
    part for part. Caution 1.2.1, printed p. 65 (PDF p. 80), is where the book
    states that a morphism is surjective if and only if it is surjective on
    stalks; that is the criterion the last line of part (a) uses. The proof of
    (a) in the direction (=>) is transcribed from Dongryul Kim, Solutions to
    Hartshorne's Algebraic Geometry, Chapter II §1, Exercise 2.1.3, PDF p. 3 (the
    folio printed on the page): the lift of the germ, its representative on a
    neighbourhood, the shrink on which the two sections agree, and the cover by
    the shrunk neighbourhoods are his. He writes of the direction (<=) only
    "the converse follows by 1.2.b", so the one line proving it is supplied on
    the card. Part (b) is his example -- the exponential map of the sheaf of
    holomorphic functions on C \ {0}, with the section z -- and he asserts
    without proof that z "doesn't have a global inverse"; the loop integral
    $\int_\gamma g'(z)\,dz = g(\gamma(2\pi)) - g(\gamma(0)) = 0$ against
    $\int_\gamma dz/z = 2\pi i$, and the construction of a primitive of $h'/h$
    on a disc that gives a logarithm, are the card's. Egbert, PDF pp. 59-60, and
    Saglam--Chris, PDF p. 1, were read and carry the same exercise with the same
    two omissions. Checked by typesetting the display with the project preamble
    in pdflatex: it renders one arrow with exp above it, not the doubled arrow
    the one-argument \surjectsvia produced. Not checked: the printed book, only
    the text layer of the retained PDF; and no other retained set was searched
    for a proof of the two omitted steps.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The event above says no other retained set was searched for a proof of the
    two steps Kim omits. They were searched in this pass. Steven V. Sam's
    solutions carry II.1.3 at printed p. 2 -- PDF p. 15 of
    tmp/sources/hartshorne-solutions-sam.pdf, whose text layer is mirrored and
    was read after reversing it; the running foot of that page reads
    "1 SHEAVES 2", so printed p. = PDF p. - 13 -- and prove part (a) in both
    directions: the lift of the germ with its representative on a neighbourhood,
    and the converse by an index i with P in U_i. His part (b) takes
    differentiation of analytic functions instead of the exponential: it is
    surjective on stalks because an analytic function has an antiderivative on a
    simply connected neighbourhood, and 1/z on C \ {0} has none, its integral
    over the unit circle being 2 pi i. The remark now says so. Cais, printed
    p. 1, and Cutrone--Marshburn, printed pp. 29--30, also carry the exercise;
    they were located in this pass but not read closely enough to be named on
    the card. Not checked: the printed copies of any of these sets.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Corrects the measurement in the 2026-11-19 event above, which says the
    display "renders one arrow with exp above it, not the doubled arrow the
    one-argument \surjectsvia produced". The page does render one arrow with exp
    above it, but the doubled arrow was never on the page: pdftotext read the
    text layer, where the macro body's second arrowhead,
    {\mathrel{\mkern-16mu}\rightarrow}, laid over the first to restore a normal
    head, prints as a second glyph whether or not the arguments are right. Four
    spans were typeset afterwards, one per document, with the author's preamble
    and each page read as an image. \surjectsvia{\exp}, the printed text, is
    correct there, the preamble declaring the macro with one optional and one
    mandatory argument, and is wrong against the macro the site ships, whose two
    parameters are both mandatory because _macro_arity in tools/qualc/emit.py
    reads them off the macro body: there exp goes below the arrow, a bare
    opening parenthesis above it, and the parenthesised pair loses its bracket.
    \surjectsvia{}{\exp} is the reverse, correct on the site and an unlabelled
    arrow with exp spilled as text beside it under the preamble.
    \xrightarrow{\ \exp\ } is correct under both, so the display is unchanged
    from a7eb7ed9d4, and \surjectsvia is not to be written in corpus/ or wiki/,
    no brace form satisfying both renderers. Not checked: the rendered page in a
    browser, the site being built in CI, and MathJax itself, the site-side
    column having been typeset as the macro vocabularies/macros.json defines it.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Issue #164, the reader's third NOT MET item: the proof of part (b) was the
    card's own argument on Kim's example, not a transcription. Kim prints the
    exponential sequence and the assertion that z has no global inverse, and
    proves neither; the loop integral and the local logarithm were the card's,
    and the remark said so. Steven V. Sam solves the exercise in full on
    printed p. 2 -- PDF p. 15 of tmp/sources/hartshorne-solutions-sam.pdf, read
    as a 150 dpi page image, whose running head reads "1 SHEAVES 2" -- proving
    (a) in both directions and (b) by differentiation of analytic functions.
    The solution now transcribes him: part (a) in both directions, and for (b)
    his example, surjective on stalks because an analytic function has an
    antiderivative on a simply connected neighbourhood, and 1/z on C \ {0}
    without one since its integral over the unit circle is 2 pi i. The
    exponential sequence stays in the remark as Kim's, with the display the
    issue's first acceptance item names, and the remark records that the two
    steps his assertion needs are absent from his set and are not used above.
    Not checked: the printed Sam, only the retained PDF's page image; and
    Kim's set only in its retained text version.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Corrects the event above at part (a), direction (<=). Sam proves that
    direction for a global section s in G(X) and a covering of X, which gives
    surjectivity of phi_P only on germs of global sections of G; Hartshorne's
    condition quantifies over every open set U, and the proof must apply it to
    the neighbourhood on which the germ s_P is represented. The edit is one
    line, it is marked on the card as the card's adaptation, and the statement
    of (a) and the transcription of (b) are unchanged. Found by the
    source-verification run on this issue, not by the reader.
---


::: {.problem}
(a) Let $\varphi: \mcf \to \mcg$ be a morphism of sheaves on $X$.
   Show that $\varphi$ is surjective if and only if the following condition holds: for every open set $U \subseteq X$ and every $s \in \mcg(U)$, there is a covering $\theset{U_i}$ of $U$ and elements $t_i \in \mcf(U_i)$ such that $\varphi(t_i) = \restrictionof{s}{U_i}$ for all $i$.

(b) Give an example of a surjective morphism of sheaves $\varphi: \mcf \to \mcg$ and an open set $U$ such that $\varphi(U): \mcf(U) \to \mcg(U)$ is not surjective.
:::

::: {.solution}
**Part (a).** The argument is transcribed from Steven V. Sam, *Solutions to Hartshorne's Algebraic Geometry*, Chapter II §1, Exercise 3, printed p. 2 (PDF p. 15 of `tmp/sources/hartshorne-solutions-sam.pdf`, whose running head reads "1 SHEAVES 2"), where both directions are written out.

($\Rightarrow$) By (1.2(b)), $\varphi$ is surjective if and only if $\varphi_P$ is surjective for every point $P \in X$.
Suppose $\varphi_P$ is surjective for every $P \in X$.
Let $U \subseteq X$ be an open set and $s \in \mcg(U)$.
There exists an element $t_P \in \mcf_P$ such that $\varphi_P(t_P) = s_P$, which means that $t_P$ has a representative $t$ on some neighbourhood $U_P$ of $P$ with $\varphi(\restrictionof{t}{U_P}) = \restrictionof{s}{U_P}$.
Then $\theset{U_P}$ is a covering of $U$, and the condition holds.

($\Leftarrow$) Conversely, suppose that the condition holds.
Let $P \in X$ and let $s_P \in \mcg_P$ be represented by a section $s$ on an open neighbourhood $U$ of $P$.
The condition applied to $U$ gives an open covering $\theset{U_i}$ of $U$ and elements $t_i \in \mcf(U_i)$ such that $\varphi(t_i) = \restrictionof{s}{U_i}$ for all $i$, and some $i$ has $P \in U_i$, which gives $\varphi_P((t_i)_P) = s_P$.
So each $\varphi_P$ is surjective, and thus $\varphi$ is surjective.
Sam writes this direction with a global section $s \in \mcg(X)$ and a covering of $X$; the condition is stated for every open set, and applying it to the neighbourhood on which the germ is represented is the one adaptation made here, and is the card's.

**Part (b).** Also Sam, on the same page. Let $\mcf$ be the sheaf on $\CC$ with the usual topology that sends an open set $U$ to the group of all analytic functions on $U$, with the obvious restriction maps, and let $D: \mcf \to \mcf$ be differentiation: for an open set $U$, $D(U)$ sends $f$ to its derivative, which is also analytic.
An analytic function $f$ on an open set $U$ has an antiderivative if and only if the integral of $f$ over any closed contour in $U$ is $0$; in particular the integral over a closed contour $C$ is $0$ if $f$ is analytic in the region bounded by $C$.
For any open set $U$ and analytic function $f$ on $U$ there exists an open covering $\theset{U_i}$ of $U$ such that each $U_i$ is simply connected (take a small enough neighbourhood around each point).
Thus the integral of $f$ along any contour in $U_i$ is $0$, so $f$ has an antiderivative, which is of course analytic.
Using part (a), this means that $D$ is a surjective morphism of sheaves.
However let $U = \CCstar$.
The function $f(z) = 1/z$ is analytic on $U$, but has no antiderivative, since the integral of $1/z$ going counterclockwise along the unit circle is $2\pi i$; so $D(U): \mcf(U) \to \mcf(U)$ is not surjective.
:::

::: {.remark title="Published solution"}
The exercise is II.1.3 of Hartshorne, read in `tmp/sources/hartshorne-1977-algebraic-geometry.md`; the statement above is its text, part for part.

The proof above is Steven V. Sam's, *Solutions to Hartshorne's Algebraic Geometry*, Chapter II §1, Exercise 3, printed p. 2 (PDF p. 15 of `tmp/sources/hartshorne-solutions-sam.pdf`). He proves part (a) in both directions, the converse by the index $i$ with $P \in U_i$, and for part (b) takes differentiation of analytic functions: it is surjective on stalks because an analytic function has an antiderivative on a simply connected neighbourhood, and $1/z$ on $\CC^\times$ has none, its integral over the unit circle being $2\pi i$.

Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §1, Exercise 1.3 (his Exercise 2.1.3), the folio printed on the page, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`, solves the same exercise by the same two steps for (a), writing of the converse only that it "follows by 1.2.b", and takes for (b) the exponential sequence of sheaves on $\CC$,
$$
0 \to \underline{\ZZ} \injects (\OO_\CC, +) \xrightarrow{\ \exp\ } (\units{\OO_\CC}, \cdot) \to 0,
$$
with the section $z$ on $U = \CC^\times$: he asserts without proof that $z$ "doesn't have a global inverse", leaving the two steps the assertion needs, the loop integral that excludes a global logarithm and the construction of a logarithm on a disc that gives surjectivity on stalks, to the reader. That example is Kim's; the solution above is Sam's, and it is the one transcribed.

Egbert, PDF pp. 59--60, and Saglam--Chris, PDF p. 1, carry the same exercise and the same two omissions as Kim: each states that a logarithm exists locally and that the section $z$ has none globally, without proving either.
:::
