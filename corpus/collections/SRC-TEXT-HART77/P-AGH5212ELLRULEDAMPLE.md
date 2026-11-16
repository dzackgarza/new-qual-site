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
    and Propositions 1.3, 1.4, 2.3, 2.10 and 2.11, printed pp. 3 to 15; and
    Fuentes and Pedreira, The Projective Theory of Ruled Surfaces
    (arXiv:math/0006204v3), tmp/sources/projective-theory-ruled-surfaces.md,
    Theorem 3.9(3) printed p. 18, Corollary 2.13 printed pp. 14 to 15 and
    Corollary 2.9 printed p. 11. Checked against the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N is
    PDF p. N+15: V.2.12 as printed on p. 385 with its Note on e = -1, Theorem
    V.2.12 on p. 376 and Theorem V.2.15 on p. 377. What the transcription
    establishes: part (a) is Proposition 1.3 for e at least 0 and Proposition
    2.10 for e = 0 and -1, over the dichotomy that the book's Theorem V.2.15
    supplies and that Fuentes' Theorem 2.7 asserts without proof; part (b) is
    Proposition 1.4 with Theorem 3.9(3) on the decomposable side and
    Proposition 2.11 on the indecomposable side, each stated as an equivalence
    and each resting on criteria whose proofs are printed. Two readings to
    note, both recorded in the steps: Proposition 1.3(2)(d) prints "since
    deg(b) <= 0" where deg(e) <= 0 is meant, and Proposition 2.10 cites [2,
    Corollary 1.8] for base-point freeness where the statement with that
    function is [2, Corollary 2.9], printed p. 11, the same number being cited
    in Proposition 2.2 for irreducible elements, which is [2, Theorem 3.6],
    printed p. 17. The card's earlier own proof of the e = -1 case through
    stability of a normalized bundle of degree one is superseded by the
    published argument and is no longer on the card; the events of 2026-09-19,
    2026-11-11 and 2026-11-16 above stand as what those passes did. No part of
    V.2.12 is left without a published argument, so this card carries no
    COMPLAINTS record of 2026-11-16. Not checked: no source beyond the two
    named and the book was read in this pass, and no machine computation was
    run.

---

::: {.problem}
Let $X$ be a ruled surface with invariant $e$ over an elliptic curve $C$, and let $\mfb$ be a divisor on $C$.

(a) If $\deg \mfb \geqslant e+2$, then there is a section $D \sim C_0+\mfb f$ such that $\linearsystem{D}$ has no base points.

(b) The linear system $\linearsystem{C_0+\mfb f}$ is very ample if and only if $\deg \mfb \geqslant e+3$.

Note.
The case $e=-1$ will require special attention.
:::

::: {.solution}
Every step below transcribes a published argument and names the source, numbered statement and printed page it transcribes: Luis Fuentes, *Classification of elliptic line scrolls*, arXiv:math/0009050v1, text version `tmp/sources/fuentes-2000-classification-elliptic-line-scrolls.md`, Lemma 1.2 and Propositions 1.3, 1.4, 2.3, 2.10 and 2.11, printed pp. 3--15; and, for the very-ampleness criterion on a decomposable surface, Luis Fuentes and Manuel Pedreira, *The Projective Theory of Ruled Surfaces*, arXiv:math/0006204v3, text version `tmp/sources/projective-theory-ruled-surfaces.md`, Theorem 3.9(3), printed p. 18, with Corollary 2.13, printed pp. 14--15, and Corollary 2.9, printed p. 11, which prove it. Fuentes numbers the second paper [2], and his notation is the book's: $\mfe$ is the divisor with $\OO_C(\mfe)\cong\bigwedge^2\mathcal E$ and $\deg\mfe=-e$, $C_0$ is the section of minimum self-intersection, and he writes $X_0$ and $\mathfrak b$ for $C_0$ and $\mfb$.

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
Fuentes, Lemma 1.2, printed p. 3, states both, and proves neither. On a curve of genus one they are the standard criterion [[T-D8TUX]] at $g=1$: degree at least $2g=2$ is base-point-free and degree at least $2g+1=3$ is very ample, and the vanishing behind them is Riemann--Roch with $K_C\cong\OO_C$, which gives $h^1(C,\mfa)=0$ and $h^0(C,\mfa)=\deg\mfa$ for $\deg\mfa\ge1$, while $h^0(C,\mfa)\le1$ for $\deg\mfa\le0$.
:::

