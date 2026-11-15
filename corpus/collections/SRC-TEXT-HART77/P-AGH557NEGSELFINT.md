---
schema: qual/card@1
id: P-AGH557NEGSELFINT
kind: problem
title: A curve contracted to a point on a projective surface has negative self-intersection
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
  date: 2026-09-20
  note: >-
    Read Hartshorne V.5.7 as transcribed here, the retained Andrew Egbert
    note, the completed V.5.4 contraction argument, and the Hodge index
    theorem. The retained note says simply that V.5.4 applies. As literally
    transcribed, however, the statement omits the hypothesis that f has
    two-dimensional image: C x P^1 -> C followed by an embedding of C into
    a projective surface has a fibre Y with Y^2=0. The intended contraction
    statement is correct once dim f(X)=2 (in particular for a birational
    contraction). The proof below records this erratum and proves the
    corrected statement using D=f^*H: D^2=deg(f)H^2>0, D.Y=0, and the
    signature form of Hodge index.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the literal statement, counterexample, corrected hypothesis, and
    Hodge-index proof. Checked that the one-dimensional-image counterexample
    has f^{-1}(P)=Y and Y^2=0. Under dim f(X)=2, properness makes f
    surjective onto the irreducible surface X_0 and therefore generically
    finite, so (f^*H)^2=deg(f)H^2>0. The hyperplane H_1 avoiding P gives
    f^*H.Y=0, an ample divisor on X shows [Y] is numerically nonzero, and
    the signature form of Hodge index gives Y^2<0. Also checked that the
    H_0 decomposition in the printed hint has only Y over P because
    f^{-1}(P)=Y.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'As printed the statement fails: X = C x P^1 mapped to an embedded C in a projective surface has f^-1(P) equal to a ruling fibre Y with Y^2 = 0. The card keeps the printed statement and proves it under the dominance hypothesis, naming that counterexample in the solution.'
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Published solution located for issue #121: M. Reid, Chapters on Algebraic
    Surfaces, arXiv:alg-geom/9602006v1, Appendix A.7, Theorem (Negativity of
    exceptional locus) part (1), statement on printed p. 29 and proof on printed
    pp. 30--31. With the bunch a single curve it is Y^2 < 0, which is the
    corrected statement of this card. Read in tmp/sources/reid-chapters-algebraic-surfaces.md and
    checked on printed pp. 29--31 of
    tmp/sources/reid-chapters-algebraic-surfaces.pdf (folios = PDF pages). The
    exercise as printed gives f : X -> X_0 with X_0 only a projective variety of
    dimension 2, so Reid's "projective birational morphism" is not literally a
    hypothesis of it; it follows from the printed f^-1(P) = Y once f is
    dominant, by the Stein factorisation argument now in the remark: the fibre
    over P is Y together with one further point per point of the finite part, so
    it is Y alone only for a degree-one, i.e. birational, f. The remark records
    that, and records that Egbert's p. 300 entry is a cross-reference and that
    the NTU set's Exercise 7 (printed p. 21) ends by concluding Y^2 = 0, which
    does not follow from its own inequality.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Correction, on a reader's report of issue #121: the argument the event
    above attributes to the Stein factorization is false. A connected fibre
    f^-1(P) = Y forces #g^-1(P) = 1, not deg g = 1, and hence says nothing
    about deg f; the counterexample is now in the remark, sigma(x:y:z) =
    (-x:-y:z) on P^2 with f: Bl_O P^2 -> P^2 -> P^2/sigma, where the fibre
    over the image of O is exactly the exceptional curve E while deg f = 2.
    What the remark now argues instead is that Reid's Theorem A.7(1) applies
    to the Stein factor h: X -> X', which is a projective birational morphism
    of the nonsingular X contracting Y to a point: h contracts Y because a
    curve image would be contracted by the finite g to a point, and h is
    birational because h_*O_X = O_X' has rank one at the generic point. So
    Y^2 < 0 follows with no claim on the degree, and Reid's theorem is the
    published proof; the card's statement that the exercise needs f dominant
    is unchanged, and so are the Hodge-index steps.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Corrections on a reader's report of issue #121, in the remark and the
    solution body. The counterexample's sigma was described as having only the
    fixed point O = (0:0:1); its fixed locus is O together with the line z = 0,
    which it fixes pointwise, and what the counterexample uses is that O is
    fixed, so that the fibre over the image of O is the single point O, while
    sigma is not the identity. The opening called Reid's Theorem A.7(1) a
    published proof of the corrected statement, which overclaims: Reid proves it
    for a projective birational morphism, and the passage from the exercise's
    dominant generically finite f to its Stein factor is the card's own
    argument. The remark and the solution body now say which part is published.
    The sentence replacing X' by its normalization is gone: X' is normal
    already, since h dominant and X normal make the normalization of X' factor
    h, and h_*O_X = O_X' then forces that normalization to be an isomorphism,
    which the remark now proves. Checked in tmp/sources/reid-chapters-algebraic-surfaces.md and on
    printed pp. 29--31 of tmp/sources/reid-chapters-algebraic-surfaces.pdf; the
    Hodge-index proof and the Steiner pass are unchanged.
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
---

