---
schema: qual/card@1
id: P-AGH555ELEMTRANSFORM
kind: problem
title: Ruled surfaces over a fixed curve are linked by elementary transformations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.5.5 as transcribed here, the retained Andrew Egbert
    entry, V.2.5 and the ruled-surface section/bundle conventions. The
    retained entry contains only the sentence that this is a consequence of
    its proof of V.2.5(a), while the printed hint proposes first changing the
    invariant e by elementary transformations and then using decomposability
    for e sufficiently large. The proof below verifies the stated
    self-intersection drop but completes the argument directly at the
    equivalent vector-bundle level: an elementary transform is a length-one
    elementary modification 0 -> F -> E -> k(p) -> 0, and two rank-two
    bundles become lattices in one generic two-dimensional vector space.
    After one harmless line-bundle twist their quotient has finite length,
    so a composition series factors the difference into finitely many such
    elementary modifications.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof against the ruled-surface quotient convention
    and the local point-blowup model. Checked that for
    F=ker(E->k(p)) one can choose E_p=Re1+Re2 and F_p=Re1+Rt e2, giving the
    rational map [x:y]->[x:ty]; its graph is the blowup at the corresponding
    fibre point and it contracts the strict transform of that fibre. Its
    inverse has the same form, so elementary transformations reverse.
    Checked also that a generic isomorphism E_eta~=E'_eta extends after an
    effective line-bundle twist to an injection with finite-length torsion
    quotient, whose composition series has k(p)-factors; the inverse images
    are torsion-free rank-two sheaves and hence locally free on the smooth
    curve. Thus every step is an elementary transformation and twisting the
    final bundle does not change its projectivization.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The published-solution remark now says what the two located entries contain.
    Egbert's V.5.5 is one sentence, a cross-reference to his V.2.5(a), on printed
    p. 299 of tmp/sources/hartshorne-solutions-egbert.pdf, whose MinerU text
    version tmp/sources/hartshorne-solutions-egbert.md carries the same sentence
    at its line 12794. Yang Pi-Yeh's Solution
    5.5.5 runs on printed pp. 113--114 of
    tmp/sources/lfwin-hartshorne-solutions.pdf: it opens at the foot of p. 113,
    p. 114 opens with the tail of that page's last sentence ("... we may assume
    E and E' are" / "decomposable with E = O_C + L and E' = O_C + L'"), and four
    whole sentences follow it above 5.5.6, which is Hartshorne V.5.6 --- the one
    asserting fraktur-e-tilde = fraktur-e + P "by definition", the one saying "we
    may blow-up X and X' more and assume fraktur-e = fraktur-e'", the one
    concluding X = X', and the last, "So there is a finite sequence of elementary
    transformations which transform X into X'"; its outline is right and three steps
    are missing or
    wrong: the sign of the elementary transform under Hartshorne's e = -deg
    fraktur-e of (2.8.1), the effect of elm_P on the normalized bundle, which he
    asserts "by definition", and the implicit choice of the points whose classes
    must be matched, which needs Riemann-Roch. There is no complete published
    proof of V.5.5 among the retained sets, so the card's own proof carries it
    and the entry in COMPLAINTS.md now says so.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    One sentence of Yang Pi-Yeh's entry, on a reader's report of issue #121,
    re-read on the printed folio of tmp/sources/lfwin-hartshorne-solutions.pdf.
    The event above called the two sentences at the head of p. 114 his last two.
    Read on the rendered page, p. 114 carries the tail of the sentence begun at
    the foot of p. 113 ("... we may assume E and E' are" / "decomposable with
    E = O_C + L and E' = O_C + L'") and then four whole sentences before 5.5.6:
    the "by definition" sentence, "So we may blow-up X and X' more and assume
    fraktur-e = fraktur-e'", "Hence X = X'", and "So there is a finite sequence
    of elementary transformations which transform X into X'". The page range
    pp. 113--114 is unchanged: the entry opens at the foot of p. 113.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The event above first read "p. 114 therefore carries three sentences of his
    entry, not two", and that was still an undercount: p. 114 carries the tail of
    the p. 113 sentence and four whole sentences. Read the same way, the symbols
    he equates are the fraktur divisor class of Hartshorne (2.8.1) and not the
    integer e: the print reads "If L = L(e), for any P in C_0, by definition,
    elm_P X has e-tilde = e + P" and "assume e = e'", with the e's set in
    fraktur, while the p. 113 line above them, "the new ruled surface
    elm_P X has e-tilde = e + 1", is the integer invariant. The remark now quotes
    the fraktur in both places, and its third gap --- that the classes, not the
    integer, are what must be matched --- is the reading the print supports.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The third gap's quotation made verbatim, on a reader's report of issue #121.
    The remark had paraphrased the sentence as "We may blow up X and X' more and
    assume fraktur-e = fraktur-e'"; the print reads "So we may blow-up X and X'
    more and assume fraktur-e = fraktur-e'", with the hyphen in "blow-up", the
    sentence opening with "So", and the fraktur class. Read in
    tmp/sources/lfwin-hartshorne-solutions.md, the sentence is the eighth of
    Solution 5.5.5 and reads "So we may blow-up X and X0 more and assume e = e'",
    the MinerU text version writing the prime of X' as a zero and the fraktur as
    a plain e; the page image of p. 114 has X' and the fraktur. The card now
    quotes the printed reading and records the text version's two renderings. No
    claim of the card changes.

- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Under issue #121 the solution is now a transcription of the published
    proof, one step per printed statement. The source is Luis Fuentes and Manuel
    Pedreira, The Projective Theory of Ruled Surfaces, read in
    tmp/sources/projective-theory-ruled-surfaces.md and in the PDF, at these
    printed pages, all read off the PDF's own folios: Proposition 1.2 with the
    normalized sheaf and the invariant e = -deg(E), p. 2--3; Definition 4.3 of
    the elementary transform and its invertibility, p. 26; Proposition 4.4(2),(3)
    with the intersection formula C'.D' = C.D + nm - n mu_x(D) - m mu_x(C), whose
    unisecant case x in C and D gives C'.D' = C.D - 1, statement p. 26 and proof
    p. 27; Lemma 4.6, p. 28; Theorem 4.9, statement p. 30 and proof p. 31, that
    the elementary transform at a point of the minimum-self-intersection curve
    has e' = e + 1; Corollary 4.10, p. 31, that an indecomposable ruled surface
    is obtained from a decomposable one by finitely many elementary
    transformations; Corollary 4.11, p. 31, that any ruled surface over the curve
    is obtained from X times P^1 by finitely many of them; and Theorem 3.2(2),
    p. 15, for the bound e at most 2g - 2 on an indecomposable ruled surface,
    which Corollary 4.10 uses. Checked against the book: the construction is
    Hartshorne's elementary transformation of Example 5.7.1 (the hint's (5.7.1)),
    the self-intersection drop in Proposition 4.4(3) is the hint's first
    computation, Theorem 4.9 with Corollary 4.10 is the hint's second ("X can be
    transformed into a geometrically ruled surface with e much greater than 0"),
    and the third hint's reduction to the decomposable case is Corollary 4.11
    with Theorem 3.2 in place of the book's (2.12). What the transcription does
    not keep is this card's earlier bundle-level proof, which worked from a
    generic isomorphism of the two rank-two sheaves and a composition series of
    its cokernel and used no published statement; the published proof replaces it
    in full, and the exercise's three printed hints are all used at the steps
    named above.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Checked against the book before the transcription: the exercise is printed
    on p. 419 (the page whose PDF folio is 434), and it asks that two
    geometrically ruled surfaces over one curve be connected by finitely many
    elementary transformations, with the three hints for (i) the drop
    D-tilde squared = D squared - 1 for a section through the centre, (ii) raising
    the invariant e, and (iii) the decomposable case via (2.12). Checked in the
    source that Definition 4.3 is the same operation as Hartshorne's Example
    5.7.1, blow up the point and contract the strict transform of the fibre
    through it, and that the paper's unisecant curves are the sections of
    Hartshorne V.2. Also checked: Corollary 4.11 concludes the theorem for one
    ruled surface against X times P^1, so the exercise's two surfaces are joined
    by composing that sequence with the reverse of the other, which is what
    Definition 4.3's remark that the inverse of an elementary transform is one
    supplies; that last composition is the card's step and is stated as such.
    Not checked here: the printed pages of Lemma 4.6 and of Proposition 3.8,
    which the card does not cite, since the text version marks only twenty-page
    blocks and the folios were read from the PDF for the statements it does cite.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report of this day on the transcription, repaired on the card.
    (i) Sign error in the step that reaches a decomposable surface from
    C x P^1. Theorem 4.9 gives e' ~ e - P at each elementary transform, and the
    points are chosen with -e_0 ~ P_1 + ... + P_e, so the e steps carry the
    determinant O_C of the normalized sheaf of P(O_C + O_C) to O_C(e_0), not to
    O_C(-e_0); the class reached is e_0, which is what S_0 =
    P(O_C + O_C(e_0)) has. The step now reads O_C(e_0).
    (ii) Gap in the same step: Theorem 4.9 fixes only the determinant of the
    normalized sheaf, and an indecomposable normalized sheaf can share a
    determinant with a decomposable one, so it does not identify the surface
    reached with P(O_C + O_C(e_0)). Theorem 4.12(1) of the same paper, printed
    p. 31, supplies exactly that: if x lies on the minimum-self-intersection
    curve then the elementary transform is decomposable with e' ~ e - P, its
    proof being that X_0 and X_1 stay disjoint. The step now cites it, and the
    remark names it among the statements the proof rests on.
    (iii) The remark's provenance --- the tmp/sources paths, the block markers
    of the text versions, and the sentence that the PDF's folios confirm the
    pages --- is removed from the rendered page and recorded here. Read for this
    pass, in tmp/sources/projective-theory-ruled-surfaces.md, whose markers are
    twenty-page blocks of the paper's own PDF: Definition 4.3, printed p. 26;
    Theorem 4.9 with its proof, printed pp. 30--31; Corollary 4.10 and
    Corollary 4.11 with its proof, printed p. 31; and Theorem 4.12 with the
    proof of its first item, printed p. 31. Read also in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, printed p. 419 for the
    exercise. Not read here: Theorem 3.2, Proposition 3.8, Corollary 3.7 and
    Proposition 1.2 were not re-read on this pass, their pages on the card being
    those of earlier events; and no search was made outside the sources listed.
    No claim of the card's statement changes; the correction is in the step that
    reaches the decomposable surface.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report of this day, repaired here. (i) The source-checked event of
    this day above had been rewritten in place by e2d674f48d, which a dated
    record does not allow; it is restored to the text it was introduced with, and
    what that commit changed is recorded in the event it appended, which stands,
    including the correction that Lemma 4.6 is cited on the card at printed p. 28
    and its proof was read. (ii) The rendered remark listed the paper's printed
    pages as "their printed pages: Proposition 1.2 at p. 3, ... pp. 30--31",
    which is bookkeeping; the page references of the statements the proof uses
    now stand only in the steps and in this audit. Read for this pass:
    Fuentes--Pedreira, printed pp. 26--31, in
    tmp/sources/projective-theory-ruled-surfaces.md, whose markers are twenty-page
    blocks of the paper's PDF, and Hartshorne's exercise, printed p. 419, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, whose marker is the PDF
    page and whose printed page is the marker minus fifteen. Nothing else on the
    card changed.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Closed under #121 on the published proof that the transcription event of
    2026-11-16 names. Read for this pass in Luis Fuentes and Manuel Pedreira,
    *The Projective Theory of Ruled Surfaces*, on the PDF copy
    tmp/sources/projective-theory-ruled-surfaces.pdf, whose printed page is
    the PDF page (the folios 15, 26, 30, 31 and 32 were read on those pages):
    Theorem 3.2(2), printed p. 15; Definition 4.3 and Proposition 4.4, printed
    p. 26; Theorem 4.9, statement printed p. 30 and proof printed p. 31;
    Corollary 4.10, printed p. 31; Corollary 4.11, statement printed p. 31
    and proof printed p. 32; and Theorem 4.12(1), printed pp. 31--32. The
    proof of Corollary 4.11 is complete: Corollary 4.10 carries S to a
    decomposable S_0, its second paragraph carries C x P^1 to S_0 by
    elementary transformations at the points P_i f cap X_0 whose sum is
    -e_0, and composing with the inverse sequence, which Definition 4.3
    supplies, carries S to C x P^1. The card's steps transcribe these
    statements, and its step two-surfaces-joined supplies the passage from
    one ruled surface to another that the statement of the corollary leaves
    to the reader. No sentence of the card changes; the COMPLAINTS entry
    that still says V.5.5 keeps its own proof is superseded by the record of
    this date.
