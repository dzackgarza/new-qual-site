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
---

::: {.problem}
Show that a divisor class $D$ on the cubic surface contains an irreducible curve $\iff$ it contains an irreducible nonsingular curve $\iff$ it is either

(a) one of the 27 lines, or

(b) a conic (meaning a curve of degree 2) with $D^2=0$, or

(c) $D . L \geqslant 0$ for every line $L$, and $D^2>0$.

Hint: Generalize (4.11) to the surfaces obtained by blowing up $2,3,4$, or 5 points of $\PP^2$, and combine with our earlier results about curves on $\PP^1 \times \PP^1$ and the rational ruled surface $X_1$, (2.18).
:::

::: {.solution}

The classification is assembled from two published sources, and each step names the source, its
numbered statement and its page. Harbourne, *Anticanonical Rational Surfaces* (January 24, 1996,
arXiv:alg-geom/9509001v2), Corollary II.3 on preprint p. 3, Lemma II.6 on preprint p. 4 and Theorem
III.1 on preprint p. 7 (text version
`tmp/sources/harbourne-1995-anticanonical-rational-surfaces.md`), determines the linear systems of
numerically effective classes on a rational surface with an effective anticanonical divisor; the
cubic surface is one, with $-K_S$ the hyperplane class $H$. Dolgachev, *Topics in Classical
Algebraic Geometry* (September 27, 2010), Lemma 8.1.3 on printed p. 248 and Theorem 8.2.19 on
printed p. 265 (text version `tmp/sources/dolgachev-topics-classical-ag.md`), gives the curves of
negative self-intersection on a Del Pezzo surface and the effective cone of the cubic surface.
Nonsingularity of a general member comes from the book's Bertini theorem, II.8.18, printed p. 179,
as at (4.13)(b), printed p. 406.

::: pf

