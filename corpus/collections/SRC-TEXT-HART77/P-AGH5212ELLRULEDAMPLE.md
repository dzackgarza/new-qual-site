---
schema: qual/card@1
id: P-AGH5212ELLRULEDAMPLE
kind: problem
title: Base points and very ampleness on a ruled surface over an elliptic curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.2.12, the retained Egbert companion pointer to
    Fuentes--Pedreira, V.2.11, and the preceding stability and e=-1 elliptic
    ruled-surface cards. For e>=0, the assertions follow from V.2.11 and the
    degree-2/degree-3 base-point-free/very-ample thresholds on an elliptic
    curve. The exceptional e=-1 case is proved directly: the normalized
    rank-two bundle has degree 1 and is stable, so its twists have the H^1
    vanishings required for fibrewise generation and separation of all
    length-two subschemes. Necessity in (b) follows by restricting to C_0.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.2,
    exercise 2.12, printed page 385, with its Note on e = -1. Checked the card
    against the book: V.2.11 as printed on page 385 for the two applications in
    steps s2 and s7, V.2.8(b) proved on the card P-AGH528STABLEBUNDLE for
    stability of a normalized bundle of degree 1, IV.1.3 and IV.3.1 for the
    degree thresholds on an elliptic curve, V.2.5 and V.2.15 for the bound
    e >= -1 in step s6, and the divisor formula of V.2.9, printed page 373, for
    O_X(C_0) = O_X(1) and L restricted to C_0. All eleven steps were re-read;
    the only imported facts are V.2.11, V.2.8 and the invariant bound, and each
    is applied with its hypotheses verified (degrees at least 2 for base-point
    freeness and at least 3 for very ampleness, positive degrees after
    subtracting a point for nonspeciality in the elliptic case). Searched
    outside the twelve retained sets: NTU 2020 has no entry for Exercise 12 of
    section 2; Yang Pi-Yeh, Hartshorne Solutions, printed pp. 104-105
    (tmp/sources/lfwin-hartshorne-solutions.pdf), disposes of e >= 0 as trivial
    and its e = -1 computation is garbled. Egbert, PDF pp. 268-269, cites
    Fuentes-Pedreira 1.3 and 1.4 alone. Not checked: Fuentes-Pedreira, which is
    not in tmp/sources, so its criterion is neither used nor verified here.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The National Taiwan University set's text version is
    tmp/sources/ntu-ag2-chapter5.md, beside its PDF tmp/sources/ntu-ag2-chapter5.pdf,
    and the same holds for every published set cited here. The event above is as
    it was dated, with the text-version names that a later edit had removed
    restored on 2026-11-16.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes and Pedreira (arXiv:math/0006204v3), Sections 2 and 3, printed
    pp. 7 to 25, on 2026-11-16. Its Theorem 3.9(3), printed p. 18, states for a
    decomposable ruled surface that the system of C_0 + bf is very ample exactly
    when b and b+e are very ample. For an elliptic base with e at least zero that
    gives the criterion behind this exercise: both degrees must reach three, and
    deg(b+e) equals deg b - e because deg e is -e, so the bound of part (b) is
    deg b at least e+3, as printed. The proof of that equivalence is complete: it
    invokes Corollary 2.13, printed p. 14, whose criterion is
    h^0(H - (P+Q)f) = h^0(H) - 4 for all P and Q in the base, and that corollary
    is proved --- its converse is Proposition 2.3, printed p. 8, applied to the
    system $\linearsystem{H-Pf}$, a point at which the map fails being a base point
    of some $\linearsystem{H-Pf}$ by Theorem 2.11, printed pp. 12--13. An earlier note here recorded
    the converse as an assertion and the two-fibre condition as blind to tangent
    directions; both readings are withdrawn, since the case Q = P is exactly what
    Theorem 2.11 supplies. Proposition 2.15, printed p. 15, rests on the same
    corollary and is sound on the same footing, and Proposition 2.14, printed
    p. 14, is the step off the section. What the paper leaves open for this
    exercise is the exception it does not reach: e = -1, the Atiyah surface, which
    Theorem V.2.15 shows is the only indecomposable elliptic ruled surface with
    negative e, and the indecomposable bundles of invariant e = 0, which Section 3
    excludes with all indecomposable ones. For e = -1 sufficiency is step s9 and
    necessity step s10; for an indecomposable e = 0 sufficiency is step s7, which
    covers every e at least zero through the book's V.2.11(b), and necessity is
    step s10, the restriction to C_0.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Three corrections on 2026-11-16. The event of 2026-11-11 is restored to its
    text of that date, the text-version names a later commit had put into it
    being removed, and the event of 2026-11-16 that recorded their restoration
    stays as what that reading did; where a source is cited in the remark it
    names its text version, and the two sets the 2026-11-11 event cites without
    one are the National Taiwan University homework, text version
    tmp/sources/ntu-ag2-chapter5.md beside its PDF, and Egbert, text version
    tmp/sources/hartshorne-solutions-egbert.md beside his. The page range of
    Fuentes--Pedreira's Sections 2 and 3 was wrong: section 2 begins on printed
    p. 7, after the end of section 1 on that page, and section 4 has begun by
    printed p. 25, whose text is item 7 of the list in Proposition 4.2, so the
    two sections run from p. 7 to p. 25 if not a page further; the printed
    pages of that paper are its PDF pages, Theorem 3.9(3) on p. 18 as cited. And
    the event above had the exceptional cases the wrong way round: for an
    indecomposable bundle of invariant zero, sufficiency is step s7, which is
    the e at least zero case, and only necessity is step s10; steps s8 and s9
    are the Atiyah surface e = -1.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Transcription pass for issue #121 on 2026-11-16: the solution is now the
    published argument, and every step names its source, numbered statement and
    printed page. Read at the cited places, in their text versions and against
    their PDFs page by page, the extractions marking only 20-page ranges: Luis
    Fuentes, Classification of elliptic line scrolls (arXiv:math/0009050v1),
    tmp/sources/fuentes-2000-classification-elliptic-line-scrolls.md, Lemma 1.2
    printed pp. 2 to 3 and Propositions 1.3, 1.4, 1.5, 2.2, 2.3, 2.10 and 2.11,
    printed pp. 3 to 15; and Fuentes and Pedreira, The Projective Theory of
    Ruled Surfaces (arXiv:math/0006204v3),
    tmp/sources/projective-theory-ruled-surfaces.md, Theorem 3.9(3) printed
    p. 18, Corollary 2.13 printed p. 14, Corollary 2.9 printed p. 11, Proposition
    3.4 printed p. 16 and Theorem 3.2(1) with Remark 3.3, both printed p. 15. Checked against the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N is
    PDF p. N+15: V.2.12 as printed on p. 385 with its Note on e = -1, Theorem
    V.2.12 on p. 376 and Theorem V.2.15 on p. 377. What the transcription
    establishes: part (a) is Proposition 1.3 for e at least 0 and Proposition
    2.10 for e = 0 and -1, over the dichotomy that Fuentes' Theorem 2.7 proves
    and that the book's Theorem V.2.15 proves independently, with the section
    the exercise asks for supplied by the irreducible-element statements,
    Proposition 1.5 with Propositions 2.2 and 2.3; part (b) is
    Proposition 1.4 with Theorem 3.9(3) on the decomposable side and
    Proposition 2.11 on the indecomposable side, each stated as an equivalence
    and each resting on criteria whose proofs are printed. Two readings to
    note, recorded in the step that rests on it: Proposition 1.3(2)(d) prints
    "since deg(b) <= 0" where deg(e) <= 0 is meant. What this event at first
    recorded as a second defect, that Proposition 2.10's citation of [2,
    Corollary 1.8] and Proposition 2.2's citation of the same number name
    different statements, is withdrawn: both are [2, Corollary 2.9], printed
    p. 11, which states the section and the base-point-freeness, and the paper
    cites its irreducible-element criterion as [2, Theorem 2.5]. What this
    event also had wrong: Fuentes' Theorem 2.7 is not asserted without proof,
    his page 13 introducing it with "Thus, we have actually proved the
    following theorem", and the step now says so. The card's earlier own proof of the e = -1 case through
    stability of a normalized bundle of degree one is superseded by the
    published argument and is no longer on the card; the events of 2026-09-19,
    2026-11-11 and 2026-11-16 above stand as what those passes did. No part of
    V.2.12 is left without a published argument, so this card carries no
    COMPLAINTS record of 2026-11-16. Not checked: no source beyond the two
    named and the book was read in this pass, and no machine computation was
    run.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report on the transcription, and the one repair it required.
    Step s4 had Fuentes' Proposition 1.5 as making the generic element
    irreducible when deg b >= 1+e, which is that proposition's case e not
    equivalent to 0 alone; its case e equivalent to 0 requires deg b >= 2 or
    b equivalent to 0, so at e = 0 the earlier sentence named a bound one
    degree too small. Re-read in the paper's own folios, in
    tmp/sources/fuentes-2000-classification-elliptic-line-scrolls.pdf, whose
    page images carry the numbers: Lemma 1.2 opens on p. 2 with its item 1 and
    its item 2 on p. 3; Proposition 1.3 and its proof are on p. 3, Proposition
    1.4 on p. 3, and Proposition 1.5's statement closes p. 3 with its two cases
    and its proof on p. 4. The step now states the two cases as printed and
    checks the exercise's m >= e+2 against each: at e = 0 with e equivalent to
    0 the exercise's bound is exactly the 2 of case (1), and with e not
    equivalent to 0 it gives m >= 2 > 1 = 1+e; at e = -1 the divisor e has
    degree 1 and case (2) asks for m >= 1+e = 0; at e >= 1 the divisor e is not
    equivalent to 0 and m >= e+2 >= 1+e. The conclusion of part (a) is
    unchanged, and the correction of the citation changes no other step. The
    record of 2026-11-16 that reports this batch gave this proposition as p. 4
    and gave Lemma 1.2 as p. 3, Proposition 1.3 as pp. 3--4 and
    Fuentes--Pedreira's Corollary 2.13 as pp. 14--15; the paper's folios give
    pp. 2--3, p. 3, p. 3 and p. 14, and the correction is stated in a record of
    this date rather than in that one. Not checked in this pass: nothing else
    of Fuentes was re-read; the prose of the 2026-11-16 event above, which says
    this card carries no COMPLAINTS record of this date, is left as written.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A reader's report on the two texts of the event above. (i) Its page
    sentence is wrong: the folio numbered 3 ends at Fuentes' opening line "The
    unisecant linear systems with generic element irreducible are:", and both
    of Proposition 1.5's cases, with the proof, are on p. 4. What the folios
    give is Proposition 1.5 opening at the foot of p. 3 and printed pp. 3--4,
    which is how the step cites it and how the COMPLAINTS record of this date
    puts it; the event above says the statement "closes p. 3 with its two
    cases" and is corrected here. (ii) Its case-by-case check of the exercise's
    m >= e+2 was wrong in two ways, and the card's step s4 now checks it
    otherwise. Proposition 1.5 is a statement about decomposable surfaces, and
    a surface with e = -1 is indecomposable, so the case e = -1 is not
    Proposition 1.5(2)'s at all but Proposition 2.3's, printed p. 10, which asks
    for deg b >= 0; and the event above wrote the exercise's bound at e = -1 as
    "m >= 1 = 1+e", where 1+e is 0 at e = -1 and the bound the exercise assumes
    is m >= 1 by the exercise's own hypothesis m >= e+2. The indecomposable case
    e = 0 likewise belongs to Proposition 2.2, printed p. 9, not to Proposition
    1.5(1), and the check now runs so: a decomposable surface has e >= 0, where
    e equivalent to 0 forces e = 0 and the exercise's m >= 2 is exactly case
    (1)'s bound, and where e not equivalent to 0 leaves case (2)'s bound 1+e
    below e+2; an indecomposable surface with e = 0 has deg b >= 1 from m >= 2
    and with e = -1 has deg b >= 0 from m >= 1. Part (a)'s conclusion is
    unchanged, m >= 1 >= 0 and m >= 2 >= 1 in the two indecomposable cases, and
    no other step changed. Not checked in this pass: nothing else of Fuentes was
    re-read, and the page sentence of the first event was checked against the
    PDF's own folios only.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Out of the rendered solution's preamble and out of the remark went the
    tmp/sources paths that named this VM's copies of the sets cited there, on
    the reader's finding against the same paths on a sibling card of this
    batch. They are bookkeeping and belong here: Fuentes is read in
    tmp/sources/fuentes-2000-classification-elliptic-line-scrolls.md with its
    PDF beside it, Fuentes and Pedreira in
    tmp/sources/projective-theory-ruled-surfaces.md with its PDF, Egbert in
    tmp/sources/hartshorne-solutions-egbert.md, Yang Pi-Yeh in
    tmp/sources/lfwin-hartshorne-solutions.md, the National Taiwan University
    set in tmp/sources/ntu-ag2-chapter5.md beside its PDF, and the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md. No citation, page or
    statement changed.

