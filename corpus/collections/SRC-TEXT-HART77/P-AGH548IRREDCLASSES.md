---
schema: qual/card@1
id: P-AGH548IRREDCLASSES
kind: problem
title: Divisor classes on the cubic surface containing an irreducible curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.8*, whose retained companion solution is blank, and
    followed the printed hint through the cubic-surface blowup model, the 27
    (-1)-curves, Castelnuovo contraction, and the lower-degree del Pezzo
    surfaces. The key lemma used below is proved
    directly and does not invoke this exercise circularly: on X_r=Bl_r P^2
    for 2<=r<=6, every integral class nonnegative on all (-1)-curves is
    globally generated. If it has positive square, it has a smooth
    irreducible member. The proof contracts a zero-intersection (-1)-curve;
    if all intersections are positive, subtract -K and induct on
    anticanonical degree. X_2 is handled explicitly from the three
    base-point-free classes h, h-e_1, h-e_2. Necessity follows from adjunction:
    an irreducible curve of negative square is a line, and one of square zero
    is a degree-two rational conic.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete contraction/global-generation induction and the
    necessity argument. Made the anticanonical-degree-zero termination
    explicit, strengthened the positive-square lemma to a general smooth
    irreducible member, and independently enumerated the complementary
    degree-one square-minus-one classes in the conic case.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published-solution pass for issue #121. Read the printed exercise in
    Hartshorne, Algebraic Geometry (1977), *4.8, printed pp. 407-408 (text
    version tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed
    p. N is PDF p. N+15), with Theorem 4.9, printed pp. 402-403, Corollary
    4.13(b), printed p. 406, Theorem V.1.9, printed p. 364, and II.8.18,
    printed p. 179. Read at the cited places: Brian Harbourne, Anticanonical
    Rational Surfaces (24 January 1996, arXiv:alg-geom/9509001v2), Corollary
    II.3, Lemma II.6 and Theorem III.1, preprint pp. 3, 4 and 7 of the PDF,
    text version tmp/sources/harbourne-1995-anticanonical-rational-surfaces.md;
    I. V. Dolgachev, Topics in Classical Algebraic Geometry (27 September
    2010), Lemma 8.1.3 and Theorem 8.2.19, printed pp. 248 and 265, text
    version tmp/sources/dolgachev-topics-classical-ag.md, with the printed
    folios read in the PDF, where printed p. N is PDF p. N+10. Checked: that
    the cubic surface is a weak del Pezzo surface and a rational surface with
    -K = H ample and effective, so both sources' hypotheses hold; that the
    chain of steps in the third condition's sufficiency has its hypotheses in
    the order D.L >= 0, D numerically effective, D effective, base point
    free, not composed with a pencil, reduced irreducible general section,
    nonsingular general member; and that D.H >= 2 follows from Hodge index
    and D^2 > 0. Not located, in either source or elsewhere read for this
    card: a published proof that a class of degree 2 with D^2 = 0 on the
    cubic surface contains an irreducible nonsingular conic.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the published arguments transcribed, each step
    naming its source, statement and page; the card's earlier
    contraction-and-induction proof, which was not a transcription, is
    replaced by it. Steps negative-square-is-a-line and
    zero-square-is-a-conic are Dolgachev's Lemma 8.1.3 and its adjunction
    computation, the second applied at C^2 = 0, which the lemma does not
    treat; steps third-condition-contains-nonsingular-curve and
    lines-contain-nonsingular-curves are Dolgachev's Theorem 8.2.19 and
    Harbourne's Corollary II.3, Theorem III.1(a) and Lemma II.6(b), with
    Bertini from the book; steps equivalence-of-the-two-existence-conditions
    and conclusion state exactly what those give, and the case (b) of the
    converse is named there as not proved.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the card beside both sources. Checked: the adjunction
    computation in each of the two necessity steps, including that d =
    H.C is a positive integer and that p_a(C) >= 0 rules out C^2 = 0 with
    d = 1; that Lemma 8.1.3 leaves C^2 = -2 possible only for a weak Del
    Pezzo and that -K ample removes it; that Harbourne's Corollary II.3
    needs a numerically effective class meeting -K nonnegatively, and that
    Theorem III.1(a) needs -K.D >= 2, which Hodge index supplies; that
    Lemma II.6(b) applies to a base-point-free system with D^2 > 0. Not
    reviewed and not supplied: no proof for the existence of a conic in a
    class of degree 2 with square 0 was added, and the remark says why the
    one route available to the card (Lemma II.6(a), for which the class must
    first be known to be numerically effective) is not taken; the
    2026-11-16 COMPLAINTS record names that case.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass, on the reader's findings for this card. Two corrections.
    (i) The converse of alternative (b) was left open on the ground that the
    numerical effectivity of a class of degree 2 with square 0 is in neither
    source; that is false. Those classes are H-L for the 27 lines L, and
    (H-L).M = 1 - L.M >= 0 for every line M, since H.M = 1, L^2 = -1 and
    L.M is 0 or 1 for M different from L; so Dolgachev's Theorem 8.2.19
    (printed p. 265) gives numerical effectivity, Harbourne's Corollary II.3
    (preprint p. 3) effectivity, Theorem III.1(a) (preprint p. 7) base point
    freeness because -K.D = 2, and Lemma II.6(a) (preprint p. 4) with
    -K.D = 2 = 2r gives r = 1, so D is the class of a reduced irreducible
    curve of degree 2 and genus 0, that is a nonsingular plane conic. The
    enumeration of the 27 classes (a in {1,2,3}, one 1, four 1s, or one 2 and
    five 1s) is the card's own and is marked as such. (ii) The first pass
    invoked Bertini's theorem II.8.18, printed p. 179, which is a statement
    about hyperplane sections and so applies only to a very ample class; the
    third alternative's class need only be nef and big. The card now cites
    Corollary III.10.9, printed p. 274, with its characteristic 0 hypothesis
    stated, and Remark 10.9.3, printed p. 275, for the failure in
    characteristic p. Checked in this pass: the two equations of a degree-2
    class of square 0 and their 27 solutions; the identification of the three
    families with H-G_i, H-F_ij and H-E_i from the classes in Theorem 4.9;
    (H-L).M >= 0 on the 27 lines; -K.D = 2 and the case r = 1 of Lemma II.6(a).
    Not checked: no proof of nonsingularity in characteristic p was found or
    added, and the sources read supply none.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The classification is now proved in both directions for all three
    alternatives, with the conic case's numerical effectivity derived from
    the line intersections and the pencil case of Lemma II.6(a) at r = 1,
    and with Bertini's theorem cited in the characteristic 0 form. The
    enumeration of the 27 classes of degree 2 and square 0 is marked as the
    card's own. Process and provenance commentary is removed from the
    rendered card.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read against both sources. Checked the adjunction computations of the
    two necessity steps, that -K ample removes C^2 = -2, that Cauchy-Schwarz
    gives a in {1,2,3} and that sum b_i(b_i-1) = 0 forces the entries to be
    0 or 1, the three case identifications, the inequality on line
    intersections, the chain Dolgachev 8.2.19 to Harbourne II.3 to III.1(a)
    to II.6(a) with its hypothesis -K.D >= 2 and its case r = 1, and that a
    reduced irreducible curve of degree 2 is a nonsingular plane conic. Not
    reviewed: characteristic p remains outside what the sources give for the
    third alternative; the COMPLAINTS record of this date says so.