:::

::: {.pf-step #s2}
If $X$ is decomposable, then $e\ge0$, and if
$$
m\ge e+2
$$
the complete system $\linearsystem{L}$ has no base points.

::: pf-proof
Fuentes, Proposition 1.3, printed pp. 3--4, over a decomposable surface. Its criterion is that $\linearsystem{X_0+\mfb f}$ is base-point-free exactly when $\mfb$ and $\mfb+\mfe$ are, which is Proposition 3.4, printed pp. 16--17, of [2], cited there as [2, Proposition 2.3]. Splitting on $\mfe$ the paper proves two cases: if $\mfe\sim0$, then $\linearsystem{X_0+\mfb f}$ is base-point-free if and only if $\deg\mfb\ge2$ or $\mfb\sim0$; and if $\mfe\not\sim0$, if and only if $\deg\mfb\ge e+2$, or $\mfb\sim-\mfe$ with $e\ge2$. The reductions are Lemma 1.2 of the same paper, which is step [](#s1){.pf-ref}, together with $e=-\deg\mfe\ge0$.

His case (d) prints "since $\deg(\mathfrak b)\le0$" where $\deg(\mfe)\le0$ is meant: a decomposable normalized bundle is $\OO_C\oplus\OO_C(-\mfe)$ with $\deg(-\mfe)\le0$ by Theorem 3.2(1) of [2], printed p. 15, so that $e\ge0$ and $\deg(\mfb+\mfe)=m-e$, which is at least $2$ once $m\ge e+2$.

With $m\ge e+2$: if $\mfe\sim0$ then $e=0$ and $m\ge2$, which is the first case; otherwise $m\ge e+2$, which is the second. Hence $\mfb$ and $\mfb+\mfe$ are base-point-free, and so is $\linearsystem{L}$.
:::

:::

::: {.pf-step #s3}
If $X$ is indecomposable with $e\in\{0,-1\}$ and $m\ge e+2$, then $\linearsystem{L}$ has no base points.

::: pf-proof
Fuentes, Proposition 2.10, printed pp. 14--15, with its proof. There are two cases, $e=0$ and $e=-1$. If $m\ge2$ then $\mfb$ is nonspecial and $\mfb$, $\mfb+\mfe$ are base-point-free by Lemma 1.2, step [](#s1){.pf-ref}, and the base-point-free criterion of [2] gives that $\linearsystem{L}$ is base-point-free. The paper cites that criterion as [2, Corollary 1.8], printed as Corollary 2.9, p. 11, of the version on disk; the same number is cited in his Proposition 2.2 for irreducible elements, which is [2, Theorem 3.6], printed p. 17, so the two citations are not the same statement.

For $m\le1$ he treats each case. At $e=0$ and $m\le0$ one has $h^0(\OO_S(X_0+\mfb f))\le h^0(\OO_X(\mfb))+h^0(\OO_X(\mfb+\mfe))$ and $h^0(\OO_S(X_0))=1$, so $h^0\le1$ and the system has base points; at $e=0$ and $m=1$ the divisor $\mfb+\mfe\sim\mfb$ has a base point. At $e=-1$ and $m\le0$ the system has at most one curve, by his Proposition 2.3, printed pp. 9--10, and so has base points; at $e=-1$ and $m=1$ he has $h^0(\OO_S(X_0+Pf))=h^0(\OO_X(P))+h^0(\OO_X(P+\mfe))=1+2=3$, and $h^0(\OO_S(X_0+(P-Q)f))=1$ for every $Q$, again by Proposition 2.3, printed pp. 9--10, so that $h^0(\OO_S(H-Qf))=h^0(\OO_S(H))-2$ for every $Q$ and Corollary 2.4 of [2], printed p. 9, makes $\linearsystem{L}$ base-point-free.

In part (a) the hypothesis is $m\ge e+2$, and $e\ge-1$. At $e=0$ it reads $m\ge2$, and at $e=-1$ it reads $m\ge1$, which are the two subcases above.
:::

:::

::: {.pf-step #s4}
Every ruled surface over the elliptic curve $C$ is decomposable with $e\ge0$, or indecomposable with $e=0$ or $e=-1$. Hence part (a) of the exercise holds.

::: pf-proof
Hartshorne, Theorem V.2.12, printed p. 376, gives $e\ge0$ for a decomposable normalized bundle, and Theorem V.2.15, printed p. 377, states that a ruled surface over an elliptic curve corresponding to an indecomposable $\mathcal E$ has $e=0$ or $-1$. Fuentes, Theorem 2.7, printed p. 13, asserts the same second half in the form "There only exist two models of indecomposable elliptic ruled surfaces. They have invariants $e=0$ and $e=-1$", and gives no proof there.

So $X$ falls under step [](#s2){.pf-ref} or under step [](#s3){.pf-ref}, and $m\ge e+2$ gives a system without base points in either case. A system with no base points is nonempty, so it contains a divisor $D\sim C_0+\mfb f$, which is the section part (a) asks for.
:::

:::

::: {.pf-step #s5}
If $X$ is decomposable, then $\linearsystem{L}$ is very ample if and only if
$$
m\ge e+3.
$$

::: pf-proof
Fuentes, Proposition 1.4, printed p. 3, states the equivalence for a decomposable surface. Its proof is the sufficiency: by Theorem 2.8 of [2], printed as Theorem 3.9(3), p. 18, $\linearsystem{X_0+\mfb f}$ is very ample exactly when $\mfb$ and $\mfb+\mfe$ are; Lemma 1.2, step [](#s1){.pf-ref}, makes a divisor of degree at least $3$ on an elliptic curve very ample, so $m\ge3$ and $m-e\ge3$ suffice, and since $e\ge0$ that is $m\ge e+3$.

The other direction is the same equivalence read backwards, which the paper's statement carries and its proof does not spell out: very ampleness of $\linearsystem{L}$ forces $\mfb$ and $\mfb+\mfe$ very ample, so $m\ge3$ and $m-e\ge3$ by Lemma 1.2, that is $m\ge e+3$.

Theorem 3.9(3) of [2] is proved on printed p. 18 from Corollary 2.13, printed pp. 14--15, whose criterion is $h^0(H-(P+Q)f)=h^0(H)-4$ for all $P,Q$ in the base, and from $h^0(\OO_S(H))=h^0(\OO_X(\mfb))+h^0(\OO_X(\mfb+\mfe))$; both directions of Corollary 2.13 are proved there, the forward one through Theorem 2.11, printed pp. 12--13.
:::

:::

::: {.pf-step #s6}
If $X$ is indecomposable with $e\in\{0,-1\}$, then $\linearsystem{L}$ is very ample if and only if
$$
m\ge e+3.
$$

::: pf-proof
Fuentes, Proposition 2.11, printed p. 15, with its proof. By the very-ampleness criterion of [2], printed as Corollary 2.13, pp. 14--15, with Corollary 2.4, p. 9, $\linearsystem{L}$ is very ample exactly when $\linearsystem{L}$ and every $\linearsystem{L-Pf}$ are base-point-free; by Proposition 2.10, step [](#s3){.pf-ref}, that happens exactly when $m\ge e+2$ and $\deg(\mfb-P)=m-1\ge e+2$, that is $m\ge e+3$. The paper writes the conclusion in the "when" form; the equivalence gives both directions, the necessity coming from applying Proposition 2.10 to $\linearsystem{L}$ and to $\linearsystem{L-Pf}$.
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

Luis Fuentes, *Classification of elliptic line scrolls* (arXiv:math/0009050v1, 6 September 2000), text version `tmp/sources/fuentes-2000-classification-elliptic-line-scrolls.md`, printed pp. 3--15: Lemma 1.2, printed p. 3, is the degree criterion on an elliptic curve; Proposition 1.3, printed pp. 3--4, is base-point freeness on a decomposable surface, with the exceptions $\mfb\sim0$ at $\mfe\sim0$ and $\mfb\sim-\mfe$ at $e\ge2$; Proposition 1.4, printed p. 3, is very ampleness on a decomposable surface; Proposition 2.10, printed pp. 14--15, is base-point freeness on an indecomposable one; Proposition 2.11, printed p. 15, is very ampleness on an indecomposable one. The exercise's hypotheses $m\ge e+2$ and $m\ge e+3$ fall in the main alternatives of Propositions 1.3 and 2.10, since $e\ge0$ there and $m\ge e+2$ excludes $\mfb\sim0$ at $e=0$ and $\mfb\sim-\mfe$ at $e\ge2$. Theorem 2.7, printed p. 13, which reduces the indecomposable case to $e=0$ and $e=-1$, is asserted there without proof; the book's Theorem V.2.15, printed p. 377, is the proof, and step [](#s4){.pf-ref} cites it.

Luis Fuentes and Manuel Pedreira, *The Projective Theory of Ruled Surfaces* (arXiv:math/0006204v3), text version `tmp/sources/projective-theory-ruled-surfaces.md`, is the paper Fuentes cites as [2] throughout, in an earlier numbering: its Theorem 3.9(3), printed p. 18, is the very-ampleness criterion $\linearsystem{X_0+\mfb f}$ very ample if and only if $\mfb$ and $\mfb+\mfe$ are, which Fuentes cites as [2, Theorem 2.8]; its Corollary 2.13, printed pp. 14--15, is the criterion $h^0(H-(P+Q)f)=h^0(H)-4$, cited as [2, Theorem 1.10]; its Corollary 2.4, printed p. 9, is the base-point-free criterion $h^0(H-Pf)=h^0(H)-2$, cited as [2, Corollary 1.4]; its Corollary 2.9, printed p. 11, is the base-point-free criterion for a section $\linearsystem{X_0+\mfb f}$, cited as [2, Corollary 1.8]; its Theorem 3.2(1), printed p. 15, is $e\ge0$ with every $e\ge0$ occurring; its Theorem 3.6, printed p. 17, is the irreducible-element criterion, also cited as [2, Corollary 1.8] by Fuentes' Proposition 2.2; and its Proposition 3.4, printed pp. 16--17, is the base-point criterion on a decomposable surface, cited as [2, Proposition 2.3]. Every one of those is proved in that paper, and Corollary 2.13's two directions are Theorem 2.11, printed pp. 12--13, and the two base-point criteria.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.2.12, PDF pp. 268--269, gives one line per part, "This is Fuentes, Pedreira Prop 1.3" and "Fuentes, Predeira prop 1.4", and no argument. Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, exercise 5.2.12, printed pp. 104--105, disposes of $e\ge0$ as "trivial by corollary 3.2 in chapter IV and 5.2.11" and its $e=-1$ computation is garbled; its two absolute values are wrong by the analysis this card's audit records on 2026-11-15 in the V.2.13 entry. Algebraic Geometry II, National Taiwan University, 2020 Spring, text version `tmp/sources/ntu-ag2-chapter5.md`, has no entry for Exercise 12 of §2.
:::
