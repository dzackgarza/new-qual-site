---
schema: qual/card@1
id: P-AGH5213ELLSCROLL
kind: problem
title: Existence of elliptic scrolls of given degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.2.13, the retained Egbert companion calculation, and
    the preceding invariant and elliptic ruled-surface very-ampleness cards.
    The companion has the intended route: choose a ruled surface of invariant
    e and embed by C_0+n f. Its final dimension line conflates h^0 with the
    projective-space dimension; the proof below keeps h^0=2n-e=d and hence
    embeds by the complete system in P^{d-1}. The e=-1 case is supplied by
    V.2.5(c), e=0 by V.2.5(a), and e>0 by the explicit normalized split bundle
    O_C direct-sum L with deg L=-e.
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
    exercise 2.13, printed page 385. Rechecked the dimension count that Egbert
    gets wrong: on an elliptic curve Riemann-Roch gives h^0(O_C(k)) = k for
    k > 0, so h^0(X, O(C_0+bf)) = h^0(b) + h^0(b+e) = n + (n-e) = 2n-e = d,
    and the scroll lies in P^{d-1}, not in P^{d+1} as the rational scroll of
    Corollary 2.19 does. Checked the applications: V.2.12(b) for very ampleness
    at n >= e+3, V.2.5(a) and (c) for the existence of the surface at e = 0 and
    e = -1, and the split normalized bundle O_C + O_C(-e) for e > 0, whose
    negative twists have no sections. Searched outside the twelve retained sets:
    Yang Pi-Yeh, Hartshorne Solutions, exercise 5.2.13, printed p. 105
    (tmp/sources/lfwin-hartshorne-solutions.pdf), gives the argument from
    V.2.12(b) and the same 2n-e count; Algebraic Geometry II, National Taiwan
    University, 2020 Spring, has no entry for Exercise 13 of section 2. Not
    checked: whether an elliptic scroll so defined is required to be minimal or
    normalised; the exercise does not ask and the card does not claim.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The input this card's very-ampleness step imports, Yang's 5.2.12, recorded
    with its two wrong values, on a reader's report of issue #121. Read in
    tmp/sources/lfwin-hartshorne-solutions.md (block "PDF pages 101-119") at
    Solution 5.2.12 and against the folios of the PDF: on printed p. 104 he
    writes h^0(L_X(C_0+Bf)) = h^0(L_C(fraktur-e+B)) = 2 at e = -1, and on p. 105
    h^0(C_0+(A+B)f) = h^0(C_0+Bf) + 2 = 4 and h^0(C_0+(A+B-P-Q)f) = 0. The true
    values are 3, 5 and 1. With e = -1 the surface is P(E) for the unique
    nontrivial extension 0 -> O_C -> E -> L(P) -> 0 of (2.11.6), so
    deg E = deg fraktur-e = -e = 1 by Notation 2.8.1; pi_*O(C_0+bf) = E tensor O(b) is
    indecomposable of degree 1 + 2 deg b, and Riemann-Roch with h^1 = 0 above
    degree 2g-1 gives h^0 = 2 deg b + 1, i.e. 3, 5, 1 at deg b = 1, 2, 0. His own
    5.2.13 count 2n-e gives the same 3 at n = 1, so his two entries disagree.
    Both tests he then applies are drops, h^0(D-Pf) = h^0(D)-2 and
    h^0(D-Pf-Qf) = h^0(D)-4, and they hold with the true values too, so his
    conclusions survive while the absolute values do not. The cause is his p. 104
    display, which keeps only the h^0(b+fraktur-e) summand of the decomposable
    splitting of 5.2.11 and then subtracts an unrelated h^1; the two-term split
    value coincides with the truth for deg b >= 1 and for every nontrivial b of
    degree 0, the terms being h^0(b) = 0 and h^0(b+fraktur-e) = 1 there, and it
    differs only at b ~ 0, where it gives 2 against the true 1 -- the one class
    at which the split formula and the indecomposable bundle part company, so the
    splitting's validity at e = -1 is not what the numbers turn on. The card's own
    steps use none of his numbers and are unchanged.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes and Pedreira (arXiv:math/0006204v3) on 2026-11-16, in
    tmp/sources/projective-theory-ruled-surfaces.md. Its introduction cites the
    classification of elliptic scrolls of Corrado Segre, its reference [17], and
    says that that classification does not follow directly from the
    very-ampleness criterion; [17] is Segre, Ricerche sulle rigate ellittiche di
    qualunque ordine, Atti Acc. Torino 21 (1885), 868--891, which is not in
    tmp/sources and was not read. The paper's own reference [4], the authors'
    "The classification of elliptic scrolls", preprint math.AG/0009050, appears
    only in its bibliography and is never cited in its text, so nothing here rests
    on it. What the paper does settle is the case e >= 0: its Theorem 3.2(1),
    printed p. 15, has a decomposable normalized bundle of invariant e >= 0 and
    every e >= 0 occurring; its Theorem 3.9(3), printed p. 18, makes the system of
    C_0 + bf very ample exactly when b and b+e are; and its Theorem 3.10(1),
    printed p. 19, gives N = h^0(b) + h^0(b+e) - 1 and degree 2 deg b - e. Those
    three are a published argument for every e >= 0 with n >= e+3. The case e = -1
    is outside the paper, whose Section 3 treats decomposable surfaces only, and
    the Atiyah surface there is indecomposable; step s1 constructs it and steps s3
    to s7 carry it through, and Yang Pi-Yeh's count, recorded above, agrees.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the remark's use of Fuentes--Pedreira's Theorem 3.10(1) on
    2026-11-16. That theorem gives N = h^0(O_X(b)) + h^0(O_X(b+e)) - 1, where N
    is the dimension of the projective space in which the scroll lies, together
    with deg S = 2 deg b - e; the remark read the first formula as the number of
    sections, which is the confusion it records against Egbert elsewhere, and it
    now says that on an elliptic base the section counts are n and n-e, so that
    h^0 = d = 2n-e and N = d-1, the scroll lying in P^{d-1}, which is what step
    s6 computes directly and what the event above states correctly. Also
    recorded here, since dated events are not rewritten: the event of 2026-11-11
    cites Yang Pi-Yeh by PDF, whose text version is
    tmp/sources/lfwin-hartshorne-solutions.md, and the National Taiwan University
    set, whose text version is tmp/sources/ntu-ag2-chapter5.md beside its PDF;
    the remark's citation of Yang names his.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Transcription pass for issue #121 on 2026-11-16: the solution is now the
    published argument, and every step names its source, numbered statement and
    printed page. What changed from the events above is the base of the
    argument: the earlier events recorded Fuentes and Pedreira's The Projective
    Theory of Ruled Surfaces as covering every e at least 0 on a decomposable
    surface and leaving e = -1 outside, the Atiyah surface being
    indecomposable. The authors' other paper, Classification of elliptic line
    scrolls (arXiv:math/0009050v1), text version
    tmp/sources/fuentes-2000-classification-elliptic-line-scrolls.md with its
    PDF beside it, is a classification of exactly these scrolls and does treat
    the indecomposable case: its Theorem 2.13(2)(b), printed pp. 16 to 17, is
    e = -1 with b at least 2, a smooth elliptic scroll of degree 2b+1 in
    P^{2b}, and its Theorem 2.13(2)(c), printed pp. 16 to 17, is e = 0 with b
    at least 3, of degree 2b in P^{2b-1}, while Theorem 1.7(2)(d), printed
    p. 6, is the decomposable case b at least 3+e of degree 2b-e in
    P^{2b-e-1}. Read against their PDFs page by page, the extractions marking
    only 20-page ranges: Theorems 1.7 (statement printed p. 5, item (2)(d) on
    p. 6), 2.7 (p. 13), 2.13 (statement p. 16, items and proof pp. 16 to 18)
    and Remark 2.9 (p. 14); and of the second paper Theorem 3.2(1), p. 15,
    Theorem 3.9(3), p. 18, Theorem 3.10(1), p. 19, Proposition 1.3, p. 4,
    Definition 1.5, p. 5, and Remark 3.3, p. 15. Checked against the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N is
    PDF p. N+15: V.2.13 as printed on p. 385, and the book's Theorem V.2.15 on
    p. 377, which proves independently what Fuentes' Theorem 2.7 proves: that
    the indecomposable invariants are 0 and -1, with one surface for each. What
    this event at first had wrong, that Theorem 2.7 is asserted without proof,
    is withdrawn in place, the paper's p. 13 introducing it with "Thus, we have
    actually proved the following theorem". It had wrong too the page of the
    minimum-self-intersection paragraph of [2], which is p. 5 and not p. 4. What the transcription
    establishes: the whole exercise, both the general statement and the
    degree-five example, for e at least 0 through Theorem 1.7(2)(d) and for
    the two indecomposable invariants through Theorem 2.13(2)(b) and (c), with
    the dimension taken from Theorem 3.10(1) of the second paper and from
    Theorem 2.13's own proof, where the paper's N is the dimension of the
    projective space and not the number of sections. The card's own steps for
    e = -1 and its own construction of the surfaces are superseded by the
    published argument and are no longer on the card; the events above stand
    as what those passes did, including the 2026-11-11 count and the
    2026-11-15 corrections to Yang's 5.2.12. No part of V.2.13 is left without
    a published argument, so this card carries no COMPLAINTS record of
    2026-11-16. Not checked: no source beyond the two papers and the book was
    read in this pass, and no machine computation was run.
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
    tmp/sources/projective-theory-ruled-surfaces.md with its PDF, Yang Pi-Yeh
    in tmp/sources/lfwin-hartshorne-solutions.md, Egbert in
    tmp/sources/hartshorne-solutions-egbert.md, the National Taiwan University
    set in tmp/sources/ntu-ag2-chapter5.md beside its PDF, and the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md. No citation, page or
    statement changed, and what this card's preamble asserts of its steps, that
    each transcribes a published argument, holds of the six steps it has.

- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read for issue #168, all six steps, against Hartshorne's Exercise V.2.13
    and its Theorem V.2.15, Fuentes' Lemma 1.2, Theorems 1.7, 2.1, 2.7 and 2.13
    and Remark 2.9, and Fuentes--Pedreira's Proposition 1.3, Theorem 3.2(1),
    Theorem 3.9(3), Theorem 3.10(1) and Corollaries 2.4, 2.9 and 2.13. Read and
    checked: s2's D.f = 1 and D^2 = 2n-e from C_0.f = 1, f^2 = 0 and C_0^2 = -e,
    the last from Fuentes--Pedreira's paragraph after their projection formula;
    s5's count h^0(O_X(D)) = h^0(O_C(b)) + h^0(O_C(b+mathfrak e)) = n + (n-e) =
    2n-e = d on the two positive-degree summands, so the scroll lies in
    P^{d-1}; s6's e = -1, n = 2 giving degree 5 in P^4; s1's existence for
    e >= 0 from Theorem 3.2(1) and for e = -1 from Theorem 2.7 with Remark
    2.9's item 5; s3's very ampleness imported from part (b) of
    P-AGH5212ELLRULEDAMPLE; and s4's three model descriptions, Theorem 1.7(2)(d)
    for a decomposable surface and Theorem 2.13(2)(b) and (2)(c) for the
    indecomposable ones, at e = -1 and e = 0. Each cited statement was found at
    its number and says what the step says.
    Two repairs, both of citation scope, no step's claim changing. In s5,
    Fuentes--Pedreira's Theorem 3.10(1) is stated for a decomposable ruled
    surface and was cited for a count asserted of every ruled surface; the step
    now says which case that theorem covers and takes the indecomposable case
    from Fuentes' Theorem 2.13, whose proof computes N as the same sum. In the
    remark, Egbert's count is reported as what he does: he takes the second
    summand to contribute n-1 and writes the count as 2n-1 and the space as
    P^{d-2}; 2n-1 equals d-1 only at e = 0, and the count is 2n-e = d.
    Not checked: Fuentes' Lemma 2.12, which the steps do not use; the printed
    text of his Remark 2.9 item 4, whose condition on the divisor reads
    inconsistently in the extraction and which this card does not cite; and no
    solution set other than the two the remark names.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Repairs on the reader's second report of this date, none changing a step's
    claim. The remark's count of Yang Pi-Yeh's wrong values said two and listed
    three; it now lists all four, the two return computations with 2 and 4 and
    both zeros, with the reason each is wrong: at e = -1 and deg b = 1 the count
    on the surface is 3 and not the 2 he takes from the curve, at deg b = 2 it
    is 5 and not 4, and the two zeros cannot hold, one summand of each count
    having positive degree on the elliptic curve. The solution's preamble no
    longer promises a printed page with each citation, the citations now being
    by numbered statement.
