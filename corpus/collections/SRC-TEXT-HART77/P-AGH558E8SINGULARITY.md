---
schema: qual/card@1
id: P-AGH558E8SINGULARITY
kind: problem
title: The $E_8$ surface singularity $x^2+y^3+z^5=0$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Blowups
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Hartshorne V.5.8 transcription and collection context,
    and checked the target exceptional configuration against the local ADE
    surface-singularity card D-SRFADE. The retained Hartshorne solution
    attachment stops in Chapter IV, so there is no retained V.5.8 source
    solution to import. The proof below is therefore an independent chart
    calculation. For part (a), it checks t=-(u^2+v^3), identifies A[z^-1]
    with a localization of k[u,v], and supplies the prime-element argument
    needed to descend unique factorization across z. For part (b), it
    follows the singular points through all eight ordinary point blowups.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Recomputed every blowup chart and the exceptional-curve incidence.
    After the first two blowups the unique remaining singular point is the
    intersection of the first two exceptional lines. The third blowup
    separates them and produces one ordinary double point and one point
    with local equation X^2+zY(Y+z)=0. One blowup resolves the ordinary
    double point; blowing up the second point produces three ordinary
    double points, each resolved by one further blowup. Thus the count is
    3+1+1+3=8. Tracking the strict transforms gives final edges
    E1-E4-E3-E7-E5-E6-E2 and E5-E8, the displayed E8 diagram.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.5,
    exercise 5.8, printed page 420. Checked part (a) as the card records it and
    part (b) step by step: the first three blowups x^2+y^3+z^5, then
    x_1^2+zy_1^3+z^3, then the two germs X^2+yZ+y^2Z^3 and X^2+zY(Y+z), the
    last of which has ordinary double points at Z = 0, Z = -1 and V = 0, and
    the incidence chain E_1-E_4-E_3-E_7-E_5-E_6-E_2 with E_8 meeting E_5, which
    is the E_8 diagram; the count of eight is consistent with the Milnor number
    (2-1)(3-1)(5-1) = 8. Searched outside the twelve retained sets and found a
    complete published computation of the eight blowups: Algebraic Geometry II,
    National Taiwan University, 2020 Spring, Chapter V homework, Exercise 8 of
    section 5 (solution by Yi-Heng), PDF p. 21
    (tmp/sources/ntu-ag2-chapter5.pdf), lists the strict transforms of the first,
    second and third blowups, the two charts of the third, the fourth blowup of
    both germs, the fifth and sixth, and ends "the inverse image of P is a union
    of eight projective lines corresponding to E8". Its four intermediate
    equations agree with the card's. Miles Reid, Chapters on Algebraic Surfaces
    (arXiv alg-geom/9602006), Chapter 4 section 4.2, printed p. 82, proves the
    D_4 case with the divisor computation in full and lists E_8: x^2+y^3+z^5=0
    with "the resolution is a bunch of -2-curves whose configuration is given by
    the corresponding Dynkin diagram", which states the result without the eight
    blowups. Not checked: whether the blowups the card writes are minimal, and
    Park's part (a), which the card already records as stopping there.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read again for issue #121, against the printed exercise (Hartshorne V.5.8,
    printed p. 420) and the two published sources on the card. Algebraic
    Geometry II, National Taiwan University, 2020 Spring, Exercise 8 of
    section 5 (Yi-Heng), PDF p. 21 of tmp/sources/ntu-ag2-chapter5.pdf, read in
    the extraction tmp/sources/ntu-ag2-chapter5.md: its (b) is a list of seven
    blowups in coordinates, with (iii) branching into two charts and (v) into
    three germs, then "(vi) ... non-singular", "(vii) this is similar to (vi)"
    and "(viii) ... non-singular", closing with "the inverse image of P is a
    union of eight projective lines corresponding to E8". Its four intermediate
    equations x1^2+zy1^3+z^3, x2^2+z2y1^2+y1z^3, x3^2+z3y1+y1^2z3^3 and
    x3^2+z2y3^2+y3z2^2 are the card's, and its first chart of the third blowup
    is the card's first germ. What it does not do: it asserts the
    non-singularity of the strict transforms rather than checking the charts,
    it leaves (vii) as "similar", and it states the E8 incidence without
    computing which exceptional curve meets which. The card's steps supply
    those. Miles Reid, Chapters on Algebraic Surfaces, Chapter 4, section 4.2,
    printed p. 82, works the D4 case in full and lists E8: x^2+y^3+z^5 with the
    Dynkin-diagram statement and no blowups. The remark's opening now says the
    source computes the blowups and states E8 without deriving it, instead of
    calling the computation complete.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Gave Park's citation its page on 2026-11-16: Exercise V.5.8 of Jinhyun
    Park's Solutions to Hartshorne's Algebraic Geometry is on PDF p. 31 of that
    set, which is where his part (a) stops, and the remark now says so; the text
    version tmp/sources/hartshorne-solutions-park.md being named there with it.
    Nothing else in the audit changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Read again for issue #121 against the printed exercise (Hartshorne V.5.8,
    printed p. 420, PDF p. 435 of tmp/sources/hartshorne-1977-algebraic-geometry.md)
    and against Egbert's set in the PDF's own text layer, PDF pp. 300--302 of
    tmp/sources/hartshorne-solutions-egbert.pdf, beside the text version
    tmp/sources/hartshorne-solutions-egbert.md. Two claims on the remark are
    corrected. First, Egbert's part (a) is given in full but for one sentence: at
    PDF p. 300 he writes "Proceed as in Algebra.NN.30, my algebra/geometry/analysis
    solutions, summerstudychallenge2.pdf" in place of a proof that k[x,y]/(x^2+y^3)
    is a domain, and that document is not in tmp/sources and was not read; the
    remark now says what he gives and what he defers. Second, the equation at his
    stopping point was named X^2+zY(Y+z)=0, which is not in his solution: his last
    strict transform is a^2+cY^2+Yc^3 in the charts a = 1 and b = 1, the card's
    x_2^2+y^2z_2+yz_2^3, he then writes the third blowup X_3 in the charts d = 1,
    e = 1 and f = 1, and stops at "so d = 0" and "etc, etc." on PDF p. 302. Reid's
    printed p. 82 was re-read at the PDF's own text layer and stands: the D_4
    resolution with the divisor computation giving Gamma_0^2 = -2, and the E_8
    list with the Dynkin-diagram sentence and no blowups. Not re-checked this
    pass: the NTU charts, already recorded in the 2026-11-16 event above, and
    whether the eight blowups are minimal. The events of 2026-11-11 and
    2026-11-16 above had been rewritten in place; both are restored to the text
    they were dated with, and this note is their correction.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Re-read for issue #121 against the printed exercise (Hartshorne V.5.8,
    printed p. 420) and transcribed part (b) from two solution sets that
    compute the blowups, which the earlier events above did not have. Yang
    Pi-Yeh, solution 5.5.8(b), printed pp. 114--115 of
    tmp/sources/lfwin-hartshorne-solutions.pdf, folios confirmed on the PDF's
    own text layer, read in tmp/sources/lfwin-hartshorne-solutions.md: seven
    blowups in coordinates with Jacobian checks for the first four, then "And
    one more blow-up to separate all exceptional curves. Hence this Du Val
    singularity is of the type E8". NTU, Exercise 8 of §5, items (i)--(viii),
    PDF p. 21, whose equations were already recorded above. Each part-(b) step
    now names the charts it uses in those two places. E. Brieskorn, Rationale
    Singularitäten komplexer Flächen, Invent. Math. 4 (1968), read in
    tmp/sources/brieskorn-1968-rationale-singularitaeten.md: Satz 2.10 and
    Satz 2.11, printed pp. 348--349, classify the resolution graphs of the
    two-dimensional quotient singularities by the platonic triples, and §3.2
    and Satz 3.3, printed pp. 354--355, identify the ring of invariants of the
    binary icosahedral group with C{x,y,z}/(x^2+y^3+z^5). The Brieskorn
    folios were read from rendered page images of the scan, which carries no
    text layer: PDF p. 15 is printed 349, p. 16 is 350, p. 20 is 354 and p. 21
    is 355. What the remark was corrected to say: the eight blowups are in
    Yang and in the NTU set, not only the NTU set, and neither derives the
    E_8 incidences, which are stated at the end of both entries; Brieskorn
    determines the graph through the classification and computes no blowup.
    Not checked: the two passages of Brieskorn's table that would name the
    (2,3,5) row entry by entry, whose MinerU extraction is garbled and whose
    page image was not read column by column, so the identification of that
    row with the eight-curve chain is the classification statement of 2.10 and
    not a quotation of the table; and whether the eight blowups are minimal,
    which no event above settled either.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The event above, of the same day, had been rewritten in place by
    ae2cc8895a and again by 16359d382b; it is restored here to the text it
    carried when 15c60853ca wrote it, and this event carries the corrections
    those two rewrites made together with the ones this pass makes.

    Yang Pi-Yeh, solution 5.5.8(b), printed pp. 114--115 of
    tmp/sources/lfwin-hartshorne-solutions.pdf (folios read on the PDF's own
    text layer; the solution begins on printed p. 114 and its fourth blowup is
    on that page), read in tmp/sources/lfwin-hartshorne-solutions.md: his
    first blowup in the three charts 1+xy_1^3+x^3z_1^5, x_1^2+y+y^3z_1^5 and
    x_1^2+zy_1^3+z^3, and his second in the three charts
    1+z_2y_2^3x_1^2+z_2^3x_1, x_2^2+y_1^2z_2+y_1z_2^3 and x_2^2+z+y_2^3z^2,
    are the card's charts of steps first-blowup-singular-locus and
    second-blowup-singular-locus, and both steps now cite him for them, the
    NTU items (i) and (ii) being cited for the one chart each of them records.
    His third blowup has the chart y_3=1 as x_3^2+z_2^2z_3+z_2z_3^2, which is
    the card's germ X^2+zY(Y+z); his chart z_3=1 is printed as
    z_2^3+y_1y_3^2+y_1z_2, whose quadratic part y_1z_2 has rank two, where
    the strict transform in that chart is x_3^2+y_1y_3+y_1^2y_3^3, of
    quadratic rank three, so that printed equation is not the strict
    transform, and the card names it as an erratum in the step and does not
    follow it. His fourth blowup is taken at that germ, its chart y_4=1 reads
    z_2^3+x_4y_3(y_3^2+z_2), of multiplicity three at the origin where his
    entry calls it nonsingular; his fifth blowup keeps only the point at -1
    and calls (0,0,0) impossible, so the three double points on E_5 are not
    his; and his seventh blows up a point coming from his own sixth chart. No
    step of the card transcribes a chart of the fourth blowup or later.

    E. Brieskorn, Rationale Singularitäten komplexer Flächen, Invent. Math. 4
    (1968), read in tmp/sources/brieskorn-1968-rationale-singularitaeten.md, a
    scan with no text layer whose folios were read from rendered page images:
    Satz 2.10 with its proof and the statement of Satz 2.11 are on printed
    p. 347, not pp. 348--349; the paper works over C; and §3.2 identifies the
    invariant ring of the binary icosahedral group with C{x,y,z}/(x^2+y^3+z^5),
    the analytic local ring, which is neither the completion C[[x,y,z]]/(f)
    nor the affine ring A of the exercise. It computes no blowup and settles
    nothing for an arbitrary algebraically closed field, so it is not cited on
    the card.

    Also corrected: the remark's opening said that part (b) is computed in two
    solution sets, which the entries do not support --- the first two blows
    are computed chart by chart in both, the third in full only in the NTU
    set, and the fourth to the eighth only there. The paragraph that listed
    which of the card's steps are its own is removed from the remark, which
    now carries citations and mathematics only; the steps carry the marking,
    and the parts no source read proves are these four: the resolution of an
    ordinary double point by a single blowup with the conic as exceptional
    curve, the chart checks of blows (vi)--(viii), the positions of the three
    double points on E_5, and the derivation of the eight-curve incidence,
    which the NTU set states and does not derive. Those four were on the card
    before this batch and are kept, not rewritten. Not checked: whether the
    eight blowups are minimal, and Brieskorn's table of Satz 2.11 row by row.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repaired on a reader's third report of this date, which is right on both
    points. The paragraph that stood in step third-blowup-two-points and
    identified Yang's chart y_3=1 with the card's germ X^2+zY(Y+z), and then
    named his printed chart z_3=1 as not being the strict transform, is source
    reading in a rendered proof and is removed from the card. Read there, in
    tmp/sources/lfwin-hartshorne-solutions.md, solution 5.5.8(b), printed
    pp. 114--115 of tmp/sources/lfwin-hartshorne-solutions.pdf: the chart
    y_3=1 of his third blowup reads x_3^2+z_2^2z_3+z_2z_3^2, which is the
    card's germ; his chart z_3=1 reads z_2^3+y_1y_3^2+y_1z_2, whose quadratic
    part y_1z_2 has rank two, where the strict transform there is
    x_3^2+y_1y_3+y_1^2y_3^3, of quadratic rank three, so that printed
    equation is not the strict transform. The card uses none of his charts of
    that blowup: the two germs of step third-blowup-two-points are the NTU
    set's items (iii), which the step now names as that set's rather than as
    "the same set" after the Yang paragraph that was removed.

    Not checked: nothing new in this pass; the charts were not recomputed.
    The fourth and later blows of Yang's entry are recorded in the event above
    of this date, which is where the reading of them belongs.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Part (b) read for issue #168 and recomputed with a sympy script that carries
    out the eight point blowups in the card's own order, starting from
    x^2+y^3+z^5, in all three charts of every step, forming each strict
    transform by substitution and division by the exceptional coordinate. Every
    strict transform displayed in steps first-blowup-singular-locus,
    second-blowup-singular-locus, third-blowup-two-points,
    resolve-ordinary-double-point-e1e3, e5-three-double-points,
    resolve-remaining-three-points and eight-blowups-e8-diagram was reproduced
    and agrees. The script also gives: after the first blowup the only singular
    point lies on E_1; after the second it is E_1 cap E_2; after the third there
    are exactly two, at E_1 cap E_3 and at E_2 cap E_3; the fourth removes the
    first and leaves none on E_4; the fifth leaves exactly three points on E_5,
    one at E_3 cap E_5, one at E_2 cap E_5 and one free point, which is what
    step e5-three-double-points asserts; and the sixth, seventh and eighth leave
    no singular point on the exceptional line. The multiplicity of every
    exceptional divisor in its total transform is 2, so every E_i^2 = -2, and
    the curves through each centre, a blowup at an intersection separating the
    two curves through it, give exactly the edges E_1E_4, E_3E_4, E_3E_7,
    E_5E_7, E_5E_6, E_2E_6 and E_5E_8, that is the seven-curve chain
    E_1-E_4-E_3-E_7-E_5-E_6-E_2 with E_8 attached to the fifth of them, which is
    the E_8 diagram. The same computation over GF(2), GF(3) and GF(5) reproduces
    the strict transforms, one singular point after each of the first three
    blowups and none after the fourth, so nothing in part (b) degenerates at 2,
    3 or 5. Not checked: whether the eight blowups are minimal, which no event
    above settled either; and Brieskorn's Satz 2.11 row by row, which this card
    does not cite.