---

::: {.problem}
Show that a divisor class $D$ on the cubic surface contains an irreducible curve $\iff$ it contains an irreducible nonsingular curve $\iff$ it is either

(a) one of the 27 lines, or

(b) a conic (meaning a curve of degree 2) with $D^2=0$, or

(c) $D . L \geqslant 0$ for every line $L$, and $D^2>0$.

Hint: Generalize (4.11) to the surfaces obtained by blowing up $2,3,4$, or 5 points of $\PP^2$, and combine with our earlier results about curves on $\PP^1 \times \PP^1$ and the rational ruled surface $X_1$, (2.18).
:::

::: {.solution}

Write $X$ for the cubic surface, so that $-K_X=H$ is the hyperplane class, and let $k$ be
algebraically closed of characteristic $0$.

::: pf

::: {.pf-step #negative-square-is-a-line}
If $D$ contains an irreducible curve $C$ with $C^2<0$, then $C$ is one of the $27$ lines, so $D$ is
alternative (a).

::: pf-proof
$X$ is a weak Del Pezzo surface, so $C\cdot K_X\le0$. Adjunction gives
$$
C^2+C\cdot K_X=2h^1(C,\OO_C)-2\ge-2,
$$
so $C^2\ge-2$ and $h^1(C,\OO_C)=0$, which forces $C\cong\PP^1$: this is I. V. Dolgachev, *Topics in
Classical Algebraic Geometry* (September 27, 2010), Lemma 8.1.3 and its proof, printed p. 248. Since
$-K_X=H$ is ample on the cubic surface, $C\cdot K_X<0$ and $C^2=-2-C\cdot K_X>-2$, so $C^2=-1$; then
$$
H\cdot C=-C\cdot K_X=C^2+2=1,
$$
and $C$ is a line. By Theorem 4.9 of the book, printed pp. 402--403, the only irreducible curves of
negative self-intersection on $X$ are the $27$ lines $E_i,F_{ij},G_j$; the first paragraph of that
proof derives the same conclusion from $p_a(C)\ge0$ without the general lemma.
:::

:::

::: {.pf-step #zero-square-is-a-conic}
If $D$ contains an irreducible curve $C$ with $C^2=0$, then
$$
H\cdot C=2,
\qquad
p_a(C)=0,
$$
so $D$ is alternative (b).

::: pf-proof
Adjunction and $K_X=-H$ give
$$
0-H\cdot C=C^2+C\cdot K_X=2p_a(C)-2,
$$
so $2p_a(C)=2-H\cdot C$. Since $H$ is ample, $d=H\cdot C\ge1$, and since $p_a(C)=h^1(C,\OO_C)\ge0$
this gives $d\le2$; $d=1$ would give $2p_a(C)=1$. Hence $d=2$ and $p_a(C)=0$, so $C$ is a conic of
self-intersection $0$. The computation is the one in the proof of Dolgachev's Lemma 8.1.3, printed
p. 248, at $C^2=0$.
:::

:::

::: {.pf-step #positive-square-satisfies-the-third-condition}
If $D$ contains an irreducible curve $C$ with $C^2>0$, then
$$
C\cdot L\ge0\quad\text{for every line }L,
\qquad
C^2>0,
$$
so $D$ is alternative (c).

::: pf-proof
Two distinct irreducible curves on a surface have nonnegative intersection number, $C\cdot L$ being a
sum of local intersection multiplicities, and if $C=L$ then $C^2=-1<0$. Since $C$ is not a line,
$C\ne L$ for each of the $27$ lines $L$, so $C\cdot L\ge0$.
:::

:::

::: {.pf-step #lines-contain-nonsingular-curves}
Every class in alternative (a) contains an irreducible nonsingular curve.

::: pf-proof
By Theorem 4.9 of the book, printed pp. 402--403, the $27$ classes $E_i,F_{ij},G_j$ are the classes
of the $27$ lines of $X$, each isomorphic to $\PP^1$.
:::

:::

::: {.pf-step #third-condition-contains-nonsingular-curve}
Let $D$ satisfy
$$
D\cdot L\ge0\quad\text{for every one of the }27\text{ lines }L,
\qquad
D^2>0 .
$$
Then the complete linear system $\linearsystem{D}$ has an irreducible nonsingular member.

::: pf-proof
First, $D$ is numerically effective: by Dolgachev, Theorem 8.2.19, printed p. 265, the effective cone
of a Del Pezzo surface of degree $d\ne8,9$ is generated by the classes of its $(-1)$-curves, which on
the cubic surface are the $27$ lines, so a class meeting every line nonnegatively meets every
effective class nonnegatively.

Second, $D$ is effective: by B. Harbourne, *Anticanonical Rational Surfaces* (24 January 1996,
arXiv:alg-geom/9509001v2), Corollary II.3, preprint p. 3, a numerically effective divisor meeting the
anticanonical class nonnegatively lies in $\mathrm{Eff}$, and here $-K_X\cdot D=D\cdot H>0$, while
$D\cdot H\ge2$: the Hodge index inequality, Theorem V.1.9 of the book, printed p. 364, gives
$3D^2\le(D\cdot H)^2$ with $D^2>0$, so $(D\cdot H)^2\ge4$ and $D\cdot H$ is a positive integer.

Third, the system is base point free and $h^1$ vanishes: since $-K_X\cdot D=D\cdot H\ge2$,
Harbourne's Theorem III.1(a), preprint p. 7, gives $h^1(X,\OO_X(D))=0$ and that the sections of $D$
are base point (and hence fixed component) free.

Fourth, a general member is reduced and irreducible: since $D^2>0$ the system is not composed with a
pencil, and Harbourne's Lemma II.6(b), preprint p. 4, then gives $D^2>0$ and that the general section
of $D$ is reduced and irreducible.

Finally, it is nonsingular: a general member of a base-point-free linear system on a nonsingular
projective surface over an algebraically closed field of characteristic $0$ is nonsingular, which is
Bertini's theorem in Corollary III.10.9 of the book, printed p. 274. Over a field of characteristic
$p$ that corollary fails, as its Remark 10.9.3, printed p. 275, records, and Lemma II.6(b) then gives
only a reduced irreducible member.
:::

:::

::: {.pf-step #conic-classes-contain-a-conic}
Every class in alternative (b) contains an irreducible nonsingular conic.

::: pf-proof
Let $D$ satisfy $D\cdot H=2$ and $D^2=0$. The classes with these two invariants are the classes
$H-L$ for the $27$ lines $L$: writing $D\sim a\ell-\sum_ib_ie_i$, the conditions
$$
3a-\sum_ib_i=2,
\qquad
a^2-\sum_ib_i^2=0
$$
give $\sum_ib_i=3a-2$ and $\sum_ib_i^2=a^2$, hence
$$
\sum_ib_i(b_i-1)=a^2-3a+2 .
$$
Cauchy--Schwarz applied to the sequences $1$ and $b_i$ gives $(3a-2)^2\le6a^2$, that is
$3a^2-12a+4\le0$, so $a\in\{1,2,3\}$. For $a=1$ and $a=2$ the sum of $b_i(b_i-1)$ vanishes, and
since each $b_i(b_i-1)\ge0$ for an integer $b_i$, every entry is $0$ or $1$: with $\sum_ib_i=1$ that
is one entry $1$, and with $\sum_ib_i=4$ it is four entries $1$. For $a=3$ the sum is $2$ and
$\sum_ib_i=7$, so exactly one entry is $2$ and the other five are $1$. These are the classes
$H-G_i$, $H-F_{ij}$ and $H-E_i$, by the classes of those lines in Theorem 4.9, printed pp. 402--403.

For $M$ a line, $H\cdot M=1$, and $L\cdot M$ is $-1$ if $M=L$ and $0$ or $1$ if $M\ne L$; hence
$$
(H-L)\cdot M=1-L\cdot M\ge0
$$
for every one of the $27$ lines, with equality only for the lines meeting $L$ and not equal to it.
So $D$ is numerically effective by Dolgachev's Theorem 8.2.19, printed p. 265, and effective by
Harbourne's Corollary II.3, preprint p. 3, since $-K_X\cdot D=D\cdot H=2>0$. Then Theorem III.1(a),
preprint p. 7, applied to the bound $-K_X\cdot D\ge2$ gives that the sections of $D$ are base point
free. Since $D^2=0$, the system is composed with a pencil, and Lemma II.6(a), preprint p. 4, with
$-K_X\cdot D=2$ gives $D=rC$ with $r=1$ and $C$ the class of a reduced irreducible curve moving in a
pencil; so $D$ itself is the class of a reduced irreducible curve $C$ with $C\cdot H=2$ and, by step
[](#zero-square-is-a-conic){.pf-ref}, $p_a(C)=0$. A reduced irreducible curve of degree $2$ spans a
plane and is an irreducible plane conic, and a singular plane conic is a pair of lines; so $C$ is
nonsingular.
:::

:::

::: {.pf-step #classification-and-equivalence}
A class contains an irreducible curve if and only if it contains an irreducible nonsingular curve,
and this happens exactly in alternatives (a), (b) and (c).

::: pf-proof
If $D$ contains an irreducible curve $C$, then $C^2<0$, $C^2=0$ or $C^2>0$, and steps
[](#negative-square-is-a-line){.pf-ref}, [](#zero-square-is-a-conic){.pf-ref} and
[](#positive-square-satisfies-the-third-condition){.pf-ref} place $D$ in alternatives (a), (b) and
(c) respectively. Conversely steps [](#lines-contain-nonsingular-curves){.pf-ref},
[](#conic-classes-contain-a-conic){.pf-ref} and
[](#third-condition-contains-nonsingular-curve){.pf-ref} give an irreducible nonsingular member of
every class in alternatives (a), (b) and (c). An irreducible nonsingular curve is an irreducible
curve, so the two existence conditions agree, and both are equivalent to the classification.
:::

:::

::: {.pf-step #conclusion}
A divisor class on the cubic surface contains an irreducible curve if and only if it is one of the
$27$ lines, or a conic of degree $2$ with $D^2=0$, or satisfies $D\cdot L\ge0$ for every line $L$
with $D^2>0$; and then it contains an irreducible nonsingular curve.

::: pf-proof
Step [](#classification-and-equivalence){.pf-ref} gives both directions and the equivalence of the two
existence conditions.
:::

:::

::: pf-qed
Steps [](#negative-square-is-a-line){.pf-ref}, [](#zero-square-is-a-conic){.pf-ref} and
[](#positive-square-satisfies-the-third-condition){.pf-ref} are the necessity of the three
alternatives; steps [](#lines-contain-nonsingular-curves){.pf-ref},
[](#conic-classes-contain-a-conic){.pf-ref} and
[](#third-condition-contains-nonsingular-curve){.pf-ref} are their sufficiency, with irreducible
nonsingular members; step [](#classification-and-equivalence){.pf-ref} is the equivalence of the two
existence conditions.
:::

:::
:::

::: {.remark title="Published solution"}
Brian Harbourne, *Anticanonical Rational Surfaces* (24 January 1996, arXiv:alg-geom/9509001v2):
Corollary II.3, preprint p. 3, that a numerically effective divisor meeting $-K$ nonnegatively is
effective; Lemma II.6, preprint p. 4, that a fixed-component-free class whose system is not composed
with a pencil has $D^2>0$ and reduced irreducible general section, and that a class whose system is
composed with a pencil is a multiple of a class with reduced irreducible general section; and Theorem
III.1(a), preprint p. 7, that $-K_X\cdot D\ge2$ makes the system base point free with $h^1=0$. The
paper works over an algebraically closed field of arbitrary characteristic, so its Lemma II.6 gives
reduced irreducible members in every characteristic, while the nonsingularity of the member of a
class of the third alternative is Bertini's theorem in characteristic $0$.

I. V. Dolgachev, *Topics in Classical Algebraic Geometry* (September 27, 2010): Lemma 8.1.3 and its
proof, printed p. 248, on irreducible curves of negative self-intersection on a weak Del Pezzo
surface; Theorem 8.2.19, printed p. 265, that the effective cone of a Del Pezzo surface of degree
$d\ne8,9$ is generated by its $(-1)$-curves, whose proof leaves the degrees $8$ and $9$ to the
reader.

Theorem 4.9 of Hartshorne, printed pp. 402--403, for the $27$ lines and for the curves of negative
self-intersection; Corollary III.10.9, printed p. 274, and its Remark 10.9.3, printed p. 275, for
Bertini's theorem in characteristic $0$ and its failure in characteristic $p$.
:::