---

::: {.problem}
Let $C$ be a curve, and let $\pi: X \rightarrow C$ and $\pi^{\prime}: X^{\prime} \rightarrow C$ be two geometrically ruled surfaces over $C$.
Show that there is a finite sequence of elementary transformations (5.7.1) which transform $X$ into $X^{\prime}$.

Hints: First show if $D \subseteq X$ is a section of $\pi$ containing a point $P$, and if $\tilde{D}$ is the strict transform of $D$ by $\operatorname{elm}_P$, then $\widetilde{D}^2=D^2-1$.
Next show that $X$ can be transformed into a geometrically ruled surface $X^{\prime \prime}$ with invariant $e \gg 0$.
Then use (2.12), and study how the ruled surface $\PP(\mathcal{E})$ with $\mathcal{E}$ decomposable behaves under $\operatorname{elm}_P$.
:::

::: {.solution}
By Proposition 1.2 of Fuentes and Pedreira, printed p. 3, which is Hartshorne V.2.2, the two geometrically ruled surfaces are
$$
X=\PP(\mathcal E),\qquad X'=\PP(\mathcal E')
$$
for locally free sheaves $\mathcal E,\mathcal E'$ of rank $2$ on $C$, in the quotient convention of Hartshorne V.2. An elementary transformation is the operation of Hartshorne's Example 5.7.1, printed p. 416: blow up a point and contract the strict transform of the fibre through it (Definition 4.3 below, printed p. 26).