::: {.pf-step #negative-square-is-a-line}
If $D$ contains an irreducible curve $C$ with $C^2<0$, then $C$ is one of the $27$ lines, so $D$ is
alternative (a).

::: pf-proof
The cubic surface is a weak Del Pezzo surface, so $C\cdot K_S\le0$ for every irreducible curve $C$.
Adjunction gives
$$
C^2+C\cdot K_S=2h^1(C,\OO_C)-2\ge-2,
$$
so $C^2\ge-2$, and $h^1(C,\OO_C)=0$, which forces $C\cong\PP^1$: this is Dolgachev's Lemma 8.1.3
and its proof, printed p. 248, which concludes that $C$ is a smooth rational curve with $C^2=-1$ or
$-2$. On the cubic surface $-K_S=H$ is ample, so $C\cdot K_S<0$ and
$C^2=-2-C\cdot K_S>-2$, leaving $C^2=-1$; then
$$
H\cdot C=-C\cdot K_S=C^2+2=1,
$$
so $C$ has degree $1$ and is a line. By Theorem 4.9 of the book, printed pp. 402--403, the only
irreducible curves of negative self-intersection on the cubic surface are the $27$ lines
$E_i,F_{ij},G_j$, and the same paragraph of that proof derives the conclusion directly from
$p_a(C)\ge0$ without the general lemma.
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
Adjunction and $K_S=-H$ give
$$
0-H\cdot C=C^2+C\cdot K_S=2p_a(C)-2,
$$
so $2p_a(C)=2-H\cdot C$. Since $H$ is ample, $d=H\cdot C\ge1$, and since $p_a(C)=h^1(C,\OO_C)\ge0$
this gives $d\le2$; $d=1$ would give $2p_a(C)=1$. Hence $d=2$ and $p_a(C)=0$, that is, $C$ is a
conic of self-intersection $0$. The computation is the one in the proof of Dolgachev's Lemma 8.1.3,
printed p. 248, applied at $C^2=0$; that lemma states it only for $C^2<0$.
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
Two distinct irreducible curves on a surface have nonnegative intersection number, since $C\cdot L$
is a sum of local intersection multiplicities, and if $C=L$ then $C^2=-1<0$. Since $C$ is not a
line, $C\ne L$ for each of the $27$ lines $L$, so $C\cdot L\ge0$, and $C^2>0$ by hypothesis.
:::

:::

::: {.pf-step #lines-contain-nonsingular-curves}
Every class in alternative (a) contains an irreducible nonsingular curve.

::: pf-proof
By Theorem 4.9 of the book, printed pp. 402--403, the $27$ classes $E_i,F_{ij},G_j$ are the classes
of the $27$ lines on $X$, each of them isomorphic to $\PP^1$ and hence irreducible and nonsingular.
:::

:::

::: {.pf-step #third-condition-contains-nonsingular-curve}
Let $D$ be a class with
$$
D\cdot L\ge0\quad\text{for every one of the }27\text{ lines }L,
\qquad
D^2>0 .
$$
Then $\linearsystem{D}$ has an irreducible nonsingular member.

::: pf-proof
Four published steps.

First, $D$ is numerically effective. By Dolgachev, Theorem 8.2.19, printed p. 265, the effective cone
of a Del Pezzo surface of degree $d\ne8,9$ is generated by the classes of its $(-1)$-curves; for the
cubic surface these are the $27$ lines, so a class meeting every line class nonnegatively meets
every effective class nonnegatively.

Second, $D$ is effective. By Harbourne, Corollary II.3, preprint p. 3, a numerically effective
divisor meeting the anticanonical class nonnegatively lies in $\mathrm{Eff}$, and here
$-K_S\cdot D=D\cdot H>0$, while $D\cdot H\ge2$: the Hodge index inequality (Theorem V.1.9 of the
book, printed p. 364) gives $3D^2\le(D\cdot H)^2$ and $D^2>0$, so $(D\cdot H)^2\ge4$, and
$D\cdot H$ is a positive integer.

Third, the linear system is base point free and regular. Since
$-K_S\cdot D=D\cdot H\ge2$, Harbourne's Theorem III.1(a), preprint p. 7, gives
$h^1(X,\OO_X(D))=0$ and that the sections of $D$ are base point free, hence without fixed
components.

Fourth, a general member is reduced, irreducible and nonsingular. Since $D^2>0$ the linear system is
not composed with a pencil, and Harbourne's Lemma II.6(b), preprint p. 4, then says that $D^2>0$ and
that the general section of $D$ is reduced and irreducible. A general member of a base-point-free
linear system on a surface over an algebraically closed field of characteristic $0$ is nonsingular
by Bertini's theorem, II.8.18 of the book, printed p. 179, applied to the morphism defined by the
system as in the proof of (4.13)(b).
:::

:::

::: {.pf-step #equivalence-of-the-two-existence-conditions}
If a class contains an irreducible curve, then it is alternative (a), (b) or (c); and every class
of alternative (a) or (c) contains an irreducible nonsingular curve. The reverse implication for
alternative (b) is not proved here.

::: pf-proof
If $D$ contains an irreducible curve, then steps [](#negative-square-is-a-line){.pf-ref},
[](#zero-square-is-a-conic){.pf-ref} and
[](#positive-square-satisfies-the-third-condition){.pf-ref} place $D$ in one of the three
alternatives. Conversely, steps [](#lines-contain-nonsingular-curves){.pf-ref} and
[](#third-condition-contains-nonsingular-curve){.pf-ref} produce an irreducible nonsingular member
in every class of alternatives (a) and (c), and an irreducible nonsingular curve is an irreducible
curve. For alternative (b) the implication from existence to the conic description is step
[](#zero-square-is-a-conic){.pf-ref}, and the opposite implication, that every class of degree $2$
with $D^2=0$ contains an irreducible nonsingular conic, is not proved on this card: neither source
read for it treats that case, and no published argument for it was located.
:::

:::

::: {.pf-step #conclusion}
The alternatives (a) and (c) are equivalent to containing an irreducible curve and to containing an
irreducible nonsingular curve, and alternative (b) is necessary for containing an irreducible curve.

::: pf-proof
Step [](#equivalence-of-the-two-existence-conditions){.pf-ref} gives the classification of a class
that contains an irreducible curve, and the two existence claims for alternatives (a) and (c). What
the exercise's statement also asserts, and what is not established here, is that every class of
alternative (b) contains an irreducible nonsingular curve.
:::

:::

::: pf-qed
Steps [](#negative-square-is-a-line){.pf-ref}, [](#zero-square-is-a-conic){.pf-ref} and
[](#positive-square-satisfies-the-third-condition){.pf-ref} are the necessity, steps
[](#lines-contain-nonsingular-curves){.pf-ref} and
[](#third-condition-contains-nonsingular-curve){.pf-ref} are the sufficiency for alternatives (a)
and (c), and step [](#equivalence-of-the-two-existence-conditions){.pf-ref} records that the
sufficiency for alternative (b) is not proved here.
:::

:::
:::

::: {.remark title="Published solution"}
Brian Harbourne, *Anticanonical Rational Surfaces* (January 24, 1996,
arXiv:alg-geom/9509001v2), text version
`tmp/sources/harbourne-1995-anticanonical-rational-surfaces.md`: Corollary II.3, preprint p. 3,
Lemma II.6, preprint p. 4, Theorem III.1(a), preprint p. 7. The paper works over an algebraically
closed field of arbitrary characteristic, which is why the card's appeal to Bertini for the
nonsingularity of a general member is made separately, from the book. Its Lemma II.6 states the
Bertini-type alternative on which step [](#third-condition-contains-nonsingular-curve){.pf-ref}
rests: a fixed-component-free class whose system is not composed with a pencil has $F^2>0$ and
reduced irreducible general section.

I. V. Dolgachev, *Topics in Classical Algebraic Geometry* (September 27, 2010), text version
`tmp/sources/dolgachev-topics-classical-ag.md`: Lemma 8.1.3, printed p. 248, on irreducible curves of
negative self-intersection on a weak Del Pezzo surface, and Theorem 8.2.19, printed p. 265, on the
effective cone of a Del Pezzo surface, whose proof leaves the degrees $8$ and $9$ to the reader and
which the card uses at degree $3$.

The two sources settle the classification outside case (b) of the converse, and they do not state the
exercise. In particular the case they do not treat is the existence of an irreducible nonsingular
conic in a class of degree $2$ with $D^2=0$: Harbourne's Lemma II.6(a) would give a reduced
irreducible member of such a pencil once the class is known to be numerically effective, and the
nefness of the $27$ classes of degree $2$ with square $0$ is not in either source, so that case is
left open on this card.
:::
