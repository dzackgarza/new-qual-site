---
schema: qual/card@1
id: P-AGH5210CANONSCROLL
kind: problem
title: Canonical curves on a rational scroll and nonhyperelliptic curves with a $g^1_3$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Canonical Divisor
relations: []
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry (1977), Chapter V, section 2,
    exercise 2.10, printed page 385 (PDF page 400 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, the checked-in
    extraction). The printed exercise reads: "For any n > e >= 0, let X be the
    rational scroll of degree d = 2n - e in P^{d+1} given by (2.19). If
    n >= 2e - 2, show that X contains a nonsingular curve Y of genus g = d + 2
    which is a canonical curve in this embedding. Conclude that for every
    g >= 4, there exists a nonhyperelliptic curve of genus g which has a g_3^1."
    The card states exactly this. The proof was read and checked, and the two
    numerical claims were recomputed: with H = C_0 + nf, H^2 = 2n - e = d and
    K.H = e - 2n - 2, so a member of |H - K_X| has degree
    H.(H - K_X) = 4n - 2e + 2 = 2g - 2 and genus g = d + 2; adjunction gives
    K_Y = (K_X + Y)|_Y = H|_Y, so Y is canonical in the embedding. Base-point
    freeness comes from pi_*O(aC_0 + bf) = sum_{i=0}^{a} O(b - ie) with a = 3
    and b - 3e = n - 2e + 2 >= 0, which is exactly the hypothesis
    n >= 2e - 2; the q = 0 case uses D.C_0 = 3(C_0 + ef).C_0 = 0 and Bertini off
    the contracted section. No retained solution set in the repository covers
    this exercise (Egbert's set, the only one that mentions scrolls, does not
    treat it), so the proof is derived and says so; the hyperplane class and
    K_X are taken from [[FE-TORHIRZ]].
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Rechecked against the printed exercise, printed page 385, and against two
    published treatments outside the twelve retained sets. Algebraic Geometry
    II, National Taiwan University, 2020 Spring, Chapter V homework, Exercise 10
    of section 2, PDF p. 8 (tmp/sources/ntu-ag2-chapter5.pdf), carries the same
    construction and cites Corollary 2.18, printed page 380, for the nonsingular
    member; it does not prove that the embedding of Y is complete, which is step
    s6 here and needs H^0(O_X(H)) = H^0(Y,K_Y) together with
    h^0(O_X(H)) = 2n-e+2. Yang Pi-Yeh, Hartshorne Solutions, exercise 5.2.10,
    printed p. 104 (tmp/sources/lfwin-hartshorne-solutions.pdf), computes the
    genus and the g_3^1 and never shows the member nonsingular or K_Y the
    restricted hyperplane class. All eight steps were re-read: the pushforward
    pi_*O(aC_0+bf) as the sum of O(b-ie) with b-3e = n-2e+2 >= 0 for
    base-point freeness, D.C_0 = 0 in the q = 0 branch, H^i(X,O(-D)) = 0 from
    H^i(X,O(H)) with R^1 pi_*O(H) = 0, H.D = 4n-2e+2, and
    h^0(O_X(H)) = 2n-e+2 = d+2. Not checked: whether Corollary 2.18's criterion
    covers the e = 0 case of the q = 0 branch exactly as used; the card proves
    that branch separately.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes and Pedreira (arXiv:math/0006204v3), Sections 2 and 3, printed
    pp. 7 to 25, on 2026-11-16: their results are base-point and very-ampleness
    criteria for the linear system of the divisor C_0 + bf, and they contain no
    statement that a curve of genus d+2 inside the rational scroll is canonical in
    its embedding, so the exercise is not in the paper. Sections 5 and 6 introduce
    "canonical surfaces" and "canonical scrolls" in the sense of scrolls of
    speciality one, and defer their characterization to the authors' "Canonical
    geometrically ruled surfaces", their reference [5], which is not retained and
    was not read; that notion is not the canonical curve inside a rational scroll
    asked for here. A search outside the checkout for a complete published proof
    that every genus at least four carries a nonhyperelliptic curve with a g^1_3
    returned two papers on canonical models lying on scrolls, arXiv:1502.07556 and
    arXiv:1803.10899, both of which begin with a trigonal curve and study its
    canonical model rather than constructing one, so neither supplies the
    conclusion. Hannah Markwig and Angelina Zheng, "Trigonal and embedded
    tropical curves of low genus" (arXiv:2602.02257), read in its introduction,
    states that a trigonal curve of genus g and Maroni invariant n has class
    3E_n + ((g+3n+2)/2)F_n in the Hirzebruch surface, which again begins with the
    curve and so is not the existence construction of this exercise. No complete
    published argument located; steps s1 to s5 remain the card's.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Restored the event of 2026-11-11 above to its text of that date, removing the
    text-version names that a later commit of 2026-11-16 inserted into it. The
    two sources it cites are in tmp/sources/ntu-ag2-chapter5.md and
    tmp/sources/lfwin-hartshorne-solutions.md, beside their PDFs, and the remark
    names the text version of each source it cites. Also corrected the page range
    of Fuentes--Pedreira's Sections 2 and 3 in the event above, which read "pp. 11
    to 22": section 2 begins on printed p. 7 and section 4 has begun by printed
    p. 25, whose text is item 7 of the list in Proposition 4.2, so the range is
    pp. 7 to 25. Nothing else in the audit changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcribed the exercise on 2026-11-16 from two published sources read in
    their text versions, and re-read the printed exercise at Hartshorne,
    Algebraic Geometry (1977), V.2, exercise 2.10, printed p. 385 (PDF p. 400).
    The construction is Hartshorne's own Corollary 2.18(b), printed p. 380:
    for D = aC_0+bf on the rational ruled surface X_e with e at least 0, the
    system |D| contains an irreducible nonsingular curve exactly when
    (a,b) = (0,1), (a,b) = (1,0), a>0 and b>ae, or e>0, a>0 and b=ae. With
    D = H-K_X = 3C_0+(n+e+2)f the two live branches are b>ae, that is
    n>2e-2, and b=ae, that is n=2e-2 with e>0, so the hypothesis n at least
    2e-2 is exactly that criterion, in both of its cases; this closes what the
    earlier events recorded as the card's own steps s1 to s3, including the
    irreducibility of the member. The count h^0(O_X(H)) = 2n-e+2 is the proof
    of Corollary 2.19 on the same printed page. Reid, Chapters on Algebraic
    surfaces, read in tmp/sources/reid-chapters-algebraic-surfaces.md: §2.7
    Remark, printed p. 19, gives the canonical class of F(a_1,...,a_n); §2.8
    Theorem (2) with (2.8.1), printed p. 19, is the base-locus criterion; §2.9,
    printed p. 20, sets A = L, B = B_0 with A^2 = 0, AB = 1, B^2 = -a and
    |eL+dM| = |(e+ad)A+dB|; §2.10, printed pp. 20-21, establishes that the
    canonical curve of the scroll F(a_1,a_2) = F_a in P^{g-1} has class
    alpha A + 3B with alpha = a+a_2+2, that a nonsingular curve of that class
    exists if and only if alpha-3a = B.(alpha A+3B) is at least 0, and that
    this is the Maroni inequality 3a at most g+2. Checked the translation
    between the two normalizations: a_1 = n-e, a_2 = n, a = a_2-a_1 = e,
    g = a_1+a_2+2 = d+2, a_2A+B = C_0+nf = H, alpha = n+e+2 and
    alpha-3a = n-2e+2, so Reid's criterion is the same inequality. Not checked:
    whether some other published treatment states the restriction isomorphism
    of step s5 outright; the step rests on the book's Corollary 2.19 count and
    on H^0(O_X(K_X)) = H^1(O_X(K_X)) = 0, both proved on the card.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected three citations on the card on 2026-11-16, after the events above
    of the same date. Corollary 2.19 and its proof sit on printed p. 381, not
    p. 380, where the marker for PDF p. 396 falls between Corollary 2.18 and it;
    the three places naming p. 380 for it now say p. 381, and Corollary 2.18(b)
    keeps p. 380. The adjunction formula in step s3 is Proposition V.1.5,
    printed p. 361, which is stated for a nonsingular curve and so applies to
    the member Y of step s2; Theorem V.1.3 is the definition of the intersection
    number, printed p. 358. The remark's step references are renumbered to the
    present steps: the construction is s1 to s5 with the g^1_3 in s7, and the
    completeness of the embedding, which was s6 before the renumbering, is s5.
    The remark no longer carries machine paths to text versions, which belong in
    these events, and its Egbert entry states what his reference is rather than
    what is absent from a directory. Not checked: nothing new; the mathematics
    of the steps is as recorded above.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the card again on 2026-11-16 on the reader's report, after the
    event above of the same date, which is left as written. The event above
    says that the three places naming printed p. 380 for Corollary 2.19 now say
    p. 381; one of them did not. The count h^0(O_X(H)) = 2n-e+2 in the proof of
    step s5 still named p. 380 and now names p. 381, which was checked again
    here in the text version of the book: Corollary 2.19 and its proof sit
    under the marker for PDF page 396, printed p. 381 at the offset 15 this
    extraction takes, while Corollary 2.18 and its proof sit under the marker
    for PDF page 395, printed p. 380. Step s5's restriction isomorphism is the
    card's own, as the record of this date says and as its event should have
    made the step say; the step now marks it so where the isomorphism is used.
    The remark's sentence "which neither source states" is removed in favour of
    the two vanishings and their reason: whether a source states a step is not
    content for a rendered remark, and the absence is recorded here.