::: {.problem}
Let $Y$ be an irreducible curve on a surface $X$, and suppose there is a morphism $f: X \rightarrow X_0$ to a projective variety $X_0$ of dimension 2, such that $f(Y)$ is a point $P$ and $f^{-1}(P)=Y$.
Then show that $Y^2<0$.

Hint: Let $\linearsystem{H}$ be a very ample (Cartier) divisor class on $X_0$, let $H_0 \in\linearsystem{H}$ be a divisor containing $P$, and let $H_1 \in\linearsystem{H}$ be a divisor not containing $P$.
Then consider $f^* H_0, f^* H_1$ and $\tilde{H}_0=f^*\left(H_0-P\right)^{-}$.
:::

::: {.solution}
As printed, the statement is false. Take a curve $C$ embedded in a projective
surface $X_0$, the product $X=C\times\PP^1$, the morphism
$f:X\to C\hookrightarrow X_0$, and the fibre $Y=\{c\}\times\PP^1$ of the ruling.
Then $f(Y)$ is the point $P$ which is the image of $c$, the set-theoretic fibre
$f^{-1}(P)$ is exactly $Y$, and $Y^2=0$ as the fibre class of a product of
curves. So the exercise needs the hypothesis that $f$ be dominant, equivalently
that $\dim f(X)=2$; it holds automatically when $f$ is surjective, and in the
contraction setting where the exercise is used. Under that hypothesis the
following argument proves $Y^2<0$. The published proof of the birational case is M. Reid's Theorem
A.7(1), *Chapters on Algebraic Surfaces*, arXiv:alg-geom/9602006v1, statement on
printed p. 29 and proof on printed pp. 30--31, applied to the single curve $Y$;
the passage from the exercise's $f$ to Reid's birational hypothesis is the
Stein-factorization step of the closing remark, which is the card's own and not
Reid's, the steps below are the card's Hodge-index route to the same inequality,
and the remark records why Reid's hypotheses hold for that factor, what the
other two sets do, and the counterexample to the degree-one inference an
earlier version of it made.

::: pf

