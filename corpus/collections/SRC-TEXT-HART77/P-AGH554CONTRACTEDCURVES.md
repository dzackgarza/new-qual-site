---
schema: qual/card@1
id: P-AGH554CONTRACTEDCURVES
kind: problem
title: Curves contracted by a birational morphism and negative definiteness of the intersection matrix
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Birational Geometry
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.5.4 as transcribed here, the retained Andrew Egbert
    companion argument, the Hodge index theorem, the point-blowup
    intersection formulas, and the surface factorization theorem. The
    retained note has the intended Hodge-index idea but says that the
    pullback of an ample divisor is ample; for a contraction this is false,
    since its pullback has intersection zero with every exceptional curve.
    What is needed is that f^*H has positive square, so the signature form
    of Hodge index makes its orthogonal complement negative definite. The
    proof below also supplies the missing independence of exceptional curve
    classes by factoring f into point blowups; the same factorization shows
    every irreducible contracted curve is a strict transform of an
    exceptional P^1.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read both parts against the factorization theorem and the signature
    form of Hodge index. Checked that each contracted prime is the final
    strict transform of a unique exceptional P^1, that the exceptional prime
    classes are triangular with diagonal 1 in the independent total-transform
    basis, and hence that every fibre-component subset is numerically
    independent. Also checked that D=f^*H has D^2=H^2>0 and D.Y_i=0 without
    being ample, so D-perp is negative definite. Therefore Y^2<0 in part (a)
    and a^T(Y_i.Y_j)a=(sum a_iY_i)^2<0 for every nonzero vector in part (b).
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Published proof located for this exercise (issue #121). M. Reid, Chapters on
    Algebraic Surfaces, arXiv:alg-geom/9602006v1 (6 February 1996), a draft of
    the notes submitted to the 1993 volume of the IAS/AMS Park City lecture notes
    series (so the draft's "Status of this draft", printed p. 2, text version `tmp/sources/reid-chapters-algebraic-surfaces.md`, and the arXiv
    record's comment field), Appendix A.7 "Contracted divisors are negative",
    Theorem (Negativity of exceptional locus), with its statement on printed
    p. 29 and its proof on printed pp. 30--31, is part (b) verbatim and in
    greater generality: for a bunch of curves on a nonsingular surface contracted
    to points by a projective birational morphism f : Y -> X to any surface, the
    matrix (Gamma_i Gamma_j) is negative definite.
    Read in tmp/sources/reid-chapters-algebraic-surfaces.md, the MinerU extraction of the whole
    paper, which marks blocks of twenty PDF pages; that paper's folios agree with
    its PDF pages, and the theorem was checked on pp. 29--31 of
    tmp/sources/reid-chapters-algebraic-surfaces.pdf, whose pdftotext render
    fixes which page carries what. With k = 1 it gives Y^2 < 0, the
    negative-self-intersection half of part (a), and because a principal
    submatrix of a negative definite matrix is negative definite it gives the
    same for one curve among several components of a larger contracted fibre.
    What it does not give is
    Y = P^1 for a curve inside a larger exceptional locus: Reid's statement of
    that is Castelnuovo's criterion, printed p. 10, an equivalence for a single
    contracted curve with the morphism an isomorphism outside it, and his route
    from Y^2 < 0 to Y^2 = -1 at a nonsingular image point is the Contraction
    Theorem (Artin), which is the theorem of his Section 4.15, stated on printed
    p. 93, Section 4.16 being its proof, together with his Theorem (Artin) of
    Section 4.17, whose section and statement begin on printed p. 94 and whose
    proof of part (1) is on printed p. 95, where it ends "so mult(P in X) = -Z^2
    follows" with no Q.E.D., and the proof of part (2) runs on printed pp. 96--97.
    So part (b) now has a published proof and part (a) one published half; the
    other half is the card's step contracted-curve-is-p1, as the body now says.
    Reid's proof is stated "for simplicity" under the connected-union,
    single-point, isomorphism-outside hypothesis (printed p. 30), and the card's
    Hodge-index proof is the alternative he names in Ex. A.16, printed p. 36.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Citation corrected on a reader's report, and re-checked in the replaced text
    version (tmp/sources/reid-chapters-algebraic-surfaces.md, the whole paper, with its folios
    checked against tmp/sources/reid-chapters-algebraic-surfaces.pdf). Reid is
    cited here as arXiv:alg-geom/9602006v1, a draft of the notes submitted to the
    1993 volume of the IAS/AMS Park City lecture notes series, and not as the MSJ
    Memoirs volume: the draft says so in "Status of this draft" on printed p. 2,
    and the arXiv record's comment field says "To appear in 1993 volume of the
    IAS/AMS Park City lecture notes series". Theorem A.7's statement is on printed
    p. 29 and its proof on printed pp. 30--31, not "p. 29 with proof pp. 29--31";
    the Contraction Theorem (Artin) is stated on printed p. 93, not pp. 92--94,
    and it is Section 4.15's theorem, Section 4.16 being its proof, while
    Section 4.17 and its Theorem (Artin) begin on printed p. 94 and the proof of
    part (1) is on printed p. 95, part (2)'s proof running on pp. 96--97, so the
    entry's pp. 94--95 for Theorem 4.17 covered its statement and the proof of
    part (1); Ex. A.16 is on printed p. 36. Section A.7's statement of the theorem is for a bunch of curves, and
    part (a) for a curve among several components of a fibre follows from it by
    restricting to the one-by-one principal submatrix, which the two step remarks
    and the published-solution remark now say.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Page correction, on a reader's report of issue #121: the event above said
    Reid's Theorem 4.17 begins on printed p. 95. Read again in
    tmp/sources/reid-chapters-algebraic-surfaces.md and located on the printed folios of
    tmp/sources/reid-chapters-algebraic-surfaces.pdf with pdftotext as a page
    locator: printed p. 93 carries the Contraction Theorem (Artin), which is the theorem of
    Section 4.15 and not of 4.16 (4.16 is headed "Proof of Theorem"), Section
    4.17 and its Theorem (Artin) begin on printed p. 94, the proof of Theorem
    4.17 (1) lies wholly on printed p. 95, where it ends "so mult(P in X) = -Z^2
    follows" with no Q.E.D., and the proof of part (2) runs on printed pp. 96--97.
    Corrected here and in the remark.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Section number and pages, on a reader's report of issue #121. The Contraction
    Theorem (Artin) is the theorem of Reid's Section 4.15, whose statement stands
    on printed p. 93; Section 4.16 is headed "Proof of Theorem" and is its proof.
    The events above called it 4.16 and attached a "Theorem (Artin)" to Section
    4.17 where the theorem proved is 4.17 itself. Theorem 4.17's statement is on
    printed p. 94, the proof of part (1) lies wholly on printed p. 95 and ends
    "so mult(P in X) = -Z^2 follows" with no Q.E.D., and the proof of part (2)
    runs on printed pp. 96--97. Read in
    tmp/sources/reid-chapters-algebraic-surfaces.md and located on the printed folios of
    tmp/sources/reid-chapters-algebraic-surfaces.pdf with pdftotext as a page
    locator: p. 92 carries "4.15. Contractibility of a rational bunch of curves",
    p. 93 opens with the running head "4.16. Proof of Theorem" and carries the
    Contraction Theorem statement, p. 94 opens 4.17 and its Theorem (Artin),
    p. 95 carries "Proof of Theorem 4.17, (1)" and then the heading of 4.18, so
    the proof of (1) is wholly there and ends with no Q.E.D., p. 96 opens
    "If V itself is a normal variety", carries the unnamed Theorem of 4.18 with
    its proof, and then begins "Proof of Theorem 4.17, (2)", and p. 97 carries
    that proof's Q.E.D. and the heading of 4.19. The remark and the two earlier
    events are corrected to the same facts.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Pages of Theorem 4.17 again, on a second reader's report of issue #121. The
    event above said the proof of part (1) runs on printed pp. 95--96 with its
    Q.E.D. on p. 96. It lies wholly on printed p. 95: "Proof of Theorem 4.17,
    (1)" begins there after the Q.E.D. that closes the lemma of 4.17, and it ends
    "so mult(P in X) = -Z^2 follows." with no Q.E.D., after which the heading
    "4.18. Graded rings over divisors" stands on the same page. The Q.E.D. on
    p. 96 that was read as part (1)'s closes the unnamed Theorem of 4.18, that
    the graded ring R(Z, L) of a numerically 1-connected divisor Z with
    h^1(O_Z) = 0 is generated in degree 1; it belongs to no lemma of 4.17. The
    proof of part (2) begins in the lower part of p. 96 and its Q.E.D. is on
    p. 97, where 4.19's heading follows. Every mention in this card's events and
    in its remark now gives pp. 95 and 96--97.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    One page fact of Reid's §4.17 and §4.18, on a third reader's report of issue
    #121, re-read here in tmp/sources/reid-chapters-algebraic-surfaces.md and on the printed folios
    of tmp/sources/reid-chapters-algebraic-surfaces.pdf. Printed p. 96 opens with
    the sentence "If V itself is a normal variety, this condition is called
    projective normality", which continues the paragraph of 4.18 begun on p. 95;
    the unnamed Theorem of 4.18 (R(Z, L) generated in degree 1) is stated and
    proved there, the proof ending "H^0(L^(x)(k-1)) into H^0(L^(x)k) onto H^0(O_A).
    Q.E.D."; after one paragraph on what that proof says, "Proof of Theorem 4.17,
    (2)" begins in the lower part of the same page, so the Q.E.D. on p. 96 closes
    the theorem of 4.18 and not, as the event above said, "the lemma preceding
    (2)". The lemma of 4.17 is on printed pp. 94--95 and its Q.E.D. closes on
    p. 95, before "Proof of Theorem 4.17, (1)". Nothing else in the citation
    changes: part (1) is proved on p. 95 and part (2) on pp. 96--97, its Q.E.D. on
    p. 97 above the heading of 4.19.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Citation repointed. The whole-paper MinerU extraction now stands beside the
    PDF under the PDF's own stem, tmp/sources/reid-chapters-algebraic-surfaces.md,
    and every reference in this card's events and remark now names that file.
    The earlier events were written against the byte-identical copy
    tmp/sources/reid-chapters.md (md5 78b2b6692c5b9d22c6ab793b0fe5132d for both),
    which is the name those readings were taken under; no reading changed.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Corrected two citations of Reid on 2026-11-16. The event of 2026-11-15 above
    and the remark both named tmp/sources/hartshorne-solutions-park.md as the
    text version of Reid's Chapters on Algebraic Surfaces; that is Jinhyun
    Park's set, and the match came from the words "Park City" in the Reid
    citation. Reid's text version is
    tmp/sources/reid-chapters-algebraic-surfaces.md, beside its PDF
    tmp/sources/reid-chapters-algebraic-surfaces.pdf, and both places now name
    it. No mathematical claim changes: Theorem A.7(1) is still on printed p. 29
    with its proof on pp. 30--31.
---

::: {.problem}
Let $f: X \rightarrow X^{\prime}$ be a birational morphism of nonsingular surfaces.

(a) If $Y \subseteq X$ is an irreducible curve such that $f(Y)$ is a point, then $Y \cong \PP^1$ and $Y^2<0$.

(b) Let $P^{\prime} \in X^{\prime}$ be a fundamental point of $f^{-1}$, and let $Y_1, \ldots, Y_r$ be the irreducible components of $f^{-1}\left(P^{\prime}\right)$.
Show that the matrix $\entrymatrix{Y_i . Y_j}$ is negative definite.
:::

::: {.solution}
We use the standing hypotheses of the surfaces chapter, so $X$ and $X'$
are nonsingular projective surfaces.

::: pf

::: {.pf-step #factorization-into-blowups}
The birational morphism $f$ factors as a finite sequence of point
blowups:
$$
X=X_n
\xrightarrow{\pi_n}
X_{n-1}
\longrightarrow
\cdots
\longrightarrow
X_1
\xrightarrow{\pi_1}
X_0=X',
$$
where each
$$
\pi_j:X_j\longrightarrow X_{j-1}
$$
is the blowup of a point and has exceptional curve
$$
E_j\cong\PP^1.
$$

::: pf-proof
This is the factorization theorem for birational morphisms of nonsingular
projective surfaces [[T-SRFZMT]]. Each elementary factor is a monoidal
transformation at a point.
:::

:::

::: {.pf-step #contracted-curve-is-p1}
Every irreducible curve $Y\subseteq X$ contracted by $f$ is the final
strict transform of one of the exceptional curves $E_j$. In particular,
$$
\boxed{Y\cong\PP^1.}
$$

::: pf-proof
For
$$
0\le i\le n,
$$
let $Y_i\subseteq X_i$ be the image of $Y$ under
$$
X=X_n\longrightarrow X_i.
$$
We have $Y_n=Y$, while
$$
Y_0=f(Y)
$$
is a point. Choose the least index $j\ge1$ for which $Y_j$ is a curve.
Then $Y_{j-1}$ is a point and
$$
\pi_j(Y_j)=Y_{j-1}.
$$
The only irreducible curve contracted by the blowup morphism $\pi_j$ is its
exceptional curve, so
$$
Y_j=E_j.
$$

For every $i>j$, the morphism
$$
\pi_i:Y_i\longrightarrow Y_{i-1}
$$
does not contract $Y_i$, hence $Y_i$ is the strict transform of
$Y_{i-1}$. Blowing up a nonsingular surface at a point preserves a
nonsingular curve under strict transform: if the centre lies on the curve,
the restriction of the blowup to its strict transform is the blowup of a
nonsingular curve at a Cartier divisor, hence an isomorphism; if the centre
does not lie on it, nothing changes.

Starting from
$$
E_j\cong\PP^1
$$
therefore gives
$$
Y=Y_n\cong\PP^1.
$$
:::

:::

::: {.pf-step #exceptional-classes-independent}
The numerical classes of all irreducible curves contracted by $f$ are
linearly independent in
$$
\operatorname{NS}(X)_\RR.
$$

::: pf-proof
At the $j$th blowup, the standard blowup decomposition gives
$$
\operatorname{NS}(X_j)_\RR
=
\pi_j^*\operatorname{NS}(X_{j-1})_\RR
\oplus
\RR[E_j],
$$
with
$$
E_j^2=-1
$$
and $E_j$ orthogonal to the pullback summand [[FE-SRFBLOW]].

Pull $[E_j]$ back through the later blowups by total transform and denote
its final class on $X$ by
$$
e_j.
$$
Iterating the displayed direct-sum decomposition shows that
$$
e_1,\ldots,e_n
$$
are linearly independent.

Let $\overline E_j\subseteq X$ be the final strict transform of $E_j$.
At any later blowup, a strict-transform class is either unchanged under
pullback or is the pullback minus the new exceptional class. Consequently
$$
[\overline E_j]
=
e_j+\sum_{\ell>j}a_{j\ell}e_\ell
$$
for some integers $a_{j\ell}$. Thus the change-of-basis matrix from the
$e_j$ to the $[\overline E_j]$ is triangular with every diagonal entry
equal to $1$. Hence
$$
[\overline E_1],\ldots,[\overline E_n]
$$
are linearly independent.

By step [](#contracted-curve-is-p1){.pf-ref}, every irreducible curve contracted by $f$ is one of the
$\overline E_j$. Any subset of these classes is therefore linearly
independent.
:::

:::

::: {.pf-step #pullback-square-and-orthogonal}
Let $H$ be a very ample divisor on $X'$ and put
$$
D=f^*H.
$$
Then
$$
\boxed{
D^2=H^2>0,
\qquad
D\cdot C=0
}
$$
for every curve $C$ contracted by $f$.

::: pf-proof
Because $f$ is birational of degree one, the projection formula for
intersection products gives
$$
(f^*H)^2=H^2.
$$
Very ampleness implies
$$
H^2>0.
$$

If $C$ is contracted, then $f_*C=0$ as a one-cycle. Hence the projection
formula gives
$$
D\cdot C
=
f^*H\cdot C
=
H\cdot f_*C
=0.
$$

Notice that $D$ is generally not ample: this zero intersection with the
exceptional curves is exactly why the retained source's statement
"pullback of ample is ample" cannot be used.
:::

:::

::: {.pf-step #hodge-index-negative-definite-complement}
The intersection form is negative definite on the orthogonal
complement
$$
D^\perp
\subseteq
\operatorname{NS}(X)_\RR.
$$

::: pf-proof
The Hodge index theorem says that the intersection form on
$$
\operatorname{NS}(X)_\RR
$$
has signature
$$
(1,\rho(X)-1)
$$
[[T-SRFHODGE]].

Step [](#pullback-square-and-orthogonal){.pf-ref} gives $D^2>0$. In a real vector space with a symmetric form of
signature $(1,\rho-1)$, the orthogonal complement of any positive-square
vector is negative definite: the positive index is already exhausted by
the line $\RR D$. Therefore every nonzero
$$
\alpha\in D^\perp
$$
satisfies
$$
\alpha^2<0.
$$
:::

:::

::: {.pf-step #contracted-curve-negative-square}
If $Y\subseteq X$ is an irreducible curve contracted by $f$, then
$$
\boxed{Y^2<0.}
$$

::: pf-proof
By step [](#pullback-square-and-orthogonal){.pf-ref},
$$
D\cdot Y=0,
$$
so
$$
[Y]\in D^\perp.
$$
The numerical class $[Y]$ is nonzero: if $A$ is any ample divisor on $X$,
then
$$
A\cdot Y>0.
$$
Step [](#hodge-index-negative-definite-complement){.pf-ref} therefore gives
$$
Y^2<0.
$$
Together with step [](#contracted-curve-is-p1){.pf-ref} this proves part (a).

The negative self-intersection is Theorem A.7(1) of M. Reid, *Chapters on Algebraic Surfaces*, text version `tmp/sources/reid-chapters-algebraic-surfaces.md`, arXiv:alg-geom/9602006v1, whose statement is on printed p. 29 and whose proof is on printed pp. 30--31, taken with $k=1$: a curve contracted to a point by a projective birational morphism of a nonsingular surface has negative self-intersection, with no hypothesis on the image surface. Applied to the whole bunch of components of a contracted fibre it gives negative definiteness of that matrix, and a principal submatrix of a negative definite matrix is negative definite, so a curve $Y$ among several components of a fibre has $Y^2<0$ as well; that is what part (a)'s inequality rests on when $f$ contracts more than $Y$. Reid's route to $Y\cong\PP^1$ is his Castelnuovo criterion, printed p. 10, which is the equivalence "$C$ is contracted to a point of a nonsingular surface with the morphism an isomorphism outside $C$ if and only if $C\cong\PP^1$ and $C^2=-1$", so that half of (a) is his when $f$ contracts the single curve $Y$; the half needed here, for a curve inside a larger exceptional locus, is step [](#contracted-curve-is-p1){.pf-ref} above.
:::

:::

::: {.pf-step #fibre-classes-negative-square}
For the components
$$
Y_1,\ldots,Y_r
$$
of the fibre over the fundamental point $P'$, every nonzero real vector
$(a_1,\ldots,a_r)$ satisfies
$$
\boxed{
\left(\sum_{i=1}^r a_iY_i\right)^2<0.}
$$

::: pf-proof
Each $Y_i$ is contracted by $f$, so step [](#pullback-square-and-orthogonal){.pf-ref} gives
$$
D\cdot Y_i=0.
$$
Hence
$$
Z=\sum_{i=1}^r a_iY_i
$$
lies in $D^\perp$.

If the coefficient vector is nonzero, step [](#exceptional-classes-independent){.pf-ref} says that the numerical
classes $[Y_i]$ are linearly independent. Thus
$$
[Z]\ne0
$$
in $\operatorname{NS}(X)_\RR$. Step [](#hodge-index-negative-definite-complement){.pf-ref} now gives
$$
Z^2<0.
$$
:::

:::

::: {.pf-step #intersection-matrix-negative-definite}
The intersection matrix
$$
\boxed{
\bigl(Y_i\cdot Y_j\bigr)_{1\le i,j\le r}
\text{ is negative definite}.}
$$

::: pf-proof
Let
$$
A=(Y_i\cdot Y_j)_{i,j}.
$$
For a column vector
$$
a=(a_1,\ldots,a_r)^T\in\RR^r,
$$
bilinearity of the intersection product gives
$$
a^TAa
=
\left(\sum_{i=1}^r a_iY_i\right)^2.
$$
By step [](#fibre-classes-negative-square){.pf-ref} this quantity is strictly negative for every nonzero $a$.
This is exactly negative definiteness of $A$, proving part (b).

Part (b) is also Theorem A.7(1) of M. Reid, *Chapters on Algebraic Surfaces*, text version `tmp/sources/reid-chapters-algebraic-surfaces.md`, arXiv:alg-geom/9602006v1, statement on printed p. 29, in greater generality: there $f:Y\to X$ is any projective birational morphism of a nonsingular surface, $X$ is an arbitrary surface, and the intersection matrix of any bunch of curves contracted to points is negative definite. His proof occupies printed pp. 30--31 and is stated there for a bunch with connected union contracted to a single point with the morphism an isomorphism outside it ("for simplicity", printed p. 30); the argument above is the Hodge-index route he records as the alternative in Ex. A.16 and carries no such restriction.
:::

:::

::: pf-qed
Steps [](#factorization-into-blowups){.pf-ref}, [](#contracted-curve-is-p1){.pf-ref} and [](#exceptional-classes-independent){.pf-ref} identify contracted irreducible curves as independent
strict transforms of exceptional $\PP^1$'s. Steps [](#pullback-square-and-orthogonal){.pf-ref}, [](#hodge-index-negative-definite-complement){.pf-ref} and [](#contracted-curve-negative-square){.pf-ref} combine the
positive-square pullback of a very ample divisor with Hodge index to prove
part (a). Steps [](#fibre-classes-negative-square){.pf-ref} and [](#intersection-matrix-negative-definite){.pf-ref} apply the same negative-definite orthogonal
complement to the whole exceptional fibre and prove part (b).
:::

:::
:::

::: {.remark title="Published solution"}
M. Reid, *Chapters on Algebraic Surfaces*, arXiv:alg-geom/9602006v1 (6 February 1996), a draft of the notes submitted to the 1993 volume of the IAS/AMS Park City lecture notes series, read in `tmp/sources/reid-chapters-algebraic-surfaces.pdf` and in its MinerU text version `tmp/sources/reid-chapters-algebraic-surfaces.md`, whose "Status of this draft" is printed p. 2, text version `tmp/sources/reid-chapters-algebraic-surfaces.md`, Theorem A.7(1), statement on printed p. 29 and proof on printed pp. 30--31, states part (b) as a theorem --- the intersection matrix of a bunch of curves contracted to points by a projective birational morphism of a nonsingular surface is negative definite --- and proves it; with $k=1$ it gives $Y^2<0$ in part (a), and by restriction to a principal submatrix the same for a curve among several components of a fibre, and his Castelnuovo criterion, printed p. 10, gives $Y\cong\PP^1$ with $Y^2=-1$ when the contraction has no other exceptional curve. The identity of the image point as a nonsingular one, which is what turns $Y^2<0$ into $Y^2=-1$ there, is his Contraction Theorem (Artin), the theorem of Section 4.15, stated on printed p. 93 and proved in Section 4.16, together with his Theorem (Artin) of Section 4.17, whose statement begins on printed p. 94 and whose proof of part (1) lies wholly on printed p. 95, part (2)'s proof running on pp. 96--97. The steps above are not a transcription of Reid: they reach both parts through the factorization into point blowups and Hodge index, the second of which he records as Ex. A.16, and they cover a contracted curve inside a larger exceptional locus, which his criterion does not.
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, V.5.4, printed p. 298, is a corollary of the Hodge index theorem for contracted curves; its part (a) proves only $Y^2\le0$, from the false statement that the pullback of an ample divisor is ample, and says nothing about $Y\cong\PP^1$.
:::