::: pf

::: {.pf-step #elementary-transform-and-its-inverse}
For a ruled surface $\pi:S\to C$ with invariant $e$ and minimum-self-intersection curve $X_0$, and a point $x\in S$ with $\pi(x)=P$, the elementary transform $S'=\operatorname{elm}_x(S)$ is built by blowing up $S$ at $x$, say $\epsilon:S_x\to S$ with exceptional divisor $E$, and contracting the strict transform $\widetilde{Pf}$ of the fibre through $x$, say $\sigma:S_x\to S'$. If $S'=\operatorname{elm}_x(S)$ then $S$ is the elementary transform of $S'$ at the point $y$ where $\widetilde{Pf}$ meets $E$.

::: pf-proof
This is Definition 4.3 of Fuentes and Pedreira, printed p. 26, including the closing sentence that the inverse of the elementary transform at $x$ is the elementary transform of $S'$ at $y$, the image under $\sigma$ of the intersection of the two exceptional divisors $\widetilde{Pf}$ and $E$. The blown-up surface is the same object in the two directions, so the operation is reversible by an operation of the same kind.
:::

:::

::: {.pf-step #intersection-formula}
Let $C$ and $D$ be a unisecant and an $m$-secant curve on $S$, and let $C',D'$ be their strict transforms on $S'$. Then
$$
C'\cdot D'=C\cdot D+nm-n\mu_x(D)-m\mu_x(C)
$$
for an $n$-secant $C$ and an $m$-secant $D$. In particular, for two sections,
$$
\boxed{\text{if } x\in C\cap D \text{ then } C'\cdot D'=C\cdot D-1.}
$$
Applied to $C=D$ a section through the centre $x$ this gives $\widetilde D^{\,2}=D^2-1$, the first computation of the printed hint.

::: pf-proof
This is Proposition 4.4(3) of Fuentes and Pedreira, statement printed p. 26 and proof printed p. 27. The proof computes $C'\cdot D'=\sigma^*(\sigma_*(\widetilde C))\cdot\widetilde D$ and uses
$$
\sigma^*(\sigma_*(\widetilde C))=\widetilde C+\bigl(\widetilde C\cdot\widetilde{Pf}\bigr)\widetilde{Pf},
\qquad
\widetilde C\cdot\widetilde{Pf}=C\cdot Pf-\mu_x(Pf)\mu_x(C)=n-\mu_x(C),
$$
with the intersection formulae of Proposition 4.2, whose items (6) and (7) give $\widetilde C\cdot\widetilde D=C\cdot D-\mu_x(C)\mu_x(D)$ for curves through $x$. Substituting gives the displayed formula, and for $n=m=1$ with $\mu_x(C)=\mu_x(D)=1$ it reads $C'\cdot D'=C\cdot D-1$.
:::

:::

::: {.pf-step #invariant-rises}
If $x\in X_0$ lies on the minimum-self-intersection curve and $\pi(x)=P$, then $S'=\operatorname{elm}_x(S)$ is again ruled over $C$, corresponds to a normalized sheaf $\mathcal E_0'$ with
$$
\bigwedge^2\mathcal E_0'\cong\OO_C(\mathfrak e-P),
\qquad\text{that is}\qquad e'=e+1,
$$
and its minimum-self-intersection curve is $X_0'$.

::: pf-proof
This is Theorem 4.9 of Fuentes and Pedreira, statement printed p. 30 and proof printed p. 31. The curve $X_0$ satisfies $X_0^2=-e$ and every other unisecant curve $D$ satisfies $D^2\ge-e$. By step [](#intersection-formula){.pf-ref}, $D'^2=D^2-1$ if $x\in D$ and $D'^2=D^2+1$ if $x\notin D$; so $X_0'^2=X_0^2-1$ and every other unisecant curve satisfies $D'^2\ge D^2-1\ge X_0^2-1=X_0'^2$. Hence $X_0'$ is the minimum-self-intersection curve of $S'$ and
$$
e'=-X_0'^2=-X_0^2+1=e+1.
$$
Lemma 4.6, printed p. 28, computes the normal bundle of a transformed section and gives $\OO_{X_0'}(X_0')\cong\OO_C(\mathfrak e-P)$, which is the divisor-class form of the same statement. This is the second computation of the printed hint: the invariant $e$ rises by one at each such transformation.
:::

:::

::: {.pf-step #decomposable-reachable}
Every indecomposable ruled surface over $C$ is obtained from a decomposable one by finitely many elementary transformations.

::: pf-proof
This is Corollary 4.10 of Fuentes and Pedreira, printed p. 31, with the proof printed there. Starting from an indecomposable $S_0$ with invariant $e_0$ and applying step [](#invariant-rises){.pf-ref} at a point of the minimum-self-intersection curve gives $S_1$ with $e_1=e_0+1$, and by step [](#elementary-transform-and-its-inverse){.pf-ref} the surface $S_0$ is obtained from $S_1$ by one elementary transformation, so iterating gives $S_n$ with $e_n=e_0+n$. By Theorem 3.2(2) of the same paper, printed p. 15, the invariant of an indecomposable ruled surface satisfies $e\le2g-2$. For $n$ large enough $e_n>2g-2$, and then $S_n$ is decomposable.
:::

:::

::: {.pf-step #from-the-product}
Every ruled surface over $C$ is obtained from $C\times\PP^1$ by finitely many elementary transformations.

::: pf-proof
This is Corollary 4.11 of Fuentes and Pedreira, printed p. 31. Let $S$ be a ruled surface over $C$. By step [](#decomposable-reachable){.pf-ref} a finite number of elementary transformations carries $S$ to a decomposable ruled surface
$$
S_0\cong\PP\bigl(\OO_C\oplus\OO_C(\mathfrak e_0)\bigr)
\qquad\text{with } -\mathfrak e_0 \text{ effective.}
$$
The product $C\times\PP^1$ corresponds to the decomposable model $\PP(\OO_C\oplus\OO_C)$; writing $-\mathfrak e_0\sim P_1+\cdots+P_e$, one makes elementary transformations of $\PP(\OO_C\oplus\OO_C)$ on its minimum-self-intersection curve at the points $P_if\cap X_0$. Each of those steps changes the determinant of the normalized sheaf by $\mathfrak e\mapsto\mathfrak e-P$, by Theorem 4.9 of step [](#invariant-rises){.pf-ref}, so the $e$ of them carry $\OO_C$ to $\OO_C(\mathfrak e_0)$, because $-\mathfrak e_0$ is congruent to $P_1+\cdots+P_e$. A determinant class fixes only $\bigwedge^2$ of the normalized sheaf, and at $e\le2g-2$ an indecomposable normalized sheaf can share it, so Theorem 4.9 alone does not identify the surface reached; Theorem 4.12(1) of the same paper, printed p. 31, does: the elementary transform of a decomposable ruled surface at a point of its minimum-self-intersection curve is again decomposable, with $\mathfrak e'\sim\mathfrak e-P$. Each of the $e$ steps therefore keeps the surface decomposable, and the decomposable normalized model with determinant $\OO_C(\mathfrak e_0)$ is $\PP(\OO_C\oplus\OO_C(\mathfrak e_0))\cong S_0$. So $S_0$, and with it $S$, is obtained from $C\times\PP^1$ by finitely many elementary transformations.
:::

:::

::: {.pf-step #two-surfaces-joined}
$X$ is transformed into $X'$ by a finite sequence of elementary transformations:
$$
\boxed{
X=\PP(\mathcal E)
\dashrightarrow
\cdots
\dashrightarrow
C\times\PP^1
\dashrightarrow
\cdots
\dashrightarrow
\PP(\mathcal E')=X'.
}
$$

::: pf-proof
By step [](#from-the-product){.pf-ref} there is a finite sequence of elementary transformations carrying $X$ to $C\times\PP^1$, and another carrying $X'$ to $C\times\PP^1$. Each transformation of the second sequence is reversible by an elementary transformation of the same kind, by step [](#elementary-transform-and-its-inverse){.pf-ref}; reversing it and composing the two finite sequences joins $X$ to $X'$ by finitely many elementary transformations.
:::

:::

::: pf-qed
Steps [](#elementary-transform-and-its-inverse){.pf-ref} and [](#intersection-formula){.pf-ref} identify the operation of Hartshorne's Example 5.7.1 with the abstract elementary transform and verify the first computation of the printed hint, the self-intersection drop for a section through the centre. Step [](#invariant-rises){.pf-ref} verifies the second computation, that the invariant rises by one at a point of the minimum-self-intersection curve, and steps [](#decomposable-reachable){.pf-ref} and [](#from-the-product){.pf-ref} give the third: a finite sequence of elementary transformations carries any ruled surface over $C$ to $C\times\PP^1$. Step [](#two-surfaces-joined){.pf-ref} composes the two sequences and reverses one, which is the exercise's assertion.
:::

:::
:::

::: {.remark title="Published solutions"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.5, exercise 5.5, printed p. 419. The operation is his Example 5.7.1, and the three printed hints are the three steps of the proof above: the drop $\widetilde D^{\,2}=D^2-1$ for a section through the centre is step [](#intersection-formula){.pf-ref}, the passage to a ruled surface with $e\gg0$ is steps [](#invariant-rises){.pf-ref} and [](#decomposable-reachable){.pf-ref}, and the decomposable case is step [](#from-the-product){.pf-ref}, where the paper's Theorem 3.2 takes the place of the book's (2.12).

Luis Fuentes and Manuel Pedreira, *The Projective Theory of Ruled Surfaces*, is a complete printed proof of the exercise: Corollary 4.11 states that any ruled surface over the curve is obtained from $X\times\PP^1$ by finitely many elementary transformations, and its proof rests on Corollary 4.10 (from a decomposable surface, via Theorem 4.9's $e'=e+1$ and the bound $e\le2g-2$ of Theorem 3.2 for indecomposable surfaces) and on Definition 4.3 and Proposition 4.4 for the operation and its intersection numbers. The decomposability of the surface reached from $X\times\PP^1$ is Theorem 4.12(1); Theorem 4.9 fixes only $\bigwedge^2$ of the normalized sheaf. The one point the statement of Corollary 4.11 leaves to the reader is the passage from one ruled surface to another, the corollary joining each of the two to $X\times\PP^1$; step [](#two-surfaces-joined){.pf-ref} composes the two sequences, using the reversibility that Definition 4.3 states.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.5.5, printed p. 299, says only "Consequence of my proof of exc V.2.5.a". That is a cross-reference, not a proof.

Yang Pi-Yeh, *Hartshorne Solutions*, Solution 5.5.5, printed pp. 113--114, is the nearest of the retained sets and its outline is the printed hint's. He writes the formula $C'\cdot D'=C\cdot D+ac-a\,\mu_P(D)-c\,\mu_P(C)$ for $C\sim aC_0+bf$ and $D\sim cC_0+df$, so that $\operatorname{elm}_P$ at $P\in C_0$ has invariant $e+1$, and finitely many transformations make $e,e'>2g-2$; there (2.12)(b) makes both bundles decomposable, and further transformations at points of $C_0$ change the divisor class $\mathfrak e$ by the class of the underlying point of $C$, so that the classes can be made equal, after which $X\cong X'$. As printed it has three gaps: the sign, since (2.8.1) sets $e=-\deg\mathfrak e$ and the kernel of $\mathcal E\to k(P)$ has determinant $(\bigwedge^2\mathcal E)(-P)$, so $\mathfrak e\mapsto\mathfrak e-P$ and $e\mapsto e+1$, not $\mathfrak e+P$; the effect of $\operatorname{elm}_P$ on the normalized bundle, which he asserts "by definition" and which is step [](#invariant-rises){.pf-ref} here; and the choice of the points whose classes must be matched, which needs that every class of degree at least $2g-1$ is effective, by Riemann--Roch, and is neither stated nor used there. His sentence "So we may blow-up $X$ and $X'$ more and assume $\mathfrak e=\mathfrak e'$" is the third gap in one line.
:::