---

::: {.problem}
Let $X$ be a ruled surface with invariant $e$ over an elliptic curve $C$, and let $\mfb$ be a divisor on $C$.

(a) If $\deg \mfb \geqslant e+2$, then there is a section $D \sim C_0+\mfb f$ such that $\linearsystem{D}$ has no base points.

(b) The linear system $\linearsystem{C_0+\mfb f}$ is very ample if and only if $\deg \mfb \geqslant e+3$.

Note.
The case $e=-1$ will require special attention.
:::

::: {.solution}
Every step below transcribes a published argument and names the source, numbered statement and printed page it transcribes: Luis Fuentes, *Classification of elliptic line scrolls*, arXiv:math/0009050v1, Lemma 1.2 and Propositions 1.3, 1.4, 2.3, 2.10 and 2.11, printed pp. 3--15; and, for the very-ampleness criterion on a decomposable surface, Luis Fuentes and Manuel Pedreira, *The Projective Theory of Ruled Surfaces*, arXiv:math/0006204v3, Theorem 3.9(3), printed p. 18, with Corollary 2.13, and Corollary 2.9, which prove it. Fuentes numbers the second paper [2], and his notation is the book's: $\mfe$ is the divisor with $\OO_C(\mfe)\cong\bigwedge^2\mathcal E$ and $\deg\mfe=-e$, $C_0$ is the section of minimum self-intersection, and he writes $X_0$ and $\mathfrak b$ for $C_0$ and $\mfb$.