---

::: {.problem}
For every $e \geqslant-1$ and $n \geqslant e+3$, there is an elliptic scroll of degree $d=2 n-e$ in $\PP^{d-1}$.
In particular, there is an elliptic scroll of degree 5 in $\PP^4$.
:::

::: {.solution}
Every step below transcribes a published argument and names the source and numbered statement: Luis Fuentes, *Classification of elliptic line scrolls*, arXiv:math/0009050v1, Theorems 1.7, 2.7 and 2.13 and Remark 2.9; and Luis Fuentes and Manuel Pedreira, *The Projective Theory of Ruled Surfaces*, arXiv:math/0006204v3, Theorem 3.2(1), Theorem 3.9(3), and Theorem 3.10(1), which Fuentes cites as his paper [2]. Notation is the book's: $\mathcal E$ normalized, $\mfe$ the divisor with $\OO_C(\mfe)\cong\bigwedge^2\mathcal E$ and $\deg\mfe=-e$, $C_0$ the section of minimum self-intersection, $f$ a ruling fibre. A scroll is the image of a ruled surface by a unisecant complete linear system, and its genus is that of the base curve, in the sense of Definition 1.5 and the paragraph after it, of [2]; over an elliptic curve the image is an elliptic scroll.

::: pf

::: {.pf-step #s1}
For every integer $e\ge-1$ there is a ruled surface over $C$ with invariant $e$.

::: pf-proof
For $e\ge0$: Theorem 3.2(1) of [2], states that a decomposable normalized $\mathcal E_0$ is $\OO_C\oplus\mathcal L$ with $\deg\mathcal L\le0$, that then $e\ge0$, and that every $e\ge0$ occurs; with $\mathfrak e$ of degree $-e$ the surface $\PP(\OO_C\oplus\OO_C(\mfe))$ has invariant $e$, which is the construction of Remark 3.3, of [2].

For $e=-1$: Fuentes, Theorem 2.7, proves that there are only two models of indecomposable elliptic ruled surfaces and that their invariants are $0$ and $-1$, from Theorem 2.1 with Propositions 2.5 and 2.6; Hartshorne's Theorem V.2.15, proves the same with uniqueness for each of the two values. Remark 2.9, records the other route: Nagata's theorem that every geometrically ruled surface is obtained from $C\times\PP^1$ by finitely many elementary transformations, and its item 5 gives the $e=-1$ model by three of them at generic points.
:::

:::

::: {.pf-step #s2}
Let $\mfb$ be a divisor of degree $n$ on $C$ and put
$$
D=C_0+\mfb f.
$$
Then
$$
D\cdot f=1,
\qquad
D^2=2n-e.
$$

::: pf-proof
Proposition 1.3 of [2], sets $\operatorname{Num}(S)=\ZZ\oplus\ZZ$ generated by $C_0$ and $f$ with $C_0\cdot f=1$ and $f^2=0$, and the paragraph printed p. 5, after the projection formula, gives $C_0^2=-e=-\deg(\mfe)$, $C_0$ being the minimum self-intersection curve. Hence
$$
D\cdot f=C_0\cdot f+n\,f^2=1,
$$
and
$$
D^2=C_0^2+2n\,C_0\cdot f+n^2f^2=-e+2n,
$$
which is $D^2=2\deg\mfb-e$, the degree formula of Theorem 3.10(1) of [2].
:::

:::

::: {.pf-step #s3}
If $n\ge e+3$, then $\linearsystem{D}$ is very ample.

::: pf-proof
This is part (b) of [[P-AGH5212ELLRULEDAMPLE]], whose published argument is Fuentes, Proposition 1.4, for a decomposable surface and Fuentes, Proposition 2.11, for an indecomposable one: $\linearsystem{C_0+\mfb f}$ is very ample if and only if $\deg\mfb\ge e+3$. On the decomposable side the criterion behind it is Theorem 3.9(3) of [2], with Corollary 2.13.
:::

:::

::: {.pf-step #s4}
The image of $X$ under $\linearsystem{D}$ is a smooth elliptic scroll of degree
$$
d=2n-e
$$
in $\PP^{d-1}$.

::: pf-proof
The three published model descriptions give it, and they agree on the degree and on the dimension.

Decomposable $X$, $n\ge3+e$: Fuentes, Theorem 1.7(2)(d), "If $b\ge3+e$, then $R$ is a smooth elliptic scroll of degree $2b-e$ in $\mathbf P^{2b-e-1}$", with $b=\deg\mfb=n$.

Indecomposable $X$ with $e=-1$, $n\ge2$: Fuentes, Theorem 2.13(2)(b), "then $R$ is a smooth elliptic scroll of degree $2b+1$ in $\mathbf P^{2b}$"; at $e=-1$ that is degree $2n-e=2n+1$ in $\PP^{2n}=\PP^{2n-e-1}$.

Indecomposable $X$ with $e=0$, $n\ge3$: Fuentes, Theorem 2.13(2)(c), "then $R$ is a smooth elliptic scroll of degree $2b$ in $\mathbf P^{2b-1}$", which at $e=0$ is degree $2n-e$ in $\PP^{2n-1}=\PP^{2n-e-1}$.

That the image is a scroll in the papers' sense is the identity $D\cdot f=1$ of step [](#s2){.pf-ref}: $\linearsystem{D}$ is unisecant, and the image of each ruling fibre is a line. Its genus is that of $C$, by Definition 1.5 of [2], so it is an elliptic scroll.
:::

:::

::: {.pf-step #s5}
The dimension is the one the exercise states: $\linearsystem{D}$ maps $X$ into $\PP^{d-1}$, with $d=2n-e$.

::: pf-proof
Theorem 3.10(1) of [2], is stated for a decomposable ruled surface, and there gives $N=h^0(\OO_X(\mfb))+h^0(\OO_X(\mfb+\mfe))-1$ for the projective space containing the scroll, together with $\deg(S)=2\deg\mfb-e$. Fuentes' Theorem 2.13, which covers the indecomposable surface and whose proof computes the same thing, gives $N$ by the identical sum: "R lies in $\mathbf P^N$ with $N=h^0(\OO_S(X_0+\mfb f))$ ... and $N=2b-e-1$", where the paper's $N$ is the dimension of the projective space and not the number of sections.

On the elliptic curve, $h^0(\OO_C(\mfa))=\deg\mfa$ for $\deg\mfa>0$, by Riemann--Roch with $K_C\cong\OO_C$. Here $n\ge e+3>0$ and $n-e\ge3>0$, so the two counts are $n$ and $n-e$ and
$$
h^0(\OO_X(D))=n+(n-e)=2n-e=d,
$$
on which the scroll lies in $\PP^{d-1}$.
:::

:::

::: {.pf-step #s6}
There is an elliptic scroll of degree $5$ in $\PP^4$.

::: pf-proof
Take $e=-1$ and $n=2$, so that $n=e+3$, and step [](#s4){.pf-ref} in its indecomposable case $e=-1$, Theorem 2.13(2)(b), gives a smooth elliptic scroll of degree $2\cdot2+1=5$ in $\PP^4$.
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} give the assertion for every $e\ge-1$ and $n\ge e+3$, and step [](#s6){.pf-ref} the stated degree-five example.
:::

:::

:::

::: {.remark title="Published solution"}
The three model descriptions transcribed in step [](#s4){.pf-ref} are Fuentes' classification of elliptic line scrolls, and together they prove the exercise for every $e\ge-1$ and $n\ge e+3$.

Luis Fuentes, *Classification of elliptic line scrolls* (arXiv:math/0009050v1): Theorem 1.7(2)(d), is the decomposable case, a smooth elliptic scroll of degree $2b-e$ in $\PP^{2b-e-1}$ for $b\ge3+e$; Theorem 2.13(2)(b), is the case $e=-1$, $b\ge2$, of degree $2b+1$ in $\PP^{2b}$; Theorem 2.13(2)(c), is the case $e=0$, $b\ge3$, of degree $2b$ in $\PP^{2b-1}$; Theorem 2.13(1)(a), is the remaining base-point-free case $e=-1$, $b=1$, a plane and a $3:1$ map, which the exercise excludes since it asks for $n\ge e+3=2$. The existence of the surfaces is Theorem 2.7, which proves it for $e=0$ and $e=-1$ from Theorem 2.1 with Propositions 2.5 and 2.6, with Remark 2.9, for the route through Nagata's theorem, and Theorem 3.2(1) of the authors' *The Projective Theory of Ruled Surfaces*, for $e\ge0$; the book's Theorem V.2.15, is an independent proof with uniqueness.

Luis Fuentes and Manuel Pedreira, *The Projective Theory of Ruled Surfaces* (arXiv:math/0006204v3), is Fuentes' reference [2], cited there in an earlier numbering: its Theorem 3.2(1), is $e\ge0$ with every $e\ge0$ occurring; its Theorem 3.9(3), is the very-ampleness criterion for a decomposable surface, cited as [2, Theorem 2.8]; its Theorem 3.10(1), is $N=h^0(\OO_X(\mfb))+h^0(\OO_X(\mfb+\mfe))-1$ with degree $2\deg\mfb-e$, cited as [2, Theorem 2.9].

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.13, argues as steps [](#s3){.pf-ref} to [](#s5){.pf-ref} do --- very ampleness from 5.2.12(b), $D\cdot f=1$, $D^2=2n-e$, and the count $h^0(\OO_C(n))+h^0(\OO_C(n-e))=2n-e$ --- and takes $e=-1$, $n=2$ for the degree-five example, but it does not construct the surface of invariant $e$, and the very-ampleness step it imports, its 5.2.12, carries absolute values that are wrong: at $e=-1$ with $\deg\mfb=1$ it gives $h^0(\OO_X(C_0+\mfb f))=2$ where the value is $3$; at $\deg\mfb=2$ its $4$ is $5$; and both of its $0$s are at least $1$, one summand being a divisor of positive degree on the elliptic curve. Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.13, counts $h^0\bigl(\OO_C(n)\oplus\OO_C(n-e)\bigr)$ by taking the second summand to contribute $n-1$, so writes the count as $2n-1$ and the ambient space as $\PP^{d-2}$; the second summand has degree $n-e>0$ and so contributes $n-e$, the count is $2n-e=d$ and the space $\PP^{d-1}$. His $2n-1$ is $d-1$ only at $e=0$, where the two agree, and is two short at $e=-1$. The count used in step [](#s5){.pf-ref} is the correct one. Algebraic Geometry II, National Taiwan University, 2020 Spring, has no entry for Exercise 13 of §2.
:::