::: {.pf-step #generically-finite}
$f$ is dominant and generically finite.

::: pf-proof
Dominance is the hypothesis added at the start of the solution. Since
$\dim X=\dim X_0=2$ and the target is integral, the generic fibre is finite.
:::

:::

::: {.pf-step #pullback-square-positive}
Let $H$ be a very ample Cartier divisor on $X_0$ and put
$$
D=f^*H.
$$
Then
$$
\boxed{D^2>0.}
$$

::: pf-proof
By step [](#generically-finite){.pf-ref}, $f$ has a positive degree
$$
d=[K(X):K(X_0)]>0.
$$
The projection formula for intersection products gives
$$
D^2
=(f^*H)^2
=d\,H^2.
$$
Very ampleness of $H$ gives
$$
H^2>0,
$$
so
$$
D^2>0.
$$
:::

:::

::: {.pf-step #pullback-meets-y-zero}
One has
$$
\boxed{D\cdot Y=0.}
$$

::: pf-proof
Choose
$$
H_1\in\linearsystem{H}
$$
with
$$
P\notin H_1,
$$
as in the hint. Since
$$
f(Y)=P,
$$
the divisor
$$
f^*H_1
$$
is disjoint from $Y$. Therefore
$$
f^*H_1\cdot Y=0.
$$
Because
$$
f^*H_1\sim f^*H=D,
$$
intersection depends only on numerical equivalence, and hence
$$
D\cdot Y=0.
$$
Equivalently, the projection formula gives
$$
f^*H\cdot Y=H\cdot f_*Y=0
$$
because $Y$ is contracted to a point.
:::

:::

::: {.pf-step #y-class-nonzero}
The numerical class
$$
[Y]\in\operatorname{NS}(X)_\RR
$$
is nonzero.

::: pf-proof
Let $A$ be any ample divisor on the nonsingular projective surface $X$.
Since $Y$ is an irreducible curve,
$$
A\cdot Y>0.
$$
Thus $Y$ cannot be numerically equivalent to zero.
:::

:::

::: {.pf-step #orthogonal-complement-negative-definite}
The intersection form is negative definite on
$$
D^\perp
=
\left\{
\alpha\in\operatorname{NS}(X)_\RR:
\alpha\cdot D=0
\right\}.
$$

::: pf-proof
The Hodge index theorem [[T-SRFHODGE]] says that the intersection form on
$$
\operatorname{NS}(X)_\RR
$$
has signature
$$
(1,\rho(X)-1).
$$
Step [](#pullback-square-positive){.pf-ref} gives
$$
D^2>0.
$$
Hence the line
$$
\RR D
$$
already supplies the unique positive direction, so its orthogonal
complement $D^\perp$ is negative definite. Therefore every nonzero
$$
\alpha\in D^\perp
$$
satisfies
$$
\alpha^2<0.
$$
:::

:::

::: {.pf-step #y-negative-square}
The contracted curve satisfies
$$
\boxed{Y^2<0.}
$$

::: pf-proof
By step [](#pullback-meets-y-zero){.pf-ref},
$$
[Y]\in D^\perp.
$$
By step [](#y-class-nonzero){.pf-ref} this class is nonzero. Step [](#orthogonal-complement-negative-definite){.pf-ref} therefore gives
$$
Y^2<0.
$$
:::

:::

::: {.pf-step #hint-divisors-reconciled}
The divisors appearing in the printed hint are compatible with the
same calculation.

::: pf-proof
Choose
$$
H_0\in\linearsystem{H},
\qquad
P\in H_0,
$$
and let $\widetilde H_0$ denote the closure of the pullback away from the
contracted point, as in the hint. Since
$$
f^{-1}(P)=Y,
$$
the pullback has the form
$$
f^*H_0=\widetilde H_0+mY
$$
for some integer
$$
m>0.
$$
Intersecting with $Y$ and using step [](#pullback-meets-y-zero){.pf-ref} gives
$$
0
=
f^*H_0\cdot Y
=
\widetilde H_0\cdot Y+mY^2.
$$
Step [](#y-negative-square){.pf-ref} says $Y^2<0$, so necessarily
$$
\widetilde H_0\cdot Y=-mY^2>0.
$$
Thus the two hyperplanes in the hint encode the same geometry: the
hyperplane avoiding $P$ gives zero intersection with $Y$, while a
hyperplane through $P$ acquires the exceptional component $mY$.
:::

:::

::: pf-qed
Steps [](#pullback-square-positive){.pf-ref}, [](#pullback-meets-y-zero){.pf-ref}, [](#y-class-nonzero){.pf-ref} and [](#orthogonal-complement-negative-definite){.pf-ref}
place the nonzero class of $Y$ in the negative-definite orthogonal
complement of the positive-square divisor $f^*H$. Step [](#y-negative-square){.pf-ref} gives
$Y^2<0$, and step [](#hint-divisors-reconciled){.pf-ref} reconciles the proof with the printed hint.
:::

:::
:::

::: {.remark title="Published solution"}
M. Reid, *Chapters on Algebraic Surfaces*, arXiv:alg-geom/9602006v1 (6 February 1996), a draft of the notes submitted to the 1993 volume of the IAS/AMS Park City lecture notes series, Appendix A.7, Theorem (Negativity of exceptional locus), part (1), statement on printed p. 29 and proof on printed pp. 30--31, proves the corrected statement for the projective birational morphisms it assumes, not for the morphism the exercise prints: the step from the exercise's $f$ to Reid's hypothesis is the Stein-factorization argument made below, and that step is this card's own and is not in Reid. Reid says that for a bunch of curves on a nonsingular surface contracted to points by a projective birational morphism to a surface, the matrix $(\Gamma_i\Gamma_j)$ is negative definite; with the bunch a single curve $Y$ that is $Y^2<0$, negative definiteness of a $1\times1$ matrix being its negativity. Under the hypothesis added above, $f$ is dominant and generically finite, so it has a Stein factorization $f=g\circ h$: a projective morphism $h:X\to X'$ with connected fibres, where $X'=\Spec_{X_0}(f_*\OO_X)$ and $h_*\OO_X=\OO_{X'}$, followed by a finite morphism $g:X'\to X_0$. Then $h$ is a projective birational morphism of the nonsingular surface $X$ which contracts $Y$ to a point, so Reid's theorem applies to the single curve $Y$ and gives $Y^2<0$. Two points are needed for that. First, $h(Y)$ is a point: $h(Y)$ is the image of an irreducible curve, so it is a point or a curve, and if it were a curve $C$ then $C$ would lie in the fibre $g^{-1}(P)$, which is finite. Second, $h$ is birational: its degree is the rank of $h_*\OO_X$ at the generic point of $X'$, and $h_*\OO_X=\OO_{X'}$ has rank one, so $[K(X):K(X')]=1$. $X'$ is already normal and there is no normalization to take: $h$ is dominant and $X$ is normal, so $h$ factors through the normalization $\nu:\widetilde X'\to X'$ of the target as $h=\nu\circ h_1$, and then
$$
h_*\OO_X
=
\nu_*\bigl((h_1)_*\OO_X\bigr)
\supseteq
\nu_*\OO_{\widetilde X'}
\supseteq
\OO_{X'}.
$$
Since $h_*\OO_X=\OO_{X'}$ both inclusions are equalities, $\nu_*\OO_{\widetilde X'}=\OO_{X'}$, and a finite dominant $\nu$ with that property is an isomorphism. The target is thus normal, which is the setting Reid's proof works in. Nothing here needs $\deg f$ to be one, and it need not be. What the fibre condition $f^{-1}(P)=Y$ gives is $\#g^{-1}(P)=1$ --- $g^{-1}(P)$ contains $h(Y)$, and a second point $Q$ of it would put the whole nonempty fibre $h^{-1}(Q)$ into $f^{-1}(P)$ --- and one point over one point of the target of a finite morphism says nothing about its degree. An earlier version of this remark read $\#g^{-1}(P)=1$ as $\deg g=1$ and with it $\deg f=1$; that inference is false, and here is a counterexample to it. Let $\sigma:\PP^2\to\PP^2$ be $\sigma(x:y:z)=(-x:-y:z)$ over a field of characteristic $\ne2$. Its fixed locus is not the single point $O$: it is $O=(0:0:1)$, which is an isolated fixed point, together with the whole line $z=0$, which $\sigma$ fixes pointwise, since $(-x:-y:0)=(x:y:0)$ in $\PP^2$; for $z\ne0$ the equations $-x=\lambda x$, $-y=\lambda y$, $z=\lambda z$ force $\lambda=1$ and then $x=y=0$. What the counterexample uses is that $O$ is a fixed point, so that its orbit is $\{O\}$ and the fibre of $\PP^2\to\PP^2/\sigma$ over the image of $O$ is the single point $O$, and that $\sigma$ is not the identity, so that the quotient map is generically two-to-one. Let $X=\Bl_O\PP^2$ with exceptional curve $E$, and let $f$ be $X\to\PP^2\to\PP^2/\sigma$. Then $f^{-1}(P)=E$ exactly, while $\deg f=2$ and $f$ is not birational. Reid's theorem applied to the Stein factor of that $f$, which is $X\to\PP^2$, still gives $E^2=-1<0$. Read in `tmp/sources/reid-chapters-algebraic-surfaces.md` (the whole paper) and checked on printed pp. 29--31 of `tmp/sources/reid-chapters-algebraic-surfaces.pdf`, whose folios are its PDF pages. His proof is written, "for simplicity", for a bunch with connected union contracted to a single point with the morphism an isomorphism outside it (printed p. 30); the steps above reach the same conclusion by Hodge index and need neither the connectedness nor the single-point hypothesis.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.5.7, printed p. 300, has one sentence: the answer follows from V.5.4 since $X$ is assumed nonsingular and $X_0$ need not be. That is a cross-reference to a defective entry, not a proof. *Algebraic Geometry II*, National Taiwan University, 2020 Spring, Chapter V homework, Exercise 7, printed p. 21, aims at the same estimate but ends "$0=\dots\ge mY^2\Rightarrow Y^2=0$", which does not follow and is false for a contracted curve; nothing in it is used here.
:::