Put
$$
m=\deg\mfb
\qquad\text{and}\qquad
L=\OO_X(C_0+\mfb f).
$$

::: pf

::: {.pf-step #s1}
On the elliptic curve $C$, a divisor is base-point-free if and only if it is linearly equivalent to $0$ or has degree at least $2$, and very ample if and only if its degree is at least $3$.

::: pf-proof
Fuentes, Lemma 1.2, states both, and proves neither. On a curve of genus one they are the standard criterion [[T-D8TUX]] at $g=1$: degree at least $2g=2$ is base-point-free and degree at least $2g+1=3$ is very ample, and the vanishing behind them is Riemann--Roch with $K_C\cong\OO_C$, which gives $h^1(C,\mfa)=0$ and $h^0(C,\mfa)=\deg\mfa$ for $\deg\mfa\ge1$, while $h^0(C,\mfa)\le1$ for $\deg\mfa\le0$.
:::

:::

::: {.pf-step #s2}
If $X$ is decomposable, then $e\ge0$, and if
$$
m\ge e+2
$$
the complete system $\linearsystem{L}$ has no base points.

::: pf-proof
Fuentes, Proposition 1.3, over a decomposable surface. Its criterion is that $\linearsystem{X_0+\mfb f}$ is base-point-free exactly when $\mfb$ and $\mfb+\mfe$ are, which is Proposition 3.4, of [2], cited there as [2, Proposition 2.3]. Splitting on $\mfe$ the paper proves two cases: if $\mfe\sim0$, then $\linearsystem{X_0+\mfb f}$ is base-point-free if and only if $\deg\mfb\ge2$ or $\mfb\sim0$; and if $\mfe\not\sim0$, if and only if $\deg\mfb\ge e+2$, or $\mfb\sim-\mfe$ with $e\ge2$. The reductions are Lemma 1.2 of the same paper, which is step [](#s1){.pf-ref}, together with $e=-\deg\mfe\ge0$.

His case (d) prints "since $\deg(\mathfrak b)\le0$" where $\deg(\mfe)\le0$ is meant: a decomposable normalized bundle is $\OO_C\oplus\OO_C(\mfe)$ with $\deg(\mfe)\le0$ by Theorem 3.2(1) of [2] with Remark 3.3, both printed p. 15, so that $e\ge0$ and $\deg(\mfb+\mfe)=m-e$, which is at least $2$ once $m\ge e+2$.

With $m\ge e+2$: if $\mfe\sim0$ then $e=0$ and $m\ge2$, which is the first case; otherwise $m\ge e+2$, which is the second. Hence $\mfb$ and $\mfb+\mfe$ are base-point-free, and so is $\linearsystem{L}$.
:::

:::

::: {.pf-step #s3}
If $X$ is indecomposable with $e\in\{0,-1\}$ and $m\ge e+2$, then $\linearsystem{L}$ has no base points.

::: pf-proof
Fuentes, Proposition 2.10, with its proof. There are two cases, $e=0$ and $e=-1$. If $m\ge2$ then $\mfb$ is nonspecial and $\mfb$, $\mfb+\mfe$ are base-point-free by Lemma 1.2, step [](#s1){.pf-ref}, and the base-point-free criterion of [2] gives that $\linearsystem{L}$ is base-point-free. The paper cites that criterion as [2, Corollary 1.8]; in the numbering of [2] read here it is Corollary 2.9, and it states both of the facts he uses: if $\mfb$ and $\mfb+\mfe$ are effective without common base points and $\mfb$ is nonspecial, there is a section $D\sim X_0+\mfb f$; and if both are base-point-free, so is $\linearsystem{X_0+\mfb f}$. His Proposition 1.5 cites the irreducible-element criterion of [2] as [2, Theorem 2.5].

For $m\le1$ he treats each case. At $e=0$ and $m\le0$ one has $h^0(\OO_S(X_0+\mfb f))\le h^0(\OO_X(\mfb))+h^0(\OO_X(\mfb+\mfe))$ and $h^0(\OO_S(X_0))=1$, so $h^0\le1$ and the system has base points; at $e=0$ and $m=1$ the divisor $\mfb+\mfe\sim\mfb$ has a base point. At $e=-1$ and $m\le0$ the system has at most one curve, by his Proposition 2.3, and so has base points; at $e=-1$ and $m=1$ he has $h^0(\OO_S(X_0+Pf))=h^0(\OO_X(P))+h^0(\OO_X(P+\mfe))=1+2=3$, and $h^0(\OO_S(X_0+(P-Q)f))=1$ for every $Q$, again by Proposition 2.3, so that $h^0(\OO_S(H-Qf))=h^0(\OO_S(H))-2$ for every $Q$ and Corollary 2.4 of [2], printed p. 9, makes $\linearsystem{L}$ base-point-free.

In part (a) the hypothesis is $m\ge e+2$, and $e\ge-1$. At $e=0$ it reads $m\ge2$, and at $e=-1$ it reads $m\ge1$, which are the two subcases above.
:::

:::

::: {.pf-step #s4}
Every ruled surface over the elliptic curve $C$ is decomposable with $e\ge0$, or indecomposable with $e=0$ or $e=-1$. Hence part (a) of the exercise holds: there is a section $D\sim C_0+\mfb f$.

::: pf-proof
Hartshorne, Theorem V.2.12, gives $e\ge0$ for a decomposable normalized bundle, and Theorem V.2.15, gives $e=0$ or $-1$ for a ruled surface over an elliptic curve corresponding to an indecomposable $\mathcal E$. Fuentes, Theorem 2.7, proves the same second half; it is the theorem his page 13 introduces with "Thus, we have actually proved the following theorem", from Theorem 2.1 with Propositions 2.5 and 2.6.

Part (a) asks for a section, and a complete system without base points gives only an effective member, which may be $C_0'$ together with fibres. The irreducible member comes from the same paper. For a decomposable surface, Proposition 1.5, makes the generic element of $\linearsystem{X_0+\mfb f}$ irreducible in two cases: when $\mfe\sim0$, with $\deg\mfb\ge2$ or $\mfb\sim0$; and when $\mfe\not\sim0$, with $\deg\mfb\ge1+e$, the alternatives $\mfb\sim0$ and $\mfb\sim-\mfe$ being the systems $\linearsystem{X_0}$ and $\linearsystem{X_0-\mfe f}$; for an indecomposable surface with $e=0$, Proposition 2.2, does when $\mfb\sim0$ or $\deg\mfb\ge1$; and with $e=-1$, Proposition 2.3, does when $\deg\mfb\ge0$. An irreducible member of the class $C_0+\mfb f$ meets each fibre once, so it is a section. Fuentes--Pedreira's Corollary 2.9, gives the same conclusion a second way, a section of that class existing as soon as $\mfb$ and $\mfb+\mfe$ are effective without common base points and $\mfb$ is nonspecial.

The hypotheses hold here, in each of the two kinds of surface. A decomposable surface has $e\ge0$: if $\mfe\sim0$ then $e=0$, the exercise assumes $m\ge e+2=2$, and that is exactly the bound of Proposition 1.5(1); if $\mfe\not\sim0$, Proposition 1.5(2) asks for $\deg\mfb\ge1+e$, and the exercise gives $m\ge e+2>1+e$. An indecomposable surface has $e=0$ or $e=-1$: with $e=0$ the exercise assumes $m\ge e+2=2$, and Proposition 2.2 asks for $\mfb\sim0$ or $\deg\mfb\ge1$; with $e=-1$ it assumes $m\ge1$, and Proposition 2.3 asks for $\deg\mfb\ge0$. So in each case there is a section $D\sim C_0+\mfb f$, and $\linearsystem{L}$ has no base points by step [](#s2){.pf-ref} or step [](#s3){.pf-ref}.
:::

:::

::: {.pf-step #s5}
If $X$ is decomposable, then $\linearsystem{L}$ is very ample if and only if
$$
m\ge e+3.
$$

::: pf-proof
Fuentes, Proposition 1.4, states the equivalence for a decomposable surface. Its proof is the sufficiency: by Theorem 2.8 of [2], printed as Theorem 3.9(3), p. 18, $\linearsystem{X_0+\mfb f}$ is very ample exactly when $\mfb$ and $\mfb+\mfe$ are; Lemma 1.2, step [](#s1){.pf-ref}, makes a divisor of degree at least $3$ on an elliptic curve very ample, so $m\ge3$ and $m-e\ge3$ suffice, and since $e\ge0$ that is $m\ge e+3$.

The other direction is the same equivalence read backwards, which the paper's statement carries and its proof does not spell out: very ampleness of $\linearsystem{L}$ forces $\mfb$ and $\mfb+\mfe$ very ample, so $m\ge3$ and $m-e\ge3$ by Lemma 1.2, that is $m\ge e+3$.

Theorem 3.9(3) of [2] is proved on printed p. 18 from Corollary 2.13, whose criterion is $h^0(H-(P+Q)f)=h^0(H)-4$ for all $P,Q$ in the base, and from $h^0(\OO_S(H))=h^0(\OO_X(\mfb))+h^0(\OO_X(\mfb+\mfe))$; both directions of Corollary 2.13 are proved there, the forward one through Theorem 2.11.
:::

:::

::: {.pf-step #s6}
If $X$ is indecomposable with $e\in\{0,-1\}$, then $\linearsystem{L}$ is very ample if and only if
$$
m\ge e+3.
$$

::: pf-proof
Fuentes, Proposition 2.11, with its proof. By the very-ampleness criterion of [2], printed as Corollary 2.13, p. 14, with Corollary 2.4, p. 9, $\linearsystem{L}$ is very ample exactly when $\linearsystem{C_0+\mfb f}$ and every $\linearsystem{C_0+(\mfb-P)f}$ are base-point-free; by Proposition 2.10, step [](#s3){.pf-ref}, that happens exactly when $m\ge e+2$ and $\deg(\mfb-P)=m-1\ge e+2$, that is $m\ge e+3$. The paper writes the conclusion in the "when" form; the equivalence gives both directions, the necessity coming from applying Proposition 2.10 to $\linearsystem{C_0+\mfb f}$ and to $\linearsystem{C_0+(\mfb-P)f}$.
:::

:::

::: {.pf-step #s7}
Therefore
$$
\linearsystem{C_0+\mfb f}\text{ is very ample}
\iff
m\ge e+3,
$$
which is part (b); and the case $e=-1$ of the Note is the case $e=-1$ of steps [](#s3){.pf-ref} and [](#s6){.pf-ref}.

::: pf-proof
By step [](#s4){.pf-ref}, $X$ is decomposable or indecomposable with $e\in\{0,-1\}$. Very ampleness for $m\ge e+3$ is step [](#s5){.pf-ref} in the first case and step [](#s6){.pf-ref} in the second, and the converse in each case is the same step, both cited as equivalences.

For $e=-1$ the two bounds read $m\ge1$ for base-point freeness and $m\ge2$ for very ampleness, and at $m=1$ step [](#s6){.pf-ref} and Proposition 2.11 deny very ampleness while step [](#s3){.pf-ref} grants base-point freeness; that is the special attention the exercise's Note asks for.
:::

:::

::: pf-qed
Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (a), steps [](#s5){.pf-ref} and [](#s6){.pf-ref} the two directions of part (b) case by case, and step [](#s7){.pf-ref} assembles part (b).
:::

:::

:::

::: {.remark title="Published solution"}
The four statements transcribed above are Fuentes' own classification of base-point-free and very ample unisecant systems on an elliptic ruled surface, and they cover the exercise completely, both parts and both the decomposable and the indecomposable case.

Luis Fuentes, *Classification of elliptic line scrolls* (arXiv:math/0009050v1, 6 September 2000), printed pp. 3--15: Lemma 1.2, is the degree criterion on an elliptic curve; Proposition 1.3, is base-point freeness on a decomposable surface, with the exceptions $\mfb\sim0$ at $\mfe\sim0$ and $\mfb\sim-\mfe$ at $e\ge2$; Proposition 1.4, is very ampleness on a decomposable surface; Proposition 2.10, is base-point freeness on an indecomposable one; Proposition 2.11, is very ampleness on an indecomposable one. The exercise's hypotheses $m\ge e+2$ and $m\ge e+3$ fall in the main alternatives of Propositions 1.3 and 2.10, since $e\ge0$ there and $m\ge e+2$ excludes $\mfb\sim0$ at $e=0$ and $\mfb\sim-\mfe$ at $e\ge2$. Theorem 2.7, which reduces the indecomposable case to $e=0$ and $e=-1$, is proved there from Theorem 2.1 with Propositions 2.5 and 2.6, as its page 13 says in introducing it; the book's Theorem V.2.15, proves the same reduction independently. Steps [](#s4){.pf-ref} cites both, and Proposition 1.5 with Propositions 2.2 and 2.3 supply the irreducible member that makes the member of the system a section.

Luis Fuentes and Manuel Pedreira, *The Projective Theory of Ruled Surfaces* (arXiv:math/0006204v3), is the paper Fuentes cites as [2] throughout, in an earlier numbering: its Theorem 3.9(3), printed p. 18, is the very-ampleness criterion $\linearsystem{X_0+\mfb f}$ very ample if and only if $\mfb$ and $\mfb+\mfe$ are, which Fuentes cites as [2, Theorem 2.8]; its Corollary 2.13, is the criterion $h^0(H-(P+Q)f)=h^0(H)-4$, cited as [2, Theorem 1.10]; its Corollary 2.4, is the base-point-free criterion $h^0(H-Pf)=h^0(H)-2$, cited as [2, Corollary 1.4]; its Corollary 2.9, is the base-point-free criterion for a section $\linearsystem{X_0+\mfb f}$, cited as [2, Corollary 1.8]; its Theorem 3.2(1), printed p. 15, is $e\ge0$ with every $e\ge0$ occurring; its Theorem 3.6, is the irreducible-element criterion, cited as [2, Theorem 2.5]; and its Proposition 3.4, is the base-point criterion on a decomposable surface, cited as [2, Proposition 2.3]. Each number Fuentes cites, including [2, Corollary 1.8] in Propositions 2.2 and 2.10, points at one of these. Every one of those is proved in that paper, and Corollary 2.13's two directions are Theorem 2.11, and the two base-point criteria.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.12, gives one line per part, "This is Fuentes, Pedreira Prop 1.3" and "Fuentes, Predeira prop 1.4", and no argument. Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.12, printed pp. 104--105, disposes of $e\ge0$ as "trivial by corollary 3.2 in chapter IV and 5.2.11" and its $e=-1$ computation is garbled; its two absolute values are wrong: $h^0(\OO_X(C_0+\mfb f))$ is 3 and not 2 at $e=-1$ with $\deg\mfb=1$, and the values $4$ and $0$ it gives are $5$ and $1$. Algebraic Geometry II, National Taiwan University, 2020 Spring, has no entry for Exercise 12 of §2.
:::