---

::: {.problem}
Let $k$ be an algebraically closed field, and let $X$ be the surface in $\AA_k^3$ defined by the equation $x^2+y^3+z^5=0$.
It has an isolated singularity at the origin $P=(0,0,0)$.

(a) Show that the affine ring $A=k[x, y, z] /\left(x^2+y^3+z^5\right)$ of $X$ is a unique factorization domain, as follows.
Let $t=z^{-1}$; $u=t^3 x$, and $v=t^2 y$.
Show that $z$ is irreducible in $A$; $t \in k[u, v]$, and $A\left[z^{-1}\right]=k\left[u, v, t^{-1}\right]$.
Conclude that $A$ is a UFD.

(b) Show that the singularity at $P$ can be resolved by eight successive blowings-up.
If $\tilde{X}$ is the resulting nonsingular surface, then the inverse image of $P$ is a union of eight projective lines, which intersect each other according to the Dynkin diagram $\mathbf{E}_8$:

\begin{tikzcd}
	\circ & \circ & \circ & \circ & \circ & \circ & \circ \\
	&&&& \circ
	\arrow[dash, from=1-1, to=1-2]
	\arrow[dash, from=1-2, to=1-3]
	\arrow[dash, from=1-3, to=1-4]
	\arrow[dash, from=1-4, to=1-5]
	\arrow[dash, from=1-5, to=1-6]
	\arrow[dash, from=1-6, to=1-7]
	\arrow[dash, from=1-5, to=2-5]