---

::: {.problem}
For any $n>e \geqslant 0$, let $X$ be the rational scroll of degree $d=2 n-e$ in $\PP^{d+1}$ given by (2.19). If $n \geqslant 2 e-2$, show that $X$ contains a nonsingular curve $Y$ of genus $g=d+2$ which is a canonical curve in this embedding.

Conclude that for every $g \geqslant 4$, there exists a nonhyperelliptic curve of genus $g$ which has a $g_3^1$.
Cf.
(IV, §5).

:::

::: {.solution}
Write $X=\FF_e$, let $C_0$ be its negative section and $f$ a fibre of the ruling
$$
\pi:X\longrightarrow\PP^1,
$$
so that
$$
C_0^2=-e,
\qquad
C_0\cdot f=1,
\qquad
f^2=0,
\qquad
K_X\sim-2C_0-(e+2)f
$$
[[FE-TORHIRZ]], the last line being Lemma 2.10, printed p. 373. In the embedding of (2.19), which Corollary 2.19, printed p. 381, produces from the very ample divisor $C_0+nf$, the hyperplane class is
$$
H\sim C_0+nf,
\qquad
H^2=2n-e=d.
$$

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} are transcribed from Hartshorne's Corollary 2.18(b), printed p. 380, and Corollary 2.19, printed p. 381, with the identification of the divisor $H-K_X$ with the class of a canonical curve on the scroll taken from Reid, *Chapters on Algebraic surfaces*, §2.8 Theorem, §2.9 and §2.10, printed pp. 19--21; steps [](#s3){.pf-ref} to [](#s7){.pf-ref} finish the exercise.