\end{tikzcd}
:::

::: {.solution}
::: pf

::: {.pf-step #z-is-prime}
Part (a): $A$ is a noetherian domain, and $z$ is a prime element of
$A$.

::: pf-proof
Put
$$
F=x^2+y^3+z^5.
$$
Regard $F$ as a polynomial in $x$ over
$$
K=k(y,z).
$$
If $F$ were reducible over $K$, then, since it has degree $2$ in $x$, it
would have a root in $K$. Thus
$$
-(y^3+z^5)
$$
would be a square in $K$.

The polynomial
$$
y^3+z^5\in k[y,z]
$$
is squarefree in every characteristic. Indeed, a repeated irreducible
factor would divide both partial derivatives whenever both are nonzero. In
characteristic $3$ the $z$-derivative is $5z^4\neq0$, and in
characteristic $5$ the $y$-derivative is $3y^2\neq0$; in all other
characteristics the two derivatives have no common nonconstant divisor
with $y^3+z^5$. Hence some irreducible factor of $y^3+z^5$ occurs with
valuation $1$, whereas every square in $K$ has even valuation at every
irreducible polynomial. Therefore $-(y^3+z^5)$ is not a square in $K$.

So $F$ is irreducible over $K$. By Gauss's lemma it is irreducible in the
UFD $k[x,y,z]$, hence prime there. Consequently
$$
A=k[x,y,z]/(F)
$$
is a domain. It is noetherian because it is a finitely generated
$k$-algebra.

Moreover,
$$
A/(z)\cong k[x,y]/(x^2+y^3).
$$
The polynomial $x^2+y^3$ is irreducible in $k[x,y]$: over $k(y)$ a
factorization would give a root, hence would make $-y^3$ a square, which
is impossible because its $y$-adic valuation is $3$. Thus $A/(z)$ is a
domain, so $(z)$ is prime in $A$. In particular $z$ is irreducible.
:::

:::

::: {.pf-step #coordinate-change-ufd}
Part (a): with
$$
t=z^{-1},
\qquad
u=t^3x,
\qquad
v=t^2y,
$$
one has
$$
\boxed{t=-(u^2+v^3)}
$$
and
$$
\boxed{A[z^{-1}]=k[u,v,t^{-1}].}
$$

::: pf-proof
In $A[z^{-1}]$ the defining equation gives
$$
u^2+v^3
=
t^6(x^2+y^3)
=
-t^6z^5
=
-t.
$$
Hence
$$
t=-(u^2+v^3)\in k[u,v].
$$

Certainly
$$
u,\ v,\ t^{-1}=z
$$
belong to $A[z^{-1}]$, so
$$
k[u,v,t^{-1}]\subseteq A[z^{-1}].
$$
Conversely,
$$
z=t^{-1},
\qquad
x=t^{-3}u=(t^{-1})^3u,
\qquad
y=t^{-2}v=(t^{-1})^2v,
$$
and $t\in k[u,v]$ by the preceding calculation. Thus every generator of
$A[z^{-1}]$ belongs to $k[u,v,t^{-1}]$, proving equality.

Equivalently,
$$
A[z^{-1}]
\cong
k[u,v,(u^2+v^3)^{-1}],
$$
via
$$
t=-(u^2+v^3).
$$
Indeed, starting with independent variables $U,V$ and putting
$$
T=-(U^2+V^3),
\qquad
z=T^{-1},
\qquad
x=T^{-3}U,
\qquad
y=T^{-2}V,
$$
gives
$$
x^2+y^3+z^5
=
T^{-6}(U^2+V^3+T)
=0.
$$
This defines an inverse to the map sending $U,V$ to $u,v$, so the
displayed isomorphism is genuine and in particular $u,v$ are
algebraically independent.
This is a localization of the polynomial UFD $k[u,v]$, hence is a UFD.
:::

:::

::: {.pf-step #a-is-ufd}
Part (a): $A$ is a unique factorization domain.

::: pf-proof
We use the prime element $z$ from step [](#z-is-prime){.pf-ref} and the UFD
$$
A[z^{-1}]
$$
from step [](#coordinate-change-ufd){.pf-ref}.

Because $A$ is noetherian, every nonzero nonunit of $A$ factors into
irreducibles. It remains to prove that every irreducible of $A$ is prime.
Let $p\in A$ be irreducible.

If $p$ is associate to $z$, then $p$ is prime because $z$ is prime.
Assume therefore that $p$ is not associate to $z$.

First, $p$ remains irreducible in $A[z^{-1}]$. Suppose
$$
p=\frac{a}{z^m}\frac{b}{z^n}
$$
in $A[z^{-1}]$. Since $A$ is a domain,
$$
z^{m+n}p=ab.
$$
As long as a factor $z$ remains on the left, primality of $z$ implies
that $z$ divides $a$ or $b$; cancel such a factor. After $m+n$
cancellations we obtain
$$
p=a'b'
$$
with $a',b'\in A$. Irreducibility of $p$ makes one of $a',b'$ a unit in
$A$. The corresponding factor $a/z^m$ or $b/z^n$ is therefore a unit in
$A[z^{-1}]$. Hence $p$ is irreducible in $A[z^{-1}]$.

Since $A[z^{-1}]$ is a UFD, $p$ is prime there. Now suppose
$$
p\mid ab
$$
in $A$. In $A[z^{-1}]$, primality gives
$$
p\mid a
\qquad\text{or}\qquad
p\mid b.
$$
Assume the first. Then for some $c\in A$ and $n\geq0$,
$$
z^na=pc.
$$
If $n>0$, the left side is divisible by $z$. Since $z$ is prime and
$z\nmid p$ (otherwise irreducibility of $p$ would make $p$ associate to
$z$), one has $z\mid c$. Cancel one factor of $z$ and repeat. After $n$
steps,
$$
a=pc'
$$
for some $c'\in A$. Thus $p\mid a$ already in $A$. The same argument
applies if $p\mid b$ in the localization.

Therefore every irreducible of $A$ is prime. Since $A$ is atomic, $A$ is
a UFD.
:::

:::

::: {.pf-step #first-blowup-singular-locus}
Part (b): after the first blowup, the only singular point of the
strict transform lies on one exceptional line $E_1$.

::: pf-proof
Blow up the origin of
$$
X:\quad x^2+y^3+z^5=0.
$$
The origin is the only singular point of $X$. In characteristics different
from $2,3,5$ this follows immediately from the three partial derivatives.
In characteristic $2$, the $y$- and $z$-derivatives force $y=z=0$, and
then the equation forces $x=0$; in characteristic $3$, the $x$- and
$z$-derivatives force $x=z=0$ and then $y=0$; in characteristic $5$, the
$x$- and $y$-derivatives force $x=y=0$ and then $z=0$.

In the $x$-chart, with
$$
y=xy_1,
\qquad
z=xz_1,
$$
the strict transform is
$$
1+xy_1^3+x^3z_1^5=0,
$$
so it does not meet the exceptional divisor.

In the $y$-chart, with
$$
x=yx_1,
\qquad
z=yz_1,
$$
the strict transform is
$$
x_1^2+y+y^3z_1^5=0.
$$
Along the exceptional divisor $y=0$ its derivative with respect to $y$
is $1$, so this chart is nonsingular along the exceptional locus.

In the $z$-chart, with
$$
x=zx_1,
\qquad
y=zy_1,
$$
the strict transform is
$$
X_1:\quad x_1^2+zy_1^3+z^3=0.
$$
Its reduced exceptional curve is
$$
E_1:\quad z=x_1=0,
$$
in this affine chart; together with its piece in the $y$-chart it is the
projective line $E_1\cong\PP^1$. Along $E_1$, the derivative with respect to $z$ is
$y_1^3$, so the only singular point on $E_1$ is
$$
x_1=y_1=z=0.
$$
Away from the exceptional divisor the blowup is an isomorphism, so this
is the only singular point of the first strict transform.

The three charts are those of Yang Pi-Yeh, *Hartshorne Solutions*, solution
5.5.8(b), printed p. 114, who writes $1+xy_1^3+x^3z_1^5$,
$x_1^2+y+y^3z_1^5$ and $x_1^2+zy_1^3+z^3$ and checks the first two by their
Jacobians, and the third is item (i) of Exercise 8 of §5 of the NTU *Chapter
V Surfaces* homework, Algebraic Geometry II, National Taiwan University, 2020
Spring, solution by Yi-Heng, PDF p. 21, which reaches
$x_1^2+zy_1^3+z^3$ in the chart $z_1=1$.
:::

:::

::: {.pf-step #second-blowup-singular-locus}
After the second blowup, the reduced exceptional locus is
$$
E_1\cup E_2,
$$
and its unique singular point is $E_1\cap E_2$.

::: pf-proof
Rename the coordinates in the singular chart of step [](#first-blowup-singular-locus){.pf-ref} as
$$
x,y,z,
$$
so the equation is
$$
x^2+zy^3+z^3=0.
$$
Blow up its origin.

The $x$-chart again misses the exceptional locus of the strict transform.
In the $z$-chart the strict transform is
$$
x_2^2+z+z^2y_2^3=0,
$$
which is nonsingular along $z=0$ because the $z$-derivative is $1$ there.

In the $y$-chart, with
$$
x=yx_2,
\qquad
z=yz_2,
$$
the strict transform is
$$
X_2:\quad x_2^2+y^2z_2+yz_2^3=0.
$$
The new reduced exceptional curve is
$$
E_2:\quad y=x_2=0,
$$
in this affine chart; globally it is a projective line
$E_2\cong\PP^1$.
and the strict transform of $E_1$ is
$$
E_1:\quad z_2=x_2=0.
$$
They meet at the origin. Along $E_2$, the derivative of the equation
with respect to $y$ is $z_2^3$ at $y=0$, so the only singular point there
is $z_2=0$. Thus the unique remaining singular point is precisely
$$
E_1\cap E_2.
$$

The chart $y_2=1$ with $x_2^2+z_2y_1^2+y_1z^3$ is item (ii) of the NTU set,
PDF p. 21. The other two charts are Yang Pi-Yeh's, solution 5.5.8(b), printed
p. 114: the piece $z_2=1$ reads $x_2^2+z+y_2^3z^2$, which is $x_2^2+z+z^2y_2^3$
above, and the piece $x_2=1$ reads $1+z_2y_2^3x_1^2+z_2^3x_1$, which is the
$x$-chart above and does not meet the exceptional curve.
:::

:::

::: {.pf-step #third-blowup-two-points}
The third blowup separates $E_1$ and $E_2$, introduces a projective
line $E_3$, and leaves exactly two singular points: an ordinary double
point at $E_1\cap E_3$ and a point with local equation
$X^2+zY(Y+z)=0$ at $E_2\cap E_3$.

::: pf-proof
Rename the coordinates in step [](#second-blowup-singular-locus){.pf-ref} as $x,y,z$, so
$$
X_2:\quad x^2+y^2z+yz^3=0.
$$
Blow up the origin.

In the $y$-chart,
$$
x=yX,
\qquad
z=yZ,
$$
and the strict transform is
$$
X^2+yZ+y^2Z^3=0.
$$
The only singular point on the exceptional curve $y=X=0$ is the origin.
Its quadratic tangent cone is
$$
X^2+yZ=0,
$$
which is a nonsingular conic in $\PP^2$. Hence this is an ordinary double
point. This point is the intersection of the strict transform of $E_1$
with the new exceptional line $E_3$.

In the $z$-chart,
$$
x=zX,
\qquad
y=zY,
$$
and the strict transform is
$$
X^2+zY^2+z^2Y
=
X^2+zY(Y+z)
=0.
$$
Again the only singular point on the exceptional curve $z=X=0$ is the
origin, with exact local equation
$$
X^2+zY(Y+z)=0.
$$
It is the intersection of the strict transform of $E_2$ with $E_3$.

Thus after the third blowup the incidence graph of the old exceptional
curves is
$$
E_1-E_3-E_2,
$$
with the two displayed intersection points still singular.

The two germs are items (iii) of Exercise 8 of §5 of the NTU *Chapter V
Surfaces* homework, PDF p. 21,
$x_3^2+z_3y_1+y_1^2z_3^3$ and $x_3^2+z_2y_3^2+y_3z_2^2$; that the second of
them is $X^2+zY(Y+z)$ and the first is $X^2+yZ+y^2Z^3$, and that their
exceptional curves are the strict transforms of $E_1$ and $E_2$ meeting
$E_3$, is this card's own reading of those charts.
:::

:::

::: {.pf-step #resolve-ordinary-double-point-e1e3}
Blowing up the ordinary double point $E_1\cap E_3$ once resolves
that point and inserts a projective line $E_4$ between $E_1$ and $E_3$.

::: pf-proof
At this point the local equation has quadratic tangent cone
$$
X^2+yZ=0,
$$
a nonsingular conic in $\PP^2$. The blowup of an ordinary double point
with nonsingular projectivized tangent cone is nonsingular, and its
exceptional curve is exactly that conic. Hence the fourth blowup resolves
this singularity and introduces
$$
E_4\cong\PP^1.
$$

The strict transforms of $E_1$ and $E_3$ meet the conic in the two
distinct tangent directions
$$
[0:1:0]
\qquad\text{and}\qquad
[0:0:1].
$$
Thus this blowup replaces the edge $E_1-E_3$ by
$$
E_1-E_4-E_3.
$$

This step is the card's own. Item (iv) of the NTU set, PDF p. 21, records
the strict transform as nonsingular and gives no chart of it.
:::

:::

::: {.pf-step #e5-three-double-points}
Blowing up the point $E_2\cap E_3$ with local equation
$X^2+zY(Y+z)=0$ introduces a projective line $E_5$ carrying exactly
three ordinary double points.

::: pf-proof
Use the exact local equation from step [](#third-blowup-two-points){.pf-ref}:
$$
X^2+zY(Y+z)=0.
$$
Blow up its origin.

In the $Y$-chart, with
$$
X=YU,
\qquad
z=YZ,
$$
the strict transform is
$$
U^2+YZ(1+Z)=0.
$$
Along the exceptional line $Y=U=0$, singular points occur exactly when
$$
Z(1+Z)=0,
$$
namely at
$$
Z=0
\qquad\text{and}\qquad
Z=-1.
$$

In the $z$-chart, with
$$
X=zU,
\qquad
Y=zV,
$$
the strict transform is
$$
U^2+zV(1+V)=0.
$$
Along the exceptional line $z=U=0$, singular points occur at
$$
V=0
\qquad\text{and}\qquad
V=-1.
$$
The points $Z=-1$ and $V=-1$ are the same point on the overlap. Hence
there are exactly three singular points on the new exceptional line
$$
E_5\cong\PP^1.
$$

Near each of them the factor multiplying the transverse coordinate is a
unit times a local parameter, so the quadratic tangent cone is
$$
U^2+ab=0.
$$
Thus all three are ordinary double points.

The point $Z=0$ is where the strict transform of $E_3$ meets $E_5$, the
point $V=0$ is where the strict transform of $E_2$ meets $E_5$, and the
third point is a free point of $E_5$.

Item (v) of the NTU set, PDF p. 21, lists the three singular points of
the strict transform. Which exceptional curve each of them lies on, and so
the incidences $E_3-E_5$ and $E_2-E_5$ below, is this card's own reading of
the charts.
:::

:::

::: {.pf-step #resolve-remaining-three-points}
Three further blowups resolve the three ordinary double points on
$E_5$ and produce projective lines $E_6,E_7,E_8$.

::: pf-proof
Blow up the ordinary double point
$$
E_2\cap E_5.
$$
As in step [](#resolve-ordinary-double-point-e1e3){.pf-ref}, this resolves that point and inserts a smooth conic
$$
E_6\cong\PP^1
$$
between $E_2$ and $E_5$.

Next blow up
$$
E_3\cap E_5.
$$
This inserts
$$
E_7\cong\PP^1
$$
between $E_3$ and $E_5$.

Finally blow up the third ordinary double point, which lies only on
$E_5$. This introduces
$$
E_8\cong\PP^1
$$
meeting $E_5$ once.

Each ordinary double point is resolved by its single blowup, and the
three points are distinct. Therefore after these three blowups the strict
transform is nonsingular.

These are items (vi)--(viii) of the NTU set, PDF p. 21, item (vii) being
recorded there as "similar to (vi)". The chart checks of the three blows,
and the resolution of each ordinary double point by a single blowup, are
this card's own.
:::

:::

::: {.pf-step #eight-blowups-e8-diagram}
The resolution uses exactly eight successive point blowups, and
the reduced inverse image of $P$ has dual graph $\mathbf E_8$.

::: pf-proof
The number of blowups is
$$
3+1+1+3=8:
$$
three blowups reach the two remaining singular points, one resolves the
ordinary double point, one blows up the point with equation
$X^2+zY(Y+z)=0$, and three resolve the resulting ordinary double points.

Tracking incidences through the blowups gives precisely the edges
$$
E_1-E_4-E_3-E_7-E_5-E_6-E_2
$$
and the additional edge
$$
E_5-E_8.
$$
Thus the seven curves
$$
E_1,E_4,E_3,E_7,E_5,E_6,E_2
$$
form a chain, and $E_8$ meets the fifth curve $E_5$ in that chain. There
are no other intersections. Hence the reduced inverse image of $P$ is a
union of eight projective lines with incidence diagram
$$
\begin{tikzcd}
\circ & \circ & \circ & \circ & \circ & \circ & \circ \\
&&&& \circ
\arrow[dash, from=1-1, to=1-2]
\arrow[dash, from=1-2, to=1-3]
\arrow[dash, from=1-3, to=1-4]
\arrow[dash, from=1-4, to=1-5]
\arrow[dash, from=1-5, to=1-6]
\arrow[dash, from=1-6, to=1-7]
\arrow[dash, from=1-5, to=2-5]
\end{tikzcd}
$$
which is the Dynkin diagram $\mathbf E_8$.

The count of eight is the count of the blows above. The derivation of
the edges $E_1-E_4-E_3-E_7-E_5-E_6-E_2$ and $E_5-E_8$ from those charts,
and so the identification of the diagram with $\mathbf E_8$, is this card's
own: item (viii) of the NTU set, PDF p. 21, states the configuration and
does not derive it.
:::

:::

::: pf-qed
Steps [](#z-is-prime){.pf-ref}, [](#coordinate-change-ufd){.pf-ref} and [](#a-is-ufd){.pf-ref} prove part (a). Steps [](#first-blowup-singular-locus){.pf-ref}, [](#second-blowup-singular-locus){.pf-ref}, [](#third-blowup-two-points){.pf-ref}, [](#resolve-ordinary-double-point-e1e3){.pf-ref}, [](#e5-three-double-points){.pf-ref}, [](#resolve-remaining-three-points){.pf-ref} and [](#eight-blowups-e8-diagram){.pf-ref} give the eight
successive blowups, prove smoothness after the eighth, and identify the
exceptional incidence graph required in part (b).
:::

:::
:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.5, exercise 5.8, printed p. 420.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.5.8, gives part (a): he takes $z$ irreducible because $A/(z)=k[x,y]/(x^2+y^3)$ is an integral domain, which is true since the cusp is parametrized by $u\mapsto(u^3,-u^2)$ and $k[x,y]/(x^2+y^3)\cong k[u^2,u^3]$, and then $t=-(u^2+v^3)\in k[u,v]$ from $u^2+v^3=t^6(x^2+y^3)=-t$, $A[z^{-1}]=k[u,v,t^{-1}]$, and $A$ a UFD because the localization is one and an irreducible of $A$ outside $(z)$ stays irreducible and hence prime there. Steps [](#z-is-prime){.pf-ref}, [](#coordinate-change-ufd){.pf-ref} and [](#a-is-ufd){.pf-ref} prove the same three statements. For part (b) his computation runs three blowups, its last strict transform being $a^2+cY^2+Yc^3$, which is the card's $x_2^2+y^2z_2+yz_2^3$ of step [](#second-blowup-singular-locus){.pf-ref}. Jinhyun Park, *Solutions to Hartshorne's Algebraic Geometry*, Exercise V.5.8, gives part (a).
:::

::: {.remark title="Published solution"}
The first two blowups of part (b) are computed chart by chart in two solution sets, the third in full in one of them and in one chart of the other, and the fourth to the eighth in one.

Exercise 8 of §5 of the NTU *Chapter V Surfaces* homework, Algebraic Geometry II, National Taiwan University, 2020 Spring, solution by Yi-Heng, PDF p. 21, records the strict transforms chart by chart: (i) $x^2+y^3+z^5$ becomes $x_1^2+zy_1^3+z^3$ in the chart $z_1=1$; (ii) that becomes $x_2^2+z_2y_1^2+y_1z^3$ in the chart $y_2=1$; (iii) that becomes $x_3^2+z_3y_1+y_1^2z_3^3$ in the chart $y_3=1$ and $x_3^2+z_2y_3^2+y_3z_2^2$ in the chart $z_3=1$; (iv) the first is resolved by one further blowup; (v) the second acquires the three germs $x_4^2+z_4y_3+y_3z_4^2$, $x_4^2+z_2y_4^2+y_4z_2$ and $x_4^2+z_4y_3+y_3z_4^2$ at $z_4=-1$; (vi)--(viii) resolve those, and it closes "the inverse image of $P$ is a union of eight projective lines corresponding to $E_8$". Its equations are the ones used above.

Yang Pi-Yeh, *Hartshorne Solutions*, solution 5.5.8(b), printed pp. 114--115, gives the three charts of the first blowup, $1+xy_1^3+x^3z_1^5$, $x_1^2+y+y^3z_1^5$ and $x_1^2+zy_1^3+z^3$, with Jacobian checks for the first two, and the second blowup in its three charts. The chart $y_3=1$ of his third blowup, $x_3^2+z_2^2z_3+z_2z_3^2$, is the germ $X^2+zY(Y+z)$ of step [](#third-blowup-two-points){.pf-ref}.

Miles Reid, *Chapters on Algebraic Surfaces* (arXiv alg-geom/9602006), Chapter 4, §4.2, carries out the $D_4$ resolution in full, including the divisor computation $2\Gamma_0^2+4=0$ that gives $\Gamma_0^2=-2$, and lists the equations $A_n:x^2+y^2+z^{n+1}$, $D_n:x^2+y^2z+z^{n-1}$, $E_6:x^2+y^3+z^4$, $E_7:x^2+y^3+yz^3$ and $E_8:x^2+y^3+z^5$, with "the resolution is a bunch of $-2$-curves whose configuration is given by the corresponding Dynkin diagram".
:::