::: pf

::: {.pf-step #s1}
The divisor
$$
D\coloneqq H-K_X
\sim
3C_0+(n+e+2)f
$$
is, in the notation of Reid §2.9, the class
$$
\alpha A+3B,
\qquad
\alpha=n+e+2=a+a_2+2,
$$
where $a=e$ is the Maroni invariant of the scroll and $a_1=n-e$, $a_2=n$ are its two scroll parameters.

::: pf-proof
Substituting $H\sim C_0+nf$ and $K_X\sim-2C_0-(e+2)f$ gives $D\sim3C_0+(n+e+2)f$. Reid §2.9, printed p. 20, writes the surface scroll $\FF_a=\FF(0,a)$ with $A=L$ the class of a fibre and $B=B_0$ the negative section, and $\Pic\FF_a=\ZZ A\oplus\ZZ B$ with $A^2=0$, $A\cdot B=1$, $B^2=-a$; there $f=A$ and $C_0=B$, and so $D=3B+\alpha A$ with $\alpha=n+e+2$. Reid §2.10, printed p. 20, writes the scroll of the exercise as $\FF(a_1,a_2)$ with $a_1=n-e$, $a_2=n$, embedded in $\PP^{g-1}$ by $a_2A+B=nA+B=C_0+nf=H$, and its genus as $g=a_1+a_2+2=2n-e+2=d+2$; the canonical curve of that scroll is linearly equivalent to $\alpha A+3B$ with $\alpha=a+a_2+2$, and $a=a_2-a_1=e$. The two expressions for $\alpha$ agree.

:::

:::

::: {.pf-step #s2}
The linear system $\linearsystem{D}$ contains an irreducible nonsingular curve $Y$.

::: pf-proof
This is Hartshorne, Corollary 2.18(b), printed p. 380: for a divisor $D=aC_0+bf$ on the rational ruled surface $X_e$ with $e\ge0$, the system $\linearsystem{D}$ contains an irreducible nonsingular curve exactly when one of $a=0,b=1$; $a=1,b=0$; $a>0,b>ae$; or $e>0,a>0,b=ae$ holds. Here $a=3$ and $b=n+e+2$, so $b>ae=3e$ is the inequality $n>2e-2$, and $b=ae$ is $n=2e-2$ with $e>0$; the hypothesis $n\ge2e-2$ therefore gives one of the two. Reid gives the same criterion in his coordinates: by Theorem 2.8, $\FF_a$ contains a nonsingular curve linearly equivalent to $\alpha A+3B$ if and only if $\alpha-3a=B\cdot(\alpha A+3B)\ge0$, printed p. 21, and $\alpha-3a=n-2e+2$. The two branches of Hartshorne's proof are its two cases: for $b>ae$ the corollary writes $D$ as a sum of base-point-free and very ample classes and applies Bertini's theorem, and for $b=ae$ it realizes $X_e$ as the blow-up of the vertex of a cone and applies Bertini's theorem there, off the vertex.

:::

:::

::: {.pf-step #s3}
The canonical bundle of $Y$ is the restriction of the hyperplane bundle:
$$
\boxed{K_Y\cong\OO_Y(H)}.
$$

::: pf-proof
Adjunction, Proposition V.1.5, printed p. 361, applied to the nonsingular curve $Y$, and the definition $D=H-K_X$ give
$$
K_Y\cong\restrictionof{(K_X+Y)}{Y}\cong\restrictionof{(K_X+D)}{Y}\cong\OO_Y(H).
$$
In Reid's coordinates this is the identity $\alpha=a+a_2+2$ of step [](#s1){.pf-ref}: adjunction on the scroll gives $K_Y=\restrictionof{(K_{\FF_a}+Y)}{Y}$ with $K_{\FF_a}\sim-(2+a)A-2B$, so $K_Y\sim(\alpha-2-a)A+B$, which is the restriction of the hyperplane class $a_2A+B$ exactly because $\alpha=a+a_2+2$.

:::

:::

::: {.pf-step #s4}
$$
\boxed{g(Y)=d+2}.
$$

::: pf-proof
By step [](#s3){.pf-ref},
$$
2g(Y)-2=\deg K_Y=H\cdot D,
$$
and with $H=C_0+nf$ and $D=3C_0+(n+e+2)f$,
$$
H\cdot D=-3e+(n+e+2)+3n=4n-2e+2=2(2n-e)+2=2d+2 .
$$

:::

:::

::: {.pf-step #s5}
The restriction map
$$
H^0(X,\OO_X(H))\longrightarrow H^0(Y,K_Y)
$$
is an isomorphism, so the given embedding of $Y$ is its complete canonical embedding.

::: pf-proof
Because $Y\sim D=H-K_X$, restriction gives
$$
0\longrightarrow\OO_X(K_X)\longrightarrow\OO_X(H)\longrightarrow\OO_Y(H)\longrightarrow0 .
$$
The first cohomology group vanishes, $H^0(X,\OO_X(K_X))=0$, since an effective canonical divisor would meet a general fibre nonnegatively whereas $K_X\cdot f=-2$; and $H^1(X,\OO_X(K_X))\cong H^1(X,\OO_X)^\vee=0$ by Serre duality, with $H^1(X,\OO_X)=0$ because $X$ is ruled over $\PP^1$ and $q(X)$ is the genus of the base, Corollary 2.5, printed p. 371. Hence $h^0(\OO_Y(H))=h^0(\OO_X(H))$, and the proof of Corollary 2.19, printed p. 381, computes
$$
h^0(X,\OO_X(H))=h^0(\PP^1,\OO(n))+h^0(\PP^1,\OO(n-e))=2n-e+2=d+2,
$$
which is $g(Y)$ by step [](#s4){.pf-ref}. The hyperplane sections of $Y$ therefore span the whole of $H^0(Y,K_Y)$, and the embedding of $Y$ in $\PP^{d+1}$ is the complete canonical one, $\PP^{d+1}=\PP H^0(Y,K_Y)^\vee$. The isomorphism itself is the card's own, assembled from the count in the proof of Corollary 2.19 and the two vanishings above.

:::

:::

::: {.pf-step #s6}
For every integer $g\ge4$ there are integers $n>e\ge0$ with
$$
2n-e=g-2
\qquad\text{and}\qquad
n\ge2e-2 .
$$

::: pf-proof
Put $d=g-2\ge2$. If $d$ is even, take $e=0$ and $n=d/2$; then $n>e$, $2n-e=d$ and $n\ge2e-2$. If $d$ is odd, so $d\ge3$, take $e=1$ and $n=(d+1)/2$; then $n>1=e$, $2n-e=d$, and $n\ge0=2e-2$. These are the pairs exhibiting the inequality $3a\le g+2$ of Reid §2.10, printed p. 21, as an existence condition rather than a constraint: with $a=e$ and $2n-e=d=g-2$ it reads $3e\le d+4$, that is $n\ge2e-2$.

:::

:::

::: {.pf-step #s7}
The curve $Y$ carries a $g^1_3$ and is nonhyperelliptic.

::: pf-proof
The ruling restricts to a morphism
$$
\restrictionof{\pi}{Y}:Y\longrightarrow\PP^1
$$
of degree
$$
Y\cdot f=D\cdot f=3,
$$
so the pullback of $\linearsystem{\OO_{\PP^1}(1)}$ is a base-point-free $g^1_3$ on $Y$; Reid §2.10, printed p. 20, records this as the statement that the pencil $A$ of the scroll cuts out the $g^1_3$ on its canonical curve. By step [](#s5){.pf-ref} the complete canonical map of $Y$ is an embedding, whereas a hyperelliptic curve of genus at least $2$ has canonical map of degree $2$ onto a rational normal curve; so $Y$ is not hyperelliptic.

:::

:::

::: pf-qed
Steps [](#s1){.pf-ref} to [](#s5){.pf-ref} produce the nonsingular curve $Y$ of genus $d+2$ which is canonical in the given embedding, and steps [](#s6){.pf-ref} and [](#s7){.pf-ref} give, for every $g\ge4$, a nonhyperelliptic curve of genus $g$ with a $g^1_3$.

:::

:::

:::

::: {.remark title="Published solution"}
Hartshorne's own Corollary 2.18(b), printed p. 380, is a complete published proof that $\linearsystem{H-K_X}$ contains an irreducible nonsingular curve for $n\ge2e-2$, and the proof of Corollary 2.19, printed p. 381, is the count $h^0(\OO_X(H))=2n-e+2$; Reid, *Chapters on Algebraic surfaces*, §2.8 Theorem with (2.8.1), printed p. 19, §2.9, printed p. 20, and §2.10, printed pp. 20--21, identifies the class $3C_0+(n+e+2)f$ with $\alpha A+3B$, $\alpha=a+a_2+2$, of the canonical curve of the scroll, states the nonsingularity criterion as $\alpha-3a\ge0$, and reads the inequality $3a\le g+2$ as the Maroni constraint. Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} are those two statements specialized to $a_1=n-e$, $a_2=n$, $a=e$; steps [](#s3){.pf-ref} to [](#s7){.pf-ref} assemble them; step [](#s5){.pf-ref} adds the vanishing of $H^0(X,\OO_X(K_X))$ and of $H^1(X,\OO_X(K_X))$, which follow from $K_X\cdot f=-2$ and from $q(X)=0$.
Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 10 of §2 (solution by Chi-Kang), printed p. 8 of that set, runs the same construction: with $D=C_0+nf$ the very ample class of the embedding, it takes $Y\in\abs{D-K_X}=\abs{3C_0+(n+e+2)f}$, which by Corollary 2.18 (printed page 380) has a nonsingular member under $e\ge0$ and $n+e+2\ge3e$, the hypothesis $n\ge2e-2$; adjunction gives $K_Y=D\restriction_Y$, then $\deg K_Y=D\cdot Y=4n-2e+2=2d+2$, so $g(Y)=d+2$, and $f\cdot Y=3$ gives a $g^1_3$. That is steps [](#s1){.pf-ref} to [](#s5){.pf-ref} and step [](#s7){.pf-ref}. It does not check that the embedding of $Y$ is the complete canonical one, which needs $H^0(\OO_X(H))\cong H^0(Y,K_Y)$; step [](#s5){.pf-ref} supplies that, and it is what makes the conclusion a canonical curve rather than a curve whose canonical class happens to be the restriction.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.10, printed p. 104, argues that "$3C_0+af$ can be written as a curve iff $C\cdot C_0\ge0$, i.e. $a\ge3e$", computes $2g-2=C\cdot(C+K)=4n-2e+2$ and reads off $g=2n-e+2$ and $C\cdot f=3$; it does not show the member nonsingular, and it never identifies $K_Y$ with the restricted hyperplane class.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.10: the whole of his entry is "See example 2.10 in Kollar's Complex Algebraic Geometry", which is a reference to Kollár's Example 2.10 and gives no argument.

:::
